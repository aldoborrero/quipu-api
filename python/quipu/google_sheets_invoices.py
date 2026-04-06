"""Export Quipu invoices (income & expenses) to a formatted Google Sheets spreadsheet.

Usage:
    python -m quipu.google_sheets_invoices [--year 2025] [--spreadsheet-id ID] [--credentials path/to/sa.json]

Requires: gspread, gspread_formatting
"""

from __future__ import annotations

import argparse
import datetime
import time
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from typing import Any

# Monetary constants. Use Decimal for all internal arithmetic to avoid the
# accumulation and rounding errors of IEEE 754 floats — these values end up on
# real tax forms and a cent of drift is not acceptable.
ZERO: Decimal = Decimal("0")
HUNDRED: Decimal = Decimal("100")
CENT: Decimal = Decimal("0.01")


def _money_round(value: Decimal) -> Decimal:
    """Round a Decimal to 2 decimal places, half-up (banker's rounding is not
    what Spanish tax forms use)."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)

import gspread
from gspread_formatting import (
    CellFormat,
    Color,
    NumberFormat,
    format_cell_ranges,
)

from quipu import create_client
from quipu_client.api.invoices import get_invoices
from quipu_client.client import Client
from quipu_client.models.get_invoices_filterkind import GetInvoicesFilterkind
from quipu_client.models.get_invoices_include import GetInvoicesInclude
from quipu_client.types import Unset

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SHEET_TYPE_INCOME: str = "income"
SHEET_TYPE_EXPENSES: str = "expenses"

# Quarter colors for row highlighting on the income master sheet (Q1 stays the
# default white and is skipped at write time, so it's omitted here).
QUARTER_COLORS: dict[int, Color] = {
    2: Color(1, 0.976, 0.769),      # Q2: #fff9c4 yellow
    3: Color(0.910, 0.961, 0.914),  # Q3: #e8f5e9 green
    4: Color(0.890, 0.949, 0.992),  # Q4: #e3f2fd blue
}

CONCEPT_WIDTH_PX: int = 300
SPREADSHEET_LOCALE: str = "es_ES"

# Formatting patterns (cell-level, in addition to native table column types)
DATE_PATTERN: str = "dd/MM/yyyy"
PERCENT_PATTERN: str = "0%"

DATE_FMT = CellFormat(
    numberFormat=NumberFormat(type="DATE", pattern=DATE_PATTERN),
    horizontalAlignment="LEFT",
)
PERCENT_FMT = CellFormat(
    numberFormat=NumberFormat(type="PERCENT", pattern=PERCENT_PATTERN),
    horizontalAlignment="RIGHT",
)
WRAP_FMT = CellFormat(wrapStrategy="WRAP")


@dataclass(frozen=True)
class SheetSpec:
    """Per-sheet-type configuration: column layout, types, and formatting."""

    headers: list[str]
    column_types: list[str]
    date_cols: list[str]
    percent_col: str
    wrap_col: str | None = None              # column letter for wrap (income's Concept)
    fixed_width_col_idx: int | None = None   # 0-based column index for fixed-width override

    @property
    def num_cols(self) -> int:
        return len(self.headers)


SHEET_SPECS: dict[str, SheetSpec] = {
    SHEET_TYPE_INCOME: SheetSpec(
        headers=[
            "Fecha de emisión", "Vencimiento", "Fecha de pago", "Número",
            "Número de Factura", "Tipo de operación", "Cliente", "Cuenta de cliente",
            "NIF", "Código postal", "Concepto", "Estado", "Rectificativa?",
            "Base", "IVA", "IVA (%)", "Recargo de equivalencia",
        ],
        column_types=[
            "DATE", "DATE", "DATE",                                              # A-C
            "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT",  # D-L
            "BOOLEAN",                                                           # M: Rectificativa?
            "CURRENCY", "CURRENCY",                                              # N-O: Base, IVA
            "PERCENT",                                                           # P: IVA (%)
            "CURRENCY",                                                          # Q: Recargo
        ],
        date_cols=["A", "B", "C"],
        percent_col="P",                  # IVA %
        wrap_col="K",                     # Concepto
        fixed_width_col_idx=10,           # K, 0-based
    ),
    SHEET_TYPE_EXPENSES: SheetSpec(
        headers=[
            "Fecha de emisión", "Número de Factura", "Proveedor",
            "Cuenta de Proveedor", "NIF", "Base", "IVA", "IVA (%)", "Total",
        ],
        column_types=[
            "DATE",                                            # A
            "TEXT", "TEXT", "TEXT", "TEXT",                    # B-E
            "CURRENCY", "CURRENCY",                            # F-G: Base, IVA
            "PERCENT",                                         # H: IVA (%)
            "CURRENCY",                                        # I: Total
        ],
        date_cols=["A"],
        percent_col="H",                  # IVA %
    ),
}


# Payment status API values to Spanish display labels
PAYMENT_STATUS_LABELS: dict[str, str] = {
    "paid": "Pagado",
    "due": "Pendiente de cobro",
    "pending": "Pendiente",
    "unpaid": "Impagado",
}

NUM_QUARTERS: int = 4
FIRST_DATA_ROW: int = 2  # 1-indexed row where data starts (after header)
SHEETS_EPOCH: datetime.date = datetime.date(1899, 12, 30)  # Google Sheets serial date epoch

# ISO 3166-1 alpha-2 codes for EU member states (as of 2026). ES is the home
# country and is classified as "national" rather than "intra_eu".
EU_COUNTRY_CODES: frozenset[str] = frozenset({
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR",
    "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL",
    "PL", "PT", "RO", "SK", "SI", "SE",
})

# Operation classification used by Modelos 303, 349 and 390.
OP_NATIONAL: str = "national"       # ES (or unknown — treated as domestic by default)
OP_INTRA_EU: str = "intra_eu"       # EU member state other than ES
OP_EXPORT: str = "export"           # non-EU country

# Type alias for invoice record dicts
InvoiceRecord = dict[str, Any]


@dataclass
class LineItem:
    """Per-line-item data needed for tax form aggregations.

    Base is the line's pre-tax amount (unitary * qty - discount). VAT and
    retention amounts are the actual EUR values on that line. Deductible
    percentages default to 100 when Quipu doesn't set them. All monetary
    fields use Decimal for exact arithmetic.
    """

    description: str
    base: Decimal
    vat_percent: Decimal
    vat_amount: Decimal
    retention_amount: Decimal
    deductible_vat_percent: Decimal     # 0-100
    deductible_expense_percent: Decimal  # 0-100
    kind: str                            # "current" | "assets" | "reimbursement"
    surcharge_amount: Decimal            # equivalence surcharge (from additional_properties)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _val(attr: Any) -> Any:
    """Return None for Unset values, otherwise the value itself."""
    if isinstance(attr, Unset) or attr is None:
        return None
    return attr


def _to_decimal(s: Any) -> Decimal | None:
    """Convert a value to Decimal, returning None for Unset/None/invalid.

    Strings are passed directly to Decimal to avoid a lossy float intermediary
    (Quipu returns amounts as strings like "172.5"). Ints are accepted as-is.
    """
    if isinstance(s, Unset) or s is None or s == "":
        return None
    try:
        return Decimal(str(s))
    except (InvalidOperation, ValueError, TypeError):
        return None


def _date_serial(d: datetime.date | None) -> int | str:
    """Convert a date to a Google Sheets serial number, or empty string if None.

    Google Sheets epoch is 1899-12-30 (with the Lotus 1-2-3 leap year bug).
    """
    if d is None:
        return ""
    return (d - SHEETS_EPOCH).days


def _payment_status_label(status: Any) -> str:
    """Translate a payment status enum value to a Spanish display label."""
    if isinstance(status, Unset) or status is None:
        return ""
    return PAYMENT_STATUS_LABELS.get(str(status.value), str(status.value))


def _get_quarter(d: datetime.date) -> int:
    """Return the quarter (1-4) for a given date."""
    return (d.month - 1) // 3 + 1


def classify_operation(country_code: str | None) -> str:
    """Classify an invoice by counterparty country for tax form aggregation.

    Returns one of OP_NATIONAL, OP_INTRA_EU, OP_EXPORT. Missing or empty
    country codes are treated as national — the defensible default for Modelo
    303, where an unclassified operation should not be reported as intra-EU
    or export without explicit evidence.
    """
    if not country_code:
        return OP_NATIONAL
    code = country_code.upper()
    if code == "ES":
        return OP_NATIONAL
    if code in EU_COUNTRY_CODES:
        return OP_INTRA_EU
    return OP_EXPORT


def _col_letter(n: int) -> str:
    """Convert 1-based column number to letter (1=A, 26=Z, 27=AA)."""
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result


def _money(val: Decimal | float | None) -> float:
    """Convert a monetary value to float for writing into a Sheets cell.

    Sheets stores numbers as IEEE 754 anyway, so we round to cents first to
    keep the displayed value exact and only bridge to float at the boundary.
    Zero values are displayed as '-' via the cell number format pattern.
    """
    if val is None:
        return 0.0
    if isinstance(val, Decimal):
        return float(_money_round(val))
    return float(val)


# ---------------------------------------------------------------------------
# Fetch from Quipu API
# ---------------------------------------------------------------------------


def _attr(item_attrs: Any, additional: dict[str, Any], *names: str) -> Any:
    """Return the first non-empty value from item_attrs.<name> or additional[name]."""
    for name in names:
        raw = getattr(item_attrs, name, None)
        val = _val(raw) if raw is not None else additional.get(name)
        if val not in (None, ""):
            return val
    return None


def _extract_line_item(items_map: dict[str, Any], item_ref: Any) -> LineItem | None:
    """Build a LineItem from an included-item reference, or None if not resolvable."""
    # The item id lives in the reference's additional_properties (not as a typed attr).
    ref_additional: dict[str, Any] = getattr(item_ref, "additional_properties", {}) or {}
    item_id = ref_additional.get("id") or getattr(item_ref, "id", None)
    if item_id is None or str(item_id) not in items_map:
        return None

    item_attrs = getattr(items_map[str(item_id)], "attributes", None)
    if item_attrs is None:
        return None

    additional: dict[str, Any] = getattr(item_attrs, "additional_properties", {}) or {}

    description = str(_attr(item_attrs, additional, "concept", "description") or "")

    # Base: unitary * quantity minus discount (either absolute or percent).
    unitary = _to_decimal(_attr(item_attrs, additional, "unitary_amount")) or ZERO
    quantity = _to_decimal(_attr(item_attrs, additional, "quantity")) or ZERO
    discount_amount = _to_decimal(_attr(item_attrs, additional, "discount_amount")) or ZERO
    discount_pct = _to_decimal(_attr(item_attrs, additional, "discount_percent")) or ZERO
    gross_base = unitary * quantity
    if discount_amount:
        base = gross_base - discount_amount
    else:
        base = gross_base * (1 - discount_pct / HUNDRED)

    vat_percent = _to_decimal(_attr(item_attrs, additional, "vat_percent")) or ZERO
    vat_amount = _to_decimal(_attr(item_attrs, additional, "vat_amount")) or ZERO
    retention_amount = _to_decimal(_attr(item_attrs, additional, "retention_amount")) or ZERO

    # Deductibility defaults to 100% when unset (most line items are fully deductible).
    deductible_vat_pct = _to_decimal(_attr(item_attrs, additional, "deductible_vat_percent"))
    deductible_expense_pct = _to_decimal(_attr(item_attrs, additional, "deductible_expense_percent"))

    kind_raw = _attr(item_attrs, additional, "kind")
    kind = str(kind_raw.value if hasattr(kind_raw, "value") else kind_raw or "current")

    surcharge_raw = additional.get("equivalence_surcharge_amount") or additional.get("surcharge_amount")
    surcharge_amount = _to_decimal(surcharge_raw) or ZERO

    return LineItem(
        description=description,
        base=base,
        vat_percent=vat_percent,
        vat_amount=vat_amount,
        retention_amount=retention_amount,
        deductible_vat_percent=deductible_vat_pct if deductible_vat_pct is not None else HUNDRED,
        deductible_expense_percent=deductible_expense_pct if deductible_expense_pct is not None else HUNDRED,
        kind=kind,
        surcharge_amount=surcharge_amount,
    )


def _infer_vat_percent(
    item_vat_percents: list[Decimal],
    vat_amount: Decimal | None,
    base: Decimal | None,
) -> int:
    """Determine the VAT % from line items or by inference from amounts."""
    if item_vat_percents:
        return int(item_vat_percents[0])
    if vat_amount is None or vat_amount == 0:
        return 0
    if base and base != 0:
        try:
            return int((vat_amount / base * HUNDRED).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        except (ZeroDivisionError, InvalidOperation):
            return 0
    return 0


def _fetch_all_invoices(client: Client, kind: GetInvoicesFilterkind, year: int) -> list[InvoiceRecord]:
    """Fetch all invoices for a given kind/year with pagination, including line items."""
    all_invoices: list[InvoiceRecord] = []

    for quarter in range(1, NUM_QUARTERS + 1):
        period = f"{year}-Q{quarter}"
        page = 1

        while True:
            collection = get_invoices.sync(
                client=client,
                filterkind=kind,
                filterperiod=period,
                sort="issue_date",
                pagenumber=page,
                include=GetInvoicesInclude.ITEMS,
            )
            if collection is None or isinstance(collection.data, Unset) or not collection.data:
                break

            # Build a map of included items by id
            items_map: dict[str, Any] = {}
            if not isinstance(collection.included, Unset) and collection.included:
                for inc in collection.included:
                    inc_id = getattr(inc, "id", None)
                    if inc_id is not None:
                        items_map[str(inc_id)] = inc

            for inv in collection.data:
                if isinstance(inv.attributes, Unset):
                    continue
                attrs = inv.attributes

                rels = inv.relationships if not isinstance(inv.relationships, Unset) else None

                # Gather line items
                line_items: list[LineItem] = []
                if rels and not isinstance(rels.items, Unset) and rels.items:
                    items_data = _val(rels.items.data)
                    if items_data:
                        for item_ref in items_data:
                            li = _extract_line_item(items_map, item_ref)
                            if li is not None:
                                line_items.append(li)

                # Determine if this is an amending (rectificative) invoice
                is_amending = False
                if rels and not isinstance(rels.amended_invoice, Unset) and rels.amended_invoice:
                    if _val(rels.amended_invoice.data) is not None:
                        is_amending = True

                issue_date: datetime.date | None = _val(attrs.issue_date)
                due_dates: list[datetime.date] | None = _val(attrs.due_dates)
                due_date = due_dates[0] if due_dates else None
                paid_at: datetime.date | None = _val(attrs.paid_at)

                base = _to_decimal(attrs.total_amount_without_taxes)
                vat_amount = _to_decimal(attrs.vat_amount)
                total = _to_decimal(attrs.total_amount)
                retention_amount = _to_decimal(attrs.retention_amount) or ZERO

                item_vat_percents = [li.vat_percent for li in line_items if li.vat_percent]
                vat_pct_value = _infer_vat_percent(item_vat_percents, vat_amount, base)
                surcharge_total = sum((li.surcharge_amount for li in line_items), start=ZERO)
                concept = " | ".join(li.description for li in line_items if li.description)

                # For issued invoices: the recipient is the client
                # For received invoices: the issuer is the supplier
                if kind == GetInvoicesFilterkind.INCOME:
                    contact_name = _val(attrs.recipient_name) or ""
                    contact_tax_id = _val(attrs.recipient_tax_id) or ""
                    contact_zip = _val(attrs.recipient_zip_code) or ""
                    country_code = (_val(attrs.recipient_country_code) or "").upper()
                    contact_account = ""
                    if rels and not isinstance(rels.accounting_subcategory, Unset) and rels.accounting_subcategory:
                        sub_data = _val(rels.accounting_subcategory.data)
                        if sub_data and hasattr(sub_data, "id"):
                            contact_account = str(_val(sub_data.id) or "")
                else:
                    contact_name = _val(attrs.issuing_name) or ""
                    contact_tax_id = _val(attrs.issuing_tax_id) or ""
                    contact_zip = _val(attrs.issuing_zip_code) or ""
                    country_code = (_val(attrs.issuing_country_code) or "").upper()
                    contact_account = ""

                record: InvoiceRecord = {
                    "issue_date": issue_date,
                    "due_date": due_date,
                    "paid_at": paid_at,
                    "number": _val(attrs.number) or "",
                    "invoice_number": _val(attrs.number) or "",
                    "kind_label": "Rectificativa" if is_amending else "Factura",
                    "contact_name": contact_name,
                    "contact_account": contact_account,
                    "contact_tax_id": contact_tax_id,
                    "contact_zip": contact_zip,
                    "country_code": country_code,
                    "concept": concept,
                    "payment_status": _payment_status_label(attrs.payment_status),
                    "is_amending": is_amending,
                    "base": base,
                    "vat_amount": vat_amount,
                    "vat_pct": vat_pct_value,
                    "surcharge": surcharge_total,
                    "retention_amount": retention_amount,
                    "total": total,
                    "quarter": _get_quarter(issue_date) if issue_date else 0,
                    "line_items": line_items,
                }
                all_invoices.append(record)

            # Pagination -- break when on the last page (or when meta is absent)
            meta = _val(collection.meta)
            if not meta:
                break
            pagination = _val(meta.pagination_info)
            if not pagination:
                break
            total_pages: int = _val(pagination.total_pages) or 1
            if page >= total_pages:
                break
            page += 1

    # Sort by issue date ascending
    all_invoices.sort(key=lambda r: r["issue_date"] or datetime.date.min)
    return all_invoices


def fetch_income(year: int) -> list[InvoiceRecord]:
    """Fetch all issued invoices for the given year."""
    with create_client() as client:
        return _fetch_all_invoices(client, GetInvoicesFilterkind.INCOME, year)


def fetch_expenses(year: int) -> list[InvoiceRecord]:
    """Fetch all received invoices for the given year."""
    with create_client() as client:
        return _fetch_all_invoices(client, GetInvoicesFilterkind.EXPENSES, year)


# ---------------------------------------------------------------------------
# Filter
# ---------------------------------------------------------------------------


def filter_by_quarter(entries: list[InvoiceRecord], quarter: int) -> list[InvoiceRecord]:
    """Filter invoice records by quarter number (1-4)."""
    return [e for e in entries if e.get("quarter") == quarter]


# ---------------------------------------------------------------------------
# Build row data
# ---------------------------------------------------------------------------


def _income_row(r: InvoiceRecord) -> list[Any]:
    """Build a single row for the Income sheet."""
    return [
        _date_serial(r["issue_date"]),
        _date_serial(r["due_date"]),
        _date_serial(r["paid_at"]),
        r["number"],
        r["invoice_number"],
        r["kind_label"],
        r["contact_name"],
        r["contact_account"],
        r["contact_tax_id"],
        r["contact_zip"],
        r["concept"],
        r["payment_status"],
        bool(r["is_amending"]),
        _money(r["base"]),
        _money(r["vat_amount"]),
        (r["vat_pct"] or 0) / 100,
        _money(r["surcharge"]),
    ]


def _expense_row(r: InvoiceRecord) -> list[Any]:
    """Build a single row for the Expenses sheet."""
    return [
        _date_serial(r["issue_date"]),
        r["invoice_number"],
        r["contact_name"],
        r["contact_account"],
        r["contact_tax_id"],
        _money(r["base"]),
        _money(r["vat_amount"]),
        (r["vat_pct"] or 0) / 100,
        _money(r["total"]),
    ]


# ---------------------------------------------------------------------------
# Write & format sheets
# ---------------------------------------------------------------------------


def _ensure_worksheet(spreadsheet: gspread.Spreadsheet, title: str, rows: int, cols: int) -> gspread.Worksheet:
    """Get or create a worksheet, resizing it to the required dimensions."""
    # Need at least 2 rows so set_frozen(rows=1) doesn't fail with "can't freeze all visible rows".
    actual_rows = max(rows, 2)
    try:
        ws = spreadsheet.worksheet(title)
        ws.clear()
        ws.resize(rows=actual_rows, cols=cols)
    except gspread.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(title=title, rows=actual_rows, cols=cols)
    return ws


def _col_pairs(cols: list[str], fmt: CellFormat, total_rows: int) -> list[tuple[str, CellFormat]]:
    """Build (range, fmt) pairs for each column from FIRST_DATA_ROW to total_rows."""
    return [(f"{col}{FIRST_DATA_ROW}:{col}{total_rows}", fmt) for col in cols]


def format_sheet(
    worksheet: gspread.Worksheet,
    sheet_type: str,
    num_rows: int,
    quarter_data: list[int] | None = None,
) -> None:
    """Apply visual formatting to a worksheet.

    Args:
        worksheet: the gspread Worksheet
        sheet_type: SHEET_TYPE_INCOME or SHEET_TYPE_EXPENSES
        num_rows: number of data rows (excluding header)
        quarter_data: list of quarter numbers (1-4) per data row, for row coloring on income sheets
    """
    spec = SHEET_SPECS[sheet_type]
    sheet_id = worksheet.id
    total_rows = num_rows + 1  # +1 for header

    # Number/date format patterns (table column types don't define a display pattern).
    fmt_pairs: list[tuple[str, CellFormat]] = []
    if num_rows > 0:
        fmt_pairs.extend(_col_pairs(spec.date_cols, DATE_FMT, total_rows))
        fmt_pairs.extend(_col_pairs([spec.percent_col], PERCENT_FMT, total_rows))
        if spec.wrap_col:
            fmt_pairs.extend(_col_pairs([spec.wrap_col], WRAP_FMT, total_rows))
    if fmt_pairs:
        format_cell_ranges(worksheet, fmt_pairs)

    # Single batch_update for: addTable, row colors, auto-resize, fixed-width override.
    # (Pre-existing tables are deleted in main() *before* data is written, since
    # deleteTable also wipes the underlying cell data.)
    batch_requests: list[dict[str, Any]] = []

    table_end_row = max(total_rows, 2)  # tables need at least 1 data row
    batch_requests.append({
        "addTable": {
            "table": {
                "name": worksheet.title,
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": table_end_row,
                    "startColumnIndex": 0,
                    "endColumnIndex": spec.num_cols,
                },
                "columnProperties": [
                    {"columnIndex": i, "columnName": spec.headers[i], "columnType": spec.column_types[i]}
                    for i in range(spec.num_cols)
                ],
            }
        }
    })

    if num_rows > 0 and quarter_data:
        for i, q in enumerate(quarter_data):
            color = QUARTER_COLORS.get(q)
            if not color:
                continue
            row_idx = i + 1  # 0-based; header is row 0, first data row is 1
            batch_requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": row_idx,
                        "endRowIndex": row_idx + 1,
                        "startColumnIndex": 0,
                        "endColumnIndex": spec.num_cols,
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {
                                "red": color.red,
                                "green": color.green,
                                "blue": color.blue,
                            }
                        }
                    },
                    "fields": "userEnteredFormat.backgroundColor",
                }
            })

    if num_rows > 0:
        batch_requests.append({
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": 0,
                    "endIndex": spec.num_cols,
                }
            }
        })

    if spec.fixed_width_col_idx is not None:
        batch_requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": spec.fixed_width_col_idx,
                    "endIndex": spec.fixed_width_col_idx + 1,
                },
                "properties": {"pixelSize": CONCEPT_WIDTH_PX},
                "fields": "pixelSize",
            }
        })

    worksheet.spreadsheet.batch_update({"requests": batch_requests})


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------


def main(year: int | None = None, spreadsheet_id: str | None = None, credentials_path: str | None = None) -> None:
    if year is None:
        year = datetime.date.today().year

    with create_client() as client:
        print(f"Fetching income invoices for {year}...")
        income = _fetch_all_invoices(client, GetInvoicesFilterkind.INCOME, year)
        print(f"  -> {len(income)} issued invoices")

        print(f"Fetching expense invoices for {year}...")
        expenses = _fetch_all_invoices(client, GetInvoicesFilterkind.EXPENSES, year)
        print(f"  -> {len(expenses)} received invoices")

    # Connect to Google Sheets
    if credentials_path:
        gc = gspread.service_account(filename=credentials_path)
    else:
        gc = gspread.service_account()

    spreadsheet: gspread.Spreadsheet
    if spreadsheet_id:
        spreadsheet = gc.open_by_key(spreadsheet_id)
    else:
        title = f"Quipu Facturas {year}"
        try:
            spreadsheet = gc.open(title)
        except gspread.SpreadsheetNotFound:
            spreadsheet = gc.create(title)
            print(f"Created new spreadsheet: {title}")

    # Ensure Spanish locale so currency/date formats render correctly
    spreadsheet.batch_update({"requests": [{
        "updateSpreadsheetProperties": {
            "properties": {"locale": SPREADSHEET_LOCALE},
            "fields": "locale",
        }
    }]})

    print(f"Writing to spreadsheet: {spreadsheet.title}")

    # Build row data
    income_rows = [_income_row(r) for r in income]
    expense_rows = [_expense_row(r) for r in expenses]
    income_quarters = [r["quarter"] for r in income]

    # Define all sheets to write: (title, sheet_type, rows, quarters_or_none)
    sheets_to_write: list[tuple[str, str, list[list[Any]], list[int] | None]] = [
        ("Ingresos", SHEET_TYPE_INCOME, income_rows, income_quarters),
        ("Gastos", SHEET_TYPE_EXPENSES, expense_rows, None),
    ]
    for q in range(1, NUM_QUARTERS + 1):
        sheets_to_write.append((
            f"Ingresos T{q}", SHEET_TYPE_INCOME,
            [_income_row(r) for r in filter_by_quarter(income, q)], None,
        ))
        sheets_to_write.append((
            f"Gastos T{q}", SHEET_TYPE_EXPENSES,
            [_expense_row(r) for r in filter_by_quarter(expenses, q)], None,
        ))

    # Step 1: ensure all worksheets exist with the correct dimensions (this clears them).
    sheet_configs: list[tuple[gspread.Worksheet, str, list[list[Any]], list[int] | None]] = []
    for title, sheet_type, rows, quarters in sheets_to_write:
        spec = SHEET_SPECS[sheet_type]
        ws = _ensure_worksheet(spreadsheet, title, len(rows) + 1, spec.num_cols)
        sheet_configs.append((ws, sheet_type, rows, quarters))

    # Remove default "Sheet1" if it exists
    try:
        spreadsheet.del_worksheet(spreadsheet.worksheet("Sheet1"))
    except gspread.WorksheetNotFound:
        pass

    # Step 2: delete any pre-existing tables in a single batch BEFORE writing data.
    # deleteTable wipes the underlying cells, so it must run on empty worksheets.
    tables_by_sheet_id = _fetch_tables_by_sheet(spreadsheet)
    delete_requests: list[dict[str, Any]] = []
    for tids in tables_by_sheet_id.values():
        for tid in tids:
            delete_requests.append({"deleteTable": {"tableId": tid}})
    if delete_requests:
        spreadsheet.batch_update({"requests": delete_requests})

    # Step 3: write data into the (now table-free, empty) worksheets.
    for ws, sheet_type, rows, _ in sheet_configs:
        spec = SHEET_SPECS[sheet_type]
        ws.update([spec.headers] + rows, value_input_option="RAW")

    # Step 4: apply formatting and recreate native tables.
    print("Applying formatting...")
    for ws, sheet_type, rows, quarters in sheet_configs:
        format_sheet(ws, sheet_type, len(rows), quarters)
        time.sleep(1.0)  # stay under Sheets API write quota (60/min/user)

    print("Done!")


def _fetch_tables_by_sheet(spreadsheet: gspread.Spreadsheet) -> dict[int, list[int | str]]:
    """Return {sheet_id: [tableId, ...]} for all tables in the spreadsheet."""
    meta = spreadsheet.fetch_sheet_metadata({"fields": "sheets(properties(sheetId),tables(tableId))"})
    out: dict[int, list[int | str]] = {}
    for sheet in meta.get("sheets", []):
        sid = sheet["properties"]["sheetId"]
        tids = [t["tableId"] for t in sheet.get("tables", [])]
        if tids:
            out[sid] = tids
    return out


def cli() -> None:
    parser = argparse.ArgumentParser(description="Export Quipu invoices to Google Sheets")
    parser.add_argument("--year", type=int, default=None, help="Fiscal year (default: current year)")
    parser.add_argument("--spreadsheet-id", type=str, default=None, help="Google Sheets spreadsheet ID")
    parser.add_argument("--credentials", type=str, default=None, help="Path to service account JSON key")
    args = parser.parse_args()
    main(year=args.year, spreadsheet_id=args.spreadsheet_id, credentials_path=args.credentials)


if __name__ == "__main__":
    cli()

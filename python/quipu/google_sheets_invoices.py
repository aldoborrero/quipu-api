"""Export Quipu invoices (income & expenses) to a formatted Google Sheets spreadsheet.

Usage:
    python -m quipu.google_sheets_invoices [--year 2025] [--spreadsheet-id ID] [--credentials path/to/sa.json]

Requires: gspread, gspread_formatting
"""

from __future__ import annotations

import argparse
import datetime
from typing import Any

import gspread
from gspread_formatting import (
    Border,
    Borders,
    CellFormat,
    Color,
    NumberFormat,
    TextFormat,
    format_cell_range,
    set_frozen,
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

# User-facing column headers (Spanish, as required by the output spreadsheet)
INCOME_HEADERS: list[str] = [
    "Fecha de emisión",
    "Vencimiento",
    "Fecha de pago",
    "Número",
    "Número de Factura",
    "Tipo de operación",
    "Cliente",
    "Cuenta de cliente",
    "NIF",
    "Código postal",
    "Concepto",
    "Estado",
    "Rectificativa?",
    "Base",
    "IVA",
    "IVA (%)",
    "Recargo de equivalencia",
]

EXPENSES_HEADERS: list[str] = [
    "Fecha de emisión",
    "Número de Factura",
    "Proveedor",
    "Cuenta de Proveedor",
    "NIF",
    "Base",
    "IVA",
    "IVA (%)",
    "Total",
]

NUM_INCOME_COLS: int = len(INCOME_HEADERS)
NUM_EXPENSES_COLS: int = len(EXPENSES_HEADERS)

SHEET_TYPE_INCOME: str = "income"
SHEET_TYPE_EXPENSES: str = "expenses"

# Quarter colors for row highlighting (income master sheet)
COLOR_WHITE: Color = Color(1, 1, 1)
COLOR_Q2_YELLOW: Color = Color(1, 0.976, 0.769)  # #fff9c4
COLOR_Q3_GREEN: Color = Color(0.910, 0.961, 0.914)  # #e8f5e9
COLOR_Q4_BLUE: Color = Color(0.890, 0.949, 0.992)  # #e3f2fd

QUARTER_COLORS: dict[int, Color] = {
    1: COLOR_WHITE,
    2: COLOR_Q2_YELLOW,
    3: COLOR_Q3_GREEN,
    4: COLOR_Q4_BLUE,
}

HEADER_BG_COLOR: Color = Color(0.827, 0.827, 0.827)  # #d3d3d3
HEADER_TEXT_COLOR: Color = Color(0, 0, 0)
BORDER_COLOR: Color = Color(0.8, 0.8, 0.8)

# Column letters for the Income sheet
INCOME_DATE_COLS: list[str] = ["A", "B", "C"]
INCOME_COL_BASE: str = "N"
INCOME_COL_VAT: str = "O"
INCOME_COL_VAT_PCT: str = "P"
INCOME_COL_SURCHARGE: str = "Q"
INCOME_COL_CONCEPT_IDX: int = 10  # 0-based index for column K

# Column letters for the Expenses sheet
EXPENSES_DATE_COLS: list[str] = ["A"]
EXPENSES_COL_BASE: str = "F"
EXPENSES_COL_VAT: str = "G"
EXPENSES_COL_VAT_PCT: str = "H"
EXPENSES_COL_TOTAL: str = "I"

CONCEPT_WIDTH_PX: int = 300
SPREADSHEET_LOCALE: str = "es_ES"

# Formatting patterns
DATE_PATTERN: str = "dd/MM/yyyy"
CURRENCY_PATTERN: str = '#,##0.00 "€"'
INTEGER_PATTERN: str = "0"

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

# Type alias for invoice record dicts
InvoiceRecord = dict[str, Any]

# Sheet config: (worksheet, sheet_type, num_data_rows, quarter_data_or_none)
SheetConfig = tuple[gspread.Worksheet, str, int, list[int] | None]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _val(attr: Any) -> Any:
    """Return None for Unset values, otherwise the value itself."""
    if isinstance(attr, Unset) or attr is None:
        return None
    return attr


def _to_float(s: Any) -> float | None:
    """Convert a value to float, returning None for Unset/None/invalid."""
    if isinstance(s, Unset) or s is None:
        return None
    try:
        return float(s)
    except (ValueError, TypeError):
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


def _col_letter(n: int) -> str:
    """Convert 1-based column number to letter (1=A, 26=Z, 27=AA)."""
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result


def _money_or_dash(val: float | None) -> float | str:
    """Return the numeric value for currency cells, or '-' if zero/None."""
    if val is None or val == 0:
        return "-"
    return val


# ---------------------------------------------------------------------------
# Fetch from Quipu API
# ---------------------------------------------------------------------------


def _extract_item_data(
    items_map: dict[str, Any],
    item_ref: Any,
) -> tuple[str | None, float | None, float | None]:
    """Extract concept, vat_percent, and surcharge from an included line item.

    Returns:
        (concept, vat_percent, surcharge_amount) -- any may be None.
    """
    item_id = getattr(item_ref, "id", None)
    if item_id is None or str(item_id) not in items_map:
        return None, None, None

    item_obj = items_map[str(item_id)]
    item_attrs = getattr(item_obj, "attributes", None)
    if item_attrs is None:
        return None, None, None

    additional: dict[str, Any] = getattr(item_attrs, "additional_properties", {})

    # Concept text
    concept: str | None = None
    for field in ("concept", "description"):
        raw = getattr(item_attrs, field, None)
        val = _val(raw) if raw is not None else additional.get(field)
        if val:
            concept = str(val)
            break

    # VAT percent
    vat_pct: float | None = None
    raw_vp = getattr(item_attrs, "vat_percent", None)
    vp_val = _val(raw_vp) if raw_vp is not None else additional.get("vat_percent")
    if vp_val is not None:
        try:
            vat_pct = float(vp_val)
        except (ValueError, TypeError):
            pass

    # Equivalence surcharge
    surcharge: float | None = None
    raw_sur = additional.get("equivalence_surcharge_amount") or additional.get("surcharge_amount")
    if raw_sur is not None:
        try:
            surcharge = float(raw_sur)
        except (ValueError, TypeError):
            pass

    return concept, vat_pct, surcharge


def _infer_vat_percent(
    item_vat_percents: list[float],
    vat_amount: float | None,
    base: float | None,
) -> int:
    """Determine the VAT % from line items or by inference from amounts."""
    if item_vat_percents:
        return int(item_vat_percents[0])
    if vat_amount is None or vat_amount == 0:
        return 0
    if base and base != 0:
        try:
            return round(vat_amount / base * 100)
        except ZeroDivisionError:
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

                # Gather line-item data
                item_concepts: list[str] = []
                item_vat_percents: list[float] = []
                item_surcharges: list[float] = []

                if rels and not isinstance(rels.items, Unset) and rels.items:
                    items_data = _val(rels.items.data)
                    if items_data:
                        for item_ref in items_data:
                            concept, vat_pct, surcharge = _extract_item_data(items_map, item_ref)
                            if concept:
                                item_concepts.append(concept)
                            if vat_pct is not None:
                                item_vat_percents.append(vat_pct)
                            if surcharge is not None:
                                item_surcharges.append(surcharge)

                # Determine if this is an amending (rectificative) invoice
                is_amending = False
                if rels and not isinstance(rels.amended_invoice, Unset) and rels.amended_invoice:
                    if _val(rels.amended_invoice.data) is not None:
                        is_amending = True

                issue_date: datetime.date | None = _val(attrs.issue_date)
                due_dates: list[datetime.date] | None = _val(attrs.due_dates)
                due_date = due_dates[0] if due_dates else None
                paid_at: datetime.date | None = _val(attrs.paid_at)

                base = _to_float(attrs.total_amount_without_taxes)
                vat_amount = _to_float(attrs.vat_amount)
                total = _to_float(attrs.total_amount)

                vat_pct_value = _infer_vat_percent(item_vat_percents, vat_amount, base)
                surcharge_total = sum(item_surcharges) if item_surcharges else 0.0

                # For issued invoices: the recipient is the client
                # For received invoices: the issuer is the supplier
                if kind == GetInvoicesFilterkind.INCOME:
                    contact_name = _val(attrs.recipient_name) or ""
                    contact_tax_id = _val(attrs.recipient_tax_id) or ""
                    contact_zip = _val(attrs.recipient_zip_code) or ""
                    contact_account = ""
                    if rels and not isinstance(rels.accounting_subcategory, Unset) and rels.accounting_subcategory:
                        sub_data = _val(rels.accounting_subcategory.data)
                        if sub_data and hasattr(sub_data, "id"):
                            contact_account = str(_val(sub_data.id) or "")
                else:
                    contact_name = _val(attrs.issuing_name) or ""
                    contact_tax_id = _val(attrs.issuing_tax_id) or ""
                    contact_zip = _val(attrs.issuing_zip_code) or ""
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
                    "concept": " | ".join(item_concepts) if item_concepts else "",
                    "payment_status": _payment_status_label(attrs.payment_status),
                    "is_amending": is_amending,
                    "base": base,
                    "vat_amount": vat_amount,
                    "vat_pct": vat_pct_value,
                    "surcharge": surcharge_total,
                    "total": total,
                    "quarter": _get_quarter(issue_date) if issue_date else 0,
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
        "Sí" if r["is_amending"] else "-",
        r["base"] if r["base"] is not None else 0,
        _money_or_dash(r["vat_amount"]),
        r["vat_pct"],
        _money_or_dash(r["surcharge"]),
    ]


def _expense_row(r: InvoiceRecord) -> list[Any]:
    """Build a single row for the Expenses sheet."""
    return [
        _date_serial(r["issue_date"]),
        r["invoice_number"],
        r["contact_name"],
        r["contact_account"],
        r["contact_tax_id"],
        r["base"] if r["base"] is not None else 0,
        _money_or_dash(r["vat_amount"]),
        r["vat_pct"],
        r["total"] if r["total"] is not None else 0,
    ]


# ---------------------------------------------------------------------------
# Write & format sheets
# ---------------------------------------------------------------------------


def _ensure_worksheet(spreadsheet: gspread.Spreadsheet, title: str, rows: int, cols: int) -> gspread.Worksheet:
    """Get or create a worksheet, resizing it to the required dimensions."""
    try:
        ws = spreadsheet.worksheet(title)
        ws.clear()
        ws.resize(rows=max(rows, 1), cols=cols)
    except gspread.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(title=title, rows=max(rows, 1), cols=cols)
    return ws


def write_sheet(worksheet: gspread.Worksheet, rows: list[list[Any]], headers: list[str]) -> None:
    """Write headers + data rows to the worksheet."""
    all_data: list[list[Any]] = [headers] + rows
    worksheet.update(all_data, value_input_option="RAW")


def _apply_date_format(worksheet: gspread.Worksheet, cols: list[str], total_rows: int) -> None:
    """Apply date formatting to the specified columns."""
    date_fmt = CellFormat(
        numberFormat=NumberFormat(type="DATE", pattern=DATE_PATTERN),
        horizontalAlignment="LEFT",
    )
    for col in cols:
        format_cell_range(worksheet, f"{col}{FIRST_DATA_ROW}:{col}{total_rows}", date_fmt)


def _apply_currency_format(worksheet: gspread.Worksheet, cols: list[str], total_rows: int) -> None:
    """Apply currency formatting to the specified columns."""
    currency_fmt = CellFormat(
        numberFormat=NumberFormat(type="NUMBER", pattern=CURRENCY_PATTERN),
        horizontalAlignment="RIGHT",
    )
    for col in cols:
        format_cell_range(worksheet, f"{col}{FIRST_DATA_ROW}:{col}{total_rows}", currency_fmt)


def _apply_integer_format(worksheet: gspread.Worksheet, col: str, total_rows: int) -> None:
    """Apply integer formatting to a column."""
    pct_fmt = CellFormat(
        numberFormat=NumberFormat(type="NUMBER", pattern=INTEGER_PATTERN),
        horizontalAlignment="RIGHT",
    )
    format_cell_range(worksheet, f"{col}{FIRST_DATA_ROW}:{col}{total_rows}", pct_fmt)


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
    num_cols = NUM_INCOME_COLS if sheet_type == SHEET_TYPE_INCOME else NUM_EXPENSES_COLS
    last_col = _col_letter(num_cols)

    set_frozen(worksheet, rows=1)

    # Header formatting (always applied, even for empty sheets)
    header_fmt = CellFormat(
        backgroundColor=HEADER_BG_COLOR,
        textFormat=TextFormat(bold=True, foregroundColor=HEADER_TEXT_COLOR),
        horizontalAlignment="CENTER",
    )
    format_cell_range(worksheet, f"A1:{last_col}1", header_fmt)

    if num_rows == 0:
        return

    total_rows = num_rows + 1  # +1 for header

    # Borders for all cells with data
    thin_border = Border("SOLID", BORDER_COLOR)
    border_fmt = CellFormat(
        borders=Borders(top=thin_border, bottom=thin_border, left=thin_border, right=thin_border)
    )
    format_cell_range(worksheet, f"A1:{last_col}{total_rows}", border_fmt)

    # Date columns
    if sheet_type == SHEET_TYPE_INCOME:
        _apply_date_format(worksheet, INCOME_DATE_COLS, total_rows)
    else:
        _apply_date_format(worksheet, EXPENSES_DATE_COLS, total_rows)

    # Currency & percentage columns
    if sheet_type == SHEET_TYPE_INCOME:
        _apply_currency_format(worksheet, [INCOME_COL_BASE, INCOME_COL_VAT, INCOME_COL_SURCHARGE], total_rows)
        _apply_integer_format(worksheet, INCOME_COL_VAT_PCT, total_rows)
    else:
        _apply_currency_format(worksheet, [EXPENSES_COL_BASE, EXPENSES_COL_VAT, EXPENSES_COL_TOTAL], total_rows)
        _apply_integer_format(worksheet, EXPENSES_COL_VAT_PCT, total_rows)

    # Concept column (K) in income sheets: wide + wrap
    if sheet_type == SHEET_TYPE_INCOME:
        wrap_fmt = CellFormat(wrapStrategy="WRAP")
        format_cell_range(worksheet, f"K{FIRST_DATA_ROW}:K{total_rows}", wrap_fmt)

    # Row coloring by quarter (income master sheet only)
    # Batch all row color requests into a single API call to avoid per-row overhead.
    if sheet_type == SHEET_TYPE_INCOME and quarter_data:
        color_requests: list[dict[str, Any]] = []
        for i, q in enumerate(quarter_data):
            if q == 1:  # Q1 is white (default), skip
                continue
            color = QUARTER_COLORS.get(q)
            if not color:
                continue
            row_idx = i + 1  # 0-based row index; header is row 0, first data row is 1
            color_requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": worksheet.id,
                        "startRowIndex": row_idx,
                        "endRowIndex": row_idx + 1,
                        "startColumnIndex": 0,
                        "endColumnIndex": num_cols,
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
        if color_requests:
            worksheet.spreadsheet.batch_update({"requests": color_requests})

    # Column widths: auto-resize all columns first
    sheet_id = worksheet.id
    auto_requests: list[dict[str, Any]] = [{
        "autoResizeDimensions": {
            "dimensions": {
                "sheetId": sheet_id,
                "dimension": "COLUMNS",
                "startIndex": 0,
                "endIndex": num_cols,
            }
        }
    }]
    worksheet.spreadsheet.batch_update({"requests": auto_requests})

    # Then override Concept (K) with fixed width so auto-resize doesn't undo it
    if sheet_type == SHEET_TYPE_INCOME:
        fix_requests: list[dict[str, Any]] = [{
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": INCOME_COL_CONCEPT_IDX,
                    "endIndex": INCOME_COL_CONCEPT_IDX + 1,
                },
                "properties": {"pixelSize": CONCEPT_WIDTH_PX},
                "fields": "pixelSize",
            }
        }]
        worksheet.spreadsheet.batch_update({"requests": fix_requests})


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

    # Master sheets
    sheet_configs: list[SheetConfig] = []

    ws = _ensure_worksheet(spreadsheet, "Ingresos", len(income_rows) + 1, NUM_INCOME_COLS)
    write_sheet(ws, income_rows, INCOME_HEADERS)
    sheet_configs.append((ws, SHEET_TYPE_INCOME, len(income_rows), income_quarters))

    ws = _ensure_worksheet(spreadsheet, "Gastos", len(expense_rows) + 1, NUM_EXPENSES_COLS)
    write_sheet(ws, expense_rows, EXPENSES_HEADERS)
    sheet_configs.append((ws, SHEET_TYPE_EXPENSES, len(expense_rows), None))

    # Quarterly sheets
    for q in range(1, NUM_QUARTERS + 1):
        q_income = filter_by_quarter(income, q)
        q_rows = [_income_row(r) for r in q_income]
        ws = _ensure_worksheet(spreadsheet, f"Ingresos T{q}", len(q_rows) + 1, NUM_INCOME_COLS)
        write_sheet(ws, q_rows, INCOME_HEADERS)
        sheet_configs.append((ws, SHEET_TYPE_INCOME, len(q_rows), None))

        q_expenses = filter_by_quarter(expenses, q)
        q_rows = [_expense_row(r) for r in q_expenses]
        ws = _ensure_worksheet(spreadsheet, f"Gastos T{q}", len(q_rows) + 1, NUM_EXPENSES_COLS)
        write_sheet(ws, q_rows, EXPENSES_HEADERS)
        sheet_configs.append((ws, SHEET_TYPE_EXPENSES, len(q_rows), None))

    # Remove default "Sheet1" if it exists
    try:
        default_sheet = spreadsheet.worksheet("Sheet1")
        spreadsheet.del_worksheet(default_sheet)
    except gspread.WorksheetNotFound:
        pass

    # Apply formatting to all sheets
    print("Applying formatting...")
    for ws, sheet_type, num_rows, quarters in sheet_configs:
        format_sheet(ws, sheet_type, num_rows, quarters)

    print("Done!")


def cli() -> None:
    parser = argparse.ArgumentParser(description="Export Quipu invoices to Google Sheets")
    parser.add_argument("--year", type=int, default=None, help="Fiscal year (default: current year)")
    parser.add_argument("--spreadsheet-id", type=str, default=None, help="Google Sheets spreadsheet ID")
    parser.add_argument("--credentials", type=str, default=None, help="Path to service account JSON key")
    args = parser.parse_args()
    main(year=args.year, spreadsheet_id=args.spreadsheet_id, credentials_path=args.credentials)


if __name__ == "__main__":
    cli()

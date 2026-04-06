"""Export Quipu invoices (income & expenses) to a formatted Google Sheets spreadsheet.

Usage:
    python -m quipu.google_sheets_invoices [--year 2025] [--spreadsheet-id ID] [--credentials path/to/sa.json]

Requires: gspread, gspread_formatting
"""

from __future__ import annotations

import argparse
import datetime
import time
from collections.abc import Callable
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
    TextFormat,
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

# Home country for operation classification. The autónomo files Modelo 303/130
# from Spain, so counterparties with this country are "national".
HOME_COUNTRY_CODE: str = "ES"

# Default rate used to self-assess VAT on reverse-charge transactions (intra-EU
# acquisitions and non-EU services under art. 84.1.2º LIVA). Most goods and
# services fall under 21 %; a gestor can override via the CLI.
SELF_ASSESS_INTRA_EU_RATE: Decimal = Decimal("21")

# Quipu ItemAttributesKind values. Treated as magic strings across the codebase
# today; extracted here so a rename in Quipu surfaces as a single compile error.
KIND_CURRENT: str = "current"
KIND_ASSETS: str = "assets"
KIND_REIMBURSEMENT: str = "reimbursement"

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
    if code == HOME_COUNTRY_CODE:
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
    kind = str(kind_raw.value if hasattr(kind_raw, "value") else kind_raw or KIND_CURRENT)

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
# Tax form aggregation helpers
# ---------------------------------------------------------------------------


def _computable_income_base(invoice: InvoiceRecord) -> Decimal:
    """Pre-VAT base of an income invoice for Modelo 130 casilla 01.

    Excludes reimbursement line items (pass-through). Rectificativas are
    already returned by Quipu with negative base/line-item amounts, so no
    manual sign flip is needed — we just sum what the API gives us.
    Falls back to the invoice-level base when line items are absent.
    """
    line_items: list[LineItem] = invoice.get("line_items") or []
    if line_items:
        return sum(
            (li.base for li in line_items if li.kind != KIND_REIMBURSEMENT),
            start=ZERO,
        )
    return invoice.get("base") or ZERO


def _deductible_expense_base(invoice: InvoiceRecord) -> Decimal:
    """Pre-VAT deductible base of an expense invoice for Modelo 130 casilla 02.

    Honors each line's deductible_expense_percent. Excludes reimbursements.
    Assets are included at 100% as a simplification — real amortization goes in
    the annual declaration, not the quarterly payment fractionado.
    """
    line_items: list[LineItem] = invoice.get("line_items") or []
    if line_items:
        return sum(
            (
                li.base * li.deductible_expense_percent / HUNDRED
                for li in line_items
                if li.kind != KIND_REIMBURSEMENT
            ),
            start=ZERO,
        )
    return invoice.get("base") or ZERO


def _income_retentions(invoice: InvoiceRecord) -> Decimal:
    """IRPF withholdings the client applied to an income invoice (casilla 06)."""
    return invoice.get("retention_amount") or ZERO


@dataclass
class Modelo130Quarter:
    """Computed Modelo 130 values for one quarter (all cumulative except *_periodo)."""

    quarter: int
    ingresos_periodo: Decimal     # delta for this quarter
    gastos_periodo: Decimal       # delta for this quarter
    retenciones_periodo: Decimal  # delta for this quarter
    ingresos_acum: Decimal        # casilla 01
    gastos_acum: Decimal          # casilla 02
    rendimiento_neto: Decimal     # casilla 03 = 01 - 02
    casilla_04: Decimal           # 20% of casilla 03 (floored at 0)
    casilla_05: Decimal           # sum of positive casilla 07 from previous quarters
    retenciones_acum: Decimal     # casilla 06
    casilla_07: Decimal           # 04 - 05 - 06 (can be negative)


def compute_modelo_130(
    income: list[InvoiceRecord],
    expenses: list[InvoiceRecord],
) -> list[Modelo130Quarter]:
    """Compute Modelo 130 values for all four quarters of a year.

    Returns a list of four Modelo130Quarter (one per T1..T4), with casilla 05
    threaded forward from prior quarters' positive casilla 07 values.
    """
    result: list[Modelo130Quarter] = []
    prior_positive_07 = ZERO  # running sum for casilla 05
    twenty_percent = Decimal("0.20")

    for q in range(1, NUM_QUARTERS + 1):
        q_income = filter_by_quarter(income, q)
        q_expenses = filter_by_quarter(expenses, q)

        ingresos_periodo = sum((_computable_income_base(r) for r in q_income), start=ZERO)
        gastos_periodo = sum((_deductible_expense_base(r) for r in q_expenses), start=ZERO)
        retenciones_periodo = sum((_income_retentions(r) for r in q_income), start=ZERO)

        if result:
            prev = result[-1]
            ingresos_acum = prev.ingresos_acum + ingresos_periodo
            gastos_acum = prev.gastos_acum + gastos_periodo
            retenciones_acum = prev.retenciones_acum + retenciones_periodo
        else:
            ingresos_acum = ingresos_periodo
            gastos_acum = gastos_periodo
            retenciones_acum = retenciones_periodo

        rendimiento_neto = ingresos_acum - gastos_acum
        casilla_04 = max(rendimiento_neto, ZERO) * twenty_percent
        casilla_05 = prior_positive_07
        casilla_07 = casilla_04 - casilla_05 - retenciones_acum

        result.append(Modelo130Quarter(
            quarter=q,
            ingresos_periodo=ingresos_periodo,
            gastos_periodo=gastos_periodo,
            retenciones_periodo=retenciones_periodo,
            ingresos_acum=ingresos_acum,
            gastos_acum=gastos_acum,
            rendimiento_neto=rendimiento_neto,
            casilla_04=casilla_04,
            casilla_05=casilla_05,
            retenciones_acum=retenciones_acum,
            casilla_07=casilla_07,
        ))

        # Thread casilla 05 forward: only positive results count.
        if casilla_07 > 0:
            prior_positive_07 += casilla_07

    return result


# ---------------------------------------------------------------------------
# Modelo 303 (IVA trimestral)
# ---------------------------------------------------------------------------


@dataclass
class BaseCuota:
    """A (base imponible, cuota IVA) pair. Mutable so aggregation is in place."""
    base: Decimal = ZERO
    cuota: Decimal = ZERO

    def add(self, base: Decimal, cuota: Decimal) -> None:
        self.base += base
        self.cuota += cuota


@dataclass
class Modelo303Quarter:
    """Computed Modelo 303 values for one quarter (per-quarter, not cumulative)."""

    quarter: int
    # --- IVA devengado (repercutido) ---
    # National sales (régimen general) bucketed by VAT rate: casillas 1-9.
    national_rep: dict[Decimal, BaseCuota]
    # Adquisiciones intracomunitarias de bienes y servicios (UE, self-assessed):
    # casillas 10-11.
    intra_eu_acq: dict[Decimal, BaseCuota]
    # Otras operaciones con inversión del sujeto pasivo (excepto adq. intracom):
    # casillas 12-13. Non-EU services with VAT=0 are self-assessed here via
    # art. 84.1.2º LIVA ("reverse charge by localization rule").
    isp_other: dict[Decimal, BaseCuota]
    # Intra-EU deliveries exentas: casilla 59.
    intra_eu_deliveries: Decimal
    # Exportaciones de bienes: casilla 60. (Kept as a row even if unused so the
    # structure is visible for future goods-export cases.)
    exports_goods: Decimal
    # No sujetas por reglas de localización con derecho a deducción: casilla 120.
    # Services to non-EU businesses go here, not in casilla 60.
    no_sujetas_loc: Decimal

    # --- IVA soportado (deducible) ---
    # Cuotas are already scaled by deductible_vat_percent.
    # IMPORTANT: nat_current / nat_assets include both domestic purchases and
    # the self-assessed side of non-EU service reverse-charge transactions —
    # that's how the AEAT form expects them to be reported (casillas 28-31).
    nat_current: BaseCuota   # casillas 28-29
    nat_assets: BaseCuota    # casillas 30-31
    imp_current: BaseCuota   # casillas 32-33 (physical imports with customs VAT)
    imp_assets: BaseCuota    # casillas 34-35
    eu_current: BaseCuota    # casillas 36-37 (intra-EU acquisitions)
    eu_assets: BaseCuota     # casillas 38-39

    @property
    def total_devengado(self) -> Decimal:
        total = ZERO
        for bc in self.national_rep.values():
            total += bc.cuota
        for bc in self.intra_eu_acq.values():
            total += bc.cuota
        for bc in self.isp_other.values():
            total += bc.cuota
        return total

    @property
    def total_deducible(self) -> Decimal:
        return (
            self.nat_current.cuota + self.nat_assets.cuota
            + self.imp_current.cuota + self.imp_assets.cuota
            + self.eu_current.cuota + self.eu_assets.cuota
        )

    @property
    def resultado(self) -> Decimal:
        return self.total_devengado - self.total_deducible


def _empty_modelo_303_quarter(quarter: int) -> Modelo303Quarter:
    return Modelo303Quarter(
        quarter=quarter,
        national_rep={},
        intra_eu_acq={},
        isp_other={},
        intra_eu_deliveries=ZERO,
        exports_goods=ZERO,
        no_sujetas_loc=ZERO,
        nat_current=BaseCuota(),
        nat_assets=BaseCuota(),
        imp_current=BaseCuota(),
        imp_assets=BaseCuota(),
        eu_current=BaseCuota(),
        eu_assets=BaseCuota(),
    )


def _aggregate_income_303(quarter: Modelo303Quarter, invoices: list[InvoiceRecord]) -> None:
    """Add income invoices to the quarter's repercutido buckets."""
    for inv in invoices:
        classification = classify_operation(inv.get("country_code"))
        line_items: list[LineItem] = inv.get("line_items") or []

        if not line_items:
            # Fall back to invoice-level base when no line items are available.
            base = inv.get("base") or ZERO
            cuota = inv.get("vat_amount") or ZERO
            rate = Decimal(inv.get("vat_pct") or 0)
            if classification == OP_NATIONAL:
                if cuota > 0 or rate > 0:
                    quarter.national_rep.setdefault(rate, BaseCuota()).add(base, cuota)
                else:
                    # National exempt is rare; fold into no_sujetas as a catch-all.
                    quarter.no_sujetas_loc += base
            elif classification == OP_INTRA_EU:
                quarter.intra_eu_deliveries += base
            else:  # OP_EXPORT — services to non-EU → casilla 120 per user direction
                quarter.no_sujetas_loc += base
            continue

        for li in line_items:
            if li.kind == KIND_REIMBURSEMENT:
                continue
            if classification == OP_NATIONAL:
                if li.vat_amount > 0 or li.vat_percent > 0:
                    quarter.national_rep.setdefault(li.vat_percent, BaseCuota()).add(
                        li.base, li.vat_amount
                    )
                else:
                    quarter.no_sujetas_loc += li.base
            elif classification == OP_INTRA_EU:
                quarter.intra_eu_deliveries += li.base
            else:  # OP_EXPORT
                quarter.no_sujetas_loc += li.base


def _aggregate_expense_303(
    quarter: Modelo303Quarter,
    invoices: list[InvoiceRecord],
    self_assess_rate: Decimal,
) -> None:
    """Add expense invoices to the quarter's soportado buckets.

    Intra-EU acquisitions with supplier VAT=0 are self-assessed at
    self_assess_rate and mirrored into casillas 10-11 (devengado) and 36-39
    (soportado, scaled by line's deductible_vat_percent).
    """
    for inv in invoices:
        classification = classify_operation(inv.get("country_code"))
        line_items: list[LineItem] = inv.get("line_items") or []

        if not line_items:
            # Fall back to invoice level without self-assessment.
            base = inv.get("base") or ZERO
            cuota = inv.get("vat_amount") or ZERO
            target = {
                OP_NATIONAL: quarter.nat_current,
                OP_INTRA_EU: quarter.eu_current,
                OP_EXPORT: quarter.imp_current,
            }.get(classification, quarter.nat_current)
            target.add(base, cuota)
            continue

        for li in line_items:
            if li.kind == KIND_REIMBURSEMENT:
                continue

            is_asset = li.kind == KIND_ASSETS
            deduct_fraction = li.deductible_vat_percent / HUNDRED
            deducible_cuota = li.vat_amount * deduct_fraction

            if classification == OP_NATIONAL:
                target = quarter.nat_assets if is_asset else quarter.nat_current
                target.add(li.base, deducible_cuota)

            elif classification == OP_INTRA_EU:
                if li.vat_percent == 0 and li.base != 0:
                    # Self-assess: synthetic cuota at self_assess_rate.
                    assessed_cuota = li.base * self_assess_rate / HUNDRED
                    # Casillas 10-11: full self-assessed cuota as IVA devengado.
                    quarter.intra_eu_acq.setdefault(self_assess_rate, BaseCuota()).add(
                        li.base, assessed_cuota
                    )
                    # Casillas 36-37 / 38-39: mirrored as IVA soportado, scaled.
                    target = quarter.eu_assets if is_asset else quarter.eu_current
                    target.add(li.base, assessed_cuota * deduct_fraction)
                else:
                    # Supplier charged VAT (unusual for intra-EU B2B); use as-is.
                    target = quarter.eu_assets if is_asset else quarter.eu_current
                    target.add(li.base, deducible_cuota)

            else:  # OP_EXPORT: non-EU supplier
                # Heuristic: VAT=0 on a non-EU supplier invoice is almost
                # always a reverse-charge service (SaaS, consulting, etc.),
                # where Spain is the place of supply (art. 84.1.2º LIVA).
                # VAT>0 from a non-EU supplier typically means customs VAT
                # on a physical import. These behave very differently on
                # the form.
                if li.vat_percent == 0 and li.base != 0:
                    assessed_cuota = li.base * self_assess_rate / HUNDRED
                    # Casillas 12-13: devengado (full self-assessed cuota).
                    quarter.isp_other.setdefault(self_assess_rate, BaseCuota()).add(
                        li.base, assessed_cuota
                    )
                    # Casillas 28-31: deducible, reported together with
                    # domestic purchases. Base is added gross, cuota scaled
                    # by the line's deductible_vat_percent.
                    target = quarter.nat_assets if is_asset else quarter.nat_current
                    target.add(li.base, assessed_cuota * deduct_fraction)
                else:
                    # Physical import with customs VAT: casillas 32-35.
                    target = quarter.imp_assets if is_asset else quarter.imp_current
                    target.add(li.base, deducible_cuota)


def compute_modelo_303(
    income: list[InvoiceRecord],
    expenses: list[InvoiceRecord],
    self_assess_rate: Decimal = SELF_ASSESS_INTRA_EU_RATE,
) -> list[Modelo303Quarter]:
    """Compute Modelo 303 values for all four quarters of a year.

    303 is per-quarter (not cumulative like 130): each quarter is a standalone
    declaration. The "Anual" column in the sheet is the sum of the four quarters.
    """
    result: list[Modelo303Quarter] = []
    for q in range(1, NUM_QUARTERS + 1):
        quarter = _empty_modelo_303_quarter(q)
        _aggregate_income_303(quarter, filter_by_quarter(income, q))
        _aggregate_expense_303(quarter, filter_by_quarter(expenses, q), self_assess_rate)
        result.append(quarter)
    return result


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


def main(
    year: int | None = None,
    spreadsheet_id: str | None = None,
    credentials_path: str | None = None,
    self_assess_rate: Decimal = SELF_ASSESS_INTRA_EU_RATE,
) -> None:
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

    # Step 5: modelo summary sheets
    print("Writing modelo summary sheets...")
    m303_quarters = compute_modelo_303(income, expenses, self_assess_rate=self_assess_rate)
    write_modelo_sheet(
        spreadsheet,
        "Modelo 303",
        _modelo_303_rows(m303_quarters, self_assess_rate=self_assess_rate),
    )
    time.sleep(1.0)
    m130_quarters = compute_modelo_130(income, expenses)
    write_modelo_sheet(spreadsheet, "Modelo 130", _modelo_130_rows(m130_quarters))
    time.sleep(1.0)

    print("Done!")


# ---------------------------------------------------------------------------
# Modelo summary sheets
# ---------------------------------------------------------------------------

MODELO_WARNING: str = (
    "Estos valores son una aproximación derivada de los datos de Quipu. "
    "Verificar con tu gestor antes de presentar."
)

WARNING_FMT = CellFormat(
    backgroundColor=Color(1, 0.949, 0.8),  # pale yellow
    textFormat=TextFormat(bold=True, foregroundColor=Color(0.4, 0.2, 0)),
    horizontalAlignment="LEFT",
    wrapStrategy="WRAP",
)
SECTION_FMT = CellFormat(
    backgroundColor=Color(0.93, 0.93, 0.93),
    textFormat=TextFormat(bold=True),
    horizontalAlignment="LEFT",
)
TOTAL_FMT = CellFormat(textFormat=TextFormat(bold=True))
MODELO_HEADER_FMT = CellFormat(
    backgroundColor=Color(0.827, 0.827, 0.827),
    textFormat=TextFormat(bold=True),
    horizontalAlignment="CENTER",
)
# Locale-aware currency format that shows 0 as a dash.
MODELO_CURRENCY_FMT = CellFormat(
    numberFormat=NumberFormat(type="CURRENCY", pattern='#,##0.00 [$€];-#,##0.00 [$€];"-"'),
    horizontalAlignment="RIGHT",
)


@dataclass
class ModeloRow:
    """One row in a modelo summary sheet."""

    label: str
    values: list[Decimal] | None = None  # None for section headers / blank rows
    bold: bool = False
    section: bool = False


def _modelo_303_rows(
    quarters: list[Modelo303Quarter],
    self_assess_rate: Decimal = SELF_ASSESS_INTRA_EU_RATE,
) -> list[ModeloRow]:
    """Build the displayable rows for the Modelo 303 sheet.

    303 is per-quarter (not cumulative like 130). Anual = sum across T1..T4.
    Rate buckets are discovered from the data, so the sheet only shows rows
    for rates actually present.
    """

    # Collect all VAT rates that appear anywhere across quarters.
    national_rates: set[Decimal] = set()
    ai_rates: set[Decimal] = set()
    isp_rates: set[Decimal] = set()
    for q in quarters:
        national_rates.update(q.national_rep.keys())
        ai_rates.update(q.intra_eu_acq.keys())
        isp_rates.update(q.isp_other.keys())

    def rate_label(rate: Decimal) -> str:
        # Strip trailing zeros for display: Decimal("21.0") → "21"
        normalized = rate.normalize()
        return f"{normalized:f}".rstrip(".")

    sa_label = rate_label(self_assess_rate)

    def across(getter: Callable[[Modelo303Quarter], Decimal]) -> list[Decimal]:
        """[T1, T2, T3, T4, Anual] — Anual is the sum of the four quarters."""
        vals = [getter(q) for q in quarters]
        return vals + [sum(vals, start=ZERO)]

    def rate_bucket_across(
        bucket_getter: Callable[[Modelo303Quarter], dict[Decimal, BaseCuota]],
        rate: Decimal,
        field: str,
    ) -> list[Decimal]:
        def pick(q: Modelo303Quarter) -> Decimal:
            bc = bucket_getter(q).get(rate)
            return getattr(bc, field) if bc is not None else ZERO
        return across(pick)

    rows: list[ModeloRow] = [
        ModeloRow(
            f"Nota: Servicios a no-UE → cas. 120 (no cas. 60). Adq. "
            f"intracomunitarias con IVA=0 se auto-liquidan al {sa_label} % en "
            f"cas. 10-11 y 36-37. Servicios recibidos de no-UE con IVA=0 "
            f"se auto-liquidan al {sa_label} % en cas. 12-13 (devengado) y "
            f"28-29 (deducible). Reverse charge doméstico no se detecta.",
            section=True,
        ),
        ModeloRow(""),
        ModeloRow("IVA DEVENGADO (repercutido)", section=True),
    ]

    if national_rates:
        for rate in sorted(national_rates):
            label = rate_label(rate)
            rows.append(ModeloRow(
                f"Base régimen general {label} %",
                rate_bucket_across(lambda q: q.national_rep, rate, "base"),
            ))
            rows.append(ModeloRow(
                f"Cuota régimen general {label} %",
                rate_bucket_across(lambda q: q.national_rep, rate, "cuota"),
            ))
    else:
        rows.append(ModeloRow("Régimen general — sin operaciones nacionales"))

    if ai_rates:
        for rate in sorted(ai_rates):
            label = rate_label(rate)
            rows.append(ModeloRow(
                f"10  Base adquisiciones intracomunitarias {label} %",
                rate_bucket_across(lambda q: q.intra_eu_acq, rate, "base"),
            ))
            rows.append(ModeloRow(
                f"11  Cuota adquisiciones intracomunitarias {label} %",
                rate_bucket_across(lambda q: q.intra_eu_acq, rate, "cuota"),
            ))

    if isp_rates:
        for rate in sorted(isp_rates):
            label = rate_label(rate)
            rows.append(ModeloRow(
                f"12  Base otras op. con inv. sujeto pasivo {label} %",
                rate_bucket_across(lambda q: q.isp_other, rate, "base"),
            ))
            rows.append(ModeloRow(
                f"13  Cuota otras op. con inv. sujeto pasivo {label} %",
                rate_bucket_across(lambda q: q.isp_other, rate, "cuota"),
            ))

    rows += [
        ModeloRow("59  Entregas intracomunitarias exentas", across(lambda q: q.intra_eu_deliveries)),
        ModeloRow("60  Exportaciones de bienes", across(lambda q: q.exports_goods)),
        ModeloRow("120 No sujetas por localización (servicios no-UE)", across(lambda q: q.no_sujetas_loc)),
        ModeloRow("TOTAL IVA devengado", across(lambda q: q.total_devengado), bold=True),
        ModeloRow(""),

        ModeloRow("IVA SOPORTADO (deducible)", section=True),
        ModeloRow("28  Base op. interiores corrientes", across(lambda q: q.nat_current.base)),
        ModeloRow("29  Cuota op. interiores corrientes", across(lambda q: q.nat_current.cuota)),
        ModeloRow("30  Base op. interiores bienes de inversión", across(lambda q: q.nat_assets.base)),
        ModeloRow("31  Cuota op. interiores bienes de inversión", across(lambda q: q.nat_assets.cuota)),
        ModeloRow("32  Base importaciones corrientes", across(lambda q: q.imp_current.base)),
        ModeloRow("33  Cuota importaciones corrientes", across(lambda q: q.imp_current.cuota)),
        ModeloRow("34  Base importaciones bienes de inversión", across(lambda q: q.imp_assets.base)),
        ModeloRow("35  Cuota importaciones bienes de inversión", across(lambda q: q.imp_assets.cuota)),
        ModeloRow("36  Base adq. intracomunitarias corrientes", across(lambda q: q.eu_current.base)),
        ModeloRow("37  Cuota adq. intracomunitarias corrientes", across(lambda q: q.eu_current.cuota)),
        ModeloRow("38  Base adq. intracomunitarias bienes de inversión", across(lambda q: q.eu_assets.base)),
        ModeloRow("39  Cuota adq. intracomunitarias bienes de inversión", across(lambda q: q.eu_assets.cuota)),
        ModeloRow("TOTAL IVA deducible", across(lambda q: q.total_deducible), bold=True),
        ModeloRow(""),

        ModeloRow("RESULTADO", section=True),
        ModeloRow("Resultado régimen general (devengado − deducible)",
                  across(lambda q: q.resultado), bold=True),
        ModeloRow(""),

        ModeloRow("No aplicados en este resumen", section=True),
        ModeloRow(
            "44 / 55 (prorata), 62-65 (regularización bienes inv.), "
            "67-68 (compensaciones anteriores), 77 (retenciones), "
            "108-111 (modificación bases), 122-125 (otras no sujetas)"
        ),
    ]
    return rows


def _modelo_130_rows(quarters: list[Modelo130Quarter]) -> list[ModeloRow]:
    """Build the displayable rows for the Modelo 130 sheet."""

    def col_values(attr: str) -> list[Decimal]:
        """[T1, T2, T3, T4, Anual] for a per-period attribute (sum = annual)."""
        vals: list[Decimal] = [getattr(q, attr) for q in quarters]
        return vals + [sum(vals, start=ZERO)]

    def cumulative_values(attr: str) -> list[Decimal]:
        """[T1, T2, T3, T4, Anual] for a cumulative attribute (Anual = T4)."""
        vals: list[Decimal] = [getattr(q, attr) for q in quarters]
        return vals + [vals[-1]]

    def casilla_07_values() -> list[Decimal]:
        vals: list[Decimal] = [q.casilla_07 for q in quarters]
        return vals + [sum(vals, start=ZERO)]  # annual = total paid across the year

    return [
        ModeloRow("Por período (delta del trimestre)", section=True),
        ModeloRow("Ingresos del período (base)", col_values("ingresos_periodo")),
        ModeloRow("Gastos del período (base deducible)", col_values("gastos_periodo")),
        ModeloRow("Retenciones soportadas del período", col_values("retenciones_periodo")),
        ModeloRow(""),

        ModeloRow("Casillas del modelo (acumulado)", section=True),
        ModeloRow("01  Ingresos computables", cumulative_values("ingresos_acum"), bold=True),
        ModeloRow("02  Gastos deducibles", cumulative_values("gastos_acum"), bold=True),
        ModeloRow("03  Rendimiento neto (01 - 02)", cumulative_values("rendimiento_neto"), bold=True),
        ModeloRow("04  20 % de casilla 03", cumulative_values("casilla_04")),
        ModeloRow("05  Pagos fraccionados anteriores", cumulative_values("casilla_05")),
        ModeloRow("06  Retenciones acumuladas", cumulative_values("retenciones_acum")),
        ModeloRow("07  Resultado (04 - 05 - 06)", casilla_07_values(), bold=True),
        ModeloRow(""),

        ModeloRow("No aplicados en este resumen", section=True),
        ModeloRow(
            "08–19 Minoraciones, rentas bajas, familia numerosa, "
            "actividades agrícolas/ganaderas/forestales/pesqueras"
        ),
    ]


def write_modelo_sheet(
    spreadsheet: gspread.Spreadsheet,
    title: str,
    rows: list[ModeloRow],
    value_cols: int = 5,  # T1, T2, T3, T4, Anual
) -> None:
    """Write a generic modelo summary sheet (not a native table).

    Layout:
        Row 1: warning banner (merged across all columns)
        Row 2: blank
        Row 3: column headers
        Row 4+: ModeloRow entries
    """
    total_cols = 1 + value_cols  # label + values
    num_rows = 3 + len(rows)

    ws = _ensure_worksheet(spreadsheet, title, num_rows, total_cols)

    # Build the raw 2-D data
    data: list[list[Any]] = [[""] * total_cols for _ in range(num_rows)]
    data[0][0] = MODELO_WARNING
    headers = ["Concepto"] + [f"T{i + 1}" for i in range(value_cols - 1)] + ["Anual"]
    data[2] = headers
    for i, row in enumerate(rows):
        r = 3 + i
        data[r][0] = row.label
        if row.values is not None:
            for j, v in enumerate(row.values):
                # Convert Decimal → float at the Sheets write boundary.
                data[r][1 + j] = _money(v)

    ws.update(data, value_input_option="RAW")

    # Merge the warning row across all columns.
    last_col_letter = _col_letter(total_cols)
    spreadsheet.batch_update({"requests": [
        {"mergeCells": {
            "range": {
                "sheetId": ws.id,
                "startRowIndex": 0, "endRowIndex": 1,
                "startColumnIndex": 0, "endColumnIndex": total_cols,
            },
            "mergeType": "MERGE_ALL",
        }},
        {"updateDimensionProperties": {
            "range": {"sheetId": ws.id, "dimension": "ROWS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 42},
            "fields": "pixelSize",
        }},
        {"updateDimensionProperties": {
            "range": {"sheetId": ws.id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 340},
            "fields": "pixelSize",
        }},
    ]})

    # Formatting: warning, headers, per-row styles, currency on value cells.
    fmt_pairs: list[tuple[str, CellFormat]] = [
        (f"A1:{last_col_letter}1", WARNING_FMT),
        (f"A3:{last_col_letter}3", MODELO_HEADER_FMT),
        (f"B4:{last_col_letter}{num_rows}", MODELO_CURRENCY_FMT),
    ]
    for i, row in enumerate(rows):
        r = 4 + i
        if row.section:
            fmt_pairs.append((f"A{r}:{last_col_letter}{r}", SECTION_FMT))
        elif row.bold:
            fmt_pairs.append((f"A{r}:{last_col_letter}{r}", TOTAL_FMT))

    format_cell_ranges(ws, fmt_pairs)


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
    parser.add_argument(
        "--self-assess-rate",
        type=Decimal,
        default=SELF_ASSESS_INTRA_EU_RATE,
        help=(
            "VAT rate used to self-assess reverse-charge transactions (intra-EU "
            f"acquisitions and non-EU services). Default: {SELF_ASSESS_INTRA_EU_RATE} %."
        ),
    )
    args = parser.parse_args()
    main(
        year=args.year,
        spreadsheet_id=args.spreadsheet_id,
        credentials_path=args.credentials,
        self_assess_rate=args.self_assess_rate,
    )


if __name__ == "__main__":
    cli()

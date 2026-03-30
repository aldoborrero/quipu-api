"""Export Quipu invoices (income & expenses) to a formatted Google Sheets spreadsheet.

Usage:
    python -m quipu.google_sheets_invoices [--year 2025] [--spreadsheet-id ID] [--credentials path/to/sa.json]

Requires: gspread, gspread_formatting
"""

from __future__ import annotations

import argparse
import datetime
import sys
from typing import Any

import gspread
from gspread_formatting import (
    BooleanCondition,
    BooleanRule,
    Border,
    Borders,
    CellFormat,
    Color,
    ConditionalFormatRule,
    NumberFormat,
    TextFormat,
    batch_updater,
    format_cell_range,
    get_conditional_format_rules,
    set_frozen,
)

from quipu import create_client
from quipu_client.api.invoices import get_invoices
from quipu_client.models.get_invoices_filterkind import GetInvoicesFilterkind
from quipu_client.models.get_invoices_include import GetInvoicesInclude
from quipu_client.types import UNSET

# ---------------------------------------------------------------------------
# Column definitions
# ---------------------------------------------------------------------------

INGRESOS_HEADERS = [
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

GASTOS_HEADERS = [
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

QUARTER_COLORS = {
    1: Color(1, 1, 1),  # white
    2: Color(1, 0.976, 0.769),  # #fff9c4
    3: Color(0.910, 0.961, 0.914),  # #e8f5e9
    4: Color(0.890, 0.949, 0.992),  # #e3f2fd
}

HEADER_BG = Color(0.827, 0.827, 0.827)  # #d3d3d3

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _val(attr: Any) -> Any:
    """Return None for UNSET values, otherwise the value itself."""
    if attr is UNSET or attr is None:
        return None
    return attr


def _to_float(s: Any) -> float | None:
    if s is UNSET or s is None:
        return None
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def _fmt_date(d: datetime.date | None) -> str:
    if d is None:
        return ""
    return d.strftime("%d/%m/%Y")


def _payment_status_label(status: Any) -> str:
    if status is UNSET or status is None:
        return ""
    mapping = {
        "paid": "Pagado",
        "due": "Pendiente de cobro",
        "pending": "Pendiente",
        "unpaid": "Impagado",
    }
    return mapping.get(str(status.value), str(status.value))


def _get_quarter(d: datetime.date) -> int:
    return (d.month - 1) // 3 + 1


# ---------------------------------------------------------------------------
# Fetch from Quipu API
# ---------------------------------------------------------------------------


def _fetch_all_invoices(client: Any, kind: GetInvoicesFilterkind, year: int) -> list[dict[str, Any]]:
    """Fetch all invoices for a given kind/year with pagination, including line items."""
    all_invoices: list[dict[str, Any]] = []
    for quarter in range(1, 5):
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
            if collection is None or isinstance(collection.data, type(UNSET)) or not collection.data:
                break

            # Build a map of included items by id
            items_map: dict[str, Any] = {}
            if not isinstance(collection.included, type(UNSET)) and collection.included:
                for inc in collection.included:
                    inc_id = _val(inc.id) if hasattr(inc, "id") else None
                    if inc_id:
                        items_map[str(inc_id)] = inc

            for inv in collection.data:
                attrs = inv.attributes if not isinstance(inv.attributes, type(UNSET)) else None
                rels = inv.relationships if not isinstance(inv.relationships, type(UNSET)) else None
                if attrs is None:
                    continue

                # Gather line-item data
                item_concepts: list[str] = []
                item_vat_percents: list[float] = []
                item_surcharges: list[float] = []

                if rels and not isinstance(rels.items, type(UNSET)) and rels.items:
                    items_data = _val(rels.items.data)
                    if items_data:
                        for item_ref in items_data:
                            item_id = _val(item_ref.id) if hasattr(item_ref, "id") else None
                            if item_id and str(item_id) in items_map:
                                item_obj = items_map[str(item_id)]
                                item_attrs = item_obj.attributes if hasattr(item_obj, "attributes") else None
                                if item_attrs:
                                    # concept / description
                                    concept = None
                                    if hasattr(item_attrs, "concept"):
                                        concept = _val(item_attrs.concept) if not isinstance(item_attrs, dict) else item_attrs.get("concept")
                                    if not concept and hasattr(item_attrs, "description"):
                                        concept = _val(item_attrs.description) if not isinstance(item_attrs, dict) else item_attrs.get("description")
                                    # Try additional_properties for untyped included items
                                    if not concept and hasattr(item_attrs, "additional_properties"):
                                        concept = item_attrs.additional_properties.get("concept") or item_attrs.additional_properties.get("description")
                                    if concept:
                                        item_concepts.append(str(concept))
                                    # vat_percent
                                    vp = None
                                    if hasattr(item_attrs, "vat_percent"):
                                        vp = _val(item_attrs.vat_percent) if not isinstance(item_attrs, dict) else item_attrs.get("vat_percent")
                                    if vp is None and hasattr(item_attrs, "additional_properties"):
                                        vp = item_attrs.additional_properties.get("vat_percent")
                                    if vp is not None:
                                        try:
                                            item_vat_percents.append(float(vp))
                                        except (ValueError, TypeError):
                                            pass
                                    # surcharge (equivalence surcharge)
                                    surcharge = None
                                    if hasattr(item_attrs, "additional_properties"):
                                        surcharge = item_attrs.additional_properties.get("equivalence_surcharge_amount") or item_attrs.additional_properties.get("surcharge_amount")
                                    if surcharge is not None:
                                        try:
                                            item_surcharges.append(float(surcharge))
                                        except (ValueError, TypeError):
                                            pass

                # Determine if rectificativa
                is_rectificativa = False
                if rels and not isinstance(rels.amended_invoice, type(UNSET)) and rels.amended_invoice:
                    amended_data = _val(rels.amended_invoice.data)
                    if amended_data is not None:
                        is_rectificativa = True

                issue_date = _val(attrs.issue_date)
                due_dates = _val(attrs.due_dates)
                due_date = due_dates[0] if due_dates else None
                paid_at = _val(attrs.paid_at)

                base = _to_float(attrs.total_amount_without_taxes)
                vat_amount = _to_float(attrs.vat_amount)
                total = _to_float(attrs.total_amount)

                vat_pct = int(item_vat_percents[0]) if item_vat_percents else (0 if vat_amount == 0 or vat_amount is None else None)
                if vat_pct is None and base and vat_amount:
                    # Infer from amounts
                    try:
                        vat_pct = round(vat_amount / base * 100)
                    except ZeroDivisionError:
                        vat_pct = 0

                surcharge_total = sum(item_surcharges) if item_surcharges else 0.0

                # For income invoices: recipient is the client; for expenses: issuer is the supplier
                if kind == GetInvoicesFilterkind.INCOME:
                    contact_name = _val(attrs.recipient_name) or ""
                    contact_tax_id = _val(attrs.recipient_tax_id) or ""
                    contact_zip = _val(attrs.recipient_zip_code) or ""
                    # "Cuenta de cliente" — use accounting_category from relationship if available
                    contact_account = ""
                    if rels and not isinstance(rels.accounting_subcategory, type(UNSET)) and rels.accounting_subcategory:
                        sub_data = _val(rels.accounting_subcategory.data)
                        if sub_data and hasattr(sub_data, "id"):
                            contact_account = str(_val(sub_data.id) or "")
                else:
                    contact_name = _val(attrs.issuing_name) or ""
                    contact_tax_id = _val(attrs.issuing_tax_id) or ""
                    contact_zip = _val(attrs.issuing_zip_code) or ""
                    contact_account = ""

                record = {
                    "issue_date": issue_date,
                    "due_date": due_date,
                    "paid_at": paid_at,
                    "number": _val(attrs.number) or "",
                    "invoice_number": _val(attrs.number) or "",
                    "kind_label": "Factura" if not is_rectificativa else "Rectificativa",
                    "contact_name": contact_name,
                    "contact_account": contact_account,
                    "contact_tax_id": contact_tax_id,
                    "contact_zip": contact_zip,
                    "concept": " | ".join(item_concepts) if item_concepts else "",
                    "payment_status": _payment_status_label(attrs.payment_status),
                    "is_rectificativa": is_rectificativa,
                    "base": base,
                    "vat_amount": vat_amount,
                    "vat_pct": vat_pct if vat_pct is not None else 0,
                    "surcharge": surcharge_total,
                    "total": total,
                    "quarter": _get_quarter(issue_date) if issue_date else 0,
                }
                all_invoices.append(record)

            # Pagination
            meta = _val(collection.meta)
            if meta:
                pagination = _val(meta.pagination_info)
                if pagination:
                    total_pages = _val(pagination.total_pages) or 1
                    if page >= total_pages:
                        break
            page += 1

    # Sort by issue_date ascending
    all_invoices.sort(key=lambda r: r["issue_date"] or datetime.date.min)
    return all_invoices


def fetch_ingresos(year: int) -> list[dict[str, Any]]:
    with create_client() as client:
        return _fetch_all_invoices(client, GetInvoicesFilterkind.INCOME, year)


def fetch_gastos(year: int) -> list[dict[str, Any]]:
    with create_client() as client:
        return _fetch_all_invoices(client, GetInvoicesFilterkind.EXPENSES, year)


# ---------------------------------------------------------------------------
# Filter
# ---------------------------------------------------------------------------


def filter_by_quarter(entries: list[dict[str, Any]], quarter: int) -> list[dict[str, Any]]:
    return [e for e in entries if e.get("quarter") == quarter]


# ---------------------------------------------------------------------------
# Build row data
# ---------------------------------------------------------------------------


def _ingreso_row(r: dict[str, Any]) -> list[Any]:
    """Build a single row for the Ingresos sheet."""
    vat = r["vat_amount"]
    surcharge = r["surcharge"]
    return [
        _fmt_date(r["issue_date"]),
        _fmt_date(r["due_date"]),
        _fmt_date(r["paid_at"]),
        r["number"],
        r["invoice_number"],
        r["kind_label"],
        r["contact_name"],
        r["contact_account"],
        r["contact_tax_id"],
        r["contact_zip"],
        r["concept"],
        r["payment_status"],
        "Sí" if r["is_rectificativa"] else "-",
        r["base"] if r["base"] is not None else 0,
        vat if vat and vat != 0 else "-",
        r["vat_pct"],
        surcharge if surcharge and surcharge != 0 else "-",
    ]


def _gasto_row(r: dict[str, Any]) -> list[Any]:
    """Build a single row for the Gastos sheet."""
    vat = r["vat_amount"]
    return [
        _fmt_date(r["issue_date"]),
        r["invoice_number"],
        r["contact_name"],
        r["contact_account"],
        r["contact_tax_id"],
        r["base"] if r["base"] is not None else 0,
        vat if vat and vat != 0 else "-",
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
    all_data = [headers] + rows
    if all_data:
        worksheet.update(all_data, value_input_option="RAW")


def format_sheet(
    worksheet: gspread.Worksheet,
    tipo: str,
    num_rows: int,
    quarter_data: list[int] | None = None,
) -> None:
    """Apply visual formatting to a worksheet.

    Args:
        worksheet: the gspread Worksheet
        tipo: "ingresos" or "gastos"
        num_rows: number of data rows (excluding header)
        quarter_data: list of quarter numbers (1-4) per data row, for row coloring on ingresos
    """
    if num_rows == 0:
        # Just format header
        set_frozen(worksheet, rows=1)
        return

    total_rows = num_rows + 1  # +1 for header
    num_cols = len(INGRESOS_HEADERS) if tipo == "ingresos" else len(GASTOS_HEADERS)

    # --- Header formatting ---
    header_fmt = CellFormat(
        backgroundColor=HEADER_BG,
        textFormat=TextFormat(bold=True, foregroundColor=Color(0, 0, 0)),
        horizontalAlignment="CENTER",
    )
    format_cell_range(worksheet, f"A1:{_col_letter(num_cols)}1", header_fmt)
    set_frozen(worksheet, rows=1)

    # --- Border for all cells with data ---
    thin_border = Border("SOLID", Color(0.8, 0.8, 0.8))
    border_fmt = CellFormat(
        borders=Borders(top=thin_border, bottom=thin_border, left=thin_border, right=thin_border)
    )
    format_cell_range(worksheet, f"A1:{_col_letter(num_cols)}{total_rows}", border_fmt)

    # --- Date columns ---
    date_fmt = CellFormat(
        numberFormat=NumberFormat(type="DATE", pattern="dd/MM/yyyy"),
        horizontalAlignment="LEFT",
    )
    if tipo == "ingresos":
        # Columns A, B, C (dates)
        for col in ["A", "B", "C"]:
            format_cell_range(worksheet, f"{col}2:{col}{total_rows}", date_fmt)
    else:
        # Column A (date)
        format_cell_range(worksheet, f"A2:A{total_rows}", date_fmt)

    # --- Currency columns ---
    currency_fmt = CellFormat(
        numberFormat=NumberFormat(type="NUMBER", pattern='#,##0.00 "€"'),
        horizontalAlignment="RIGHT",
    )
    if tipo == "ingresos":
        # N=Base(14), O=IVA(15), Q=Recargo(17)
        format_cell_range(worksheet, f"N2:N{total_rows}", currency_fmt)
        # IVA and Recargo: only format cells that have numeric values (not "-")
        # We still apply the currency format; the "-" string cells will show as-is
        format_cell_range(worksheet, f"O2:O{total_rows}", currency_fmt)
        format_cell_range(worksheet, f"Q2:Q{total_rows}", currency_fmt)
        # IVA (%) - P column, integer right-aligned
        pct_fmt = CellFormat(
            numberFormat=NumberFormat(type="NUMBER", pattern="0"),
            horizontalAlignment="RIGHT",
        )
        format_cell_range(worksheet, f"P2:P{total_rows}", pct_fmt)
    else:
        # F=Base(6), G=IVA(7), I=Total(9)
        format_cell_range(worksheet, f"F2:F{total_rows}", currency_fmt)
        format_cell_range(worksheet, f"G2:G{total_rows}", currency_fmt)
        format_cell_range(worksheet, f"I2:I{total_rows}", currency_fmt)
        # H=IVA (%)
        pct_fmt = CellFormat(
            numberFormat=NumberFormat(type="NUMBER", pattern="0"),
            horizontalAlignment="RIGHT",
        )
        format_cell_range(worksheet, f"H2:H{total_rows}", pct_fmt)

    # --- Concepto column (K) in ingresos: wide + wrap ---
    if tipo == "ingresos":
        wrap_fmt = CellFormat(wrapStrategy="WRAP")
        format_cell_range(worksheet, f"K2:K{total_rows}", wrap_fmt)

    # --- Row coloring by quarter (ingresos master sheet only) ---
    if tipo == "ingresos" and quarter_data:
        for i, q in enumerate(quarter_data):
            row_num = i + 2  # 1-indexed, header is row 1
            color = QUARTER_COLORS.get(q)
            if color and q != 1:  # Q1 is white (default), skip
                row_range = f"A{row_num}:{_col_letter(num_cols)}{row_num}"
                format_cell_range(worksheet, row_range, CellFormat(backgroundColor=color))

    # --- Column widths ---
    requests = []
    sheet_id = worksheet.id
    if tipo == "ingresos":
        # K (index 10) = Concepto, fixed 300px
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": 10,
                    "endIndex": 11,
                },
                "properties": {"pixelSize": 300},
                "fields": "pixelSize",
            }
        })
    # Auto-resize all other columns
    requests.append({
        "autoResizeDimensions": {
            "dimensions": {
                "sheetId": sheet_id,
                "dimension": "COLUMNS",
                "startIndex": 0,
                "endIndex": num_cols,
            }
        }
    })
    if requests:
        worksheet.spreadsheet.batch_update({"requests": requests})


def _col_letter(n: int) -> str:
    """Convert 1-based column number to letter (1=A, 26=Z, 27=AA)."""
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------


def main(year: int | None = None, spreadsheet_id: str | None = None, credentials_path: str | None = None) -> None:
    if year is None:
        year = datetime.date.today().year

    print(f"Fetching ingresos for {year}...")
    ingresos = fetch_ingresos(year)
    print(f"  → {len(ingresos)} facturas emitidas")

    print(f"Fetching gastos for {year}...")
    gastos = fetch_gastos(year)
    print(f"  → {len(gastos)} facturas recibidas")

    # --- Connect to Google Sheets ---
    if credentials_path:
        gc = gspread.service_account(filename=credentials_path)
    else:
        gc = gspread.service_account()

    if spreadsheet_id:
        spreadsheet = gc.open_by_key(spreadsheet_id)
    else:
        title = f"Quipu Facturas {year}"
        try:
            spreadsheet = gc.open(title)
        except gspread.SpreadsheetNotFound:
            spreadsheet = gc.create(title)
            print(f"Created new spreadsheet: {title}")

    print(f"Writing to spreadsheet: {spreadsheet.title}")

    # --- Build row data ---
    ingreso_rows = [_ingreso_row(r) for r in ingresos]
    gasto_rows = [_gasto_row(r) for r in gastos]
    ingreso_quarters = [r["quarter"] for r in ingresos]

    # --- Master sheets ---
    sheet_configs = []

    # Ingresos master
    ws = _ensure_worksheet(spreadsheet, "Ingresos", len(ingreso_rows) + 1, len(INGRESOS_HEADERS))
    write_sheet(ws, ingreso_rows, INGRESOS_HEADERS)
    sheet_configs.append((ws, "ingresos", len(ingreso_rows), ingreso_quarters))

    # Gastos master
    ws = _ensure_worksheet(spreadsheet, "Gastos", len(gasto_rows) + 1, len(GASTOS_HEADERS))
    write_sheet(ws, gasto_rows, GASTOS_HEADERS)
    sheet_configs.append((ws, "gastos", len(gasto_rows), None))

    # --- Quarterly sheets ---
    for q in range(1, 5):
        # Ingresos Tx
        q_ingresos = filter_by_quarter(ingresos, q)
        q_rows = [_ingreso_row(r) for r in q_ingresos]
        ws = _ensure_worksheet(spreadsheet, f"Ingresos T{q}", len(q_rows) + 1, len(INGRESOS_HEADERS))
        write_sheet(ws, q_rows, INGRESOS_HEADERS)
        sheet_configs.append((ws, "ingresos", len(q_rows), None))

        # Gastos Tx
        q_gastos = filter_by_quarter(gastos, q)
        q_rows = [_gasto_row(r) for r in q_gastos]
        ws = _ensure_worksheet(spreadsheet, f"Gastos T{q}", len(q_rows) + 1, len(GASTOS_HEADERS))
        write_sheet(ws, q_rows, GASTOS_HEADERS)
        sheet_configs.append((ws, "gastos", len(q_rows), None))

    # --- Remove default "Sheet1" if it exists ---
    try:
        default_sheet = spreadsheet.worksheet("Sheet1")
        spreadsheet.del_worksheet(default_sheet)
    except gspread.WorksheetNotFound:
        pass

    # --- Apply formatting to all sheets ---
    print("Applying formatting...")
    for ws, tipo, num_rows, quarters in sheet_configs:
        format_sheet(ws, tipo, num_rows, quarters)

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

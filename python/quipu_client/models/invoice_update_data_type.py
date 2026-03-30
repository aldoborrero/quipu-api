from enum import Enum


class InvoiceUpdateDataType(str, Enum):
    INVOICES = "invoices"

    def __str__(self) -> str:
        return str(self.value)

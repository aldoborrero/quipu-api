from enum import Enum


class InvoiceRelationshipsAmendedInvoiceDataType0Type(str, Enum):
    INVOICES = "invoices"

    def __str__(self) -> str:
        return str(self.value)

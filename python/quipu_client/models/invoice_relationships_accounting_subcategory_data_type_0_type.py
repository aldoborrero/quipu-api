from enum import Enum


class InvoiceRelationshipsAccountingSubcategoryDataType0Type(str, Enum):
    ACCOUNTING_SUBCATEGORIES = "accounting_subcategories"

    def __str__(self) -> str:
        return str(self.value)

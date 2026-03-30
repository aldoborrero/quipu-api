from enum import Enum

class SimplifiedInvoiceWritableAttributesKind(str, Enum):
    EXPENSES = "expenses"
    INCOME = "income"

    def __str__(self) -> str:
        return str(self.value)

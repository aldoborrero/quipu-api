from enum import Enum


class AccountingSubcategoryDataType(str, Enum):
    ACCOUNTING_SUBCATEGORIES = "accounting_subcategories"

    def __str__(self) -> str:
        return str(self.value)

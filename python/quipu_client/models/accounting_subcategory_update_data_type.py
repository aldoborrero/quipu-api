from enum import Enum


class AccountingSubcategoryUpdateDataType(str, Enum):
    ACCOUNTING_SUBCATEGORIES = "accounting_subcategories"

    def __str__(self) -> str:
        return str(self.value)

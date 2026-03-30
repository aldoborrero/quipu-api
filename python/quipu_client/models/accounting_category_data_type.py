from enum import Enum


class AccountingCategoryDataType(str, Enum):
    ACCOUNTING_CATEGORIES = "accounting_categories"

    def __str__(self) -> str:
        return str(self.value)

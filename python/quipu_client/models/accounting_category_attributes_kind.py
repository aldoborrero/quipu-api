from enum import Enum


class AccountingCategoryAttributesKind(str, Enum):
    ASSETS = "assets"
    EXPENSES = "expenses"
    INCOME = "income"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class AdditionalIncomeAttributesKind(str, Enum):
    EXPENSES = "expenses"
    INCOME = "income"

    def __str__(self) -> str:
        return str(self.value)

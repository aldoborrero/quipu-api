from enum import Enum

class ListContactsSort(str, Enum):
    NAME = "name"
    TOTAL_PAID_EXPENSES = "total_paid_expenses"
    TOTAL_PAID_INCOME = "total_paid_income"
    TOTAL_UNPAID_EXPENSES = "total_unpaid_expenses"
    TOTAL_UNPAID_INCOME = "total_unpaid_income"
    VALUE_1 = "-name"
    VALUE_3 = "-total_paid_income"
    VALUE_5 = "-total_unpaid_income"
    VALUE_7 = "-total_paid_expenses"
    VALUE_9 = "-total_unpaid_expenses"

    def __str__(self) -> str:
        return str(self.value)

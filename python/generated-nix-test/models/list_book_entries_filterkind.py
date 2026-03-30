from enum import Enum

class ListBookEntriesFilterkind(str, Enum):
    EXPENSES = "expenses"
    INCOME = "income"

    def __str__(self) -> str:
        return str(self.value)

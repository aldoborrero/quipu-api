from enum import Enum


class GetTicketsFilterkind(str, Enum):
    ASSETS = "assets"
    CLIENT = "client"
    EMPLOYEE = "employee"
    EXPENSES = "expenses"
    INCOME = "income"
    SUPPLIER = "supplier"

    def __str__(self) -> str:
        return str(self.value)

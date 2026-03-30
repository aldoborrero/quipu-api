from enum import Enum


class GetNumberingSeriesFilterapplicableTo(str, Enum):
    BUDGETS = "budgets"
    INVOICES = "invoices"
    TICKETS = "tickets"

    def __str__(self) -> str:
        return str(self.value)

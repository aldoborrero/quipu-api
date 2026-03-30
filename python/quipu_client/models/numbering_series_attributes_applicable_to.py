from enum import Enum


class NumberingSeriesAttributesApplicableTo(str, Enum):
    INVOICES = "invoices"
    TICKETS = "tickets"

    def __str__(self) -> str:
        return str(self.value)

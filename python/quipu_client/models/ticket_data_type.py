from enum import Enum


class TicketDataType(str, Enum):
    TICKETS = "tickets"

    def __str__(self) -> str:
        return str(self.value)

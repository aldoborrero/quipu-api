from enum import Enum


class TicketCreateDataType(str, Enum):
    TICKETS = "tickets"

    def __str__(self) -> str:
        return str(self.value)

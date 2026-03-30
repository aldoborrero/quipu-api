from enum import Enum


class TicketRelationshipsAmendedTicketDataType0Type(str, Enum):
    TICKETS = "tickets"

    def __str__(self) -> str:
        return str(self.value)

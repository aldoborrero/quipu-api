from enum import Enum


class GetTicketInclude(str, Enum):
    ITEMS = "items"

    def __str__(self) -> str:
        return str(self.value)

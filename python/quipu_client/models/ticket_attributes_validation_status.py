from enum import Enum


class TicketAttributesValidationStatus(str, Enum):
    PENDING = "pending"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class InvoiceAttributesValidationStatus(str, Enum):
    PENDING = "pending"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class InvoiceWritableAttributesExemptReason(str, Enum):
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"

    def __str__(self) -> str:
        return str(self.value)

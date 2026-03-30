from enum import Enum

class InvoiceWritableAttributesCollectionType(str, Enum):
    NONE = "none"
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    R4 = "R4"

    def __str__(self) -> str:
        return str(self.value)

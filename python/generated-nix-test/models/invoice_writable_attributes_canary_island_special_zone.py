from enum import Enum

class InvoiceWritableAttributesCanaryIslandSpecialZone(str, Enum):
    R1 = "R1"

    def __str__(self) -> str:
        return str(self.value)

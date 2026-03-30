from enum import Enum

class InvoiceAttributesStage(str, Enum):
    DRAFT = "draft"
    FINAL = "final"

    def __str__(self) -> str:
        return str(self.value)

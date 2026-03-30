from enum import Enum


class ItemAttributesKind(str, Enum):
    ASSETS = "assets"
    CURRENT = "current"
    REIMBURSEMENT = "reimbursement"

    def __str__(self) -> str:
        return str(self.value)

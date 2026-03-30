from enum import Enum


class InvoiceRelationshipsNumerationDataType0Type(str, Enum):
    NUMBERING_SERIES = "numbering_series"

    def __str__(self) -> str:
        return str(self.value)

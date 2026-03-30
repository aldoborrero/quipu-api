from enum import Enum


class PaysheetRelationshipsNumerationDataType0Type(str, Enum):
    NUMBERING_SERIES = "numbering_series"

    def __str__(self) -> str:
        return str(self.value)

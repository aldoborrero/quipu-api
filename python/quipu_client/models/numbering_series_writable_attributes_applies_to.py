from enum import Enum

class NumberingSeriesWritableAttributesAppliesTo(str, Enum):
    EXISTING_DOCUMENTS = "existing_documents"
    NEW_DOCUMENTS = "new_documents"

    def __str__(self) -> str:
        return str(self.value)

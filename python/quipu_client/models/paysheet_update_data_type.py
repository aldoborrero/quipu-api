from enum import Enum


class PaysheetUpdateDataType(str, Enum):
    PAYSHEETS = "paysheets"

    def __str__(self) -> str:
        return str(self.value)

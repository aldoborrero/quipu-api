from enum import Enum


class PaysheetDataType(str, Enum):
    PAYSHEETS = "paysheets"

    def __str__(self) -> str:
        return str(self.value)

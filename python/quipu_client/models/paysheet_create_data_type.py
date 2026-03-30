from enum import Enum


class PaysheetCreateDataType(str, Enum):
    PAYSHEETS = "paysheets"

    def __str__(self) -> str:
        return str(self.value)

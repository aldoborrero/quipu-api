from enum import Enum

class ListBookEntriesSort(str, Enum):
    COUNTERPART_NAME = "counterpart_name"
    ISSUE_DATE = "issue_date"
    NUMBER = "number"
    TOTAL_AMOUNT = "total_amount"
    TOTAL_AMOUNT_WITHOUT_TAXES = "total_amount_without_taxes"
    VALUE_1 = "-number"
    VALUE_3 = "-issue_date"
    VALUE_5 = "-counterpart_name"
    VALUE_7 = "-total_amount"
    VALUE_9 = "-total_amount_without_taxes"

    def __str__(self) -> str:
        return str(self.value)

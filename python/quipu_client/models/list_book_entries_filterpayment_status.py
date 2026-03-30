from enum import Enum

class ListBookEntriesFilterpaymentStatus(str, Enum):
    PAID = "paid"
    PARTIALLY_PAID = "partially_paid"
    UNPAID = "unpaid"

    def __str__(self) -> str:
        return str(self.value)

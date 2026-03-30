from enum import Enum


class GetInvoicesFilterpaymentStatus(str, Enum):
    DUE = "due"
    PAID = "paid"
    PENDING = "pending"
    UNPAID = "unpaid"

    def __str__(self) -> str:
        return str(self.value)

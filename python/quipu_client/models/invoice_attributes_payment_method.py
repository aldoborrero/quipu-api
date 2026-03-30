from enum import Enum


class InvoiceAttributesPaymentMethod(str, Enum):
    BANK_CARD = "bank_card"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"
    CHECK = "check"
    DIRECT_DEBIT = "direct_debit"
    FACTORING = "factoring"
    PAYPAL = "paypal"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ItemInvoiceUpdateType(str, Enum):
    BOOK_ENTRY_ITEMS = "book_entry_items"

    def __str__(self) -> str:
        return str(self.value)

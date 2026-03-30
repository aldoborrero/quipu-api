from enum import Enum


class AttachmentRelationshipsBookEntryDataType(str, Enum):
    INVOICES = "invoices"
    PAYSHEETS = "paysheets"
    TICKETS = "tickets"

    def __str__(self) -> str:
        return str(self.value)

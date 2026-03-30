from enum import Enum


class InvoiceRelationshipsContactDataType(str, Enum):
    CONTACTS = "contacts"

    def __str__(self) -> str:
        return str(self.value)

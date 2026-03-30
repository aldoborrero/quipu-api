from enum import Enum


class ContactCreateDataType(str, Enum):
    CONTACTS = "contacts"

    def __str__(self) -> str:
        return str(self.value)

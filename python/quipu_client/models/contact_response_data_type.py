from enum import Enum


class ContactResponseDataType(str, Enum):
    CONTACTS = "contacts"

    def __str__(self) -> str:
        return str(self.value)

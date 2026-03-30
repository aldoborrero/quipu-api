from enum import Enum

class ListContactsFilterkind(str, Enum):
    CLIENT = "client"
    EMPLOYEE = "employee"
    SUPPLIER = "supplier"

    def __str__(self) -> str:
        return str(self.value)

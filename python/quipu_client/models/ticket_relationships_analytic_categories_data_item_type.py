from enum import Enum


class TicketRelationshipsAnalyticCategoriesDataItemType(str, Enum):
    ANALYTIC_CATEGORIES = "analytic_categories"

    def __str__(self) -> str:
        return str(self.value)

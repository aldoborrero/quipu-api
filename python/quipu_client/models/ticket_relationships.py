from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ticket_relationships_accounting_category import TicketRelationshipsAccountingCategory
    from ..models.ticket_relationships_accounting_subcategory import TicketRelationshipsAccountingSubcategory
    from ..models.ticket_relationships_amended_ticket import TicketRelationshipsAmendedTicket
    from ..models.ticket_relationships_amending_tickets import TicketRelationshipsAmendingTickets
    from ..models.ticket_relationships_analytic_categories import TicketRelationshipsAnalyticCategories
    from ..models.ticket_relationships_items import TicketRelationshipsItems
    from ..models.ticket_relationships_numeration import TicketRelationshipsNumeration


T = TypeVar("T", bound="TicketRelationships")


@_attrs_define
class TicketRelationships:
    """
    Attributes:
        accounting_category (TicketRelationshipsAccountingCategory | Unset):
        accounting_subcategory (TicketRelationshipsAccountingSubcategory | Unset):
        numeration (TicketRelationshipsNumeration | Unset):
        analytic_categories (TicketRelationshipsAnalyticCategories | Unset):
        items (TicketRelationshipsItems | Unset):
        amended_ticket (TicketRelationshipsAmendedTicket | Unset):
        amending_tickets (TicketRelationshipsAmendingTickets | Unset):
    """

    accounting_category: TicketRelationshipsAccountingCategory | Unset = UNSET
    accounting_subcategory: TicketRelationshipsAccountingSubcategory | Unset = UNSET
    numeration: TicketRelationshipsNumeration | Unset = UNSET
    analytic_categories: TicketRelationshipsAnalyticCategories | Unset = UNSET
    items: TicketRelationshipsItems | Unset = UNSET
    amended_ticket: TicketRelationshipsAmendedTicket | Unset = UNSET
    amending_tickets: TicketRelationshipsAmendingTickets | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounting_category, Unset):
            accounting_category = self.accounting_category.to_dict()

        accounting_subcategory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounting_subcategory, Unset):
            accounting_subcategory = self.accounting_subcategory.to_dict()

        numeration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.numeration, Unset):
            numeration = self.numeration.to_dict()

        analytic_categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analytic_categories, Unset):
            analytic_categories = self.analytic_categories.to_dict()

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        amended_ticket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amended_ticket, Unset):
            amended_ticket = self.amended_ticket.to_dict()

        amending_tickets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amending_tickets, Unset):
            amending_tickets = self.amending_tickets.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounting_category is not UNSET:
            field_dict["accounting_category"] = accounting_category
        if accounting_subcategory is not UNSET:
            field_dict["accounting_subcategory"] = accounting_subcategory
        if numeration is not UNSET:
            field_dict["numeration"] = numeration
        if analytic_categories is not UNSET:
            field_dict["analytic_categories"] = analytic_categories
        if items is not UNSET:
            field_dict["items"] = items
        if amended_ticket is not UNSET:
            field_dict["amended_ticket"] = amended_ticket
        if amending_tickets is not UNSET:
            field_dict["amending_tickets"] = amending_tickets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ticket_relationships_accounting_category import TicketRelationshipsAccountingCategory
        from ..models.ticket_relationships_accounting_subcategory import TicketRelationshipsAccountingSubcategory
        from ..models.ticket_relationships_amended_ticket import TicketRelationshipsAmendedTicket
        from ..models.ticket_relationships_amending_tickets import TicketRelationshipsAmendingTickets
        from ..models.ticket_relationships_analytic_categories import TicketRelationshipsAnalyticCategories
        from ..models.ticket_relationships_items import TicketRelationshipsItems
        from ..models.ticket_relationships_numeration import TicketRelationshipsNumeration

        d = dict(src_dict)
        _accounting_category = d.pop("accounting_category", UNSET)
        accounting_category: TicketRelationshipsAccountingCategory | Unset
        if isinstance(_accounting_category, Unset):
            accounting_category = UNSET
        else:
            accounting_category = TicketRelationshipsAccountingCategory.from_dict(_accounting_category)

        _accounting_subcategory = d.pop("accounting_subcategory", UNSET)
        accounting_subcategory: TicketRelationshipsAccountingSubcategory | Unset
        if isinstance(_accounting_subcategory, Unset):
            accounting_subcategory = UNSET
        else:
            accounting_subcategory = TicketRelationshipsAccountingSubcategory.from_dict(_accounting_subcategory)

        _numeration = d.pop("numeration", UNSET)
        numeration: TicketRelationshipsNumeration | Unset
        if isinstance(_numeration, Unset):
            numeration = UNSET
        else:
            numeration = TicketRelationshipsNumeration.from_dict(_numeration)

        _analytic_categories = d.pop("analytic_categories", UNSET)
        analytic_categories: TicketRelationshipsAnalyticCategories | Unset
        if isinstance(_analytic_categories, Unset):
            analytic_categories = UNSET
        else:
            analytic_categories = TicketRelationshipsAnalyticCategories.from_dict(_analytic_categories)

        _items = d.pop("items", UNSET)
        items: TicketRelationshipsItems | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = TicketRelationshipsItems.from_dict(_items)

        _amended_ticket = d.pop("amended_ticket", UNSET)
        amended_ticket: TicketRelationshipsAmendedTicket | Unset
        if isinstance(_amended_ticket, Unset):
            amended_ticket = UNSET
        else:
            amended_ticket = TicketRelationshipsAmendedTicket.from_dict(_amended_ticket)

        _amending_tickets = d.pop("amending_tickets", UNSET)
        amending_tickets: TicketRelationshipsAmendingTickets | Unset
        if isinstance(_amending_tickets, Unset):
            amending_tickets = UNSET
        else:
            amending_tickets = TicketRelationshipsAmendingTickets.from_dict(_amending_tickets)

        ticket_relationships = cls(
            accounting_category=accounting_category,
            accounting_subcategory=accounting_subcategory,
            numeration=numeration,
            analytic_categories=analytic_categories,
            items=items,
            amended_ticket=amended_ticket,
            amending_tickets=amending_tickets,
        )

        ticket_relationships.additional_properties = d
        return ticket_relationships

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

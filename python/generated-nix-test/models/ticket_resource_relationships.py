from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.relationship_linkage_array import RelationshipLinkageArray
  from ..models.relationship_linkage_type_0 import RelationshipLinkageType0





T = TypeVar("T", bound="TicketResourceRelationships")



@_attrs_define
class TicketResourceRelationships:
    """ 
        Attributes:
            numeration (None | RelationshipLinkageType0 | Unset):
            items (RelationshipLinkageArray | Unset):
            accounting_category (None | RelationshipLinkageType0 | Unset):
            accounting_subcategory (None | RelationshipLinkageType0 | Unset):
            amending_tickets (RelationshipLinkageArray | Unset):
            amended_ticket (None | RelationshipLinkageType0 | Unset):
     """

    numeration: None | RelationshipLinkageType0 | Unset = UNSET
    items: RelationshipLinkageArray | Unset = UNSET
    accounting_category: None | RelationshipLinkageType0 | Unset = UNSET
    accounting_subcategory: None | RelationshipLinkageType0 | Unset = UNSET
    amending_tickets: RelationshipLinkageArray | Unset = UNSET
    amended_ticket: None | RelationshipLinkageType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.relationship_linkage_array import RelationshipLinkageArray
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        numeration: dict[str, Any] | None | Unset
        if isinstance(self.numeration, Unset):
            numeration = UNSET
        elif isinstance(self.numeration, RelationshipLinkageType0):
            numeration = self.numeration.to_dict()
        else:
            numeration = self.numeration

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        accounting_category: dict[str, Any] | None | Unset
        if isinstance(self.accounting_category, Unset):
            accounting_category = UNSET
        elif isinstance(self.accounting_category, RelationshipLinkageType0):
            accounting_category = self.accounting_category.to_dict()
        else:
            accounting_category = self.accounting_category

        accounting_subcategory: dict[str, Any] | None | Unset
        if isinstance(self.accounting_subcategory, Unset):
            accounting_subcategory = UNSET
        elif isinstance(self.accounting_subcategory, RelationshipLinkageType0):
            accounting_subcategory = self.accounting_subcategory.to_dict()
        else:
            accounting_subcategory = self.accounting_subcategory

        amending_tickets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amending_tickets, Unset):
            amending_tickets = self.amending_tickets.to_dict()

        amended_ticket: dict[str, Any] | None | Unset
        if isinstance(self.amended_ticket, Unset):
            amended_ticket = UNSET
        elif isinstance(self.amended_ticket, RelationshipLinkageType0):
            amended_ticket = self.amended_ticket.to_dict()
        else:
            amended_ticket = self.amended_ticket


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if numeration is not UNSET:
            field_dict["numeration"] = numeration
        if items is not UNSET:
            field_dict["items"] = items
        if accounting_category is not UNSET:
            field_dict["accounting_category"] = accounting_category
        if accounting_subcategory is not UNSET:
            field_dict["accounting_subcategory"] = accounting_subcategory
        if amending_tickets is not UNSET:
            field_dict["amending_tickets"] = amending_tickets
        if amended_ticket is not UNSET:
            field_dict["amended_ticket"] = amended_ticket

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relationship_linkage_array import RelationshipLinkageArray
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        d = dict(src_dict)
        def _parse_numeration(data: object) -> None | RelationshipLinkageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_relationship_linkage_type_0 = RelationshipLinkageType0.from_dict(data)



                return componentsschemas_relationship_linkage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RelationshipLinkageType0 | Unset, data)

        numeration = _parse_numeration(d.pop("numeration", UNSET))


        _items = d.pop("items", UNSET)
        items: RelationshipLinkageArray | Unset
        if isinstance(_items,  Unset):
            items = UNSET
        else:
            items = RelationshipLinkageArray.from_dict(_items)




        def _parse_accounting_category(data: object) -> None | RelationshipLinkageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_relationship_linkage_type_0 = RelationshipLinkageType0.from_dict(data)



                return componentsschemas_relationship_linkage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RelationshipLinkageType0 | Unset, data)

        accounting_category = _parse_accounting_category(d.pop("accounting_category", UNSET))


        def _parse_accounting_subcategory(data: object) -> None | RelationshipLinkageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_relationship_linkage_type_0 = RelationshipLinkageType0.from_dict(data)



                return componentsschemas_relationship_linkage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RelationshipLinkageType0 | Unset, data)

        accounting_subcategory = _parse_accounting_subcategory(d.pop("accounting_subcategory", UNSET))


        _amending_tickets = d.pop("amending_tickets", UNSET)
        amending_tickets: RelationshipLinkageArray | Unset
        if isinstance(_amending_tickets,  Unset):
            amending_tickets = UNSET
        else:
            amending_tickets = RelationshipLinkageArray.from_dict(_amending_tickets)




        def _parse_amended_ticket(data: object) -> None | RelationshipLinkageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_relationship_linkage_type_0 = RelationshipLinkageType0.from_dict(data)



                return componentsschemas_relationship_linkage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RelationshipLinkageType0 | Unset, data)

        amended_ticket = _parse_amended_ticket(d.pop("amended_ticket", UNSET))


        ticket_resource_relationships = cls(
            numeration=numeration,
            items=items,
            accounting_category=accounting_category,
            accounting_subcategory=accounting_subcategory,
            amending_tickets=amending_tickets,
            amended_ticket=amended_ticket,
        )


        ticket_resource_relationships.additional_properties = d
        return ticket_resource_relationships

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

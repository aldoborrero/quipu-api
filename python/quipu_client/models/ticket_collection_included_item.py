from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ticket_collection_included_item_attributes import TicketCollectionIncludedItemAttributes


T = TypeVar("T", bound="TicketCollectionIncludedItem")


@_attrs_define
class TicketCollectionIncludedItem:
    """
    Attributes:
        id (str | Unset):
        type_ (str | Unset):
        attributes (TicketCollectionIncludedItemAttributes | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: TicketCollectionIncludedItemAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ticket_collection_included_item_attributes import TicketCollectionIncludedItemAttributes

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: TicketCollectionIncludedItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TicketCollectionIncludedItemAttributes.from_dict(_attributes)

        ticket_collection_included_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        ticket_collection_included_item.additional_properties = d
        return ticket_collection_included_item

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

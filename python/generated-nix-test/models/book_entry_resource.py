from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.book_entry_attributes import BookEntryAttributes
  from ..models.book_entry_resource_relationships import BookEntryResourceRelationships





T = TypeVar("T", bound="BookEntryResource")



@_attrs_define
class BookEntryResource:
    """ 
        Attributes:
            id (str | Unset):
            type_ (str | Unset): The specific type (invoices, tickets, simplified_invoices, additional_incomes, paysheets)
            attributes (BookEntryAttributes | Unset):
            relationships (BookEntryResourceRelationships | Unset):
     """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: BookEntryAttributes | Unset = UNSET
    relationships: BookEntryResourceRelationships | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.book_entry_attributes import BookEntryAttributes
        from ..models.book_entry_resource_relationships import BookEntryResourceRelationships
        id = self.id

        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_entry_attributes import BookEntryAttributes
        from ..models.book_entry_resource_relationships import BookEntryResourceRelationships
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: BookEntryAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = BookEntryAttributes.from_dict(_attributes)




        _relationships = d.pop("relationships", UNSET)
        relationships: BookEntryResourceRelationships | Unset
        if isinstance(_relationships,  Unset):
            relationships = UNSET
        else:
            relationships = BookEntryResourceRelationships.from_dict(_relationships)




        book_entry_resource = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )


        book_entry_resource.additional_properties = d
        return book_entry_resource

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

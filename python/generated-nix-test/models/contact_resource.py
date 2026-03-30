from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.contact_attributes import ContactAttributes





T = TypeVar("T", bound="ContactResource")



@_attrs_define
class ContactResource:
    """ 
        Attributes:
            id (str | Unset):
            type_ (Literal['contacts'] | Unset):
            attributes (ContactAttributes | Unset):
     """

    id: str | Unset = UNSET
    type_: Literal['contacts'] | Unset = UNSET
    attributes: ContactAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_attributes import ContactAttributes
        id = self.id

        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()


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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_attributes import ContactAttributes
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = cast(Literal['contacts'] | Unset , d.pop("type", UNSET))
        if type_ != 'contacts'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'contacts', got '{type_}'")

        _attributes = d.pop("attributes", UNSET)
        attributes: ContactAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = ContactAttributes.from_dict(_attributes)




        contact_resource = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        contact_resource.additional_properties = d
        return contact_resource

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

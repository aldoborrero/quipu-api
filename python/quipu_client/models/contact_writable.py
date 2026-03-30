from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.contact_writable_attributes import ContactWritableAttributes





T = TypeVar("T", bound="ContactWritable")



@_attrs_define
class ContactWritable:
    """ 
        Attributes:
            type_ (Literal['contacts']):
            attributes (ContactWritableAttributes):
     """

    type_: Literal['contacts']
    attributes: 'ContactWritableAttributes'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_writable_attributes import ContactWritableAttributes
        type_ = self.type_

        attributes = self.attributes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "attributes": attributes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_writable_attributes import ContactWritableAttributes
        d = dict(src_dict)
        type_ = cast(Literal['contacts'] , d.pop("type"))
        if type_ != 'contacts':
            raise ValueError(f"type must match const 'contacts', got '{type_}'")

        attributes = ContactWritableAttributes.from_dict(d.pop("attributes"))




        contact_writable = cls(
            type_=type_,
            attributes=attributes,
        )


        contact_writable.additional_properties = d
        return contact_writable

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

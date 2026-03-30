from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, Union, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.attachment_resource_attributes import AttachmentResourceAttributes





T = TypeVar("T", bound="AttachmentResource")



@_attrs_define
class AttachmentResource:
    """ 
        Attributes:
            id (Union[Unset, str]):
            type_ (Union[Literal['attachments'], Unset]):
            attributes (Union[Unset, AttachmentResourceAttributes]):
     """

    id: Union[Unset, str] = UNSET
    type_: Union[Literal['attachments'], Unset] = UNSET
    attributes: Union[Unset, 'AttachmentResourceAttributes'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_resource_attributes import AttachmentResourceAttributes
        id = self.id

        type_ = self.type_

        attributes: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.attachment_resource_attributes import AttachmentResourceAttributes
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = cast(Union[Literal['attachments'], Unset] , d.pop("type", UNSET))
        if type_ != 'attachments'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'attachments', got '{type_}'")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, AttachmentResourceAttributes]
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = AttachmentResourceAttributes.from_dict(_attributes)




        attachment_resource = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        attachment_resource.additional_properties = d
        return attachment_resource

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

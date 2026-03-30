from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttachmentResourceAttributes")



@_attrs_define
class AttachmentResourceAttributes:
    """ 
        Attributes:
            file_name (str | Unset):
            file_size (int | Unset):
            content_type (str | Unset):
            url (str | Unset):
     """

    file_name: str | Unset = UNSET
    file_size: int | Unset = UNSET
    content_type: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        file_size = self.file_size

        content_type = self.content_type

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("file_name", UNSET)

        file_size = d.pop("file_size", UNSET)

        content_type = d.pop("content_type", UNSET)

        url = d.pop("url", UNSET)

        attachment_resource_attributes = cls(
            file_name=file_name,
            file_size=file_size,
            content_type=content_type,
            url=url,
        )


        attachment_resource_attributes.additional_properties = d
        return attachment_resource_attributes

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

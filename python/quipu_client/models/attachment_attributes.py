from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentAttributes")


@_attrs_define
class AttachmentAttributes:
    """
    Attributes:
        url (str | Unset):
        small_url (str | Unset):
        thumbnail_url (str | Unset):
    """

    url: str | Unset = UNSET
    small_url: str | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        small_url = self.small_url

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if small_url is not UNSET:
            field_dict["small_url"] = small_url
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        small_url = d.pop("small_url", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        attachment_attributes = cls(
            url=url,
            small_url=small_url,
            thumbnail_url=thumbnail_url,
        )

        attachment_attributes.additional_properties = d
        return attachment_attributes

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_relationships_book_entry import AttachmentRelationshipsBookEntry


T = TypeVar("T", bound="AttachmentRelationships")


@_attrs_define
class AttachmentRelationships:
    """
    Attributes:
        book_entry (AttachmentRelationshipsBookEntry | Unset):
    """

    book_entry: AttachmentRelationshipsBookEntry | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        book_entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.book_entry, Unset):
            book_entry = self.book_entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if book_entry is not UNSET:
            field_dict["book_entry"] = book_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_relationships_book_entry import AttachmentRelationshipsBookEntry

        d = dict(src_dict)
        _book_entry = d.pop("book_entry", UNSET)
        book_entry: AttachmentRelationshipsBookEntry | Unset
        if isinstance(_book_entry, Unset):
            book_entry = UNSET
        else:
            book_entry = AttachmentRelationshipsBookEntry.from_dict(_book_entry)

        attachment_relationships = cls(
            book_entry=book_entry,
        )

        attachment_relationships.additional_properties = d
        return attachment_relationships

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

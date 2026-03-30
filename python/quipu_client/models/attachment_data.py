from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attachment_data_type import AttachmentDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_attributes import AttachmentAttributes
    from ..models.attachment_relationships import AttachmentRelationships


T = TypeVar("T", bound="AttachmentData")


@_attrs_define
class AttachmentData:
    """
    Attributes:
        id (str | Unset):
        type_ (AttachmentDataType | Unset):
        attributes (AttachmentAttributes | Unset):
        relationships (AttachmentRelationships | Unset):
    """

    id: str | Unset = UNSET
    type_: AttachmentDataType | Unset = UNSET
    attributes: AttachmentAttributes | Unset = UNSET
    relationships: AttachmentRelationships | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        from ..models.attachment_attributes import AttachmentAttributes
        from ..models.attachment_relationships import AttachmentRelationships

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AttachmentDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AttachmentDataType(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: AttachmentAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = AttachmentAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: AttachmentRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = AttachmentRelationships.from_dict(_relationships)

        attachment_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )

        attachment_data.additional_properties = d
        return attachment_data

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

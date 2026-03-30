from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_data_type import InvoiceDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_attributes import InvoiceAttributes
    from ..models.invoice_relationships import InvoiceRelationships


T = TypeVar("T", bound="InvoiceData")


@_attrs_define
class InvoiceData:
    """
    Attributes:
        id (str | Unset):
        type_ (InvoiceDataType | Unset):
        attributes (InvoiceAttributes | Unset):
        relationships (InvoiceRelationships | Unset):
    """

    id: str | Unset = UNSET
    type_: InvoiceDataType | Unset = UNSET
    attributes: InvoiceAttributes | Unset = UNSET
    relationships: InvoiceRelationships | Unset = UNSET
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
        from ..models.invoice_attributes import InvoiceAttributes
        from ..models.invoice_relationships import InvoiceRelationships

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: InvoiceDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InvoiceDataType(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: InvoiceAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = InvoiceAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: InvoiceRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = InvoiceRelationships.from_dict(_relationships)

        invoice_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )

        invoice_data.additional_properties = d
        return invoice_data

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

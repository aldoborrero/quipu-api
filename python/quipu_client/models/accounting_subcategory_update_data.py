from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.accounting_subcategory_update_data_type import AccountingSubcategoryUpdateDataType

if TYPE_CHECKING:
    from ..models.accounting_subcategory_attributes import AccountingSubcategoryAttributes


T = TypeVar("T", bound="AccountingSubcategoryUpdateData")


@_attrs_define
class AccountingSubcategoryUpdateData:
    """
    Attributes:
        type_ (AccountingSubcategoryUpdateDataType):
        attributes (AccountingSubcategoryAttributes):
    """

    type_: AccountingSubcategoryUpdateDataType
    attributes: AccountingSubcategoryAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounting_subcategory_attributes import AccountingSubcategoryAttributes

        d = dict(src_dict)
        type_ = AccountingSubcategoryUpdateDataType(d.pop("type"))

        attributes = AccountingSubcategoryAttributes.from_dict(d.pop("attributes"))

        accounting_subcategory_update_data = cls(
            type_=type_,
            attributes=attributes,
        )

        accounting_subcategory_update_data.additional_properties = d
        return accounting_subcategory_update_data

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

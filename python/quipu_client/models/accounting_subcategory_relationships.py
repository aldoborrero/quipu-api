from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accounting_subcategory_relationships_accounting_category import (
        AccountingSubcategoryRelationshipsAccountingCategory,
    )


T = TypeVar("T", bound="AccountingSubcategoryRelationships")


@_attrs_define
class AccountingSubcategoryRelationships:
    """
    Attributes:
        accounting_category (AccountingSubcategoryRelationshipsAccountingCategory | Unset):
    """

    accounting_category: AccountingSubcategoryRelationshipsAccountingCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounting_category, Unset):
            accounting_category = self.accounting_category.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounting_category is not UNSET:
            field_dict["accounting_category"] = accounting_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounting_subcategory_relationships_accounting_category import (
            AccountingSubcategoryRelationshipsAccountingCategory,
        )

        d = dict(src_dict)
        _accounting_category = d.pop("accounting_category", UNSET)
        accounting_category: AccountingSubcategoryRelationshipsAccountingCategory | Unset
        if isinstance(_accounting_category, Unset):
            accounting_category = UNSET
        else:
            accounting_category = AccountingSubcategoryRelationshipsAccountingCategory.from_dict(_accounting_category)

        accounting_subcategory_relationships = cls(
            accounting_category=accounting_category,
        )

        accounting_subcategory_relationships.additional_properties = d
        return accounting_subcategory_relationships

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

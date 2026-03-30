from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.accounting_category_attributes_kind import AccountingCategoryAttributesKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountingCategoryAttributes")


@_attrs_define
class AccountingCategoryAttributes:
    """
    Attributes:
        prefix (str | Unset):
        name (str | Unset):
        kind (AccountingCategoryAttributesKind | Unset):
    """

    prefix: str | Unset = UNSET
    name: str | Unset = UNSET
    kind: AccountingCategoryAttributesKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix = d.pop("prefix", UNSET)

        name = d.pop("name", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: AccountingCategoryAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = AccountingCategoryAttributesKind(_kind)

        accounting_category_attributes = cls(
            prefix=prefix,
            name=name,
            kind=kind,
        )

        accounting_category_attributes.additional_properties = d
        return accounting_category_attributes

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_attributes_kind import ItemAttributesKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemAttributes")


@_attrs_define
class ItemAttributes:
    """
    Attributes:
        concept (str | Unset):
        unitary_amount (str | Unset):
        quantity (str | Unset):
        kind (ItemAttributesKind | Unset):  Default: ItemAttributesKind.CURRENT.
        vat_percent (str | Unset):
        retention_percent (str | Unset):
        discount_percent (str | Unset):
        deductible_vat_percent (str | Unset):
        deductible_expense_percent (str | Unset):
        description (str | Unset):
        vat_amount (str | Unset):
        retention_amount (str | Unset):
        discount_amount (str | Unset):
        total_amount (str | Unset):
    """

    concept: str | Unset = UNSET
    unitary_amount: str | Unset = UNSET
    quantity: str | Unset = UNSET
    kind: ItemAttributesKind | Unset = ItemAttributesKind.CURRENT
    vat_percent: str | Unset = UNSET
    retention_percent: str | Unset = UNSET
    discount_percent: str | Unset = UNSET
    deductible_vat_percent: str | Unset = UNSET
    deductible_expense_percent: str | Unset = UNSET
    description: str | Unset = UNSET
    vat_amount: str | Unset = UNSET
    retention_amount: str | Unset = UNSET
    discount_amount: str | Unset = UNSET
    total_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concept = self.concept

        unitary_amount = self.unitary_amount

        quantity = self.quantity

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        vat_percent = self.vat_percent

        retention_percent = self.retention_percent

        discount_percent = self.discount_percent

        deductible_vat_percent = self.deductible_vat_percent

        deductible_expense_percent = self.deductible_expense_percent

        description = self.description

        vat_amount = self.vat_amount

        retention_amount = self.retention_amount

        discount_amount = self.discount_amount

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concept is not UNSET:
            field_dict["concept"] = concept
        if unitary_amount is not UNSET:
            field_dict["unitary_amount"] = unitary_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if kind is not UNSET:
            field_dict["kind"] = kind
        if vat_percent is not UNSET:
            field_dict["vat_percent"] = vat_percent
        if retention_percent is not UNSET:
            field_dict["retention_percent"] = retention_percent
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if deductible_vat_percent is not UNSET:
            field_dict["deductible_vat_percent"] = deductible_vat_percent
        if deductible_expense_percent is not UNSET:
            field_dict["deductible_expense_percent"] = deductible_expense_percent
        if description is not UNSET:
            field_dict["description"] = description
        if vat_amount is not UNSET:
            field_dict["vat_amount"] = vat_amount
        if retention_amount is not UNSET:
            field_dict["retention_amount"] = retention_amount
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        concept = d.pop("concept", UNSET)

        unitary_amount = d.pop("unitary_amount", UNSET)

        quantity = d.pop("quantity", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: ItemAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ItemAttributesKind(_kind)

        vat_percent = d.pop("vat_percent", UNSET)

        retention_percent = d.pop("retention_percent", UNSET)

        discount_percent = d.pop("discount_percent", UNSET)

        deductible_vat_percent = d.pop("deductible_vat_percent", UNSET)

        deductible_expense_percent = d.pop("deductible_expense_percent", UNSET)

        description = d.pop("description", UNSET)

        vat_amount = d.pop("vat_amount", UNSET)

        retention_amount = d.pop("retention_amount", UNSET)

        discount_amount = d.pop("discount_amount", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        item_attributes = cls(
            concept=concept,
            unitary_amount=unitary_amount,
            quantity=quantity,
            kind=kind,
            vat_percent=vat_percent,
            retention_percent=retention_percent,
            discount_percent=discount_percent,
            deductible_vat_percent=deductible_vat_percent,
            deductible_expense_percent=deductible_expense_percent,
            description=description,
            vat_amount=vat_amount,
            retention_amount=retention_amount,
            discount_amount=discount_amount,
            total_amount=total_amount,
        )

        item_attributes.additional_properties = d
        return item_attributes

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ItemAttributes")



@_attrs_define
class ItemAttributes:
    """ Line item on an invoice, ticket, or simplified invoice

        Attributes:
            id (str | Unset):
            concept (str | Unset): Name / description of the line item
            unitary_amount (str | Unset): Unit price as decimal string
            quantity (float | Unset): Quantity
            kind (str | Unset): Item kind
            vat_amount (str | Unset): Calculated VAT amount
            retention_amount (str | Unset): Calculated retention amount
            discount_amount (str | Unset): Calculated discount amount
            deductible_vat_amount (str | Unset): Deductible VAT amount
            total_amount (str | Unset): Total amount for this line item
            description (str | Unset): Extended description
            discount_percent (float | Unset): Discount percentage
            vat_percent (float | Unset): VAT percentage
            retention_percent (float | Unset): Retention percentage
            deductible_vat_percent (float | Unset): Deductible VAT percentage
            deductible_expense_percent (float | Unset): Deductible expense percentage
     """

    id: str | Unset = UNSET
    concept: str | Unset = UNSET
    unitary_amount: str | Unset = UNSET
    quantity: float | Unset = UNSET
    kind: str | Unset = UNSET
    vat_amount: str | Unset = UNSET
    retention_amount: str | Unset = UNSET
    discount_amount: str | Unset = UNSET
    deductible_vat_amount: str | Unset = UNSET
    total_amount: str | Unset = UNSET
    description: str | Unset = UNSET
    discount_percent: float | Unset = UNSET
    vat_percent: float | Unset = UNSET
    retention_percent: float | Unset = UNSET
    deductible_vat_percent: float | Unset = UNSET
    deductible_expense_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        concept = self.concept

        unitary_amount = self.unitary_amount

        quantity = self.quantity

        kind = self.kind

        vat_amount = self.vat_amount

        retention_amount = self.retention_amount

        discount_amount = self.discount_amount

        deductible_vat_amount = self.deductible_vat_amount

        total_amount = self.total_amount

        description = self.description

        discount_percent = self.discount_percent

        vat_percent = self.vat_percent

        retention_percent = self.retention_percent

        deductible_vat_percent = self.deductible_vat_percent

        deductible_expense_percent = self.deductible_expense_percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if concept is not UNSET:
            field_dict["concept"] = concept
        if unitary_amount is not UNSET:
            field_dict["unitary_amount"] = unitary_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if kind is not UNSET:
            field_dict["kind"] = kind
        if vat_amount is not UNSET:
            field_dict["vat_amount"] = vat_amount
        if retention_amount is not UNSET:
            field_dict["retention_amount"] = retention_amount
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if deductible_vat_amount is not UNSET:
            field_dict["deductible_vat_amount"] = deductible_vat_amount
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount
        if description is not UNSET:
            field_dict["description"] = description
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if vat_percent is not UNSET:
            field_dict["vat_percent"] = vat_percent
        if retention_percent is not UNSET:
            field_dict["retention_percent"] = retention_percent
        if deductible_vat_percent is not UNSET:
            field_dict["deductible_vat_percent"] = deductible_vat_percent
        if deductible_expense_percent is not UNSET:
            field_dict["deductible_expense_percent"] = deductible_expense_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        concept = d.pop("concept", UNSET)

        unitary_amount = d.pop("unitary_amount", UNSET)

        quantity = d.pop("quantity", UNSET)

        kind = d.pop("kind", UNSET)

        vat_amount = d.pop("vat_amount", UNSET)

        retention_amount = d.pop("retention_amount", UNSET)

        discount_amount = d.pop("discount_amount", UNSET)

        deductible_vat_amount = d.pop("deductible_vat_amount", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        description = d.pop("description", UNSET)

        discount_percent = d.pop("discount_percent", UNSET)

        vat_percent = d.pop("vat_percent", UNSET)

        retention_percent = d.pop("retention_percent", UNSET)

        deductible_vat_percent = d.pop("deductible_vat_percent", UNSET)

        deductible_expense_percent = d.pop("deductible_expense_percent", UNSET)

        item_attributes = cls(
            id=id,
            concept=concept,
            unitary_amount=unitary_amount,
            quantity=quantity,
            kind=kind,
            vat_amount=vat_amount,
            retention_amount=retention_amount,
            discount_amount=discount_amount,
            deductible_vat_amount=deductible_vat_amount,
            total_amount=total_amount,
            description=description,
            discount_percent=discount_percent,
            vat_percent=vat_percent,
            retention_percent=retention_percent,
            deductible_vat_percent=deductible_vat_percent,
            deductible_expense_percent=deductible_expense_percent,
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

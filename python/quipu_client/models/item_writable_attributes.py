from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ItemWritableAttributes")



@_attrs_define
class ItemWritableAttributes:
    """ 
        Attributes:
            concept (Union[Unset, str]):
            unitary_amount (Union[Unset, str]):
            quantity (Union[Unset, float]):
            vat_percent (Union[Unset, float]):
            retention_percent (Union[Unset, float]):
            discount_percent (Union[Unset, float]):
            kind (Union[Unset, str]):
            description (Union[Unset, str]):
     """

    concept: Union[Unset, str] = UNSET
    unitary_amount: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    vat_percent: Union[Unset, float] = UNSET
    retention_percent: Union[Unset, float] = UNSET
    discount_percent: Union[Unset, float] = UNSET
    kind: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        concept = self.concept

        unitary_amount = self.unitary_amount

        quantity = self.quantity

        vat_percent = self.vat_percent

        retention_percent = self.retention_percent

        discount_percent = self.discount_percent

        kind = self.kind

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if concept is not UNSET:
            field_dict["concept"] = concept
        if unitary_amount is not UNSET:
            field_dict["unitary_amount"] = unitary_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if vat_percent is not UNSET:
            field_dict["vat_percent"] = vat_percent
        if retention_percent is not UNSET:
            field_dict["retention_percent"] = retention_percent
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        concept = d.pop("concept", UNSET)

        unitary_amount = d.pop("unitary_amount", UNSET)

        quantity = d.pop("quantity", UNSET)

        vat_percent = d.pop("vat_percent", UNSET)

        retention_percent = d.pop("retention_percent", UNSET)

        discount_percent = d.pop("discount_percent", UNSET)

        kind = d.pop("kind", UNSET)

        description = d.pop("description", UNSET)

        item_writable_attributes = cls(
            concept=concept,
            unitary_amount=unitary_amount,
            quantity=quantity,
            vat_percent=vat_percent,
            retention_percent=retention_percent,
            discount_percent=discount_percent,
            kind=kind,
            description=description,
        )


        item_writable_attributes.additional_properties = d
        return item_writable_attributes

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

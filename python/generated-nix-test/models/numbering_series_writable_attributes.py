from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.numbering_series_writable_attributes_applies_to import NumberingSeriesWritableAttributesAppliesTo
from ..types import UNSET, Unset






T = TypeVar("T", bound="NumberingSeriesWritableAttributes")



@_attrs_define
class NumberingSeriesWritableAttributes:
    """ 
        Attributes:
            prefix (str | Unset):
            default (bool | Unset):
            amending (bool | Unset):
            applies_to (NumberingSeriesWritableAttributesAppliesTo | Unset):
     """

    prefix: str | Unset = UNSET
    default: bool | Unset = UNSET
    amending: bool | Unset = UNSET
    applies_to: NumberingSeriesWritableAttributesAppliesTo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        default = self.default

        amending = self.amending

        applies_to: str | Unset = UNSET
        if not isinstance(self.applies_to, Unset):
            applies_to = self.applies_to.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if default is not UNSET:
            field_dict["default"] = default
        if amending is not UNSET:
            field_dict["amending"] = amending
        if applies_to is not UNSET:
            field_dict["applies_to"] = applies_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix = d.pop("prefix", UNSET)

        default = d.pop("default", UNSET)

        amending = d.pop("amending", UNSET)

        _applies_to = d.pop("applies_to", UNSET)
        applies_to: NumberingSeriesWritableAttributesAppliesTo | Unset
        if isinstance(_applies_to,  Unset):
            applies_to = UNSET
        else:
            applies_to = NumberingSeriesWritableAttributesAppliesTo(_applies_to)




        numbering_series_writable_attributes = cls(
            prefix=prefix,
            default=default,
            amending=amending,
            applies_to=applies_to,
        )


        numbering_series_writable_attributes.additional_properties = d
        return numbering_series_writable_attributes

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

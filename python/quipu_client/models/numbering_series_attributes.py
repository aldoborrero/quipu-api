from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.numbering_series_attributes_applicable_to import NumberingSeriesAttributesApplicableTo
from ..types import UNSET, Unset

T = TypeVar("T", bound="NumberingSeriesAttributes")


@_attrs_define
class NumberingSeriesAttributes:
    """
    Attributes:
        prefix (str | Unset):
        applicable_to (NumberingSeriesAttributesApplicableTo | Unset):
        default (bool | Unset):
        amending (bool | Unset):
        deletable (bool | Unset):
    """

    prefix: str | Unset = UNSET
    applicable_to: NumberingSeriesAttributesApplicableTo | Unset = UNSET
    default: bool | Unset = UNSET
    amending: bool | Unset = UNSET
    deletable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        applicable_to: str | Unset = UNSET
        if not isinstance(self.applicable_to, Unset):
            applicable_to = self.applicable_to.value

        default = self.default

        amending = self.amending

        deletable = self.deletable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if applicable_to is not UNSET:
            field_dict["applicable_to"] = applicable_to
        if default is not UNSET:
            field_dict["default"] = default
        if amending is not UNSET:
            field_dict["amending"] = amending
        if deletable is not UNSET:
            field_dict["deletable"] = deletable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix = d.pop("prefix", UNSET)

        _applicable_to = d.pop("applicable_to", UNSET)
        applicable_to: NumberingSeriesAttributesApplicableTo | Unset
        if isinstance(_applicable_to, Unset):
            applicable_to = UNSET
        else:
            applicable_to = NumberingSeriesAttributesApplicableTo(_applicable_to)

        default = d.pop("default", UNSET)

        amending = d.pop("amending", UNSET)

        deletable = d.pop("deletable", UNSET)

        numbering_series_attributes = cls(
            prefix=prefix,
            applicable_to=applicable_to,
            default=default,
            amending=amending,
            deletable=deletable,
        )

        numbering_series_attributes.additional_properties = d
        return numbering_series_attributes

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

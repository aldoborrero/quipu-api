from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.numbering_series_attributes_applies_to import NumberingSeriesAttributesAppliesTo
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="NumberingSeriesAttributes")



@_attrs_define
class NumberingSeriesAttributes:
    """ 
        Attributes:
            prefix (Union[Unset, str]):  Example: F-.
            default (Union[Unset, bool]):
            amending (Union[Unset, bool]):
            deletable (Union[Unset, bool]):
            applicable_to (Union[None, Unset, str]):
            is_valid (Union[Unset, bool]):
            applies_to (Union[Unset, NumberingSeriesAttributesAppliesTo]):
     """

    prefix: Union[Unset, str] = UNSET
    default: Union[Unset, bool] = UNSET
    amending: Union[Unset, bool] = UNSET
    deletable: Union[Unset, bool] = UNSET
    applicable_to: Union[None, Unset, str] = UNSET
    is_valid: Union[Unset, bool] = UNSET
    applies_to: Union[Unset, NumberingSeriesAttributesAppliesTo] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        default = self.default

        amending = self.amending

        deletable = self.deletable

        applicable_to: Union[None, Unset, str]
        if isinstance(self.applicable_to, Unset):
            applicable_to = UNSET
        else:
            applicable_to = self.applicable_to

        is_valid = self.is_valid

        applies_to: Union[Unset, str] = UNSET
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
        if deletable is not UNSET:
            field_dict["deletable"] = deletable
        if applicable_to is not UNSET:
            field_dict["applicable_to"] = applicable_to
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid
        if applies_to is not UNSET:
            field_dict["applies_to"] = applies_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix = d.pop("prefix", UNSET)

        default = d.pop("default", UNSET)

        amending = d.pop("amending", UNSET)

        deletable = d.pop("deletable", UNSET)

        def _parse_applicable_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        applicable_to = _parse_applicable_to(d.pop("applicable_to", UNSET))


        is_valid = d.pop("is_valid", UNSET)

        _applies_to = d.pop("applies_to", UNSET)
        applies_to: Union[Unset, NumberingSeriesAttributesAppliesTo]
        if isinstance(_applies_to,  Unset):
            applies_to = UNSET
        else:
            applies_to = NumberingSeriesAttributesAppliesTo(_applies_to)




        numbering_series_attributes = cls(
            prefix=prefix,
            default=default,
            amending=amending,
            deletable=deletable,
            applicable_to=applicable_to,
            is_valid=is_valid,
            applies_to=applies_to,
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

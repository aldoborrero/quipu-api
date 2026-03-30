from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.numbering_series_writable_attributes import NumberingSeriesWritableAttributes





T = TypeVar("T", bound="NumberingSeriesWritable")



@_attrs_define
class NumberingSeriesWritable:
    """ 
        Attributes:
            type_ (Literal['numbering_series']):
            attributes (NumberingSeriesWritableAttributes):
     """

    type_: Literal['numbering_series']
    attributes: NumberingSeriesWritableAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.numbering_series_writable_attributes import NumberingSeriesWritableAttributes
        type_ = self.type_

        attributes = self.attributes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "attributes": attributes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.numbering_series_writable_attributes import NumberingSeriesWritableAttributes
        d = dict(src_dict)
        type_ = cast(Literal['numbering_series'] , d.pop("type"))
        if type_ != 'numbering_series':
            raise ValueError(f"type must match const 'numbering_series', got '{type_}'")

        attributes = NumberingSeriesWritableAttributes.from_dict(d.pop("attributes"))




        numbering_series_writable = cls(
            type_=type_,
            attributes=attributes,
        )


        numbering_series_writable.additional_properties = d
        return numbering_series_writable

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

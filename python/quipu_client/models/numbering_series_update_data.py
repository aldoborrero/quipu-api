from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.numbering_series_update_data_type import NumberingSeriesUpdateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.numbering_series_attributes import NumberingSeriesAttributes


T = TypeVar("T", bound="NumberingSeriesUpdateData")


@_attrs_define
class NumberingSeriesUpdateData:
    """
    Attributes:
        id (str):
        type_ (NumberingSeriesUpdateDataType):
        attributes (NumberingSeriesAttributes | Unset):
    """

    id: str
    type_: NumberingSeriesUpdateDataType
    attributes: NumberingSeriesAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.numbering_series_attributes import NumberingSeriesAttributes

        d = dict(src_dict)
        id = d.pop("id")

        type_ = NumberingSeriesUpdateDataType(d.pop("type"))

        _attributes = d.pop("attributes", UNSET)
        attributes: NumberingSeriesAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = NumberingSeriesAttributes.from_dict(_attributes)

        numbering_series_update_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        numbering_series_update_data.additional_properties = d
        return numbering_series_update_data

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

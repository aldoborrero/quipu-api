from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.additional_income_writable_attributes import AdditionalIncomeWritableAttributes
  from ..models.additional_income_writable_relationships import AdditionalIncomeWritableRelationships





T = TypeVar("T", bound="AdditionalIncomeWritable")



@_attrs_define
class AdditionalIncomeWritable:
    """ 
        Attributes:
            type_ (Literal['additional_incomes']):
            attributes (AdditionalIncomeWritableAttributes):
            relationships (AdditionalIncomeWritableRelationships | Unset):
     """

    type_: Literal['additional_incomes']
    attributes: AdditionalIncomeWritableAttributes
    relationships: AdditionalIncomeWritableRelationships | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.additional_income_writable_attributes import AdditionalIncomeWritableAttributes
        from ..models.additional_income_writable_relationships import AdditionalIncomeWritableRelationships
        type_ = self.type_

        attributes = self.attributes.to_dict()

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "attributes": attributes,
        })
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.additional_income_writable_attributes import AdditionalIncomeWritableAttributes
        from ..models.additional_income_writable_relationships import AdditionalIncomeWritableRelationships
        d = dict(src_dict)
        type_ = cast(Literal['additional_incomes'] , d.pop("type"))
        if type_ != 'additional_incomes':
            raise ValueError(f"type must match const 'additional_incomes', got '{type_}'")

        attributes = AdditionalIncomeWritableAttributes.from_dict(d.pop("attributes"))




        _relationships = d.pop("relationships", UNSET)
        relationships: AdditionalIncomeWritableRelationships | Unset
        if isinstance(_relationships,  Unset):
            relationships = UNSET
        else:
            relationships = AdditionalIncomeWritableRelationships.from_dict(_relationships)




        additional_income_writable = cls(
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )


        additional_income_writable.additional_properties = d
        return additional_income_writable

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

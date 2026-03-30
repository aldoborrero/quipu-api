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
  from ..models.accounting_subcategory_writable_attributes import AccountingSubcategoryWritableAttributes
  from ..models.accounting_subcategory_writable_relationships import AccountingSubcategoryWritableRelationships





T = TypeVar("T", bound="AccountingSubcategoryWritable")



@_attrs_define
class AccountingSubcategoryWritable:
    """ 
        Attributes:
            type_ (Literal['accounting_subcategories']):
            attributes (AccountingSubcategoryWritableAttributes):
            relationships (AccountingSubcategoryWritableRelationships | Unset):
     """

    type_: Literal['accounting_subcategories']
    attributes: AccountingSubcategoryWritableAttributes
    relationships: AccountingSubcategoryWritableRelationships | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.accounting_subcategory_writable_attributes import AccountingSubcategoryWritableAttributes
        from ..models.accounting_subcategory_writable_relationships import AccountingSubcategoryWritableRelationships
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
        from ..models.accounting_subcategory_writable_attributes import AccountingSubcategoryWritableAttributes
        from ..models.accounting_subcategory_writable_relationships import AccountingSubcategoryWritableRelationships
        d = dict(src_dict)
        type_ = cast(Literal['accounting_subcategories'] , d.pop("type"))
        if type_ != 'accounting_subcategories':
            raise ValueError(f"type must match const 'accounting_subcategories', got '{type_}'")

        attributes = AccountingSubcategoryWritableAttributes.from_dict(d.pop("attributes"))




        _relationships = d.pop("relationships", UNSET)
        relationships: AccountingSubcategoryWritableRelationships | Unset
        if isinstance(_relationships,  Unset):
            relationships = UNSET
        else:
            relationships = AccountingSubcategoryWritableRelationships.from_dict(_relationships)




        accounting_subcategory_writable = cls(
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )


        accounting_subcategory_writable.additional_properties = d
        return accounting_subcategory_writable

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

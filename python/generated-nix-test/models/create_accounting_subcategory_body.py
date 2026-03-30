from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.accounting_subcategory_writable import AccountingSubcategoryWritable





T = TypeVar("T", bound="CreateAccountingSubcategoryBody")



@_attrs_define
class CreateAccountingSubcategoryBody:
    """ 
        Attributes:
            data (AccountingSubcategoryWritable):
     """

    data: AccountingSubcategoryWritable
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.accounting_subcategory_writable import AccountingSubcategoryWritable
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounting_subcategory_writable import AccountingSubcategoryWritable
        d = dict(src_dict)
        data = AccountingSubcategoryWritable.from_dict(d.pop("data"))




        create_accounting_subcategory_body = cls(
            data=data,
        )


        create_accounting_subcategory_body.additional_properties = d
        return create_accounting_subcategory_body

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

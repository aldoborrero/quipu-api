from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.relationship_linkage_type_0 import RelationshipLinkageType0





T = TypeVar("T", bound="AccountingSubcategoryWritableRelationships")



@_attrs_define
class AccountingSubcategoryWritableRelationships:
    """ 
        Attributes:
            accounting_category (Union['RelationshipLinkageType0', None, Unset]):
     """

    accounting_category: Union['RelationshipLinkageType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        accounting_category: Union[None, Unset, dict[str, Any]]
        if isinstance(self.accounting_category, Unset):
            accounting_category = UNSET
        elif isinstance(self.accounting_category, RelationshipLinkageType0):
            accounting_category = self.accounting_category.to_dict()
        else:
            accounting_category = self.accounting_category


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if accounting_category is not UNSET:
            field_dict["accounting_category"] = accounting_category

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        d = dict(src_dict)
        def _parse_accounting_category(data: object) -> Union['RelationshipLinkageType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_relationship_linkage_type_0 = RelationshipLinkageType0.from_dict(data)



                return componentsschemas_relationship_linkage_type_0
            except: # noqa: E722
                pass
            return cast(Union['RelationshipLinkageType0', None, Unset], data)

        accounting_category = _parse_accounting_category(d.pop("accounting_category", UNSET))


        accounting_subcategory_writable_relationships = cls(
            accounting_category=accounting_category,
        )


        accounting_subcategory_writable_relationships.additional_properties = d
        return accounting_subcategory_writable_relationships

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

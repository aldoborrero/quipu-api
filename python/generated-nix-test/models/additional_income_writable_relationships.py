from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.additional_income_writable_relationships_items import AdditionalIncomeWritableRelationshipsItems
  from ..models.relationship_linkage_type_0 import RelationshipLinkageType0





T = TypeVar("T", bound="AdditionalIncomeWritableRelationships")



@_attrs_define
class AdditionalIncomeWritableRelationships:
    """ 
        Attributes:
            numeration (None | RelationshipLinkageType0 | Unset):
            items (AdditionalIncomeWritableRelationshipsItems | Unset):
     """

    numeration: None | RelationshipLinkageType0 | Unset = UNSET
    items: AdditionalIncomeWritableRelationshipsItems | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.additional_income_writable_relationships_items import AdditionalIncomeWritableRelationshipsItems
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        numeration: dict[str, Any] | None | Unset
        if isinstance(self.numeration, Unset):
            numeration = UNSET
        elif isinstance(self.numeration, RelationshipLinkageType0):
            numeration = self.numeration.to_dict()
        else:
            numeration = self.numeration

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if numeration is not UNSET:
            field_dict["numeration"] = numeration
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.additional_income_writable_relationships_items import AdditionalIncomeWritableRelationshipsItems
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        d = dict(src_dict)
        def _parse_numeration(data: object) -> None | RelationshipLinkageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_relationship_linkage_type_0 = RelationshipLinkageType0.from_dict(data)



                return componentsschemas_relationship_linkage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RelationshipLinkageType0 | Unset, data)

        numeration = _parse_numeration(d.pop("numeration", UNSET))


        _items = d.pop("items", UNSET)
        items: AdditionalIncomeWritableRelationshipsItems | Unset
        if isinstance(_items,  Unset):
            items = UNSET
        else:
            items = AdditionalIncomeWritableRelationshipsItems.from_dict(_items)




        additional_income_writable_relationships = cls(
            numeration=numeration,
            items=items,
        )


        additional_income_writable_relationships.additional_properties = d
        return additional_income_writable_relationships

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

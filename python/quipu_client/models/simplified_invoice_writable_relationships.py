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
  from ..models.simplified_invoice_writable_relationships_items import SimplifiedInvoiceWritableRelationshipsItems
  from ..models.relationship_linkage_type_0 import RelationshipLinkageType0





T = TypeVar("T", bound="SimplifiedInvoiceWritableRelationships")



@_attrs_define
class SimplifiedInvoiceWritableRelationships:
    """ 
        Attributes:
            numeration (Union['RelationshipLinkageType0', None, Unset]):
            items (Union[Unset, SimplifiedInvoiceWritableRelationshipsItems]):
     """

    numeration: Union['RelationshipLinkageType0', None, Unset] = UNSET
    items: Union[Unset, 'SimplifiedInvoiceWritableRelationshipsItems'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.simplified_invoice_writable_relationships_items import SimplifiedInvoiceWritableRelationshipsItems
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        numeration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.numeration, Unset):
            numeration = UNSET
        elif isinstance(self.numeration, RelationshipLinkageType0):
            numeration = self.numeration.to_dict()
        else:
            numeration = self.numeration

        items: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.simplified_invoice_writable_relationships_items import SimplifiedInvoiceWritableRelationshipsItems
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        d = dict(src_dict)
        def _parse_numeration(data: object) -> Union['RelationshipLinkageType0', None, Unset]:
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

        numeration = _parse_numeration(d.pop("numeration", UNSET))


        _items = d.pop("items", UNSET)
        items: Union[Unset, SimplifiedInvoiceWritableRelationshipsItems]
        if isinstance(_items,  Unset):
            items = UNSET
        else:
            items = SimplifiedInvoiceWritableRelationshipsItems.from_dict(_items)




        simplified_invoice_writable_relationships = cls(
            numeration=numeration,
            items=items,
        )


        simplified_invoice_writable_relationships.additional_properties = d
        return simplified_invoice_writable_relationships

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

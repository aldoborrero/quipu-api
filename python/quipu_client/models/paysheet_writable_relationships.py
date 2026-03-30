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





T = TypeVar("T", bound="PaysheetWritableRelationships")



@_attrs_define
class PaysheetWritableRelationships:
    """ 
        Attributes:
            contact (Union['RelationshipLinkageType0', None, Unset]):
     """

    contact: Union['RelationshipLinkageType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        contact: Union[None, Unset, dict[str, Any]]
        if isinstance(self.contact, Unset):
            contact = UNSET
        elif isinstance(self.contact, RelationshipLinkageType0):
            contact = self.contact.to_dict()
        else:
            contact = self.contact


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contact is not UNSET:
            field_dict["contact"] = contact

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relationship_linkage_type_0 import RelationshipLinkageType0
        d = dict(src_dict)
        def _parse_contact(data: object) -> Union['RelationshipLinkageType0', None, Unset]:
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

        contact = _parse_contact(d.pop("contact", UNSET))


        paysheet_writable_relationships = cls(
            contact=contact,
        )


        paysheet_writable_relationships.additional_properties = d
        return paysheet_writable_relationships

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

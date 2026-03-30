from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, Union, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.paysheet_resource_relationships import PaysheetResourceRelationships
  from ..models.paysheet_attributes import PaysheetAttributes





T = TypeVar("T", bound="PaysheetResource")



@_attrs_define
class PaysheetResource:
    """ 
        Attributes:
            id (Union[Unset, str]):
            type_ (Union[Literal['paysheets'], Unset]):
            attributes (Union[Unset, PaysheetAttributes]):
            relationships (Union[Unset, PaysheetResourceRelationships]):
     """

    id: Union[Unset, str] = UNSET
    type_: Union[Literal['paysheets'], Unset] = UNSET
    attributes: Union[Unset, 'PaysheetAttributes'] = UNSET
    relationships: Union[Unset, 'PaysheetResourceRelationships'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.paysheet_resource_relationships import PaysheetResourceRelationships
        from ..models.paysheet_attributes import PaysheetAttributes
        id = self.id

        type_ = self.type_

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paysheet_resource_relationships import PaysheetResourceRelationships
        from ..models.paysheet_attributes import PaysheetAttributes
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = cast(Union[Literal['paysheets'], Unset] , d.pop("type", UNSET))
        if type_ != 'paysheets'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'paysheets', got '{type_}'")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, PaysheetAttributes]
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = PaysheetAttributes.from_dict(_attributes)




        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, PaysheetResourceRelationships]
        if isinstance(_relationships,  Unset):
            relationships = UNSET
        else:
            relationships = PaysheetResourceRelationships.from_dict(_relationships)




        paysheet_resource = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )


        paysheet_resource.additional_properties = d
        return paysheet_resource

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

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
  from ..models.ticket_resource_relationships import TicketResourceRelationships
  from ..models.ticket_attributes import TicketAttributes





T = TypeVar("T", bound="TicketResource")



@_attrs_define
class TicketResource:
    """ 
        Attributes:
            id (Union[Unset, str]):
            type_ (Union[Literal['tickets'], Unset]):
            attributes (Union[Unset, TicketAttributes]):
            relationships (Union[Unset, TicketResourceRelationships]):
     """

    id: Union[Unset, str] = UNSET
    type_: Union[Literal['tickets'], Unset] = UNSET
    attributes: Union[Unset, 'TicketAttributes'] = UNSET
    relationships: Union[Unset, 'TicketResourceRelationships'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.ticket_resource_relationships import TicketResourceRelationships
        from ..models.ticket_attributes import TicketAttributes
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
        from ..models.ticket_resource_relationships import TicketResourceRelationships
        from ..models.ticket_attributes import TicketAttributes
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = cast(Union[Literal['tickets'], Unset] , d.pop("type", UNSET))
        if type_ != 'tickets'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'tickets', got '{type_}'")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, TicketAttributes]
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = TicketAttributes.from_dict(_attributes)




        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, TicketResourceRelationships]
        if isinstance(_relationships,  Unset):
            relationships = UNSET
        else:
            relationships = TicketResourceRelationships.from_dict(_relationships)




        ticket_resource = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )


        ticket_resource.additional_properties = d
        return ticket_resource

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

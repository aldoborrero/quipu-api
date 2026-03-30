from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ticket_writable_attributes import TicketWritableAttributes
  from ..models.ticket_writable_relationships import TicketWritableRelationships





T = TypeVar("T", bound="TicketWritable")



@_attrs_define
class TicketWritable:
    """ 
        Attributes:
            type_ (Literal['tickets']):
            attributes (TicketWritableAttributes):
            relationships (Union[Unset, TicketWritableRelationships]):
     """

    type_: Literal['tickets']
    attributes: 'TicketWritableAttributes'
    relationships: Union[Unset, 'TicketWritableRelationships'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.ticket_writable_attributes import TicketWritableAttributes
        from ..models.ticket_writable_relationships import TicketWritableRelationships
        type_ = self.type_

        attributes = self.attributes.to_dict()

        relationships: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.ticket_writable_attributes import TicketWritableAttributes
        from ..models.ticket_writable_relationships import TicketWritableRelationships
        d = dict(src_dict)
        type_ = cast(Literal['tickets'] , d.pop("type"))
        if type_ != 'tickets':
            raise ValueError(f"type must match const 'tickets', got '{type_}'")

        attributes = TicketWritableAttributes.from_dict(d.pop("attributes"))




        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, TicketWritableRelationships]
        if isinstance(_relationships,  Unset):
            relationships = UNSET
        else:
            relationships = TicketWritableRelationships.from_dict(_relationships)




        ticket_writable = cls(
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )


        ticket_writable.additional_properties = d
        return ticket_writable

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

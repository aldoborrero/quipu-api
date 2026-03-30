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
  from ..models.simplified_invoice_writable_relationships import SimplifiedInvoiceWritableRelationships
  from ..models.simplified_invoice_writable_attributes import SimplifiedInvoiceWritableAttributes





T = TypeVar("T", bound="SimplifiedInvoiceWritable")



@_attrs_define
class SimplifiedInvoiceWritable:
    """ 
        Attributes:
            type_ (Literal['simplified_invoices']):
            attributes (SimplifiedInvoiceWritableAttributes):
            relationships (Union[Unset, SimplifiedInvoiceWritableRelationships]):
     """

    type_: Literal['simplified_invoices']
    attributes: 'SimplifiedInvoiceWritableAttributes'
    relationships: Union[Unset, 'SimplifiedInvoiceWritableRelationships'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.simplified_invoice_writable_relationships import SimplifiedInvoiceWritableRelationships
        from ..models.simplified_invoice_writable_attributes import SimplifiedInvoiceWritableAttributes
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
        from ..models.simplified_invoice_writable_relationships import SimplifiedInvoiceWritableRelationships
        from ..models.simplified_invoice_writable_attributes import SimplifiedInvoiceWritableAttributes
        d = dict(src_dict)
        type_ = cast(Literal['simplified_invoices'] , d.pop("type"))
        if type_ != 'simplified_invoices':
            raise ValueError(f"type must match const 'simplified_invoices', got '{type_}'")

        attributes = SimplifiedInvoiceWritableAttributes.from_dict(d.pop("attributes"))




        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, SimplifiedInvoiceWritableRelationships]
        if isinstance(_relationships,  Unset):
            relationships = UNSET
        else:
            relationships = SimplifiedInvoiceWritableRelationships.from_dict(_relationships)




        simplified_invoice_writable = cls(
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )


        simplified_invoice_writable.additional_properties = d
        return simplified_invoice_writable

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

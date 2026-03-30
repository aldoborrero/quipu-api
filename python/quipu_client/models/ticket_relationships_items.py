from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_invoice_create import ItemInvoiceCreate
    from ..models.item_invoice_update import ItemInvoiceUpdate


T = TypeVar("T", bound="TicketRelationshipsItems")


@_attrs_define
class TicketRelationshipsItems:
    """
    Attributes:
        data (list[ItemInvoiceCreate | ItemInvoiceUpdate] | Unset):
    """

    data: list[ItemInvoiceCreate | ItemInvoiceUpdate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_invoice_create import ItemInvoiceCreate

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(data_item_data, ItemInvoiceCreate):
                    data_item = data_item_data.to_dict()
                else:
                    data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_invoice_create import ItemInvoiceCreate
        from ..models.item_invoice_update import ItemInvoiceUpdate

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[ItemInvoiceCreate | ItemInvoiceUpdate] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:

                def _parse_data_item(data: object) -> ItemInvoiceCreate | ItemInvoiceUpdate:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        data_item_type_0 = ItemInvoiceCreate.from_dict(data)

                        return data_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = ItemInvoiceUpdate.from_dict(data)

                    return data_item_type_1

                data_item = _parse_data_item(data_item_data)

                data.append(data_item)

        ticket_relationships_items = cls(
            data=data,
        )

        ticket_relationships_items.additional_properties = d
        return ticket_relationships_items

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

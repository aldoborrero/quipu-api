from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_data import InvoiceData
    from ..models.pagination_meta_meta import PaginationMetaMeta
    from ..models.paysheet_data import PaysheetData
    from ..models.ticket_data import TicketData


T = TypeVar("T", bound="BookEntryCollection")


@_attrs_define
class BookEntryCollection:
    """
    Attributes:
        meta (PaginationMetaMeta | Unset):
        data (list[InvoiceData | PaysheetData | TicketData] | Unset):
    """

    meta: PaginationMetaMeta | Unset = UNSET
    data: list[InvoiceData | PaysheetData | TicketData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_data import InvoiceData
        from ..models.ticket_data import TicketData

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(data_item_data, InvoiceData):
                    data_item = data_item_data.to_dict()
                elif isinstance(data_item_data, TicketData):
                    data_item = data_item_data.to_dict()
                else:
                    data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_data import InvoiceData
        from ..models.pagination_meta_meta import PaginationMetaMeta
        from ..models.paysheet_data import PaysheetData
        from ..models.ticket_data import TicketData

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: PaginationMetaMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = PaginationMetaMeta.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: list[InvoiceData | PaysheetData | TicketData] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:

                def _parse_data_item(data: object) -> InvoiceData | PaysheetData | TicketData:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        data_item_type_0 = InvoiceData.from_dict(data)

                        return data_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        data_item_type_1 = TicketData.from_dict(data)

                        return data_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_2 = PaysheetData.from_dict(data)

                    return data_item_type_2

                data_item = _parse_data_item(data_item_data)

                data.append(data_item)

        book_entry_collection = cls(
            meta=meta,
            data=data,
        )

        book_entry_collection.additional_properties = d
        return book_entry_collection

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

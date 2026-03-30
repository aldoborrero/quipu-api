from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_collection_included_item import InvoiceCollectionIncludedItem
    from ..models.invoice_data import InvoiceData
    from ..models.pagination_meta_meta import PaginationMetaMeta


T = TypeVar("T", bound="InvoiceCollection")


@_attrs_define
class InvoiceCollection:
    """
    Attributes:
        meta (PaginationMetaMeta | Unset):
        data (list[InvoiceData] | Unset):
        included (list[InvoiceCollectionIncludedItem] | Unset):
    """

    meta: PaginationMetaMeta | Unset = UNSET
    data: list[InvoiceData] | Unset = UNSET
    included: list[InvoiceCollectionIncludedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        included: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_collection_included_item import InvoiceCollectionIncludedItem
        from ..models.invoice_data import InvoiceData
        from ..models.pagination_meta_meta import PaginationMetaMeta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: PaginationMetaMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = PaginationMetaMeta.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: list[InvoiceData] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = InvoiceData.from_dict(data_item_data)

                data.append(data_item)

        _included = d.pop("included", UNSET)
        included: list[InvoiceCollectionIncludedItem] | Unset = UNSET
        if _included is not UNSET:
            included = []
            for included_item_data in _included:
                included_item = InvoiceCollectionIncludedItem.from_dict(included_item_data)

                included.append(included_item)

        invoice_collection = cls(
            meta=meta,
            data=data,
            included=included,
        )

        invoice_collection.additional_properties = d
        return invoice_collection

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

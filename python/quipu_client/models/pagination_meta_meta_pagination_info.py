from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationMetaMetaPaginationInfo")


@_attrs_define
class PaginationMetaMetaPaginationInfo:
    """
    Attributes:
        total_pages (int | Unset):
        current_page (int | Unset):
        total_results (int | Unset):
    """

    total_pages: int | Unset = UNSET
    current_page: int | Unset = UNSET
    total_results: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_pages = self.total_pages

        current_page = self.current_page

        total_results = self.total_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if total_results is not UNSET:
            field_dict["total_results"] = total_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_pages = d.pop("total_pages", UNSET)

        current_page = d.pop("current_page", UNSET)

        total_results = d.pop("total_results", UNSET)

        pagination_meta_meta_pagination_info = cls(
            total_pages=total_pages,
            current_page=current_page,
            total_results=total_results,
        )

        pagination_meta_meta_pagination_info.additional_properties = d
        return pagination_meta_meta_pagination_info

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

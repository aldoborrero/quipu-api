from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_errors_item_source import ErrorResponseErrorsItemSource


T = TypeVar("T", bound="ErrorResponseErrorsItem")


@_attrs_define
class ErrorResponseErrorsItem:
    """
    Attributes:
        detail (str | Unset):
        source (ErrorResponseErrorsItemSource | Unset):
    """

    detail: str | Unset = UNSET
    source: ErrorResponseErrorsItemSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_errors_item_source import ErrorResponseErrorsItemSource

        d = dict(src_dict)
        detail = d.pop("detail", UNSET)

        _source = d.pop("source", UNSET)
        source: ErrorResponseErrorsItemSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ErrorResponseErrorsItemSource.from_dict(_source)

        error_response_errors_item = cls(
            detail=detail,
            source=source,
        )

        error_response_errors_item.additional_properties = d
        return error_response_errors_item

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

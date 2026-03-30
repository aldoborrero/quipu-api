from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.error_response_errors_item_source import ErrorResponseErrorsItemSource





T = TypeVar("T", bound="ErrorResponseErrorsItem")



@_attrs_define
class ErrorResponseErrorsItem:
    """ 
        Attributes:
            source (Union[Unset, ErrorResponseErrorsItemSource]):
            detail (Union[Unset, str]):  Example: can't be blank.
     """

    source: Union[Unset, 'ErrorResponseErrorsItemSource'] = UNSET
    detail: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.error_response_errors_item_source import ErrorResponseErrorsItemSource
        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        detail = self.detail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_errors_item_source import ErrorResponseErrorsItemSource
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: Union[Unset, ErrorResponseErrorsItemSource]
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = ErrorResponseErrorsItemSource.from_dict(_source)




        detail = d.pop("detail", UNSET)

        error_response_errors_item = cls(
            source=source,
            detail=detail,
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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ticket_data import TicketData
    from ..models.ticket_response_included_item import TicketResponseIncludedItem


T = TypeVar("T", bound="TicketResponse")


@_attrs_define
class TicketResponse:
    """
    Attributes:
        data (TicketData | Unset):
        included (list[TicketResponseIncludedItem] | Unset):
    """

    data: TicketData | Unset = UNSET
    included: list[TicketResponseIncludedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        included: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ticket_data import TicketData
        from ..models.ticket_response_included_item import TicketResponseIncludedItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: TicketData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TicketData.from_dict(_data)

        _included = d.pop("included", UNSET)
        included: list[TicketResponseIncludedItem] | Unset = UNSET
        if _included is not UNSET:
            included = []
            for included_item_data in _included:
                included_item = TicketResponseIncludedItem.from_dict(included_item_data)

                included.append(included_item)

        ticket_response = cls(
            data=data,
            included=included,
        )

        ticket_response.additional_properties = d
        return ticket_response

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

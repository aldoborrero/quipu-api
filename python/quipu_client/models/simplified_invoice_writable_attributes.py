from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.simplified_invoice_writable_attributes_kind import SimplifiedInvoiceWritableAttributesKind
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="SimplifiedInvoiceWritableAttributes")



@_attrs_define
class SimplifiedInvoiceWritableAttributes:
    """ 
        Attributes:
            kind (SimplifiedInvoiceWritableAttributesKind):
            issue_date (datetime.date):
            filing_number (Union[None, Unset, str]):
            due_dates (Union[Unset, list[datetime.date]]):
            paid_at (Union[None, Unset, datetime.date]):
            payment_method (Union[Unset, str]):
            tags (Union[Unset, list[str]]):
            notes (Union[Unset, str]):
     """

    kind: SimplifiedInvoiceWritableAttributesKind
    issue_date: datetime.date
    filing_number: Union[None, Unset, str] = UNSET
    due_dates: Union[Unset, list[datetime.date]] = UNSET
    paid_at: Union[None, Unset, datetime.date] = UNSET
    payment_method: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        issue_date = self.issue_date.isoformat()

        filing_number: Union[None, Unset, str]
        if isinstance(self.filing_number, Unset):
            filing_number = UNSET
        else:
            filing_number = self.filing_number

        due_dates: Union[Unset, list[str]] = UNSET
        if not isinstance(self.due_dates, Unset):
            due_dates = []
            for due_dates_item_data in self.due_dates:
                due_dates_item = due_dates_item_data.isoformat()
                due_dates.append(due_dates_item)



        paid_at: Union[None, Unset, str]
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.date):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        payment_method = self.payment_method

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "issue_date": issue_date,
        })
        if filing_number is not UNSET:
            field_dict["filing_number"] = filing_number
        if due_dates is not UNSET:
            field_dict["due_dates"] = due_dates
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if tags is not UNSET:
            field_dict["tags"] = tags
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = SimplifiedInvoiceWritableAttributesKind(d.pop("kind"))




        issue_date = isoparse(d.pop("issue_date")).date()




        def _parse_filing_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        filing_number = _parse_filing_number(d.pop("filing_number", UNSET))


        due_dates = []
        _due_dates = d.pop("due_dates", UNSET)
        for due_dates_item_data in (_due_dates or []):
            due_dates_item = isoparse(due_dates_item_data).date()



            due_dates.append(due_dates_item)


        def _parse_paid_at(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = isoparse(data).date()



                return paid_at_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        paid_at = _parse_paid_at(d.pop("paid_at", UNSET))


        payment_method = d.pop("payment_method", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        notes = d.pop("notes", UNSET)

        simplified_invoice_writable_attributes = cls(
            kind=kind,
            issue_date=issue_date,
            filing_number=filing_number,
            due_dates=due_dates,
            paid_at=paid_at,
            payment_method=payment_method,
            tags=tags,
            notes=notes,
        )


        simplified_invoice_writable_attributes.additional_properties = d
        return simplified_invoice_writable_attributes

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

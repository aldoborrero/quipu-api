from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.paysheet_writable_attributes_kind import PaysheetWritableAttributesKind
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PaysheetWritableAttributes")



@_attrs_define
class PaysheetWritableAttributes:
    """ 
        Attributes:
            kind (PaysheetWritableAttributesKind):
            issue_date (datetime.date):
            paid_at (datetime.date | None | Unset):
            payment_method (str | Unset):
            tags (list[str] | Unset):
            net_pay (float | Unset): Net pay amount
            gross_pay (str | Unset):
            employee_ss_amount (float | Unset): Employee social security amount
            employee_retention (float | Unset): Employee retention amount
            company_ss_amount (float | Unset): Company social security amount
     """

    kind: PaysheetWritableAttributesKind
    issue_date: datetime.date
    paid_at: datetime.date | None | Unset = UNSET
    payment_method: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    net_pay: float | Unset = UNSET
    gross_pay: str | Unset = UNSET
    employee_ss_amount: float | Unset = UNSET
    employee_retention: float | Unset = UNSET
    company_ss_amount: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        issue_date = self.issue_date.isoformat()

        paid_at: None | str | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.date):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        payment_method = self.payment_method

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        net_pay = self.net_pay

        gross_pay = self.gross_pay

        employee_ss_amount = self.employee_ss_amount

        employee_retention = self.employee_retention

        company_ss_amount = self.company_ss_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "issue_date": issue_date,
        })
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if tags is not UNSET:
            field_dict["tags"] = tags
        if net_pay is not UNSET:
            field_dict["net_pay"] = net_pay
        if gross_pay is not UNSET:
            field_dict["gross_pay"] = gross_pay
        if employee_ss_amount is not UNSET:
            field_dict["employee_ss_amount"] = employee_ss_amount
        if employee_retention is not UNSET:
            field_dict["employee_retention"] = employee_retention
        if company_ss_amount is not UNSET:
            field_dict["company_ss_amount"] = company_ss_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = PaysheetWritableAttributesKind(d.pop("kind"))




        issue_date = isoparse(d.pop("issue_date")).date()




        def _parse_paid_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = isoparse(data).date()



                return paid_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        paid_at = _parse_paid_at(d.pop("paid_at", UNSET))


        payment_method = d.pop("payment_method", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        net_pay = d.pop("net_pay", UNSET)

        gross_pay = d.pop("gross_pay", UNSET)

        employee_ss_amount = d.pop("employee_ss_amount", UNSET)

        employee_retention = d.pop("employee_retention", UNSET)

        company_ss_amount = d.pop("company_ss_amount", UNSET)

        paysheet_writable_attributes = cls(
            kind=kind,
            issue_date=issue_date,
            paid_at=paid_at,
            payment_method=payment_method,
            tags=tags,
            net_pay=net_pay,
            gross_pay=gross_pay,
            employee_ss_amount=employee_ss_amount,
            employee_retention=employee_retention,
            company_ss_amount=company_ss_amount,
        )


        paysheet_writable_attributes.additional_properties = d
        return paysheet_writable_attributes

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

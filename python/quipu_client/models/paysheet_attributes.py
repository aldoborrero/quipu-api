from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.paysheet_attributes_kind import PaysheetAttributesKind
from ..models.paysheet_attributes_payment_status import PaysheetAttributesPaymentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaysheetAttributes")


@_attrs_define
class PaysheetAttributes:
    """
    Attributes:
        kind (PaysheetAttributesKind | Unset):
        number (str | Unset):
        issue_date (datetime.date | Unset):
        paid_at (datetime.date | None | Unset):
        payment_method (None | str | Unset):
        payment_status (PaysheetAttributesPaymentStatus | Unset):
        net_pay (str | Unset):
        gross_pay (str | Unset):
        employee_ss_amount (str | Unset):
        employee_retention (str | Unset):
        company_ss_amount (str | Unset):
        issuing_name (str | Unset):
        issuing_tax_id (str | Unset):
        issuing_address (str | Unset):
        issuing_phone (str | Unset):
        issuing_town (str | Unset):
        issuing_zip_code (str | Unset):
        issuing_country_code (str | Unset):
        recipient_name (str | Unset):
        recipient_tax_id (str | Unset):
        recipient_address (str | Unset):
        recipient_phone (str | Unset):
        recipient_town (str | Unset):
        recipient_zip_code (str | Unset):
        recipient_country_code (str | Unset):
        tags (str | Unset):
    """

    kind: PaysheetAttributesKind | Unset = UNSET
    number: str | Unset = UNSET
    issue_date: datetime.date | Unset = UNSET
    paid_at: datetime.date | None | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    payment_status: PaysheetAttributesPaymentStatus | Unset = UNSET
    net_pay: str | Unset = UNSET
    gross_pay: str | Unset = UNSET
    employee_ss_amount: str | Unset = UNSET
    employee_retention: str | Unset = UNSET
    company_ss_amount: str | Unset = UNSET
    issuing_name: str | Unset = UNSET
    issuing_tax_id: str | Unset = UNSET
    issuing_address: str | Unset = UNSET
    issuing_phone: str | Unset = UNSET
    issuing_town: str | Unset = UNSET
    issuing_zip_code: str | Unset = UNSET
    issuing_country_code: str | Unset = UNSET
    recipient_name: str | Unset = UNSET
    recipient_tax_id: str | Unset = UNSET
    recipient_address: str | Unset = UNSET
    recipient_phone: str | Unset = UNSET
    recipient_town: str | Unset = UNSET
    recipient_zip_code: str | Unset = UNSET
    recipient_country_code: str | Unset = UNSET
    tags: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        number = self.number

        issue_date: str | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        paid_at: None | str | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.date):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        net_pay = self.net_pay

        gross_pay = self.gross_pay

        employee_ss_amount = self.employee_ss_amount

        employee_retention = self.employee_retention

        company_ss_amount = self.company_ss_amount

        issuing_name = self.issuing_name

        issuing_tax_id = self.issuing_tax_id

        issuing_address = self.issuing_address

        issuing_phone = self.issuing_phone

        issuing_town = self.issuing_town

        issuing_zip_code = self.issuing_zip_code

        issuing_country_code = self.issuing_country_code

        recipient_name = self.recipient_name

        recipient_tax_id = self.recipient_tax_id

        recipient_address = self.recipient_address

        recipient_phone = self.recipient_phone

        recipient_town = self.recipient_town

        recipient_zip_code = self.recipient_zip_code

        recipient_country_code = self.recipient_country_code

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if number is not UNSET:
            field_dict["number"] = number
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
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
        if issuing_name is not UNSET:
            field_dict["issuing_name"] = issuing_name
        if issuing_tax_id is not UNSET:
            field_dict["issuing_tax_id"] = issuing_tax_id
        if issuing_address is not UNSET:
            field_dict["issuing_address"] = issuing_address
        if issuing_phone is not UNSET:
            field_dict["issuing_phone"] = issuing_phone
        if issuing_town is not UNSET:
            field_dict["issuing_town"] = issuing_town
        if issuing_zip_code is not UNSET:
            field_dict["issuing_zip_code"] = issuing_zip_code
        if issuing_country_code is not UNSET:
            field_dict["issuing_country_code"] = issuing_country_code
        if recipient_name is not UNSET:
            field_dict["recipient_name"] = recipient_name
        if recipient_tax_id is not UNSET:
            field_dict["recipient_tax_id"] = recipient_tax_id
        if recipient_address is not UNSET:
            field_dict["recipient_address"] = recipient_address
        if recipient_phone is not UNSET:
            field_dict["recipient_phone"] = recipient_phone
        if recipient_town is not UNSET:
            field_dict["recipient_town"] = recipient_town
        if recipient_zip_code is not UNSET:
            field_dict["recipient_zip_code"] = recipient_zip_code
        if recipient_country_code is not UNSET:
            field_dict["recipient_country_code"] = recipient_country_code
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: PaysheetAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PaysheetAttributesKind(_kind)

        number = d.pop("number", UNSET)

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: datetime.date | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date).date()

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

        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("payment_method", UNSET))

        _payment_status = d.pop("payment_status", UNSET)
        payment_status: PaysheetAttributesPaymentStatus | Unset
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = PaysheetAttributesPaymentStatus(_payment_status)

        net_pay = d.pop("net_pay", UNSET)

        gross_pay = d.pop("gross_pay", UNSET)

        employee_ss_amount = d.pop("employee_ss_amount", UNSET)

        employee_retention = d.pop("employee_retention", UNSET)

        company_ss_amount = d.pop("company_ss_amount", UNSET)

        issuing_name = d.pop("issuing_name", UNSET)

        issuing_tax_id = d.pop("issuing_tax_id", UNSET)

        issuing_address = d.pop("issuing_address", UNSET)

        issuing_phone = d.pop("issuing_phone", UNSET)

        issuing_town = d.pop("issuing_town", UNSET)

        issuing_zip_code = d.pop("issuing_zip_code", UNSET)

        issuing_country_code = d.pop("issuing_country_code", UNSET)

        recipient_name = d.pop("recipient_name", UNSET)

        recipient_tax_id = d.pop("recipient_tax_id", UNSET)

        recipient_address = d.pop("recipient_address", UNSET)

        recipient_phone = d.pop("recipient_phone", UNSET)

        recipient_town = d.pop("recipient_town", UNSET)

        recipient_zip_code = d.pop("recipient_zip_code", UNSET)

        recipient_country_code = d.pop("recipient_country_code", UNSET)

        tags = d.pop("tags", UNSET)

        paysheet_attributes = cls(
            kind=kind,
            number=number,
            issue_date=issue_date,
            paid_at=paid_at,
            payment_method=payment_method,
            payment_status=payment_status,
            net_pay=net_pay,
            gross_pay=gross_pay,
            employee_ss_amount=employee_ss_amount,
            employee_retention=employee_retention,
            company_ss_amount=company_ss_amount,
            issuing_name=issuing_name,
            issuing_tax_id=issuing_tax_id,
            issuing_address=issuing_address,
            issuing_phone=issuing_phone,
            issuing_town=issuing_town,
            issuing_zip_code=issuing_zip_code,
            issuing_country_code=issuing_country_code,
            recipient_name=recipient_name,
            recipient_tax_id=recipient_tax_id,
            recipient_address=recipient_address,
            recipient_phone=recipient_phone,
            recipient_town=recipient_town,
            recipient_zip_code=recipient_zip_code,
            recipient_country_code=recipient_country_code,
            tags=tags,
        )

        paysheet_attributes.additional_properties = d
        return paysheet_attributes

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

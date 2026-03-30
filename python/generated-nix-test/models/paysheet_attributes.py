from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.book_entry_attributes_payment_status import BookEntryAttributesPaymentStatus
from ..models.paysheet_attributes_kind import PaysheetAttributesKind
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PaysheetAttributes")



@_attrs_define
class PaysheetAttributes:
    """ 
        Attributes:
            number (None | str | Unset):
            issue_date (datetime.date | Unset):
            due_dates (list[datetime.date] | None | Unset):
            paid_at (datetime.date | None | Unset):
            payment_method (None | str | Unset):
            payment_status (BookEntryAttributesPaymentStatus | Unset):
            total_amount (str | Unset):
            tags (list[str] | Unset):
            issuing_name (str | Unset):
            issuing_tax_id (str | Unset):
            issuing_address (None | str | Unset):
            issuing_phone (None | str | Unset):
            issuing_town (None | str | Unset):
            issuing_zip_code (None | str | Unset):
            issuing_country_code (None | str | Unset):
            recipient_name (None | str | Unset):
            recipient_tax_id (None | str | Unset):
            recipient_address (None | str | Unset):
            recipient_phone (None | str | Unset):
            recipient_town (None | str | Unset):
            recipient_zip_code (None | str | Unset):
            recipient_country_code (None | str | Unset):
            kind (PaysheetAttributesKind | Unset):
            net_pay (str | Unset):
            gross_pay (str | Unset):
            employee_ss_amount (str | Unset):
            employee_retention (str | Unset):
            company_ss_amount (str | Unset):
     """

    number: None | str | Unset = UNSET
    issue_date: datetime.date | Unset = UNSET
    due_dates: list[datetime.date] | None | Unset = UNSET
    paid_at: datetime.date | None | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    payment_status: BookEntryAttributesPaymentStatus | Unset = UNSET
    total_amount: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    issuing_name: str | Unset = UNSET
    issuing_tax_id: str | Unset = UNSET
    issuing_address: None | str | Unset = UNSET
    issuing_phone: None | str | Unset = UNSET
    issuing_town: None | str | Unset = UNSET
    issuing_zip_code: None | str | Unset = UNSET
    issuing_country_code: None | str | Unset = UNSET
    recipient_name: None | str | Unset = UNSET
    recipient_tax_id: None | str | Unset = UNSET
    recipient_address: None | str | Unset = UNSET
    recipient_phone: None | str | Unset = UNSET
    recipient_town: None | str | Unset = UNSET
    recipient_zip_code: None | str | Unset = UNSET
    recipient_country_code: None | str | Unset = UNSET
    kind: PaysheetAttributesKind | Unset = UNSET
    net_pay: str | Unset = UNSET
    gross_pay: str | Unset = UNSET
    employee_ss_amount: str | Unset = UNSET
    employee_retention: str | Unset = UNSET
    company_ss_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        number: None | str | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        issue_date: str | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        due_dates: list[str] | None | Unset
        if isinstance(self.due_dates, Unset):
            due_dates = UNSET
        elif isinstance(self.due_dates, list):
            due_dates = []
            for due_dates_type_0_item_data in self.due_dates:
                due_dates_type_0_item = due_dates_type_0_item_data.isoformat()
                due_dates.append(due_dates_type_0_item)


        else:
            due_dates = self.due_dates

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


        total_amount = self.total_amount

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        issuing_name = self.issuing_name

        issuing_tax_id = self.issuing_tax_id

        issuing_address: None | str | Unset
        if isinstance(self.issuing_address, Unset):
            issuing_address = UNSET
        else:
            issuing_address = self.issuing_address

        issuing_phone: None | str | Unset
        if isinstance(self.issuing_phone, Unset):
            issuing_phone = UNSET
        else:
            issuing_phone = self.issuing_phone

        issuing_town: None | str | Unset
        if isinstance(self.issuing_town, Unset):
            issuing_town = UNSET
        else:
            issuing_town = self.issuing_town

        issuing_zip_code: None | str | Unset
        if isinstance(self.issuing_zip_code, Unset):
            issuing_zip_code = UNSET
        else:
            issuing_zip_code = self.issuing_zip_code

        issuing_country_code: None | str | Unset
        if isinstance(self.issuing_country_code, Unset):
            issuing_country_code = UNSET
        else:
            issuing_country_code = self.issuing_country_code

        recipient_name: None | str | Unset
        if isinstance(self.recipient_name, Unset):
            recipient_name = UNSET
        else:
            recipient_name = self.recipient_name

        recipient_tax_id: None | str | Unset
        if isinstance(self.recipient_tax_id, Unset):
            recipient_tax_id = UNSET
        else:
            recipient_tax_id = self.recipient_tax_id

        recipient_address: None | str | Unset
        if isinstance(self.recipient_address, Unset):
            recipient_address = UNSET
        else:
            recipient_address = self.recipient_address

        recipient_phone: None | str | Unset
        if isinstance(self.recipient_phone, Unset):
            recipient_phone = UNSET
        else:
            recipient_phone = self.recipient_phone

        recipient_town: None | str | Unset
        if isinstance(self.recipient_town, Unset):
            recipient_town = UNSET
        else:
            recipient_town = self.recipient_town

        recipient_zip_code: None | str | Unset
        if isinstance(self.recipient_zip_code, Unset):
            recipient_zip_code = UNSET
        else:
            recipient_zip_code = self.recipient_zip_code

        recipient_country_code: None | str | Unset
        if isinstance(self.recipient_country_code, Unset):
            recipient_country_code = UNSET
        else:
            recipient_country_code = self.recipient_country_code

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        net_pay = self.net_pay

        gross_pay = self.gross_pay

        employee_ss_amount = self.employee_ss_amount

        employee_retention = self.employee_retention

        company_ss_amount = self.company_ss_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if number is not UNSET:
            field_dict["number"] = number
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if due_dates is not UNSET:
            field_dict["due_dates"] = due_dates
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount
        if tags is not UNSET:
            field_dict["tags"] = tags
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
        if kind is not UNSET:
            field_dict["kind"] = kind
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
        def _parse_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number = _parse_number(d.pop("number", UNSET))


        _issue_date = d.pop("issue_date", UNSET)
        issue_date: datetime.date | Unset
        if isinstance(_issue_date,  Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date).date()




        def _parse_due_dates(data: object) -> list[datetime.date] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                due_dates_type_0 = []
                _due_dates_type_0 = data
                for due_dates_type_0_item_data in (_due_dates_type_0):
                    due_dates_type_0_item = isoparse(due_dates_type_0_item_data).date()



                    due_dates_type_0.append(due_dates_type_0_item)

                return due_dates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[datetime.date] | None | Unset, data)

        due_dates = _parse_due_dates(d.pop("due_dates", UNSET))


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
        payment_status: BookEntryAttributesPaymentStatus | Unset
        if isinstance(_payment_status,  Unset):
            payment_status = UNSET
        else:
            payment_status = BookEntryAttributesPaymentStatus(_payment_status)




        total_amount = d.pop("total_amount", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        issuing_name = d.pop("issuing_name", UNSET)

        issuing_tax_id = d.pop("issuing_tax_id", UNSET)

        def _parse_issuing_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuing_address = _parse_issuing_address(d.pop("issuing_address", UNSET))


        def _parse_issuing_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuing_phone = _parse_issuing_phone(d.pop("issuing_phone", UNSET))


        def _parse_issuing_town(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuing_town = _parse_issuing_town(d.pop("issuing_town", UNSET))


        def _parse_issuing_zip_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuing_zip_code = _parse_issuing_zip_code(d.pop("issuing_zip_code", UNSET))


        def _parse_issuing_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuing_country_code = _parse_issuing_country_code(d.pop("issuing_country_code", UNSET))


        def _parse_recipient_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_name = _parse_recipient_name(d.pop("recipient_name", UNSET))


        def _parse_recipient_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_tax_id = _parse_recipient_tax_id(d.pop("recipient_tax_id", UNSET))


        def _parse_recipient_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_address = _parse_recipient_address(d.pop("recipient_address", UNSET))


        def _parse_recipient_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_phone = _parse_recipient_phone(d.pop("recipient_phone", UNSET))


        def _parse_recipient_town(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_town = _parse_recipient_town(d.pop("recipient_town", UNSET))


        def _parse_recipient_zip_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_zip_code = _parse_recipient_zip_code(d.pop("recipient_zip_code", UNSET))


        def _parse_recipient_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_country_code = _parse_recipient_country_code(d.pop("recipient_country_code", UNSET))


        _kind = d.pop("kind", UNSET)
        kind: PaysheetAttributesKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = PaysheetAttributesKind(_kind)




        net_pay = d.pop("net_pay", UNSET)

        gross_pay = d.pop("gross_pay", UNSET)

        employee_ss_amount = d.pop("employee_ss_amount", UNSET)

        employee_retention = d.pop("employee_retention", UNSET)

        company_ss_amount = d.pop("company_ss_amount", UNSET)

        paysheet_attributes = cls(
            number=number,
            issue_date=issue_date,
            due_dates=due_dates,
            paid_at=paid_at,
            payment_method=payment_method,
            payment_status=payment_status,
            total_amount=total_amount,
            tags=tags,
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
            kind=kind,
            net_pay=net_pay,
            gross_pay=gross_pay,
            employee_ss_amount=employee_ss_amount,
            employee_retention=employee_retention,
            company_ss_amount=company_ss_amount,
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

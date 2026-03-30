from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ticket_attributes_kind import TicketAttributesKind
from ..models.ticket_attributes_payment_method import TicketAttributesPaymentMethod
from ..models.ticket_attributes_payment_status import TicketAttributesPaymentStatus
from ..models.ticket_attributes_validation_status import TicketAttributesValidationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketAttributes")


@_attrs_define
class TicketAttributes:
    """
    Attributes:
        kind (TicketAttributesKind | Unset):
        number (str | Unset):
        issue_date (datetime.date | Unset):
        paid_at (datetime.date | None | Unset):
        payment_method (TicketAttributesPaymentMethod | Unset):
        payment_status (TicketAttributesPaymentStatus | Unset):
        validation_status (TicketAttributesValidationStatus | Unset):
        total_amount (str | Unset):
        total_amount_without_taxes (str | Unset):
        vat_amount (str | Unset):
        issuing_name (str | Unset):
        issuing_tax_id (None | str | Unset):
        issuing_address (None | str | Unset):
        issuing_phone (None | str | Unset):
        issuing_town (None | str | Unset):
        issuing_zip_code (None | str | Unset):
        issuing_country_code (None | str | Unset):
        recipient_name (str | Unset):
        recipient_tax_id (str | Unset):
        recipient_address (str | Unset):
        recipient_phone (str | Unset):
        recipient_town (str | Unset):
        recipient_zip_code (str | Unset):
        recipient_country_code (str | Unset):
        tags (str | Unset):
        notes (str | Unset):
        download_pdf_url (str | Unset):
    """

    kind: TicketAttributesKind | Unset = UNSET
    number: str | Unset = UNSET
    issue_date: datetime.date | Unset = UNSET
    paid_at: datetime.date | None | Unset = UNSET
    payment_method: TicketAttributesPaymentMethod | Unset = UNSET
    payment_status: TicketAttributesPaymentStatus | Unset = UNSET
    validation_status: TicketAttributesValidationStatus | Unset = UNSET
    total_amount: str | Unset = UNSET
    total_amount_without_taxes: str | Unset = UNSET
    vat_amount: str | Unset = UNSET
    issuing_name: str | Unset = UNSET
    issuing_tax_id: None | str | Unset = UNSET
    issuing_address: None | str | Unset = UNSET
    issuing_phone: None | str | Unset = UNSET
    issuing_town: None | str | Unset = UNSET
    issuing_zip_code: None | str | Unset = UNSET
    issuing_country_code: None | str | Unset = UNSET
    recipient_name: str | Unset = UNSET
    recipient_tax_id: str | Unset = UNSET
    recipient_address: str | Unset = UNSET
    recipient_phone: str | Unset = UNSET
    recipient_town: str | Unset = UNSET
    recipient_zip_code: str | Unset = UNSET
    recipient_country_code: str | Unset = UNSET
    tags: str | Unset = UNSET
    notes: str | Unset = UNSET
    download_pdf_url: str | Unset = UNSET
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

        payment_method: str | Unset = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        validation_status: str | Unset = UNSET
        if not isinstance(self.validation_status, Unset):
            validation_status = self.validation_status.value

        total_amount = self.total_amount

        total_amount_without_taxes = self.total_amount_without_taxes

        vat_amount = self.vat_amount

        issuing_name = self.issuing_name

        issuing_tax_id: None | str | Unset
        if isinstance(self.issuing_tax_id, Unset):
            issuing_tax_id = UNSET
        else:
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

        recipient_name = self.recipient_name

        recipient_tax_id = self.recipient_tax_id

        recipient_address = self.recipient_address

        recipient_phone = self.recipient_phone

        recipient_town = self.recipient_town

        recipient_zip_code = self.recipient_zip_code

        recipient_country_code = self.recipient_country_code

        tags = self.tags

        notes = self.notes

        download_pdf_url = self.download_pdf_url

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
        if validation_status is not UNSET:
            field_dict["validation_status"] = validation_status
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount
        if total_amount_without_taxes is not UNSET:
            field_dict["total_amount_without_taxes"] = total_amount_without_taxes
        if vat_amount is not UNSET:
            field_dict["vat_amount"] = vat_amount
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
        if notes is not UNSET:
            field_dict["notes"] = notes
        if download_pdf_url is not UNSET:
            field_dict["download_pdf_url"] = download_pdf_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: TicketAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = TicketAttributesKind(_kind)

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

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: TicketAttributesPaymentMethod | Unset
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = TicketAttributesPaymentMethod(_payment_method)

        _payment_status = d.pop("payment_status", UNSET)
        payment_status: TicketAttributesPaymentStatus | Unset
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = TicketAttributesPaymentStatus(_payment_status)

        _validation_status = d.pop("validation_status", UNSET)
        validation_status: TicketAttributesValidationStatus | Unset
        if isinstance(_validation_status, Unset):
            validation_status = UNSET
        else:
            validation_status = TicketAttributesValidationStatus(_validation_status)

        total_amount = d.pop("total_amount", UNSET)

        total_amount_without_taxes = d.pop("total_amount_without_taxes", UNSET)

        vat_amount = d.pop("vat_amount", UNSET)

        issuing_name = d.pop("issuing_name", UNSET)

        def _parse_issuing_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuing_tax_id = _parse_issuing_tax_id(d.pop("issuing_tax_id", UNSET))

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

        recipient_name = d.pop("recipient_name", UNSET)

        recipient_tax_id = d.pop("recipient_tax_id", UNSET)

        recipient_address = d.pop("recipient_address", UNSET)

        recipient_phone = d.pop("recipient_phone", UNSET)

        recipient_town = d.pop("recipient_town", UNSET)

        recipient_zip_code = d.pop("recipient_zip_code", UNSET)

        recipient_country_code = d.pop("recipient_country_code", UNSET)

        tags = d.pop("tags", UNSET)

        notes = d.pop("notes", UNSET)

        download_pdf_url = d.pop("download_pdf_url", UNSET)

        ticket_attributes = cls(
            kind=kind,
            number=number,
            issue_date=issue_date,
            paid_at=paid_at,
            payment_method=payment_method,
            payment_status=payment_status,
            validation_status=validation_status,
            total_amount=total_amount,
            total_amount_without_taxes=total_amount_without_taxes,
            vat_amount=vat_amount,
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
            notes=notes,
            download_pdf_url=download_pdf_url,
        )

        ticket_attributes.additional_properties = d
        return ticket_attributes

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

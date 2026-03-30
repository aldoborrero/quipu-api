from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.book_entry_attributes_payment_status import BookEntryAttributesPaymentStatus
from ..models.invoice_attributes_kind import InvoiceAttributesKind
from ..models.invoice_attributes_stage import InvoiceAttributesStage
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="InvoiceAttributes")



@_attrs_define
class InvoiceAttributes:
    """ 
        Attributes:
            number (Union[None, Unset, str]):
            issue_date (Union[Unset, datetime.date]):
            due_dates (Union[None, Unset, list[datetime.date]]):
            paid_at (Union[None, Unset, datetime.date]):
            payment_method (Union[None, Unset, str]):
            payment_status (Union[Unset, BookEntryAttributesPaymentStatus]):
            total_amount (Union[Unset, str]):
            tags (Union[Unset, list[str]]):
            issuing_name (Union[Unset, str]):
            issuing_tax_id (Union[Unset, str]):
            issuing_address (Union[None, Unset, str]):
            issuing_phone (Union[None, Unset, str]):
            issuing_town (Union[None, Unset, str]):
            issuing_zip_code (Union[None, Unset, str]):
            issuing_country_code (Union[None, Unset, str]):
            recipient_name (Union[None, Unset, str]):
            recipient_tax_id (Union[None, Unset, str]):
            recipient_address (Union[None, Unset, str]):
            recipient_phone (Union[None, Unset, str]):
            recipient_town (Union[None, Unset, str]):
            recipient_zip_code (Union[None, Unset, str]):
            recipient_country_code (Union[None, Unset, str]):
            kind (Union[Unset, InvoiceAttributesKind]):
            total_amount_without_taxes (Union[Unset, str]):
            vat_amount (Union[Unset, str]):
            retention_amount (Union[Unset, str]):
            last_sent_at (Union[None, Unset, datetime.datetime]):
            notes (Union[None, Unset, str]):
            stage (Union[Unset, InvoiceAttributesStage]):
            download_pdf_url (Union[None, Unset, str]):
            ephemeral_open_download_pdf_url (Union[None, Unset, str]):
     """

    number: Union[None, Unset, str] = UNSET
    issue_date: Union[Unset, datetime.date] = UNSET
    due_dates: Union[None, Unset, list[datetime.date]] = UNSET
    paid_at: Union[None, Unset, datetime.date] = UNSET
    payment_method: Union[None, Unset, str] = UNSET
    payment_status: Union[Unset, BookEntryAttributesPaymentStatus] = UNSET
    total_amount: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    issuing_name: Union[Unset, str] = UNSET
    issuing_tax_id: Union[Unset, str] = UNSET
    issuing_address: Union[None, Unset, str] = UNSET
    issuing_phone: Union[None, Unset, str] = UNSET
    issuing_town: Union[None, Unset, str] = UNSET
    issuing_zip_code: Union[None, Unset, str] = UNSET
    issuing_country_code: Union[None, Unset, str] = UNSET
    recipient_name: Union[None, Unset, str] = UNSET
    recipient_tax_id: Union[None, Unset, str] = UNSET
    recipient_address: Union[None, Unset, str] = UNSET
    recipient_phone: Union[None, Unset, str] = UNSET
    recipient_town: Union[None, Unset, str] = UNSET
    recipient_zip_code: Union[None, Unset, str] = UNSET
    recipient_country_code: Union[None, Unset, str] = UNSET
    kind: Union[Unset, InvoiceAttributesKind] = UNSET
    total_amount_without_taxes: Union[Unset, str] = UNSET
    vat_amount: Union[Unset, str] = UNSET
    retention_amount: Union[Unset, str] = UNSET
    last_sent_at: Union[None, Unset, datetime.datetime] = UNSET
    notes: Union[None, Unset, str] = UNSET
    stage: Union[Unset, InvoiceAttributesStage] = UNSET
    download_pdf_url: Union[None, Unset, str] = UNSET
    ephemeral_open_download_pdf_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        due_dates: Union[None, Unset, list[str]]
        if isinstance(self.due_dates, Unset):
            due_dates = UNSET
        elif isinstance(self.due_dates, list):
            due_dates = []
            for due_dates_type_0_item_data in self.due_dates:
                due_dates_type_0_item = due_dates_type_0_item_data.isoformat()
                due_dates.append(due_dates_type_0_item)


        else:
            due_dates = self.due_dates

        paid_at: Union[None, Unset, str]
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.date):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        payment_method: Union[None, Unset, str]
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        payment_status: Union[Unset, str] = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value


        total_amount = self.total_amount

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        issuing_name = self.issuing_name

        issuing_tax_id = self.issuing_tax_id

        issuing_address: Union[None, Unset, str]
        if isinstance(self.issuing_address, Unset):
            issuing_address = UNSET
        else:
            issuing_address = self.issuing_address

        issuing_phone: Union[None, Unset, str]
        if isinstance(self.issuing_phone, Unset):
            issuing_phone = UNSET
        else:
            issuing_phone = self.issuing_phone

        issuing_town: Union[None, Unset, str]
        if isinstance(self.issuing_town, Unset):
            issuing_town = UNSET
        else:
            issuing_town = self.issuing_town

        issuing_zip_code: Union[None, Unset, str]
        if isinstance(self.issuing_zip_code, Unset):
            issuing_zip_code = UNSET
        else:
            issuing_zip_code = self.issuing_zip_code

        issuing_country_code: Union[None, Unset, str]
        if isinstance(self.issuing_country_code, Unset):
            issuing_country_code = UNSET
        else:
            issuing_country_code = self.issuing_country_code

        recipient_name: Union[None, Unset, str]
        if isinstance(self.recipient_name, Unset):
            recipient_name = UNSET
        else:
            recipient_name = self.recipient_name

        recipient_tax_id: Union[None, Unset, str]
        if isinstance(self.recipient_tax_id, Unset):
            recipient_tax_id = UNSET
        else:
            recipient_tax_id = self.recipient_tax_id

        recipient_address: Union[None, Unset, str]
        if isinstance(self.recipient_address, Unset):
            recipient_address = UNSET
        else:
            recipient_address = self.recipient_address

        recipient_phone: Union[None, Unset, str]
        if isinstance(self.recipient_phone, Unset):
            recipient_phone = UNSET
        else:
            recipient_phone = self.recipient_phone

        recipient_town: Union[None, Unset, str]
        if isinstance(self.recipient_town, Unset):
            recipient_town = UNSET
        else:
            recipient_town = self.recipient_town

        recipient_zip_code: Union[None, Unset, str]
        if isinstance(self.recipient_zip_code, Unset):
            recipient_zip_code = UNSET
        else:
            recipient_zip_code = self.recipient_zip_code

        recipient_country_code: Union[None, Unset, str]
        if isinstance(self.recipient_country_code, Unset):
            recipient_country_code = UNSET
        else:
            recipient_country_code = self.recipient_country_code

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        total_amount_without_taxes = self.total_amount_without_taxes

        vat_amount = self.vat_amount

        retention_amount = self.retention_amount

        last_sent_at: Union[None, Unset, str]
        if isinstance(self.last_sent_at, Unset):
            last_sent_at = UNSET
        elif isinstance(self.last_sent_at, datetime.datetime):
            last_sent_at = self.last_sent_at.isoformat()
        else:
            last_sent_at = self.last_sent_at

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        stage: Union[Unset, str] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.value


        download_pdf_url: Union[None, Unset, str]
        if isinstance(self.download_pdf_url, Unset):
            download_pdf_url = UNSET
        else:
            download_pdf_url = self.download_pdf_url

        ephemeral_open_download_pdf_url: Union[None, Unset, str]
        if isinstance(self.ephemeral_open_download_pdf_url, Unset):
            ephemeral_open_download_pdf_url = UNSET
        else:
            ephemeral_open_download_pdf_url = self.ephemeral_open_download_pdf_url


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
        if total_amount_without_taxes is not UNSET:
            field_dict["total_amount_without_taxes"] = total_amount_without_taxes
        if vat_amount is not UNSET:
            field_dict["vat_amount"] = vat_amount
        if retention_amount is not UNSET:
            field_dict["retention_amount"] = retention_amount
        if last_sent_at is not UNSET:
            field_dict["last_sent_at"] = last_sent_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if stage is not UNSET:
            field_dict["stage"] = stage
        if download_pdf_url is not UNSET:
            field_dict["download_pdf_url"] = download_pdf_url
        if ephemeral_open_download_pdf_url is not UNSET:
            field_dict["ephemeral_open_download_pdf_url"] = ephemeral_open_download_pdf_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))


        _issue_date = d.pop("issue_date", UNSET)
        issue_date: Union[Unset, datetime.date]
        if isinstance(_issue_date,  Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date).date()




        def _parse_due_dates(data: object) -> Union[None, Unset, list[datetime.date]]:
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
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[datetime.date]], data)

        due_dates = _parse_due_dates(d.pop("due_dates", UNSET))


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


        def _parse_payment_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_method = _parse_payment_method(d.pop("payment_method", UNSET))


        _payment_status = d.pop("payment_status", UNSET)
        payment_status: Union[Unset, BookEntryAttributesPaymentStatus]
        if isinstance(_payment_status,  Unset):
            payment_status = UNSET
        else:
            payment_status = BookEntryAttributesPaymentStatus(_payment_status)




        total_amount = d.pop("total_amount", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        issuing_name = d.pop("issuing_name", UNSET)

        issuing_tax_id = d.pop("issuing_tax_id", UNSET)

        def _parse_issuing_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        issuing_address = _parse_issuing_address(d.pop("issuing_address", UNSET))


        def _parse_issuing_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        issuing_phone = _parse_issuing_phone(d.pop("issuing_phone", UNSET))


        def _parse_issuing_town(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        issuing_town = _parse_issuing_town(d.pop("issuing_town", UNSET))


        def _parse_issuing_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        issuing_zip_code = _parse_issuing_zip_code(d.pop("issuing_zip_code", UNSET))


        def _parse_issuing_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        issuing_country_code = _parse_issuing_country_code(d.pop("issuing_country_code", UNSET))


        def _parse_recipient_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recipient_name = _parse_recipient_name(d.pop("recipient_name", UNSET))


        def _parse_recipient_tax_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recipient_tax_id = _parse_recipient_tax_id(d.pop("recipient_tax_id", UNSET))


        def _parse_recipient_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recipient_address = _parse_recipient_address(d.pop("recipient_address", UNSET))


        def _parse_recipient_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recipient_phone = _parse_recipient_phone(d.pop("recipient_phone", UNSET))


        def _parse_recipient_town(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recipient_town = _parse_recipient_town(d.pop("recipient_town", UNSET))


        def _parse_recipient_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recipient_zip_code = _parse_recipient_zip_code(d.pop("recipient_zip_code", UNSET))


        def _parse_recipient_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recipient_country_code = _parse_recipient_country_code(d.pop("recipient_country_code", UNSET))


        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, InvoiceAttributesKind]
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = InvoiceAttributesKind(_kind)




        total_amount_without_taxes = d.pop("total_amount_without_taxes", UNSET)

        vat_amount = d.pop("vat_amount", UNSET)

        retention_amount = d.pop("retention_amount", UNSET)

        def _parse_last_sent_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sent_at_type_0 = isoparse(data)



                return last_sent_at_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_sent_at = _parse_last_sent_at(d.pop("last_sent_at", UNSET))


        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))


        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, InvoiceAttributesStage]
        if isinstance(_stage,  Unset):
            stage = UNSET
        else:
            stage = InvoiceAttributesStage(_stage)




        def _parse_download_pdf_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_pdf_url = _parse_download_pdf_url(d.pop("download_pdf_url", UNSET))


        def _parse_ephemeral_open_download_pdf_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ephemeral_open_download_pdf_url = _parse_ephemeral_open_download_pdf_url(d.pop("ephemeral_open_download_pdf_url", UNSET))


        invoice_attributes = cls(
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
            total_amount_without_taxes=total_amount_without_taxes,
            vat_amount=vat_amount,
            retention_amount=retention_amount,
            last_sent_at=last_sent_at,
            notes=notes,
            stage=stage,
            download_pdf_url=download_pdf_url,
            ephemeral_open_download_pdf_url=ephemeral_open_download_pdf_url,
        )


        invoice_attributes.additional_properties = d
        return invoice_attributes

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

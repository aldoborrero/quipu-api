from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_writable_attributes_canary_island_special_zone import InvoiceWritableAttributesCanaryIslandSpecialZone
from ..models.invoice_writable_attributes_collection_type import InvoiceWritableAttributesCollectionType
from ..models.invoice_writable_attributes_credit_note_reason import InvoiceWritableAttributesCreditNoteReason
from ..models.invoice_writable_attributes_exempt_reason import InvoiceWritableAttributesExemptReason
from ..models.invoice_writable_attributes_kind import InvoiceWritableAttributesKind
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="InvoiceWritableAttributes")



@_attrs_define
class InvoiceWritableAttributes:
    """ 
        Attributes:
            kind (InvoiceWritableAttributesKind): Whether this is an income or expense invoice (REQUIRED)
            issue_date (datetime.date): Issue date (REQUIRED)
            filing_number (None | str | Unset):
            due_dates (list[datetime.date] | Unset):
            due_date_intervals (list[int] | Unset): Due date intervals in days from issue date
            paid_at (datetime.date | None | Unset):
            payment_method (str | Unset):
            tags (list[str] | Unset):
            notes (str | Unset):
            equivalence_surcharge (bool | Unset): Whether equivalence surcharge applies
            credit_note_reason (InvoiceWritableAttributesCreditNoteReason | Unset): Reason code for credit notes
            exempt_reason (InvoiceWritableAttributesExemptReason | Unset): Reason code for VAT exemption
            collection_type (InvoiceWritableAttributesCollectionType | Unset): Collection type
            canary_island_special_zone (InvoiceWritableAttributesCanaryIslandSpecialZone | Unset): Canary Island special
                zone indicator
            account_number_and_swift_bic (str | Unset): Bank account number and SWIFT/BIC code
     """

    kind: InvoiceWritableAttributesKind
    issue_date: datetime.date
    filing_number: None | str | Unset = UNSET
    due_dates: list[datetime.date] | Unset = UNSET
    due_date_intervals: list[int] | Unset = UNSET
    paid_at: datetime.date | None | Unset = UNSET
    payment_method: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    notes: str | Unset = UNSET
    equivalence_surcharge: bool | Unset = UNSET
    credit_note_reason: InvoiceWritableAttributesCreditNoteReason | Unset = UNSET
    exempt_reason: InvoiceWritableAttributesExemptReason | Unset = UNSET
    collection_type: InvoiceWritableAttributesCollectionType | Unset = UNSET
    canary_island_special_zone: InvoiceWritableAttributesCanaryIslandSpecialZone | Unset = UNSET
    account_number_and_swift_bic: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        issue_date = self.issue_date.isoformat()

        filing_number: None | str | Unset
        if isinstance(self.filing_number, Unset):
            filing_number = UNSET
        else:
            filing_number = self.filing_number

        due_dates: list[str] | Unset = UNSET
        if not isinstance(self.due_dates, Unset):
            due_dates = []
            for due_dates_item_data in self.due_dates:
                due_dates_item = due_dates_item_data.isoformat()
                due_dates.append(due_dates_item)



        due_date_intervals: list[int] | Unset = UNSET
        if not isinstance(self.due_date_intervals, Unset):
            due_date_intervals = self.due_date_intervals



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



        notes = self.notes

        equivalence_surcharge = self.equivalence_surcharge

        credit_note_reason: str | Unset = UNSET
        if not isinstance(self.credit_note_reason, Unset):
            credit_note_reason = self.credit_note_reason.value


        exempt_reason: str | Unset = UNSET
        if not isinstance(self.exempt_reason, Unset):
            exempt_reason = self.exempt_reason.value


        collection_type: str | Unset = UNSET
        if not isinstance(self.collection_type, Unset):
            collection_type = self.collection_type.value


        canary_island_special_zone: str | Unset = UNSET
        if not isinstance(self.canary_island_special_zone, Unset):
            canary_island_special_zone = self.canary_island_special_zone.value


        account_number_and_swift_bic = self.account_number_and_swift_bic


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
        if due_date_intervals is not UNSET:
            field_dict["due_date_intervals"] = due_date_intervals
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if tags is not UNSET:
            field_dict["tags"] = tags
        if notes is not UNSET:
            field_dict["notes"] = notes
        if equivalence_surcharge is not UNSET:
            field_dict["equivalence_surcharge"] = equivalence_surcharge
        if credit_note_reason is not UNSET:
            field_dict["credit_note_reason"] = credit_note_reason
        if exempt_reason is not UNSET:
            field_dict["exempt_reason"] = exempt_reason
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if canary_island_special_zone is not UNSET:
            field_dict["canary_island_special_zone"] = canary_island_special_zone
        if account_number_and_swift_bic is not UNSET:
            field_dict["account_number_and_swift_bic"] = account_number_and_swift_bic

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = InvoiceWritableAttributesKind(d.pop("kind"))




        issue_date = isoparse(d.pop("issue_date")).date()




        def _parse_filing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filing_number = _parse_filing_number(d.pop("filing_number", UNSET))


        _due_dates = d.pop("due_dates", UNSET)
        due_dates: list[datetime.date] | Unset = UNSET
        if _due_dates is not UNSET:
            due_dates = []
            for due_dates_item_data in _due_dates:
                due_dates_item = isoparse(due_dates_item_data).date()



                due_dates.append(due_dates_item)


        due_date_intervals = cast(list[int], d.pop("due_date_intervals", UNSET))


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


        notes = d.pop("notes", UNSET)

        equivalence_surcharge = d.pop("equivalence_surcharge", UNSET)

        _credit_note_reason = d.pop("credit_note_reason", UNSET)
        credit_note_reason: InvoiceWritableAttributesCreditNoteReason | Unset
        if isinstance(_credit_note_reason,  Unset):
            credit_note_reason = UNSET
        else:
            credit_note_reason = InvoiceWritableAttributesCreditNoteReason(_credit_note_reason)




        _exempt_reason = d.pop("exempt_reason", UNSET)
        exempt_reason: InvoiceWritableAttributesExemptReason | Unset
        if isinstance(_exempt_reason,  Unset):
            exempt_reason = UNSET
        else:
            exempt_reason = InvoiceWritableAttributesExemptReason(_exempt_reason)




        _collection_type = d.pop("collection_type", UNSET)
        collection_type: InvoiceWritableAttributesCollectionType | Unset
        if isinstance(_collection_type,  Unset):
            collection_type = UNSET
        else:
            collection_type = InvoiceWritableAttributesCollectionType(_collection_type)




        _canary_island_special_zone = d.pop("canary_island_special_zone", UNSET)
        canary_island_special_zone: InvoiceWritableAttributesCanaryIslandSpecialZone | Unset
        if isinstance(_canary_island_special_zone,  Unset):
            canary_island_special_zone = UNSET
        else:
            canary_island_special_zone = InvoiceWritableAttributesCanaryIslandSpecialZone(_canary_island_special_zone)




        account_number_and_swift_bic = d.pop("account_number_and_swift_bic", UNSET)

        invoice_writable_attributes = cls(
            kind=kind,
            issue_date=issue_date,
            filing_number=filing_number,
            due_dates=due_dates,
            due_date_intervals=due_date_intervals,
            paid_at=paid_at,
            payment_method=payment_method,
            tags=tags,
            notes=notes,
            equivalence_surcharge=equivalence_surcharge,
            credit_note_reason=credit_note_reason,
            exempt_reason=exempt_reason,
            collection_type=collection_type,
            canary_island_special_zone=canary_island_special_zone,
            account_number_and_swift_bic=account_number_and_swift_bic,
        )


        invoice_writable_attributes.additional_properties = d
        return invoice_writable_attributes

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

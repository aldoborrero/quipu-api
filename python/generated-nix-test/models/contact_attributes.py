from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ContactAttributes")



@_attrs_define
class ContactAttributes:
    """ 
        Attributes:
            name (str | Unset):
            tax_id (str | Unset):
            phone (str | Unset):
            email (str | Unset):
            address (str | Unset):
            town (str | Unset):
            zip_code (str | Unset):
            country_code (str | Unset):  Example: ES.
            total_paid_incomes (str | Unset):
            total_unpaid_incomes (str | Unset):
            total_incomes (str | Unset):
            total_paid_expenses (str | Unset):
            total_unpaid_expenses (str | Unset):
            total_expenses (str | Unset):
            client_number (None | str | Unset):
            supplier_number (None | str | Unset):
            document_type (None | str | Unset):
            is_client (bool | Unset):
            is_supplier (bool | Unset):
            is_supplier_of_direct_goods (bool | Unset):
            bank_account_number (None | str | Unset):
            bank_account_swift_bic (None | str | Unset):
            deletable (bool | Unset):
     """

    name: str | Unset = UNSET
    tax_id: str | Unset = UNSET
    phone: str | Unset = UNSET
    email: str | Unset = UNSET
    address: str | Unset = UNSET
    town: str | Unset = UNSET
    zip_code: str | Unset = UNSET
    country_code: str | Unset = UNSET
    total_paid_incomes: str | Unset = UNSET
    total_unpaid_incomes: str | Unset = UNSET
    total_incomes: str | Unset = UNSET
    total_paid_expenses: str | Unset = UNSET
    total_unpaid_expenses: str | Unset = UNSET
    total_expenses: str | Unset = UNSET
    client_number: None | str | Unset = UNSET
    supplier_number: None | str | Unset = UNSET
    document_type: None | str | Unset = UNSET
    is_client: bool | Unset = UNSET
    is_supplier: bool | Unset = UNSET
    is_supplier_of_direct_goods: bool | Unset = UNSET
    bank_account_number: None | str | Unset = UNSET
    bank_account_swift_bic: None | str | Unset = UNSET
    deletable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tax_id = self.tax_id

        phone = self.phone

        email = self.email

        address = self.address

        town = self.town

        zip_code = self.zip_code

        country_code = self.country_code

        total_paid_incomes = self.total_paid_incomes

        total_unpaid_incomes = self.total_unpaid_incomes

        total_incomes = self.total_incomes

        total_paid_expenses = self.total_paid_expenses

        total_unpaid_expenses = self.total_unpaid_expenses

        total_expenses = self.total_expenses

        client_number: None | str | Unset
        if isinstance(self.client_number, Unset):
            client_number = UNSET
        else:
            client_number = self.client_number

        supplier_number: None | str | Unset
        if isinstance(self.supplier_number, Unset):
            supplier_number = UNSET
        else:
            supplier_number = self.supplier_number

        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        is_client = self.is_client

        is_supplier = self.is_supplier

        is_supplier_of_direct_goods = self.is_supplier_of_direct_goods

        bank_account_number: None | str | Unset
        if isinstance(self.bank_account_number, Unset):
            bank_account_number = UNSET
        else:
            bank_account_number = self.bank_account_number

        bank_account_swift_bic: None | str | Unset
        if isinstance(self.bank_account_swift_bic, Unset):
            bank_account_swift_bic = UNSET
        else:
            bank_account_swift_bic = self.bank_account_swift_bic

        deletable = self.deletable


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if address is not UNSET:
            field_dict["address"] = address
        if town is not UNSET:
            field_dict["town"] = town
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if total_paid_incomes is not UNSET:
            field_dict["total_paid_incomes"] = total_paid_incomes
        if total_unpaid_incomes is not UNSET:
            field_dict["total_unpaid_incomes"] = total_unpaid_incomes
        if total_incomes is not UNSET:
            field_dict["total_incomes"] = total_incomes
        if total_paid_expenses is not UNSET:
            field_dict["total_paid_expenses"] = total_paid_expenses
        if total_unpaid_expenses is not UNSET:
            field_dict["total_unpaid_expenses"] = total_unpaid_expenses
        if total_expenses is not UNSET:
            field_dict["total_expenses"] = total_expenses
        if client_number is not UNSET:
            field_dict["client_number"] = client_number
        if supplier_number is not UNSET:
            field_dict["supplier_number"] = supplier_number
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if is_client is not UNSET:
            field_dict["is_client"] = is_client
        if is_supplier is not UNSET:
            field_dict["is_supplier"] = is_supplier
        if is_supplier_of_direct_goods is not UNSET:
            field_dict["is_supplier_of_direct_goods"] = is_supplier_of_direct_goods
        if bank_account_number is not UNSET:
            field_dict["bank_account_number"] = bank_account_number
        if bank_account_swift_bic is not UNSET:
            field_dict["bank_account_swift_bic"] = bank_account_swift_bic
        if deletable is not UNSET:
            field_dict["deletable"] = deletable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        address = d.pop("address", UNSET)

        town = d.pop("town", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        country_code = d.pop("country_code", UNSET)

        total_paid_incomes = d.pop("total_paid_incomes", UNSET)

        total_unpaid_incomes = d.pop("total_unpaid_incomes", UNSET)

        total_incomes = d.pop("total_incomes", UNSET)

        total_paid_expenses = d.pop("total_paid_expenses", UNSET)

        total_unpaid_expenses = d.pop("total_unpaid_expenses", UNSET)

        total_expenses = d.pop("total_expenses", UNSET)

        def _parse_client_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_number = _parse_client_number(d.pop("client_number", UNSET))


        def _parse_supplier_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        supplier_number = _parse_supplier_number(d.pop("supplier_number", UNSET))


        def _parse_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type = _parse_document_type(d.pop("document_type", UNSET))


        is_client = d.pop("is_client", UNSET)

        is_supplier = d.pop("is_supplier", UNSET)

        is_supplier_of_direct_goods = d.pop("is_supplier_of_direct_goods", UNSET)

        def _parse_bank_account_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_account_number = _parse_bank_account_number(d.pop("bank_account_number", UNSET))


        def _parse_bank_account_swift_bic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_account_swift_bic = _parse_bank_account_swift_bic(d.pop("bank_account_swift_bic", UNSET))


        deletable = d.pop("deletable", UNSET)

        contact_attributes = cls(
            name=name,
            tax_id=tax_id,
            phone=phone,
            email=email,
            address=address,
            town=town,
            zip_code=zip_code,
            country_code=country_code,
            total_paid_incomes=total_paid_incomes,
            total_unpaid_incomes=total_unpaid_incomes,
            total_incomes=total_incomes,
            total_paid_expenses=total_paid_expenses,
            total_unpaid_expenses=total_unpaid_expenses,
            total_expenses=total_expenses,
            client_number=client_number,
            supplier_number=supplier_number,
            document_type=document_type,
            is_client=is_client,
            is_supplier=is_supplier,
            is_supplier_of_direct_goods=is_supplier_of_direct_goods,
            bank_account_number=bank_account_number,
            bank_account_swift_bic=bank_account_swift_bic,
            deletable=deletable,
        )


        contact_attributes.additional_properties = d
        return contact_attributes

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

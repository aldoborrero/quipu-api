from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ContactWritableAttributes")



@_attrs_define
class ContactWritableAttributes:
    """ 
        Attributes:
            name (str | Unset):
            tax_id (str | Unset):
            phone (str | Unset):
            email (str | Unset):
            address (str | Unset):
            town (str | Unset):
            zip_code (str | Unset):
            country_code (str | Unset):
            client_number (str | Unset):
            supplier_number (str | Unset):
            employee_number (str | Unset):
            a3_nom_id (str | Unset):
            is_supplier_of_direct_goods (bool | Unset):
            description (str | Unset):
            bank_account_number (str | Unset):
            bank_account_swift_bic (str | Unset):
            document_type (str | Unset):
     """

    name: str | Unset = UNSET
    tax_id: str | Unset = UNSET
    phone: str | Unset = UNSET
    email: str | Unset = UNSET
    address: str | Unset = UNSET
    town: str | Unset = UNSET
    zip_code: str | Unset = UNSET
    country_code: str | Unset = UNSET
    client_number: str | Unset = UNSET
    supplier_number: str | Unset = UNSET
    employee_number: str | Unset = UNSET
    a3_nom_id: str | Unset = UNSET
    is_supplier_of_direct_goods: bool | Unset = UNSET
    description: str | Unset = UNSET
    bank_account_number: str | Unset = UNSET
    bank_account_swift_bic: str | Unset = UNSET
    document_type: str | Unset = UNSET
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

        client_number = self.client_number

        supplier_number = self.supplier_number

        employee_number = self.employee_number

        a3_nom_id = self.a3_nom_id

        is_supplier_of_direct_goods = self.is_supplier_of_direct_goods

        description = self.description

        bank_account_number = self.bank_account_number

        bank_account_swift_bic = self.bank_account_swift_bic

        document_type = self.document_type


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
        if client_number is not UNSET:
            field_dict["client_number"] = client_number
        if supplier_number is not UNSET:
            field_dict["supplier_number"] = supplier_number
        if employee_number is not UNSET:
            field_dict["employee_number"] = employee_number
        if a3_nom_id is not UNSET:
            field_dict["a3_nom_id"] = a3_nom_id
        if is_supplier_of_direct_goods is not UNSET:
            field_dict["is_supplier_of_direct_goods"] = is_supplier_of_direct_goods
        if description is not UNSET:
            field_dict["description"] = description
        if bank_account_number is not UNSET:
            field_dict["bank_account_number"] = bank_account_number
        if bank_account_swift_bic is not UNSET:
            field_dict["bank_account_swift_bic"] = bank_account_swift_bic
        if document_type is not UNSET:
            field_dict["document_type"] = document_type

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

        client_number = d.pop("client_number", UNSET)

        supplier_number = d.pop("supplier_number", UNSET)

        employee_number = d.pop("employee_number", UNSET)

        a3_nom_id = d.pop("a3_nom_id", UNSET)

        is_supplier_of_direct_goods = d.pop("is_supplier_of_direct_goods", UNSET)

        description = d.pop("description", UNSET)

        bank_account_number = d.pop("bank_account_number", UNSET)

        bank_account_swift_bic = d.pop("bank_account_swift_bic", UNSET)

        document_type = d.pop("document_type", UNSET)

        contact_writable_attributes = cls(
            name=name,
            tax_id=tax_id,
            phone=phone,
            email=email,
            address=address,
            town=town,
            zip_code=zip_code,
            country_code=country_code,
            client_number=client_number,
            supplier_number=supplier_number,
            employee_number=employee_number,
            a3_nom_id=a3_nom_id,
            is_supplier_of_direct_goods=is_supplier_of_direct_goods,
            description=description,
            bank_account_number=bank_account_number,
            bank_account_swift_bic=bank_account_swift_bic,
            document_type=document_type,
        )


        contact_writable_attributes.additional_properties = d
        return contact_writable_attributes

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

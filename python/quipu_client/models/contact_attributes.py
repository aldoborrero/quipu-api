from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ContactAttributes")



@_attrs_define
class ContactAttributes:
    """ 
        Attributes:
            name (Union[Unset, str]):
            tax_id (Union[Unset, str]):
            phone (Union[Unset, str]):
            email (Union[Unset, str]):
            address (Union[Unset, str]):
            town (Union[Unset, str]):
            zip_code (Union[Unset, str]):
            country_code (Union[Unset, str]):  Example: ES.
            total_paid_incomes (Union[Unset, str]):
            total_unpaid_incomes (Union[Unset, str]):
            total_incomes (Union[Unset, str]):
            total_paid_expenses (Union[Unset, str]):
            total_unpaid_expenses (Union[Unset, str]):
            total_expenses (Union[Unset, str]):
            client_number (Union[None, Unset, str]):
            supplier_number (Union[None, Unset, str]):
            document_type (Union[None, Unset, str]):
            is_client (Union[Unset, bool]):
            is_supplier (Union[Unset, bool]):
            is_supplier_of_direct_goods (Union[Unset, bool]):
            bank_account_number (Union[None, Unset, str]):
            bank_account_swift_bic (Union[None, Unset, str]):
            deletable (Union[Unset, bool]):
     """

    name: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    town: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    total_paid_incomes: Union[Unset, str] = UNSET
    total_unpaid_incomes: Union[Unset, str] = UNSET
    total_incomes: Union[Unset, str] = UNSET
    total_paid_expenses: Union[Unset, str] = UNSET
    total_unpaid_expenses: Union[Unset, str] = UNSET
    total_expenses: Union[Unset, str] = UNSET
    client_number: Union[None, Unset, str] = UNSET
    supplier_number: Union[None, Unset, str] = UNSET
    document_type: Union[None, Unset, str] = UNSET
    is_client: Union[Unset, bool] = UNSET
    is_supplier: Union[Unset, bool] = UNSET
    is_supplier_of_direct_goods: Union[Unset, bool] = UNSET
    bank_account_number: Union[None, Unset, str] = UNSET
    bank_account_swift_bic: Union[None, Unset, str] = UNSET
    deletable: Union[Unset, bool] = UNSET
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

        client_number: Union[None, Unset, str]
        if isinstance(self.client_number, Unset):
            client_number = UNSET
        else:
            client_number = self.client_number

        supplier_number: Union[None, Unset, str]
        if isinstance(self.supplier_number, Unset):
            supplier_number = UNSET
        else:
            supplier_number = self.supplier_number

        document_type: Union[None, Unset, str]
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        is_client = self.is_client

        is_supplier = self.is_supplier

        is_supplier_of_direct_goods = self.is_supplier_of_direct_goods

        bank_account_number: Union[None, Unset, str]
        if isinstance(self.bank_account_number, Unset):
            bank_account_number = UNSET
        else:
            bank_account_number = self.bank_account_number

        bank_account_swift_bic: Union[None, Unset, str]
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

        def _parse_client_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_number = _parse_client_number(d.pop("client_number", UNSET))


        def _parse_supplier_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supplier_number = _parse_supplier_number(d.pop("supplier_number", UNSET))


        def _parse_document_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        document_type = _parse_document_type(d.pop("document_type", UNSET))


        is_client = d.pop("is_client", UNSET)

        is_supplier = d.pop("is_supplier", UNSET)

        is_supplier_of_direct_goods = d.pop("is_supplier_of_direct_goods", UNSET)

        def _parse_bank_account_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_account_number = _parse_bank_account_number(d.pop("bank_account_number", UNSET))


        def _parse_bank_account_swift_bic(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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

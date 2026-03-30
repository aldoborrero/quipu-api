from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_relationships_accounting_category import InvoiceRelationshipsAccountingCategory
    from ..models.invoice_relationships_accounting_subcategory import InvoiceRelationshipsAccountingSubcategory
    from ..models.invoice_relationships_amended_invoice import InvoiceRelationshipsAmendedInvoice
    from ..models.invoice_relationships_amending_invoices import InvoiceRelationshipsAmendingInvoices
    from ..models.invoice_relationships_analytic_categories import InvoiceRelationshipsAnalyticCategories
    from ..models.invoice_relationships_contact import InvoiceRelationshipsContact
    from ..models.invoice_relationships_items import InvoiceRelationshipsItems
    from ..models.invoice_relationships_numeration import InvoiceRelationshipsNumeration


T = TypeVar("T", bound="InvoiceRelationships")


@_attrs_define
class InvoiceRelationships:
    """
    Attributes:
        contact (InvoiceRelationshipsContact | Unset):
        accounting_category (InvoiceRelationshipsAccountingCategory | Unset):
        accounting_subcategory (InvoiceRelationshipsAccountingSubcategory | Unset):
        numeration (InvoiceRelationshipsNumeration | Unset):
        analytic_categories (InvoiceRelationshipsAnalyticCategories | Unset):
        items (InvoiceRelationshipsItems | Unset):
        amended_invoice (InvoiceRelationshipsAmendedInvoice | Unset):
        amending_invoices (InvoiceRelationshipsAmendingInvoices | Unset):
    """

    contact: InvoiceRelationshipsContact | Unset = UNSET
    accounting_category: InvoiceRelationshipsAccountingCategory | Unset = UNSET
    accounting_subcategory: InvoiceRelationshipsAccountingSubcategory | Unset = UNSET
    numeration: InvoiceRelationshipsNumeration | Unset = UNSET
    analytic_categories: InvoiceRelationshipsAnalyticCategories | Unset = UNSET
    items: InvoiceRelationshipsItems | Unset = UNSET
    amended_invoice: InvoiceRelationshipsAmendedInvoice | Unset = UNSET
    amending_invoices: InvoiceRelationshipsAmendingInvoices | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        accounting_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounting_category, Unset):
            accounting_category = self.accounting_category.to_dict()

        accounting_subcategory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounting_subcategory, Unset):
            accounting_subcategory = self.accounting_subcategory.to_dict()

        numeration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.numeration, Unset):
            numeration = self.numeration.to_dict()

        analytic_categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analytic_categories, Unset):
            analytic_categories = self.analytic_categories.to_dict()

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        amended_invoice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amended_invoice, Unset):
            amended_invoice = self.amended_invoice.to_dict()

        amending_invoices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amending_invoices, Unset):
            amending_invoices = self.amending_invoices.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if accounting_category is not UNSET:
            field_dict["accounting_category"] = accounting_category
        if accounting_subcategory is not UNSET:
            field_dict["accounting_subcategory"] = accounting_subcategory
        if numeration is not UNSET:
            field_dict["numeration"] = numeration
        if analytic_categories is not UNSET:
            field_dict["analytic_categories"] = analytic_categories
        if items is not UNSET:
            field_dict["items"] = items
        if amended_invoice is not UNSET:
            field_dict["amended_invoice"] = amended_invoice
        if amending_invoices is not UNSET:
            field_dict["amending_invoices"] = amending_invoices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_relationships_accounting_category import InvoiceRelationshipsAccountingCategory
        from ..models.invoice_relationships_accounting_subcategory import InvoiceRelationshipsAccountingSubcategory
        from ..models.invoice_relationships_amended_invoice import InvoiceRelationshipsAmendedInvoice
        from ..models.invoice_relationships_amending_invoices import InvoiceRelationshipsAmendingInvoices
        from ..models.invoice_relationships_analytic_categories import InvoiceRelationshipsAnalyticCategories
        from ..models.invoice_relationships_contact import InvoiceRelationshipsContact
        from ..models.invoice_relationships_items import InvoiceRelationshipsItems
        from ..models.invoice_relationships_numeration import InvoiceRelationshipsNumeration

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: InvoiceRelationshipsContact | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = InvoiceRelationshipsContact.from_dict(_contact)

        _accounting_category = d.pop("accounting_category", UNSET)
        accounting_category: InvoiceRelationshipsAccountingCategory | Unset
        if isinstance(_accounting_category, Unset):
            accounting_category = UNSET
        else:
            accounting_category = InvoiceRelationshipsAccountingCategory.from_dict(_accounting_category)

        _accounting_subcategory = d.pop("accounting_subcategory", UNSET)
        accounting_subcategory: InvoiceRelationshipsAccountingSubcategory | Unset
        if isinstance(_accounting_subcategory, Unset):
            accounting_subcategory = UNSET
        else:
            accounting_subcategory = InvoiceRelationshipsAccountingSubcategory.from_dict(_accounting_subcategory)

        _numeration = d.pop("numeration", UNSET)
        numeration: InvoiceRelationshipsNumeration | Unset
        if isinstance(_numeration, Unset):
            numeration = UNSET
        else:
            numeration = InvoiceRelationshipsNumeration.from_dict(_numeration)

        _analytic_categories = d.pop("analytic_categories", UNSET)
        analytic_categories: InvoiceRelationshipsAnalyticCategories | Unset
        if isinstance(_analytic_categories, Unset):
            analytic_categories = UNSET
        else:
            analytic_categories = InvoiceRelationshipsAnalyticCategories.from_dict(_analytic_categories)

        _items = d.pop("items", UNSET)
        items: InvoiceRelationshipsItems | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = InvoiceRelationshipsItems.from_dict(_items)

        _amended_invoice = d.pop("amended_invoice", UNSET)
        amended_invoice: InvoiceRelationshipsAmendedInvoice | Unset
        if isinstance(_amended_invoice, Unset):
            amended_invoice = UNSET
        else:
            amended_invoice = InvoiceRelationshipsAmendedInvoice.from_dict(_amended_invoice)

        _amending_invoices = d.pop("amending_invoices", UNSET)
        amending_invoices: InvoiceRelationshipsAmendingInvoices | Unset
        if isinstance(_amending_invoices, Unset):
            amending_invoices = UNSET
        else:
            amending_invoices = InvoiceRelationshipsAmendingInvoices.from_dict(_amending_invoices)

        invoice_relationships = cls(
            contact=contact,
            accounting_category=accounting_category,
            accounting_subcategory=accounting_subcategory,
            numeration=numeration,
            analytic_categories=analytic_categories,
            items=items,
            amended_invoice=amended_invoice,
            amending_invoices=amending_invoices,
        )

        invoice_relationships.additional_properties = d
        return invoice_relationships

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

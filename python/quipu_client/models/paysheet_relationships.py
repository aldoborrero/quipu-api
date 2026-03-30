from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paysheet_relationships_accounting_category import PaysheetRelationshipsAccountingCategory
    from ..models.paysheet_relationships_accounting_subcategory import PaysheetRelationshipsAccountingSubcategory
    from ..models.paysheet_relationships_analytic_categories import PaysheetRelationshipsAnalyticCategories
    from ..models.paysheet_relationships_contact import PaysheetRelationshipsContact
    from ..models.paysheet_relationships_numeration import PaysheetRelationshipsNumeration


T = TypeVar("T", bound="PaysheetRelationships")


@_attrs_define
class PaysheetRelationships:
    """
    Attributes:
        contact (PaysheetRelationshipsContact | Unset):
        accounting_category (PaysheetRelationshipsAccountingCategory | Unset):
        accounting_subcategory (PaysheetRelationshipsAccountingSubcategory | Unset):
        numeration (PaysheetRelationshipsNumeration | Unset):
        analytic_categories (PaysheetRelationshipsAnalyticCategories | Unset):
    """

    contact: PaysheetRelationshipsContact | Unset = UNSET
    accounting_category: PaysheetRelationshipsAccountingCategory | Unset = UNSET
    accounting_subcategory: PaysheetRelationshipsAccountingSubcategory | Unset = UNSET
    numeration: PaysheetRelationshipsNumeration | Unset = UNSET
    analytic_categories: PaysheetRelationshipsAnalyticCategories | Unset = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paysheet_relationships_accounting_category import PaysheetRelationshipsAccountingCategory
        from ..models.paysheet_relationships_accounting_subcategory import PaysheetRelationshipsAccountingSubcategory
        from ..models.paysheet_relationships_analytic_categories import PaysheetRelationshipsAnalyticCategories
        from ..models.paysheet_relationships_contact import PaysheetRelationshipsContact
        from ..models.paysheet_relationships_numeration import PaysheetRelationshipsNumeration

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: PaysheetRelationshipsContact | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = PaysheetRelationshipsContact.from_dict(_contact)

        _accounting_category = d.pop("accounting_category", UNSET)
        accounting_category: PaysheetRelationshipsAccountingCategory | Unset
        if isinstance(_accounting_category, Unset):
            accounting_category = UNSET
        else:
            accounting_category = PaysheetRelationshipsAccountingCategory.from_dict(_accounting_category)

        _accounting_subcategory = d.pop("accounting_subcategory", UNSET)
        accounting_subcategory: PaysheetRelationshipsAccountingSubcategory | Unset
        if isinstance(_accounting_subcategory, Unset):
            accounting_subcategory = UNSET
        else:
            accounting_subcategory = PaysheetRelationshipsAccountingSubcategory.from_dict(_accounting_subcategory)

        _numeration = d.pop("numeration", UNSET)
        numeration: PaysheetRelationshipsNumeration | Unset
        if isinstance(_numeration, Unset):
            numeration = UNSET
        else:
            numeration = PaysheetRelationshipsNumeration.from_dict(_numeration)

        _analytic_categories = d.pop("analytic_categories", UNSET)
        analytic_categories: PaysheetRelationshipsAnalyticCategories | Unset
        if isinstance(_analytic_categories, Unset):
            analytic_categories = UNSET
        else:
            analytic_categories = PaysheetRelationshipsAnalyticCategories.from_dict(_analytic_categories)

        paysheet_relationships = cls(
            contact=contact,
            accounting_category=accounting_category,
            accounting_subcategory=accounting_subcategory,
            numeration=numeration,
            analytic_categories=analytic_categories,
        )

        paysheet_relationships.additional_properties = d
        return paysheet_relationships

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

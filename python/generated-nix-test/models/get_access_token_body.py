from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_access_token_body_grant_type import GetAccessTokenBodyGrantType
from ..types import UNSET, Unset






T = TypeVar("T", bound="GetAccessTokenBody")



@_attrs_define
class GetAccessTokenBody:
    """ 
        Attributes:
            grant_type (GetAccessTokenBodyGrantType):
            scope (str | Unset):  Example: ecommerce.
     """

    grant_type: GetAccessTokenBodyGrantType
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        scope = self.scope


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "grant_type": grant_type,
        })
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = GetAccessTokenBodyGrantType(d.pop("grant_type"))




        scope = d.pop("scope", UNSET)

        get_access_token_body = cls(
            grant_type=grant_type,
            scope=scope,
        )


        get_access_token_body.additional_properties = d
        return get_access_token_body

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

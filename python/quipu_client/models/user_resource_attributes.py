from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.user_resource_attributes_sign_up_draft_data_type_0 import UserResourceAttributesSignUpDraftDataType0





T = TypeVar("T", bound="UserResourceAttributes")



@_attrs_define
class UserResourceAttributes:
    """ 
        Attributes:
            email (Union[Unset, str]):
            name (Union[Unset, str]):
            surnames (Union[Unset, str]):
            locale (Union[Unset, str]):  Example: es.
            sign_up_draft_data (Union['UserResourceAttributesSignUpDraftDataType0', None, Unset]):
            is_full_admin (Union[Unset, bool]):
     """

    email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    surnames: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    sign_up_draft_data: Union['UserResourceAttributesSignUpDraftDataType0', None, Unset] = UNSET
    is_full_admin: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.user_resource_attributes_sign_up_draft_data_type_0 import UserResourceAttributesSignUpDraftDataType0
        email = self.email

        name = self.name

        surnames = self.surnames

        locale = self.locale

        sign_up_draft_data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.sign_up_draft_data, Unset):
            sign_up_draft_data = UNSET
        elif isinstance(self.sign_up_draft_data, UserResourceAttributesSignUpDraftDataType0):
            sign_up_draft_data = self.sign_up_draft_data.to_dict()
        else:
            sign_up_draft_data = self.sign_up_draft_data

        is_full_admin = self.is_full_admin


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if surnames is not UNSET:
            field_dict["surnames"] = surnames
        if locale is not UNSET:
            field_dict["locale"] = locale
        if sign_up_draft_data is not UNSET:
            field_dict["sign_up_draft_data"] = sign_up_draft_data
        if is_full_admin is not UNSET:
            field_dict["is_full_admin"] = is_full_admin

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_resource_attributes_sign_up_draft_data_type_0 import UserResourceAttributesSignUpDraftDataType0
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        surnames = d.pop("surnames", UNSET)

        locale = d.pop("locale", UNSET)

        def _parse_sign_up_draft_data(data: object) -> Union['UserResourceAttributesSignUpDraftDataType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sign_up_draft_data_type_0 = UserResourceAttributesSignUpDraftDataType0.from_dict(data)



                return sign_up_draft_data_type_0
            except: # noqa: E722
                pass
            return cast(Union['UserResourceAttributesSignUpDraftDataType0', None, Unset], data)

        sign_up_draft_data = _parse_sign_up_draft_data(d.pop("sign_up_draft_data", UNSET))


        is_full_admin = d.pop("is_full_admin", UNSET)

        user_resource_attributes = cls(
            email=email,
            name=name,
            surnames=surnames,
            locale=locale,
            sign_up_draft_data=sign_up_draft_data,
            is_full_admin=is_full_admin,
        )


        user_resource_attributes.additional_properties = d
        return user_resource_attributes

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

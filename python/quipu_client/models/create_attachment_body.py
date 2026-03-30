from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json

from ..types import UNSET, Unset

from ..types import File, FileJsonType
from io import BytesIO






T = TypeVar("T", bound="CreateAttachmentBody")



@_attrs_define
class CreateAttachmentBody:
    """ 
        Attributes:
            file (File): The file to upload
            book_entry_id (str): ID of the book entry to attach the file to (required)
     """

    file: File
    book_entry_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        book_entry_id = self.book_entry_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
            "book_entry_id": book_entry_id,
        })

        return field_dict


    def to_multipart(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        book_entry_id =  (None, str(self.book_entry_id).encode(), "text/plain")



        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] =  (None, str(prop).encode(), "text/plain")

        field_dict.update({
            "file": file,
            "book_entry_id": book_entry_id,
        })

        return field_dict


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(
             payload = BytesIO(d.pop("file"))
        )




        book_entry_id = d.pop("book_entry_id")

        create_attachment_body = cls(
            file=file,
            book_entry_id=book_entry_id,
        )


        create_attachment_body.additional_properties = d
        return create_attachment_body

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

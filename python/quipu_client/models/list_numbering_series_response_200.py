from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.numbering_series_resource import NumberingSeriesResource
  from ..models.pagination_meta import PaginationMeta





T = TypeVar("T", bound="ListNumberingSeriesResponse200")



@_attrs_define
class ListNumberingSeriesResponse200:
    """ 
        Attributes:
            data (Union[Unset, list['NumberingSeriesResource']]):
            meta (Union[Unset, PaginationMeta]):
     """

    data: Union[Unset, list['NumberingSeriesResource']] = UNSET
    meta: Union[Unset, 'PaginationMeta'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.numbering_series_resource import NumberingSeriesResource
        from ..models.pagination_meta import PaginationMeta
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.numbering_series_resource import NumberingSeriesResource
        from ..models.pagination_meta import PaginationMeta
        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in (_data or []):
            data_item = NumberingSeriesResource.from_dict(data_item_data)



            data.append(data_item)


        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, PaginationMeta]
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = PaginationMeta.from_dict(_meta)




        list_numbering_series_response_200 = cls(
            data=data,
            meta=meta,
        )


        list_numbering_series_response_200.additional_properties = d
        return list_numbering_series_response_200

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

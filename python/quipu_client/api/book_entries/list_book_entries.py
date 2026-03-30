from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.list_book_entries_filterkind import ListBookEntriesFilterkind
from ...models.list_book_entries_filterpayment_status import ListBookEntriesFilterpaymentStatus
from ...models.list_book_entries_filtertype import ListBookEntriesFiltertype
from ...models.list_book_entries_response_200 import ListBookEntriesResponse200
from ...models.list_book_entries_sort import ListBookEntriesSort
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    owner_slug: str,
    *,
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filtertype: Union[Unset, ListBookEntriesFiltertype] = UNSET,
    filterkind: Union[Unset, ListBookEntriesFilterkind] = UNSET,
    filterq: Union[Unset, str] = UNSET,
    filterperiod: Union[Unset, str] = UNSET,
    filterpayment_status: Union[Unset, ListBookEntriesFilterpaymentStatus] = UNSET,
    filtercontact_id: Union[Unset, int] = UNSET,
    filtervalidation_status: Union[Unset, str] = UNSET,
    filterfield_queryfield: Union[Unset, str] = UNSET,
    filterfield_queryterm: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListBookEntriesSort] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    json_filtertype: Union[Unset, str] = UNSET
    if not isinstance(filtertype, Unset):
        json_filtertype = filtertype.value

    params["filter[type]"] = json_filtertype

    json_filterkind: Union[Unset, str] = UNSET
    if not isinstance(filterkind, Unset):
        json_filterkind = filterkind.value

    params["filter[kind]"] = json_filterkind

    params["filter[q]"] = filterq

    params["filter[period]"] = filterperiod

    json_filterpayment_status: Union[Unset, str] = UNSET
    if not isinstance(filterpayment_status, Unset):
        json_filterpayment_status = filterpayment_status.value

    params["filter[payment_status]"] = json_filterpayment_status

    params["filter[contact_id]"] = filtercontact_id

    params["filter[validation_status]"] = filtervalidation_status

    params["filter[field_query][field]"] = filterfield_queryfield

    params["filter[field_query][term]"] = filterfield_queryterm

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{owner_slug}/book_entries".format(owner_slug=owner_slug,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorResponse, ListBookEntriesResponse200]]:
    if response.status_code == 200:
        response_200 = ListBookEntriesResponse200.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorResponse, ListBookEntriesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    owner_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filtertype: Union[Unset, ListBookEntriesFiltertype] = UNSET,
    filterkind: Union[Unset, ListBookEntriesFilterkind] = UNSET,
    filterq: Union[Unset, str] = UNSET,
    filterperiod: Union[Unset, str] = UNSET,
    filterpayment_status: Union[Unset, ListBookEntriesFilterpaymentStatus] = UNSET,
    filtercontact_id: Union[Unset, int] = UNSET,
    filtervalidation_status: Union[Unset, str] = UNSET,
    filterfield_queryfield: Union[Unset, str] = UNSET,
    filterfield_queryterm: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListBookEntriesSort] = UNSET,

) -> Response[Union[ErrorResponse, ListBookEntriesResponse200]]:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filtertype (Union[Unset, ListBookEntriesFiltertype]):
        filterkind (Union[Unset, ListBookEntriesFilterkind]):
        filterq (Union[Unset, str]):
        filterperiod (Union[Unset, str]):
        filterpayment_status (Union[Unset, ListBookEntriesFilterpaymentStatus]):
        filtercontact_id (Union[Unset, int]):
        filtervalidation_status (Union[Unset, str]):
        filterfield_queryfield (Union[Unset, str]):
        filterfield_queryterm (Union[Unset, str]):
        sort (Union[Unset, ListBookEntriesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListBookEntriesResponse200]]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,
filtertype=filtertype,
filterkind=filterkind,
filterq=filterq,
filterperiod=filterperiod,
filterpayment_status=filterpayment_status,
filtercontact_id=filtercontact_id,
filtervalidation_status=filtervalidation_status,
filterfield_queryfield=filterfield_queryfield,
filterfield_queryterm=filterfield_queryterm,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    owner_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filtertype: Union[Unset, ListBookEntriesFiltertype] = UNSET,
    filterkind: Union[Unset, ListBookEntriesFilterkind] = UNSET,
    filterq: Union[Unset, str] = UNSET,
    filterperiod: Union[Unset, str] = UNSET,
    filterpayment_status: Union[Unset, ListBookEntriesFilterpaymentStatus] = UNSET,
    filtercontact_id: Union[Unset, int] = UNSET,
    filtervalidation_status: Union[Unset, str] = UNSET,
    filterfield_queryfield: Union[Unset, str] = UNSET,
    filterfield_queryterm: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListBookEntriesSort] = UNSET,

) -> Optional[Union[ErrorResponse, ListBookEntriesResponse200]]:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filtertype (Union[Unset, ListBookEntriesFiltertype]):
        filterkind (Union[Unset, ListBookEntriesFilterkind]):
        filterq (Union[Unset, str]):
        filterperiod (Union[Unset, str]):
        filterpayment_status (Union[Unset, ListBookEntriesFilterpaymentStatus]):
        filtercontact_id (Union[Unset, int]):
        filtervalidation_status (Union[Unset, str]):
        filterfield_queryfield (Union[Unset, str]):
        filterfield_queryterm (Union[Unset, str]):
        sort (Union[Unset, ListBookEntriesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListBookEntriesResponse200]
     """


    return sync_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filtertype=filtertype,
filterkind=filterkind,
filterq=filterq,
filterperiod=filterperiod,
filterpayment_status=filterpayment_status,
filtercontact_id=filtercontact_id,
filtervalidation_status=filtervalidation_status,
filterfield_queryfield=filterfield_queryfield,
filterfield_queryterm=filterfield_queryterm,
sort=sort,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filtertype: Union[Unset, ListBookEntriesFiltertype] = UNSET,
    filterkind: Union[Unset, ListBookEntriesFilterkind] = UNSET,
    filterq: Union[Unset, str] = UNSET,
    filterperiod: Union[Unset, str] = UNSET,
    filterpayment_status: Union[Unset, ListBookEntriesFilterpaymentStatus] = UNSET,
    filtercontact_id: Union[Unset, int] = UNSET,
    filtervalidation_status: Union[Unset, str] = UNSET,
    filterfield_queryfield: Union[Unset, str] = UNSET,
    filterfield_queryterm: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListBookEntriesSort] = UNSET,

) -> Response[Union[ErrorResponse, ListBookEntriesResponse200]]:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filtertype (Union[Unset, ListBookEntriesFiltertype]):
        filterkind (Union[Unset, ListBookEntriesFilterkind]):
        filterq (Union[Unset, str]):
        filterperiod (Union[Unset, str]):
        filterpayment_status (Union[Unset, ListBookEntriesFilterpaymentStatus]):
        filtercontact_id (Union[Unset, int]):
        filtervalidation_status (Union[Unset, str]):
        filterfield_queryfield (Union[Unset, str]):
        filterfield_queryterm (Union[Unset, str]):
        sort (Union[Unset, ListBookEntriesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListBookEntriesResponse200]]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,
filtertype=filtertype,
filterkind=filterkind,
filterq=filterq,
filterperiod=filterperiod,
filterpayment_status=filterpayment_status,
filtercontact_id=filtercontact_id,
filtervalidation_status=filtervalidation_status,
filterfield_queryfield=filterfield_queryfield,
filterfield_queryterm=filterfield_queryterm,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    owner_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filtertype: Union[Unset, ListBookEntriesFiltertype] = UNSET,
    filterkind: Union[Unset, ListBookEntriesFilterkind] = UNSET,
    filterq: Union[Unset, str] = UNSET,
    filterperiod: Union[Unset, str] = UNSET,
    filterpayment_status: Union[Unset, ListBookEntriesFilterpaymentStatus] = UNSET,
    filtercontact_id: Union[Unset, int] = UNSET,
    filtervalidation_status: Union[Unset, str] = UNSET,
    filterfield_queryfield: Union[Unset, str] = UNSET,
    filterfield_queryterm: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListBookEntriesSort] = UNSET,

) -> Optional[Union[ErrorResponse, ListBookEntriesResponse200]]:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filtertype (Union[Unset, ListBookEntriesFiltertype]):
        filterkind (Union[Unset, ListBookEntriesFilterkind]):
        filterq (Union[Unset, str]):
        filterperiod (Union[Unset, str]):
        filterpayment_status (Union[Unset, ListBookEntriesFilterpaymentStatus]):
        filtercontact_id (Union[Unset, int]):
        filtervalidation_status (Union[Unset, str]):
        filterfield_queryfield (Union[Unset, str]):
        filterfield_queryterm (Union[Unset, str]):
        sort (Union[Unset, ListBookEntriesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListBookEntriesResponse200]
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filtertype=filtertype,
filterkind=filterkind,
filterq=filterq,
filterperiod=filterperiod,
filterpayment_status=filterpayment_status,
filtercontact_id=filtercontact_id,
filtervalidation_status=filtervalidation_status,
filterfield_queryfield=filterfield_queryfield,
filterfield_queryterm=filterfield_queryterm,
sort=sort,

    )).parsed

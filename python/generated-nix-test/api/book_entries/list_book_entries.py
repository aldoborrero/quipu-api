from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

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



def _get_kwargs(
    owner_slug: str,
    *,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filtertype: ListBookEntriesFiltertype | Unset = UNSET,
    filterkind: ListBookEntriesFilterkind | Unset = UNSET,
    filterq: str | Unset = UNSET,
    filterperiod: str | Unset = UNSET,
    filterpayment_status: ListBookEntriesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: int | Unset = UNSET,
    filtervalidation_status: str | Unset = UNSET,
    filterfield_queryfield: str | Unset = UNSET,
    filterfield_queryterm: str | Unset = UNSET,
    sort: ListBookEntriesSort | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    json_filtertype: str | Unset = UNSET
    if not isinstance(filtertype, Unset):
        json_filtertype = filtertype.value

    params["filter[type]"] = json_filtertype

    json_filterkind: str | Unset = UNSET
    if not isinstance(filterkind, Unset):
        json_filterkind = filterkind.value

    params["filter[kind]"] = json_filterkind

    params["filter[q]"] = filterq

    params["filter[period]"] = filterperiod

    json_filterpayment_status: str | Unset = UNSET
    if not isinstance(filterpayment_status, Unset):
        json_filterpayment_status = filterpayment_status.value

    params["filter[payment_status]"] = json_filterpayment_status

    params["filter[contact_id]"] = filtercontact_id

    params["filter[validation_status]"] = filtervalidation_status

    params["filter[field_query][field]"] = filterfield_queryfield

    params["filter[field_query][term]"] = filterfield_queryterm

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{owner_slug}/book_entries".format(owner_slug=quote(str(owner_slug), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | ListBookEntriesResponse200 | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | ListBookEntriesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    owner_slug: str,
    *,
    client: AuthenticatedClient | Client,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filtertype: ListBookEntriesFiltertype | Unset = UNSET,
    filterkind: ListBookEntriesFilterkind | Unset = UNSET,
    filterq: str | Unset = UNSET,
    filterperiod: str | Unset = UNSET,
    filterpayment_status: ListBookEntriesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: int | Unset = UNSET,
    filtervalidation_status: str | Unset = UNSET,
    filterfield_queryfield: str | Unset = UNSET,
    filterfield_queryterm: str | Unset = UNSET,
    sort: ListBookEntriesSort | Unset = UNSET,

) -> Response[ErrorResponse | ListBookEntriesResponse200]:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filtertype (ListBookEntriesFiltertype | Unset):
        filterkind (ListBookEntriesFilterkind | Unset):
        filterq (str | Unset):
        filterperiod (str | Unset):
        filterpayment_status (ListBookEntriesFilterpaymentStatus | Unset):
        filtercontact_id (int | Unset):
        filtervalidation_status (str | Unset):
        filterfield_queryfield (str | Unset):
        filterfield_queryterm (str | Unset):
        sort (ListBookEntriesSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListBookEntriesResponse200]
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
    client: AuthenticatedClient | Client,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filtertype: ListBookEntriesFiltertype | Unset = UNSET,
    filterkind: ListBookEntriesFilterkind | Unset = UNSET,
    filterq: str | Unset = UNSET,
    filterperiod: str | Unset = UNSET,
    filterpayment_status: ListBookEntriesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: int | Unset = UNSET,
    filtervalidation_status: str | Unset = UNSET,
    filterfield_queryfield: str | Unset = UNSET,
    filterfield_queryterm: str | Unset = UNSET,
    sort: ListBookEntriesSort | Unset = UNSET,

) -> ErrorResponse | ListBookEntriesResponse200 | None:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filtertype (ListBookEntriesFiltertype | Unset):
        filterkind (ListBookEntriesFilterkind | Unset):
        filterq (str | Unset):
        filterperiod (str | Unset):
        filterpayment_status (ListBookEntriesFilterpaymentStatus | Unset):
        filtercontact_id (int | Unset):
        filtervalidation_status (str | Unset):
        filterfield_queryfield (str | Unset):
        filterfield_queryterm (str | Unset):
        sort (ListBookEntriesSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListBookEntriesResponse200
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
    client: AuthenticatedClient | Client,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filtertype: ListBookEntriesFiltertype | Unset = UNSET,
    filterkind: ListBookEntriesFilterkind | Unset = UNSET,
    filterq: str | Unset = UNSET,
    filterperiod: str | Unset = UNSET,
    filterpayment_status: ListBookEntriesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: int | Unset = UNSET,
    filtervalidation_status: str | Unset = UNSET,
    filterfield_queryfield: str | Unset = UNSET,
    filterfield_queryterm: str | Unset = UNSET,
    sort: ListBookEntriesSort | Unset = UNSET,

) -> Response[ErrorResponse | ListBookEntriesResponse200]:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filtertype (ListBookEntriesFiltertype | Unset):
        filterkind (ListBookEntriesFilterkind | Unset):
        filterq (str | Unset):
        filterperiod (str | Unset):
        filterpayment_status (ListBookEntriesFilterpaymentStatus | Unset):
        filtercontact_id (int | Unset):
        filtervalidation_status (str | Unset):
        filterfield_queryfield (str | Unset):
        filterfield_queryterm (str | Unset):
        sort (ListBookEntriesSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListBookEntriesResponse200]
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
    client: AuthenticatedClient | Client,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filtertype: ListBookEntriesFiltertype | Unset = UNSET,
    filterkind: ListBookEntriesFilterkind | Unset = UNSET,
    filterq: str | Unset = UNSET,
    filterperiod: str | Unset = UNSET,
    filterpayment_status: ListBookEntriesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: int | Unset = UNSET,
    filtervalidation_status: str | Unset = UNSET,
    filterfield_queryfield: str | Unset = UNSET,
    filterfield_queryterm: str | Unset = UNSET,
    sort: ListBookEntriesSort | Unset = UNSET,

) -> ErrorResponse | ListBookEntriesResponse200 | None:
    """ List all book entries

     Returns a paginated list of all book entries including invoices,
    tickets, simplified invoices, additional income, and paysheets.

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filtertype (ListBookEntriesFiltertype | Unset):
        filterkind (ListBookEntriesFilterkind | Unset):
        filterq (str | Unset):
        filterperiod (str | Unset):
        filterpayment_status (ListBookEntriesFilterpaymentStatus | Unset):
        filtercontact_id (int | Unset):
        filtervalidation_status (str | Unset):
        filterfield_queryfield (str | Unset):
        filterfield_queryterm (str | Unset):
        sort (ListBookEntriesSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListBookEntriesResponse200
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

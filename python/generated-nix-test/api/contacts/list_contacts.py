from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.list_contacts_filterkind import ListContactsFilterkind
from ...models.list_contacts_response_200 import ListContactsResponse200
from ...models.list_contacts_sort import ListContactsSort
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    owner_slug: str,
    *,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filterkind: ListContactsFilterkind | Unset = UNSET,
    filtertax_id: str | Unset = UNSET,
    filtercountry: str | Unset = UNSET,
    filteremail: str | Unset = UNSET,
    filterq: str | Unset = UNSET,
    sort: ListContactsSort | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    json_filterkind: str | Unset = UNSET
    if not isinstance(filterkind, Unset):
        json_filterkind = filterkind.value

    params["filter[kind]"] = json_filterkind

    params["filter[tax_id]"] = filtertax_id

    params["filter[country]"] = filtercountry

    params["filter[email]"] = filteremail

    params["filter[q]"] = filterq

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{owner_slug}/contacts".format(owner_slug=quote(str(owner_slug), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | ListContactsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListContactsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | ListContactsResponse200]:
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
    filterkind: ListContactsFilterkind | Unset = UNSET,
    filtertax_id: str | Unset = UNSET,
    filtercountry: str | Unset = UNSET,
    filteremail: str | Unset = UNSET,
    filterq: str | Unset = UNSET,
    sort: ListContactsSort | Unset = UNSET,

) -> Response[ErrorResponse | ListContactsResponse200]:
    """ List contacts

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (ListContactsFilterkind | Unset):
        filtertax_id (str | Unset):
        filtercountry (str | Unset):
        filteremail (str | Unset):
        filterq (str | Unset):
        sort (ListContactsSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListContactsResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filtertax_id=filtertax_id,
filtercountry=filtercountry,
filteremail=filteremail,
filterq=filterq,
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
    filterkind: ListContactsFilterkind | Unset = UNSET,
    filtertax_id: str | Unset = UNSET,
    filtercountry: str | Unset = UNSET,
    filteremail: str | Unset = UNSET,
    filterq: str | Unset = UNSET,
    sort: ListContactsSort | Unset = UNSET,

) -> ErrorResponse | ListContactsResponse200 | None:
    """ List contacts

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (ListContactsFilterkind | Unset):
        filtertax_id (str | Unset):
        filtercountry (str | Unset):
        filteremail (str | Unset):
        filterq (str | Unset):
        sort (ListContactsSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListContactsResponse200
     """


    return sync_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filtertax_id=filtertax_id,
filtercountry=filtercountry,
filteremail=filteremail,
filterq=filterq,
sort=sort,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    *,
    client: AuthenticatedClient | Client,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filterkind: ListContactsFilterkind | Unset = UNSET,
    filtertax_id: str | Unset = UNSET,
    filtercountry: str | Unset = UNSET,
    filteremail: str | Unset = UNSET,
    filterq: str | Unset = UNSET,
    sort: ListContactsSort | Unset = UNSET,

) -> Response[ErrorResponse | ListContactsResponse200]:
    """ List contacts

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (ListContactsFilterkind | Unset):
        filtertax_id (str | Unset):
        filtercountry (str | Unset):
        filteremail (str | Unset):
        filterq (str | Unset):
        sort (ListContactsSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListContactsResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filtertax_id=filtertax_id,
filtercountry=filtercountry,
filteremail=filteremail,
filterq=filterq,
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
    filterkind: ListContactsFilterkind | Unset = UNSET,
    filtertax_id: str | Unset = UNSET,
    filtercountry: str | Unset = UNSET,
    filteremail: str | Unset = UNSET,
    filterq: str | Unset = UNSET,
    sort: ListContactsSort | Unset = UNSET,

) -> ErrorResponse | ListContactsResponse200 | None:
    """ List contacts

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (ListContactsFilterkind | Unset):
        filtertax_id (str | Unset):
        filtercountry (str | Unset):
        filteremail (str | Unset):
        filterq (str | Unset):
        sort (ListContactsSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListContactsResponse200
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filtertax_id=filtertax_id,
filtercountry=filtercountry,
filteremail=filteremail,
filterq=filterq,
sort=sort,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.list_accounting_categories_response_200 import ListAccountingCategoriesResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    owner_slug: str,
    *,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filterkind: str | Unset = UNSET,
    filterprefix: str | Unset = UNSET,
    filteractive: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[kind]"] = filterkind

    params["filter[prefix]"] = filterprefix

    params["filter[active]"] = filteractive


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{owner_slug}/accounting_categories".format(owner_slug=quote(str(owner_slug), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | ListAccountingCategoriesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAccountingCategoriesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | ListAccountingCategoriesResponse200]:
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
    filterkind: str | Unset = UNSET,
    filterprefix: str | Unset = UNSET,
    filteractive: bool | Unset = UNSET,

) -> Response[ErrorResponse | ListAccountingCategoriesResponse200]:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (str | Unset):
        filterprefix (str | Unset):
        filteractive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAccountingCategoriesResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filterprefix=filterprefix,
filteractive=filteractive,

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
    filterkind: str | Unset = UNSET,
    filterprefix: str | Unset = UNSET,
    filteractive: bool | Unset = UNSET,

) -> ErrorResponse | ListAccountingCategoriesResponse200 | None:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (str | Unset):
        filterprefix (str | Unset):
        filteractive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAccountingCategoriesResponse200
     """


    return sync_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filterprefix=filterprefix,
filteractive=filteractive,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    *,
    client: AuthenticatedClient | Client,
    pagenumber: int | Unset = 1,
    pagesize: int | Unset = 25,
    filterkind: str | Unset = UNSET,
    filterprefix: str | Unset = UNSET,
    filteractive: bool | Unset = UNSET,

) -> Response[ErrorResponse | ListAccountingCategoriesResponse200]:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (str | Unset):
        filterprefix (str | Unset):
        filteractive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAccountingCategoriesResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filterprefix=filterprefix,
filteractive=filteractive,

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
    filterkind: str | Unset = UNSET,
    filterprefix: str | Unset = UNSET,
    filteractive: bool | Unset = UNSET,

) -> ErrorResponse | ListAccountingCategoriesResponse200 | None:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 25.
        filterkind (str | Unset):
        filterprefix (str | Unset):
        filteractive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAccountingCategoriesResponse200
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filterkind=filterkind,
filterprefix=filterprefix,
filteractive=filteractive,

    )).parsed

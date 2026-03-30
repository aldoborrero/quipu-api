from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.list_accounting_categories_response_200 import ListAccountingCategoriesResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    owner_slug: str,
    *,
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filterkind: Union[Unset, str] = UNSET,
    filterprefix: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,

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
        "url": "/{owner_slug}/accounting_categories".format(owner_slug=owner_slug,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorResponse, ListAccountingCategoriesResponse200]]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorResponse, ListAccountingCategoriesResponse200]]:
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
    filterkind: Union[Unset, str] = UNSET,
    filterprefix: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,

) -> Response[Union[ErrorResponse, ListAccountingCategoriesResponse200]]:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filterkind (Union[Unset, str]):
        filterprefix (Union[Unset, str]):
        filteractive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListAccountingCategoriesResponse200]]
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
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filterkind: Union[Unset, str] = UNSET,
    filterprefix: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,

) -> Optional[Union[ErrorResponse, ListAccountingCategoriesResponse200]]:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filterkind (Union[Unset, str]):
        filterprefix (Union[Unset, str]):
        filteractive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListAccountingCategoriesResponse200]
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
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filterkind: Union[Unset, str] = UNSET,
    filterprefix: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,

) -> Response[Union[ErrorResponse, ListAccountingCategoriesResponse200]]:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filterkind (Union[Unset, str]):
        filterprefix (Union[Unset, str]):
        filteractive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListAccountingCategoriesResponse200]]
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
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,
    filterkind: Union[Unset, str] = UNSET,
    filterprefix: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,

) -> Optional[Union[ErrorResponse, ListAccountingCategoriesResponse200]]:
    """ List accounting categories

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.
        filterkind (Union[Unset, str]):
        filterprefix (Union[Unset, str]):
        filteractive (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListAccountingCategoriesResponse200]
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

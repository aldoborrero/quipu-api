from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.list_tickets_response_200 import ListTicketsResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    owner_slug: str,
    *,
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{owner_slug}/tickets".format(owner_slug=owner_slug,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorResponse, ListTicketsResponse200]]:
    if response.status_code == 200:
        response_200 = ListTicketsResponse200.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorResponse, ListTicketsResponse200]]:
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

) -> Response[Union[ErrorResponse, ListTicketsResponse200]]:
    """ List tickets

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListTicketsResponse200]]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,

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

) -> Optional[Union[ErrorResponse, ListTicketsResponse200]]:
    """ List tickets

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListTicketsResponse200]
     """


    return sync_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagenumber: Union[Unset, int] = 1,
    pagesize: Union[Unset, int] = 25,

) -> Response[Union[ErrorResponse, ListTicketsResponse200]]:
    """ List tickets

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListTicketsResponse200]]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
pagenumber=pagenumber,
pagesize=pagesize,

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

) -> Optional[Union[ErrorResponse, ListTicketsResponse200]]:
    """ List tickets

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        pagenumber (Union[Unset, int]):  Default: 1.
        pagesize (Union[Unset, int]):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListTicketsResponse200]
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,

    )).parsed

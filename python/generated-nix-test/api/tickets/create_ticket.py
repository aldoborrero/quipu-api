from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_ticket_body import CreateTicketBody
from ...models.create_ticket_response_201 import CreateTicketResponse201
from ...models.error_response import ErrorResponse
from typing import cast



def _get_kwargs(
    owner_slug: str,
    *,
    body: CreateTicketBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{owner_slug}/tickets".format(owner_slug=quote(str(owner_slug), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/vnd.quipu.v1+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateTicketResponse201 | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = CreateTicketResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateTicketResponse201 | ErrorResponse]:
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
    body: CreateTicketBody,

) -> Response[CreateTicketResponse201 | ErrorResponse]:
    """ Create ticket

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        body (CreateTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTicketResponse201 | ErrorResponse]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    owner_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateTicketBody,

) -> CreateTicketResponse201 | ErrorResponse | None:
    """ Create ticket

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        body (CreateTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTicketResponse201 | ErrorResponse
     """


    return sync_detailed(
        owner_slug=owner_slug,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateTicketBody,

) -> Response[CreateTicketResponse201 | ErrorResponse]:
    """ Create ticket

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        body (CreateTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTicketResponse201 | ErrorResponse]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    owner_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateTicketBody,

) -> CreateTicketResponse201 | ErrorResponse | None:
    """ Create ticket

     **Deprecated.** Use Simplified Invoices or Additional Income instead. Returns 403 Forbidden for
    Verifactu-activated accounts.

    Args:
        owner_slug (str):
        body (CreateTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTicketResponse201 | ErrorResponse
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
client=client,
body=body,

    )).parsed

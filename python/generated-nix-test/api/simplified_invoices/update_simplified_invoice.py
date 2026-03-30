from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.update_simplified_invoice_body import UpdateSimplifiedInvoiceBody
from ...models.update_simplified_invoice_response_200 import UpdateSimplifiedInvoiceResponse200
from typing import cast



def _get_kwargs(
    owner_slug: str,
    id: int,
    *,
    body: UpdateSimplifiedInvoiceBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/{owner_slug}/simplified_invoices/{id}".format(owner_slug=quote(str(owner_slug), safe=""),id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/vnd.quipu.v1+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | UpdateSimplifiedInvoiceResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateSimplifiedInvoiceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | UpdateSimplifiedInvoiceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    owner_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSimplifiedInvoiceBody,

) -> Response[ErrorResponse | UpdateSimplifiedInvoiceResponse200]:
    """ Update simplified invoice

    Args:
        owner_slug (str):
        id (int):
        body (UpdateSimplifiedInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateSimplifiedInvoiceResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    owner_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSimplifiedInvoiceBody,

) -> ErrorResponse | UpdateSimplifiedInvoiceResponse200 | None:
    """ Update simplified invoice

    Args:
        owner_slug (str):
        id (int):
        body (UpdateSimplifiedInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateSimplifiedInvoiceResponse200
     """


    return sync_detailed(
        owner_slug=owner_slug,
id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSimplifiedInvoiceBody,

) -> Response[ErrorResponse | UpdateSimplifiedInvoiceResponse200]:
    """ Update simplified invoice

    Args:
        owner_slug (str):
        id (int):
        body (UpdateSimplifiedInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateSimplifiedInvoiceResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    owner_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSimplifiedInvoiceBody,

) -> ErrorResponse | UpdateSimplifiedInvoiceResponse200 | None:
    """ Update simplified invoice

    Args:
        owner_slug (str):
        id (int):
        body (UpdateSimplifiedInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateSimplifiedInvoiceResponse200
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
id=id,
client=client,
body=body,

    )).parsed

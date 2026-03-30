from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.get_attachment_response_200 import GetAttachmentResponse200
from typing import cast



def _get_kwargs(
    owner_slug: str,
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{owner_slug}/attachments/{id}".format(owner_slug=quote(str(owner_slug), safe=""),id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | GetAttachmentResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAttachmentResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | GetAttachmentResponse200]:
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

) -> Response[ErrorResponse | GetAttachmentResponse200]:
    """ Show attachment

    Args:
        owner_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetAttachmentResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
id=id,

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

) -> ErrorResponse | GetAttachmentResponse200 | None:
    """ Show attachment

    Args:
        owner_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetAttachmentResponse200
     """


    return sync_detailed(
        owner_slug=owner_slug,
id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorResponse | GetAttachmentResponse200]:
    """ Show attachment

    Args:
        owner_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetAttachmentResponse200]
     """


    kwargs = _get_kwargs(
        owner_slug=owner_slug,
id=id,

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

) -> ErrorResponse | GetAttachmentResponse200 | None:
    """ Show attachment

    Args:
        owner_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetAttachmentResponse200
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
id=id,
client=client,

    )).parsed

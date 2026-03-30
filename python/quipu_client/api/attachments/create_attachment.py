from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_attachment_body import CreateAttachmentBody
from ...models.create_attachment_response_201 import CreateAttachmentResponse201
from ...models.error_response import ErrorResponse
from typing import cast



def _get_kwargs(
    owner_slug: str,
    *,
    body: CreateAttachmentBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{owner_slug}/attachments".format(owner_slug=owner_slug,),
    }

    _body = body.to_multipart()


    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CreateAttachmentResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateAttachmentResponse201.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CreateAttachmentResponse201, ErrorResponse]]:
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
    body: CreateAttachmentBody,

) -> Response[Union[CreateAttachmentResponse201, ErrorResponse]]:
    """ Create attachment (file upload)

     Upload a file as a multipart form data request.

    Args:
        owner_slug (str):
        body (CreateAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateAttachmentResponse201, ErrorResponse]]
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
    client: Union[AuthenticatedClient, Client],
    body: CreateAttachmentBody,

) -> Optional[Union[CreateAttachmentResponse201, ErrorResponse]]:
    """ Create attachment (file upload)

     Upload a file as a multipart form data request.

    Args:
        owner_slug (str):
        body (CreateAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateAttachmentResponse201, ErrorResponse]
     """


    return sync_detailed(
        owner_slug=owner_slug,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    owner_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAttachmentBody,

) -> Response[Union[CreateAttachmentResponse201, ErrorResponse]]:
    """ Create attachment (file upload)

     Upload a file as a multipart form data request.

    Args:
        owner_slug (str):
        body (CreateAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateAttachmentResponse201, ErrorResponse]]
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
    client: Union[AuthenticatedClient, Client],
    body: CreateAttachmentBody,

) -> Optional[Union[CreateAttachmentResponse201, ErrorResponse]]:
    """ Create attachment (file upload)

     Upload a file as a multipart form data request.

    Args:
        owner_slug (str):
        body (CreateAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateAttachmentResponse201, ErrorResponse]
     """


    return (await asyncio_detailed(
        owner_slug=owner_slug,
client=client,
body=body,

    )).parsed

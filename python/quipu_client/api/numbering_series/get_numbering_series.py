from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_numbering_series_filterapplicable_to import GetNumberingSeriesFilterapplicableTo
from ...models.numbering_series_collection import NumberingSeriesCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterprefix: None | str | Unset = UNSET,
    filterapplicable_to: GetNumberingSeriesFilterapplicableTo | Unset = UNSET,
    filteramending: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filterprefix: None | str | Unset
    if isinstance(filterprefix, Unset):
        json_filterprefix = UNSET
    else:
        json_filterprefix = filterprefix
    params["filter[prefix]"] = json_filterprefix

    json_filterapplicable_to: str | Unset = UNSET
    if not isinstance(filterapplicable_to, Unset):
        json_filterapplicable_to = filterapplicable_to.value

    params["filter[applicable_to]"] = json_filterapplicable_to

    json_filteramending: bool | None | Unset
    if isinstance(filteramending, Unset):
        json_filteramending = UNSET
    else:
        json_filteramending = filteramending
    params["filter[amending]"] = json_filteramending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/numbering_series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NumberingSeriesCollection | None:
    if response.status_code == 200:
        response_200 = NumberingSeriesCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NumberingSeriesCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterprefix: None | str | Unset = UNSET,
    filterapplicable_to: GetNumberingSeriesFilterapplicableTo | Unset = UNSET,
    filteramending: bool | None | Unset = UNSET,
) -> Response[NumberingSeriesCollection]:
    """Retrieve all numbering series

    Args:
        filterprefix (None | str | Unset):
        filterapplicable_to (GetNumberingSeriesFilterapplicableTo | Unset):
        filteramending (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NumberingSeriesCollection]
    """

    kwargs = _get_kwargs(
        filterprefix=filterprefix,
        filterapplicable_to=filterapplicable_to,
        filteramending=filteramending,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filterprefix: None | str | Unset = UNSET,
    filterapplicable_to: GetNumberingSeriesFilterapplicableTo | Unset = UNSET,
    filteramending: bool | None | Unset = UNSET,
) -> NumberingSeriesCollection | None:
    """Retrieve all numbering series

    Args:
        filterprefix (None | str | Unset):
        filterapplicable_to (GetNumberingSeriesFilterapplicableTo | Unset):
        filteramending (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NumberingSeriesCollection
    """

    return sync_detailed(
        client=client,
        filterprefix=filterprefix,
        filterapplicable_to=filterapplicable_to,
        filteramending=filteramending,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterprefix: None | str | Unset = UNSET,
    filterapplicable_to: GetNumberingSeriesFilterapplicableTo | Unset = UNSET,
    filteramending: bool | None | Unset = UNSET,
) -> Response[NumberingSeriesCollection]:
    """Retrieve all numbering series

    Args:
        filterprefix (None | str | Unset):
        filterapplicable_to (GetNumberingSeriesFilterapplicableTo | Unset):
        filteramending (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NumberingSeriesCollection]
    """

    kwargs = _get_kwargs(
        filterprefix=filterprefix,
        filterapplicable_to=filterapplicable_to,
        filteramending=filteramending,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filterprefix: None | str | Unset = UNSET,
    filterapplicable_to: GetNumberingSeriesFilterapplicableTo | Unset = UNSET,
    filteramending: bool | None | Unset = UNSET,
) -> NumberingSeriesCollection | None:
    """Retrieve all numbering series

    Args:
        filterprefix (None | str | Unset):
        filterapplicable_to (GetNumberingSeriesFilterapplicableTo | Unset):
        filteramending (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NumberingSeriesCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            filterprefix=filterprefix,
            filterapplicable_to=filterapplicable_to,
            filteramending=filteramending,
        )
    ).parsed

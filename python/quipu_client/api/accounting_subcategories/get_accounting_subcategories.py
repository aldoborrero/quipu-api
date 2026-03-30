from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accounting_subcategory_collection import AccountingSubcategoryCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filteraccounting_category_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filteraccounting_category_id: None | str | Unset
    if isinstance(filteraccounting_category_id, Unset):
        json_filteraccounting_category_id = UNSET
    else:
        json_filteraccounting_category_id = filteraccounting_category_id
    params["filter[accounting_category_id]"] = json_filteraccounting_category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounting_subcategories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountingSubcategoryCollection | None:
    if response.status_code == 200:
        response_200 = AccountingSubcategoryCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountingSubcategoryCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filteraccounting_category_id: None | str | Unset = UNSET,
) -> Response[AccountingSubcategoryCollection]:
    """Retrieve all accounting subcategories

    Args:
        filteraccounting_category_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountingSubcategoryCollection]
    """

    kwargs = _get_kwargs(
        filteraccounting_category_id=filteraccounting_category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filteraccounting_category_id: None | str | Unset = UNSET,
) -> AccountingSubcategoryCollection | None:
    """Retrieve all accounting subcategories

    Args:
        filteraccounting_category_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountingSubcategoryCollection
    """

    return sync_detailed(
        client=client,
        filteraccounting_category_id=filteraccounting_category_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filteraccounting_category_id: None | str | Unset = UNSET,
) -> Response[AccountingSubcategoryCollection]:
    """Retrieve all accounting subcategories

    Args:
        filteraccounting_category_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountingSubcategoryCollection]
    """

    kwargs = _get_kwargs(
        filteraccounting_category_id=filteraccounting_category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filteraccounting_category_id: None | str | Unset = UNSET,
) -> AccountingSubcategoryCollection | None:
    """Retrieve all accounting subcategories

    Args:
        filteraccounting_category_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountingSubcategoryCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            filteraccounting_category_id=filteraccounting_category_id,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accounting_category_collection import AccountingCategoryCollection
from ...models.get_accounting_categories_filterkind import GetAccountingCategoriesFilterkind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterkind: GetAccountingCategoriesFilterkind | Unset = UNSET,
    filterprefix: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filterkind: str | Unset = UNSET
    if not isinstance(filterkind, Unset):
        json_filterkind = filterkind.value

    params["filter[kind]"] = json_filterkind

    json_filterprefix: None | str | Unset
    if isinstance(filterprefix, Unset):
        json_filterprefix = UNSET
    else:
        json_filterprefix = filterprefix
    params["filter[prefix]"] = json_filterprefix

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounting_categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountingCategoryCollection | None:
    if response.status_code == 200:
        response_200 = AccountingCategoryCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountingCategoryCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetAccountingCategoriesFilterkind | Unset = UNSET,
    filterprefix: None | str | Unset = UNSET,
) -> Response[AccountingCategoryCollection]:
    """Retrieve all accounting categories

    Args:
        filterkind (GetAccountingCategoriesFilterkind | Unset):
        filterprefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountingCategoryCollection]
    """

    kwargs = _get_kwargs(
        filterkind=filterkind,
        filterprefix=filterprefix,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetAccountingCategoriesFilterkind | Unset = UNSET,
    filterprefix: None | str | Unset = UNSET,
) -> AccountingCategoryCollection | None:
    """Retrieve all accounting categories

    Args:
        filterkind (GetAccountingCategoriesFilterkind | Unset):
        filterprefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountingCategoryCollection
    """

    return sync_detailed(
        client=client,
        filterkind=filterkind,
        filterprefix=filterprefix,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetAccountingCategoriesFilterkind | Unset = UNSET,
    filterprefix: None | str | Unset = UNSET,
) -> Response[AccountingCategoryCollection]:
    """Retrieve all accounting categories

    Args:
        filterkind (GetAccountingCategoriesFilterkind | Unset):
        filterprefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountingCategoryCollection]
    """

    kwargs = _get_kwargs(
        filterkind=filterkind,
        filterprefix=filterprefix,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetAccountingCategoriesFilterkind | Unset = UNSET,
    filterprefix: None | str | Unset = UNSET,
) -> AccountingCategoryCollection | None:
    """Retrieve all accounting categories

    Args:
        filterkind (GetAccountingCategoriesFilterkind | Unset):
        filterprefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountingCategoryCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            filterkind=filterkind,
            filterprefix=filterprefix,
        )
    ).parsed

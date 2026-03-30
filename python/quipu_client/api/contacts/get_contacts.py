from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_collection import ContactCollection
from ...models.get_contacts_filterkind import GetContactsFilterkind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterq: None | str | Unset = UNSET,
    filterkind: GetContactsFilterkind | Unset = UNSET,
    filtertax_id: None | str | Unset = UNSET,
    filtercountry: None | str | Unset = UNSET,
    filteremail: None | str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filterq: None | str | Unset
    if isinstance(filterq, Unset):
        json_filterq = UNSET
    else:
        json_filterq = filterq
    params["filter[q]"] = json_filterq

    json_filterkind: str | Unset = UNSET
    if not isinstance(filterkind, Unset):
        json_filterkind = filterkind.value

    params["filter[kind]"] = json_filterkind

    json_filtertax_id: None | str | Unset
    if isinstance(filtertax_id, Unset):
        json_filtertax_id = UNSET
    else:
        json_filtertax_id = filtertax_id
    params["filter[tax_id]"] = json_filtertax_id

    json_filtercountry: None | str | Unset
    if isinstance(filtercountry, Unset):
        json_filtercountry = UNSET
    else:
        json_filtercountry = filtercountry
    params["filter[country]"] = json_filtercountry

    json_filteremail: None | str | Unset
    if isinstance(filteremail, Unset):
        json_filteremail = UNSET
    else:
        json_filteremail = filteremail
    params["filter[email]"] = json_filteremail

    params["sort"] = sort

    params["page[number]"] = pagenumber

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContactCollection | None:
    if response.status_code == 200:
        response_200 = ContactCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ContactCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterq: None | str | Unset = UNSET,
    filterkind: GetContactsFilterkind | Unset = UNSET,
    filtertax_id: None | str | Unset = UNSET,
    filtercountry: None | str | Unset = UNSET,
    filteremail: None | str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
) -> Response[ContactCollection]:
    """Retrieve all contacts

    Args:
        filterq (None | str | Unset):
        filterkind (GetContactsFilterkind | Unset):
        filtertax_id (None | str | Unset):
        filtercountry (None | str | Unset):
        filteremail (None | str | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactCollection]
    """

    kwargs = _get_kwargs(
        filterq=filterq,
        filterkind=filterkind,
        filtertax_id=filtertax_id,
        filtercountry=filtercountry,
        filteremail=filteremail,
        sort=sort,
        pagenumber=pagenumber,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filterq: None | str | Unset = UNSET,
    filterkind: GetContactsFilterkind | Unset = UNSET,
    filtertax_id: None | str | Unset = UNSET,
    filtercountry: None | str | Unset = UNSET,
    filteremail: None | str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
) -> ContactCollection | None:
    """Retrieve all contacts

    Args:
        filterq (None | str | Unset):
        filterkind (GetContactsFilterkind | Unset):
        filtertax_id (None | str | Unset):
        filtercountry (None | str | Unset):
        filteremail (None | str | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactCollection
    """

    return sync_detailed(
        client=client,
        filterq=filterq,
        filterkind=filterkind,
        filtertax_id=filtertax_id,
        filtercountry=filtercountry,
        filteremail=filteremail,
        sort=sort,
        pagenumber=pagenumber,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterq: None | str | Unset = UNSET,
    filterkind: GetContactsFilterkind | Unset = UNSET,
    filtertax_id: None | str | Unset = UNSET,
    filtercountry: None | str | Unset = UNSET,
    filteremail: None | str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
) -> Response[ContactCollection]:
    """Retrieve all contacts

    Args:
        filterq (None | str | Unset):
        filterkind (GetContactsFilterkind | Unset):
        filtertax_id (None | str | Unset):
        filtercountry (None | str | Unset):
        filteremail (None | str | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactCollection]
    """

    kwargs = _get_kwargs(
        filterq=filterq,
        filterkind=filterkind,
        filtertax_id=filtertax_id,
        filtercountry=filtercountry,
        filteremail=filteremail,
        sort=sort,
        pagenumber=pagenumber,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filterq: None | str | Unset = UNSET,
    filterkind: GetContactsFilterkind | Unset = UNSET,
    filtertax_id: None | str | Unset = UNSET,
    filtercountry: None | str | Unset = UNSET,
    filteremail: None | str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
) -> ContactCollection | None:
    """Retrieve all contacts

    Args:
        filterq (None | str | Unset):
        filterkind (GetContactsFilterkind | Unset):
        filtertax_id (None | str | Unset):
        filtercountry (None | str | Unset):
        filteremail (None | str | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            filterq=filterq,
            filterkind=filterkind,
            filtertax_id=filtertax_id,
            filtercountry=filtercountry,
            filteremail=filteremail,
            sort=sort,
            pagenumber=pagenumber,
        )
    ).parsed

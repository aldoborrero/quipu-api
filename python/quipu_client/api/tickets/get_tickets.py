from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tickets_filterfield_query import GetTicketsFilterfieldQuery
from ...models.get_tickets_filterkind import GetTicketsFilterkind
from ...models.get_tickets_filterpayment_status import GetTicketsFilterpaymentStatus
from ...models.get_tickets_include import GetTicketsInclude
from ...models.ticket_collection import TicketCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterkind: GetTicketsFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetTicketsFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetTicketsFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetTicketsInclude | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filterkind: str | Unset = UNSET
    if not isinstance(filterkind, Unset):
        json_filterkind = filterkind.value

    params["filter[kind]"] = json_filterkind

    json_filterq: None | str | Unset
    if isinstance(filterq, Unset):
        json_filterq = UNSET
    else:
        json_filterq = filterq
    params["filter[q]"] = json_filterq

    json_filterperiod: None | str | Unset
    if isinstance(filterperiod, Unset):
        json_filterperiod = UNSET
    else:
        json_filterperiod = filterperiod
    params["filter[period]"] = json_filterperiod

    json_filterpayment_status: str | Unset = UNSET
    if not isinstance(filterpayment_status, Unset):
        json_filterpayment_status = filterpayment_status.value

    params["filter[payment_status]"] = json_filterpayment_status

    json_filtercontact_id: None | str | Unset
    if isinstance(filtercontact_id, Unset):
        json_filtercontact_id = UNSET
    else:
        json_filtercontact_id = filtercontact_id
    params["filter[contact_id]"] = json_filtercontact_id

    json_filterfield_query: dict[str, Any] | Unset = UNSET
    if not isinstance(filterfield_query, Unset):
        json_filterfield_query = filterfield_query.to_dict()
    if not isinstance(json_filterfield_query, Unset):
        params.update(json_filterfield_query)

    params["sort"] = sort

    params["page[number]"] = pagenumber

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include.value

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tickets",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TicketCollection | None:
    if response.status_code == 200:
        response_200 = TicketCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TicketCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetTicketsFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetTicketsFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetTicketsFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetTicketsInclude | Unset = UNSET,
) -> Response[TicketCollection]:
    """Retrieve all tickets

    Args:
        filterkind (GetTicketsFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetTicketsFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetTicketsFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetTicketsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TicketCollection]
    """

    kwargs = _get_kwargs(
        filterkind=filterkind,
        filterq=filterq,
        filterperiod=filterperiod,
        filterpayment_status=filterpayment_status,
        filtercontact_id=filtercontact_id,
        filterfield_query=filterfield_query,
        sort=sort,
        pagenumber=pagenumber,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetTicketsFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetTicketsFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetTicketsFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetTicketsInclude | Unset = UNSET,
) -> TicketCollection | None:
    """Retrieve all tickets

    Args:
        filterkind (GetTicketsFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetTicketsFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetTicketsFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetTicketsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TicketCollection
    """

    return sync_detailed(
        client=client,
        filterkind=filterkind,
        filterq=filterq,
        filterperiod=filterperiod,
        filterpayment_status=filterpayment_status,
        filtercontact_id=filtercontact_id,
        filterfield_query=filterfield_query,
        sort=sort,
        pagenumber=pagenumber,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetTicketsFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetTicketsFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetTicketsFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetTicketsInclude | Unset = UNSET,
) -> Response[TicketCollection]:
    """Retrieve all tickets

    Args:
        filterkind (GetTicketsFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetTicketsFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetTicketsFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetTicketsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TicketCollection]
    """

    kwargs = _get_kwargs(
        filterkind=filterkind,
        filterq=filterq,
        filterperiod=filterperiod,
        filterpayment_status=filterpayment_status,
        filtercontact_id=filtercontact_id,
        filterfield_query=filterfield_query,
        sort=sort,
        pagenumber=pagenumber,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetTicketsFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetTicketsFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetTicketsFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetTicketsInclude | Unset = UNSET,
) -> TicketCollection | None:
    """Retrieve all tickets

    Args:
        filterkind (GetTicketsFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetTicketsFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetTicketsFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetTicketsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TicketCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            filterkind=filterkind,
            filterq=filterq,
            filterperiod=filterperiod,
            filterpayment_status=filterpayment_status,
            filtercontact_id=filtercontact_id,
            filterfield_query=filterfield_query,
            sort=sort,
            pagenumber=pagenumber,
            include=include,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_invoices_filterfield_query import GetInvoicesFilterfieldQuery
from ...models.get_invoices_filterkind import GetInvoicesFilterkind
from ...models.get_invoices_filterpayment_status import GetInvoicesFilterpaymentStatus
from ...models.get_invoices_include import GetInvoicesInclude
from ...models.invoice_collection import InvoiceCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterkind: GetInvoicesFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetInvoicesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetInvoicesFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetInvoicesInclude | Unset = UNSET,
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
        "url": "/invoices",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceCollection | None:
    if response.status_code == 200:
        response_200 = InvoiceCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filterkind: GetInvoicesFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetInvoicesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetInvoicesFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetInvoicesInclude | Unset = UNSET,
) -> Response[InvoiceCollection]:
    """Retrieve all invoices

    Args:
        filterkind (GetInvoicesFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetInvoicesFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetInvoicesFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetInvoicesInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceCollection]
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
    filterkind: GetInvoicesFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetInvoicesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetInvoicesFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetInvoicesInclude | Unset = UNSET,
) -> InvoiceCollection | None:
    """Retrieve all invoices

    Args:
        filterkind (GetInvoicesFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetInvoicesFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetInvoicesFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetInvoicesInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceCollection
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
    filterkind: GetInvoicesFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetInvoicesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetInvoicesFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetInvoicesInclude | Unset = UNSET,
) -> Response[InvoiceCollection]:
    """Retrieve all invoices

    Args:
        filterkind (GetInvoicesFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetInvoicesFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetInvoicesFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetInvoicesInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceCollection]
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
    filterkind: GetInvoicesFilterkind | Unset = UNSET,
    filterq: None | str | Unset = UNSET,
    filterperiod: None | str | Unset = UNSET,
    filterpayment_status: GetInvoicesFilterpaymentStatus | Unset = UNSET,
    filtercontact_id: None | str | Unset = UNSET,
    filterfield_query: GetInvoicesFilterfieldQuery | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    include: GetInvoicesInclude | Unset = UNSET,
) -> InvoiceCollection | None:
    """Retrieve all invoices

    Args:
        filterkind (GetInvoicesFilterkind | Unset):
        filterq (None | str | Unset):
        filterperiod (None | str | Unset):  Example: 2015-Q1.
        filterpayment_status (GetInvoicesFilterpaymentStatus | Unset):
        filtercontact_id (None | str | Unset):
        filterfield_query (GetInvoicesFilterfieldQuery | Unset):
        sort (str | Unset):  Example: -issue_date,total_amount.
        pagenumber (int | Unset):
        include (GetInvoicesInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceCollection
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

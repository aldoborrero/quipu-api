"""OAuth2 client_credentials flow for Quipu API.

Provides a QuipuAuth (httpx.Auth subclass) that transparently handles
token exchange and refresh. Inject it into the generated Client via httpx_args.
"""

from __future__ import annotations

import os
import time
from typing import Generator

import httpx

from quipu_client import Client

BASE_URL = "https://getquipu.com"


class QuipuAuth(httpx.Auth):
    """httpx.Auth that manages Quipu's OAuth2 client_credentials flow.

    Automatically fetches a Bearer token on first request and refreshes
    it 60 seconds before expiry.
    """

    def __init__(
        self,
        app_id: str | None = None,
        app_secret: str | None = None,
        *,
        base_url: str = BASE_URL,
        scope: str = "ecommerce",
    ) -> None:
        self.app_id = app_id or os.environ["QUIPU_APP_ID"]
        self.app_secret = app_secret or os.environ["QUIPU_APP_SECRET"]
        self.base_url = base_url
        self.scope = scope
        self._access_token: str | None = None
        self._expires_in: int = 0
        self._token_acquired_at: float = 0

    @property
    def token_expired(self) -> bool:
        if self._access_token is None:
            return True
        elapsed = time.time() - self._token_acquired_at
        return elapsed >= (self._expires_in - 60)

    def _fetch_token(self) -> None:
        """Exchange client credentials for a Bearer token."""
        resp = httpx.post(
            f"{self.base_url}/oauth/token",
            data={"grant_type": "client_credentials", "scope": self.scope},
            auth=(self.app_id, self.app_secret),
        )
        resp.raise_for_status()
        data = resp.json()
        self._access_token = data["access_token"]
        self._expires_in = data.get("expires_in", 7200)
        self._token_acquired_at = time.time()

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        if self.token_expired:
            self._fetch_token()
        assert self._access_token is not None
        request.headers["Authorization"] = f"Bearer {self._access_token}"
        yield request


def create_client(
    app_id: str | None = None,
    app_secret: str | None = None,
    *,
    base_url: str = BASE_URL,
    scope: str = "ecommerce",
) -> Client:
    """Create a Client with auto-refreshing OAuth2 auth.

    Usage:
        client = create_client()
        from quipu_client.api.contacts import get_contacts
        contacts = get_contacts.sync(client=client)
    """
    auth = QuipuAuth(app_id, app_secret, base_url=base_url, scope=scope)
    return Client(
        base_url=base_url,
        headers={"Accept": "application/vnd.quipu.v1+json"},
        httpx_args={"auth": auth},
    )

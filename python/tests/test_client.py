"""Tests for the Quipu client auth wrapper and generated API."""

from __future__ import annotations

import time

import httpx
import pytest
from pytest_httpx import HTTPXMock

from quipu.auth import QuipuAuth, create_client

BASE = "https://getquipu.com"

TOKEN_RESPONSE = {
    "token_type": "bearer",
    "created_at": 1700000000,
    "access_token": "test-token-123",
    "refresh_token": None,
    "expires_in": 7200,
}


class TestQuipuAuth:
    def test_token_exchange(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(url=f"{BASE}/oauth/token", json=TOKEN_RESPONSE)

        auth = QuipuAuth(app_id="my-id", app_secret="my-secret", base_url=BASE)
        assert auth.token_expired is True

        # Trigger the auth flow via a real request
        httpx_mock.add_response(url=f"{BASE}/contacts", json={"data": []})
        with httpx.Client(base_url=BASE, auth=auth) as client:
            client.get("/contacts")

        # Verify the token request was made with correct form data
        token_req = httpx_mock.get_requests()[0]
        assert token_req.url.path == "/oauth/token"
        assert b"grant_type=client_credentials" in token_req.content
        assert b"scope=ecommerce" in token_req.content

        # Verify the contacts request got the Bearer header
        contacts_req = httpx_mock.get_requests()[1]
        assert contacts_req.headers["Authorization"] == "Bearer test-token-123"

    def test_token_reuse_across_requests(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(url=f"{BASE}/oauth/token", json=TOKEN_RESPONSE)
        httpx_mock.add_response(url=f"{BASE}/contacts", json={"data": []})
        httpx_mock.add_response(url=f"{BASE}/contacts", json={"data": []})

        auth = QuipuAuth(app_id="my-id", app_secret="my-secret", base_url=BASE)
        with httpx.Client(base_url=BASE, auth=auth) as client:
            client.get("/contacts")
            client.get("/contacts")

        # Only one token request, two contacts requests
        token_requests = [r for r in httpx_mock.get_requests() if r.url.path == "/oauth/token"]
        assert len(token_requests) == 1

    def test_token_refresh_on_expiry(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(url=f"{BASE}/oauth/token", json=TOKEN_RESPONSE)
        httpx_mock.add_response(url=f"{BASE}/contacts", json={"data": []})

        auth = QuipuAuth(app_id="my-id", app_secret="my-secret", base_url=BASE)
        with httpx.Client(base_url=BASE, auth=auth) as client:
            client.get("/contacts")

        # Simulate token expiry
        auth._token_acquired_at = time.time() - 7200

        httpx_mock.add_response(
            url=f"{BASE}/oauth/token",
            json={**TOKEN_RESPONSE, "access_token": "refreshed-token"},
        )
        httpx_mock.add_response(url=f"{BASE}/contacts", json={"data": []})

        with httpx.Client(base_url=BASE, auth=auth) as client:
            client.get("/contacts")

        # Second token request should have been made
        token_requests = [r for r in httpx_mock.get_requests() if r.url.path == "/oauth/token"]
        assert len(token_requests) == 2

        # Last contacts request should use the refreshed token
        contacts_requests = [r for r in httpx_mock.get_requests() if r.url.path == "/contacts"]
        assert contacts_requests[-1].headers["Authorization"] == "Bearer refreshed-token"


class TestCreateClient:
    def test_creates_client_with_auth(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(url=f"{BASE}/oauth/token", json=TOKEN_RESPONSE)
        httpx_mock.add_response(url=f"{BASE}/contacts", json={"data": []})

        client = create_client(app_id="my-id", app_secret="my-secret", base_url=BASE)
        with client:
            resp = client.get_httpx_client().get("/contacts")

        assert resp.status_code == 200
        # Verify Accept header is set
        contacts_req = [r for r in httpx_mock.get_requests() if r.url.path == "/contacts"][0]
        assert "application/vnd.quipu.v1+json" in contacts_req.headers["Accept"]

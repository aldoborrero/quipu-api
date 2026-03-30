"""Quipu API — thin auth wrapper over the generated client."""

from quipu.auth import QuipuAuth, create_client
from quipu_client import Client

__all__ = [
    "Client",
    "QuipuAuth",
    "create_client",
]

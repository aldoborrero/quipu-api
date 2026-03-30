# quipu-client

Multi-language [Quipu](https://getquipu.com) API client, generated from OpenAPI.

The OpenAPI source of truth is `openapi/openapi.yaml`.

## Prerequisites

- [Nix](https://nixos.org/) with flakes enabled
- [direnv](https://direnv.net/) (optional, for automatic shell activation)

## Quick start

```bash
# Allow direnv (loads the default devshell)
direnv allow

# Or enter the Python devshell manually
nix develop .#python

# Build the Python package
nix build .#quipu-python

# Run checks (pytest, mypy, treefmt)
nix flake check

# Format code (nixfmt + ruff)
nix fmt
```

## Structure

```
quipu-client/
├── flake.nix                 # Nix flake (wires numtide/blueprint)
├── openapi/                  # OpenAPI specs (source of truth)
│   └── openapi.yaml
├── nix/                      # All Nix files (blueprint prefix)
│   ├── devshell.nix          # Default devshell
│   ├── packages/quipu-python # Python package derivation
│   ├── checks/               # nix flake check targets (pytest, mypy, treefmt)
│   └── formatter.nix         # treefmt-nix config (nixfmt + ruff)
└── python/                   # Python client
    ├── quipu_client/     # Generated from openapi.json
    ├── quipu/                # Thin auth wrapper (OAuth2)
    └── tests/
```

## Authentication

Quipu uses OAuth2 `client_credentials`. Set your credentials in `.envrc.local` (gitignored):

```bash
export QUIPU_APP_ID="your-app-id"
export QUIPU_APP_SECRET="your-app-secret"
```

## Python usage

```python
from quipu import create_client
from quipu_client.api.contacts import get_contacts
from quipu_client.api.invoices import create_invoice

# Client auto-refreshes the OAuth2 token
with create_client() as client:
    contacts = get_contacts.sync(client=client)
    invoice = create_invoice.sync(client=client, body=...)
```

## Regenerating the client

When the OpenAPI spec changes:

```bash
bash scripts/regenerate-quipu.sh
```

This script regenerates the Python client from `openapi/openapi.yaml`.
It also applies a small preprocessing step needed for `openapi-python-client`:

- removes explicit `Accept`/`Content-Type` header parameters from operations
- extracts a shared relationship schema to avoid duplicate inline model names

After regeneration, the generated package is written to `python/quipu_client/`.

## Adding a new language

1. Add `nix/devshells/{lang}.nix`
1. Add `nix/packages/quipu-{lang}/default.nix`
1. Generate client from `openapi/openapi.json` into `{lang}/`

## License

MIT

{ pkgs }:
let
  python = pkgs.python3.withPackages (
    ps: with ps; [
      httpx
      attrs
      python-dateutil
      pytest
      pytest-httpx
    ]
  );
in
pkgs.mkShell {
  packages = [
    python
    pkgs.ruff
    pkgs.openapi-generator-cli
  ];

  shellHook = ''
    echo "quipu-client python shell"
  '';
}

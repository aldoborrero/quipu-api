{ pkgs }:
pkgs.mkShell {
  packages = [
    pkgs.nodejs_22
    pkgs.nodePackages.typescript
    pkgs.openapi-generator-cli
  ];

  shellHook = ''
    echo "quipu-client typescript shell"
  '';
}

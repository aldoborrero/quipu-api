{
  pkgs,
  inputs,
  system,
  ...
}:
let
  inherit (inputs.self.packages.${system}) formatter;
in
pkgs.runCommand "treefmt-check" { buildInputs = [ formatter ]; } ''
  cp -r ${inputs.self} src
  chmod -R u+w src
  cd src
  export HOME=$(mktemp -d)
  treefmt --ci --no-cache
  touch $out
''

{
  pkgs,
  inputs,
  system,
  ...
}:
let
  inherit (inputs.self.packages.${system}) quipu-python;
in
pkgs.runCommand "python-tests"
  {
    buildInputs = [
      quipu-python
      pkgs.python3Packages.pytest
      pkgs.python3Packages.pytest-httpx
    ];
  }
  ''
    cd ${inputs.self}/python
    pytest tests/
    touch $out
  ''

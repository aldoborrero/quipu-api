{
  pkgs,
  inputs,
  system,
  ...
}:
let
  inherit (inputs.self.packages.${system}) quipu-python;
in
pkgs.runCommand "python-mypy"
  {
    buildInputs = [
      quipu-python
      pkgs.python3Packages.mypy
    ];
  }
  ''
    cd ${inputs.self}/python
    mypy quipu/
    touch $out
  ''

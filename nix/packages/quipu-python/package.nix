{ python3Packages, ... }:
python3Packages.buildPythonPackage {
  pname = "quipu-api-client";
  version = "1.0.0";
  src = ../../../python;
  format = "pyproject";

  build-system = [ python3Packages.setuptools ];

  dependencies = with python3Packages; [
    httpx
    attrs
    python-dateutil
  ];

  nativeCheckInputs = with python3Packages; [
    pytest
    pytest-httpx
  ];

  pythonImportsCheck = [ "quipu_client" ];
}

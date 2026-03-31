{ pkgs, ... }:
pkgs.buildNpmPackage {
  pname = "quipu-api-client-typescript";
  version = "1.0.0";
  src = ../../../typescript;

  npmDepsHash = "";

  buildPhase = ''
    npx tsc
  '';

  installPhase = ''
    mkdir -p $out
    cp -r dist $out/
    cp package.json $out/
  '';
}

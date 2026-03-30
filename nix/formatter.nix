{ inputs, pkgs, ... }:
let
  treefmt = inputs.treefmt-nix.lib.evalModule pkgs {
    projectRootFile = "flake.nix";

    # nix
    programs.nixfmt.enable = true;
    programs.deadnix.enable = true;
    programs.statix.enable = true;
    settings.deadnix.pipeline = "nix";
    settings.deadnix.priority = 1;
    settings.statix.pipeline = "nix";
    settings.statix.priority = 2;
    settings.nixfmt.pipeline = "nix";
    settings.nixfmt.priority = 3;

    # shell
    programs.shellcheck.enable = true;
    programs.shfmt.enable = true;
    settings.shellcheck.pipeline = "shell";
    settings.shellcheck.priority = 1;
    settings.shfmt.pipeline = "shell";
    settings.shfmt.priority = 2;

    # markdown
    programs.mdformat.enable = true;

    # python
    programs.ruff-format.enable = true;
  };
in
treefmt.config.build.wrapper

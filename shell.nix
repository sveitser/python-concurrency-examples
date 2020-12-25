{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
  buildInputs = [
    (python3.withPackages (ps: with ps; [
      black
      isort
      pytest
      pytest-watch
    ]))
  ];
}

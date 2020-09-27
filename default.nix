with import <nixpkgs> {};

python3.pkgs.buildPythonApplication rec {
  name = "trello-capture";
  src = ./.;
  propagatedBuildInputs = [
    python3
    python3Packages.sh
    python3Packages.requests
  ];
}

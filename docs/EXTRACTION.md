# Lokalna ekstrakcja API — wymagania i szybki start

Ten dokument zawiera instrukcje instalacji wymagań systemowych i Pythonowych potrzebnych do uruchomienia ekstraktora (libclang + Node/tree-sitter).

## Co NIE trafia do requirements.txt
Plik `requirements.txt` obsługuje tylko pakiety instalowane przez pip (Python). Narzędzia takie jak `cmake`, `clang/libclang`, `node`, `npm`, `build-essential` muszą być zainstalowane jako pakiety systemowe (apt/brew/choco/WSL).

## Instalacja (Ubuntu / Debian)
Najwygodniej uruchomić przygotowany skrypt (wymaga sudo):
```bash
sudo chmod +x scripts/bootstrap-ubuntu.sh
sudo ./scripts/bootstrap-ubuntu.sh
```

Ręczne polecenia (alternatywnie):
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get update
sudo apt-get install -y build-essential cmake git curl ca-certificates jq \
  python3 python3-venv python3-pip nodejs npm clang libclang-dev llvm pkg-config
```

## Instalacja zależności Pythonowych
Utwórz wirtualne środowisko i zainstaluj requirements:
```bash
python3 -m venv .venv-extract
source .venv-extract/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
Wymagane w `requirements.txt` (repo zawiera paczki Sphinx + dodałem bindingi do clang):
- clang (python bindings)
- wheel, setuptools (pomocne przy budowaniu)

## Instalacja parserów tree-sitter (opcjonalne)
Jeśli chcesz korzystać z tree-sitter (Node extractor):
```bash
npm install --no-audit --no-fund tree-sitter tree-sitter-cpp tree-sitter-lua
# lub, jeśli używasz package.json:
# npm ci
```

## Szybkie sanity-checki
- Sprawdź Node:
  node -v
- Sprawdź Python + clang binding:
  python3 -c "import clang.cindex; print('clang binding ok')"
- Jeżeli import działa, ale libclang nie ładuje, możesz wskazać bibliotekę:
  ```py
  python3 - <<PY
  import clang.cindex as c
  c.Config.set_library_file('/usr/lib/llvm-14/lib/libclang.so')  # dostosuj ścieżkę
  print('ok')
  PY
  ```
- Wygeneruj compile_commands.json:
  ./scripts/generate-compile-commands.sh
  test -f compile_commands.json && echo "compile_commands.json OK"

## Uruchomienie pełnego pipeline (lokalnie)
- Szybki test (bez libclang):
  ./scripts/run-extract-full.sh --no-venv --skip-libclang
- Pełny run (po przygotowaniu venv i zainstalowaniu requirements):
  source .venv-extract/bin/activate
  ./scripts/run-extract-full.sh --install-deps

## Gdzie szukać wyników i logów
- tmp/extract_report.txt — raport orchestratora
- tmp/extract-api.log — log Node extractor
- tmp/clang_entities.json — wynik libclang (jeśli uruchomiony)
- docs/_data/_api_manifest.json — manifest do walidacji
- docs/authoring/datasets/ — istniejące CSV do porównania

## Troubleshooting
- Jeśli `python3 -c "import clang.cindex"` zgłasza błąd:
  - upewnij się, że `libclang-dev` jest zainstalowany,
  - w razie potrzeby ustaw `LD_LIBRARY_PATH` (Linux) lub `DYLD_LIBRARY_PATH` (macOS),
  - lub ustaw bibliotekę w kodzie: `c.Config.set_library_file('/path/to/libclang.so')`.
- Jeśli `npm install` dla tree-sitter failuje:
  - zainstaluj `build-essential` i `python` (node-gyp deps).
- Jeśli w CI chcesz testować libclang, rozważ Docker z zainstalowanym LLVM lub specjalny runner (czas i zależności są większe).

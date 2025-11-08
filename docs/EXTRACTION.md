# Lokalna ekstrakcja API — wymagania i szybki start

Ten dokument opisuje wymagania i kroki do uruchomienia lokalnego pipeline ekstrakcji (libclang + Node/tree-sitter).

Wymagania systemowe (minimum)
- cmake >= 3.5
- node >= 18 (LTS 18 zalecane)
- npm
- python3 (3.8+) i pip
- libclang (llvm/clang) + nagłówki (libclang-dev) — wymagane do użycia libclang helpera
- jq (opcjonalnie, do JSON sanity checks)
- build-essential (make, g++) — potrzebne przy kompilacji natywnych zależności npm / node-gyp

Szybkie instalacje

Ubuntu / Debian:
```bash
# node (NodeSource), a potem podstawowe narzędzia
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get update
sudo apt-get install -y nodejs cmake jq python3 python3-venv python3-pip build-essential clang libclang-dev llvm
```

macOS (Homebrew):
```bash
brew update
brew install node cmake python jq llvm
# jeśli libclang nie jest wykryte, ustaw:
# export LD_LIBRARY_PATH="/opt/homebrew/opt/llvm/lib:$LD_LIBRARY_PATH"
```

Windows:
- Najwygodniej użyć WSL (Ubuntu) i postępować jak dla Ubuntu.

Python (venv) — rekomendowane przed uruchomieniem libclang:
```bash
python3 -m venv .venv-extract
source .venv-extract/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Node (opcjonalnie, do tree-sitter):
```bash
npm install --no-audit --no-fund tree-sitter tree-sitter-cpp tree-sitter-lua
# albo jeśli używasz package.json:
npm ci
npm run install:parsers
```

Szybkie sanity checks:
```bash
# node
node -e "console.log(process.version)"

# python + clang binding
python3 -c "import clang.cindex; print('clang binding ok')"

# check compile_commands.json
./scripts/generate-compile-commands.sh
test -f compile_commands.json && echo "compile_commands.json OK"
```

Uruchomienie pełnego pipeline (orchestrator):
```bash
chmod +x scripts/*.sh
./scripts/run-extract-full.sh --install-deps
# lub dla szybkiego run w CI:
./scripts/run-extract-full.sh --no-venv --skip-libclang
```

Troubleshooting
- import clang.cindex fails: upewnij się, że masz libclang-dev zainstalowane i ewentualnie ustaw LD_LIBRARY_PATH/DYLD_LIBRARY_PATH do katalogu z libclang.
- npm install natywnych parserów wymaga build-essential / python / node-gyp — zainstaluj je jeśli pojawiają się błędy.

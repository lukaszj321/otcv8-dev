# Lokalna ekstrakcja API — wymagania i szybki start

Ten dokument opisuje wymagania, przygotowanie środowiska i kroki uruchomienia lokalnego pipeline'u ekstrakcji API używanego w projekcie. Zawiera instrukcje dla deweloperów (lokalnie) oraz wskazówki CI (smoke vs full).

Spis treści
- Wymagania
- Instalacja systemowa (Ubuntu / macOS / Windows(WSL))
- Python: venv i pip
- Node / tree-sitter (opcjonalnie)
- Szybkie sanity checks
- Uruchomienie orchestratora (scripts/run-extract-full.sh)
- Strategia CI (smoke vs full)
- Pinowanie libclang (reprodukowalność)
- Docker (opcjonalnie)
- Troubleshooting
- Gdzie szukać wyników i logów

---

## Wymagania

Minimalne narzędzia:
- cmake >= 3.5
- node >= 18 (LTS 18 rekomendowane)
- npm
- python3 (3.8+)
- pip, python3-venv
- libclang (systemowy) — wymagane dla pythonowego modułu clang
- jq (opcjonalnie, do sanity-checków)
- build-essential / make / g++ (potrzebne przy kompilacji natywnych modułów npm)

Pliki Pythonowe:
- `requirements.txt` — podstawowe zależności dokumentacji i dodatkowo: `clang`, `wheel`, `setuptools`.

---

## Instalacja systemowa

### Ubuntu / Debian (szybkie)
Możesz uruchomić przygotowany skrypt bootstrap (wymaga sudo):
```bash
sudo chmod +x scripts/bootstrap-ubuntu.sh
sudo ./scripts/bootstrap-ubuntu.sh
```

Jeśli chcesz instalować ręcznie:
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  build-essential cmake git curl ca-certificates jq \
  python3 python3-venv python3-pip nodejs npm \
  clang libclang-dev llvm pkg-config
```

Jeśli chcesz pinuć wersję libclang (rekomendowane dla pełnych jobów CI / reproducibility), zobacz sekcję "Pinowanie libclang".

### macOS (Homebrew)
```bash
brew update
brew install node cmake python jq llvm
# Jeśli libclang nie jest wykryty, możesz dodać:
# export LD_LIBRARY_PATH="/opt/homebrew/opt/llvm/lib:$LD_LIBRARY_PATH"
```

### Windows
Najwygodniej użyć WSL (Ubuntu) i postępować jak w sekcji Ubuntu.

---

## Python: venv i instalacja zależności

Zalecane: utworzyć venv i zainstalować `requirements.txt`.

```bash
python3 -m venv .venv-extract
source .venv-extract/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

W `requirements.txt` powinny być wpisane:
- pakiety Sphinx/dokumentacyjne (istniejące),
- oraz: `clang`, `wheel`, `setuptools` (python bindings i pomocnicze narzędzia).

Uwaga: `clang` (pip) to bindingi Pythona; nadal potrzebujesz natywnej biblioteki `libclang` (instalowanej przez systemowy pakiet `libclang-dev`).

---

## Node / tree-sitter (opcjonalnie)

Jeśli extractor Node wymaga parserów tree-sitter:
```bash
npm install --no-audit --no-fund tree-sitter tree-sitter-cpp tree-sitter-lua
# lub, jeśli jest package.json:
# npm ci
# npm run install:parsers
```

W CI używaj `actions/setup-node` + `cache: 'npm'` dla szybszych instalacji.

---

## Szybkie sanity checks

Po instalacji narzędzi sprawdź:
```bash
node -v
python3 --version
python3 -c "import clang.cindex; print('clang binding ok')"
```

Jeśli import `clang.cindex` się nie powiedzie, ale `clang` jest zainstalowany, może być konieczne ustawienie ścieżki do biblioteki natywnej (patrz Troubleshooting).

---

## Uruchomienie orchestratora (pełne, jedno polecenie)

Mamy skrypt orchestrator: `scripts/run-extract-full.sh`, który:
- przygotowuje (opcjonalnie) venv i pip,
- generuje `compile_commands.json`,
- uruchamia libclang helper i Node extractor,
- zapisuje logi i prosty raport w `tmp/`.

Przykłady:
- szybki (CI-like) run bez libclang:
  ```bash
  ./scripts/run-extract-full.sh --no-venv --skip-libclang
  ```
- pełny lokalny run (instaluje pip deps):
  ```bash
  ./scripts/run-extract-full.sh --install-deps
  ```

Po uruchomieniu sprawdź:
- tmp/extract_report.txt
- tmp/extract-api.log
- tmp/clang_entities.json (jeśli libclang)
- docs/_data/_api_manifest.json i docs/_data/_api_entities.json (jeśli extractor je generuje)

---

## Strategia CI: smoke vs full

- PR (smoke-check)
  - Szybki job, uruchamiany na pull_request. Uruchamia Node extractor i podstawowe sanity checks. Nie instaluje libclang ani heavy deps. Powinien trwać krótko (np. < 15 min).
- Full-extract (manual / nightly)
  - Oddzielny workflow (workflow_dispatch / schedule) wykonujący pełny przebieg z pinned libclang. Ten job może trwać dłużej i instalować ciężkie zależności albo używać przygotowanego Docker image z wszystkimi zależnościami.
- Opcjonalnie: trigger full-extract na PR gdy maintainer doda label `run/full-extract`.

Powód: oszczędność czasu i minut CI przy PR-ach, a jednocześnie możliwość wykonania pełnej, powtarzalnej ekstrakcji w określonych momentach.

---

## Pinowanie libclang (reproducibility)

Aby uniknąć ABI mismatch między python bindings a natywnym `libclang`, rekomendujemy pinowanie wersji libclang w pełnych jobach.

Przykład (Ubuntu, LLVM 14):
```bash
curl -sSL https://apt.llvm.org/llvm.sh | sudo bash -s -- 14
sudo apt-get update
sudo apt-get install -y libclang-14-dev llvm-14
```

W CI możesz zainstalować konkretny pakiet (`libclang-14-dev`), albo użyć Docker image z już zainstalowanymi, sprecyzowanymi wersjami (najwygodniej).

Jeśli Python załaduje bindingi, ale nie znajdzie natywnej biblioteki, można ją wskazać ręcznie:
```bash
python3 - <<PY
import clang.cindex as c
c.Config.set_library_file('/usr/lib/llvm-14/lib/libclang.so')
print('libclang set')
PY
```

---

## Docker (opcjonalnie)

Zalety:
- pełna powtarzalność środowiska,
- możesz zbudować obraz raz i używać go w CI (GHCR), co oszczędza czas.

Wady:
- budowa obrazu może być kosztowna, jeśli robisz to w każdym runie. Rekomendacja: buduj obraz raz i pushuj do GHCR, używaj gotowego obrazu w `full-extract` job.

Jeśli chcesz, użyj przygotowanego `Dockerfile` (repo zawiera przykład). Build & push do GHCR można zautomatyzować w oddzielnym workflow.

---

## Troubleshooting

1. Import `clang.cindex` nie działa:
   - Upewnij się, że zainstalowałeś `pip install clang` w venv.
   - Upewnij się, że systemowo zainstalowałeś `libclang-dev`/`llvm`.
   - Spróbuj wskazać bibliotekę: `c.Config.set_library_file('/path/to/libclang.so')`
   - Sprawdź LD_LIBRARY_PATH/DYLD_LIBRARY_PATH (Linux/macOS).

2. `npm install` dla tree-sitter failuje:
   - Zainstaluj `build-essential`, `python`, `node-gyp` dependencies.
   - Upewnij się, że Node/V8 mają kompatybilne binaria (Node 18 rekomendowane).

3. `cmake` nie generuje `compile_commands.json`:
   - Użyj: `cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON`
   - Sprawdź, czy w repo root jest `CMakeLists.txt`.
   - Jeśli projekt ma wiele build-ów/platform, wygeneruj `compile_commands.json` dla odpowiedniej konfiguracji.

4. Długie czasy w CI:
   - Nie instaluj libclang w każdym PR; używaj `--skip-libclang` w smoke jobach.
   - Dla pełnych runów używaj Docker image albo uruchamiaj je nocami/na żądanie.

---

## Gdzie szukać wyników i logów

- tmp/extract_report.txt — raport orchestratora
- tmp/extract-api.log — log Node extractor
- tmp/clang_entities.json — dane wyjściowe libclang
- docs/_data/_api_manifest.json — manifest do walidacji
- docs/authoring/datasets/ — przykładowe CSV do porównań / baseline

---

## Zalecane workflow developerskie

1. Przygotowanie:
   - `sudo ./scripts/bootstrap-ubuntu.sh` (opcjonalnie)
   - `python3 -m venv .venv-extract && source .venv-extract/bin/activate`
   - `pip install -r requirements.txt`
   - `npm ci` (jeśli jest package.json z parserami)

2. Smoke run (szybki):
   - `./scripts/run-extract-full.sh --no-venv --skip-libclang`

3. Full run (lokalny, z libclang):
   - `source .venv-extract/bin/activate`
   - `./scripts/run-extract-full.sh --install-deps`

4. W razie problemów: dołącz `tmp/*` artefakty do issue lub PR, żeby ułatwić debug.

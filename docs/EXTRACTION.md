## Lokalna ekstrakcja API

Krótki opis jak uruchomić ekstraktor lokalnie.

Wymagania:
- cmake (3.5+)
- node (v18+)
- python3 (+opcjonalnie pip package `clang`)
- jq (opcjonalnie, do sanity checks)

Szybkie kroki:
1. Nadaj prawa: `chmod +x scripts/*.sh`
2. Wygeneruj compile_commands: `./scripts/generate-compile-commands.sh`
3. Smoke-test libclang (opcjonalnie): 
   - `printf 'src/some/header.h\n' > tmp/test_headers.txt`
   - `python3 tools/clang-extract/clang_extract.py compile_commands.json tmp/test_headers.txt > tmp/test_clang.json`
4. Uruchom full run: `./scripts/run-extract-full.sh --install-deps`

Jeśli masz problemy:
- Sprawdź, czy import `clang.cindex` działa: `python3 -c "import clang.cindex; print('ok')"`
- Jeśli `libclang` nie ładuje, ustaw LD_LIBRARY_PATH lub zainstaluj pakiet libclang-dev odpowiedniej wersji.
``` ````

Co z tego jest najbardziej przydatne teraz?
- Jeśli chcesz tylko uruchomić lokalnie i szybko zobaczyć efekt: zrób smoke-test (kroki 2–4 powyżej). Nie potrzebujesz Docker/CI.
- Jeśli chcesz mieć powtarzalne środowisko lub CI dla PR: dodaj Dockerfile i / lub workflow CI (mogę przygotować PR z tymi plikami).

Powiedz co preferujesz:
- Uruchamiamy smoke-test i wkleisz logi (pomogę debugować)?
- Chcesz, żebym wygenerował i dodał do repo któryś z powyższych plików (Dockerfile, CI workflow, docs)? Jeśli tak — który plik dodać najpierw?

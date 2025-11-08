url=https://github.com/lukaszj321/otcv8-dev/blob/main/docs/CONTRIBUTING_EXTRACT.md
# Contributing: ekstrakcja API — krótka instrukcja

Jeśli zgłaszasz błąd lub chcesz, aby maintainer uruchomił pełen extract dla PR:

- Dołącz do PR/tmp artefakty, jeśli lokalny run się nie powiódł:
  - tmp/extract_report.txt
  - tmp/extract-api.log
  - tmp/clang_entities.json (jeśli istnieje)

- Aby poprosić o pełny run (libclang), dodaj labelę `run/full-extract` do PR (maintainer/owner może ją dodać).

- Jeżeli chcesz zrobić pełny run lokalnie:
  1. Uruchom bootstrap (opcjonalnie): `sudo ./scripts/bootstrap-ubuntu.sh 14`
  2. Utwórz venv i zainstaluj pip deps:
     ```
     python3 -m venv .venv-extract
     source .venv-extract/bin/activate
     pip install -r requirements.txt
     ```
  3. Wykonaj:
     ```
     ./scripts/run-extract-full.sh --install-deps --regression-threshold 10
     ```
     (przykład: threshold=10 -> fail, jeśli delta >10%)

- Jeśli zgłaszasz problem — wklej krótkie podsumowanie i załącz tmp/*.

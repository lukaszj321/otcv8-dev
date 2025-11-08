## Opis zmian / What changed
Krótki opis zmian w tym PR.

## Jak przetestować / How to test
- Uruchom lokalnie (szybkie): `./scripts/run-extract-full.sh --no-venv --skip-libclang`
- Jeśli chcesz uruchomić pełny extract (libclang) na tym PR: dodaj label `run/full-extract` do PR (maintainer/owner może go dodać).

## Debug i artefakty
Jeśli pipeline/ekstrakcja się nie powiodła, dołącz proszę:
- tmp/full-extract-summary.md (czytelne podsumowanie)
- tmp/extract_report.txt
- tmp/extract-api.log
- tmp/clang_entities.json (jeśli istnieje)

## Prośba o full run
Aby wymusić pełen run (może być kosztowny), dodaj labelę `run/full-extract` do PR (maintainer/owner powinien używać).

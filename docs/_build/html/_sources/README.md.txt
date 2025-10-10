# Jak używać

1. Skopiuj folder `docs/` i `.github/workflows/docs.yml` do **roota repo**.
2. Zmień ścieżki `literalinclude` w `docs/reference/*.md` na realne pliki w repo.
3. (Opcjonalnie) dodaj zasoby do `data/` — workflow skopiuje je do `docs/_static/data/`.
4. Budowa lokalnie:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
sphinx-build -b json docs docs/_build/json
```

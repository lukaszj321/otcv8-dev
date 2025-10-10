# Getting Started

## Wymagania
- Python 3.10+
- `pip install -r requirements.txt`
- Dokumentacja: `sphinx-build -b html docs docs/_build/html`

## Struktura
```
docs/
  _static/
  _data/
  api/
  overview/
  dashboard/
  rag/
```

## Budowanie
```bash
sphinx-build -b html docs docs/_build/html
```

## Deploy (GitHub Pages)
Workflow `docs.yml` zbuduje i opublikuje stronę.

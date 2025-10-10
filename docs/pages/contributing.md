# Contributing

Dzięki za chęć pomocy! Poniżej szybkie zasady współpracy nad dokumentacją i kodem:

## Style guide

- Pisz po **polsku**, zwięźle, z przykładami.
- Tytuły: `H2`/`H3`/`H4` poprawiają nawigację i generację ToC.
- Dla bloków kodu używaj potrójnych backticków z językiem (np. ` ```cpp `, ` ```python `).
- Dodawaj referencje do modułów (np. `01_core/api`, `03_modules`) oraz linki krzyżowe.

## Dodawanie stron

1. Umieść nową stronę w `docs/pages/` lub we właściwym rozdziale.
2. Dodaj ją do spisu treści (`index.md` / toctree).
3. Jeśli strona wymaga assetów (obrazy/CSV), dodaj je do `docs/assets/...` lub `docs/images/...`.

## PR checklist

- [ ] Strony mają sensowny tytuł i nagłówki (H2+).
- [ ] Kody mają poprawne bloki (język + copybutton działa).
- [ ] Diagrams: weryfikacja mermaid (podgląd w buildzie lokalnie).
- [ ] Linki względne działają po zbudowaniu lokalnie.

## Build lokalny

```bash
pip install -r requirements.txt
sphinx-build -b html docs docs/_build/html
# podgląd:
python -m http.server --directory docs/_build/html 8877
```

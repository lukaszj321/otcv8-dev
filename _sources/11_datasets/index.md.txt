# Datasets i integracja z katalogiem `data/`

Ten rozdział opisuje, jak korzystać z zasobów (obrazy, fonty, dźwięki) z repozytoryjnego katalogu `data/`.

## Jak to działa w Sphinx
W pliku `conf.py` dodaliśmy:
```python
html_extra_path = ["../data"]
```
Dzięki temu zawartość `../data` (względem `docs/`) jest kopiowana do wynikowej strony, więc można do niej linkować.

## Przykłady użycia
### Wstawienie obrazu
```markdown
![Tytuł obrazka](../data/graphics/example.png)
```

### Link do pobrania pliku
```markdown
[ Pobierz paczkę ](../data/archive/assets.7z)
```

> Uwaga: upewnij się, że pliki faktycznie istnieją w katalogu `data/` w repozytorium.

# Datasets i katalog `data/`

Katalog `data/` w repozytorium zawiera dodatkowe zasoby (obrazy, fonty, mapy). Aby z nich korzystać w dokumentacji, rekomendowana struktura to:

```
data/
  images/
  fonts/
  maps/
```

## Jak odwoływać się do plików z `data/`

- Najprościej **skopiować niezbędne zasoby** do `docs/_static` i odwoływać się ścieżką względną, np. `![](_static/logo.png)`.
- Można także dodać skrypt CI, który podczas builda **synchronizuje** wybrane pliki z `data/` do `docs/_static`.

> **Uwaga:** PyData theme wspiera tryb jasny/ciemny. Dobrze jest przygotować obrazy, które wyglądają poprawnie w obu trybach (np. przez transparentne PNG/SVG).


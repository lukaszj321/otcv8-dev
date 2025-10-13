# Datasets — folder `data/`

**Cel:** publikować zasoby (obrazy, fonty, binaria), by były dostępne z poziomu dokumentacji.

## Jak to działa
- W `conf.py` ustawiono `html_extra_path = ["../data"]`, więc wszystko z repo `data/` pojawi się obok strony.
- Linkowanie do pliku:
  - Markdown: `[Pobierz paczkę](../data/paczka.7z)`
  - Obraz: `![Sprite](../data/sprites/hero.png)`

## Struktura rekomendowana
```
data/
  sprites/
  fonts/
  audio/
  binaries/
  samples/
```


---
title: Odniesienia między rozdziałami (xref)
owner: docs/authoring
inputs:
  - źródła: docs/authoring/**/index.md
outputs:
  - md: dopisane sekcje "Zobacz też" (H2/H3) z linkami {{ref}}
render:
  - myst: autosectionlabel, admonitions
rules:
  - zakotwicz H2..H4, generuj stabilne kotwice
acceptance:
  - brak linków 404
---

## Zasada
Dla wspólnych słów-kluczy (np. "UI", "hotkeys", "events") dodawaj:
```md
## Zobacz też
- {{ref}} `04_ui/index` — Interfejs
- {{ref}} `02_events/index` — Zdarzenia
```

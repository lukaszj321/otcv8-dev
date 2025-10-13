
---
title: RAG datasets — ekstrakcja i manifest
owner: docs/authoring
inputs:
  - źródła: docs/**/*.md, src/**/*, layouts/**/*, schemas/**/*.json
  - zależności: node/python (do parsowania), utf-8
outputs:
  - datasets: docs/authoring/_data/{summary.csv,entities.csv}
  - manifest: docs/_data/_rag_manifest.json
  - wstawki: per-rozdział `docs/authoring/<chapter>/datasets/*.csv`
render:
  - myst: {csv-table}, admonitions
rules:
  - idempotent: nadpisuj/wyczyść poprzednie CSV
  - CSV: separator ',', nagłówki wymagane
acceptance:
  - manifest zawiera mapowanie rozdział → pliki CSV/MD
  - index rozdziałów osadza tabele
---

## Kolumny CSV
- `entity,type,count,file,anchor`
- `metric,key,value,scope`

## Wstawki MyST (do każdego index.md rozdziału)
```{{csv-table}} Podsumowanie
:header: "Klucz","Wartość","Zakres"
:file: datasets/summary.csv
:widths: 30, 40, 30
```

```{{csv-table}} Encje
:header: "Encja","Typ","Liczba","Plik","Sekcja"
:file: datasets/entities.csv
:widths: 30, 20, 10, 25, 15
```

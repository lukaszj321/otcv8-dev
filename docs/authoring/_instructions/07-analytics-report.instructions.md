
---
title: Analytics — metryki dokumentacji
owner: docs/authoring
inputs:
  - źródła: docs/**, src/**
outputs:
  - csv: docs/authoring/<chapter>/datasets/summary.csv
  - md: dopisek sekcji "Metryki" do index.md
render:
  - myst: {csv-table}, admonitions
rules:
  - policz: liczba plików .md/.mmd/.csv, liczba funkcji C++ (z Doxygen), liczba snippettów Lua
acceptance:
  - tabele widoczne, wartości > 0 dla aktywnych rozdziałów
---

## Sekcja do wstawienia
```md
## Metryki
```{{csv-table}} Metryki
:header: "Klucz","Wartość","Zakres"
:file: datasets/summary.csv
```
```

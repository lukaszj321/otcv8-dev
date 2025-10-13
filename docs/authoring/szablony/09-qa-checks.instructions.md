
---
title: QA — walidacje dokumentacji
owner: docs/authoring
inputs:
  - źródła: docs/authoring/**/*
outputs:
  - md: docs/authoring/qa/index.md
render:
  - myst: admonitions, tables
rules:
  - waliduj istnienie plików referencjonowanych w toctree/csv/mermaid click
  - raportuj brakujące pliki oraz puste katalogi
acceptance:
  - sekcja "Problemy" pusta (lub lista błędów)
---

## Sekcje raportu
- **Brakujące pliki**
- **Puste katalogi**
- **Zduplikowane kotwice**
- **Zewnętrzne linki** (niepożądane surowe URL do GitHuba)

---
name: "otmod"
applyTo:
  - "modules/**/*"
read:
  - "modules/**"
  - "mods/**"
  - "src/**"
  - "data/**"
write:
  - "docs/authoring/12_otmod/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"

outputs:
  - "docs/authoring/12_otmod/index.md"
  - "docs/authoring/12_otmod/datasets/otmod_packages.csv"
  - "docs/authoring/12_otmod/datasets/otmod_packages.ndjson"
  - "docs/authoring/12_otmod/diagrams/modules_deps.mmd"
---

# OTMOD — Instructions

## Goal
Zmapuj pakiety/moduły (OTMOD): manifesty, zależności, eksporty, powiązane zasoby i UI.

## Extraction
- Wykryj moduły po strukturze/manifestach (np. `*.otmod`, `manifest.json`, katalog modułu).
- Zbierz:
  - **dependencies** (nazwy/ścieżki modułów),
  - **exports** (Lua API, pliki `.lua` z `return {...}`/globalami),
  - **assets** (ścieżki z `data/**`),
  - **ui_roots** (pliki `.otui`/root layouty),
  - **entry_lua** (główne wejście modułu).
- Użyj heurystyk (grep w `*.lua`, `*.otui`, manifestach). Ścieżki względne względem repo.

## Datasets
- `docs/authoring/12_otmod/datasets/otmod_packages.csv` **lub** `.ndjson`
  - **CSV kolumny**:
    - `module` (string)
    - `path` (string)
    - `manifest` (string|null)
    - `dependencies` (JSON array)
    - `exports` (JSON array)
    - `assets` (JSON array)
    - `ui_roots` (JSON array)
    - `entry_lua` (string|null)
    - `notes` (string)
  - **NDJSON**: jeden obiekt/wiersz z tymi samymi kluczami.

## Diagrams (opcjonalnie)
- `docs/authoring/12_otmod/diagrams/modules_deps.mmd` — zależności modułów (flowchart).
- **Pierwsza linia wymagana**:

```

%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%

```
- Uwaga: `click` tylko w flowchart/graph (nie w `sequenceDiagram`).

## Crosslinks
- Dodaj xref do: `03_modules` (Lua), `11_data` (assets), `04_ui` (OTUI).

## Index
- `docs/authoring/12_otmod/index.md`:
- frontmatter, `{toctree}` (hidden), `{contents} :local:`
- `{csv-table}` z `otmod_packages.csv`
- `{mermaid}` z diagramem (jeśli wygenerowany)
- sekcja **Appendix / Facets** (jeśli używasz facetów)

## Acceptance
- [ ] Wygenerowano `index.md`
- [ ] Istnieje `otmod_packages.csv` **lub** `.ndjson` (kolumny/klucze jak wyżej)
- [ ] Listy w CSV są **JSON arrays** (np. `["a","b"]`)
- [ ] (Jeśli diagram) Mermaid renderuje się poprawnie (init w 1. linii, brak Unicode strzałek)
- [ ] Crosslinki do `03_modules`, `11_data`, `04_ui` istnieją

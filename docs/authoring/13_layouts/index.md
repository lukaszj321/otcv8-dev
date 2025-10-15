---
chapter: "13_layouts"
slug: "13_layouts"
title: "Layouts — overrides, motywy i warianty zasobów"
status: "agent_ready"
doc_id: "authoring.13_layouts"
language: "pl"
last_sync_iso: "2025-10-15T16:30:48.251568"
tags: ["otclient","layouts","themes","overrides","ui","assets","rag"]
artifacts:
  datasets:
    - id: "layout_index"
      file: "layout_index.csv"
      headers: ["layout", "description", "priority", "author", "notes"]
      facet: "13_layouts.layout_index"
    - id: "layout_overrides"
      file: "layout_overrides.csv"
      headers: ["layout", "kind", "source_path", "override_path", "status", "note"]
      facet: "13_layouts.layout_overrides"
    - id: "layout_images"
      file: "layout_images.csv"
      headers: ["layout", "image_path", "width", "height", "theme", "used_by"]
      facet: "13_layouts.layout_images"
  diagrams:
    - id: "layouts_overview"
      file: "layouts_overview.mmd"
      facet: "13_layouts.layouts_overview"
    - id: "override_resolution"
      file: "override_resolution.mmd"
      facet: "13_layouts.override_resolution"
xrefs:
  - to: "11_data.images"
    type: "overrides"
    evidence: "docs/authoring/13_layouts/datasets/layout_overrides.csv"
  - to: "04_ui.widgets_catalog"
    type: "renders"
    evidence: "docs/authoring/13_layouts/datasets/layout_images.csv"
---

# Layouts — overrides, motywy i warianty zasobów

**Cel rozdziału:** zdefiniować **reguły override** i strukturę katalogu `layouts/**`, aby agent mógł deterministycznie rozwiązać, które zasoby (obrazy, style, czcionki, dźwięki, shadery) są aktywne przy wybranym layoucie (np. `mobile`, `retro`).

```{contents}
:local:
:depth: 2
```

:::{admonition} TL;DR
:class: tip
`layouts/<N>/...` **nadpisuje** `data/...`. Jeśli istnieją oba pliki, wygrywa ten z *aktywnego* layoutu. Nazwa `default` jest zarezerwowana — **nie** używaj jej na layout.
:::

## Co to jest layout?

Layout to *warstwa tematyczna* nakładana na `data/**`. Umożliwia:
- zmianę palety kolorów i ikon (np. **mobile-first** większe ikony),
- alternatywne tła i ramki,
- pakiety zasobów dla eventów okolicznościowych (np. **retro**).

**Struktura** (przykład):

```
layouts/
  mobile/
    images/**      # nadpisane bitmapy i sprity
    styles/**      # alternatywne style OTUI
    shaders/**     # warianty shaderów (np. jaśniejsze)
    fonts/**       # opcjonalne, np. inne kerning/rozmiar
  retro/
    images/** 
    styles/**
```

## Kontrakt override (agent)

1. **Katalog bazowy:** `data/**` (źródło prawdy).
2. **Warstwa layout:** `layouts/<name>/**` (opcjonalna, *wyższy priorytet*).
3. **Rozwiązywanie ścieżki:**
   - OTUI: `image-source: /images/ui/tabbutton_square` → sprawdź
     - `layouts/<name>/images/ui/tabbutton_square.png`
     - w przeciwnym razie: `data/images/ui/tabbutton_square.png`
4. **Zasady konfliktów:**
   - jeśli pliki istnieją w obu miejscach, użyj layoutu;
   - jeśli asset jest folderem *sprite sheet*, sprawdź **zgodność rozmiarów** (`width×height`) i `image-clip`.
5. **QA:** każda pozycja w `layout_overrides.csv` musi mieć `status ∈ {applied,missing,format_mismatch}`.

## Datasets

### `layout_index.csv` — lista layoutów
| layout | description | priority | author | notes |
|---|---|---|---|---|

### `layout_overrides.csv` — konkretne nadpisania
| layout | kind | source_path | override_path | status | note |
|---|---|---|---|---|---|

**Przykład:**
```csv
layout,kind,source_path,override_path,status,note
mobile,image,data/images/ui/tabbutton_square.png,layouts/mobile/images/ui/tabbutton_square.png,applied,"większy przycisk pod dotyk"
retro,image,data/images/topbuttons/skills.png,layouts/retro/images/topbuttons/skills.png,applied,"wariant pixel-art"
mobile,style,data/styles/tabs.otui,layouts/mobile/styles/tabs.otui,applied,"większe marginesy"
```

### `layout_images.csv` — metadane obrazów
| layout | image_path | width | height | theme | used_by |
|---|---|---|---|---|---|

## Diagramy

### layouts_overview
*Facet:* [`13_layouts.layouts_overview`](#facet-13_layouts.layouts_overview)

```{mermaid}
%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%
graph TD
  A[data/**] --> B[images/**]
  A --> C[styles/**]
  A --> D[fonts/**]
  A --> E[sounds/**]
  A --> F[shaders/**]
  L[layouts/<name>/**] -->|override| B
  L -->|override| C
  L -->|override| D
  L -->|override| E
  L -->|override| F
  click B "./../11_data/index.html#facet-11_data.images" "Zobacz obrazy"
```

### override_resolution
*Facet:* [`13_layouts.override_resolution`](#facet-13_layouts.override_resolution)

```{mermaid}
%{init: { 'theme': 'neutral' } }%
sequenceDiagram
  participant UI as OTUI
  participant RES as Resolver
  participant DATA as data/**
  participant LAY as layouts/<name>/**
  UI->>RES: image-source=/images/ui/tabbutton_square
  RES->>LAY: exists(images/ui/tabbutton_square.png)?
  alt TAK
    RES-->>UI: use layouts/<name>/images/ui/tabbutton_square.png
  else NIE
    RES->>DATA: use data/images/ui/tabbutton_square.png
  end
```

## Checklista wdrożeniowa (layout authoring)

- [ ] Nazwy `kebab-case` (`mobile`, `retro`).
- [ ] Rozmiary sprite'ów kompatybilne z `image-clip` w OTUI.
- [ ] Paleta barw z kontrastem AA (WCAG) dla dark/light.
- [ ] Index rekordów w `layout_overrides.csv`.
- [ ] Podlinkowanie scen w `04_ui` i assetów w `11_data`.

## Integracja z `04_ui` i `11_data`

- W `ui_asset_usage.csv` (rozdz. 11) `resolved_path` pokazuje **realny** asset po uwzględnieniu layoutu.
- W `module_ui_links.csv` (rozdz. 12) można policzyć liczbę widgetów dotkniętych przez layout.

:::{note}
Layouty nie dodają funkcjonalności — **tylko** zmieniają zasoby i style. Funkcje i zdarzenia pochodzą z modułów (`03_modules`/`12_otmod`) i UI (`04_ui`).
:::

## Blueprints

Zobacz `blueprints/layout_blueprints.csv` — szablony minimalne i rozbudowane (`mobile`, `retro`).

## QA

- `diagram-lint`: każdy `.mmd` musi mieć **init header**.
- `dataset sanity`: każdy CSV posiada nagłówek, brak `NaN`.
- `idempotency`: drugi przebieg generatora nie wprowadza zmian.

## See also

- `11_data` — zasoby bazowe i mapowanie OTUI → asset
- `04_ui` — struktura widgetów i style OTUI
- `12_otmod` — moduły i lifecycle

## Appendix / Facets

(facet-13_layouts.layout_index)=
### Facet: `13_layouts.layout_index`
Type: dataset

(facet-13_layouts.layout_overrides)=
### Facet: `13_layouts.layout_overrides`
Type: dataset

(facet-13_layouts.layout_images)=
### Facet: `13_layouts.layout_images`
Type: dataset

(facet-13_layouts.layouts_overview)=
### Facet: `13_layouts.layouts_overview`
Type: diagram

(facet-13_layouts.override_resolution)=
### Facet: `13_layouts.override_resolution`
Type: diagram

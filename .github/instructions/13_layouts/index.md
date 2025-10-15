---
title: 13_layouts - Layouts — screens & topology
generated: 2025-10-15T09:04:30Z
---

# 13_layouts - Layouts — screens & topology

```{contents} Table of contents
:depth: 2
:local:
```

## Intro
Krótki opis celu rozdziału oraz sposobu generowania danych (skrypty w `docs/authoring/_tools`).

## Datasets
#### `layouts.csv`
*Facet:* [`13_layouts.layouts`](#facet-13_layouts.layouts)

```{csv-table} layouts
:header-rows: 1
:file: ./13_layouts/datasets/layouts.csv
:widths: auto
```
## Diagrams
#### `layouts_topology.mmd`
*Facet:* [`13_layouts.layouts_topology`](#facet-13_layouts.layouts_topology)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    Home[Home Screen] --> Inv[Inventory]
    Home --> Map
    Inv --> Inspect
    click Home "./index.html#facet-13_layouts.layouts" "Open layouts dataset"
```

## Crosslinks
- Crosslink do `04_ui` oraz `11_data`.

## Appendix / Facets
(facet-13_layouts.layouts)=
### Facet: `13_layouts.layouts`
(facet-13_layouts.layouts_topology)=
### Facet: `13_layouts.layouts_topology`

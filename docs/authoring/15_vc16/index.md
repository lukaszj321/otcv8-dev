---
title: 15_vc16 - MSVC (vc16) solution — projects & defines
generated: 2025-10-15T09:04:30Z
---

# 15_vc16 - MSVC (vc16) solution — projects & defines

```{contents} Table of contents
:depth: 2
:local:
```

## Intro
Krótki opis celu rozdziału oraz sposobu generowania danych (skrypty w `docs/authoring/_tools`).

## Datasets
#### `projects.csv`
*Facet:* [`15_vc16.projects`](#facet-15_vc16.projects)

```{csv-table} projects
:header-rows: 1
:file: ./15_vc16/datasets/projects.csv
:widths: auto
```
#### `defines.csv`
*Facet:* [`15_vc16.defines`](#facet-15_vc16.defines)

```{csv-table} defines
:header-rows: 1
:file: ./15_vc16/datasets/defines.csv
:widths: auto
```
## Diagrams
#### `solution_graph.mmd`
*Facet:* [`15_vc16.solution_graph`](#facet-15_vc16.solution_graph)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    Sln[Solution] --> Core[Core]
    Sln --> Client[Client]
    click Core "./index.html#facet-15_vc16.projects" "Open projects dataset"
```

## Crosslinks
- Crosslink do `01_core` i `14_android`.

## Appendix / Facets
(facet-15_vc16.projects)=
### Facet: `15_vc16.projects`
(facet-15_vc16.defines)=
### Facet: `15_vc16.defines`
(facet-15_vc16.solution_graph)=
### Facet: `15_vc16.solution_graph`

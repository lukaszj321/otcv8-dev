
---
title: OTMOD — Modules (12)
doc_id: "authoring.12_otmod.index"
---

# OTMOD — Modules, Hooks, Dependencies, UI

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

::: {grid} 1 1 2 2
:gutter: 2

::: {grid-item}
#### `modules_index.csv`
*Facet:* [`12_otmod.modules_index`](#facet-12_otmod.modules_index)

```{csv-table} modules_index
:header-rows: 1
:file: ./datasets/modules_index.csv
:widths: auto
```
:::

::: {grid-item}
#### `module_scripts.csv`
*Facet:* [`12_otmod.module_scripts`](#facet-12_otmod.module_scripts)

```{csv-table} module_scripts
:header-rows: 1
:file: ./datasets/module_scripts.csv
:widths: auto
```
:::

::: {grid-item}
#### `module_deps.csv`
*Facet:* [`12_otmod.module_deps`](#facet-12_otmod.module_deps)

```{csv-table} module_deps
:header-rows: 1
:file: ./datasets/module_deps.csv
:widths: auto
```
:::

::: {grid-item}
#### `module_hooks.csv`
*Facet:* [`12_otmod.module_hooks`](#facet-12_otmod.module_hooks)

```{csv-table} module_hooks
:header-rows: 1
:file: ./datasets/module_hooks.csv
:widths: auto
```
:::

::: {grid-item}
#### `module_ui_links.csv`
*Facet:* [`12_otmod.module_ui_links`](#facet-12_otmod.module_ui_links)

```{csv-table} module_ui_links
:header-rows: 1
:file: ./datasets/module_ui_links.csv
:widths: auto
```
:::
:::

## Diagrams

#### `lifecycle.mmd`
*Facet:* [`12_otmod.lifecycle`](#facet-12_otmod.lifecycle)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
sequenceDiagram
  participant Loader
  participant Module as game_interface
  participant UI as OTUI
  Loader->>Module: @onLoad → init()
  Module->>UI: load skills.otui
  Module-->>Loader: ready
```

#### `deps_graph.mmd`
*Facet:* [`12_otmod.deps_graph`](#facet-12_otmod.deps_graph)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph TD
  A[game_interface] --> B[game_skills]
  A --> C[game_hotkeys]
  B --> D[game_stats]
```

## Appendix / Facets

(facet-12_otmod.modules_index)=
### Facet: `12_otmod.modules_index`
Type: dataset

(facet-12_otmod.module_scripts)=
### Facet: `12_otmod.module_scripts`
Type: dataset

(facet-12_otmod.module_deps)=
### Facet: `12_otmod.module_deps`
Type: dataset

(facet-12_otmod.module_hooks)=
### Facet: `12_otmod.module_hooks`
Type: dataset

(facet-12_otmod.module_ui_links)=
### Facet: `12_otmod.module_ui_links`
Type: dataset

(facet-12_otmod.lifecycle)=
### Facet: `12_otmod.lifecycle`
Type: diagram

(facet-12_otmod.deps_graph)=
### Facet: `12_otmod.deps_graph`
Type: diagram

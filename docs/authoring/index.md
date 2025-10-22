---
title: Authoring (Chapters)
---

# Authoring (Chapters)

```{toctree}
:hidden:
:maxdepth: 2
01_core/index
01_runtime/index
02_events/index
03_modules/index
04_ui/index
05_events/index
05_network/index
06_assets/index
07_settings_crypto/index
08_audio/index
09_logging/index
10_game_runtime/index
11_data/index
12_otmod/index
13_layouts/index
14_android/index
15_vc16/index
analytics/summary
qa/summary
```

:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} 01 — Core
:link: 01_core/index
Podstawy klienta, framework, C++ i API.
:::

:::{grid-item-card} 02 — Events
:link: 02_events/index
System zdarzeń, strumienie, emitery.
:::

:::{grid-item-card} 04 — UI (OTUI)
:link: 04_ui/index
Widżety, layouty, presety i style.
:::

:::{grid-item-card} 11 — Data
:link: 11_data/index
Assets, images, fonts, sounds, shaders.
:::

:::{grid-item-card} 12 — OTMOD
:link: 12_otmod/index
Moduły, pakiety, zależności.
:::

:::{grid-item-card} 13 — Layouts
:link: 13_layouts/index
Layouty, overrides, sprite grids.
:::
:::

````{tabs}
```{tab} Guide
Struktura Authoring: każdy rozdział ma `datasets/` (CSV), `diagrams/` (Mermaid/Graphviz) i `examples/` z kodem.
```

```{tab} Reference
Indeksy rozdziałów (patrz TOC). Krótkie opisy i odnośniki do API/typów, jeśli dotyczy.
```

```{tab} Examples
**CSV**
```{csv-table} Presety UI — przykład
:header-rows: 1
:file: 04_ui/datasets/ui_widgets.csv
:widths: 20, 20, 20, 20, 20
```

**Mermaid**
```{mermaid}
flowchart LR
  A[Authoring]-->B[Datasets]
  A-->C[Diagrams]
  A-->D[Code Examples]
```

**Graphviz**
```{graphviz}
digraph G { 
  Authoring -> Datasets;
  Authoring -> Diagrams;
  Authoring -> Code;
}
```
```
````

:::{card}
**Quality gates**
{badge}`lint ok,success` {badge}`examples ✓,info` {badge}`dark-mode todo,warning`
:::

```{dropdown} Quick tasks (Authoring)
- [ ] `csv-table` renderuje nagłówki z datasets/
- [ ] Mermaid/Graphviz w dark‑mode OK
- [ ] „See also" prowadzi do UI/Events/Templates
```

:::{grid} 1 1 2 3
:class-row: gap-2

**See also:** {ref}`04_ui/index` · {ref}`02_events/index` · {ref}`11_data/index`
:::

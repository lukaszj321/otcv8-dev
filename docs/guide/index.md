---
title: Guide & Components
---

# Guide & Components

Praktyczne elementy PyData + sphinx‑design stosowane w projekcie.

```{toctree}
:maxdepth: 2
:hidden:
kitchen/admonitions
kitchen/blocks
kitchen/tables
kitchen/lists
kitchen/generic
kitchen/components
kitchen/indices
```

## Kitchen‑sink in practice

Admonitions, grids, cards, tabs, dropdowns – z linkami do realnych użyć.

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Admonitions
:link: kitchen/admonitions
Notatki, ostrzeżenia, tips.
:::

:::{grid-item-card} Komponenty
:link: kitchen/components
Grids, cards, tabs, badges.
:::

:::{grid-item-card} Tabele
:link: kitchen/tables
CSV-table i inne.
:::

:::{grid-item-card} Indeksy
:link: kitchen/indices
Generowanie indeksów.
:::
:::

## Graphviz + Mermaid

```{mermaid}
sequenceDiagram
  participant App
  participant Core
  App->>Core: init()
  Core-->>App: ready
```

```{graphviz}
digraph G { 
  A -> B;
  B -> C;
}
```

## CSV‑table (datasets)

```{csv-table} Przykład tabeli
:header-rows: 1
:file: ../authoring/04_ui/datasets/ui_widgets.csv
:widths: 20, 20, 20, 20, 20
```

## Tabs: Guide / Reference / Examples

````{tabs}
```{tab} Guide
Best practices + checklisty.
```
```{tab} Reference
Linki do indeksów i API.
```
```{tab} Examples
`literalinclude` z regionami, krótkie snippety.
```
````

## Sidebar & buttons

Prawy TOC + „Show source" + „Edit this page" włączone globalnie.

```{dropdown} Quick tasks (Guide)
- [ ] Dark‑mode przykładów OK
- [ ] `copybutton` na blokach kodu działa
- [ ] „See also" spójny z Authoring/Copilot Docs
```

:::{grid} 1 1 2 3
**See also:** {ref}`authoring/index` · {ref}`dokumentacja copilot/sphinx/index` · {ref}`04_ui/index`
:::
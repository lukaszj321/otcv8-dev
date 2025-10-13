---
title: 02_events — Events
---

# 02_events — Events

> Źródła: `docs/reposzablony/02_events/`

:::{admonition} Co jest na tej stronie?
:class: tip
- **Datasets** — CSV z `datasets/` osadzone jako tabele
- **Diagrams** — Mermaid z `diagrams/` + podgląd kodu w dropdown
:::

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

```{admonition} entities.csv (CSV)
:class: dropdown
Lokalizacja: `../../reposzablony/02_events/datasets/entities.csv`
```

```{csv-table} entities
:header-rows: 1
:file: ../../reposzablony/02_events/datasets/entities.csv
:widths: 50,50
```

:::

:::{grid-item}

```{admonition} summary.csv (CSV)
:class: dropdown
Lokalizacja: `../../reposzablony/02_events/datasets/summary.csv`
```

```{csv-table} summary
:header-rows: 1
:file: ../../reposzablony/02_events/datasets/summary.csv
:widths: 50,50
```

:::

:::

## Diagrams
```{admonition} architecture.mmd (Mermaid)
:class: tip
Lokalizacja: `../../reposzablony/02_events/diagrams/architecture.mmd`
```

````{mermaid}
:caption: architecture
```{include} ../../reposzablony/02_events/diagrams/architecture.mmd
```
````

```{admonition} Kod źródłowy (architecture.mmd)
:class: dropdown
```{literalinclude} ../../reposzablony/02_events/diagrams/architecture.mmd
:language: mermaid
```

```{admonition} flow.mmd (Mermaid)
:class: tip
Lokalizacja: `../../reposzablony/02_events/diagrams/flow.mmd`
```

````{mermaid}
:caption: flow
```{include} ../../reposzablony/02_events/diagrams/flow.mmd
```
````

```{admonition} Kod źródłowy (flow.mmd)
:class: dropdown
```{literalinclude} ../../reposzablony/02_events/diagrams/flow.mmd
:language: mermaid
```

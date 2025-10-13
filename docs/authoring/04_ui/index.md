
---
title: 04 UI
---

# 04 UI

Krótki opis rozdziału – skąd pochodzą dane, co przedstawiają wykresy i jak interpretować metryki.

## Datasets

```{csv-table} Summary
:header: "Metric","Value"
:file: datasets/summary.csv
:widths: 40,60
```

```{csv-table} Entities
:header: "Entity","Count"
:file: datasets/entities.csv
:widths: 50,50
```

## Diagrams

```{dropdown} Flow Diagram
:icon: flow
```{mermaid}
flowchart TD
A[Start: 04 UI] --> B[Process data]
B --> C[Generate CSV]
B --> D[Render Diagrams]
C --> E[Page build]
D --> E
click B "../04_ui/index.html" "Open 04 UI"
click E "../index.html" "Back to Authoring"
```
```

```{dropdown} Architecture Diagram
:icon: blueprint
```{mermaid}
graph TD
subgraph Ingestion
    S1[Sources] --> S2[Collectors]
end
subgraph Processing
    S2 --> P1[Parser]
    P1 --> P2[Validator]
    P2 --> P3[Exporter]
end
subgraph Output
    P3 --> O1[CSV datasets]
    P3 --> O2[Mermaid diagrams]
    O1 --> O3[Authoring Page]
    O2 --> O3
end
```
```

## Zawartość rozdziału

```{toctree}
:maxdepth: 1
:titlesonly:

```

## Zobacz też

- {doc}/modules/index
- {doc}/ui/index

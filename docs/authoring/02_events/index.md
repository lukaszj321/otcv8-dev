# Event System Documentation

Event system, signals, and event flow documentation

## Summary

```{csv-table} Chapter Summary
:file: ../../_data/02_events/summary.csv
:header-rows: 1
:widths: 30, 30, 40
```

## Entities

```{csv-table} Entity Information
:file: ../../_data/02_events/entities.csv
:header-rows: 1
:widths: 40, 20, 40
```

## Architecture

The following diagram shows the overall architecture and component relationships:

```{mermaid}
:caption: Architecture Diagram

graph LR
    subgraph Events
        E0[Event Types]
        E1[Signal Handlers]
        E2[Event Sequences]
        E0 --> E1
        E1 --> E2
    end
```

## Data Flow

```{mermaid}
:caption: Data Flow Diagram

    A[Events] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```

## Source Files

The raw data files for this chapter are available in the repository:

- [Datasets](https://github.com/lukaszj321/otcv8-dev/tree/master/docs/reposzablony/02_events/datasets)
- [Diagrams](https://github.com/lukaszj321/otcv8-dev/tree/master/docs/reposzablony/02_events/diagrams)
- [Chapter Index](https://github.com/lukaszj321/otcv8-dev/blob/master/docs/reposzablony/02_events/index.md)

## Navigation

::{note}
Return to [Authoring Index](../index.md) for other chapters.
::

---

*Generated from source data in `docs/reposzablony/02_events/`*

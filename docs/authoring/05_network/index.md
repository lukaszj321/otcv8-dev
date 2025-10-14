---
title: Network protocol — export kit
---

# Network protocol — export kit

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

### flows
*Facet:* [`05_network.flows`](#facet-05_network.flows)

```{csv-table} flows
:header-rows: 1
:file: ./datasets/flows.csv
:widths: auto
```

### network_messages
*Facet:* [`05_network.network_messages`](#facet-05_network.network_messages)

```{csv-table} network_messages
:header-rows: 1
:file: ./datasets/network_messages.csv
:widths: auto
```

### opcodes
*Facet:* [`05_network.opcodes`](#facet-05_network.opcodes)

```{csv-table} opcodes
:header-rows: 1
:file: ./datasets/opcodes.csv
:widths: auto
```

### summary
*Facet:* [`05_network.summary`](#facet-05_network.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams

### handshake
*Facet:* [`05_network.handshake`](#facet-05_network.handshake)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[05_network.handshake] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-05_network.handshake" "Open handshake"
```

## Cross-References

- **influences** → `10_game_runtime.game_state` (evidence: `docs/authoring/10_game_runtime/datasets/game_state.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-05_network.flows)=
### Facet: `05_network.flows`
Type: dataset

(facet-05_network.handshake)=
### Facet: `05_network.handshake`
Type: diagram

(facet-05_network.network_messages)=
### Facet: `05_network.network_messages`
Type: dataset

(facet-05_network.opcodes)=
### Facet: `05_network.opcodes`
Type: dataset

(facet-05_network.summary)=
### Facet: `05_network.summary`
Type: dataset

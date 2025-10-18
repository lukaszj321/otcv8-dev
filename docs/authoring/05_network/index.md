---
title: 05_network - Network
---

# 05_network - Network

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### entities
*Facet:* [`05_network.entities`](#facet-05_network.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### extended_opcodes
*Facet:* [`05_network.extended_opcodes`](#facet-05_network.extended_opcodes)

```{csv-table} extended_opcodes
:header-rows: 1
:file: ./datasets/extended_opcodes.csv
:widths: auto
```

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
### architecture
*Facet:* [`05_network.architecture`](#facet-05_network.architecture)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Network
        E0[Network Messages]
        E1[Protocol Handlers]
        E2[Network Stats]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-05_network.architecture" "Open architecture"
```

### flow
*Facet:* [`05_network.flow`](#facet-05_network.flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Network] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-05_network.flow" "Open flow"
```

### handshake
*Facet:* [`05_network.handshake`](#facet-05_network.handshake)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[05_network.handshake] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-05_network.handshake" "Open handshake"
click Handshake "./index.html#facet-05_network.handshake" "Open handshake"
```

### network_sequence
*Facet:* [`05_network.network_sequence`](#facet-05_network.network_sequence)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  NetworkEquence[05_network:network_sequence] --> Data[Datasets]
  Data --> Page[Index]

click NetworkEquence "./index.html#facet-05_network.network_sequence" "Open network_sequence"
click NetworkSequence "./index.html#facet-05_network.network_sequence" "Open network_sequence"
```

### overview
*Facet:* [`05_network.overview`](#facet-05_network.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Network Protocol] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-05_network.overview" "Open overview"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
```

## Crosslinks

- **influences** → `10_game_runtime.game_state` (evidence: `docs/authoring/10_game_runtime/datasets/game_state.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-05_network.architecture)=
### Facet: `05_network.architecture`
Type: diagram

(facet-05_network.entities)=
### Facet: `05_network.entities`
Type: dataset

(facet-05_network.extended_opcodes)=
### Facet: `05_network.extended_opcodes`
Type: dataset

(facet-05_network.flow)=
### Facet: `05_network.flow`
Type: diagram

(facet-05_network.flows)=
### Facet: `05_network.flows`
Type: dataset

(facet-05_network.handshake)=
### Facet: `05_network.handshake`
Type: diagram

(facet-05_network.network_messages)=
### Facet: `05_network.network_messages`
Type: dataset

(facet-05_network.network_sequence)=
### Facet: `05_network.network_sequence`
Type: diagram

(facet-05_network.opcodes)=
### Facet: `05_network.opcodes`
Type: dataset

(facet-05_network.overview)=
### Facet: `05_network.overview`
Type: diagram

(facet-05_network.summary)=
### Facet: `05_network.summary`
Type: dataset


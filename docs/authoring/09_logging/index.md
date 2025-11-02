---
title: 09_logging - Logging
---

# 09_logging - Logging

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### emitters
*Facet:* [`09_logging.emitters`](#facet-09_logging.emitters)

```{csv-table} emitters
:header-rows: 1
:file: ./datasets/emitters.csv
:widths: auto
```

### entities
*Facet:* [`09_logging.entities`](#facet-09_logging.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### log_config
*Facet:* [`09_logging.log_config`](#facet-09_logging.log_config)

```{csv-table} log_config
:header-rows: 1
:file: ./datasets/log_config.csv
:widths: auto
```

### log_events
*Facet:* [`09_logging.log_events`](#facet-09_logging.log_events)

```{csv-table} log_events
:header-rows: 1
:file: ./datasets/log_events.csv
:widths: auto
```

### log_examples
*Facet:* [`09_logging.log_examples`](#facet-09_logging.log_examples)

```{csv-table} log_examples
:header-rows: 1
:file: ./datasets/log_examples.csv
:widths: auto
```

### log_levels
*Facet:* [`09_logging.log_levels`](#facet-09_logging.log_levels)

```{csv-table} log_levels
:header-rows: 1
:file: ./datasets/log_levels.csv
:widths: auto
```

### logging_categories
*Facet:* [`09_logging.logging_categories`](#facet-09_logging.logging_categories)

```{csv-table} logging_categories
:header-rows: 1
:file: ./datasets/logging_categories.csv
:widths: auto
```

### sinks
*Facet:* [`09_logging.sinks`](#facet-09_logging.sinks)

```{csv-table} sinks
:header-rows: 1
:file: ./datasets/sinks.csv
:widths: auto
```

### summary
*Facet:* [`09_logging.summary`](#facet-09_logging.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`09_logging.architecture`](#facet-09_logging.architecture)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Logging
        E0[Log Entries]
        E1[Log Levels]
        E2[Log Sources]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-09_logging.architecture" "Open architecture"
```

### flow
*Facet:* [`09_logging.flow`](#facet-09_logging.flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Logging] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-09_logging.flow" "Open flow"
```

### logging_architecture
*Facet:* [`09_logging.logging_architecture`](#facet-09_logging.logging_architecture)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    App[Application Code] -->|log call| Logger[Logger g_logger]
    
    Logger --> Console[Console Sink stdout]
    Logger --> File[File Sink log.txt]
    Logger --> Callback[Callback Sink Custom Handler]
    Logger --> History[Memory History 1000 msgs]
    
    subgraph "Log Levels"
        L0[0-Debug]
        L1[1-Info]
        L2[2-Warning]
        L3[3-Error]
        L4[4-Fatal]
    end
    
    Logger --> L0
    Logger --> L1
    Logger --> L2
    Logger --> L3
    Logger --> L4
    
    Callback -->|UI Display| UI[Console Widget]
    History -->|getLastLog| Crash[Crash Reporter]
    
    click Logger "../index.html#facet-09_logging.architecture" "Logging Architecture"
    click Console "../index.html#facet-09_logging.sinks" "Log Sinks"
click LoggingArchitecture "./index.html#facet-09_logging.logging_architecture" "Open logging_architecture"
```

### logging_flow
*Facet:* [`09_logging.logging_flow`](#facet-09_logging.logging_flow)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
sequenceDiagram
    autonumber
    participant App as Application
    participant Log as g_logger
    participant File as Log File
    participant CB as Callback
    participant Hist as History Buffer

    App->>Log: setLogFile("log.txt")
    Log->>File: Open file stream

    App->>Log: setOnLog(callback)
    Log->>CB: Register callback

    App->>Log: info("Starting application")
    Log->>File: Write to file
    Log->>CB: Invoke callback
    Log->>Hist: Store in buffer (1/1000)

    App->>Log: error("Network failure")
    Log->>File: Write to file
    Log->>CB: Invoke callback
    Log->>Hist: Store in buffer (2/1000)

    App->>Log: getLastLog()
    Log-->>App: Return last message

    Note over Log: [[../index.html#facet-09_logging.flow|Logging Flow]]
    %% click LoggingFlow "./index.html#facet-09_logging.logging_flow" "Open logging_flow" %% REMOVED: click not supported in sequenceDiagram
```

### overview
*Facet:* [`09_logging.overview`](#facet-09_logging.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Logging System] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-09_logging.overview" "Open overview"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
```

## Crosslinks

- **observes** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **observes** → `05_network.network_messages` (evidence: `docs/authoring/05_network/datasets/network_messages.csv`)

## Appendix / Facets

(facet-09_logging.architecture)=
### Facet: `09_logging.architecture`
Type: diagram

(facet-09_logging.emitters)=
### Facet: `09_logging.emitters`
Type: dataset

(facet-09_logging.entities)=
### Facet: `09_logging.entities`
Type: dataset

(facet-09_logging.flow)=
### Facet: `09_logging.flow`
Type: diagram

(facet-09_logging.log_config)=
### Facet: `09_logging.log_config`
Type: dataset

(facet-09_logging.log_events)=
### Facet: `09_logging.log_events`
Type: dataset

(facet-09_logging.log_examples)=
### Facet: `09_logging.log_examples`
Type: dataset

(facet-09_logging.log_levels)=
### Facet: `09_logging.log_levels`
Type: dataset

(facet-09_logging.logging_architecture)=
### Facet: `09_logging.logging_architecture`
Type: diagram

(facet-09_logging.logging_categories)=
### Facet: `09_logging.logging_categories`
Type: dataset

(facet-09_logging.logging_flow)=
### Facet: `09_logging.logging_flow`
Type: diagram

(facet-09_logging.overview)=
### Facet: `09_logging.overview`
Type: diagram

(facet-09_logging.sinks)=
### Facet: `09_logging.sinks`
Type: dataset

(facet-09_logging.summary)=
### Facet: `09_logging.summary`
Type: dataset


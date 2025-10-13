# Authoring Documentation

This section contains auto-generated documentation artifacts including datasets, diagrams, and analysis for all major components of OTClientV8.

## Overview

The authoring documentation provides:
- **Datasets**: CSV and JSON data exports for analysis and RAG systems
- **Diagrams**: Visual representations of architecture and data flows
- **Statistics**: Aggregated metrics and summaries
- **Analysis**: Insights and correlations across components

## Chapters

:::{grid} 3
:gutter: 2

:::{grid-item-card} 01. Core API
:link: 01_core/index
:link-type: doc

Core C++ API documentation and class hierarchies
:::

:::{grid-item-card} 01. Runtime
:link: 01_runtime/index
:link-type: doc

Runtime statistics and monitoring data
:::

:::{grid-item-card} 02. Events
:link: 02_events/index
:link-type: doc

Event system, signals, and event flow
:::

:::{grid-item-card} 03. Lua Modules
:link: 03_modules/index
:link-type: doc

Lua module exports and functions
:::

:::{grid-item-card} 04. UI (OTUI)
:link: 04_ui/index
:link-type: doc

OTUI widget hierarchy and components
:::

:::{grid-item-card} 05. Event Details
:link: 05_events/index
:link-type: doc

Detailed event documentation
:::

:::{grid-item-card} 05. Network
:link: 05_network/index
:link-type: doc

Network protocol and messages
:::

:::{grid-item-card} 06. Assets
:link: 06_assets/index
:link-type: doc

Asset management and resources
:::

:::{grid-item-card} 07. Settings & Crypto
:link: 07_settings_crypto/index
:link-type: doc

Configuration and cryptography
:::

:::{grid-item-card} 08. Audio
:link: 08_audio/index
:link-type: doc

Audio system and sound channels
:::

:::{grid-item-card} 09. Logging
:link: 09_logging/index
:link-type: doc

Logging system and log analysis
:::

:::{grid-item-card} 10. Game Runtime
:link: 10_game_runtime/index
:link-type: doc

Game runtime state and metrics
:::

:::

## Navigation

```{toctree}
:maxdepth: 1
:hidden:

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
```

## How to Use

1. **Browse by chapter**: Select a chapter from the grid above
2. **Review datasets**: Each chapter includes CSV files with structured data
3. **Explore diagrams**: Visual representations help understand architecture
4. **Check statistics**: Summary tables provide quick insights

## Source Files

The source data for this documentation is located in:
- `docs/reposzablony/<chapter>/datasets/` - Raw CSV and JSON data
- `docs/reposzablony/<chapter>/diagrams/` - Mermaid diagram definitions
- `docs/_data/<chapter>/` - Sphinx-optimized data files

## Generated Content

:::{note}
All content in this section is auto-generated from source code and configuration files.
Last updated: {sub-ref}`today`
:::

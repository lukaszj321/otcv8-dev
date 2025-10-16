---
title: Authoring Documentation
---

# OTClient v8 - Comprehensive Documentation (Chapters 01-15)

Complete authoring documentation for OTClient v8, covering all major systems from Core C++ API to platform-specific implementations.

## Overview

This documentation provides comprehensive coverage of:
- **Core Systems** (01-02): C++ API, Runtime, Events
- **Modules & UI** (03-04): Lua Modules, OTUI Widgets
- **Infrastructure** (05-10): Network, Assets, Settings, Audio, Logging, Game Runtime
- **Resources** (11-13): Data Assets, OTMOD Modules, Layouts
- **Platform** (14-15): Android, VC16/ANGLE

**Total Documentation:** 2.28 MB across 15 chapters
**Datasets:** 85 CSV files with structured data
**Diagrams:** 129 Mermaid visualizations
**Blueprints:** 15 reusable templates

## Chapters

:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} 01. Core C++ API
:link: 01_core/index
:link-type: doc
:shadow: md
Core framework, classes, and C++ architecture. Comprehensive API documentation with 1+ MB of content.
:::

:::{grid-item-card} 02. Runtime System
:link: 01_runtime/index
:link-type: doc
:shadow: md
Application lifecycle, scheduler, dispatcher, threads, and event queues.
:::

:::{grid-item-card} 03. Events System
:link: 02_events/index
:link-type: doc
:shadow: md
C++/Lua event system, emitter/handler matrix, event bus architecture.
:::

:::{grid-item-card} 04. Lua Modules
:link: 03_modules/index
:link-type: doc
:shadow: md
Lua module system, C++ bindings, exports, and integration patterns.
:::

:::{grid-item-card} 05. UI & OTUI
:link: 04_ui/index
:link-type: doc
:shadow: md
OTUI widget hierarchy, styles, and user interface system.
:::

:::{grid-item-card} 06. Network Protocol
:link: 05_network/index
:link-type: doc
:shadow: md
Network stack, protocol handling, encryption, and TFS integration.
:::

:::{grid-item-card} 07. Assets Pipeline
:link: 06_assets/index
:link-type: doc
:shadow: md
Asset processing, atlas generation, compression, and optimization.
:::

:::{grid-item-card} 08. Settings & Crypto
:link: 07_settings_crypto/index
:link-type: doc
:shadow: md
Configuration management, encryption, and security systems.
:::

:::{grid-item-card} 09. Audio System
:link: 08_audio/index
:link-type: doc
:shadow: md
Sound channels, audio loading, playback, and effects.
:::

:::{grid-item-card} 10. Logging System
:link: 09_logging/index
:link-type: doc
:shadow: md
Logging levels, targets, categories, and integration.
:::

:::{grid-item-card} 11. Game Runtime
:link: 10_game_runtime/index
:link-type: doc
:shadow: md
Game loop, input handling, map system, and gameplay runtime.
:::

:::{grid-item-card} 12. Data Assets
:link: 11_data/index
:link-type: doc
:shadow: md
Complete catalog of images, fonts, sounds, styles, locales, and shaders.
:::

:::{grid-item-card} 13. OTMOD System
:link: 12_otmod/index
:link-type: doc
:shadow: md
Module packaging, structure, hooks, dependencies, and load system.
:::

:::{grid-item-card} 14. Layouts
:link: 13_layouts/index
:link-type: doc
:shadow: md
Layout system for asset overrides and theme variants.
:::

:::{grid-item-card} 15. Android Platform
:link: 14_android/index
:link-type: doc
:shadow: md
Android assets, ABI support, packaging, and platform integration.
:::

:::{grid-item-card} 16. VC16/ANGLE
:link: 15_vc16/index
:link-type: doc
:shadow: md
Visual C++ 2019, ANGLE integration, EGL/GLES, and Windows build.
:::

:::

```{toctree}
:caption: Core Systems
:maxdepth: 2
:titlesonly:

01_core/index
01_runtime/index
02_events/index
```

```{toctree}
:caption: Modules & UI
:maxdepth: 2
:titlesonly:

03_modules/index
04_ui/index
```

```{toctree}
:caption: Infrastructure
:maxdepth: 2
:titlesonly:

05_network/index
06_assets/index
07_settings_crypto/index
08_audio/index
09_logging/index
10_game_runtime/index
```

```{toctree}
:caption: Resources & Platform
:maxdepth: 2
:titlesonly:

11_data/index
12_otmod/index
13_layouts/index
14_android/index
15_vc16/index
```

```{toctree}
:caption: Reports & Analytics
:maxdepth: 2

analytics/execution_report
analytics/gaps
qa/qa_summary
relations/matrix
```

## Quick Links

- [Execution Report](analytics/execution_report.md) - Full rebuild statistics
- [Gaps Analysis](analytics/gaps.md) - Identified gaps and recommendations
- [QA Summary](qa/qa_summary.md) - Quality assurance results
- [Relations Matrix](relations/matrix.md) - Cross-chapter relationships
- [Download ZIP Artifact](artifacts/authoring_full_rebuild.zip) - Complete documentation package (2.2 MB)

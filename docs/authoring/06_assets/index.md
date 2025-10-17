---
doc_id: "06_assets"
source_path: "docs/authoring/06_assets/index.md"
source_sha: "latest"
last_sync_iso: "2025-10-17T23:29:18Z"
doc_class: "guide"
language: "pl"
title: "Assets Pipeline"
summary: "Asset processing and optimization"
tags: ["assets", "otclient", "docs"]
---

# Assets Pipeline

## Overview

Asset processing and optimization

This chapter provides comprehensive documentation for the Assets Pipeline subsystem of OTClient v8.

## Architecture

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Assets Pipeline] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
```

## Datasets

```{csv-table} Summary
:file: ./datasets/summary.csv
:header-rows: 1
:widths: auto
```

## Key Features

- Comprehensive documentation
- Dataset exports
- Architecture diagrams
- Code examples

## Related Chapters

- [Core C++ API](../01_core/index.md)
- [Runtime System](../01_runtime/index.md)
- [Events System](../02_events/index.md)


## Appendix / Facets

(facet-06_assets.overview)=
### Facet: `06_assets.overview`

Overview diagram and summary for Assets Pipeline.

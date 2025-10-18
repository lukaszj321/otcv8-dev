---
doc_id: "11_data"
source_path: "docs/authoring/11_data/index.md"
source_sha: "latest"
last_sync_iso: "2025-10-17T23:29:18Z"
doc_class: "guide"
language: "pl"
title: "Data Assets"
summary: "Data directory assets catalog"
tags: ["data", "otclient", "docs"]
---

# Data Assets

## Overview

Data directory assets catalog

This chapter provides comprehensive documentation for the Data Assets subsystem of OTClient v8.

## Architecture

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Data Assets] --> B[Components]
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

(facet-11_data.overview)=
### Facet: `11_data.overview`

Overview diagram and summary for Data Assets.

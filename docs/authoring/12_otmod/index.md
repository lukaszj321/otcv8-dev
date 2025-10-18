---
doc_id: 12_otmod
source_path: docs/authoring/12_otmod
source_sha: adcc8b9
last_sync_iso: "2025-10-18T01:36:41.412944Z"
doc_class: spec
language: pl
title: 12 - OTMOD
---


# 12 - OTMOD

Module structure, hooks, dependencies, load-later, sandbox, and blueprints.

## Przegląd

Ten rozdział dokumentuje 12 otmod w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

README
load_later_patterns
sandbox_security
blueprints/index
datasets/index
diagrams/index
```

## Key Topics

### Load-Later Mechanism

The **load-later** pattern allows modules to defer initialization until dependencies are ready. See [Load-Later Patterns](./load_later_patterns.md) for detailed examples and best practices.

### Sandbox Security

OTClient v8 implements sandboxed Lua environments for user modules. See [Sandbox Security](./sandbox_security.md) for security patterns and guidelines.

### Module Lifecycle

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph LR
    A[Parse Manifest] --> B[Check Dependencies]
    B --> C{Load-Later?}
    C -->|No| D[Create Sandbox]
    C -->|Yes| E[Defer to Phase 3]
    D --> F[Call init]
    E --> G[Wait for Dependencies]
    G --> D
    F --> H[Module Ready]
    
    style C fill:#6a4,stroke:#8c6
    style D fill:#46a,stroke:#68c
```

See [Module Lifecycle Diagram](./diagrams/module_lifecycle.mmd) for detailed sequence.

## Datasets

- `lua_exports.csv`
- `module_deps.csv`
- `module_hooks.csv`

## Diagramy

```{contents}
:local:
:depth: 2
```

## Crosslinks

- [Modules (Lua API)](../03_modules/index.md) - Lua scripting and API reference
- [Data Assets](../11_data/index.md) - Asset loading and management
- [UI System](../04_ui/index.md) - OTUI widget system
- [Core C++ API](../01_core/index.md) - C++ core functionality and bindings
- [Events System](../02_events/index.md) - Event handling and hooks


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.412944Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [x] Diagrams added (module_lifecycle.mmd)
- [x] Crosslinks verified (5 links)
- [x] Content complete (load-later + sandbox docs added)

## Appendix / Facets

(facet-12_otmod.main)=
### Facet: `12_otmod.main`

Main documentation facet for 12_otmod.

(facet-12_otmod.load_later)=
### Facet: `12_otmod.load_later`

Load-later patterns and dependency management.

(facet-12_otmod.sandbox)=
### Facet: `12_otmod.sandbox`

Sandbox security and permission model.
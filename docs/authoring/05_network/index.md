---
doc_id: 05_network
source_path: docs/authoring/05_network
source_sha: 0659034
last_sync_iso: "2025-10-18T01:36:41.411532Z"
doc_class: spec
language: pl
title: 05 - Network
summary: Network protocol classes and TFS extended opcode patch appendix.
---


# 05 - Network

Network protocol classes and TFS extended opcode patch appendix.

## Przegląd

Ten rozdział dokumentuje 05 network w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

README
protocol_versions
packet_structure
extended_opcodes
appendix_tfs_extendedopcode
blueprints/index
datasets/index
diagrams/index
```

## Key Topics

### Protocol Version Compatibility

OTClient v8 supports protocols 7.4-12.0+. See [Protocol Versions](./protocol_versions.md) for compatibility matrix, version negotiation, and feature detection.

### Packet Structure

Binary packet format with length, opcode, and payload. See [Packet Structure](./packet_structure.md) for serialization examples, common patterns, and debugging tools.

### Extended Opcodes

Custom communication channel for server-specific features. See [Extended Opcodes Usage](./extended_opcodes.md) for registration, common patterns, and best practices.

## Datasets

- `entities.csv`
- `extended_opcodes.csv`
- `flows.csv`

## Diagramy

```{contents}
:local:
:depth: 2
```

## Crosslinks

- [Core API](../01_core/index.md) - Network classes and protocol implementation
- [Events](../02_events/index.md) - Network event handling
- [Game Runtime](../10_game_runtime/index.md) - Game state synchronization
- [Modules](../03_modules/index.md) - Lua network API


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.411532Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [x] Diagrams added (protocol negotiation sequence)
- [x] Crosslinks verified (4 links)
- [x] Content complete (protocol versions + packet structure + extended opcodes)

## Appendix / Facets

(facet-05_network.main)=
### Facet: `05_network.main`

Main documentation facet for 05_network.

(facet-05_network.protocol)=
### Facet: `05_network.protocol`

Protocol version compatibility and negotiation.

(facet-05_network.packets)=
### Facet: `05_network.packets`

Packet structure, serialization, and common patterns.

(facet-05_network.extended)=
### Facet: `05_network.extended`

Extended opcodes usage and custom communication.
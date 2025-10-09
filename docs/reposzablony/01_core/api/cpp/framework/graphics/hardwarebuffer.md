---
doc_id: "cpp-api-ca317df995c1"
source_path: "framework/graphics/hardwarebuffer.h"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:40Z"
doc_class: "api"
language: "pl"
title: "API: hardwarebuffer.h"
summary: "Dokumentacja API C++ dla framework/graphics/hardwarebuffer.h"
tags: ["cpp", "api", "otclient"]
---

# framework/graphics/hardwarebuffer.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu hardwarebuffer.

## Classes/Structs

### Klasa: `HardwareBuffer`

| Member | Brief | Signature |
|--------|-------|-----------|
| `bind` |  | `void bind() { glBindBuffer(m_type, m_id); }` |
| `unbind` |  | `static void unbind(Type type) { glBindBuffer(type, 0); }` |
| `write` |  | `void write(void *data, int count, UsagePattern usage) { glBufferData(m_type, count, data, usage); }` |

## Enums

### `Type`

**Wartości:**

- `VertexBuffer`
- `IndexBuffer`

### `UsagePattern`

**Wartości:**

- `StreamDraw`
- `StaticDraw`
- `DynamicDraw`

## Functions

### `bind`

**Sygnatura:** `void bind() { glBindBuffer(m_type, m_id); }`

### `unbind`

**Sygnatura:** `static void unbind(Type type) { glBindBuffer(type, 0); }`

### `write`

**Sygnatura:** `void write(void *data, int count, UsagePattern usage) { glBufferData(m_type, count, data, usage); }`

## Class Diagram

Zobacz: [../diagrams/hardwarebuffer.mmd](../diagrams/hardwarebuffer.mmd)

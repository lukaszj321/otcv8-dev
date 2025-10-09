---
doc_id: "cpp-api-672df5d261f6"
source_path: "framework/net/server.h"
source_sha: "05ca843"
last_sync_iso: "2025-10-09T05:38:05Z"
doc_class: "api"
language: "pl"
title: "API: server.h"
summary: "Dokumentacja API C++ dla framework/net/server.h"
tags: ["cpp", "api", "otclient"]
---

# framework/net/server.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu server.

## Classes/Structs

### Klasa: `Server`

| Member | Brief | Signature |
|--------|-------|-----------|
| `create` |  | `static ServerPtr create(int port)` |
| `isOpen` |  | `bool isOpen() { return m_isOpen; }` |
| `close` |  | `void close()` |
| `acceptNext` |  | `void acceptNext()` |

## Functions

### `create`

**Sygnatura:** `static ServerPtr create(int port)`

### `isOpen`

**Sygnatura:** `bool isOpen() { return m_isOpen; }`

### `close`

**Sygnatura:** `void close()`

### `acceptNext`

**Sygnatura:** `void acceptNext()`

## Class Diagram

Zobacz: [../diagrams/server.mmd](../diagrams/server.mmd)

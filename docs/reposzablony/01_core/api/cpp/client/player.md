---
doc_id: "cpp-api-0c90220d7246"
source_path: "client/player.h"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:39Z"
doc_class: "api"
language: "pl"
title: "API: player.h"
summary: "Dokumentacja API C++ dla client/player.h"
tags: ["cpp", "api", "otclient"]
---

# client/player.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu player.

## Classes/Structs

### Klasa: `Player`

| Member | Brief | Signature |
|--------|-------|-----------|
| `asPlayer` |  | `PlayerPtr asPlayer() { return static_self_cast<Player>(); }` |
| `isPlayer` |  | `bool isPlayer() { return true; }` |

## Functions

### `asPlayer`

**Sygnatura:** `PlayerPtr asPlayer() { return static_self_cast<Player>(); }`

### `isPlayer`

**Sygnatura:** `bool isPlayer() { return true; }`

## Class Diagram

Zobacz: [../diagrams/player.mmd](../diagrams/player.mmd)

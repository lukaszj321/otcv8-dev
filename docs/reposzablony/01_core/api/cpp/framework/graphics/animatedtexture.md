---
doc_id: "cpp-api-816adc7bba31"
source_path: "framework/graphics/animatedtexture.h"
source_sha: "05ca843"
last_sync_iso: "2025-10-09T05:38:05Z"
doc_class: "api"
language: "pl"
title: "API: animatedtexture.h"
summary: "Dokumentacja API C++ dla framework/graphics/animatedtexture.h"
tags: ["cpp", "api", "otclient"]
---

# framework/graphics/animatedtexture.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu animatedtexture.

## Classes/Structs

### Klasa: `AnimatedTexture`

| Member | Brief | Signature |
|--------|-------|-----------|
| `replace` |  | `void replace(const ImagePtr& image) { }` |
| `update` |  | `void update()` |
| `isAnimatedTexture` |  | `virtual bool isAnimatedTexture() { return true; }` |
| `buildHardwareMipmaps` |  | `virtual bool buildHardwareMipmaps()` |
| `setSmooth` |  | `virtual void setSmooth(bool smooth)` |
| `setRepeat` |  | `virtual void setRepeat(bool repeat)` |

## Functions

### `replace`

**Sygnatura:** `void replace(const ImagePtr& image) { }`

### `update`

**Sygnatura:** `void update()`

## Class Diagram

Zobacz: [../diagrams/animatedtexture.mmd](../diagrams/animatedtexture.mmd)

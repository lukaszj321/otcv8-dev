---
doc_id: "cpp-api-da28a5b58953"
source_path: "client/uiprogressrect.h"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:39Z"
doc_class: "api"
language: "pl"
title: "API: uiprogressrect.h"
summary: "Dokumentacja API C++ dla client/uiprogressrect.h"
tags: ["cpp", "api", "otclient"]
---

# client/uiprogressrect.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu uiprogressrect.

## Classes/Structs

### Klasa: `UIProgressRect`

| Member | Brief | Signature |
|--------|-------|-----------|
| `drawSelf` |  | `void drawSelf(Fw::DrawPane drawPane)` |
| `setPercent` |  | `void setPercent(float percent)` |
| `getPercent` |  | `float getPercent() { return m_percent; }` |
| `onStyleApply` |  | `void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)` |
| `m_percent` |  | `float m_percent` |

## Functions

### `drawSelf`

**Sygnatura:** `void drawSelf(Fw::DrawPane drawPane)`

### `setPercent`

**Sygnatura:** `void setPercent(float percent)`

### `getPercent`

**Sygnatura:** `float getPercent() { return m_percent; }`

### `onStyleApply`

**Sygnatura:** `void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`

## Class Diagram

Zobacz: [../diagrams/uiprogressrect.mmd](../diagrams/uiprogressrect.mmd)

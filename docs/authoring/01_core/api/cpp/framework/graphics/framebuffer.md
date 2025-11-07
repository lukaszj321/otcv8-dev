---
doc_id: "cpp-api-b8aeec25ee0e"
source_path: "framework/graphics/framebuffer.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: framebuffer.h"
summary: "Dokumentacja API C++ dla framework/graphics/framebuffer.h"
tags: ["cpp", "api", "otclient"]
---

# framework/graphics/framebuffer.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu framebuffer.

## Classes/Structs

### Klasa: `FrameBuffer`

| Member | Brief | Signature |
|--------|-------|-----------|
| `resize` |  | `void resize(const Size& size)` |
| `bind` |  | `void bind(const FrameBufferPtr& depthFramebuffer = nullptr)` |
| `release` |  | `void release()` |
| `draw` |  | `void draw()` |
| `draw` |  | `void draw(const Rect& dest)` |
| `draw` |  | `void draw(const Rect& dest, const Rect& src)` |
| `setSmooth` |  | `void setSmooth(bool enabled)` |
| `getTexture` |  | `TexturePtr getTexture() { return m_texture; }` |
| `getSize` |  | `Size getSize()` |
| `isSmooth` |  | `bool isSmooth() { return m_smooth; }` |
| `getDepthRenderBuffer` |  | `uint getDepthRenderBuffer() { return m_depthRbo; }` |
| `hasDepth` |  | `bool hasDepth() { return m_depth; }` |
| `readPixels` |  | `std::vector<uint32_t> readPixels()` |
| `doScreenshot` |  | `void doScreenshot(std::string fileName)` |

## Functions

### `resize`

**Sygnatura:** `void resize(const Size& size)`

### `bind`

**Sygnatura:** `void bind(const FrameBufferPtr& depthFramebuffer = nullptr)`

### `release`

**Sygnatura:** `void release()`

### `draw`

**Sygnatura:** `void draw()`

### `draw`

**Sygnatura:** `void draw(const Rect& dest)`

### `draw`

**Sygnatura:** `void draw(const Rect& dest, const Rect& src)`

### `setSmooth`

**Sygnatura:** `void setSmooth(bool enabled)`

### `getTexture`

**Sygnatura:** `TexturePtr getTexture() { return m_texture; }`

### `getSize`

**Sygnatura:** `Size getSize()`

### `isSmooth`

**Sygnatura:** `bool isSmooth() { return m_smooth; }`

### `getDepthRenderBuffer`

**Sygnatura:** `uint getDepthRenderBuffer() { return m_depthRbo; }`

### `hasDepth`

**Sygnatura:** `bool hasDepth() { return m_depth; }`

### `readPixels`

**Sygnatura:** `std::vector<uint32_t> readPixels()`

### `doScreenshot`

**Sygnatura:** `void doScreenshot(std::string fileName)`

### `internalCreate`

**Sygnatura:** `void internalCreate()`

### `internalBind`

**Sygnatura:** `void internalBind()`

### `internalRelease`

**Sygnatura:** `void internalRelease()`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    FrameBuffer["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>FrameBuffer</div><hr/>
            <b>Lifecycle:</b><br/>
            + resize(size)<br/>
            <b>Rendering:</b><br/>
            + bind(depthFramebuffer)<br/>
            + release()<br/>
            + draw()<br/>
            + draw(dest)<br/>
            + draw(dest, src)<br/>
            <b>Configuration:</b><br/>
            + setSmooth(enabled)<br/>
            <b>Access:</b><br/>
            + getTexture()<br/>
            + getSize()<br/>
            + isSmooth()<br/>
            + hasDepth()<br/>
            <b>Utilities:</b><br/>
            + readPixels()<br/>
            + doScreenshot(fileName)
        </div>
    "]:::core;
    
    Texture["Texture"]:::data
    
    FrameBuffer --> |"contains"| Texture
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

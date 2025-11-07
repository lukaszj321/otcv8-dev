---
doc_id: "cpp-api-03f1fba29e0d"
source_path: "framework/graphics/framebuffermanager.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: framebuffermanager.h"
summary: "Dokumentacja API C++ dla framework/graphics/framebuffermanager.h"
tags: ["cpp", "api", "otclient"]
---

# framework/graphics/framebuffermanager.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu framebuffermanager.

## Classes/Structs

### Klasa: `FrameBufferManager`

| Member | Brief | Signature |
|--------|-------|-----------|
| `init` |  | `void init()` |
| `terminate` |  | `void terminate()` |
| `clear` |  | `void clear()` |
| `createFrameBuffer` |  | `FrameBufferPtr createFrameBuffer(bool withDepth = false)` |
| `m_temporaryFramebuffer` |  | `FrameBufferPtr m_temporaryFramebuffer` |
| `m_drawQueueTemporaryFramebuffer` |  | `FrameBufferPtr m_drawQueueTemporaryFramebuffer` |
| `m_framebuffers` |  | `std::vector<FrameBufferPtr> m_framebuffers` |

## Functions

### `init`

**Sygnatura:** `void init()`

### `terminate`

**Sygnatura:** `void terminate()`

### `clear`

**Sygnatura:** `void clear()`

### `createFrameBuffer`

**Sygnatura:** `FrameBufferPtr createFrameBuffer(bool withDepth = false)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    FrameBufferManager["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>FrameBufferManager</div><hr/>
            <b>Lifecycle:</b><br/>
            + init()<br/>
            + terminate()<br/>
            <b>Management:</b><br/>
            + clear()<br/>
            + createFrameBuffer(withDepth)<br/>
            <b>Special Buffers:</b><br/>
            - m_temporaryFramebuffer<br/>
            - m_drawQueueTemporaryFramebuffer<br/>
            <b>Storage:</b><br/>
            - m_framebuffers
        </div>
    "]:::core;
    
    FrameBuffer["FrameBuffer"]:::data
    
    FrameBufferManager --> |"manages"| FrameBuffer
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

## Diagram: Framebuffer System Block Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
block-beta
    columns 2
    
    block:framebufferManager:1
        FrameBufferManager["FrameBufferManager<br/>Manages framebuffers"]
    end
    
    block:framebuffers:2
        StandardFB["Standard Framebuffer<br/>Color + optional depth"]
        TemporaryFB["Temporary Framebuffer<br/>For intermediate rendering"]
        DrawQueueFB["Draw Queue FB<br/>For draw queue operations"]
    end
    
    block:components:3
        ColorTexture["Color Texture<br/>Render target"]
        DepthBuffer["Depth Buffer<br/>Depth testing"]
    end
    
    FrameBufferManager --> StandardFB
    FrameBufferManager --> TemporaryFB
    FrameBufferManager --> DrawQueueFB
    StandardFB --> ColorTexture
    StandardFB --> DepthBuffer
    TemporaryFB --> ColorTexture
```
<!-- /mermaid-diagram -->

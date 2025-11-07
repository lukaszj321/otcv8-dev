---
doc_id: "cpp-api-08d7d4d49331"
source_path: "framework/graphics/texturemanager.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: texturemanager.h"
summary: "Dokumentacja API C++ dla framework/graphics/texturemanager.h"
tags: ["cpp", "api", "otclient"]
---

# framework/graphics/texturemanager.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu texturemanager.

## Classes/Structs

### Klasa: `TextureManager`

| Member | Brief | Signature |
|--------|-------|-----------|
| `init` |  | `void init()` |
| `terminate` |  | `void terminate()` |
| `clearCache` |  | `void clearCache()` |
| `reload` |  | `void reload()` |
| `preload` |  | `void preload(const std::string& fileName) { getTexture(fileName); }` |
| `getTexture` |  | `TexturePtr getTexture(const std::string& fileName)` |
| `loadTexture` |  | `TexturePtr loadTexture(std::stringstream& file, const std::string& source)` |

## Functions

### `init`

**Sygnatura:** `void init()`

### `terminate`

**Sygnatura:** `void terminate()`

### `clearCache`

**Sygnatura:** `void clearCache()`

### `reload`

**Sygnatura:** `void reload()`

### `preload`

**Sygnatura:** `void preload(const std::string& fileName) { getTexture(fileName); }`

### `getTexture`

**Sygnatura:** `TexturePtr getTexture(const std::string& fileName)`

### `loadTexture`

**Sygnatura:** `TexturePtr loadTexture(std::stringstream& file, const std::string& source)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    TextureManager["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>TextureManager</div><hr/>
            <b>Lifecycle:</b><br/>
            + init()<br/>
            + terminate()<br/>
            <b>Cache Management:</b><br/>
            + clearCache()<br/>
            + reload()<br/>
            <b>Loading:</b><br/>
            + getTexture(fileName)<br/>
            + loadTexture(file, source)<br/>
            + preload(fileName)
        </div>
    "]:::core;
    
    Texture["Texture"]:::data
    Cache["Texture Cache"]:::data
    
    TextureManager --> |"manages"| Texture
    TextureManager --> |"uses"| Cache
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

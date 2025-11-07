---
doc_id: "cpp-api-9121fe15dd7f"
source_path: "framework/graphics/shadermanager.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: shadermanager.h"
summary: "Dokumentacja API C++ dla framework/graphics/shadermanager.h"
tags: ["cpp", "api", "otclient"]
---

# framework/graphics/shadermanager.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu shadermanager.

## Classes/Structs

### Klasa: `ShaderManager`

| Member | Brief | Signature |
|--------|-------|-----------|
| `init` |  | `void init()` |
| `terminate` |  | `void terminate()` |
| `createShader` |  | `void createShader(const std::string& name, std::string vertex, std::string fragment, bool colorMatrix = false)` |
| `createOutfitShader` |  | `void createOutfitShader(const std::string& name, std::string vertex, std::string fragment)` |
| `createShader` |  | `return createShader(name, vertex, fragment, true)` |
| `addTexture` |  | `void addTexture(const std::string& name, const std::string& file)` |
| `getShader` |  | `PainterShaderProgramPtr getShader(const std::string& name)` |

## Functions

### `init`

**Sygnatura:** `void init()`

### `terminate`

**Sygnatura:** `void terminate()`

### `createShader`

**Sygnatura:** `void createShader(const std::string& name, std::string vertex, std::string fragment, bool colorMatrix = false)`

### `createOutfitShader`

**Sygnatura:** `void createOutfitShader(const std::string& name, std::string vertex, std::string fragment)`

### `createShader`

**Sygnatura:** `return createShader(name, vertex, fragment, true)`

### `addTexture`

**Sygnatura:** `void addTexture(const std::string& name, const std::string& file)`

### `getShader`

**Sygnatura:** `PainterShaderProgramPtr getShader(const std::string& name)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    ShaderManager["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>ShaderManager</div><hr/>
            <b>Lifecycle:</b><br/>
            + init()<br/>
            + terminate()<br/>
            <b>Shader Creation:</b><br/>
            + createShader(name, vertex, fragment, colorMatrix)<br/>
            + createOutfitShader(name, vertex, fragment)<br/>
            <b>Texture Management:</b><br/>
            + addTexture(name, file)<br/>
            <b>Access:</b><br/>
            + getShader(name)
        </div>
    "]:::core;
    
    PainterShaderProgram["PainterShaderProgram"]:::data
    ShaderCache["Shader Cache"]:::data
    
    ShaderManager --> |"manages"| PainterShaderProgram
    ShaderManager --> |"uses"| ShaderCache
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

## Diagram: Shader System Block Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
block-beta
    columns 3
    
    block:shaderSystem:1
        ShaderManager["ShaderManager<br/>Manages shader programs"]
    end
    
    block:shaderCreation:2
        VertexShader["Vertex Shader<br/>Vertex processing"]
        FragmentShader["Fragment Shader<br/>Pixel processing"]
        ShaderProgram["Shader Program<br/>Linked shaders"]
    end
    
    block:shaderCache:3
        ShaderCache["Shader Cache<br/>Stored programs"]
        TextureCache["Texture Cache<br/>Bound textures"]
    end
    
    ShaderManager --> VertexShader
    ShaderManager --> FragmentShader
    VertexShader --> ShaderProgram
    FragmentShader --> ShaderProgram
    ShaderProgram --> ShaderCache
    ShaderManager --> TextureCache
```
<!-- /mermaid-diagram -->

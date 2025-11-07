---
doc_id: "cpp-api-bee100a8dc6c"
source_path: "framework/core/config.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: config.h"
summary: "Dokumentacja API C++ dla framework/core/config.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/config.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu config.

## Classes/Structs

### Klasa: `Config`

| Member | Brief | Signature |
|--------|-------|-----------|
| `load` |  | `bool load(const std::string& file)` |
| `unload` |  | `bool unload()` |
| `save` |  | `bool save()` |
| `clear` |  | `void clear()` |
| `setValue` |  | `void setValue(const std::string& key, const std::string& value)` |
| `setList` |  | `void setList(const std::string& key, const std::vector<std::string>& list)` |
| `getValue` |  | `std::string getValue(const std::string& key)` |
| `getList` |  | `std::vector<std::string> getList(const std::string& key)` |
| `setNode` |  | `void setNode(const std::string& key, const OTMLNodePtr& node)` |
| `mergeNode` |  | `void mergeNode(const std::string& key, const OTMLNodePtr& node)` |
| `getNode` |  | `OTMLNodePtr getNode(const std::string& key)` |
| `getNodeSize` |  | `int getNodeSize(const std::string& key)` |
| `exists` |  | `bool exists(const std::string& key)` |
| `remove` |  | `void remove(const std::string& key)` |
| `getFileName` |  | `std::string getFileName()` |
| `isLoaded` |  | `bool isLoaded()` |
| `asConfig` |  | `ConfigPtr asConfig() { return static_self_cast<Config>(); }` |

## Functions

### `load`

**Sygnatura:** `bool load(const std::string& file)`

### `unload`

**Sygnatura:** `bool unload()`

### `save`

**Sygnatura:** `bool save()`

### `clear`

**Sygnatura:** `void clear()`

### `setValue`

**Sygnatura:** `void setValue(const std::string& key, const std::string& value)`

### `setList`

**Sygnatura:** `void setList(const std::string& key, const std::vector<std::string>& list)`

### `getValue`

**Sygnatura:** `std::string getValue(const std::string& key)`

### `getList`

**Sygnatura:** `std::vector<std::string> getList(const std::string& key)`

### `setNode`

**Sygnatura:** `void setNode(const std::string& key, const OTMLNodePtr& node)`

### `mergeNode`

**Sygnatura:** `void mergeNode(const std::string& key, const OTMLNodePtr& node)`

### `getNode`

**Sygnatura:** `OTMLNodePtr getNode(const std::string& key)`

### `getNodeSize`

**Sygnatura:** `int getNodeSize(const std::string& key)`

### `exists`

**Sygnatura:** `bool exists(const std::string& key)`

### `remove`

**Sygnatura:** `void remove(const std::string& key)`

### `getFileName`

**Sygnatura:** `std::string getFileName()`

### `isLoaded`

**Sygnatura:** `bool isLoaded()`

### `asConfig`

**Sygnatura:** `ConfigPtr asConfig() { return static_self_cast<Config>(); }`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    Config["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>Config</div><hr/>
            <b>File Operations:</b><br/>
            + load(file)<br/>
            + unload()<br/>
            + save()<br/>
            + clear()<br/>
            <b>Value Access:</b><br/>
            + setValue(key, value)<br/>
            + getValue(key)<br/>
            + setList(key, list)<br/>
            + getList(key)<br/>
            <b>Node Operations:</b><br/>
            + setNode(key, node)<br/>
            + mergeNode(key, node)<br/>
            + getNode(key)<br/>
            <b>Management:</b><br/>
            + exists(key)<br/>
            + remove(key)<br/>
            + getNodeSize(key)<br/>
            <b>State:</b><br/>
            + isLoaded()<br/>
            + getFileName()
        </div>
    "]:::core;
    
    OTMLNode["OTMLNode"]:::data
    ConfigManager["ConfigManager"]:::core
    
    Config --> |"contains"| OTMLNode
    ConfigManager --> |"manages"| Config
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

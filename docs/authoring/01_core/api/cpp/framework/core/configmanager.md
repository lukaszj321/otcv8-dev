---
doc_id: "cpp-api-67c7a080caa9"
source_path: "framework/core/configmanager.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: configmanager.h"
summary: "Dokumentacja API C++ dla framework/core/configmanager.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/configmanager.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu configmanager.

## Classes/Structs

### Klasa: `ConfigManager`

| Member | Brief | Signature |
|--------|-------|-----------|
| `init` |  | `void init()` |
| `terminate` |  | `void terminate()` |
| `getSettings` |  | `ConfigPtr getSettings()` |
| `get` |  | `ConfigPtr get(const std::string& file)` |
| `create` |  | `ConfigPtr create(const std::string& file)` |
| `loadSettings` |  | `ConfigPtr loadSettings(const std::string file)` |
| `load` |  | `ConfigPtr load(const std::string& file)` |
| `unload` |  | `bool unload(const std::string& file)` |
| `remove` |  | `void remove(const ConfigPtr config)` |
| `m_settings` |  | `ConfigPtr m_settings` |

## Functions

### `init`

**Sygnatura:** `void init()`

### `terminate`

**Sygnatura:** `void terminate()`

### `getSettings`

**Sygnatura:** `ConfigPtr getSettings()`

### `get`

**Sygnatura:** `ConfigPtr get(const std::string& file)`

### `create`

**Sygnatura:** `ConfigPtr create(const std::string& file)`

### `loadSettings`

**Sygnatura:** `ConfigPtr loadSettings(const std::string file)`

### `load`

**Sygnatura:** `ConfigPtr load(const std::string& file)`

### `unload`

**Sygnatura:** `bool unload(const std::string& file)`

### `remove`

**Sygnatura:** `void remove(const ConfigPtr config)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    ConfigManager["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>ConfigManager</div><hr/>
            <b>Lifecycle:</b><br/>
            + init()<br/>
            + terminate()<br/>
            <b>Config Access:</b><br/>
            + getSettings()<br/>
            + get(file)<br/>
            + create(file)<br/>
            <b>Loading:</b><br/>
            + loadSettings(file)<br/>
            + load(file)<br/>
            <b>Management:</b><br/>
            + unload(file)<br/>
            + remove(config)
        </div>
    "]:::core;
    
    Config["Config"]:::data
    
    ConfigManager --> |"manages"| Config
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

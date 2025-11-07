---
doc_id: "cpp-api-e2d0a13cdfb3"
source_path: "framework/core/modulemanager.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: modulemanager.h"
summary: "Dokumentacja API C++ dla framework/core/modulemanager.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/modulemanager.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu modulemanager.

## Classes/Structs

### Klasa: `ModuleManager`

| Member | Brief | Signature |
|--------|-------|-----------|
| `clear` |  | `void clear()` |
| `discoverModules` |  | `void discoverModules()` |
| `autoLoadModules` |  | `void autoLoadModules(int maxPriority)` |
| `discoverModule` |  | `ModulePtr discoverModule(const std::string& moduleFile)` |
| `ensureModuleLoaded` |  | `void ensureModuleLoaded(const std::string& moduleName)` |
| `unloadModules` |  | `void unloadModules()` |
| `reloadModules` |  | `void reloadModules()` |
| `getModule` |  | `ModulePtr getModule(const std::string& moduleName)` |
| `getModules` |  | `std::deque<ModulePtr> getModules() { return m_modules; }` |
| `updateModuleLoadOrder` |  | `void updateModuleLoadOrder(ModulePtr module)` |

## Functions

### `clear`

**Sygnatura:** `void clear()`

### `discoverModules`

**Sygnatura:** `void discoverModules()`

### `autoLoadModules`

**Sygnatura:** `void autoLoadModules(int maxPriority)`

### `discoverModule`

**Sygnatura:** `ModulePtr discoverModule(const std::string& moduleFile)`

### `ensureModuleLoaded`

**Sygnatura:** `void ensureModuleLoaded(const std::string& moduleName)`

### `unloadModules`

**Sygnatura:** `void unloadModules()`

### `reloadModules`

**Sygnatura:** `void reloadModules()`

### `getModule`

**Sygnatura:** `ModulePtr getModule(const std::string& moduleName)`

### `getModules`

**Sygnatura:** `std::deque<ModulePtr> getModules() { return m_modules; }`

### `updateModuleLoadOrder`

**Sygnatura:** `void updateModuleLoadOrder(ModulePtr module)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef module fill:#24343a,stroke:#8fa2a8,color:#ddd,stroke-width:1px;
    
    ModuleManager["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>ModuleManager</div><hr/>
            <b>Discovery:</b><br/>
            + discoverModules()<br/>
            + discoverModule(file)<br/>
            <b>Loading:</b><br/>
            + autoLoadModules(priority)<br/>
            + ensureModuleLoaded(name)<br/>
            + reloadModules()<br/>
            + unloadModules()<br/>
            <b>Access:</b><br/>
            + getModule(name)<br/>
            + getModules()<br/>
            <b>Management:</b><br/>
            + updateModuleLoadOrder(module)<br/>
            + clear()
        </div>
    "]:::core;
    
    Module["Module"]:::module
    
    ModuleManager --> |"manages"| Module
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef module fill:#24343a,stroke:#8fa2a8,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->

## Diagram: Module Loading Architecture (C4 Component)

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
C4Component
    title Module Manager Component Diagram
    
    Container_Boundary(otclient, "OTClient Application") {
        Component(modulemanager, "ModuleManager", "C++", "Discovers and loads Lua modules")
        Component(discoverer, "Module Discoverer", "C++", "Scans module directories")
        Component(loader, "Module Loader", "C++", "Loads and initializes modules")
        Component(luaengine, "Lua Engine", "C++", "Lua VM and bindings")
    }
    SystemDb_Ext(moduledir, "Module Directory", "File System")
    System_Ext(lua, "Lua Runtime", "Lua 5.4")
    
    Rel(modulemanager, discoverer, "Uses")
    Rel(modulemanager, loader, "Uses")
    Rel(loader, luaengine, "Executes via")
    Rel(discoverer, moduledir, "Reads from")
    Rel(luaengine, lua, "Uses")
```
<!-- /mermaid-diagram -->

## Diagram: Module Loading Sequence

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant App
    participant ModuleManager
    participant Discoverer
    participant Loader
    participant LuaEngine
    participant Module
    
    App->>ModuleManager: discoverModules()
    ModuleManager->>Discoverer: scan directories
    Discoverer-->>ModuleManager: module list
    ModuleManager->>ModuleManager: updateModuleLoadOrder()
    
    App->>ModuleManager: autoLoadModules(priority)
    ModuleManager->>Loader: load module
    Loader->>LuaEngine: execute module script
    LuaEngine->>Module: init()
    Module-->>LuaEngine: registered
    LuaEngine-->>Loader: success
    Loader-->>ModuleManager: module loaded
    ModuleManager-->>App: modules ready
```
<!-- /mermaid-diagram -->

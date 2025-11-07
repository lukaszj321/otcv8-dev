---
doc_id: "cpp-api-75c631f52e64"
source_path: "framework/graphics/fontmanager.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: fontmanager.h"
summary: "Dokumentacja API C++ dla framework/graphics/fontmanager.h"
tags: ["cpp", "api", "otclient"]
---

# framework/graphics/fontmanager.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu fontmanager.

## Classes/Structs

### Klasa: `FontManager`

| Member | Brief | Signature |
|--------|-------|-----------|
| `terminate` |  | `void terminate()` |
| `clearFonts` |  | `void clearFonts()` |
| `importFont` |  | `void importFont(std::string file)` |
| `fontExists` |  | `bool fontExists(const std::string& fontName)` |
| `getFont` |  | `BitmapFontPtr getFont(const std::string& fontName)` |
| `getDefaultFont` |  | `BitmapFontPtr getDefaultFont() { return m_defaultFont; }` |
| `setDefaultFont` |  | `void setDefaultFont(const std::string& fontName) { m_defaultFont = getFont(fontName); }` |

## Functions

### `terminate`

**Sygnatura:** `void terminate()`

### `clearFonts`

**Sygnatura:** `void clearFonts()`

### `importFont`

**Sygnatura:** `void importFont(std::string file)`

### `fontExists`

**Sygnatura:** `bool fontExists(const std::string& fontName)`

### `getFont`

**Sygnatura:** `BitmapFontPtr getFont(const std::string& fontName)`

### `getDefaultFont`

**Sygnatura:** `BitmapFontPtr getDefaultFont() { return m_defaultFont; }`

### `setDefaultFont`

**Sygnatura:** `void setDefaultFont(const std::string& fontName) { m_defaultFont = getFont(fontName); }`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    FontManager["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>FontManager</div><hr/>
            <b>Lifecycle:</b><br/>
            + terminate()<br/>
            <b>Font Management:</b><br/>
            + clearFonts()<br/>
            + importFont(file)<br/>
            + fontExists(fontName)<br/>
            + getFont(fontName)<br/>
            <b>Default Font:</b><br/>
            + getDefaultFont()<br/>
            + setDefaultFont(fontName)
        </div>
    "]:::core;
    
    BitmapFont["BitmapFont"]:::data
    FontCache["Font Cache"]:::data
    
    FontManager --> |"manages"| BitmapFont
    FontManager --> |"uses"| FontCache
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

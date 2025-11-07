---
doc_id: "cpp-api-e56a90848570"
source_path: "framework/util/databuffer.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: databuffer.h"
summary: "Dokumentacja API C++ dla framework/util/databuffer.h"
tags: ["cpp", "api", "otclient"]
---

# framework/util/databuffer.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu databuffer.

## Classes/Structs

### Klasa: `DataBuffer`

**Szablon:** `template<class T>`

| Member | Brief | Signature |
|--------|-------|-----------|
| `reset` |  | `inline void reset() { m_size = 0; }` |
| `clear` |  | `inline void clear() {` |
| `empty` |  | `inline bool empty() const { return m_size == 0; }` |
| `size` |  | `inline uint size() const { return m_size; }` |
| `reserve` |  | `inline void reserve(uint n) {` |
| `resize` |  | `inline void resize(uint n, T def = T()) {` |
| `grow` |  | `inline void grow(uint n, bool precise = false) {` |
| `newcapacity` |  | `uint newcapacity = m_capacity` |
| `add` |  | `inline void add(const T& v) {` |

## Functions

### `reset`

**Sygnatura:** `inline void reset() { m_size = 0; }`

### `clear`

**Sygnatura:** `inline void clear() {`

### `empty`

**Sygnatura:** `inline bool empty() const { return m_size == 0; }`

### `size`

**Sygnatura:** `inline uint size() const { return m_size; }`

### `reserve`

**Sygnatura:** `inline void reserve(uint n) {`

### `resize`

**Sygnatura:** `inline void resize(uint n, T def = T()) {`

### `grow`

**Sygnatura:** `inline void grow(uint n, bool precise = false) {`

### `add`

**Sygnatura:** `inline void add(const T& v) {`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    DataBuffer["DataBuffer&lt;T&gt;<br/><i>template class</i>"]:::core
    
    DataBuffer --> |"contains"| Buffer["Buffer<br/>m_data"]:::data
    DataBuffer --> |"tracks"| Size["Size<br/>m_size"]:::data
    DataBuffer --> |"tracks"| Capacity["Capacity<br/>m_capacity"]:::data
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

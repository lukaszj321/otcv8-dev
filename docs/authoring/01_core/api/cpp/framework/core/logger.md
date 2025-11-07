---
doc_id: "cpp-api-beaef2d6673d"
source_path: "framework/core/logger.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: logger.h"
summary: "Dokumentacja API C++ dla framework/core/logger.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/logger.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu logger.

## Classes/Structs

### Struktura: `LogMessage`

### Klasa: `Logger`

| Member | Brief | Signature |
|--------|-------|-----------|
| `log` |  | `void log(Fw::LogLevel level, const std::string& message)` |
| `logFunc` |  | `void logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction)` |
| `debug` |  | `void debug(const std::string& what) { log(Fw::LogDebug, what); }` |
| `info` |  | `void info(const std::string& what) { log(Fw::LogInfo, what); }` |
| `warning` |  | `void warning(const std::string& what) { log(Fw::LogWarning, what); }` |
| `error` |  | `void error(const std::string& what) { log(Fw::LogError, what); }` |
| `fatal` |  | `void fatal(const std::string& what) { log(Fw::LogFatal, what); }` |
| `fireOldMessages` |  | `void fireOldMessages()` |
| `setLogFile` |  | `void setLogFile(const std::string& file)` |
| `setOnLog` |  | `void setOnLog(const OnLogCallback& onLog) { m_onLog = onLog; }` |
| `getLastLog` |  | `std::string getLastLog() {` |
| `m_lastLog` |  | `return m_lastLog` |
| `setTestingMode` |  | `void setTestingMode()` |

## Functions

### `log`

**Sygnatura:** `void log(Fw::LogLevel level, const std::string& message)`

### `logFunc`

**Sygnatura:** `void logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction)`

### `debug`

**Sygnatura:** `void debug(const std::string& what) { log(Fw::LogDebug, what); }`

### `info`

**Sygnatura:** `void info(const std::string& what) { log(Fw::LogInfo, what); }`

### `warning`

**Sygnatura:** `void warning(const std::string& what) { log(Fw::LogWarning, what); }`

### `error`

**Sygnatura:** `void error(const std::string& what) { log(Fw::LogError, what); }`

### `fatal`

**Sygnatura:** `void fatal(const std::string& what) { log(Fw::LogFatal, what); }`

### `fireOldMessages`

**Sygnatura:** `void fireOldMessages()`

### `setLogFile`

**Sygnatura:** `void setLogFile(const std::string& file)`

### `setOnLog`

**Sygnatura:** `void setOnLog(const OnLogCallback& onLog) { m_onLog = onLog; }`

### `getLastLog`

**Sygnatura:** `std::string getLastLog() {`

### `setTestingMode`

**Sygnatura:** `void setTestingMode()`

## Types/Aliases

### `OnLogCallback`

**Typedef:** `std::function<void(Fw::LogLevel, const std::string&, int64)>`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    Logger["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>Logger</div><hr/>
            <b>Logging Methods:</b><br/>
            + log(level, message)<br/>
            + logFunc(level, message, function)<br/>
            + debug(message)<br/>
            + info(message)<br/>
            + warning(message)<br/>
            + error(message)<br/>
            + fatal(message)<br/>
            <b>Configuration:</b><br/>
            + setLogFile(file)<br/>
            + setOnLog(callback)<br/>
            + setTestingMode()<br/>
            <b>Access:</b><br/>
            + getLastLog()<br/>
            + fireOldMessages()
        </div>
    "]:::core;
    
    LogMessage["LogMessage<br/><i>struct</i>"]:::data
    
    Logger --> |"creates"| LogMessage
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

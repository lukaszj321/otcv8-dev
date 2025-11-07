---
doc_id: "cpp-api-763dbdb72d2c"
source_path: "framework/platform/platform.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: platform.h"
summary: "Dokumentacja API C++ dla framework/platform/platform.h"
tags: ["cpp", "api", "otclient"]
---

# framework/platform/platform.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu platform.

## Classes/Structs

### Klasa: `Platform`

| Member | Brief | Signature |
|--------|-------|-----------|
| `processArgs` |  | `void processArgs(std::vector<std::string>& args)` |
| `spawnProcess` |  | `bool spawnProcess(std::string process, const std::vector<std::string>& args)` |
| `getProcessId` |  | `int getProcessId()` |
| `isProcessRunning` |  | `bool isProcessRunning(const std::string& name)` |
| `killProcess` |  | `bool killProcess(const std::string& name)` |
| `getTempPath` |  | `std::string getTempPath()` |
| `getCurrentDir` |  | `std::string getCurrentDir()` |
| `copyFile` |  | `bool copyFile(std::string from, std::string to)` |
| `fileExists` |  | `bool fileExists(std::string file)` |
| `removeFile` |  | `bool removeFile(std::string file)` |
| `getFileModificationTime` |  | `ticks_t getFileModificationTime(std::string file)` |
| `openUrl` |  | `bool openUrl(std::string url, bool now = false)` |
| `openDir` |  | `bool openDir(std::string path, bool now = false)` |
| `getCPUName` |  | `std::string getCPUName()` |
| `getTotalSystemMemory` |  | `double getTotalSystemMemory()` |
| `getMemoryUsage` |  | `double getMemoryUsage()` |
| `getOSName` |  | `std::string getOSName()` |
| `traceback` |  | `std::string traceback(const std::string& where, int level = 1, int maxDepth = 32)` |
| `getMacAddresses` |  | `std::vector<std::string> getMacAddresses()` |
| `getUserName` |  | `std::string getUserName()` |
| `getDlls` |  | `std::vector<std::string> getDlls()` |
| `getProcesses` |  | `std::vector<std::string> getProcesses()` |
| `getWindows` |  | `std::vector<std::string> getWindows()` |

## Functions

### `processArgs`

**Sygnatura:** `void processArgs(std::vector<std::string>& args)`

### `spawnProcess`

**Sygnatura:** `bool spawnProcess(std::string process, const std::vector<std::string>& args)`

### `getProcessId`

**Sygnatura:** `int getProcessId()`

### `isProcessRunning`

**Sygnatura:** `bool isProcessRunning(const std::string& name)`

### `killProcess`

**Sygnatura:** `bool killProcess(const std::string& name)`

### `getTempPath`

**Sygnatura:** `std::string getTempPath()`

### `getCurrentDir`

**Sygnatura:** `std::string getCurrentDir()`

### `copyFile`

**Sygnatura:** `bool copyFile(std::string from, std::string to)`

### `fileExists`

**Sygnatura:** `bool fileExists(std::string file)`

### `removeFile`

**Sygnatura:** `bool removeFile(std::string file)`

### `getFileModificationTime`

**Sygnatura:** `ticks_t getFileModificationTime(std::string file)`

### `openUrl`

**Sygnatura:** `bool openUrl(std::string url, bool now = false)`

### `openDir`

**Sygnatura:** `bool openDir(std::string path, bool now = false)`

### `getCPUName`

**Sygnatura:** `std::string getCPUName()`

### `getTotalSystemMemory`

**Sygnatura:** `double getTotalSystemMemory()`

### `getMemoryUsage`

**Sygnatura:** `double getMemoryUsage()`

### `getOSName`

**Sygnatura:** `std::string getOSName()`

### `traceback`

**Sygnatura:** `std::string traceback(const std::string& where, int level = 1, int maxDepth = 32)`

### `getMacAddresses`

**Sygnatura:** `std::vector<std::string> getMacAddresses()`

### `getUserName`

**Sygnatura:** `std::string getUserName()`

### `getDlls`

**Sygnatura:** `std::vector<std::string> getDlls()`

### `getProcesses`

**Sygnatura:** `std::vector<std::string> getProcesses()`

### `getWindows`

**Sygnatura:** `std::vector<std::string> getWindows()`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef platform fill:#7f8c8d,stroke:#fff,color:#fff;
    
    Platform["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>Platform</div><hr/>
            <b>Process Management:</b><br/>
            + spawnProcess(process, args)<br/>
            + getProcessId()<br/>
            + isProcessRunning(name)<br/>
            + killProcess(name)<br/>
            <b>File Operations:</b><br/>
            + copyFile(from, to)<br/>
            + fileExists(file)<br/>
            + removeFile(file)<br/>
            + getFileModificationTime(file)<br/>
            <b>System Info:</b><br/>
            + getCPUName()<br/>
            + getTotalSystemMemory()<br/>
            + getMemoryUsage()<br/>
            + getOSName()<br/>
            + getUserName()<br/>
            <b>Utilities:</b><br/>
            + openUrl(url)<br/>
            + openDir(path)<br/>
            + traceback(where, level)
        </div>
    "]:::platform;
    
    OS["Operating System"]:::platform
    
    Platform --> |"interacts with"| OS
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef platform fill:#7f8c8d,stroke:#fff,color:#fff;
```
<!-- /mermaid-diagram -->

## Diagram: Platform Abstraction Architecture (C4 Component)

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
C4Component
    title Platform Abstraction Component Diagram
    
    Container_Boundary(otclient, "OTClient Application") {
        Component(platform, "Platform", "C++", "Cross-platform abstraction layer")
        Component(win32window, "Win32Window", "C++", "Windows window implementation")
        Component(sdlwindow, "SDLWindow", "C++", "SDL window implementation")
        Component(x11window, "X11Window", "C++", "Linux X11 window implementation")
        Component(androidwindow, "AndroidWindow", "C++", "Android window implementation")
    }
    System_Ext(win32, "Windows API", "Win32")
    System_Ext(sdl, "SDL2", "Simple DirectMedia Layer")
    System_Ext(x11, "X11", "X Window System")
    System_Ext(android, "Android NDK", "Android Native")
    
    Rel(platform, win32window, "Uses on Windows")
    Rel(platform, sdlwindow, "Uses on Linux/Mac")
    Rel(platform, x11window, "Uses on Linux")
    Rel(platform, androidwindow, "Uses on Android")
    Rel(win32window, win32, "Calls")
    Rel(sdlwindow, sdl, "Calls")
    Rel(x11window, x11, "Calls")
    Rel(androidwindow, android, "Calls")
```
<!-- /mermaid-diagram -->

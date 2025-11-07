---
doc_id: "cpp-api-a75894abc87a"
source_path: "framework/sound/soundmanager.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: soundmanager.h"
summary: "Dokumentacja API C++ dla framework/sound/soundmanager.h"
tags: ["cpp", "api", "otclient"]
---

# framework/sound/soundmanager.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu soundmanager.

## Classes/Structs

### Klasa: `SoundManager`

| Member | Brief | Signature |
|--------|-------|-----------|
| `init` |  | `void init()` |
| `terminate` |  | `void terminate()` |
| `poll` |  | `void poll()` |
| `setAudioEnabled` |  | `void setAudioEnabled(bool enable)` |
| `isAudioEnabled` |  | `bool isAudioEnabled() { return m_device && m_context && m_audioEnabled ; }` |
| `enableAudio` |  | `void enableAudio() { setAudioEnabled(true); }` |
| `disableAudio` |  | `void disableAudio() { setAudioEnabled(true); }` |
| `stopAll` |  | `void stopAll()` |
| `preload` |  | `void preload(std::string filename)` |
| `play` |  | `SoundSourcePtr play(std::string filename, float fadetime = 0, float gain = 0)` |
| `getChannel` |  | `SoundChannelPtr getChannel(int channel)` |
| `resolveSoundFile` |  | `std::string resolveSoundFile(std::string file)` |
| `ensureContext` |  | `void ensureContext()` |

## Functions

### `init`

**Sygnatura:** `void init()`

### `terminate`

**Sygnatura:** `void terminate()`

### `poll`

**Sygnatura:** `void poll()`

### `setAudioEnabled`

**Sygnatura:** `void setAudioEnabled(bool enable)`

### `isAudioEnabled`

**Sygnatura:** `bool isAudioEnabled() { return m_device && m_context && m_audioEnabled ; }`

### `enableAudio`

**Sygnatura:** `void enableAudio() { setAudioEnabled(true); }`

### `disableAudio`

**Sygnatura:** `void disableAudio() { setAudioEnabled(true); }`

### `stopAll`

**Sygnatura:** `void stopAll()`

### `preload`

**Sygnatura:** `void preload(std::string filename)`

### `play`

**Sygnatura:** `SoundSourcePtr play(std::string filename, float fadetime = 0, float gain = 0)`

### `getChannel`

**Sygnatura:** `SoundChannelPtr getChannel(int channel)`

### `resolveSoundFile`

**Sygnatura:** `std::string resolveSoundFile(std::string file)`

### `ensureContext`

**Sygnatura:** `void ensureContext()`

### `createSoundSource`

**Sygnatura:** `SoundSourcePtr createSoundSource(const std::string& filename)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef sound fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    SoundManager["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>SoundManager</div><hr/>
            <b>Lifecycle:</b><br/>
            + init()<br/>
            + terminate()<br/>
            + poll()<br/>
            <b>Audio Control:</b><br/>
            + setAudioEnabled(enable)<br/>
            + enableAudio()<br/>
            + disableAudio()<br/>
            + isAudioEnabled()<br/>
            <b>Playback:</b><br/>
            + play(filename, fadetime, gain)<br/>
            + stopAll()<br/>
            + preload(filename)<br/>
            <b>Channels:</b><br/>
            + getChannel(channel)<br/>
            <b>Utilities:</b><br/>
            + resolveSoundFile(file)<br/>
            + ensureContext()
        </div>
    "]:::core;
    
    SoundSource["SoundSource"]:::sound
    SoundChannel["SoundChannel"]:::sound
    OpenAL["OpenAL Context"]:::sound
    
    SoundManager --> |"manages"| SoundSource
    SoundManager --> |"manages"| SoundChannel
    SoundManager --> |"uses"| OpenAL
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef sound fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->

## Diagram: Sound Playback Flow (Advanced Sequence)

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant App
    participant SoundManager
    participant SoundSource
    participant SoundFile
    participant OpenAL
    participant Channel
    
    Note over App,Channel: Sound Playback Request
    App->>SoundManager: play(filename, fadetime, gain)
    
    critical Audio must be enabled
        SoundManager->>SoundManager: isAudioEnabled()
        alt Audio enabled
            SoundManager->>SoundFile: resolveSoundFile(filename)
            SoundFile-->>SoundManager: Resolved path
            SoundManager->>SoundFile: Load sound file
            SoundFile-->>SoundManager: Sound data
            SoundManager->>SoundSource: Create source
            SoundSource->>OpenAL: Create AL source
            OpenAL-->>SoundSource: Source ID
            SoundSource->>OpenAL: Set buffer data
            SoundSource->>OpenAL: Set gain/fade
            opt Fade time > 0
                SoundSource->>SoundSource: Start fade in
            end
            SoundSource->>OpenAL: Play source
            SoundManager->>Channel: Assign to channel
            Channel-->>SoundManager: Channel assigned
            SoundManager-->>App: SoundSourcePtr
        else Audio disabled
            SoundManager->>SoundManager: ensureContext()
            alt Context created
                SoundManager->>SoundManager: enableAudio()
                SoundManager->>SoundFile: Load sound file
            else Context failed
                SoundManager-->>App: nullptr
            end
        end
    option Audio initialization failed
        SoundManager-->>App: nullptr
    end
    
    par Polling loop
        loop Every frame
            SoundManager->>SoundManager: poll()
            SoundManager->>SoundSource: Update all sources
            SoundSource->>OpenAL: Update state
        end
    and Sound playback
        loop While playing
            SoundSource->>OpenAL: Check playback state
            alt Playback finished
                SoundSource->>SoundSource: Mark as finished
                SoundSource->>Channel: Release channel
            end
        end
    end
```
<!-- /mermaid-diagram -->

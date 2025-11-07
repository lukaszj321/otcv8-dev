---
doc_id: "cpp-api-87c163ef0f6a"
source_path: "framework/net/packet_recorder.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: packet_recorder.h"
summary: "Dokumentacja API C++ dla framework/net/packet_recorder.h"
tags: ["cpp", "api", "otclient"]
---

# framework/net/packet_recorder.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu packet_recorder.

## Classes/Structs

### Klasa: `PacketRecorder`

## Functions

### `addInputPacket`

**Sygnatura:** `void addInputPacket(const InputMessagePtr& packet)`

### `addOutputPacket`

**Sygnatura:** `void addOutputPacket(const OutputMessagePtr& packet)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    PacketRecorder["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>PacketRecorder</div><hr/>
            <b>Recording:</b><br/>
            + addInputPacket(packet)<br/>
            + addOutputPacket(packet)
        </div>
    "]:::netsec;
    
    InputMessage["InputMessage"]:::data
    OutputMessage["OutputMessage"]:::data
    RecordFile["Record File"]:::data
    
    PacketRecorder --> |"records"| InputMessage
    PacketRecorder --> |"records"| OutputMessage
    PacketRecorder --> |"saves to"| RecordFile
    
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

## Diagram: Packet Recording Flow

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant Protocol
    participant Recorder
    participant InputMsg
    participant OutputMsg
    participant File
    
    Note over Protocol,File: Recording Input Packets
    Protocol->>InputMsg: Receive Packet
    Protocol->>Recorder: addInputPacket(packet)
    Recorder->>File: Save Input Packet
    
    Note over Protocol,File: Recording Output Packets
    Protocol->>OutputMsg: Create Packet
    Protocol->>Recorder: addOutputPacket(packet)
    Recorder->>File: Save Output Packet
```
<!-- /mermaid-diagram -->

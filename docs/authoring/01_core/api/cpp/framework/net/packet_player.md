---
doc_id: "cpp-api-b3ae73a63415"
source_path: "framework/net/packet_player.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: packet_player.h"
summary: "Dokumentacja API C++ dla framework/net/packet_player.h"
tags: ["cpp", "api", "otclient"]
---

# framework/net/packet_player.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu packet_player.

## Classes/Structs

### Klasa: `PacketPlayer`

## Functions

### `start`

**Sygnatura:** `void start(std::function<void(std::shared_ptr<std::vector<uint8_t>>)> recvCallback, std::function<void(boost::system::error_code)> disconnectCallback)`

### `stop`

**Sygnatura:** `void stop()`

### `onOutputPacket`

**Sygnatura:** `void onOutputPacket(const OutputMessagePtr& packet)`

### `process`

**Sygnatura:** `void process()`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    PacketPlayer["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>PacketPlayer</div><hr/>
            <b>Control:</b><br/>
            + start(recvCallback, disconnectCallback)<br/>
            + stop()<br/>
            <b>Playback:</b><br/>
            + onOutputPacket(packet)<br/>
            + process()
        </div>
    "]:::netsec;
    
    RecordFile["Record File"]:::data
    InputMessage["InputMessage"]:::data
    OutputMessage["OutputMessage"]:::data
    
    PacketPlayer --> |"loads from"| RecordFile
    PacketPlayer --> |"plays"| InputMessage
    PacketPlayer --> |"plays"| OutputMessage
    
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

## Diagram: Packet Playback Flow

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant Player
    participant File
    participant Protocol
    participant Callback
    
    Note over Player,Callback: Playback Start
    Player->>File: Load Recorded Packets
    Player->>Player: start(callbacks)
    
    Note over Player,Callback: Playback Process
    loop For each packet
        Player->>File: Read Next Packet
        File-->>Player: Packet Data
        Player->>Protocol: onOutputPacket(packet)
        Player->>Callback: recvCallback(packet)
        Player->>Player: process()
    end
    
    Note over Player,Callback: Playback Stop
    Player->>Player: stop()
```
<!-- /mermaid-diagram -->

---
doc_id: "cpp-api-5dbd3875be0e"
source_path: "framework/net/protocol.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: protocol.h"
summary: "Dokumentacja API C++ dla framework/net/protocol.h"
tags: ["cpp", "api", "otclient"]
---

# framework/net/protocol.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu protocol.

## Classes/Structs

### Klasa: `Protocol`

| Member | Brief | Signature |
|--------|-------|-----------|
| `connect` |  | `void connect(const std::string& host, uint16 port)` |
| `disconnect` |  | `void disconnect()` |
| `setRecorder` |  | `void setRecorder(PacketRecorderPtr recorder)` |
| `playRecord` |  | `void playRecord(PacketPlayerPtr player)` |
| `isConnected` |  | `bool isConnected()` |
| `isConnecting` |  | `bool isConnecting()` |
| `getElapsedTicksSinceLastRead` |  | `ticks_t getElapsedTicksSinceLastRead() { return m_connection ? m_connection->getElapsedTicksSinceLastRead() : -1; }` |
| `getConnection` |  | `ConnectionPtr getConnection() { return m_connection; }` |
| `setConnection` |  | `void setConnection(const ConnectionPtr& connection) { m_connection = connection; }` |
| `generateXteaKey` |  | `void generateXteaKey()` |
| `setXteaKey` |  | `void setXteaKey(uint32 a, uint32 b, uint32 c, uint32 d)` |
| `getXteaKey` |  | `std::vector<uint32> getXteaKey()` |
| `enableXteaEncryption` |  | `void enableXteaEncryption() { m_xteaEncryptionEnabled = true; }` |
| `enableChecksum` |  | `void enableChecksum() { m_checksumEnabled = true; }` |
| `enabledSequencedPackets` |  | `void enabledSequencedPackets() { m_sequencedPackets = true; }` |
| `enableBigPackets` |  | `void enableBigPackets() { m_bigPackets = true; }` |
| `enableCompression` |  | `void enableCompression() { m_compression = true; }` |
| `send` |  | `virtual void send(const OutputMessagePtr& outputMessage, bool rawPacket = false)` |
| `recv` |  | `virtual void recv()` |
| `asProtocol` |  | `ProtocolPtr asProtocol() { return static_self_cast<Protocol>(); }` |
| `onConnect` |  | `virtual void onConnect()` |
| `onRecv` |  | `virtual void onRecv(const InputMessagePtr& inputMessage)` |
| `onError` |  | `virtual void onError(const boost::system::error_code& err)` |
| `onProxyPacket` |  | `void onProxyPacket(const std::shared_ptr<std::vector<uint8_t>>& packet)` |
| `onPlayerPacket` |  | `void onPlayerPacket(const std::shared_ptr<std::vector<uint8_t>>& packet)` |
| `onLocalDisconnected` |  | `void onLocalDisconnected(boost::system::error_code ec)` |
| `m_disconnected` |  | `bool m_disconnected = false` |
| `m_proxy` |  | `uint32_t m_proxy = 0` |
| `m_packetNumber` |  | `uint32 m_packetNumber` |
| `m_player` |  | `PacketPlayerPtr m_player` |
| `m_recorder` |  | `PacketRecorderPtr m_recorder` |

## Functions

### `connect`

**Sygnatura:** `void connect(const std::string& host, uint16 port)`

### `disconnect`

**Sygnatura:** `void disconnect()`

### `setRecorder`

**Sygnatura:** `void setRecorder(PacketRecorderPtr recorder)`

### `playRecord`

**Sygnatura:** `void playRecord(PacketPlayerPtr player)`

### `isConnected`

**Sygnatura:** `bool isConnected()`

### `isConnecting`

**Sygnatura:** `bool isConnecting()`

### `getElapsedTicksSinceLastRead`

**Sygnatura:** `ticks_t getElapsedTicksSinceLastRead() { return m_connection ? m_connection->getElapsedTicksSinceLastRead() : -1; }`

### `getConnection`

**Sygnatura:** `ConnectionPtr getConnection() { return m_connection; }`

### `setConnection`

**Sygnatura:** `void setConnection(const ConnectionPtr& connection) { m_connection = connection; }`

### `generateXteaKey`

**Sygnatura:** `void generateXteaKey()`

### `setXteaKey`

**Sygnatura:** `void setXteaKey(uint32 a, uint32 b, uint32 c, uint32 d)`

### `getXteaKey`

**Sygnatura:** `std::vector<uint32> getXteaKey()`

### `enableXteaEncryption`

**Sygnatura:** `void enableXteaEncryption() { m_xteaEncryptionEnabled = true; }`

### `enableChecksum`

**Sygnatura:** `void enableChecksum() { m_checksumEnabled = true; }`

### `enabledSequencedPackets`

**Sygnatura:** `void enabledSequencedPackets() { m_sequencedPackets = true; }`

### `enableBigPackets`

**Sygnatura:** `void enableBigPackets() { m_bigPackets = true; }`

### `enableCompression`

**Sygnatura:** `void enableCompression() { m_compression = true; }`

### `asProtocol`

**Sygnatura:** `ProtocolPtr asProtocol() { return static_self_cast<Protocol>(); }`

### `onProxyPacket`

**Sygnatura:** `void onProxyPacket(const std::shared_ptr<std::vector<uint8_t>>& packet)`

### `onPlayerPacket`

**Sygnatura:** `void onPlayerPacket(const std::shared_ptr<std::vector<uint8_t>>& packet)`

### `onLocalDisconnected`

**Sygnatura:** `void onLocalDisconnected(boost::system::error_code ec)`

### `internalRecvHeader`

**Sygnatura:** `void internalRecvHeader(uint8* buffer, uint32 size)`

### `internalRecvData`

**Sygnatura:** `void internalRecvData(uint8* buffer, uint32 size)`

### `xteaDecrypt`

**Sygnatura:** `bool xteaDecrypt(const InputMessagePtr& inputMessage)`

### `xteaEncrypt`

**Sygnatura:** `void xteaEncrypt(const OutputMessagePtr& outputMessage)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    Protocol["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>Protocol</div><hr/>
            <b>Connection:</b><br/>
            + connect(host, port)<br/>
            + disconnect()<br/>
            + isConnected()<br/>
            <b>I/O:</b><br/>
            + send(outputMessage)<br/>
            + recv()<br/>
            <b>Encryption:</b><br/>
            + generateXteaKey()<br/>
            + setXteaKey(a, b, c, d)<br/>
            + enableXteaEncryption()<br/>
            <b>Features:</b><br/>
            + enableChecksum()<br/>
            + enableCompression()<br/>
            + enabledSequencedPackets()<br/>
            <b>Recording:</b><br/>
            + setRecorder(recorder)<br/>
            + playRecord(player)
        </div>
    "]:::netsec;
    
    Connection["Connection"]:::netsec
    OutputMessage["OutputMessage"]:::data
    InputMessage["InputMessage"]:::data
    PacketRecorder["PacketRecorder"]:::data
    PacketPlayer["PacketPlayer"]:::data
    
    Protocol --> |"uses"| Connection
    Protocol --> |"creates"| OutputMessage
    Protocol --> |"receives"| InputMessage
    Protocol --> |"records"| PacketRecorder
    Protocol --> |"plays"| PacketPlayer
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

## Diagram: Protocol Communication Flow

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant App
    participant Protocol
    participant Connection
    participant Server
    
    Note over App,Server: Connection Phase
    App->>Protocol: connect(host, port)
    Protocol->>Connection: connect(host, port)
    Connection->>Server: TCP Connect
    Server-->>Connection: Connection Established
    Connection-->>Protocol: onConnect()
    Protocol->>Protocol: generateXteaKey()
    Protocol-->>App: onConnect()
    
    Note over App,Server: Sending Data
    App->>Protocol: send(outputMessage)
    Protocol->>Protocol: xteaEncrypt()
    Protocol->>Protocol: addChecksum()
    Protocol->>Connection: write(buffer)
    Connection->>Server: Send Packet
    
    Note over App,Server: Receiving Data
    Server->>Connection: Receive Packet
    Connection->>Protocol: onRecv()
    Protocol->>Protocol: verifyChecksum()
    Protocol->>Protocol: xteaDecrypt()
    Protocol->>Protocol: onRecv(inputMessage)
    Protocol-->>App: onRecv(inputMessage)
```
<!-- /mermaid-diagram -->

---
doc_id: "cpp-api-e1dc74da055a"
source_path: "framework/net/outputmessage.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: outputmessage.h"
summary: "Dokumentacja API C++ dla framework/net/outputmessage.h"
tags: ["cpp", "api", "otclient"]
---

# framework/net/outputmessage.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu outputmessage.

## Classes/Structs

### Klasa: `OutputMessage`

| Member | Brief | Signature |
|--------|-------|-----------|
| `reset` |  | `void reset()` |
| `setBuffer` |  | `void setBuffer(const std::string& buffer)` |
| `getBuffer` |  | `std::string getBuffer() { return std::string((char*)m_buffer + m_headerPos, m_messageSize); }` |
| `addU8` |  | `void addU8(uint8 value)` |
| `addU16` |  | `void addU16(uint16 value)` |
| `addU32` |  | `void addU32(uint32 value)` |
| `addU64` |  | `void addU64(uint64 value)` |
| `addString` |  | `void addString(const std::string& buffer)` |
| `addRawString` |  | `void addRawString(const std::string& buffer)` |
| `addPaddingBytes` |  | `void addPaddingBytes(int bytes, uint8 byte = 0)` |
| `encryptRsa` |  | `void encryptRsa()` |
| `getWritePos` |  | `uint32 getWritePos() { return m_writePos; }` |
| `getMessageSize` |  | `uint32 getMessageSize() { return m_messageSize; }` |
| `setWritePos` |  | `void setWritePos(uint32 writePos) { m_writePos = writePos; }` |
| `setMessageSize` |  | `void setMessageSize(uint32 messageSize) { m_messageSize = messageSize; }` |
| `writeChecksum` |  | `void writeChecksum()` |
| `writeSequence` |  | `void writeSequence(uint32_t sequence)` |
| `writeMessageSize` |  | `void writeMessageSize(bool bigSize)` |

## Functions

### `reset`

**Sygnatura:** `void reset()`

### `setBuffer`

**Sygnatura:** `void setBuffer(const std::string& buffer)`

### `getBuffer`

**Sygnatura:** `std::string getBuffer() { return std::string((char*)m_buffer + m_headerPos, m_messageSize); }`

### `addU8`

**Sygnatura:** `void addU8(uint8 value)`

### `addU16`

**Sygnatura:** `void addU16(uint16 value)`

### `addU32`

**Sygnatura:** `void addU32(uint32 value)`

### `addU64`

**Sygnatura:** `void addU64(uint64 value)`

### `addString`

**Sygnatura:** `void addString(const std::string& buffer)`

### `addRawString`

**Sygnatura:** `void addRawString(const std::string& buffer)`

### `addPaddingBytes`

**Sygnatura:** `void addPaddingBytes(int bytes, uint8 byte = 0)`

### `encryptRsa`

**Sygnatura:** `void encryptRsa()`

### `getWritePos`

**Sygnatura:** `uint32 getWritePos() { return m_writePos; }`

### `getMessageSize`

**Sygnatura:** `uint32 getMessageSize() { return m_messageSize; }`

### `setWritePos`

**Sygnatura:** `void setWritePos(uint32 writePos) { m_writePos = writePos; }`

### `setMessageSize`

**Sygnatura:** `void setMessageSize(uint32 messageSize) { m_messageSize = messageSize; }`

### `writeChecksum`

**Sygnatura:** `void writeChecksum()`

### `writeSequence`

**Sygnatura:** `void writeSequence(uint32_t sequence)`

### `writeMessageSize`

**Sygnatura:** `void writeMessageSize(bool bigSize)`

### `canWrite`

**Sygnatura:** `bool canWrite(int bytes)`

### `checkWrite`

**Sygnatura:** `void checkWrite(int bytes)`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    OutputMessage["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>OutputMessage</div><hr/>
            <b>Buffer Management:</b><br/>
            + reset()<br/>
            + setBuffer(buffer)<br/>
            + getBuffer()<br/>
            <b>Writing Primitives:</b><br/>
            + addU8(value)<br/>
            + addU16(value)<br/>
            + addU32(value)<br/>
            + addU64(value)<br/>
            + addString(buffer)<br/>
            + addRawString(buffer)<br/>
            <b>Position Control:</b><br/>
            + setWritePos(pos)<br/>
            + setMessageSize(size)<br/>
            <b>Message Building:</b><br/>
            + writeMessageSize(bigSize)<br/>
            + writeChecksum()<br/>
            + writeSequence(sequence)<br/>
            <b>Security:</b><br/>
            + encryptRsa()<br/>
            + addPaddingBytes(bytes)
        </div>
    "]:::netsec;
    
    Buffer["Buffer<br/>m_buffer"]:::data
    
    OutputMessage --> |"contains"| Buffer
    
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->

## Diagram: OutputMessage Packet Structure

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
packet-beta
    0,16,Header Space (reserved for Length)
    16,24,Opcode (1 byte)
    24,32,Sequence (optional, 4 bytes)
    32,64,Payload Data (variable)
    64,96,Checksum (optional, 4 bytes)
```
<!-- /mermaid-diagram -->

## Diagram: Message Serialization Flow

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
flowchart LR
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    App["Application"]:::core
    OutputMsg["OutputMessage<br/>addU8/U16/U32/String"]:::netsec
    Build["Build Packet<br/>writeMessageSize<br/>writeChecksum"]:::netsec
    Encrypt["Encrypt<br/>encryptRsa<br/>xteaEncrypt"]:::netsec
    Send["Send to<br/>Connection"]:::netsec
    
    App --> |"create"| OutputMsg
    OutputMsg --> |"finalize"| Build
    Build --> |"secure"| Encrypt
    Encrypt --> |"transmit"| Send
    
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->

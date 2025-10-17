---
doc_id: "05_network"
source_path: "docs/authoring/05_network/index.md"
source_sha: "latest"
last_sync_iso: "2025-10-17T23:34:49Z"
doc_class: "guide"
language: "pl"
title: "Network Protocol"
summary: "Network communication protocol, packet structure, and TFS extended opcode"
tags: ["network", "protocol", "tfs", "communication"]
---

# Network Protocol

## Overview

The OTClient v8 network subsystem provides robust, secure communication between the client and game server. 
It implements a custom protocol based on XTEA encryption and supports extended opcodes for custom functionality.

## Protocol Architecture

The network protocol is built on several key layers:

1. **Transport Layer**: TCP/IP socket communication
2. **Encryption Layer**: XTEA cipher for packet encryption
3. **Protocol Layer**: Packet structure and opcode handling
4. **Application Layer**: Game-specific message handling

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
    participant Client
    participant Socket
    participant Protocol
    participant Server
    
    Client->>Socket: Connect
    Socket->>Server: TCP Handshake
    Server-->>Socket: Accept
    Socket-->>Client: Connected
    Client->>Protocol: Authenticate
    Protocol->>Server: Login Packet
    Server-->>Protocol: Character List
    Protocol-->>Client: Available Characters
    Client->>Protocol: Select Character
    Protocol->>Server: Enter Game
    Server-->>Protocol: Game World Data
    loop Game Loop
        Client->>Protocol: Player Actions
        Protocol->>Server: Action Packets
        Server-->>Protocol: World Updates
        Protocol-->>Client: Render Updates
    end
```

## Packet Structure

### Standard Packet Format

Every packet follows this structure:

```
[Size: 2 bytes][Checksum: 4 bytes][Encrypted Payload]
```

**Payload Structure:**
```
[Opcode: 1 byte][Data: N bytes]
```

### Encryption

Packets are encrypted using XTEA (eXtended Tiny Encryption Algorithm) with a 128-bit key.

**XTEA Parameters:**
- Block size: 64 bits (8 bytes)
- Key size: 128 bits (16 bytes)
- Rounds: 32

## Core Opcodes

### Client-to-Server Opcodes

| Opcode | Name | Description |
|--------|------|-------------|
| 0x0A | LoginServer | Login to server |
| 0x14 | EnterGame | Enter game world |
| 0x64 | Walk | Player movement |
| 0x65 | WalkNorth | Move north |
| 0x66 | WalkEast | Move east |
| 0x67 | WalkSouth | Move south |
| 0x68 | WalkWest | Move west |
| 0x78 | Talk | Send chat message |
| 0x82 | UseItem | Use item |
| 0x96 | RequestTrade | Initiate trade |

### Server-to-Client Opcodes

| Opcode | Name | Description |
|--------|------|-------------|
| 0x0A | LoginSuccess | Login successful |
| 0x14 | CharacterList | Available characters |
| 0x64 | MapDescription | Map tile data |
| 0x6D | TextMessage | Text message |
| 0x78 | CreatureSay | Creature speech |
| 0x8C | ContainerOpen | Open container |
| 0xA0 | Stats | Player statistics |

## TFS Extended Opcode

The TFS (The Forgotten Server) extended opcode system allows custom client-server communication.

### Patch Details

The extended opcode patch adds support for custom opcodes beyond the standard protocol.

**File:** `_static/patches/tfs_extendedopcode.diff`

**Key Changes:**
1. Adds `CREATURE_EVENT_EXTENDED_OPCODE` event type
2. Implements `onExtendedOpcode` callback
3. Supports custom opcode routing

### Extended Opcode Structure

```
[Opcode: 0x32][Custom Opcode: 1 byte][Buffer: N bytes]
```

**Example Usage:**

```lua
-- Server-side (TFS)
function onExtendedOpcode(player, opcode, buffer)
    if opcode == 1 then
        -- Custom handler for opcode 1
        player:sendTextMessage(MESSAGE_INFO, "Extended opcode received: " .. buffer)
    end
end
```

```lua
-- Client-side (OTClient)
function sendExtendedOpcode(opcode, buffer)
    local protocol = g_game.getProtocolGame()
    if protocol then
        protocol:sendExtendedOpcode(opcode, buffer)
    end
end
```

### Security Considerations

**Risks:**
- Extended opcodes bypass standard protocol validation
- Potential for buffer overflow if not properly validated
- Can be used for cheating if not properly secured

**Mitigations:**
1. Validate all buffer data on server side
2. Implement rate limiting for custom opcodes
3. Log all extended opcode usage
4. Use checksums for critical data

## Connection Flow

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
stateDiagram-v2
    [*] --> Disconnected
    Disconnected --> Connecting: connect()
    Connecting --> Authenticating: TCP established
    Authenticating --> CharacterSelection: credentials valid
    Authenticating --> Disconnected: auth failed
    CharacterSelection --> EnteringGame: select character
    CharacterSelection --> Disconnected: logout
    EnteringGame --> InGame: world loaded
    InGame --> Disconnected: disconnect
    InGame --> InGame: playing
```

## Protocol Classes

### ProtocolGame

Main protocol handler for game communication.

**Key Methods:**
- `connect()`: Establish connection
- `login()`: Authenticate user
- `logout()`: Disconnect cleanly
- `sendPacket()`: Send raw packet
- `receivePacket()`: Receive and parse packet

### InputMessage / OutputMessage

Buffer classes for packet serialization.

**InputMessage Methods:**
- `getByte()`: Read 1 byte
- `getU16()`: Read 2 bytes (unsigned)
- `getU32()`: Read 4 bytes (unsigned)
- `getString()`: Read length-prefixed string

**OutputMessage Methods:**
- `addByte()`: Write 1 byte
- `addU16()`: Write 2 bytes (unsigned)
- `addU32()`: Write 4 bytes (unsigned)
- `addString()`: Write length-prefixed string

## Error Handling

### Connection Errors

- **Timeout**: Connection attempt exceeds timeout limit
- **Refused**: Server actively refused connection
- **Reset**: Connection reset by peer
- **Lost**: Connection unexpectedly dropped

### Protocol Errors

- **Invalid Packet**: Malformed packet structure
- **Checksum Mismatch**: Packet integrity check failed
- **Unknown Opcode**: Unsupported opcode received
- **Decryption Failed**: Unable to decrypt packet

## Performance Optimization

### Packet Batching

Multiple small packets can be batched into a single TCP send operation to reduce overhead.

### Compression

Large packets (e.g., map data) can be compressed using zlib to reduce bandwidth.

### Priority Queuing

Critical packets (e.g., player movement) are prioritized over non-critical packets (e.g., outfit changes).

## Debugging

### Packet Logging

Enable packet logging to diagnose protocol issues:

```lua
g_network:setPacketLogging(true)
```

### Protocol Analyzer

Use Wireshark with custom dissector to analyze OTClient protocol traffic.

## Related Chapters

- [Core](../01_core/index.md) - Core C++ API
- [Events](../02_events/index.md) - Event system
- [Settings & Crypto](../07_settings_crypto/index.md) - Encryption settings

## Appendix / Facets

(facet-05_network.protocol_flow)=
### Facet: `05_network.protocol_flow`
Network protocol flow and packet structure diagrams.

(facet-05_network.extended_opcode)=
### Facet: `05_network.extended_opcode`
TFS extended opcode implementation and security considerations.

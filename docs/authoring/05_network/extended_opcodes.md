# Extended Opcodes Usage Patterns

## Overview

Extended opcodes provide a custom communication channel between client and server beyond the standard Tibia protocol. This enables server-specific features, bot integration, and custom UI elements.

## Registration

### Client-Side Registration

```cpp
// Register for extended opcodes on connection
void ProtocolGame::onConnect() {
    // Send registration packet
    OutputMessagePtr msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientOpcodes::ExtendedOpcode);
    msg->addU8(0x00);  // Opcode 0 = Register
    msg->addString(""); // Empty buffer for registration
    send(msg);
}
```

### Server-Side Handler (TFS)

```lua
-- data/events/scripts/player.lua

function Player.onExtendedOpcode(player, opcode, buffer)
    if opcode == 0 then
        -- Client registered for extended opcodes
        player:sendExtendedOpcode(0, "OK")
        return true
    end
    
    -- Handle custom opcodes
    return handleCustomOpcode(player, opcode, buffer)
end
```

## Common Use Cases

### 1. Server Information

**Opcode 1**: Server info and features

```lua
-- Server (TFS)
function sendServerInfo(player)
    local info = {
        name = "My OT Server",
        version = "1.0",
        features = {"market", "prey", "stash"}
    }
    
    player:sendExtendedOpcode(1, json.encode(info))
end
```

```cpp
// Client
void handleServerInfo(const std::string& buffer) {
    json data = json::parse(buffer);
    
    std::string name = data["name"];
    std::string version = data["version"];
    std::vector<std::string> features = data["features"];
    
    g_logger.info("Server: %s v%s", name.c_str(), version.c_str());
    g_game.setServerFeatures(features);
}
```

### 2. Custom UI Updates

**Opcode 2**: Update custom UI elements

```lua
-- Server
function updateCustomUI(player)
    local data = {
        type = "health_bar",
        value = player:getHealth(),
        max = player:getMaxHealth()
    }
    
    player:sendExtendedOpcode(2, json.encode(data))
end
```

```cpp
// Client
void handleUIUpdate(const std::string& buffer) {
    json data = json::parse(buffer);
    
    std::string type = data["type"];
    
    if (type == "health_bar") {
        int value = data["value"];
        int max = data["max"];
        g_ui.updateHealthBar(value, max);
    }
}
```

### 3. Bot Commands

**Opcode 10**: Bot control messages

```lua
-- Server
function onBotCommand(player, buffer)
    local cmd = json.decode(buffer)
    
    if cmd.action == "start" then
        player:setBotEnabled(true)
        player:sendExtendedOpcode(10, json.encode({status = "started"}))
    elseif cmd.action == "stop" then
        player:setBotEnabled(false)
        player:sendExtendedOpcode(10, json.encode({status = "stopped"}))
    end
end
```

```cpp
// Client - Send command
void sendBotCommand(const std::string& action) {
    json data = {
        {"action", action}
    };
    
    OutputMessagePtr msg = std::make_shared<OutputMessage>();
    msg->addU8(Proto::ClientOpcodes::ExtendedOpcode);
    msg->addU8(10);
    msg->addString(data.dump());
    g_game.getProtocolGame()->send(msg);
}

// Client - Handle response
void handleBotResponse(const std::string& buffer) {
    json data = json::parse(buffer);
    std::string status = data["status"];
    
    g_logger.info("Bot %s", status.c_str());
}
```

### 4. Quest/Task System

**Opcode 20**: Quest updates

```lua
-- Server
function updateQuests(player)
    local quests = {}
    
    for _, quest in ipairs(player:getActiveQuests()) do
        table.insert(quests, {
            id = quest:getId(),
            name = quest:getName(),
            progress = quest:getProgress(),
            complete = quest:isComplete()
        })
    end
    
    player:sendExtendedOpcode(20, json.encode({quests = quests}))
end
```

```cpp
// Client
void handleQuestUpdate(const std::string& buffer) {
    json data = json::parse(buffer);
    
    for (auto& quest : data["quests"]) {
        int id = quest["id"];
        std::string name = quest["name"];
        int progress = quest["progress"];
        bool complete = quest["complete"];
        
        g_game.updateQuest(id, name, progress, complete);
    }
}
```

## Data Formats

### JSON (Recommended)

```cpp
// Advantages: Flexible, human-readable, widely supported
json data = {
    {"type", "update"},
    {"values", {1, 2, 3}},
    {"nested", {{"key", "value"}}}
};

std::string buffer = data.dump();
```

### Binary (For Performance)

```cpp
// Advantages: Compact, fast, no parsing overhead
OutputMessagePtr msg = std::make_shared<OutputMessage>();
msg->addU8(10);  // Extended opcode
msg->addU8(1);   // Sub-type
msg->addU32(1000);  // Value 1
msg->addU32(2000);  // Value 2
msg->addString("data");
```

### Plain Text (For Simplicity)

```cpp
// Advantages: Simple, no dependencies
std::string buffer = "action:update;value:100";
```

## Best Practices

### 1. Version Your Protocol

```lua
-- Server
function sendData(player, data)
    local packet = {
        version = 1,
        data = data
    }
    player:sendExtendedOpcode(99, json.encode(packet))
end
```

```cpp
// Client
void handleData(const std::string& buffer) {
    json packet = json::parse(buffer);
    int version = packet["version"];
    
    if (version == 1) {
        handleDataV1(packet["data"]);
    } else {
        g_logger.warning("Unknown protocol version: %d", version);
    }
}
```

### 2. Handle Errors Gracefully

```cpp
void parseExtendedOpcode(InputMessagePtr msg) {
    uint8_t opcode = msg->getU8();
    std::string buffer = msg->getString();
    
    try {
        switch (opcode) {
            case 1:
                handleServerInfo(buffer);
                break;
            case 2:
                handleUIUpdate(buffer);
                break;
            default:
                g_logger.warning("Unknown opcode: %d", opcode);
        }
    } catch (const std::exception& e) {
        g_logger.error("Extended opcode error: %s", e.what());
    }
}
```

### 3. Rate Limiting

```lua
-- Server
local lastOpcode = {}

function Player.onExtendedOpcode(player, opcode, buffer)
    local now = os.time()
    local playerId = player:getId()
    
    -- Rate limit: 1 opcode per second
    if lastOpcode[playerId] and (now - lastOpcode[playerId]) < 1 then
        player:sendCancelMessage("Too many requests")
        return false
    end
    
    lastOpcode[playerId] = now
    return handleOpcode(player, opcode, buffer)
end
```

### 4. Validate Input

```lua
-- Server
function handleBotCommand(player, buffer)
    local success, data = pcall(json.decode, buffer)
    
    if not success then
        player:sendCancelMessage("Invalid JSON")
        return false
    end
    
    if type(data.action) ~= "string" then
        player:sendCancelMessage("Invalid action")
        return false
    end
    
    -- Process command
    processBotCommand(player, data)
end
```

## Security Considerations

### 1. Sanitize Input

```lua
function sanitizeString(str)
    -- Remove control characters
    str = str:gsub("[%z\1-\31]", "")
    
    -- Limit length
    if #str > 1000 then
        str = str:sub(1, 1000)
    end
    
    return str
end
```

### 2. Authenticate Actions

```lua
function handleAdminCommand(player, data)
    -- Verify admin status
    if not player:getGroup():getAccess() then
        player:sendCancelMessage("Access denied")
        return false
    end
    
    -- Process admin command
    processAdminCommand(player, data)
end
```

### 3. Log Suspicious Activity

```lua
function Player.onExtendedOpcode(player, opcode, buffer)
    -- Log all extended opcodes
    logger.info(string.format(
        "ExtendedOpcode: player=%s opcode=%d size=%d",
        player:getName(), opcode, #buffer
    ))
    
    return handleOpcode(player, opcode, buffer)
end
```

## Debugging

### Client-Side Logger

```cpp
void logExtendedOpcode(uint8_t opcode, const std::string& buffer) {
    std::cout << "Extended Opcode Received:" << std::endl;
    std::cout << "  Opcode: " << (int)opcode << std::endl;
    std::cout << "  Size: " << buffer.size() << std::endl;
    std::cout << "  Data: " << buffer << std::endl;
}
```

### Server-Side Logger

```lua
function Player.onExtendedOpcode(player, opcode, buffer)
    print(string.format(
        "[ExtendedOpcode] Player: %s, Opcode: %d, Buffer: %s",
        player:getName(), opcode, buffer
    ))
    
    return handleOpcode(player, opcode, buffer)
end
```

## See Also

- [Protocol Versions](./protocol_versions.md)
- [Packet Structure](./packet_structure.md)
- [TFS Extended Opcode Patch](./appendix_tfs_extendedopcode.md)
- [Bot Integration](../03_modules/lua/game_bot/bot.md)

## Diagram: Extended Opcode Packet Structure

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
packet-beta
    0,8,Extended Opcode (1 byte)
    8,16,Sub-opcode (1 byte)
    16,32,Data Length (2 bytes)
    32,64,Data Buffer (variable, JSON/Text/Binary)
```
<!-- /mermaid-diagram -->

## Diagram: Extended Opcodes Flow

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant Client
    participant Protocol
    participant Server
    participant Handler
    
    Note over Client,Handler: Registration Phase
    Client->>Protocol: ExtendedOpcode(0, "")
    Protocol->>Server: Send Registration
    Server->>Handler: onExtendedOpcode(0, "")
    Handler->>Server: sendExtendedOpcode(0, "OK")
    Server->>Protocol: Response
    Protocol->>Client: Registration Confirmed
    
    Note over Client,Handler: Custom Opcode Usage
    Client->>Protocol: ExtendedOpcode(opcode, data)
    Protocol->>Server: Send Custom Opcode
    Server->>Handler: onExtendedOpcode(opcode, buffer)
    Handler->>Handler: Process Custom Logic
    Handler->>Server: sendExtendedOpcode(opcode, response)
    Server->>Protocol: Response
    Protocol->>Client: Handle Response
```
<!-- /mermaid-diagram -->

## Diagram: Extended Opcodes Use Cases

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
flowchart TD
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef module fill:#24343a,stroke:#8fa2a8,color:#ddd,stroke-width:1px;
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    
    ExtendedOpcode["Extended Opcode<br/>System"]:::netsec
    
    ServerInfo["Opcode 1<br/>Server Info"]:::module
    UIUpdate["Opcode 2<br/>UI Updates"]:::ui
    BotControl["Opcode 10<br/>Bot Commands"]:::module
    QuestSystem["Opcode 20<br/>Quest Updates"]:::module
    
    ExtendedOpcode --> ServerInfo
    ExtendedOpcode --> UIUpdate
    ExtendedOpcode --> BotControl
    ExtendedOpcode --> QuestSystem
    
    ServerInfo --> |"JSON: name, version, features"| ClientApp["Client<br/>Application"]:::core
    UIUpdate --> |"JSON: type, value, max"| UIComponents["UI<br/>Components"]:::ui
    BotControl --> |"JSON: action, status"| BotModule["Bot<br/>Module"]:::module
    QuestSystem --> |"JSON: quests array"| GameLogic["Game<br/>Logic"]:::core
    
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef module fill:#24343a,stroke:#8fa2a8,color:#ddd,stroke-width:1px;
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
```
<!-- /mermaid-diagram -->

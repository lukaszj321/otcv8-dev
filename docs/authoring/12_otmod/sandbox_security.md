# Sandbox Security in OTMOD

## Overview

OTClient v8 implements a **sandboxed Lua environment** for OTMOD modules to ensure security and prevent malicious code execution. Each module runs in an isolated environment with controlled access to system resources.

## Sandbox Architecture

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[User Module] --> B[Sandbox Layer]
    B --> C{Permission Check}
    C -->|Allowed| D[Safe API]
    C -->|Blocked| E[Access Denied]
    D --> F[Core Functions]
    D --> G[File I/O Restricted]
    D --> H[Network Restricted]
    
    style B fill:#6a4,stroke:#8c6,stroke-width:2px
    style C fill:#a64,stroke:#c86,stroke-width:2px
    style E fill:#a44,stroke:#c66,stroke-width:2px
```

## Sandboxed vs. Non-Sandboxed Modules

### Non-Sandboxed (System Modules)

Core OTClient modules run with full privileges:

```lua
Module
  name: corelib
  description: Core library with system access
  sandboxed: false  // Full access to all Lua features
  
  @onLoad: init.lua
end
```

**Capabilities:**
- Direct file system access (`io.*`, `os.*`)
- Loading C libraries (`require`, `package.loadlib`)
- Full OS interaction
- Direct memory manipulation

### Sandboxed (User Modules)

User-created modules run in restricted environment:

```lua
Module
  name: my_custom_module
  description: User module with sandbox restrictions
  sandboxed: true  // Default, can be omitted
  
  @onLoad: init.lua
end
```

**Restrictions:**
- No `io.*` library access
- No `os.execute()`, `os.exit()`, `os.remove()`
- No `package.loadlib()`
- No `debug.*` library
- Limited `os.*` functions (only safe ones like `os.time()`, `os.date()`)

## Safe API Functions

Sandboxed modules have access to approved APIs:

### File Operations (Controlled)

```lua
-- Use g_resources for file access (sandboxed)
local content = g_resources.readFileContents('/modules/my_module/data.txt')

-- Direct io.* is blocked
-- local file = io.open('file.txt') -- ERROR: io is nil

-- Use g_configs for configuration
local config = g_configs.create('/my_module_config.otml')
config:set('setting', 'value')
config:save()
```

### Network Operations (Controlled)

```lua
-- Use g_http for HTTP requests (sandboxed)
g_http.get('https://api.example.com/data', function(data, error)
  if error then
    g_logger.error('HTTP error: ' .. error)
    return
  end
  
  processData(data)
end)

-- Direct socket access is blocked
-- local socket = require('socket') -- ERROR: blocked
```

### System Information (Limited)

```lua
-- Safe OS functions
local timestamp = os.time()
local dateStr = os.date('%Y-%m-%d')
local clock = os.clock()

-- Blocked OS functions
-- os.execute('ls') -- ERROR: blocked
-- os.exit(0) -- ERROR: blocked
-- os.remove('file.txt') -- ERROR: blocked
```

## Bypassing Sandbox (Advanced)

### Declaring Privileged Access

For trusted modules that require system access:

```lua
Module
  name: admin_tools
  description: Administrative tools requiring system access
  sandboxed: false
  author: TrustedDeveloper
  
  // Explicit permission declarations
  permissions: file_write, network_raw, system_exec
  
  @onLoad: init.lua
end
```

**Warning**: Only use `sandboxed: false` for:
- Official OTClient modules
- Thoroughly audited admin tools
- Development/debugging modules (never in production)

### Security Audit Checklist

Before marking a module as `sandboxed: false`:

- [ ] Code reviewed by trusted developer
- [ ] No user input passed to `os.execute()` or `io.popen()`
- [ ] File paths validated and sanitized
- [ ] Network operations use HTTPS with certificate validation
- [ ] No sensitive data logged or exposed
- [ ] Module signed by trusted developer

## Common Security Patterns

### 1. Input Validation

Always validate user input before processing:

```lua
function processUserInput(text)
  -- Validate length
  if #text > 1000 then
    g_logger.warning('Input too long, truncating')
    text = text:sub(1, 1000)
  end
  
  -- Sanitize special characters
  text = text:gsub('[<>&"\']', function(c)
    return string.format('&#%d;', string.byte(c))
  end)
  
  -- Process sanitized input
  return processText(text)
end
```

### 2. Resource Path Validation

Ensure file paths stay within module directory:

```lua
function loadModuleFile(filename)
  -- Block directory traversal
  if filename:find('%.%.') then
    g_logger.error('Invalid path: directory traversal detected')
    return nil
  end
  
  -- Construct safe path
  local modulePath = g_resources.getModuleDirectory('my_module')
  local fullPath = modulePath .. '/' .. filename
  
  -- Verify path is within module directory
  if not fullPath:startsWith(modulePath) then
    g_logger.error('Path outside module directory')
    return nil
  end
  
  return g_resources.readFileContents(fullPath)
end
```

### 3. API Rate Limiting

Prevent abuse of network APIs:

```lua
local apiCalls = {}
local RATE_LIMIT = 10 -- max calls per minute
local WINDOW = 60000 -- 1 minute in milliseconds

function callAPI(endpoint)
  local now = os.time()
  
  -- Clean old entries
  for i = #apiCalls, 1, -1 do
    if now - apiCalls[i] > WINDOW then
      table.remove(apiCalls, i)
    end
  end
  
  -- Check rate limit
  if #apiCalls >= RATE_LIMIT then
    g_logger.warning('API rate limit exceeded')
    return false
  end
  
  -- Record call
  table.insert(apiCalls, now)
  
  -- Make API call
  g_http.get(endpoint, onResponse)
  return true
end
```

### 4. Event Handler Validation

Validate event data before processing:

```lua
function onCreatureSpeak(creature, level, type, message)
  -- Validate creature exists
  if not creature or not creature:isValid() then
    return
  end
  
  -- Validate message length
  if #message > 255 then
    message = message:sub(1, 255)
  end
  
  -- Validate message type
  local validTypes = {
    [MessageTypes.Say] = true,
    [MessageTypes.Yell] = true,
    [MessageTypes.Whisper] = true
  }
  
  if not validTypes[type] then
    g_logger.warning('Invalid message type: ' .. type)
    return
  end
  
  -- Process validated data
  processSpeech(creature, message, type)
end
```

## Security Best Practices

### 1. Principle of Least Privilege

Request only necessary permissions:

```lua
-- BAD: Requesting unnecessary system access
Module
  sandboxed: false  // Full access when not needed
end

-- GOOD: Use sandbox with approved APIs
Module
  sandboxed: true  // Default safe mode
end
```

### 2. Data Sanitization

Never trust external data:

```lua
function handleNetworkData(packet)
  -- Validate packet structure
  if type(packet) ~= 'table' then
    return
  end
  
  -- Sanitize each field
  local safeData = {
    id = tonumber(packet.id) or 0,
    name = tostring(packet.name):sub(1, 50),
    level = math.max(1, math.min(1000, tonumber(packet.level) or 1))
  }
  
  processData(safeData)
end
```

### 3. Error Handling

Prevent information leakage through errors:

```lua
function loadSensitiveData()
  local success, result = pcall(function()
    return internalLoadFunction()
  end)
  
  if not success then
    -- Don't expose internal error details
    g_logger.error('Failed to load data')
    return nil
  end
  
  return result
end
```

### 4. Secure Configuration

Store sensitive data securely:

```lua
-- BAD: Hardcoded credentials
local API_KEY = "secret_key_12345"

-- GOOD: Use encrypted config
local config = g_configs.create('/my_module_secure.otml')
local apiKey = config:get('api_key')  -- Encrypted storage

if not apiKey then
  -- Prompt user for key
  apiKey = promptForAPIKey()
  config:set('api_key', apiKey)
  config:save()
end
```

## Vulnerability Testing

### Common Attack Vectors

1. **Path Traversal**: `../../etc/passwd`
2. **Command Injection**: `; rm -rf /`
3. **Script Injection**: `<script>alert('xss')</script>`
4. **SQL Injection**: `' OR '1'='1`
5. **Buffer Overflow**: Extremely long strings

### Testing Checklist

- [ ] Path traversal attempts blocked
- [ ] Special characters sanitized
- [ ] Input length limits enforced
- [ ] API rate limiting works
- [ ] Error messages don't leak internal info
- [ ] Module can't access files outside its directory
- [ ] Network requests use secure protocols

## Module Signing (Future)

Planned security feature for OTClient v8:

```lua
Module
  name: verified_module
  author: TrustedDeveloper
  signature: SHA256:abc123...
  certificate: /certs/trusted_dev.pem
end
```

This will enable:
- Verified author identity
- Tamper detection
- Trust levels (official, community, untrusted)
- Automatic security warnings

## See Also

- [Load-Later Patterns](./load_later_patterns.md)
- [Module Dependencies](./module_dependencies.md)
- [Lua API Reference](../03_modules/index.md)
- [Security Best Practices](../01_core/security.md)

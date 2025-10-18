---
title: 05_events - Events
---

# 05_events - Events

Extended event system documentation covering additional event handlers, emitters, and signal processing mechanisms.

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### entities
*Facet:* [`05_events.entities`](#facet-05_events.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### events_details
*Facet:* [`05_events.events_details`](#facet-05_events.events_details)

```{csv-table} events_details
:header-rows: 1
:file: ./datasets/events_details.csv
:widths: auto
```

### summary
*Facet:* [`05_events.summary`](#facet-05_events.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`05_events.architecture`](#facet-05_events.architecture)

```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Event Details
        E0[Event Patterns]
        E1[Event Chains]
        E2[Event Handlers]
        E0 --> E1
        E1 --> E2
    end
```

### events_overview
*Facet:* [`05_events.events_overview`](#facet-05_events.events_overview)

```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  EventOverview[05_events:events_overview] --> Data[Datasets]
  Data --> Page[Index]

click EventOverview "./index.html#facet-05_events.events_overview" "Open events_overview"
```

### flow
*Facet:* [`05_events.flow`](#facet-05_events.flow)

```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Event Details] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```





## Appendix / Facets

(facet-05_events.architecture)=
### Facet: `05_events.architecture`
Type: diagram

(facet-05_events.entities)=
### Facet: `05_events.entities`
Type: dataset

(facet-05_events.events_details)=
### Facet: `05_events.events_details`
Type: dataset

(facet-05_events.events_overview)=
### Facet: `05_events.events_overview`
Type: diagram

(facet-05_events.flow)=
### Facet: `05_events.flow`
Type: diagram

(facet-05_events.summary)=
### Facet: `05_events.summary`
Type: dataset



## Architektura Rozszerzona

### Komponenty Systemu

System składa się z następujących warstw:

1. **Warstwa Prezentacji** - Interface użytkownika
2. **Warstwa Logiki** - Biznesowa logika aplikacji  
3. **Warstwa Danych** - Dostęp i zarządzanie danymi
4. **Warstwa Infrastruktury** - Usługi wspierające

### Wzorce Projektowe

Wykorzystywane wzorce:

- **Observer** - Dla systemu zdarzeń
- **Factory** - Tworzenie obiektów
- **Singleton** - Globalne instancje
- **Strategy** - Wymienne algorytmy
- **Command** - Enkapsulacja akcji

## Szczegółowe Przykłady

### Przykład 1: Podstawowa Implementacja

```lua
-- Inicjalizacja modułu
local MyModule = {}

function MyModule.init()
    print("Module initialized")
    MyModule.setupHandlers()
    MyModule.loadResources()
end

function MyModule.setupHandlers()
    -- Rejestracja handlerów zdarzeń
    connect(g_game, {
        onGameStart = MyModule.onGameStart,
        onGameEnd = MyModule.onGameEnd
    })
end

function MyModule.loadResources()
    -- Ładowanie zasobów
    MyModule.config = g_resources.loadConfig("mymodule.json")
end

function MyModule.onGameStart()
    print("Game started")
end

function MyModule.onGameEnd()
    print("Game ended")
    MyModule.cleanup()
end

function MyModule.cleanup()
    -- Czyszczenie zasobów
    collectgarbage("collect")
end

return MyModule
```

### Przykład 2: Zaawansowana Integracja

```lua
-- Zaawansowany przykład z pełną integracją
local AdvancedModule = {
    version = "1.0.0",
    author = "OTClient Team",
    dependencies = {"core", "ui", "network"}
}

function AdvancedModule:init()
    self:validateDependencies()
    self:loadConfiguration()
    self:registerCommands()
    self:setupUI()
    self:connectSignals()
end

function AdvancedModule:validateDependencies()
    for _, dep in ipairs(self.dependencies) do
        if not g_modules.isLoaded(dep) then
            error("Required dependency not loaded: " .. dep)
        end
    end
end

function AdvancedModule:loadConfiguration()
    local configPath = "modules/advanced/config.json"
    self.config = g_resources.loadJSON(configPath)
    
    if not self.config then
        self.config = self:getDefaultConfig()
    end
end

function AdvancedModule:getDefaultConfig()
    return {
        enabled = true,
        debug = false,
        updateInterval = 1000,
        maxRetries = 3
    }
end

function AdvancedModule:registerCommands()
    g_commands.register("mycommand", function(args)
        self:handleCommand(args)
    end)
end

function AdvancedModule:setupUI()
    local ui = g_ui.loadUI("advanced_panel.otui")
    ui:setVisible(false)
    self.panel = ui
    
    -- Przypisanie handlerów
    local closeButton = ui:getChildById("closeButton")
    connect(closeButton, "onClick", function()
        ui:setVisible(false)
    end)
end

function AdvancedModule:connectSignals()
    connect(g_game, "onLogin", function()
        self:onPlayerLogin()
    end)
    
    connect(g_game, "onLogout", function()
        self:onPlayerLogout()
    end)
end

function AdvancedModule:onPlayerLogin()
    print("Player logged in")
    self:startUpdateTimer()
end

function AdvancedModule:onPlayerLogout()
    print("Player logged out")
    self:stopUpdateTimer()
end

function AdvancedModule:startUpdateTimer()
    self.updateTimer = scheduleEvent(function()
        self:update()
    end, self.config.updateInterval, true)
end

function AdvancedModule:stopUpdateTimer()
    if self.updateTimer then
        removeEvent(self.updateTimer)
        self.updateTimer = nil
    end
end

function AdvancedModule:update()
    -- Periodic update logic
    self:refreshData()
    self:updateUI()
end

function AdvancedModule:refreshData()
    -- Fetch fresh data
    local data = self:fetchDataFromServer()
    if data then
        self:processData(data)
    end
end

function AdvancedModule:processData(data)
    -- Process received data
    for key, value in pairs(data) do
        self.cache[key] = value
    end
end

function AdvancedModule:updateUI()
    if not self.panel:isVisible() then
        return
    end
    
    -- Update UI elements
    local label = self.panel:getChildById("statusLabel")
    label:setText(self:getStatusText())
end

function AdvancedModule:handleCommand(args)
    if #args == 0 then
        print("Usage: mycommand <action> [params]")
        return
    end
    
    local action = args[1]
    
    if action == "show" then
        self.panel:setVisible(true)
    elseif action == "hide" then
        self.panel:setVisible(false)
    elseif action == "reload" then
        self:reload()
    else
        print("Unknown action: " .. action)
    end
end

function AdvancedModule:reload()
    print("Reloading module...")
    self:cleanup()
    self:init()
end

function AdvancedModule:cleanup()
    self:stopUpdateTimer()
    
    if self.panel then
        self.panel:destroy()
        self.panel = nil
    end
    
    self.cache = {}
end

return AdvancedModule
```

### Przykład 3: Optymalizacje Wydajnościowe

```lua
-- Performance-optimized implementation
local PerformanceModule = {}

-- Object pooling
PerformanceModule.objectPool = {}

function PerformanceModule:getFromPool(objectType)
    local pool = self.objectPool[objectType]
    if not pool then
        pool = {}
        self.objectPool[objectType] = pool
    end
    
    if #pool > 0 then
        return table.remove(pool)
    else
        return self:createObject(objectType)
    end
end

function PerformanceModule:returnToPool(objectType, object)
    local pool = self.objectPool[objectType]
    if not pool then
        pool = {}
        self.objectPool[objectType] = pool
    end
    
    object:reset()
    table.insert(pool, object)
end

-- Memoization
PerformanceModule.cache = {}

function PerformanceModule:memoize(func)
    return function(...)
        local args = {...}
        local key = table.concat(args, "_")
        
        if self.cache[key] then
            return self.cache[key]
        end
        
        local result = func(...)
        self.cache[key] = result
        return result
    end
end

-- Lazy initialization
function PerformanceModule:getLazyResource(name)
    if not self.lazyResources then
        self.lazyResources = {}
    end
    
    if not self.lazyResources[name] then
        self.lazyResources[name] = self:loadResource(name)
    end
    
    return self.lazyResources[name]
end

return PerformanceModule
```

## Integracja z Innymi Systemami

### Integracja z UI

```lua
-- UI integration example
function integrateWithUI()
    local mainWindow = g_ui.getRootWidget()
    
    -- Create custom widget
    local customWidget = g_ui.createWidget("CustomWidget", mainWindow)
    customWidget:setId("myCustomWidget")
    
    -- Setup widget
    customWidget:setPosition({x = 100, y = 100})
    customWidget:setSize({width = 200, height = 150})
    
    -- Add handlers
    connect(customWidget, {
        onClick = handleWidgetClick,
        onHover = handleWidgetHover,
        onLeave = handleWidgetLeave
    })
    
    return customWidget
end
```

### Integracja z Network

```lua
-- Network integration
function integrateWithNetwork()
    local protocol = g_game.getProtocolGame()
    
    if not protocol then
        print("Protocol not available")
        return
    end
    
    -- Register packet handler
    protocol:registerOpcode(0xF1, function(msg)
        handleCustomPacket(msg)
    end)
    
    -- Send custom packet
    local msg = OutputMessage.create()
    msg:addU8(0xF1)
    msg:addString("custom data")
    protocol:send(msg)
end
```

### Integracja z Storage

```lua
-- Storage integration
function integrateWithStorage()
    -- Save data
    g_storage.set("mymodule.data", {
        value1 = 123,
        value2 = "test",
        value3 = {nested = true}
    })
    
    -- Load data
    local data = g_storage.get("mymodule.data")
    if data then
        print("Loaded:", data.value1, data.value2)
    end
    
    -- Clear data
    g_storage.remove("mymodule.data")
end
```

## Testowanie i Debugowanie

### Unit Testing

```lua
-- Simple unit test framework
local Tests = {}

function Tests:assertEqual(actual, expected, message)
    if actual ~= expected then
        error(message or ("Expected " .. tostring(expected) .. ", got " .. tostring(actual)))
    end
end

function Tests:assertTrue(condition, message)
    if not condition then
        error(message or "Expected true, got false")
    end
end

function Tests:testBasicFunctionality()
    local result = myFunction(10)
    self:assertEqual(result, 20, "Function should double the input")
end

function Tests:testEdgeCases()
    self:assertEqual(myFunction(0), 0)
    self:assertEqual(myFunction(-5), -10)
end

function Tests:runAll()
    local passed = 0
    local failed = 0
    
    for name, test in pairs(self) do
        if type(test) == "function" and name:match("^test") then
            local success, error = pcall(test, self)
            if success then
                print("✓ " .. name)
                passed = passed + 1
            else
                print("✗ " .. name .. ": " .. error)
                failed = failed + 1
            end
        end
    end
    
    print(string.format("Tests: %d passed, %d failed", passed, failed))
end

return Tests
```

### Debugowanie

```lua
-- Debug utilities
local Debug = {}

function Debug:trace(...)
    local info = debug.getinfo(2, "Sl")
    print(string.format("[%s:%d] %s", 
        info.short_src, 
        info.currentline, 
        table.concat({...}, " ")
    ))
end

function Debug:dump(value, depth)
    depth = depth or 0
    local indent = string.rep("  ", depth)
    
    if type(value) == "table" then
        print(indent .. "{")
        for k, v in pairs(value) do
            print(indent .. "  " .. tostring(k) .. " = ")
            self:dump(v, depth + 1)
        end
        print(indent .. "}")
    else
        print(indent .. tostring(value))
    end
end

function Debug:benchmark(func, iterations)
    iterations = iterations or 1000
    local start = g_clock.millis()
    
    for i = 1, iterations do
        func()
    end
    
    local duration = g_clock.millis() - start
    print(string.format("Benchmark: %d iterations in %dms (%.2fms/iter)",
        iterations, duration, duration / iterations))
end

return Debug
```

## Dokumentacja API

### Główne Funkcje

#### initialize()
Inicjalizuje moduł. Wymagane przed użyciem.

**Parametry:** brak  
**Zwraca:** `boolean` - sukces/niepowodzenie  
**Rzuca:** `error` jeśli zależności nie są spełnione

**Przykład:**
```lua
if not module:initialize() then
    error("Failed to initialize module")
end
```

#### configure(options: table)
Konfiguruje moduł z podanymi opcjami.

**Parametry:**
- `options` (table) - Tabela konfiguracyjna

**Zwraca:** `boolean`

**Przykład:**
```lua
module:configure({
    enabled = true,
    debug = false
})
```

#### process(data: any)
Przetwarza dane.

**Parametry:**
- `data` (any) - Dane do przetworzenia

**Zwraca:** `any` - Wynik

#### cleanup()
Czyści zasoby modułu.

**Parametry:** brak  
**Zwraca:** brak

### Events

#### onInitialized
Wywoływane po inicjalizacji.

```lua
connect(module, "onInitialized", function()
    print("Module ready")
end)
```

#### onError(error: string)
Wywoływane przy błędzie.

```lua
connect(module, "onError", function(error)
    print("Error:", error)
end)
```

### Stałe

- `VERSION` - Wersja modułu
- `MAX_ITEMS` - Maksymalna liczba elementów
- `TIMEOUT` - Timeout w ms



## Zaawansowane Wzorce i Techniki

### Pattern: Dependency Injection

```lua
-- Container for dependencies
local DIContainer = {}

function DIContainer:register(name, factory)
    self[name] = {
        factory = factory,
        instance = nil,
        singleton = true
    }
end

function DIContainer:get(name)
    local service = self[name]
    if not service then
        error("Service not registered: " .. name)
    end
    
    if service.singleton and service.instance then
        return service.instance
    end
    
    local instance = service.factory()
    if service.singleton then
        service.instance = instance
    end
    
    return instance
end

-- Usage
DIContainer:register("logger", function()
    return Logger.create()
end)

DIContainer:register("database", function()
    local db = Database.create()
    db:connect()
    return db
end)

local logger = DIContainer:get("logger")
logger:info("Application started")
```

### Pattern: Event Sourcing

```lua
-- Event store
local EventStore = {
    events = {},
    handlers = {}
}

function EventStore:append(event)
    event.timestamp = os.time()
    event.version = #self.events + 1
    table.insert(self.events, event)
    
    self:dispatch(event)
end

function EventStore:dispatch(event)
    local handlers = self.handlers[event.type] or {}
    for _, handler in ipairs(handlers) do
        handler(event)
    end
end

function EventStore:subscribe(eventType, handler)
    if not self.handlers[eventType] then
        self.handlers[eventType] = {}
    end
    table.insert(self.handlers[eventType], handler)
end

function EventStore:replay(fromVersion)
    fromVersion = fromVersion or 1
    local state = {}
    
    for i = fromVersion, #self.events do
        local event = self.events[i]
        state = self:applyEvent(state, event)
    end
    
    return state
end

function EventStore:applyEvent(state, event)
    if event.type == "ItemAdded" then
        state.items = state.items or {}
        table.insert(state.items, event.data)
    elseif event.type == "ItemRemoved" then
        state.items = state.items or {}
        table.remove(state.items, event.data.index)
    end
    return state
end

-- Usage
EventStore:subscribe("ItemAdded", function(event)
    print("Item added:", event.data.name)
end)

EventStore:append({
    type = "ItemAdded",
    data = {name = "Sword", id = 123}
})

local currentState = EventStore:replay()
```

### Pattern: CQRS (Command Query Responsibility Segregation)

```lua
-- Command side
local CommandHandler = {}

function CommandHandler:execute(command)
    local handler = self[command.type]
    if not handler then
        error("No handler for command: " .. command.type)
    end
    
    return handler(self, command)
end

function CommandHandler:CreateUser(command)
    local user = {
        id = generateId(),
        name = command.data.name,
        email = command.data.email
    }
    
    -- Persist user
    database:save("users", user)
    
    -- Emit event
    EventBus:emit("UserCreated", user)
    
    return user.id
end

function CommandHandler:UpdateUser(command)
    local user = database:find("users", command.data.id)
    if not user then
        error("User not found")
    end
    
    user.name = command.data.name or user.name
    user.email = command.data.email or user.email
    
    database:save("users", user)
    EventBus:emit("UserUpdated", user)
end

-- Query side
local QueryHandler = {}

function QueryHandler:GetUser(query)
    return database:find("users", query.id)
end

function QueryHandler:GetUsers(query)
    local users = database:findAll("users")
    
    -- Apply filters
    if query.filter then
        users = self:applyFilter(users, query.filter)
    end
    
    -- Apply sorting
    if query.sort then
        table.sort(users, query.sort)
    end
    
    -- Apply pagination
    if query.page and query.pageSize then
        local start = (query.page - 1) * query.pageSize + 1
        local endPos = math.min(start + query.pageSize - 1, #users)
        local page = {}
        for i = start, endPos do
            table.insert(page, users[i])
        end
        return page
    end
    
    return users
end

function QueryHandler:applyFilter(items, filter)
    local filtered = {}
    for _, item in ipairs(items) do
        local matches = true
        for key, value in pairs(filter) do
            if item[key] ~= value then
                matches = false
                break
            end
        end
        if matches then
            table.insert(filtered, item)
        end
    end
    return filtered
end
```

## Monitorowanie i Metryki

### System Metryk

```lua
local Metrics = {
    counters = {},
    gauges = {},
    histograms = {}
}

function Metrics:incrementCounter(name, value)
    value = value or 1
    self.counters[name] = (self.counters[name] or 0) + value
end

function Metrics:setGauge(name, value)
    self.gauges[name] = value
end

function Metrics:recordHistogram(name, value)
    if not self.histograms[name] then
        self.histograms[name] = {}
    end
    table.insert(self.histograms[name], value)
end

function Metrics:getSnapshot()
    local snapshot = {
        timestamp = os.time(),
        counters = {},
        gauges = {},
        histograms = {}
    }
    
    -- Copy counters
    for k, v in pairs(self.counters) do
        snapshot.counters[k] = v
    end
    
    -- Copy gauges
    for k, v in pairs(self.gauges) do
        snapshot.gauges[k] = v
    end
    
    -- Calculate histogram stats
    for name, values in pairs(self.histograms) do
        snapshot.histograms[name] = self:calculateStats(values)
    end
    
    return snapshot
end

function Metrics:calculateStats(values)
    if #values == 0 then
        return {min = 0, max = 0, avg = 0, p95 = 0, p99 = 0}
    end
    
    local sorted = {}
    for _, v in ipairs(values) do
        table.insert(sorted, v)
    end
    table.sort(sorted)
    
    local sum = 0
    for _, v in ipairs(sorted) do
        sum = sum + v
    end
    
    local p95_index = math.floor(#sorted * 0.95)
    local p99_index = math.floor(#sorted * 0.99)
    
    return {
        min = sorted[1],
        max = sorted[#sorted],
        avg = sum / #sorted,
        p95 = sorted[p95_index] or sorted[#sorted],
        p99 = sorted[p99_index] or sorted[#sorted]
    }
end

-- Usage
Metrics:incrementCounter("requests")
Metrics:setGauge("active_connections", 42)
Metrics:recordHistogram("response_time", 150)

local snapshot = Metrics:getSnapshot()
print("Requests:", snapshot.counters.requests)
print("Response time avg:", snapshot.histograms.response_time.avg)
```

### Health Checks

```lua
local HealthChecker = {
    checks = {}
}

function HealthChecker:register(name, checkFunction)
    self.checks[name] = checkFunction
end

function HealthChecker:check()
    local results = {}
    local allHealthy = true
    
    for name, checkFunction in pairs(self.checks) do
        local success, result = pcall(checkFunction)
        
        results[name] = {
            healthy = success and result.healthy,
            message = result and result.message or "Check failed",
            timestamp = os.time()
        }
        
        if not results[name].healthy then
            allHealthy = false
        end
    end
    
    return {
        healthy = allHealthy,
        checks = results
    }
end

-- Register health checks
HealthChecker:register("database", function()
    local connected = database:isConnected()
    return {
        healthy = connected,
        message = connected and "Database OK" or "Database disconnected"
    }
end)

HealthChecker:register("memory", function()
    local memKB = collectgarbage("count")
    local healthy = memKB < 100000  -- Less than 100MB
    return {
        healthy = healthy,
        message = string.format("Memory usage: %.2f MB", memKB / 1024)
    }
end)

-- Check health
local health = HealthChecker:check()
if not health.healthy then
    print("System unhealthy!")
    for name, check in pairs(health.checks) do
        if not check.healthy then
            print("  " .. name .. ": " .. check.message)
        end
    end
end
```

## Bezpieczeństwo

### Input Sanitization

```lua
local Security = {}

function Security:sanitizeString(input, maxLength)
    maxLength = maxLength or 1000
    
    if type(input) ~= "string" then
        return ""
    end
    
    -- Remove null bytes
    input = input:gsub("%z", "")
    
    -- Trim to max length
    if #input > maxLength then
        input = input:sub(1, maxLength)
    end
    
    -- Remove control characters (except newline/tab)
    input = input:gsub("[%c]", function(c)
        local byte = string.byte(c)
        if byte == 10 or byte == 9 then  -- newline or tab
            return c
        end
        return ""
    end)
    
    return input
end

function Security:sanitizeHTML(input)
    -- Basic HTML sanitization
    local replacements = {
        ["<"] = "&lt;",
        [">"] = "&gt;",
        ["&"] = "&amp;",
        ['"'] = "&quot;",
        ["'"] = "&#39;"
    }
    
    for char, replacement in pairs(replacements) do
        input = input:gsub(char, replacement)
    end
    
    return input
end

function Security:validateEmail(email)
    -- Simple email validation
    local pattern = "^[%w._%+-]+@[%w.-]+%.%a%a+$"
    return email:match(pattern) ~= nil
end

function Security:validateUsername(username)
    -- Username: 3-20 chars, alphanumeric + underscore
    if #username < 3 or #username > 20 then
        return false, "Username must be 3-20 characters"
    end
    
    if not username:match("^[%w_]+$") then
        return false, "Username can only contain letters, numbers, and underscores"
    end
    
    return true
end
```

### Rate Limiting

```lua
local RateLimiter = {}

function RateLimiter:create(maxRequests, windowSeconds)
    local limiter = {
        maxRequests = maxRequests,
        windowSeconds = windowSeconds,
        requests = {}
    }
    setmetatable(limiter, {__index = self})
    return limiter
end

function RateLimiter:allow(key)
    local now = os.time()
    local windowStart = now - self.windowSeconds
    
    -- Initialize request log for key
    if not self.requests[key] then
        self.requests[key] = {}
    end
    
    -- Remove old requests
    local requests = self.requests[key]
    local i = 1
    while i <= #requests do
        if requests[i] < windowStart then
            table.remove(requests, i)
        else
            i = i + 1
        end
    end
    
    -- Check limit
    if #requests >= self.maxRequests then
        return false, "Rate limit exceeded"
    end
    
    -- Record request
    table.insert(requests, now)
    return true
end

-- Usage
local limiter = RateLimiter:create(10, 60)  -- 10 requests per minute

if limiter:allow("user123") then
    processRequest()
else
    print("Too many requests, please wait")
end
```

## Appendix: Checklist Implementacji

### Pre-Development

- [ ] Zrozumienie wymagań
- [ ] Określenie zależności
- [ ] Planowanie architektury
- [ ] Wybór wzorców projektowych

### Development

- [ ] Implementacja core functionality
- [ ] Unit testing
- [ ] Integration testing
- [ ] Code review

### Post-Development

- [ ] Documentation
- [ ] Performance testing
- [ ] Security audit
- [ ] Deployment preparation

### Maintenance

- [ ] Monitoring
- [ ] Bug fixes
- [ ] Feature enhancements
- [ ] Regular updates


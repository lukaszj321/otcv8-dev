---
title: "src/framework/core/eventdispatcher.h"
source_file: "src/framework/core/eventdispatcher.h"
generated_at: "2025-11-01T04:06:42.740Z"
doc_type: "cpp_api"
---

# src/framework/core/eventdispatcher.h

(shutdown)=
## `shutdown`

**Signature:**
```cpp
public: void shutdown();
```

---

(poll)=
## `poll`

**Signature:**
```cpp
void poll();
```

---

(addeventex)=
## `addEventEx`

**Signature:**
```cpp
EventPtr addEventEx(const std::string& function, const std::function<void()>& callback, bool pushFront = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `function` |  | - |
| `const std::function&lt;void()&gt;&` | `callback` |  | - |
| `bool` | `pushFront` | `false` | - |

**Returns:**
- `EventPtr`

---

(scheduleeventex)=
## `scheduleEventEx`

**Signature:**
```cpp
ScheduledEventPtr scheduleEventEx(const std::string& function, const std::function<void()>& callback, int delay);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `function` | - |
| `const std::function&lt;void()&gt;&` | `callback` | - |
| `int` | `delay` | - |

**Returns:**
- `ScheduledEventPtr`

---

(cycleeventex)=
## `cycleEventEx`

**Signature:**
```cpp
ScheduledEventPtr cycleEventEx(const std::string& function, const std::function<void()>& callback, int delay);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `function` | - |
| `const std::function&lt;void()&gt;&` | `callback` | - |
| `int` | `delay` | - |

**Returns:**
- `ScheduledEventPtr`

---

(isbotsafe)=
## `isBotSafe`

**Signature:**
```cpp
bool isBotSafe();
```

**Returns:**
- `bool`

---

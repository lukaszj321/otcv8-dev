---
title: "src/framework/core/scheduledevent.h"
source_file: "src/framework/core/scheduledevent.h"
generated_at: "2025-11-01T06:09:06.181Z"
doc_type: "cpp_api"
---

# src/framework/core/scheduledevent.h

(scheduledevent)=
## `ScheduledEvent`

**Signature:**
```cpp
public: ScheduledEvent(const std::string& function, const std::function<void()>& callback, int delay, int maxCycles, bool botSafe = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `function` |  | - |
| `const std::function&lt;void()&gt;&` | `callback` |  | - |
| `int` | `delay` |  | - |
| `int` | `maxCycles` |  | - |
| `bool` | `botSafe` | `false` | - |

---

(execute)=
## `execute`

**Signature:**
```cpp
void execute();
```

---

(nextcycle)=
## `nextCycle`

**Signature:**
```cpp
bool nextCycle();
```

**Returns:**
- `bool`

---

(ticks)=
## `ticks`

**Signature:**
```cpp
int ticks();
```

**Returns:**
- `int`

---

(remainingticks)=
## `remainingTicks`

**Signature:**
```cpp
int remainingTicks();
```

**Returns:**
- `int`

---

(delay)=
## `delay`

**Signature:**
```cpp
int delay();
```

**Returns:**
- `int`

---

(cyclesexecuted)=
## `cyclesExecuted`

**Signature:**
```cpp
int cyclesExecuted();
```

**Returns:**
- `int`

---

(maxcycles)=
## `maxCycles`

**Signature:**
```cpp
int maxCycles();
```

**Returns:**
- `int`

---

(operator)=
## `operator`

**Signature:**
```cpp
bool operator()(const ScheduledEventPtr& a, const ScheduledEventPtr& b);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `)(const ScheduledEventPtr&` | `a` | - |
| `const ScheduledEventPtr&` | `b` | - |

**Returns:**
- `bool`

---

---
title: "src/framework/core/event.h"
source_file: "src/framework/core/event.h"
generated_at: "2025-11-01T05:32:59.274Z"
doc_type: "cpp_api"
---

# src/framework/core/event.h

(event)=
## `Event`

**Signature:**
```cpp
public: Event(const std::string& function, const std::function<void()>& callback, bool botSafe = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `function` |  | - |
| `const std::function&lt;void()&gt;&` | `callback` |  | - |
| `bool` | `botSafe` | `false` | - |

---

(execute)=
## `execute`

**Signature:**
```cpp
virtual void execute();
```

---

(cancel)=
## `cancel`

**Signature:**
```cpp
void cancel();
```

---

(iscanceled)=
## `isCanceled`

**Signature:**
```cpp
bool isCanceled();
```

**Returns:**
- `bool`

---

(isexecuted)=
## `isExecuted`

**Signature:**
```cpp
bool isExecuted();
```

**Returns:**
- `bool`

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

(getfunction)=
## `getFunction`

**Signature:**
```cpp
const std::string& getFunction();
```

**Returns:**
- `const std::string&`

---

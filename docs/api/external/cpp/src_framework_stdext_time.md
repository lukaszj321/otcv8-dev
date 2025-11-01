---
title: "src/framework/stdext/time.h"
source_file: "src/framework/stdext/time.h"
generated_at: "2025-11-01T08:45:15.323Z"
doc_type: "cpp_api"
---

# src/framework/stdext/time.h

(time)=
## `time`

**Signature:**
```cpp
ticks_t time();
```

**Returns:**
- `ticks_t`

---

(millis)=
## `millis`

**Signature:**
```cpp
ticks_t millis();
```

**Returns:**
- `ticks_t`

---

(micros)=
## `micros`

**Signature:**
```cpp
ticks_t micros();
```

**Returns:**
- `ticks_t`

---

(millisleep)=
## `millisleep`

**Signature:**
```cpp
void millisleep(size_t ms);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `ms` | - |

---

(microsleep)=
## `microsleep`

**Signature:**
```cpp
void microsleep(size_t us);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `us` | - |

---

(timer)=
## `timer`

**Signature:**
```cpp
public: timer();
```

---

(elapsed_seconds)=
## `elapsed_seconds`

**Signature:**
```cpp
float elapsed_seconds();
```

**Returns:**
- `float`

---

(elapsed_millis)=
## `elapsed_millis`

**Signature:**
```cpp
ticks_t elapsed_millis();
```

**Returns:**
- `ticks_t`

---

(elapsed_micros)=
## `elapsed_micros`

**Signature:**
```cpp
ticks_t elapsed_micros();
```

**Returns:**
- `ticks_t`

---

(restart)=
## `restart`

**Signature:**
```cpp
void restart(int shift = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `shift` | `0` | - |

---

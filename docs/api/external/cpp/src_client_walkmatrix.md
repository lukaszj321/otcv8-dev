---
title: "src/client/walkmatrix.h"
source_file: "src/client/walkmatrix.h"
generated_at: "2025-10-31T23:33:30.332Z"
doc_type: "cpp_api"
---

# src/client/walkmatrix.h

(clear)=
## `clear`

**Signature:**
```cpp
return clear();
```

**Returns:**
- `return`

---

(updateposition)=
## `updatePosition`

**Signature:**
```cpp
public: void updatePosition(const Position& newPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `newPos` | - |

**Returns:**
- `public: void`

---

(inrange)=
## `inRange`

**Signature:**
```cpp
bool inRange(const Position& pos2);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos2` | - |

**Returns:**
- `bool`

---

(update)=
## `update`

**Signature:**
```cpp
int32_t update(const Position& pos2, int32_t value = 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos2` | - |
| `int32_t value = 0` | - | - |

**Returns:**
- `int32_t`

---

(get)=
## `get`

**Signature:**
```cpp
int32_t get(const Position& pos2);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos2` | - |

**Returns:**
- `int32_t`

---

(clear-void)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(reset)=
## `reset`

**Signature:**
```cpp
uint32_t reset(uint32_t value = 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t value = 0` | - | - |

**Returns:**
- `uint32_t`

---

(dump)=
## `dump`

**Signature:**
```cpp
std::string dump();
```

**Returns:**
- `std::string`

---

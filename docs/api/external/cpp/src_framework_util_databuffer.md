---
title: "src/framework/util/databuffer.h"
source_file: "src/framework/util/databuffer.h"
generated_at: "2025-10-31T23:33:30.368Z"
doc_type: "cpp_api"
---

# src/framework/util/databuffer.h

(databuffer)=
## `DataBuffer`

**Signature:**
```cpp
public: DataBuffer(uint res = 64) : m_size(0), m_capacity(res), m_buffer(new T[m_capacity]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint res = 64) : m_size(0)` | - | - |
| `m_capacity(res)` | - | - |
| `m_buffer(new T[m_capacity]` | - | - |

**Returns:**
- `public:`

---

(reset)=
## `reset`

**Signature:**
```cpp
inline void reset();
```

**Returns:**
- `inline void`

---

(clear)=
## `clear`

**Signature:**
```cpp
inline void clear();
```

**Returns:**
- `inline void`

---

(empty)=
## `empty`

**Signature:**
```cpp
inline bool empty();
```

**Returns:**
- `inline bool`

---

(size)=
## `size`

**Signature:**
```cpp
inline uint size();
```

**Returns:**
- `inline uint`

---

(at)=
## `at`

**Signature:**
```cpp
inline const T& at(uint i);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `i` | - |

**Returns:**
- `inline const T&`

---

(last)=
## `last`

**Signature:**
```cpp
inline const T& last();
```

**Returns:**
- `inline const T&`

---

(first)=
## `first`

**Signature:**
```cpp
inline const T& first();
```

**Returns:**
- `inline const T&`

---

(reserve)=
## `reserve`

**Signature:**
```cpp
inline void reserve(uint n);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `n` | - |

**Returns:**
- `inline void`

---

(resize)=
## `resize`

**Signature:**
```cpp
inline void resize(uint n, T def = T());
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `n` | - |
| `T def = T()` | - | - |

**Returns:**
- `inline void`

---

(grow)=
## `grow`

**Signature:**
```cpp
inline void grow(uint n, bool precise = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `n` | - |
| `bool precise =` | `false` | - |

**Returns:**
- `inline void`

---

(add)=
## `add`

**Signature:**
```cpp
inline void add(const T& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `v` | - |

**Returns:**
- `inline void`

---

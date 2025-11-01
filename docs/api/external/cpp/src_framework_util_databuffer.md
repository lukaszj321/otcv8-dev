---
title: "src/framework/util/databuffer.h"
source_file: "src/framework/util/databuffer.h"
generated_at: "2025-11-01T08:45:15.329Z"
doc_type: "cpp_api"
---

# src/framework/util/databuffer.h

(reset)=
## `reset`

**Signature:**
```cpp
inline void reset();
```

---

(clear)=
## `clear`

**Signature:**
```cpp
inline void clear();
```

---

(empty)=
## `empty`

**Signature:**
```cpp
inline bool empty();
```

**Returns:**
- `bool`

---

(size)=
## `size`

**Signature:**
```cpp
inline uint size();
```

**Returns:**
- `uint`

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
- `const T&`

---

(last)=
## `last`

**Signature:**
```cpp
inline const T& last();
```

**Returns:**
- `const T&`

---

(first)=
## `first`

**Signature:**
```cpp
inline const T& first();
```

**Returns:**
- `const T&`

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

---

(resize)=
## `resize`

**Signature:**
```cpp
inline void resize(uint n, T def = T());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `uint` | `n` |  | - |
| `T` | `def` | `T()` | - |

---

(grow)=
## `grow`

**Signature:**
```cpp
inline void grow(uint n, bool precise = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `uint` | `n` |  | - |
| `bool` | `precise` | `false` | - |

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

---

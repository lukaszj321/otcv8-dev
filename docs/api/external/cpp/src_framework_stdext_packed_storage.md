---
title: "src/framework/stdext/packed_storage.h"
source_file: "src/framework/stdext/packed_storage.h"
generated_at: "2025-10-31T23:33:30.361Z"
doc_type: "cpp_api"
---

# src/framework/stdext/packed_storage.h

(packed_any_castt)=
## `packed_any_cast<T>`

**Signature:**
```cpp
return packed_any_cast<T>(m_values[i].value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `m_values[i].` | `value` | - |

**Returns:**
- `return`

---

(t)=
## `T`

**Signature:**
```cpp
return T();
```

**Returns:**
- `return`

---

(packed_storage)=
## `packed_storage`

**Signature:**
```cpp
public: packed_storage() : m_values(nullptr), m_size(0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) : m_values(nullptr)` | - | - |
| `m_size(0` | - | - |

**Returns:**
- `public:`

---

(set)=
## `set`

**Signature:**
```cpp
void set(Key id, const T& value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Key` | `id` | - |
| `const T&` | `value` | - |

---

(remove)=
## `remove`

**Signature:**
```cpp
bool remove(Key id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Key` | `id` | - |

**Returns:**
- `bool`

---

(get)=
## `get`

**Signature:**
```cpp
template<typename T> T get(Key id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Key` | `id` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

(has)=
## `has`

**Signature:**
```cpp
bool has(Key id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Key` | `id` | - |

**Returns:**
- `bool`

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(size)=
## `size`

**Signature:**
```cpp
std::size_t size();
```

**Returns:**
- `std::size_t`

---

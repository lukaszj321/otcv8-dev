---
title: "src/framework/stdext/packed_storage.h"
source_file: "src/framework/stdext/packed_storage.h"
generated_at: "2025-11-01T05:32:59.302Z"
doc_type: "cpp_api"
---

# src/framework/stdext/packed_storage.h

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

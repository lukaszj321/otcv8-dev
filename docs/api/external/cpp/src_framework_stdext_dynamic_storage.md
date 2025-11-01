---
title: "src/framework/stdext/dynamic_storage.h"
source_file: "src/framework/stdext/dynamic_storage.h"
generated_at: "2025-11-01T06:09:06.204Z"
doc_type: "cpp_api"
---

# src/framework/stdext/dynamic_storage.h

(set)=
## `set`

**Signature:**
```cpp
public: template<typename T> void set(const Key& k, const T& value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Key&` | `k` | - |
| `const T&` | `value` | - |

**Returns:**
- `template&lt;typename T&gt; void`

---

(remove)=
## `remove`

**Signature:**
```cpp
bool remove(const Key& k);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Key&` | `k` | - |

**Returns:**
- `bool`

---

(get)=
## `get`

**Signature:**
```cpp
template<typename T> T get(const Key& k);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Key&` | `k` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

(has)=
## `has`

**Signature:**
```cpp
bool has(const Key& k);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Key&` | `k` | - |

**Returns:**
- `bool`

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

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

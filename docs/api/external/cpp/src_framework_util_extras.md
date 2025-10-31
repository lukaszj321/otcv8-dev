---
title: "src/framework/util/extras.h"
source_file: "src/framework/util/extras.h"
generated_at: "2025-10-31T23:33:30.368Z"
doc_type: "cpp_api"
---

# src/framework/util/extras.h

(extras)=
## `Extras`

**Signature:**
```cpp
public: Extras();
```

**Returns:**
- `public:`

---

(set)=
## `set`

**Signature:**
```cpp
void set(const std::string& key, bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |
| `bool` | `value` | - |

---

(get)=
## `get`

**Signature:**
```cpp
bool get(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `bool`

---

(getdescription)=
## `getDescription`

**Signature:**
```cpp
std::string getDescription(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `std::string`

---

(getall)=
## `getAll`

**Signature:**
```cpp
std::vector<std::string> getAll();
```

**Returns:**
- `std::vector&lt;std::string&gt;`

---

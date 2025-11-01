---
title: "src/framework/core/configmanager.h"
source_file: "src/framework/core/configmanager.h"
generated_at: "2025-11-01T00:11:49.034Z"
doc_type: "cpp_api"
---

# src/framework/core/configmanager.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(getsettings)=
## `getSettings`

**Signature:**
```cpp
ConfigPtr getSettings();
```

**Returns:**
- `ConfigPtr`

---

(get)=
## `get`

**Signature:**
```cpp
ConfigPtr get(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

**Returns:**
- `ConfigPtr`

---

(create)=
## `create`

**Signature:**
```cpp
ConfigPtr create(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

**Returns:**
- `ConfigPtr`

---

(loadsettings)=
## `loadSettings`

**Signature:**
```cpp
ConfigPtr loadSettings(const std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string` | `file` | - |

**Returns:**
- `ConfigPtr`

---

(load)=
## `load`

**Signature:**
```cpp
ConfigPtr load(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

**Returns:**
- `ConfigPtr`

---

(unload)=
## `unload`

**Signature:**
```cpp
bool unload(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

**Returns:**
- `bool`

---

(remove)=
## `remove`

**Signature:**
```cpp
void remove(const ConfigPtr config);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ConfigPtr` | `config` | - |

---

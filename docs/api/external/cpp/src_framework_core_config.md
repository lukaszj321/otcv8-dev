---
title: "src/framework/core/config.h"
source_file: "src/framework/core/config.h"
generated_at: "2025-11-01T00:11:49.033Z"
doc_type: "cpp_api"
---

# src/framework/core/config.h

(config)=
## `Config`

**Signature:**
```cpp
public: Config();
```

---

(load)=
## `load`

**Signature:**
```cpp
bool load(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

**Returns:**
- `bool`

---

(unload)=
## `unload`

**Signature:**
```cpp
bool unload();
```

**Returns:**
- `bool`

---

(save)=
## `save`

**Signature:**
```cpp
bool save();
```

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

(setvalue)=
## `setValue`

**Signature:**
```cpp
void setValue(const std::string& key, const std::string& value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |
| `const std::string&` | `value` | - |

---

(setlist)=
## `setList`

**Signature:**
```cpp
void setList(const std::string& key, const std::vector<std::string>& list);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |
| `const std::vector&lt;std::string&gt;&` | `list` | - |

---

(getvalue)=
## `getValue`

**Signature:**
```cpp
std::string getValue(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `std::string`

---

(getlist)=
## `getList`

**Signature:**
```cpp
std::vector<std::string> getList(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `std::vector&lt;std::string&gt;`

---

(setnode)=
## `setNode`

**Signature:**
```cpp
void setNode(const std::string& key, const OTMLNodePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |
| `const OTMLNodePtr&` | `node` | - |

---

(mergenode)=
## `mergeNode`

**Signature:**
```cpp
void mergeNode(const std::string& key, const OTMLNodePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |
| `const OTMLNodePtr&` | `node` | - |

---

(getnode)=
## `getNode`

**Signature:**
```cpp
OTMLNodePtr getNode(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `OTMLNodePtr`

---

(getnodesize)=
## `getNodeSize`

**Signature:**
```cpp
int getNodeSize(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `int`

---

(exists)=
## `exists`

**Signature:**
```cpp
bool exists(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `bool`

---

(remove)=
## `remove`

**Signature:**
```cpp
void remove(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

---

(getfilename)=
## `getFileName`

**Signature:**
```cpp
std::string getFileName();
```

**Returns:**
- `std::string`

---

(isloaded)=
## `isLoaded`

**Signature:**
```cpp
bool isLoaded();
```

**Returns:**
- `bool`

---

(asconfig)=
## `asConfig`

**Signature:**
```cpp
ConfigPtr asConfig();
```

**Returns:**
- `ConfigPtr`

---

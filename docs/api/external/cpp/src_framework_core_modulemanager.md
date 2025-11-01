---
title: "src/framework/core/modulemanager.h"
source_file: "src/framework/core/modulemanager.h"
generated_at: "2025-11-01T08:19:49.437Z"
doc_type: "cpp_api"
---

# src/framework/core/modulemanager.h

(clear)=
## `clear`

**Signature:**
```cpp
public: void clear();
```

---

(discovermodules)=
## `discoverModules`

**Signature:**
```cpp
void discoverModules();
```

---

(autoloadmodules)=
## `autoLoadModules`

**Signature:**
```cpp
void autoLoadModules(int maxPriority);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `maxPriority` | - |

---

(discovermodule)=
## `discoverModule`

**Signature:**
```cpp
ModulePtr discoverModule(const std::string& moduleFile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `moduleFile` | - |

**Returns:**
- `ModulePtr`

---

(ensuremoduleloaded)=
## `ensureModuleLoaded`

**Signature:**
```cpp
void ensureModuleLoaded(const std::string& moduleName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `moduleName` | - |

---

(unloadmodules)=
## `unloadModules`

**Signature:**
```cpp
void unloadModules();
```

---

(reloadmodules)=
## `reloadModules`

**Signature:**
```cpp
void reloadModules();
```

---

(getmodule)=
## `getModule`

**Signature:**
```cpp
ModulePtr getModule(const std::string& moduleName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `moduleName` | - |

**Returns:**
- `ModulePtr`

---

(updatemoduleloadorder)=
## `updateModuleLoadOrder`

**Signature:**
```cpp
protected: void updateModuleLoadOrder(ModulePtr module);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ModulePtr` | `module` | - |

---

(getmodules)=
## `getModules`

**Signature:**
```cpp
std::deque<ModulePtr> getModules();
```

**Returns:**
- `std::deque&lt;ModulePtr&gt;`

---

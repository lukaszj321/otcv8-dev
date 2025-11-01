---
title: "src/framework/core/module.h"
source_file: "src/framework/core/module.h"
generated_at: "2025-11-01T08:29:23.695Z"
doc_type: "cpp_api"
---

# src/framework/core/module.h

(module)=
## `Module`

**Signature:**
```cpp
public: Module(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(load)=
## `load`

**Signature:**
```cpp
bool load();
```

**Returns:**
- `bool`

---

(unload)=
## `unload`

**Signature:**
```cpp
void unload();
```

---

(reload)=
## `reload`

**Signature:**
```cpp
bool reload();
```

**Returns:**
- `bool`

---

(isdependent)=
## `isDependent`

**Signature:**
```cpp
bool isDependent();
```

**Returns:**
- `bool`

---

(hasdependency)=
## `hasDependency`

**Signature:**
```cpp
bool hasDependency(const std::string& name, bool recursive = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `name` |  | - |
| `bool` | `recursive` | `false` | - |

**Returns:**
- `bool`

---

(getsandbox)=
## `getSandbox`

**Signature:**
```cpp
int getSandbox(LuaInterface *lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `LuaInterface *lua` | - | - |

**Returns:**
- `int`

---

(discover)=
## `discover`

**Signature:**
```cpp
protected: void discover(const OTMLNodePtr& moduleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `moduleNode` | - |

---

(canunload)=
## `canUnload`

**Signature:**
```cpp
bool canUnload();
```

**Returns:**
- `bool`

---

(canreload)=
## `canReload`

**Signature:**
```cpp
bool canReload();
```

**Returns:**
- `bool`

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

(isreloadable)=
## `isReloadable`

**Signature:**
```cpp
bool isReloadable();
```

**Returns:**
- `bool`

---

(issandboxed)=
## `isSandboxed`

**Signature:**
```cpp
bool isSandboxed();
```

**Returns:**
- `bool`

---

(getdescription)=
## `getDescription`

**Signature:**
```cpp
std::string getDescription();
```

**Returns:**
- `std::string`

---

(getname)=
## `getName`

**Signature:**
```cpp
std::string getName();
```

**Returns:**
- `std::string`

---

(getauthor)=
## `getAuthor`

**Signature:**
```cpp
std::string getAuthor();
```

**Returns:**
- `std::string`

---

(getwebsite)=
## `getWebsite`

**Signature:**
```cpp
std::string getWebsite();
```

**Returns:**
- `std::string`

---

(getversion)=
## `getVersion`

**Signature:**
```cpp
std::string getVersion();
```

**Returns:**
- `std::string`

---

(isautoload)=
## `isAutoLoad`

**Signature:**
```cpp
bool isAutoLoad();
```

**Returns:**
- `bool`

---

(getautoloadpriority)=
## `getAutoLoadPriority`

**Signature:**
```cpp
int getAutoLoadPriority();
```

**Returns:**
- `int`

---

(asmodule)=
## `asModule`

**Signature:**
```cpp
ModulePtr asModule();
```

**Returns:**
- `ModulePtr`

---

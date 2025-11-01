---
title: "src/framework/core/application.h"
source_file: "src/framework/core/application.h"
generated_at: "2025-11-01T08:45:15.293Z"
doc_type: "cpp_api"
---

# src/framework/core/application.h

(application)=
## `Application`

**Signature:**
```cpp
public: Application();
```

---

(init)=
## `init`

**Signature:**
```cpp
virtual void init(std::vector<std::string>& args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::vector&lt;std::string&gt;&` | `args` | - |

---

(deinit)=
## `deinit`

**Signature:**
```cpp
virtual void deinit();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
virtual void terminate();
```

---

(run)=
## `run`

**Signature:**
```cpp
virtual void run();
```

---

(poll)=
## `poll`

**Signature:**
```cpp
virtual void poll();
```

---

(exit)=
## `exit`

**Signature:**
```cpp
virtual void exit();
```

---

(quick_exit)=
## `quick_exit`

**Signature:**
```cpp
virtual void quick_exit();
```

---

(close)=
## `close`

**Signature:**
```cpp
virtual void close();
```

---

(restart)=
## `restart`

**Signature:**
```cpp
void restart();
```

---

(restartargs)=
## `restartArgs`

**Signature:**
```cpp
void restartArgs(const std::vector<std::string>& args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;std::string&gt;&` | `args` | - |

---

(getos)=
## `getOs`

**Signature:**
```cpp
std::string getOs();
```

**Returns:**
- `std::string`

---

(registerluafunctions)=
## `registerLuaFunctions`

**Signature:**
```cpp
protected: void registerLuaFunctions();
```

---

(setname)=
## `setName`

**Signature:**
```cpp
void setName(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(setcompactname)=
## `setCompactName`

**Signature:**
```cpp
void setCompactName(const std::string& compactName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `compactName` | - |

---

(setversion)=
## `setVersion`

**Signature:**
```cpp
void setVersion(const std::string& version);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `version` | - |

---

(isrunning)=
## `isRunning`

**Signature:**
```cpp
bool isRunning();
```

**Returns:**
- `bool`

---

(isstopping)=
## `isStopping`

**Signature:**
```cpp
bool isStopping();
```

**Returns:**
- `bool`

---

(isterminated)=
## `isTerminated`

**Signature:**
```cpp
bool isTerminated();
```

**Returns:**
- `bool`

---

(getname)=
## `getName`

**Signature:**
```cpp
const std::string& getName();
```

**Returns:**
- `const std::string&`

---

(getcompactname)=
## `getCompactName`

**Signature:**
```cpp
const std::string& getCompactName();
```

**Returns:**
- `const std::string&`

---

(getversion)=
## `getVersion`

**Signature:**
```cpp
const std::string& getVersion();
```

**Returns:**
- `const std::string&`

---

(getcharset)=
## `getCharset`

**Signature:**
```cpp
std::string getCharset();
```

**Returns:**
- `std::string`

---

(getbuildcompiler)=
## `getBuildCompiler`

**Signature:**
```cpp
std::string getBuildCompiler();
```

**Returns:**
- `std::string`

---

(getbuilddate)=
## `getBuildDate`

**Signature:**
```cpp
std::string getBuildDate();
```

**Returns:**
- `std::string`

---

(getbuildrevision)=
## `getBuildRevision`

**Signature:**
```cpp
std::string getBuildRevision();
```

**Returns:**
- `std::string`

---

(getbuildcommit)=
## `getBuildCommit`

**Signature:**
```cpp
std::string getBuildCommit();
```

**Returns:**
- `std::string`

---

(getbuildtype)=
## `getBuildType`

**Signature:**
```cpp
std::string getBuildType();
```

**Returns:**
- `std::string`

---

(getbuildtype-1)=
## `getBuildType`

**Signature:**
```cpp
std::string getBuildType();
```

**Returns:**
- `std::string`

---

(getbuildarch)=
## `getBuildArch`

**Signature:**
```cpp
std::string getBuildArch();
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

(getstartupoptions)=
## `getStartupOptions`

**Signature:**
```cpp
std::string getStartupOptions();
```

**Returns:**
- `std::string`

---

(ismobile)=
## `isMobile`

**Signature:**
```cpp
bool isMobile();
```

**Returns:**
- `bool`


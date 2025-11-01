---
title: "src/framework/core/logger.h"
source_file: "src/framework/core/logger.h"
generated_at: "2025-11-01T08:19:49.436Z"
doc_type: "cpp_api"
---

# src/framework/core/logger.h

(log)=
## `log`

**Signature:**
```cpp
public: void log(Fw::LogLevel level, const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::LogLevel` | `level` | - |
| `const std::string&` | `message` | - |

---

(logfunc)=
## `logFunc`

**Signature:**
```cpp
void logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::LogLevel` | `level` | - |
| `const std::string&` | `message` | - |
| `std::string` | `prettyFunction` | - |

---

(fireoldmessages)=
## `fireOldMessages`

**Signature:**
```cpp
void fireOldMessages();
```

---

(setlogfile)=
## `setLogFile`

**Signature:**
```cpp
void setLogFile(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(debug)=
## `debug`

**Signature:**
```cpp
void debug(const std::string& what);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `what` | - |

---

(info)=
## `info`

**Signature:**
```cpp
void info(const std::string& what);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `what` | - |

---

(warning)=
## `warning`

**Signature:**
```cpp
void warning(const std::string& what);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `what` | - |

---

(error)=
## `error`

**Signature:**
```cpp
void error(const std::string& what);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `what` | - |

---

(fatal)=
## `fatal`

**Signature:**
```cpp
void fatal(const std::string& what);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `what` | - |

---

(setonlog)=
## `setOnLog`

**Signature:**
```cpp
void setOnLog(const OnLogCallback& onLog);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OnLogCallback&` | `onLog` | - |

---

(getlastlog)=
## `getLastLog`

**Signature:**
```cpp
std::string getLastLog();
```

**Returns:**
- `std::string`

---

(settestingmode)=
## `setTestingMode`

**Signature:**
```cpp
void setTestingMode();
```

---

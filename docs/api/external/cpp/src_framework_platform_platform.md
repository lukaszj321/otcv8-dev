---
title: "src/framework/platform/platform.h"
source_file: "src/framework/platform/platform.h"
generated_at: "2025-10-31T23:33:30.353Z"
doc_type: "cpp_api"
---

# src/framework/platform/platform.h

(processargs)=
## `processArgs`

**Signature:**
```cpp
public: void processArgs(std::vector<std::string>& args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::vector&lt;std::string&gt;&` | `args` | - |

**Returns:**
- `public: void`

---

(spawnprocess)=
## `spawnProcess`

**Signature:**
```cpp
bool spawnProcess(std::string process, const std::vector<std::string>& args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `process` | - |
| `const std::vector&lt;std::string&gt;&` | `args` | - |

**Returns:**
- `bool`

---

(getprocessid)=
## `getProcessId`

**Signature:**
```cpp
int getProcessId();
```

**Returns:**
- `int`

---

(isprocessrunning)=
## `isProcessRunning`

**Signature:**
```cpp
bool isProcessRunning(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

**Returns:**
- `bool`

---

(killprocess)=
## `killProcess`

**Signature:**
```cpp
bool killProcess(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

**Returns:**
- `bool`

---

(gettemppath)=
## `getTempPath`

**Signature:**
```cpp
std::string getTempPath();
```

**Returns:**
- `std::string`

---

(getcurrentdir)=
## `getCurrentDir`

**Signature:**
```cpp
std::string getCurrentDir();
```

**Returns:**
- `std::string`

---

(copyfile)=
## `copyFile`

**Signature:**
```cpp
bool copyFile(std::string from, std::string to);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `from` | - |
| `std::string` | `to` | - |

**Returns:**
- `bool`

---

(fileexists)=
## `fileExists`

**Signature:**
```cpp
bool fileExists(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(removefile)=
## `removeFile`

**Signature:**
```cpp
bool removeFile(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(getfilemodificationtime)=
## `getFileModificationTime`

**Signature:**
```cpp
ticks_t getFileModificationTime(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `ticks_t`

---

(openurl)=
## `openUrl`

**Signature:**
```cpp
bool openUrl(std::string url, bool now = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `url` | - |
| `bool now =` | `false` | - |

**Returns:**
- `bool`

---

(opendir)=
## `openDir`

**Signature:**
```cpp
bool openDir(std::string path, bool now = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `path` | - |
| `bool now =` | `false` | - |

**Returns:**
- `bool`

---

(getcpuname)=
## `getCPUName`

**Signature:**
```cpp
std::string getCPUName();
```

**Returns:**
- `std::string`

---

(gettotalsystemmemory)=
## `getTotalSystemMemory`

**Signature:**
```cpp
double getTotalSystemMemory();
```

**Returns:**
- `double`

---

(getmemoryusage)=
## `getMemoryUsage`

**Signature:**
```cpp
double getMemoryUsage();
```

**Returns:**
- `double`

---

(getosname)=
## `getOSName`

**Signature:**
```cpp
std::string getOSName();
```

**Returns:**
- `std::string`

---

(traceback)=
## `traceback`

**Signature:**
```cpp
std::string traceback(const std::string& where, int level = 1, int maxDepth = 32);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `where` | - |
| `int level = 1` | - | - |
| `int maxDepth = 32` | - | - |

**Returns:**
- `std::string`

---

(getmacaddresses)=
## `getMacAddresses`

**Signature:**
```cpp
std::vector<std::string> getMacAddresses();
```

**Returns:**
- `std::vector&lt;std::string&gt;`

---

(getusername)=
## `getUserName`

**Signature:**
```cpp
std::string getUserName();
```

**Returns:**
- `std::string`

---

(getdlls)=
## `getDlls`

**Signature:**
```cpp
std::vector<std::string> getDlls();
```

**Returns:**
- `std::vector&lt;std::string&gt;`

---

(getprocesses)=
## `getProcesses`

**Signature:**
```cpp
std::vector<std::string> getProcesses();
```

**Returns:**
- `std::vector&lt;std::string&gt;`

---

(getwindows)=
## `getWindows`

**Signature:**
```cpp
std::vector<std::string> getWindows();
```

**Returns:**
- `std::vector&lt;std::string&gt;`

---

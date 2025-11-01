---
title: "src/framework/luaengine/luaexception.h"
source_file: "src/framework/luaengine/luaexception.h"
generated_at: "2025-11-01T08:19:49.451Z"
doc_type: "cpp_api"
---

# src/framework/luaengine/luaexception.h

(luaexception)=
## `LuaException`

**Signature:**
```cpp
public: LuaException(const std::string& error, int traceLevel = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `error` |  | - |
| `int` | `traceLevel` | `-1` | - |

---

(generateluaerrormessage)=
## `generateLuaErrorMessage`

**Signature:**
```cpp
void generateLuaErrorMessage(const std::string& error, int traceLevel);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `error` | - |
| `int` | `traceLevel` | - |

---

(luabadnumberofargumentsexception)=
## `LuaBadNumberOfArgumentsException`

**Signature:**
```cpp
public: LuaBadNumberOfArgumentsException(int expected = -1, int got = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `expected` | `-1` | - |
| `int` | `got` | `-1` | - |

---

(luabadvaluecastexception)=
## `LuaBadValueCastException`

**Signature:**
```cpp
public: LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `luaTypeName` | - |
| `const std::string&` | `cppTypeName` | - |

---

(what)=
## `what`

**Signature:**
```cpp
virtual const char* what() const throw();
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) const throw(` | - | - |

**Returns:**
- `const char*`

---

(luaexception-1)=
## `LuaException`

**Signature:**
```cpp
protected: LuaException();
```

---

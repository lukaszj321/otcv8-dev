---
title: "src/framework/luaengine/luaexception.h"
source_file: "src/framework/luaengine/luaexception.h"
generated_at: "2025-10-31T23:33:30.347Z"
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

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `error` | - |
| `int traceLevel = -1` | - | - |

**Returns:**
- `public:`

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

| Type | Name | Description |
|------|------|-------------|
| `int expected = -1` | - | - |
| `int got = -1` | - | - |

**Returns:**
- `public:`

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

**Returns:**
- `public:`

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
- `virtual const char*`

---

(luaexception)=
## `LuaException`

**Signature:**
```cpp
protected: LuaException();
```

**Returns:**
- `protected:`

---

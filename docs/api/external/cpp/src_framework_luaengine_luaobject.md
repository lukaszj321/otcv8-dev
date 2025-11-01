---
title: "src/framework/luaengine/luaobject.h"
source_file: "src/framework/luaengine/luaobject.h"
generated_at: "2025-11-01T08:46:04.923Z"
doc_type: "cpp_api"
---

# src/framework/luaengine/luaobject.h

(luaobject)=
## `LuaObject`

**Signature:**
```cpp
public: LuaObject();
```

---

(connectluafield)=
## `connectLuaField`

**Signature:**
```cpp
void connectLuaField(const std::string& field, const std::function<T>& f, bool pushFront = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `field` |  | - |
| `const std::function&lt;T&gt;&` | `f` |  | - |
| `bool` | `pushFront` | `false` | - |

---

(luacallluafield)=
## `luaCallLuaField`

Calls a function or table of functions stored in a lua field, results are pushed onto the stack,
if any lua error occurs, it will be reported to stdout and return 0 results
@return the number of results

**Signature:**
```cpp
int luaCallLuaField(const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

**Returns:**
- `int`

---

(callluafield)=
## `callLuaField`

**Signature:**
```cpp
void callLuaField(const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

---

(hasluafield)=
## `hasLuaField`

Returns true if the lua field exists

**Signature:**
```cpp
bool hasLuaField(const std::string& field);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `field` | - |

**Returns:**
- `bool`

---

(setluafield)=
## `setLuaField`

Sets a field in this lua object

**Signature:**
```cpp
void setLuaField(const std::string& key, const T& value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |
| `const T&` | `value` | - |

---

(getluafield)=
## `getLuaField`

Gets a field from this lua object

**Signature:**
```cpp
template<typename T> T getLuaField(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

(releaseluafieldstable)=
## `releaseLuaFieldsTable`

Release fields table reference

**Signature:**
```cpp
void releaseLuaFieldsTable();
```

---

(luasetfield)=
## `luaSetField`

Sets a field from this lua object, the value must be on the stack

**Signature:**
```cpp
void luaSetField(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

---

(luagetfield)=
## `luaGetField`

Gets a field from this lua object, the result is pushed onto the stack

**Signature:**
```cpp
void luaGetField(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

---

(luagetmetatable)=
## `luaGetMetatable`

Get object's metatable

**Signature:**
```cpp
void luaGetMetatable();
```

---

(luagetfieldstable)=
## `luaGetFieldsTable`

Gets the table containing all stored fields of this lua object, the result is pushed onto the stack

**Signature:**
```cpp
void luaGetFieldsTable();
```

---

(getusecount)=
## `getUseCount`

Returns the number of references of this object
@note each userdata of this object on lua counts as a reference

**Signature:**
```cpp
int getUseCount();
```

**Returns:**
- `int`

---

(getclassname)=
## `getClassName`

Returns the derived class name, its the same name used in Lua

**Signature:**
```cpp
std::string getClassName();
```

**Returns:**
- `std::string`

---

(connect)=
## `connect`

**Signature:**
```cpp
void connect(const LuaObjectPtr& obj, const std::string& field, const std::function<F>& f, bool pushFront = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const LuaObjectPtr&` | `obj` |  | - |
| `const std::string&` | `field` |  | - |
| `const std::function&lt;F&gt;&` | `f` |  | - |
| `bool` | `pushFront` | `false` | - |

---

(stdenable_ifstdis_constructibledecltype)=
## `std::enable_if<std::is_constructible<decltype`

**Signature:**
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, void>::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `&Lambda::operator())&gt;::value, void&gt;::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool` | `pushFront` | `false` | - |

**Returns:**
- `typename`

---

(s)=
## `s`

**Signature:**
```cpp
AutoStat s(STATS_LUA, getClassName() + ":" + field);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `STATS_LUA` | - | - |
| `getClassName() + ":" +` | `field` | - |

**Returns:**
- `AutoStat`

---

(asluaobject)=
## `asLuaObject`

**Signature:**
```cpp
LuaObjectPtr asLuaObject();
```

**Returns:**
- `LuaObjectPtr`

---

(luaobjectconnectluafield)=
## `LuaObject::connectLuaField`

**Signature:**
```cpp
void LuaObject::connectLuaField(const std::string& field, const std::function<T>& f, bool pushFront);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `field` | - |
| `const std::function&lt;T&gt;&` | `f` | - |
| `bool` | `pushFront` | - |

---

(connect-1)=
## `connect`

**Signature:**
```cpp
void connect(const LuaObjectPtr& obj, const std::string& field, const std::function<F>& f, bool pushFront);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const LuaObjectPtr&` | `obj` | - |
| `const std::string&` | `field` | - |
| `const std::function&lt;F&gt;&` | `f` | - |
| `bool` | `pushFront` | - |

---

(call)=
## `call`

**Signature:**
```cpp
static void call(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const LuaObjectPtr&` | `obj` | - |
| `const std::string&` | `field` | - |
| `const Lambda&` | `f` | - |
| `bool` | `pushFront` | - |

---

(stdenable_ifstdis_constructibledecltype-1)=
## `std::enable_if<std::is_constructible<decltype`

**Signature:**
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, void>::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `&Lambda::operator())&gt;::value, void&gt;::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool` | `pushFront` | - |

**Returns:**
- `typename`

---

(luaobjectluacallluafield)=
## `LuaObject::luaCallLuaField`

**Signature:**
```cpp
int LuaObject::luaCallLuaField(const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

**Returns:**
- `int`

---

(luaobjectcallluafield)=
## `LuaObject::callLuaField`

**Signature:**
```cpp
void LuaObject::callLuaField(const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

---

(luaobjectsetluafield)=
## `LuaObject::setLuaField`

**Signature:**
```cpp
void LuaObject::setLuaField(const std::string& key, const T& value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |
| `const T&` | `value` | - |

---

(luaobjectgetluafield)=
## `LuaObject::getLuaField`

**Signature:**
```cpp
template<typename T> T LuaObject::getLuaField(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

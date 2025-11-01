---
title: "src/framework/luaengine/luabinder.h"
source_file: "src/framework/luaengine/luabinder.h"
generated_at: "2025-11-01T08:45:15.308Z"
doc_type: "cpp_api"
---

# src/framework/luaengine/luabinder.h

(luaexception)=
## `LuaException`

**Signature:**
```cpp
throw LuaException("failed to call a member function because the passed object is nil");
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `"failed to call a member function because the passed object is nil"` | - | - |

**Returns:**
- `throw`

---

(luaexception-1)=
## `LuaException`

**Signature:**
```cpp
throw LuaException("failed to call a member function because the passed object is nil");
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `"failed to call a member function because the passed object is nil"` | - | - |

**Returns:**
- `throw`

---

(call)=
## `call`

**Signature:**
```cpp
static void call(Tuple& tuple, LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Tuple&` | `tuple` | - |
| `LuaInterface*` | `lua` | - |

---

(call-1)=
## `call`

**Signature:**
```cpp
static void call(Tuple& tuple, LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Tuple&` | `tuple` | - |
| `LuaInterface*` | `lua` | - |

---

(call-2)=
## `call`

**Signature:**
```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |
| `const F&` | `f` | - |
| `LuaInterface*` | `lua` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(call-3)=
## `call`

**Signature:**
```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |
| `const F&` | `f` | - |
| `LuaInterface*` | `lua` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(bind_fun_specializer)=
## `bind_fun_specializer`

Bind different types of functions generating a lambda

**Signature:**
```cpp
LuaCppFunction bind_fun_specializer(const F& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const F&` | `f` | - |

**Returns:**
- `LuaCppFunction`

---

(bind_fun)=
## `bind_fun`

Bind a customized function

**Signature:**
```cpp
inline LuaCppFunction bind_fun(const std::function<int(LuaInterface*)>& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::function&lt;int(LuaInterface*)&gt;&` | `f` | - |

**Returns:**
- `LuaCppFunction`

---

(bind_fun-1)=
## `bind_fun`

Bind a std::function

**Signature:**
```cpp
LuaCppFunction bind_fun(const std::function<Ret(Args...)>& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::function&lt;Ret(Args...)&gt;&` | `f` | - |

**Returns:**
- `LuaCppFunction`

---

(call-4)=
## `call`

**Signature:**
```cpp
static LuaCppFunction call(const Lambda& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Lambda&` | `f` | - |

**Returns:**
- `LuaCppFunction`

---

(stdenable_ifstdis_constructibledecltype)=
## `std::enable_if<std::is_constructible<decltype`

**Signature:**
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, LuaCppFunction>::type bind_fun(const Lambda& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `&Lambda::operator())&gt;::value, LuaCppFunction&gt;::type bind_fun(const Lambda&` | `f` | - |

**Returns:**
- `typename`

---

(bind_fun-2)=
## `bind_fun`

Convert to C++ functions pointers to std::function then bind

**Signature:**
```cpp
LuaCppFunction bind_fun(Ret (*f)(Args...));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Ret (*f)(Args...)` | - | - |

**Returns:**
- `LuaCppFunction`

---

(bind_mem_fun)=
## `bind_mem_fun`

Bind member functions

**Signature:**
```cpp
LuaCppFunction bind_mem_fun(Ret (FC::* f)(Args...));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Ret (FC::* f)(Args...)` | - | - |

**Returns:**
- `LuaCppFunction`

---

(bind_singleton_mem_fun)=
## `bind_singleton_mem_fun`

Bind singleton member functions

**Signature:**
```cpp
LuaCppFunction bind_singleton_mem_fun(Ret (FC::*f)(Args...), C *instance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Ret (FC::*f)(Args...)` | - | - |
| `C *instance` | - | - |

**Returns:**
- `LuaCppFunction`

---

(bind_mem_fun-1)=
## `bind_mem_fun`

Bind customized member functions

**Signature:**
```cpp
LuaCppFunction bind_mem_fun(int (C::*f)(LuaInterface*));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int (C::*f)(LuaInterface*)` | - | - |

**Returns:**
- `LuaCppFunction`

---

---
title: "src/framework/luaengine/luavaluecasts.h"
source_file: "src/framework/luaengine/luavaluecasts.h"
generated_at: "2025-11-01T04:06:42.758Z"
doc_type: "cpp_api"
---

# src/framework/luaengine/luavaluecasts.h

(push_internal_luavalue)=
## `push_internal_luavalue`

**Signature:**
```cpp
int push_internal_luavalue(T v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `v` | - |

**Returns:**
- `int`

---

(push_luavalue)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(bool b);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `b` | - |

**Returns:**
- `int`

---

(luavalue_cast)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, bool& b);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `bool&` | `b` | - |

**Returns:**
- `bool`

---

(push_luavalue-1)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(int i);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `i` | - |

**Returns:**
- `int`

---

(luavalue_cast-1)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, int& i);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `int&` | `i` | - |

**Returns:**
- `bool`

---

(push_luavalue-2)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(double d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `d` | - |

**Returns:**
- `int`

---

(luavalue_cast-2)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, double& d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `double&` | `d` | - |

**Returns:**
- `bool`

---

(push_luavalue-3)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const char* cstr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `cstr` | - |

**Returns:**
- `int`

---

(push_luavalue-4)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |

**Returns:**
- `int`

---

(luavalue_cast-3)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::string&` | `str` | - |

**Returns:**
- `bool`

---

(push_luavalue-5)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const LuaCppFunction& func);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const LuaCppFunction&` | `func` | - |

**Returns:**
- `int`

---

(push_luavalue-6)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

**Returns:**
- `int`

---

(luavalue_cast-4)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `Color&` | `color` | - |

**Returns:**
- `bool`

---

(push_luavalue-7)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

**Returns:**
- `int`

---

(luavalue_cast-5)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `Rect&` | `rect` | - |

**Returns:**
- `bool`

---

(push_luavalue-8)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const Point& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |

**Returns:**
- `int`

---

(luavalue_cast-6)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, Point& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `Point&` | `point` | - |

**Returns:**
- `bool`

---

(push_luavalue-9)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

**Returns:**
- `int`

---

(luavalue_cast-7)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `Size&` | `size` | - |

**Returns:**
- `bool`

---

(push_luavalue-10)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const OTMLNodePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `node` | - |

**Returns:**
- `int`

---

(luavalue_cast-8)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, OTMLNodePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `OTMLNodePtr&` | `node` | - |

**Returns:**
- `bool`

---

(luavalue_cast-9)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, LuaObjectPtr& obj);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `LuaObjectPtr&` | `obj` | - |

**Returns:**
- `bool`

---

(push_luavalue-11)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::function<Ret(Args...)>& func);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::function&lt;Ret(Args...)&gt;&` | `func` | - |

**Returns:**
- `int`

---

(luavalue_cast-10)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::function<void(Args...)>& func);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::function&lt;void(Args...)&gt;&` | `func` | - |

**Returns:**
- `bool`

---

(push_luavalue-12)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::list<T>& list);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::list&lt;T&gt;&` | `list` | - |

**Returns:**
- `int`

---

(luavalue_cast-11)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::list<T>& list);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::list&lt;T&gt;&` | `list` | - |

**Returns:**
- `bool`

---

(push_luavalue-13)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::vector<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;T&gt;&` | `vec` | - |

**Returns:**
- `int`

---

(luavalue_cast-12)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::vector<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::vector&lt;T&gt;&` | `vec` | - |

**Returns:**
- `bool`

---

(push_luavalue-14)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::set<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::set&lt;T&gt;&` | `vec` | - |

**Returns:**
- `int`

---

(luavalue_cast-13)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::set<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::set&lt;T&gt;&` | `vec` | - |

**Returns:**
- `bool`

---

(push_luavalue-15)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::deque<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::deque&lt;T&gt;&` | `vec` | - |

**Returns:**
- `int`

---

(luavalue_cast-14)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::deque<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::deque&lt;T&gt;&` | `vec` | - |

**Returns:**
- `bool`

---

(push_luavalue-16)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::map<K, V>& map);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::map&lt;K, V&gt;&` | `map` | - |

**Returns:**
- `int`

---

(luavalue_cast-15)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::map<K, V>& map);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::map&lt;K, V&gt;&` | `map` | - |

**Returns:**
- `bool`

---

(luavalue_cast-16)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::pair<K, V>& pair);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::pair&lt;K, V&gt;&` | `pair` | - |

**Returns:**
- `bool`

---

(push_luavalue-17)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::tuple<Args...>& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::tuple&lt;Args...&gt;&` | `tuple` | - |

**Returns:**
- `int`

---

(push_internal_luavalue-1)=
## `push_internal_luavalue`

**Signature:**
```cpp
int push_internal_luavalue(const std::tuple<Args...>& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::tuple&lt;Args...&gt;&` | `tuple` | - |

**Returns:**
- `int`

---

(luaexception)=
## `LuaException`

**Signature:**
```cpp
throw LuaException("a function from lua didn't retrieve the expected number of results", 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `"a function from lua didn't retrieve the expected number of results"` | - | - |
| `0` | - | - |

**Returns:**
- `throw`

---

(luaexception-1)=
## `LuaException`

**Signature:**
```cpp
throw LuaException("attempt to call an expired lua function from C++," "did you forget to hold a reference for that function?", 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `"attempt to call an expired lua function from C++` | - | - |
| `" "did you forget to hold a reference for that function?"` | - | - |
| `0` | - | - |

**Returns:**
- `throw`

---

(push_luavalue-18)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(float f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `f` | - |

**Returns:**
- `int`

---

(luavalue_cast-17)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, float& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `float&` | `f` | - |

**Returns:**
- `bool`

---

(push_luavalue-19)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(int8 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int8` | `v` | - |

**Returns:**
- `int`

---

(luavalue_cast-18)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, int8& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `int8&` | `v` | - |

**Returns:**
- `bool`

---

(push_luavalue-20)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(uint8 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `v` | - |

**Returns:**
- `int`

---

(luavalue_cast-19)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, uint8& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `uint8&` | `v` | - |

**Returns:**
- `bool`

---

(push_luavalue-21)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(int16 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int16` | `v` | - |

**Returns:**
- `int`

---

(luavalue_cast-20)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, int16& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `int16&` | `v` | - |

**Returns:**
- `bool`

---

(push_luavalue-22)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(uint16 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `v` | - |

**Returns:**
- `int`

---

(luavalue_cast-21)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, uint16& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `uint16&` | `v` | - |

**Returns:**
- `bool`

---

(push_luavalue-23)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(uint32 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `v` | - |

**Returns:**
- `int`

---

(luavalue_cast-22)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, uint32& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `uint32&` | `v` | - |

**Returns:**
- `bool`

---

(push_luavalue-24)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(int64 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int64` | `v` | - |

**Returns:**
- `int`

---

(luavalue_cast-23)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, int64& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `int64&` | `v` | - |

**Returns:**
- `bool`

---

(push_luavalue-25)=
## `push_luavalue`

**Signature:**
```cpp
inline int push_luavalue(uint64 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint64` | `v` | - |

**Returns:**
- `int`

---

(luavalue_cast-24)=
## `luavalue_cast`

**Signature:**
```cpp
inline bool luavalue_cast(int index, uint64& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `uint64&` | `v` | - |

**Returns:**
- `bool`

---

(push_internal_luavalue-2)=
## `push_internal_luavalue`

**Signature:**
```cpp
int push_internal_luavalue(T v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `v` | - |

**Returns:**
- `int`

---

(push_luavalue-26)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::function<Ret(Args...)>& func);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::function&lt;Ret(Args...)&gt;&` | `func` | - |

**Returns:**
- `int`

---

(luavalue_cast-25)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::function<void(Args...)>& func);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::function&lt;void(Args...)&gt;&` | `func` | - |

**Returns:**
- `bool`

---

(push_luavalue-27)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::list<T>& list);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::list&lt;T&gt;&` | `list` | - |

**Returns:**
- `int`

---

(luavalue_cast-26)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::list<T>& list);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::list&lt;T&gt;&` | `list` | - |

**Returns:**
- `bool`

---

(push_luavalue-28)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::vector<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;T&gt;&` | `vec` | - |

**Returns:**
- `int`

---

(luavalue_cast-27)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::vector<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::vector&lt;T&gt;&` | `vec` | - |

**Returns:**
- `bool`

---

(push_luavalue-29)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::set<T>& set);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::set&lt;T&gt;&` | `set` | - |

**Returns:**
- `int`

---

(luavalue_cast-28)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::set<T>& set);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::set&lt;T&gt;&` | `set` | - |

**Returns:**
- `bool`

---

(push_luavalue-30)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::deque<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::deque&lt;T&gt;&` | `vec` | - |

**Returns:**
- `int`

---

(luavalue_cast-29)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::deque<T>& vec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::deque&lt;T&gt;&` | `vec` | - |

**Returns:**
- `bool`

---

(push_luavalue-31)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::map<K, V>& map);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::map&lt;K, V&gt;&` | `map` | - |

**Returns:**
- `int`

---

(luavalue_cast-30)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::map<K, V>& map);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::map&lt;K, V&gt;&` | `map` | - |

**Returns:**
- `bool`

---

(luavalue_cast-31)=
## `luavalue_cast`

**Signature:**
```cpp
bool luavalue_cast(int index, std::pair<K, V>& pair);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `std::pair&lt;K, V&gt;&` | `pair` | - |

**Returns:**
- `bool`

---

(call)=
## `call`

**Signature:**
```cpp
static void call(const Tuple& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |

---

(call-1)=
## `call`

**Signature:**
```cpp
static void call(const Tuple& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |

---

(push_internal_luavalue-3)=
## `push_internal_luavalue`

**Signature:**
```cpp
int push_internal_luavalue(const std::tuple<Args...>& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::tuple&lt;Args...&gt;&` | `tuple` | - |

**Returns:**
- `int`

---

(call-2)=
## `call`

**Signature:**
```cpp
static void call(const Tuple& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |

---

(call-3)=
## `call`

**Signature:**
```cpp
static void call(const Tuple& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |

---

(push_luavalue-32)=
## `push_luavalue`

**Signature:**
```cpp
int push_luavalue(const std::tuple<Args...>& tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::tuple&lt;Args...&gt;&` | `tuple` | - |

**Returns:**
- `int`

---

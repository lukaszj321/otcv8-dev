# src/framework/luaengine/luavaluecasts.h

```cpp
int push_internal_luavalue(T v);
```
```cpp
int push_luavalue(bool b);
```
```cpp
bool luavalue_cast(int index, bool& b);
```
```cpp
int push_luavalue(int i);
```
```cpp
bool luavalue_cast(int index, int& i);
```
```cpp
int push_luavalue(double d);
```
```cpp
bool luavalue_cast(int index, double& d);
```
```cpp
inline int push_luavalue(float f) { push_luavalue((double)f);
```
```cpp
inline bool luavalue_cast(int index, float& f) { double d; bool r = luavalue_cast(index, d);
```
```cpp
inline int push_luavalue(int8 v) { push_luavalue((int)v);
```
```cpp
inline bool luavalue_cast(int index, int8& v) { int i; bool r = luavalue_cast(index, i);
```
```cpp
inline int push_luavalue(uint8 v) { push_luavalue((int)v);
```
```cpp
inline bool luavalue_cast(int index, uint8& v){ int i; bool r = luavalue_cast(index, i);
```
```cpp
inline int push_luavalue(int16 v) { push_luavalue((int)v);
```
```cpp
inline bool luavalue_cast(int index, int16& v){ int i; bool r = luavalue_cast(index, i);
```
```cpp
inline int push_luavalue(uint16 v) { push_luavalue((int)v);
```
```cpp
inline bool luavalue_cast(int index, uint16& v){ int i; bool r = luavalue_cast(index, i);
```
```cpp
inline int push_luavalue(uint32 v) { push_luavalue((double)v);
```
```cpp
inline bool luavalue_cast(int index, uint32& v) { double d; bool r = luavalue_cast(index, d);
```
```cpp
inline int push_luavalue(int64 v) { push_luavalue((double)v);
```
```cpp
inline bool luavalue_cast(int index, int64& v) { double d; bool r = luavalue_cast(index, d);
```
```cpp
inline int push_luavalue(uint64 v) { push_luavalue((double)v);
```
```cpp
inline bool luavalue_cast(int index, uint64& v) { double d; bool r = luavalue_cast(index, d);
```
```cpp
int push_luavalue(const char* cstr);
```
```cpp
int push_luavalue(const std::string& str);
```
```cpp
bool luavalue_cast(int index, std::string& str);
```
```cpp
int push_luavalue(const LuaCppFunction& func);
```
```cpp
int push_luavalue(const Color& color);
```
```cpp
bool luavalue_cast(int index, Color& color);
```
```cpp
int push_luavalue(const Rect& rect);
```
```cpp
bool luavalue_cast(int index, Rect& rect);
```
```cpp
int push_luavalue(const Point& point);
```
```cpp
bool luavalue_cast(int index, Point& point);
```
```cpp
int push_luavalue(const Size& size);
```
```cpp
bool luavalue_cast(int index, Size& size);
```
```cpp
int push_luavalue(const OTMLNodePtr& node);
```
```cpp
bool luavalue_cast(int index, OTMLNodePtr& node);
```
```cpp
int push_luavalue(const std::function<Ret(Args...)>& func);
```
```cpp
bool luavalue_cast(int index, std::function<void(Args...)>& func);
```
```cpp
int push_luavalue(const std::list<T>& list);
```
```cpp
bool luavalue_cast(int index, std::list<T>& list);
```
```cpp
int push_luavalue(const std::vector<T>& vec);
```
```cpp
bool luavalue_cast(int index, std::vector<T>& vec);
```
```cpp
int push_luavalue(const std::set<T>& vec);
```
```cpp
bool luavalue_cast(int index, std::set<T>& vec);
```
```cpp
int push_luavalue(const std::deque<T>& vec);
```
```cpp
bool luavalue_cast(int index, std::deque<T>& vec);
```
```cpp
int push_luavalue(const std::map<K, V>& map);
```
```cpp
bool luavalue_cast(int index, std::map<K, V>& map);
```
```cpp
bool luavalue_cast(int index, std::pair<K, V>& pair);
```
```cpp
int push_luavalue(const std::tuple<Args...>& tuple);
```
```cpp
int push_internal_luavalue(const std::tuple<Args...>& tuple);
```
```cpp
int push_internal_luavalue(T v) { return push_luavalue(v);
```
```cpp
int push_luavalue(const std::function<Ret(Args...)>& func) { if(func) { LuaCppFunction f = luabinder::bind_fun(func);
```
```cpp
bool luavalue_cast(int index, std::function<void(Args...)>& func) { if(g_lua.isFunction(index)) { g_lua.pushValue(index);
```
```cpp
int push_luavalue(const std::list<T>& list) { g_lua.createTable(list.size(), 0);
```
```cpp
bool luavalue_cast(int index, std::list<T>& list) { if(g_lua.isTable(index)) { g_lua.pushNil();
```
```cpp
int push_luavalue(const std::vector<T>& vec) { g_lua.createTable(vec.size(), 0);
```
```cpp
bool luavalue_cast(int index, std::vector<T>& vec) { if (g_lua.isTable(index)) { g_lua.pushNil();
```
```cpp
int push_luavalue(const std::set<T>& set) { g_lua.createTable(set.size(), 0);
```
```cpp
bool luavalue_cast(int index, std::set<T>& set) { if (g_lua.isTable(index)) { g_lua.pushNil();
```
```cpp
int push_luavalue(const std::deque<T>& vec) { g_lua.createTable(vec.size(), 0);
```
```cpp
bool luavalue_cast(int index, std::deque<T>& vec) { if(g_lua.isTable(index)) { g_lua.pushNil();
```
```cpp
int push_luavalue(const std::map<K, V>& map) { g_lua.newTable();
```
```cpp
bool luavalue_cast(int index, std::map<K, V>& map) { if(g_lua.isTable(index)) { g_lua.pushNil();
```
```cpp
bool luavalue_cast(int index, std::pair<K, V>& pair) { if (g_lua.isTable(index)) { g_lua.pushNil();
```
```cpp
static void call(const Tuple& tuple) { push_internal_luavalue(std::get<N-1>(tuple));
```
```cpp
static void call(const Tuple& tuple) { } }; template<typename... Args> int push_internal_luavalue(const std::tuple<Args...>& tuple) { g_lua.newTable();
```
```cpp
static void call(const Tuple& tuple) { push_internal_luavalue(std::get<std::tuple_size<Tuple>::value - N>(tuple));
```
```cpp
static void call(const Tuple& tuple) { } }; template<typename... Args> int push_luavalue(const std::tuple<Args...>& tuple) { push_tuple_luavalue<sizeof...(Args)>::call(tuple);
```
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
bool luavalue_cast(int index, LuaObjectPtr& obj);
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
return push_luavalue(v);
```
```cpp
throw LuaException("a function from lua didn't retrieve the expected number of results", 0);
```
```cpp
throw LuaException("attempt to call an expired lua function from C++," "did you forget to hold a reference for that function?", 0);
```
```cpp
return Ret();
```
```cpp
inline int push_luavalue(float f);
```
```cpp
inline bool luavalue_cast(int index, float& f);
```
```cpp
inline int push_luavalue(int8 v);
```
```cpp
inline bool luavalue_cast(int index, int8& v);
```
```cpp
inline int push_luavalue(uint8 v);
```
```cpp
inline bool luavalue_cast(int index, uint8& v);
```
```cpp
inline int push_luavalue(int16 v);
```
```cpp
inline bool luavalue_cast(int index, int16& v);
```
```cpp
inline int push_luavalue(uint16 v);
```
```cpp
inline bool luavalue_cast(int index, uint16& v);
```
```cpp
inline int push_luavalue(uint32 v);
```
```cpp
inline bool luavalue_cast(int index, uint32& v);
```
```cpp
inline int push_luavalue(int64 v);
```
```cpp
inline bool luavalue_cast(int index, int64& v);
```
```cpp
inline int push_luavalue(uint64 v);
```
```cpp
inline bool luavalue_cast(int index, uint64& v);
```
```cpp
int push_internal_luavalue(T v);
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
int push_luavalue(const std::set<T>& set);
```
```cpp
bool luavalue_cast(int index, std::set<T>& set);
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
static void call(const Tuple& tuple);
```
```cpp
static void call(const Tuple& tuple);
```
```cpp
int push_internal_luavalue(const std::tuple<Args...>& tuple);
```
```cpp
static void call(const Tuple& tuple);
```
```cpp
static void call(const Tuple& tuple);
```
```cpp
int push_luavalue(const std::tuple<Args...>& tuple);
```
# src/framework/luaengine/luaobject.h

```cpp
public:
    LuaObject();
```
```cpp
void connectLuaField(const std::string& field, const std::function<T>& f, bool pushFront = false);
```
```cpp
int luaCallLuaField(const std::string& field, const T&... args);
```
Calls a function or table of functions stored in a lua field, results are pushed onto the stack,
if any lua error occurs, it will be reported to stdout and return 0 results
@return the number of results

```cpp
void callLuaField(const std::string& field, const T&... args);
```
```cpp
bool hasLuaField(const std::string& field);
```
Returns true if the lua field exists

```cpp
void setLuaField(const std::string& key, const T& value);
```
Sets a field in this lua object

```cpp
void connect(const LuaObjectPtr& obj, const std::string& field, const std::function<F>& f, bool pushFront = false);
```
Gets a field from this lua object

```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, void>::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront = false);
```
```cpp
void LuaObject::connectLuaField(const std::string& field, const std::function<T>& f, bool pushFront) { luaGetField(field);
```
```cpp
void connect(const LuaObjectPtr& obj, const std::string& field, const std::function<F>& f, bool pushFront) { obj->connectLuaField<F>(field, f, pushFront);
```
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, void>::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront) { typedef decltype(&Lambda::operator()) F; luabinder::connect_lambda<F>::call(obj, field, f, pushFront);
```
```cpp
int LuaObject::luaCallLuaField(const std::string& field, const T&... args) { AutoStat s(STATS_LUA, getClassName() + ":" + field);
```
```cpp
void LuaObject::callLuaField(const std::string& field, const T&... args) { int rets = luaCallLuaField(field, args...);
```
```cpp
void LuaObject::setLuaField(const std::string& key, const T& value) { g_lua.polymorphicPush(value);
```
```cpp
template<typename T>
T LuaObject::getLuaField(const std::string& key) { luaGetField(key);
```
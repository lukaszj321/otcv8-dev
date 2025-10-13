# src/framework/luaengine/luaobject.h

```cpp
public: LuaObject();
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
template<typename T> T getLuaField(const std::string& key);
```
Gets a field from this lua object

```cpp
void releaseLuaFieldsTable();
```
Release fields table reference

```cpp
void luaSetField(const std::string& key);
```
Sets a field from this lua object, the value must be on the stack

```cpp
void luaGetField(const std::string& key);
```
Gets a field from this lua object, the result is pushed onto the stack

```cpp
void luaGetMetatable();
```
Get object's metatable

```cpp
void luaGetFieldsTable();
```
Gets the table containing all stored fields of this lua object, the result is pushed onto the stack

```cpp
int getUseCount();
```
Returns the number of references of this object
@note each userdata of this object on lua counts as a reference

```cpp
std::string getClassName();
```
Returns the derived class name, its the same name used in Lua

```cpp
void connect(const LuaObjectPtr& obj, const std::string& field, const std::function<F>& f, bool pushFront = false);
```
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, void>::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront = false);
```
```cpp
AutoStat s(STATS_LUA, getClassName() + ":" + field);
```
```cpp
LuaObjectPtr asLuaObject();
```
```cpp
void LuaObject::connectLuaField(const std::string& field, const std::function<T>& f, bool pushFront);
```
```cpp
void connect(const LuaObjectPtr& obj, const std::string& field, const std::function<F>& f, bool pushFront);
```
```cpp
static void call(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront);
```
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, void>::type connect(const LuaObjectPtr& obj, const std::string& field, const Lambda& f, bool pushFront);
```
```cpp
int LuaObject::luaCallLuaField(const std::string& field, const T&... args);
```
```cpp
void LuaObject::callLuaField(const std::string& field, const T&... args);
```
```cpp
void LuaObject::setLuaField(const std::string& key, const T& value);
```
```cpp
template<typename T> T LuaObject::getLuaField(const std::string& key);
```
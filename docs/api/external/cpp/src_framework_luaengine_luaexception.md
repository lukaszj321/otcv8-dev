# src/framework/luaengine/luaexception.h

```cpp
public: LuaException(const std::string& error, int traceLevel = -1);
```
```cpp
void generateLuaErrorMessage(const std::string& error, int traceLevel);
```
```cpp
public: LuaBadNumberOfArgumentsException(int expected = -1, int got = -1);
```
```cpp
public: LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName);
```
```cpp
virtual const char* what() const throw();
```
```cpp
protected: LuaException();
```
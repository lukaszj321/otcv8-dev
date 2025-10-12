# src/framework/luaengine/luaexception.h

```cpp
public:
    LuaException(const std::string& error, int traceLevel = -1);
```
```cpp
void generateLuaErrorMessage(const std::string& error, int traceLevel);
```
```cpp
virtual const char* what() const throw() { return m_what.c_str();
```
```cpp
protected:
    LuaException() { } std::string m_what; }; class LuaBadNumberOfArgumentsException : public LuaException { public: LuaBadNumberOfArgumentsException(int expected = -1, int got = -1);
```
```cpp
public:
    LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName);
```
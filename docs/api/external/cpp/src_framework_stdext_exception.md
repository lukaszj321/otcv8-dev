# src/framework/stdext/exception.h

```cpp
public:
    exception() { } exception(const std::string& what) : m_what(what) { } virtual ~exception() throw() { }; virtual const char* what() const throw() { return m_what.c_str();
```
```cpp
inline void throw_exception(const std::string& what) { throw exception(what);
```
Throws a generic exception

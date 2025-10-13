# src/framework/stdext/exception.h

```cpp
public: exception();
```
```cpp
virtual const char* what() const throw();
```
```cpp
inline void throw_exception(const std::string& what);
```
Throws a generic exception

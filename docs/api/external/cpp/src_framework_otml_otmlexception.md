# src/framework/otml/otmlexception.h

```cpp
public:
    OTMLException(const OTMLNodePtr& node, const std::string& error);
```
```cpp
virtual const char* what() const throw() { return m_what.c_str();
```
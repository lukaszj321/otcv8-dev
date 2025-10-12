# src/framework/stdext/demangle.h

```cpp
const char* demangle_name(const char* name);
```
Demangle names for GNU g++ compiler

```cpp
std::string demangle_class() { #ifdef _MSC_VER return demangle_name(typeid(T).name()) + 6; #else return demangle_name(typeid(T).name());
```
Returns the name of a class

```cpp
std::string demangle_type() { return demangle_name(typeid(T).name());
```
Returns the name of a type

# src/framework/stdext/demangle.h

```cpp
const char* demangle_name(const char* name);
```
Demangle names for GNU g++ compiler

```cpp
return demangle_name(typeid(T).name());
```
```cpp
std::string demangle_class();
```
Returns the name of a class

```cpp
std::string demangle_type();
```
Returns the name of a type

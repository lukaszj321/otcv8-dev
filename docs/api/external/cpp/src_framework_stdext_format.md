# src/framework/stdext/format.h

```cpp
return _snprintf(s, maxlen, format, args...);
```
```cpp
return snprintf(s, maxlen, format, args...);
```
```cpp
return expand_snprintf<std::tuple_size<decltype(tuple)>::value>::call(s, maxlen, format, tuple);
```
```cpp
return strlen(s);
```
```cpp
std::string buffer(n + 1, '\0');
```
```cpp
void print_ostream(std::ostringstream& stream, const T& last);
```
```cpp
void print_ostream(std::ostringstream& stream, const T& first, const Args&... rest);
```
```cpp
void print(const T&... args);
```
```cpp
static int call(char *s, size_t maxlen, const char *format, const Tuple& tuple, const Args&... args);
```
```cpp
static int call(char *s, size_t maxlen, const char *format, const Tuple& tuple, const Args&... args);
```
```cpp
int snprintf(char *s, size_t maxlen, const char *format, const Args&... args);
```
```cpp
inline int snprintf(char *s, size_t maxlen, const char *format);
```
```cpp
inline std::string format();
```
```cpp
inline std::string format(const std::string& format);
```
```cpp
std::string format(const std::string& format, const Args&... args);
```
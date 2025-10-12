# src/framework/stdext/format.h

```cpp
void print_ostream(std::ostringstream& stream, const T& last) { stream << last; } template<class T, class... Args> void print_ostream(std::ostringstream& stream, const T& first, const Args&... rest) { stream << "\t" << first; print_ostream(stream, rest...);
```
```cpp
static int call(char *s, size_t maxlen, const char *format, const Tuple& tuple, const Args&... args) { return expand_snprintf<N-1>::call(s, maxlen, format, tuple, sprintf_cast(std::get<N-1>(tuple)), args...);
```
```cpp
static int call(char *s, size_t maxlen, const char *format, const Tuple& tuple, const Args&... args) { #ifdef _MSC_VER return _snprintf(s, maxlen, format, args...);
```
```cpp
return snprintf(s, maxlen, format, args...);
```
```cpp
int snprintf(char *s, size_t maxlen, const char *format, const Args&... args) { std::tuple<typename replace_extent<Args>::type...> tuple(args...);
```
```cpp
return expand_snprintf<std::tuple_size<decltype(tuple)>::value>::call(s, maxlen, format, tuple);
```
```cpp
inline int snprintf(char *s, size_t maxlen, const char *format) { std::strncpy(s, format, maxlen);
```
```cpp
return strlen(s);
```
```cpp
inline std::string format() { return std::string();
```
```cpp
inline std::string format(const std::string& format) { return format; } // Format strings with the sprintf style, accepting std::string and string convertible types for %s template<typename... Args> std::string format(const std::string& format, const Args&... args) { int n = snprintf(NULL, 0, format.c_str(), args...);
```
```cpp
std::string buffer(n + 1, '\0');
```
# src/framework/stdext/string.h

```cpp
std::string to_string(const T& t) { return unsafe_cast<std::string, T>(t);
```
```cpp
std::vector<T> split(const std::string& str, const std::string& separators = " ") { std::vector<std::string> splitted = split(str, separators);
```
```cpp
std::vector<T> results(splitted.size());
```
# src/framework/stdext/string.h

```cpp
std::string resolve_path(const std::string& filePath, std::string sourcePath);
```
Resolve a file path by combining sourcePath with filePath

```cpp
std::string date_time_string();
```
Get current date and time in a std::string

```cpp
std::string timestamp_to_date(time_t tnow);
```
```cpp
std::string dec_to_hex(uint32_t num);
```
```cpp
std::string dec_to_hex(uint64_t num);
```
```cpp
uint64_t hex_to_dec(const std::string& str);
```
```cpp
void tolower(std::string& str);
```
```cpp
void toupper(std::string& str);
```
```cpp
void trim(std::string& str);
```
```cpp
void ucwords(std::string& str);
```
```cpp
char upchar(char c);
```
```cpp
char lochar(char c);
```
```cpp
bool ends_with(const std::string& str, const std::string& test);
```
```cpp
bool starts_with(const std::string& str, const std::string& test);
```
```cpp
void replace_all(std::string& str, const std::string& search, const std::string& replacement);
```
```cpp
bool is_valid_utf8(const std::string& src);
```
```cpp
std::string utf8_to_latin1(const std::string& src);
```
```cpp
std::string latin1_to_utf8(const std::string& src);
```
```cpp
std::wstring utf8_to_utf16(const std::string& src);
```
```cpp
std::string utf16_to_utf8(const std::wstring& src);
```
```cpp
std::string utf16_to_latin1(const std::wstring& src);
```
```cpp
std::wstring latin1_to_utf16(const std::string& src);
```
```cpp
std::vector<std::string> split(const std::string& str, const std::string& separators = " ");
```
```cpp
std::vector<T> results(splitted.size());
```
```cpp
std::string to_string(const T& t);
```
```cpp
template<typename T> T from_string(const std::string& str, T def = T());
```
```cpp
std::vector<T> split(const std::string& str, const std::string& separators = " ");
```
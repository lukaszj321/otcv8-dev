# src/framework/xml/tinystr.h

```cpp
return assign(copy, (size_type)strlen(copy));
```
```cpp
return assign(copy.start(), copy.length());
```
```cpp
return append(suffix, static_cast<size_type>( strlen(suffix) ));
```
```cpp
return append(&single, 1);
```
```cpp
return append(suffix.data(), suffix.length());
```
```cpp
return find(lookup, 0);
```
```cpp
void reserve(size_type cap);
```
```cpp
TiXmlString& assign(const char* str, size_type len);
```
```cpp
TiXmlString& append(const char* str, size_type len);
```
```cpp
TIXML_EXPLICIT TiXmlString(const char * copy) : rep_(0);
```
```cpp
TIXML_EXPLICIT TiXmlString(const char * str, size_type len) : rep_(0);
```
```cpp
const char * c_str();
```
```cpp
const char * data();
```
```cpp
size_type length();
```
```cpp
size_type size();
```
```cpp
bool empty();
```
```cpp
size_type capacity();
```
```cpp
const char& at(size_type index);
```
```cpp
size_type find(char lookup);
```
```cpp
size_type find(char tofind, size_type offset);
```
```cpp
void clear();
```
```cpp
void swap(TiXmlString& other);
```
```cpp
private: void init(size_type sz);
```
```cpp
void set_size(size_type sz);
```
```cpp
char* start();
```
```cpp
char* finish();
```
```cpp
void init(size_type sz, size_type cap);
```
```cpp
void quit();
```
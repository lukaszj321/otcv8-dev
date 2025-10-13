# src/framework/stdext/cast.h

```cpp
bool cast(const T& in, R& out);
```
```cpp
bool cast(const T& in, std::string& out);
```
```cpp
template<> inline bool cast(const std::string& in, std::string& out);
```
```cpp
template<> inline bool cast(const std::string& in, bool& b);
```
```cpp
template<> inline bool cast(const std::string& in, char& c);
```
```cpp
template<> inline bool cast(const std::string& in, long& l);
```
```cpp
template<> inline bool cast(const std::string& in, int& i);
```
```cpp
template<> inline bool cast(const std::string& in, double& d);
```
```cpp
template<> inline bool cast(const std::string& in, float& f);
```
```cpp
template<> inline bool cast(const bool& in, std::string& out);
```
```cpp
void update_what();
```
```cpp
virtual const char* what() const throw();
```
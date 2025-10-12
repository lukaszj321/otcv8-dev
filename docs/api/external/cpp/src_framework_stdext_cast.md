# src/framework/stdext/cast.h

```cpp
bool cast(const T& in, R& out) { std::stringstream ss; ss << in; ss >> out; return !!ss && ss.eof();
```
```cpp
bool cast(const T& in, std::string& out) { std::stringstream ss; ss << in; out = ss.str();
```
```cpp
inline bool cast(const std::string& in, std::string& out) { out = in; return true; } // special cast from string to boolean template<> inline bool cast(const std::string& in, bool& b) { if(in == "true") b = true; else if(in == "false") b = false; else return false; return true; } // special cast from string to char template<> inline bool cast(const std::string& in, char& c) { if(in.length() != 1) return false; c = in[0]; return true; } // special cast from string to long template<> inline bool cast(const std::string& in, long& l) { if(in.find_first_not_of("-0123456789") != std::string::npos) return false; std::size_t t = in.find_last_of('-');
```
```cpp
inline bool cast(const std::string& in, int& i) { long l; if(cast(in, l)) { i=l; return true; } return false; } // special cast from string to double template<> inline bool cast(const std::string& in, double& d) { if(in.find_first_not_of("-0123456789.") != std::string::npos) return false; std::size_t t = in.find_last_of('-');
```
```cpp
inline bool cast(const std::string& in, float& f) { double d; if(cast(in, d)) { f=(float)d; return true; } return false; } // special cast from boolean to string template<> inline bool cast(const bool& in, std::string& out) { out = (in ? "true" : "false");
```
```cpp
void update_what() { std::stringstream ss; ss << "failed to cast value of type '" << demangle_type<T>() << "' to type '" << demangle_type<R>() << "'"; m_what = ss.str();
```
```cpp
virtual const char* what() const throw() { return m_what.c_str();
```
# src/framework/xml/tinystr.h

```cpp
TIXML_EXPLICIT TiXmlString(const char * copy) : rep_(0) { init( static_cast<size_type>( strlen(copy) ));
```
```cpp
TIXML_EXPLICIT TiXmlString(const char * str, size_type len) : rep_(0) { init(len);
```
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
const char * c_str() const { return rep_->str; } // Convert a TiXmlString into a char * (need not be null terminated). const char * data () const { return rep_->str; } // Return the length of a TiXmlString size_type length () const { return rep_->size; } // Alias for length() size_type size () const { return rep_->size; } // Checks if a TiXmlString is empty bool empty () const { return rep_->size == 0; } // Return capacity of string size_type capacity () const { return rep_->capacity; } // single char extraction const char& at (size_type index) const { VALIDATE( index < length());
```
```cpp
size_type find(char lookup) const { return find(lookup, 0);
```
```cpp
size_type find(char tofind, size_type offset) const { if (offset >= length()) return npos; for (const char* p = c_str() + offset; *p != '\0'; ++p) { if (*p == tofind) return static_cast< size_type >( p - c_str());
```
```cpp
void clear() { //Lee: //The original was just too strange, though correct: // TiXmlString().swap(*this);
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
void swap(TiXmlString& other) { Rep* r = rep_; rep_ = other.rep_; other.rep_ = r; } private: void init(size_type sz) { init(sz, sz);
```
```cpp
void set_size(size_type sz) { rep_->str[ rep_->size = sz ] = '\0'; } char* start() const { return rep_->str; } char* finish() const { return rep_->str + rep_->size; } struct Rep { size_type size, capacity; char str[1]; }; void init(size_type sz, size_type cap) { if (cap) { // Lee: the original form: // rep_ = static_cast<Rep*>(operator new(sizeof(Rep) + cap));
```
```cpp
void quit() { if (rep_ != &nullrep_) { // The rep_ is really an array of ints. (see the allocator, above). // Cast it back before delete, so the compiler won't incorrectly call destructors. delete [] ( reinterpret_cast<int*>( rep_ ));
```
```cpp
return strcmp(a.c_str(), b.c_str()) < 0; } inline bool operator != (const TiXmlString & a, const TiXmlString & b) { return !(a == b);
```
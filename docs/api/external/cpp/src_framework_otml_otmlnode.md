# src/framework/otml/otmlnode.h

```cpp
static OTMLNodePtr create(std::string tag = "", bool unique = false);
```
```cpp
static OTMLNodePtr create(std::string tag, std::string value);
```
```cpp
bool hasChildren();
```
```cpp
void setTag(const std::string& tag);
```
```cpp
OTMLNodePtr get(const std::string& childTag);
```
```cpp
OTMLNodePtr getIndex(int childIndex);
```
```cpp
OTMLNodePtr at(const std::string& childTag);
```
```cpp
void addChild(const OTMLNodePtr& newChild);
```
```cpp
bool removeChild(const OTMLNodePtr& oldChild);
```
```cpp
void copy(const OTMLNodePtr& node);
```
```cpp
void merge(const OTMLNodePtr& node);
```
```cpp
void clear();
```
```cpp
OTMLNodeList children();
```
```cpp
OTMLNodePtr clone();
```
```cpp
void write(const T& v);
```
```cpp
void writeAt(const std::string& childTag, const T& v);
```
```cpp
void writeIn(const T& v);
```
```cpp
virtual std::string emit();
```
```cpp
throw OTMLException(asOTMLNode(), stdext::format("failed to cast node value '%s' to type '%s'", m_value, stdext::demangle_type<T>()));
```
```cpp
std::string tag();
```
```cpp
int size();
```
```cpp
std::string source();
```
```cpp
std::string rawValue();
```
```cpp
bool isUnique();
```
```cpp
bool isNull();
```
```cpp
bool hasTag();
```
```cpp
bool hasValue();
```
```cpp
bool hasChildAt(const std::string& childTag);
```
```cpp
size_t getIndex();
```
```cpp
void setValue(const std::string& value);
```
```cpp
void setNull(bool null);
```
```cpp
void setUnique(bool unique);
```
```cpp
void setSource(const std::string& source);
```
```cpp
void setIndex(size_t index);
```
```cpp
void lockTag();
```
```cpp
OTMLNodePtr asOTMLNode();
```
```cpp
protected: OTMLNode() : m_unique(false), m_null(false);
```
```cpp
template<> inline std::string OTMLNode::value<std::string>();
```
```cpp
template<typename T> T OTMLNode::value();
```
```cpp
template<typename T> T OTMLNode::valueAt(const std::string& childTag);
```
```cpp
template<typename T> T OTMLNode::valueAt(const std::string& childTag, const T& def);
```
```cpp
template<typename T> T OTMLNode::valueAtIndex(int childIndex, const T& def);
```
```cpp
void OTMLNode::write(const T& v);
```
```cpp
void OTMLNode::writeAt(const std::string& childTag, const T& v);
```
```cpp
void OTMLNode::writeIn(const T& v);
```
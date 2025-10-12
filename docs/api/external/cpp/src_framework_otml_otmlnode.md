# src/framework/otml/otmlnode.h

```cpp
static OTMLNodePtr create(std::string tag = "", bool unique = false);
```
```cpp
static OTMLNodePtr create(std::string tag, std::string value);
```
```cpp
std::string tag() { return m_tag; } int size() { return m_children.size();
```
```cpp
std::string source() { return m_source; } std::string rawValue() { return m_value; } bool isUnique() { return m_unique; } bool isNull() { return m_null; } bool hasTag() { return !m_tag.empty();
```
```cpp
bool hasValue() { return !m_value.empty();
```
```cpp
bool hasChildren();
```
```cpp
bool hasChildAt(const std::string& childTag) { return !!get(childTag);
```
```cpp
size_t getIndex() { return m_index; } void setTag(const std::string& tag);
```
```cpp
void setValue(const std::string& value) { m_value = value; } void setNull(bool null) { m_null = null; } void setUnique(bool unique) { m_unique = unique; } void setSource(const std::string& source) { m_source = source; } void setIndex(size_t index) { m_index = index; } void lockTag() { m_tagLocked = true; } OTMLNodePtr get(const std::string& childTag);
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
OTMLNodePtr asOTMLNode() { return static_self_cast<OTMLNode>();
```
```cpp
protected:
    OTMLNode() : m_unique(false), m_null(false) { } std::unordered_map<std::string, std::vector<OTMLNodePtr>> m_children; std::string m_tag; std::string m_value; std::string m_source; size_t m_index = 0; bool m_unique; bool m_null; bool m_tagLocked = false; }; #include "otmlexception.h" template<> inline std::string OTMLNode::value<std::string>() { std::string value = m_value; if(stdext::starts_with(value, "\"") && stdext::ends_with(value, "\"")) { value = value.substr(1, value.length()-2);
```
```cpp
void OTMLNode::write(const T& v) { m_value = stdext::safe_cast<std::string>(v);
```
```cpp
void OTMLNode::writeAt(const std::string& childTag, const T& v) { OTMLNodePtr child = OTMLNode::create(childTag);
```
```cpp
void OTMLNode::writeIn(const T& v) { OTMLNodePtr child = OTMLNode::create();
```
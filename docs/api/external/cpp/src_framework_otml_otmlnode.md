---
title: "src/framework/otml/otmlnode.h"
source_file: "src/framework/otml/otmlnode.h"
generated_at: "2025-11-01T06:09:06.197Z"
doc_type: "cpp_api"
---

# src/framework/otml/otmlnode.h

(create)=
## `create`

**Signature:**
```cpp
static OTMLNodePtr create(std::string tag = "", bool unique = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `std::string` | `tag` | `""` | - |
| `bool` | `unique` | `false` | - |

**Returns:**
- `OTMLNodePtr`

---

(create-1)=
## `create`

**Signature:**
```cpp
static OTMLNodePtr create(std::string tag, std::string value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `tag` | - |
| `std::string` | `value` | - |

**Returns:**
- `OTMLNodePtr`

---

(haschildren)=
## `hasChildren`

**Signature:**
```cpp
bool hasChildren();
```

**Returns:**
- `bool`

---

(settag)=
## `setTag`

**Signature:**
```cpp
void setTag(const std::string& tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `tag` | - |

---

(get)=
## `get`

**Signature:**
```cpp
OTMLNodePtr get(const std::string& childTag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childTag` | - |

**Returns:**
- `OTMLNodePtr`

---

(getindex)=
## `getIndex`

**Signature:**
```cpp
OTMLNodePtr getIndex(int childIndex);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `childIndex` | - |

**Returns:**
- `OTMLNodePtr`

---

(at)=
## `at`

**Signature:**
```cpp
OTMLNodePtr at(const std::string& childTag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childTag` | - |

**Returns:**
- `OTMLNodePtr`

---

(addchild)=
## `addChild`

**Signature:**
```cpp
void addChild(const OTMLNodePtr& newChild);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `newChild` | - |

---

(removechild)=
## `removeChild`

**Signature:**
```cpp
bool removeChild(const OTMLNodePtr& oldChild);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `oldChild` | - |

**Returns:**
- `bool`

---

(copy)=
## `copy`

**Signature:**
```cpp
void copy(const OTMLNodePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `node` | - |

---

(merge)=
## `merge`

**Signature:**
```cpp
void merge(const OTMLNodePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `node` | - |

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(children)=
## `children`

**Signature:**
```cpp
OTMLNodeList children();
```

**Returns:**
- `OTMLNodeList`

---

(clone)=
## `clone`

**Signature:**
```cpp
OTMLNodePtr clone();
```

**Returns:**
- `OTMLNodePtr`

---

(write)=
## `write`

**Signature:**
```cpp
void write(const T& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `v` | - |

---

(writeat)=
## `writeAt`

**Signature:**
```cpp
void writeAt(const std::string& childTag, const T& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childTag` | - |
| `const T&` | `v` | - |

---

(writein)=
## `writeIn`

**Signature:**
```cpp
void writeIn(const T& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `v` | - |

---

(emit)=
## `emit`

**Signature:**
```cpp
virtual std::string emit();
```

**Returns:**
- `std::string`

---

(otmlexception)=
## `OTMLException`

**Signature:**
```cpp
throw OTMLException(asOTMLNode(), stdext::format("failed to cast node value '%s' to type '%s'", m_value, stdext::demangle_type<T>()));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `asOTMLNode()` | - | - |
| `stdext::format("failed to cast node value '%s' to type '%s'"` | - | - |
| `m_value` | - | - |
| `stdext::demangle_type&lt;T&gt;())` | - | - |

**Returns:**
- `throw`

---

(tag)=
## `tag`

**Signature:**
```cpp
std::string tag();
```

**Returns:**
- `std::string`

---

(size)=
## `size`

**Signature:**
```cpp
int size();
```

**Returns:**
- `int`

---

(source)=
## `source`

**Signature:**
```cpp
std::string source();
```

**Returns:**
- `std::string`

---

(rawvalue)=
## `rawValue`

**Signature:**
```cpp
std::string rawValue();
```

**Returns:**
- `std::string`

---

(isunique)=
## `isUnique`

**Signature:**
```cpp
bool isUnique();
```

**Returns:**
- `bool`

---

(isnull)=
## `isNull`

**Signature:**
```cpp
bool isNull();
```

**Returns:**
- `bool`

---

(hastag)=
## `hasTag`

**Signature:**
```cpp
bool hasTag();
```

**Returns:**
- `bool`

---

(hasvalue)=
## `hasValue`

**Signature:**
```cpp
bool hasValue();
```

**Returns:**
- `bool`

---

(haschildat)=
## `hasChildAt`

**Signature:**
```cpp
bool hasChildAt(const std::string& childTag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childTag` | - |

**Returns:**
- `bool`

---

(getindex-1)=
## `getIndex`

**Signature:**
```cpp
size_t getIndex();
```

**Returns:**
- `size_t`

---

(setvalue)=
## `setValue`

**Signature:**
```cpp
void setValue(const std::string& value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `value` | - |

---

(setnull)=
## `setNull`

**Signature:**
```cpp
void setNull(bool null);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `null` | - |

---

(setunique)=
## `setUnique`

**Signature:**
```cpp
void setUnique(bool unique);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `unique` | - |

---

(setsource)=
## `setSource`

**Signature:**
```cpp
void setSource(const std::string& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `source` | - |

---

(setindex)=
## `setIndex`

**Signature:**
```cpp
void setIndex(size_t index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `index` | - |

---

(locktag)=
## `lockTag`

**Signature:**
```cpp
void lockTag();
```

---

(asotmlnode)=
## `asOTMLNode`

**Signature:**
```cpp
OTMLNodePtr asOTMLNode();
```

**Returns:**
- `OTMLNodePtr`

---

(otmlnodevaluestdstring)=
## `OTMLNode::value<std::string>`

**Signature:**
```cpp
template<> inline std::string OTMLNode::value<std::string>();
```

**Returns:**
- `template&lt;&gt; inline std::string`

---

(otmlnodevalue)=
## `OTMLNode::value`

**Signature:**
```cpp
template<typename T> T OTMLNode::value();
```

**Returns:**
- `template&lt;typename T&gt; T`

---

(otmlnodevalueat)=
## `OTMLNode::valueAt`

**Signature:**
```cpp
template<typename T> T OTMLNode::valueAt(const std::string& childTag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childTag` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

(otmlnodevalueat-1)=
## `OTMLNode::valueAt`

**Signature:**
```cpp
template<typename T> T OTMLNode::valueAt(const std::string& childTag, const T& def);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childTag` | - |
| `const T&` | `def` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

(otmlnodevalueatindex)=
## `OTMLNode::valueAtIndex`

**Signature:**
```cpp
template<typename T> T OTMLNode::valueAtIndex(int childIndex, const T& def);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `childIndex` | - |
| `const T&` | `def` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

(otmlnodewrite)=
## `OTMLNode::write`

**Signature:**
```cpp
void OTMLNode::write(const T& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `v` | - |

---

(otmlnodewriteat)=
## `OTMLNode::writeAt`

**Signature:**
```cpp
void OTMLNode::writeAt(const std::string& childTag, const T& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childTag` | - |
| `const T&` | `v` | - |

---

(otmlnodewritein)=
## `OTMLNode::writeIn`

**Signature:**
```cpp
void OTMLNode::writeIn(const T& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `v` | - |

---

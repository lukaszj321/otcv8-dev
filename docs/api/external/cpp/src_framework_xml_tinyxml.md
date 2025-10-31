---
title: "src/framework/xml/tinyxml.h"
source_file: "src/framework/xml/tinyxml.h"
generated_at: "2025-10-31T23:33:30.371Z"
doc_type: "cpp_api"
---

# src/framework/xml/tinyxml.h

(class)=
## `class`

All TinyXml classes can print themselves to a filestream

**Signature:**
```cpp
or the string class(TiXmlString in non-STL mode, std::string in STL mode.) Either or both cfile and str can be null. This is a formatted print, and will insert tabs and newlines. (For an unformatted stream, use the << operator.) */ virtual void Print( FILE* cfile, int depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlString in non-STL` | `mode` | - |
| `std::string in STL mode.) Either or both cfile and str can be null. This is a formatted` | `print` | - |
| `and will insert tabs and newlines. (For an unformatted` | `stream` | - |
| `use the &lt;&lt; operator.) */ virtual void Print( FILE*` | `cfile` | - |
| `int` | `depth` | - |

**Returns:**
- `or the string`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding /*= TIXML_ENCODING_UNKNOWN */);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData*` | `data` | - |
| `TiXmlEncoding encoding /*= TIXML_ENCODING_UNKNOWN */` | - | - |

**Returns:**
- `virtual const char*`

---

(encodestring)=
## `EncodeString`

**Signature:**
```cpp
static void EncodeString(const TIXML_STRING& str, TIXML_STRING* out);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TIXML_STRING&` | `str` | - |
| `TIXML_STRING*` | `out` | - |

**Returns:**
- `static void`

---

(skipwhitespace)=
## `SkipWhiteSpace`

**Signature:**
```cpp
protected: static const char* SkipWhiteSpace(const char*, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | - | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `protected: static const char*`

---

(iswhitespace)=
## `IsWhiteSpace`

**Signature:**
```cpp
return IsWhiteSpace((char) c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `(char)` | `c` | - |

**Returns:**
- `return`

---

(streamwhitespace)=
## `StreamWhiteSpace`

**Signature:**
```cpp
static bool StreamWhiteSpace(std::istream * in, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `static bool`

---

(streamto)=
## `StreamTo`

**Signature:**
```cpp
static bool StreamTo(std::istream * in, int character, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `int` | `character` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `static bool`

---

(readname)=
## `ReadName`

**Signature:**
```cpp
static const char* ReadName(const char* p, TIXML_STRING* name, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TIXML_STRING*` | `name` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `static const char*`

---

(getentity)=
## `GetEntity`

**Signature:**
```cpp
static const char* GetEntity(const char* in, char* value, int* length, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `in` | - |
| `char*` | `value` | - |
| `int*` | `length` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `static const char*`

---

(getentity)=
## `GetEntity`

**Signature:**
```cpp
return GetEntity(p, _value, length, encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `p` | - |
| `` | `_value` | - |
| `` | `length` | - |
| `` | `encoding` | - |

**Returns:**
- `return`

---

(stringequal)=
## `StringEqual`

**Signature:**
```cpp
static bool StringEqual(const char* p, const char* endTag, bool ignoreCase, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `const char*` | `endTag` | - |
| `bool` | `ignoreCase` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `static bool`

---

(isalpha)=
## `IsAlpha`

**Signature:**
```cpp
static int IsAlpha(unsigned char anyByte, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `unsigned char` | `anyByte` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `static int`

---

(isalphanum)=
## `IsAlphaNum`

**Signature:**
```cpp
static int IsAlphaNum(unsigned char anyByte, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `unsigned char` | `anyByte` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `static int`

---

(tolower)=
## `tolower`

**Signature:**
```cpp
return tolower(v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `v` | - |

**Returns:**
- `return`

---

(convertutf32toutf8)=
## `ConvertUTF32ToUTF8`

**Signature:**
```cpp
static void ConvertUTF32ToUTF8(unsigned long input, char* output, int* length);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `unsigned long` | `input` | - |
| `char*` | `output` | - |
| `int*` | `length` | - |

**Returns:**
- `static void`

---

(operator)=
## `operator<<`

**Signature:**
```cpp
friend std::ostream& operator<<(std::ostream& out, const TiXmlNode& base);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostream&` | `out` | - |
| `const TiXmlNode&` | `base` | - |

**Returns:**
- `friend std::ostream&`

---

(operator)=
## `operator<<`

Appends the XML node or attribute to a std::string.

**Signature:**
```cpp
friend std::string& operator<<(std::string& out, const TiXmlNode& base);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string&` | `out` | - |
| `const TiXmlNode&` | `base` | - |

**Returns:**
- `friend std::string&`

---

(clear)=
## `Clear`

Delete all the children of this node. Does not affect 'this'.

**Signature:**
```cpp
void Clear();
```

---

(iteratechildren)=
## `IterateChildren`

**Signature:**
```cpp
const TiXmlNode* IterateChildren(const TiXmlNode* previous);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlNode*` | `previous` | - |

**Returns:**
- `const TiXmlNode*`

---

(iteratechildren)=
## `IterateChildren`

This flavor of IterateChildren searches for children with a particular 'value'

**Signature:**
```cpp
const TiXmlNode* IterateChildren(const char * value, const TiXmlNode* previous);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `value` | - |
| `const TiXmlNode*` | `previous` | - |

**Returns:**
- `const TiXmlNode*`

---

(insertendchild)=
## `InsertEndChild`

**Signature:**
```cpp
TiXmlNode* InsertEndChild(const TiXmlNode& addThis);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlNode&` | `addThis` | - |

**Returns:**
- `TiXmlNode*`

---

(owned)=
## `owned`

**Signature:**
```cpp
henceforth owned(and deleted) by tinyXml. This method is efficient and avoids an extra copy, but should be used with care as it uses a different memory model than the other insert functions. @sa InsertEndChild */ TiXmlNode* LinkEndChild( TiXmlNode* addThis);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `and deleted) by tinyXml. This method is efficient and avoids an extra` | `copy` | - |
| `but should be used with care as it uses a different memory model than the other insert functions. @sa InsertEndChild */ TiXmlNode* LinkEndChild( TiXmlNode*` | `addThis` | - |

**Returns:**
- `henceforth`

---

(insertbeforechild)=
## `InsertBeforeChild`

**Signature:**
```cpp
TiXmlNode* InsertBeforeChild(TiXmlNode* beforeThis, const TiXmlNode& addThis);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlNode*` | `beforeThis` | - |
| `const TiXmlNode&` | `addThis` | - |

**Returns:**
- `TiXmlNode*`

---

(insertafterchild)=
## `InsertAfterChild`

**Signature:**
```cpp
TiXmlNode* InsertAfterChild(TiXmlNode* afterThis, const TiXmlNode& addThis);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlNode*` | `afterThis` | - |
| `const TiXmlNode&` | `addThis` | - |

**Returns:**
- `TiXmlNode*`

---

(replacechild)=
## `ReplaceChild`

**Signature:**
```cpp
TiXmlNode* ReplaceChild(TiXmlNode* replaceThis, const TiXmlNode& withThis);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlNode*` | `replaceThis` | - |
| `const TiXmlNode&` | `withThis` | - |

**Returns:**
- `TiXmlNode*`

---

(removechild)=
## `RemoveChild`

Delete a child of this node.

**Signature:**
```cpp
bool RemoveChild(TiXmlNode* removeThis);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlNode*` | `removeThis` | - |

**Returns:**
- `bool`

---

(previoussibling)=
## `PreviousSibling`

Navigate to a sibling node.

**Signature:**
```cpp
const TiXmlNode* PreviousSibling(const char *);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | - | - |

**Returns:**
- `const TiXmlNode*`

---

(nextsibling)=
## `NextSibling`

Navigate to a sibling node with the given 'value'.

**Signature:**
```cpp
const TiXmlNode* NextSibling(const char *);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | - | - |

**Returns:**
- `const TiXmlNode*`

---

(nextsiblingelement)=
## `NextSiblingElement`

**Signature:**
```cpp
const TiXmlElement* NextSiblingElement();
```

**Returns:**
- `const TiXmlElement*`

---

(nextsiblingelement)=
## `NextSiblingElement`

**Signature:**
```cpp
const TiXmlElement* NextSiblingElement(const char *);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | - | - |

**Returns:**
- `const TiXmlElement*`

---

(firstchildelement)=
## `FirstChildElement`

Convenience function to get through elements.

**Signature:**
```cpp
const TiXmlElement* FirstChildElement();
```

**Returns:**
- `const TiXmlElement*`

---

(firstchildelement)=
## `FirstChildElement`

Convenience function to get through elements.

**Signature:**
```cpp
const TiXmlElement* FirstChildElement(const char * _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_value` | - |

**Returns:**
- `const TiXmlElement*`

---

(getdocument)=
## `GetDocument`

**Signature:**
```cpp
const TiXmlDocument* GetDocument();
```

**Returns:**
- `const TiXmlDocument*`

---

(clone)=
## `Clone`

**Signature:**
```cpp
virtual TiXmlNode* Clone();
```

**Returns:**
- `virtual TiXmlNode*`

---

(accept)=
## `Accept`

**Signature:**
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlVisitor*` | `visitor` | - |

**Returns:**
- `virtual bool`

---

(tixmlnode)=
## `TiXmlNode`

**Signature:**
```cpp
protected: TiXmlNode(NodeType _type);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `NodeType` | `_type` | - |

**Returns:**
- `protected:`

---

(copyto)=
## `CopyTo`

**Signature:**
```cpp
void CopyTo(TiXmlNode* target);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlNode*` | `target` | - |

---

(streamin)=
## `StreamIn`

**Signature:**
```cpp
virtual void StreamIn(std::istream* in, TIXML_STRING* tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream*` | `in` | - |
| `TIXML_STRING*` | `tag` | - |

**Returns:**
- `virtual void`

---

(identify)=
## `Identify`

**Signature:**
```cpp
TiXmlNode* Identify(const char* start, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `start` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `TiXmlNode*`

---

(queryintvalue)=
## `QueryIntValue`

**Signature:**
```cpp
int QueryIntValue(int* _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int*` | `_value` | - |

**Returns:**
- `int`

---

(querydoublevalue)=
## `QueryDoubleValue`

QueryDoubleValue examines the value string. See QueryIntValue().

**Signature:**
```cpp
int QueryDoubleValue(double* _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double*` | `_value` | - |

**Returns:**
- `int`

---

(next)=
## `Next`

Get the next sibling attribute in the DOM. Returns null at end.

**Signature:**
```cpp
const TiXmlAttribute* Next();
```

**Returns:**
- `const TiXmlAttribute*`

---

(previous)=
## `Previous`

Get the previous sibling attribute in the DOM. Returns null at beginning.

**Signature:**
```cpp
const TiXmlAttribute* Previous();
```

**Returns:**
- `const TiXmlAttribute*`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData*` | `data` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `virtual const char*`

---

(print)=
## `Print`

**Signature:**
```cpp
void Print(FILE* cfile, int depth, TIXML_STRING* str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |
| `TIXML_STRING*` | `str` | - |

---

(tixmlattributeset)=
## `TiXmlAttributeSet`

**Signature:**
```cpp
public: TiXmlAttributeSet();
```

**Returns:**
- `public:`

---

(add)=
## `Add`

**Signature:**
```cpp
void Add(TiXmlAttribute* attribute);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlAttribute*` | `attribute` | - |

---

(remove)=
## `Remove`

**Signature:**
```cpp
void Remove(TiXmlAttribute* attribute);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlAttribute*` | `attribute` | - |

---

(find)=
## `Find`

**Signature:**
```cpp
TiXmlAttribute* Find(const char* _name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `_name` | - |

**Returns:**
- `TiXmlAttribute*`

---

(findorcreate)=
## `FindOrCreate`

**Signature:**
```cpp
TiXmlAttribute* FindOrCreate(const char* _name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `_name` | - |

**Returns:**
- `TiXmlAttribute*`

---

(find)=
## `Find`

**Signature:**
```cpp
TiXmlAttribute* Find(const std::string& _name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_name` | - |

**Returns:**
- `TiXmlAttribute*`

---

(findorcreate)=
## `FindOrCreate`

**Signature:**
```cpp
TiXmlAttribute* FindOrCreate(const std::string& _name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_name` | - |

**Returns:**
- `TiXmlAttribute*`

---

(tixmlelement)=
## `TiXmlElement`

**Signature:**
```cpp
public: TiXmlElement(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `public:`

---

(t)=
## `T`

**Signature:**
```cpp
return T();
```

**Returns:**
- `return`

---

(sstream)=
## `sstream`

**Signature:**
```cpp
std::stringstream sstream(node->ValueStr());
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `node-&gt;ValueStr()` | - | - |

**Returns:**
- `std::stringstream`

---

(attribute)=
## `Attribute`

**Signature:**
```cpp
std::string Attribute(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

**Returns:**
- `std::string`

---

(attribute)=
## `Attribute`

**Signature:**
```cpp
std::string Attribute(const std::string& name, int* i);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `int*` | `i` | - |

**Returns:**
- `std::string`

---

(attribute)=
## `Attribute`

**Signature:**
```cpp
std::string Attribute(const std::string& name, double* d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `double*` | `d` | - |

**Returns:**
- `std::string`

---

(setattribute)=
## `SetAttribute`

**Signature:**
```cpp
void SetAttribute(const std::string& name, const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `const std::string&` | `_value` | - |

---

(removeattribute)=
## `RemoveAttribute`

**Signature:**
```cpp
void RemoveAttribute(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(gettext)=
## `GetText`

**Signature:**
```cpp
WARNING: GetText() accesses a child node - don't become confused with the similarly named TiXmlHandle::Text() and TiXmlNode::ToText() which are safe type casts on the referenced node. */ const char* GetText();
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) accesses a child node - don't become confused with the similarly named TiXmlHandle::Text() and TiXmlNode::ToText() which are safe type casts on the referenced node. */ const char* GetText(` | - | - |

**Returns:**
- `WARNING:`

---

(clone)=
## `Clone`

Creates a new Element and returns it - the returned element is a copy.

**Signature:**
```cpp
virtual TiXmlNode* Clone();
```

**Returns:**
- `virtual TiXmlNode*`

---

(print)=
## `Print`

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |

**Returns:**
- `virtual void`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData*` | `data` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `virtual const char*`

---

(accept)=
## `Accept`

Walk the XML tree visiting this node and all of its children.

**Signature:**
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlVisitor*` | `visitor` | - |

**Returns:**
- `virtual bool`

---

(copyto)=
## `CopyTo`

**Signature:**
```cpp
protected: void CopyTo(TiXmlElement* target);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlElement*` | `target` | - |

**Returns:**
- `protected: void`

---

(streamin)=
## `StreamIn`

**Signature:**
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `virtual void`

---

(readvalue)=
## `ReadValue`

**Signature:**
```cpp
const char* ReadValue(const char* in, TiXmlParsingData* prevData, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `in` | - |
| `TiXmlParsingData*` | `prevData` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `const char*`

---

(clone)=
## `Clone`

Returns a copy of this Comment.

**Signature:**
```cpp
virtual TiXmlNode* Clone();
```

**Returns:**
- `virtual TiXmlNode*`

---

(print)=
## `Print`

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |

**Returns:**
- `virtual void`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData*` | `data` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `virtual const char*`

---

(accept)=
## `Accept`

Walk the XML tree visiting this node and all of its children.

**Signature:**
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlVisitor*` | `visitor` | - |

**Returns:**
- `virtual bool`

---

(copyto)=
## `CopyTo`

**Signature:**
```cpp
protected: void CopyTo(TiXmlComment* target);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlComment*` | `target` | - |

**Returns:**
- `protected: void`

---

(streamin)=
## `StreamIn`

**Signature:**
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `virtual void`

---

(print)=
## `Print`

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |

**Returns:**
- `virtual void`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData*` | `data` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `virtual const char*`

---

(accept)=
## `Accept`

Walk the XML tree visiting this node and all of its children.

**Signature:**
```cpp
virtual bool Accept(TiXmlVisitor* content);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlVisitor*` | `content` | - |

**Returns:**
- `virtual bool`

---

(clone)=
## `Clone`

[internal use] Creates a new Element and returns it.

**Signature:**
```cpp
virtual TiXmlNode* Clone();
```

**Returns:**
- `virtual TiXmlNode*`

---

(copyto)=
## `CopyTo`

**Signature:**
```cpp
void CopyTo(TiXmlText* target);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlText*` | `target` | - |

---

(streamin)=
## `StreamIn`

**Signature:**
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `virtual void`

---

(clone)=
## `Clone`

Creates a copy of this Declaration and returns it.

**Signature:**
```cpp
virtual TiXmlNode* Clone();
```

**Returns:**
- `virtual TiXmlNode*`

---

(print)=
## `Print`

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth, TIXML_STRING* str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |
| `TIXML_STRING*` | `str` | - |

**Returns:**
- `virtual void`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData*` | `data` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `virtual const char*`

---

(accept)=
## `Accept`

Walk the XML tree visiting this node and all of its children.

**Signature:**
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlVisitor*` | `visitor` | - |

**Returns:**
- `virtual bool`

---

(copyto)=
## `CopyTo`

**Signature:**
```cpp
protected: void CopyTo(TiXmlDeclaration* target);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlDeclaration*` | `target` | - |

**Returns:**
- `protected: void`

---

(streamin)=
## `StreamIn`

**Signature:**
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `virtual void`

---

(clone)=
## `Clone`

Creates a copy of this Unknown and returns it.

**Signature:**
```cpp
virtual TiXmlNode* Clone();
```

**Returns:**
- `virtual TiXmlNode*`

---

(print)=
## `Print`

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |

**Returns:**
- `virtual void`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData*` | `data` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `virtual const char*`

---

(accept)=
## `Accept`

Walk the XML tree visiting this node and all of its children.

**Signature:**
```cpp
virtual bool Accept(TiXmlVisitor* content);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlVisitor*` | `content` | - |

**Returns:**
- `virtual bool`

---

(copyto)=
## `CopyTo`

**Signature:**
```cpp
protected: void CopyTo(TiXmlUnknown* target);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlUnknown*` | `target` | - |

**Returns:**
- `protected: void`

---

(streamin)=
## `StreamIn`

**Signature:**
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `virtual void`

---

(loadfile)=
## `LoadFile`

**Signature:**
```cpp
bool LoadFile(TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlEncoding encoding =` | `TIXML_DEFAULT_ENCODING` | - |

**Returns:**
- `bool`

---

(savefile)=
## `SaveFile`

Save a file using the current document value. Returns true if successful.

**Signature:**
```cpp
bool SaveFile();
```

**Returns:**
- `bool`

---

(loadfile)=
## `LoadFile`

Load a file using the given filename. Returns true if successful.

**Signature:**
```cpp
bool LoadFile(const char * filename, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `filename` | - |
| `TiXmlEncoding encoding =` | `TIXML_DEFAULT_ENCODING` | - |

**Returns:**
- `bool`

---

(savefile)=
## `SaveFile`

Save a file using the given filename. Returns true if successful.

**Signature:**
```cpp
bool SaveFile(const char * filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `filename` | - |

**Returns:**
- `bool`

---

(loadfile)=
## `LoadFile`

**Signature:**
```cpp
bool LoadFile(FILE*, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | - | - |
| `TiXmlEncoding encoding =` | `TIXML_DEFAULT_ENCODING` | - |

**Returns:**
- `bool`

---

(savefile)=
## `SaveFile`

Save a file using the given FILE*. Returns true if successful.

**Signature:**
```cpp
bool SaveFile(FILE*);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | - | - |

**Returns:**
- `bool`

---

(loadfile)=
## `LoadFile`

**Signature:**
```cpp
return LoadFile(filename.c_str(), encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `filename.c_str()` | - | - |
| `` | `encoding` | - |

**Returns:**
- `return`

---

(savefile)=
## `SaveFile`

**Signature:**
```cpp
return SaveFile(filename.c_str());
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `filename.c_str()` | - | - |

**Returns:**
- `return`

---

(parse)=
## `Parse`

**Signature:**
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data = 0, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `TiXmlParsingData* data = 0` | - | - |
| `TiXmlEncoding encoding =` | `TIXML_DEFAULT_ENCODING` | - |

**Returns:**
- `virtual const char*`

---

(array)=
## `array`

**Signature:**
```cpp
will allocate a character array(new char[]) and return it as a pointer. The calling code pust call delete[] on the return char* to avoid a memory leak. */ //char* PrintToMemory();
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `new char[]) and return it as a pointer. The calling code pust call delete[] on the return char* to avoid a memory leak. */ //char* PrintToMemory(` | - | - |

**Returns:**
- `will allocate a character`

---

(print)=
## `Print`

Print this Document to a FILE stream.

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth = 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int depth = 0` | - | - |

**Returns:**
- `virtual void`

---

(seterror)=
## `SetError`

**Signature:**
```cpp
void SetError(int err, const char* errorLocation, TiXmlParsingData* prevData, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `err` | - |
| `const char*` | `errorLocation` | - |
| `TiXmlParsingData*` | `prevData` | - |
| `TiXmlEncoding` | `encoding` | - |

---

(accept)=
## `Accept`

Walk the XML tree visiting this node and all of its children.

**Signature:**
```cpp
virtual bool Accept(TiXmlVisitor* content);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlVisitor*` | `content` | - |

**Returns:**
- `virtual bool`

---

(clone)=
## `Clone`

**Signature:**
```cpp
virtual TiXmlNode* Clone();
```

**Returns:**
- `virtual TiXmlNode*`

---

(streamin)=
## `StreamIn`

**Signature:**
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream *` | `in` | - |
| `TIXML_STRING *` | `tag` | - |

**Returns:**
- `virtual void`

---

(copyto)=
## `CopyTo`

**Signature:**
```cpp
private: void CopyTo(TiXmlDocument* target);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlDocument*` | `target` | - |

**Returns:**
- `private: void`

---

(dochandle)=
## `docHandle`

**Signature:**
```cpp
TiXmlHandle docHandle(&document);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `&` | `document` | - |

**Returns:**
- `TiXmlHandle`

---

(firstchild)=
## `FirstChild`

Return a handle to the first child node.

**Signature:**
```cpp
TiXmlHandle FirstChild();
```

**Returns:**
- `TiXmlHandle`

---

(firstchild)=
## `FirstChild`

Return a handle to the first child node with the given name.

**Signature:**
```cpp
TiXmlHandle FirstChild(const char * value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `value` | - |

**Returns:**
- `TiXmlHandle`

---

(firstchildelement)=
## `FirstChildElement`

Return a handle to the first child element.

**Signature:**
```cpp
TiXmlHandle FirstChildElement();
```

**Returns:**
- `TiXmlHandle`

---

(firstchildelement)=
## `FirstChildElement`

Return a handle to the first child element with the given name.

**Signature:**
```cpp
TiXmlHandle FirstChildElement(const char * value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `value` | - |

**Returns:**
- `TiXmlHandle`

---

(child)=
## `Child`

**Signature:**
```cpp
TiXmlHandle Child(const char* value, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `value` | - |
| `int` | `index` | - |

**Returns:**
- `TiXmlHandle`

---

(child)=
## `Child`

**Signature:**
```cpp
TiXmlHandle Child(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

**Returns:**
- `TiXmlHandle`

---

(childelement)=
## `ChildElement`

**Signature:**
```cpp
TiXmlHandle ChildElement(const char* value, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `value` | - |
| `int` | `index` | - |

**Returns:**
- `TiXmlHandle`

---

(childelement)=
## `ChildElement`

**Signature:**
```cpp
TiXmlHandle ChildElement(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

**Returns:**
- `TiXmlHandle`

---

(visitenter)=
## `VisitEnter`

**Signature:**
```cpp
virtual bool VisitEnter(const TiXmlDocument& doc);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlDocument&` | `doc` | - |

**Returns:**
- `virtual bool`

---

(visitexit)=
## `VisitExit`

**Signature:**
```cpp
virtual bool VisitExit(const TiXmlDocument& doc);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlDocument&` | `doc` | - |

**Returns:**
- `virtual bool`

---

(visitenter)=
## `VisitEnter`

**Signature:**
```cpp
virtual bool VisitEnter(const TiXmlElement& element, const TiXmlAttribute* firstAttribute);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlElement&` | `element` | - |
| `const TiXmlAttribute*` | `firstAttribute` | - |

**Returns:**
- `virtual bool`

---

(visitexit)=
## `VisitExit`

**Signature:**
```cpp
virtual bool VisitExit(const TiXmlElement& element);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlElement&` | `element` | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

**Signature:**
```cpp
virtual bool Visit(const TiXmlDeclaration& declaration);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlDeclaration&` | `declaration` | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

**Signature:**
```cpp
virtual bool Visit(const TiXmlText& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlText&` | `text` | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

**Signature:**
```cpp
virtual bool Visit(const TiXmlComment& comment);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlComment&` | `comment` | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

**Signature:**
```cpp
virtual bool Visit(const TiXmlUnknown& unknown);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlUnknown&` | `unknown` | - |

**Returns:**
- `virtual bool`

---

(clear)=
## `Clear`

**Signature:**
```cpp
void Clear();
```

---

(visitenter)=
## `VisitEnter`

Visit a document.

**Signature:**
```cpp
virtual bool VisitEnter(const TiXmlDocument& /*doc*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlDocument& /*doc*/` | - | - |

**Returns:**
- `virtual bool`

---

(visitexit)=
## `VisitExit`

Visit a document.

**Signature:**
```cpp
virtual bool VisitExit(const TiXmlDocument& /*doc*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlDocument& /*doc*/` | - | - |

**Returns:**
- `virtual bool`

---

(visitenter)=
## `VisitEnter`

Visit an element.

**Signature:**
```cpp
virtual bool VisitEnter(const TiXmlElement& /*element*/, const TiXmlAttribute* /*firstAttribute*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlElement& /*element*/` | - | - |
| `const TiXmlAttribute* /*firstAttribute*/` | - | - |

**Returns:**
- `virtual bool`

---

(visitexit)=
## `VisitExit`

Visit an element.

**Signature:**
```cpp
virtual bool VisitExit(const TiXmlElement& /*element*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlElement& /*element*/` | - | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

Visit a declaration

**Signature:**
```cpp
virtual bool Visit(const TiXmlDeclaration& /*declaration*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlDeclaration& /*declaration*/` | - | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

Visit a text node

**Signature:**
```cpp
virtual bool Visit(const TiXmlText& /*text*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlText& /*text*/` | - | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

Visit a comment node

**Signature:**
```cpp
virtual bool Visit(const TiXmlComment& /*comment*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlComment& /*comment*/` | - | - |

**Returns:**
- `virtual bool`

---

(visit)=
## `Visit`

Visit an unknown node

**Signature:**
```cpp
virtual bool Visit(const TiXmlUnknown& /*unknown*/);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlUnknown& /*unknown*/` | - | - |

**Returns:**
- `virtual bool`

---

(setcondensewhitespace)=
## `SetCondenseWhiteSpace`

**Signature:**
```cpp
static void SetCondenseWhiteSpace(bool condense);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `condense` | - |

**Returns:**
- `static void`

---

(iswhitespacecondensed)=
## `IsWhiteSpaceCondensed`

Return the current white space setting.

**Signature:**
```cpp
static bool IsWhiteSpaceCondensed();
```

**Returns:**
- `static bool`

---

(tixmldocumentsettabsize)=
## `TiXmlDocument::SetTabSize`

**Signature:**
```cpp
can be disabled if TiXmlDocument::SetTabSize() is called with 0 as the value. @sa TiXmlDocument::SetTabSize() */ int Row();
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) is called with 0 as the value. @sa TiXmlDocument::SetTabSize() */ int Row(` | - | - |

**Returns:**
- `can be disabled if`

---

(column)=
## `Column`

**Signature:**
```cpp
int Column();
```

**Returns:**
- `int`

---

(setuserdata)=
## `SetUserData`

**Signature:**
```cpp
void SetUserData(void* user);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void*` | `user` | - |

---

(getuserdata)=
## `GetUserData`

**Signature:**
```cpp
void* GetUserData();
```

**Returns:**
- `void*`

---

(getuserdata)=
## `GetUserData`

**Signature:**
```cpp
const void* GetUserData();
```

**Returns:**
- `const void*`

---

(iswhitespace)=
## `IsWhiteSpace`

**Signature:**
```cpp
inline static bool IsWhiteSpace(char c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char` | `c` | - |

**Returns:**
- `inline static bool`

---

(iswhitespace)=
## `IsWhiteSpace`

**Signature:**
```cpp
inline static bool IsWhiteSpace(int c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `c` | - |

**Returns:**
- `inline static bool`

---

(getchar)=
## `GetChar`

**Signature:**
```cpp
inline static const char* GetChar(const char* p, char* _value, int* length, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `p` | - |
| `char*` | `_value` | - |
| `int*` | `length` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `inline static const char*`

---

(if)=
## `if`

**Signature:**
```cpp
else if(*length);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `*` | `length` | - |

**Returns:**
- `else`

---

(tolower)=
## `ToLower`

**Signature:**
```cpp
inline static int ToLower(int v, TiXmlEncoding encoding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `v` | - |
| `TiXmlEncoding` | `encoding` | - |

**Returns:**
- `inline static int`

---

(value)=
## `Value`

Return Value() as a std::string. If you only use STL,

**Signature:**
```cpp
this is more efficient than calling Value(). Only available in STL mode. */ const std::string& ValueStr();
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `). Only available in STL mode. */ const std::string& ValueStr(` | - | - |

**Returns:**
- `this is more efficient than calling`

---

(valuetstr)=
## `ValueTStr`

**Signature:**
```cpp
const TIXML_STRING& ValueTStr();
```

**Returns:**
- `const TIXML_STRING&`

---

(setvalue)=
## `SetValue`

**Signature:**
```cpp
void SetValue(const char * _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_value` | - |

---

(setvalue)=
## `SetValue`

STL std::string form.

**Signature:**
```cpp
void SetValue(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

---

(parent)=
## `Parent`

One step up the DOM.

**Signature:**
```cpp
TiXmlNode* Parent();
```

**Returns:**
- `TiXmlNode*`

---

(parent)=
## `Parent`

**Signature:**
```cpp
const TiXmlNode* Parent();
```

**Returns:**
- `const TiXmlNode*`

---

(firstchild)=
## `FirstChild`

**Signature:**
```cpp
const TiXmlNode* FirstChild();
```

**Returns:**
- `const TiXmlNode*`

---

(firstchild)=
## `FirstChild`

**Signature:**
```cpp
TiXmlNode* FirstChild();
```

**Returns:**
- `TiXmlNode*`

---

(firstchild)=
## `FirstChild`

The first child of this node with the matching 'value'. Will be null if none found.

**Signature:**
```cpp
TiXmlNode* FirstChild(const char * _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_value` | - |

**Returns:**
- `TiXmlNode*`

---

(lastchild)=
## `LastChild`

**Signature:**
```cpp
const TiXmlNode* LastChild();
```

**Returns:**
- `const TiXmlNode*`

---

(lastchild)=
## `LastChild`

**Signature:**
```cpp
TiXmlNode* LastChild();
```

**Returns:**
- `TiXmlNode*`

---

(lastchild)=
## `LastChild`

**Signature:**
```cpp
TiXmlNode* LastChild(const char * _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_value` | - |

**Returns:**
- `TiXmlNode*`

---

(firstchild)=
## `FirstChild`

**Signature:**
```cpp
const TiXmlNode* FirstChild(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `const TiXmlNode*`

---

(firstchild)=
## `FirstChild`

**Signature:**
```cpp
TiXmlNode* FirstChild(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlNode*`

---

(lastchild)=
## `LastChild`

**Signature:**
```cpp
const TiXmlNode* LastChild(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `const TiXmlNode*`

---

(lastchild)=
## `LastChild`

**Signature:**
```cpp
TiXmlNode* LastChild(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlNode*`

---

(iteratechildren)=
## `IterateChildren`

**Signature:**
```cpp
TiXmlNode* IterateChildren(const TiXmlNode* previous);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlNode*` | `previous` | - |

**Returns:**
- `TiXmlNode*`

---

(iteratechildren)=
## `IterateChildren`

**Signature:**
```cpp
TiXmlNode* IterateChildren(const char * _value, const TiXmlNode* previous);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_value` | - |
| `const TiXmlNode*` | `previous` | - |

**Returns:**
- `TiXmlNode*`

---

(iteratechildren)=
## `IterateChildren`

**Signature:**
```cpp
const TiXmlNode* IterateChildren(const std::string& _value, const TiXmlNode* previous);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |
| `const TiXmlNode*` | `previous` | - |

**Returns:**
- `const TiXmlNode*`

---

(iteratechildren)=
## `IterateChildren`

**Signature:**
```cpp
TiXmlNode* IterateChildren(const std::string& _value, const TiXmlNode* previous);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |
| `const TiXmlNode*` | `previous` | - |

**Returns:**
- `TiXmlNode*`

---

(previoussibling)=
## `PreviousSibling`

Navigate to a sibling node.

**Signature:**
```cpp
const TiXmlNode* PreviousSibling();
```

**Returns:**
- `const TiXmlNode*`

---

(previoussibling)=
## `PreviousSibling`

**Signature:**
```cpp
TiXmlNode* PreviousSibling();
```

**Returns:**
- `TiXmlNode*`

---

(previoussibling)=
## `PreviousSibling`

**Signature:**
```cpp
TiXmlNode* PreviousSibling(const char *_prev);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_prev` | - |

**Returns:**
- `TiXmlNode*`

---

(previoussibling)=
## `PreviousSibling`

**Signature:**
```cpp
const TiXmlNode* PreviousSibling(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `const TiXmlNode*`

---

(previoussibling)=
## `PreviousSibling`

**Signature:**
```cpp
TiXmlNode* PreviousSibling(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlNode*`

---

(nextsibling)=
## `NextSibling`

**Signature:**
```cpp
const TiXmlNode* NextSibling(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `const TiXmlNode*`

---

(nextsibling)=
## `NextSibling`

**Signature:**
```cpp
TiXmlNode* NextSibling(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlNode*`

---

(nextsibling)=
## `NextSibling`

Navigate to a sibling node.

**Signature:**
```cpp
const TiXmlNode* NextSibling();
```

**Returns:**
- `const TiXmlNode*`

---

(nextsibling)=
## `NextSibling`

**Signature:**
```cpp
TiXmlNode* NextSibling();
```

**Returns:**
- `TiXmlNode*`

---

(nextsibling)=
## `NextSibling`

**Signature:**
```cpp
TiXmlNode* NextSibling(const char* _next);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `_next` | - |

**Returns:**
- `TiXmlNode*`

---

(nextsiblingelement)=
## `NextSiblingElement`

**Signature:**
```cpp
TiXmlElement* NextSiblingElement();
```

**Returns:**
- `TiXmlElement*`

---

(nextsiblingelement)=
## `NextSiblingElement`

**Signature:**
```cpp
TiXmlElement* NextSiblingElement(const char *_next);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_next` | - |

**Returns:**
- `TiXmlElement*`

---

(nextsiblingelement)=
## `NextSiblingElement`

**Signature:**
```cpp
const TiXmlElement* NextSiblingElement(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `const TiXmlElement*`

---

(nextsiblingelement)=
## `NextSiblingElement`

**Signature:**
```cpp
TiXmlElement* NextSiblingElement(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlElement*`

---

(firstchildelement)=
## `FirstChildElement`

**Signature:**
```cpp
TiXmlElement* FirstChildElement();
```

**Returns:**
- `TiXmlElement*`

---

(firstchildelement)=
## `FirstChildElement`

**Signature:**
```cpp
TiXmlElement* FirstChildElement(const char * _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *` | `_value` | - |

**Returns:**
- `TiXmlElement*`

---

(firstchildelement)=
## `FirstChildElement`

**Signature:**
```cpp
const TiXmlElement* FirstChildElement(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `const TiXmlElement*`

---

(firstchildelement)=
## `FirstChildElement`

**Signature:**
```cpp
TiXmlElement* FirstChildElement(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlElement*`

---

(type)=
## `Type`

**Signature:**
```cpp
int Type();
```

**Returns:**
- `int`

---

(getdocument)=
## `GetDocument`

**Signature:**
```cpp
TiXmlDocument* GetDocument();
```

**Returns:**
- `TiXmlDocument*`

---

(nochildren)=
## `NoChildren`

Returns true if this node has no children.

**Signature:**
```cpp
bool NoChildren();
```

**Returns:**
- `bool`

---

(todocument)=
## `ToDocument`

**Signature:**
```cpp
virtual const TiXmlDocument* ToDocument();
```

**Returns:**
- `virtual const TiXmlDocument*`

---

(toelement)=
## `ToElement`

**Signature:**
```cpp
virtual const TiXmlElement* ToElement();
```

**Returns:**
- `virtual const TiXmlElement*`

---

(tocomment)=
## `ToComment`

**Signature:**
```cpp
virtual const TiXmlComment* ToComment();
```

**Returns:**
- `virtual const TiXmlComment*`

---

(tounknown)=
## `ToUnknown`

**Signature:**
```cpp
virtual const TiXmlUnknown* ToUnknown();
```

**Returns:**
- `virtual const TiXmlUnknown*`

---

(totext)=
## `ToText`

**Signature:**
```cpp
virtual const TiXmlText* ToText();
```

**Returns:**
- `virtual const TiXmlText*`

---

(todeclaration)=
## `ToDeclaration`

**Signature:**
```cpp
virtual const TiXmlDeclaration* ToDeclaration();
```

**Returns:**
- `virtual const TiXmlDeclaration*`

---

(todocument)=
## `ToDocument`

**Signature:**
```cpp
virtual TiXmlDocument* ToDocument();
```

**Returns:**
- `virtual TiXmlDocument*`

---

(toelement)=
## `ToElement`

**Signature:**
```cpp
virtual TiXmlElement* ToElement();
```

**Returns:**
- `virtual TiXmlElement*`

---

(tocomment)=
## `ToComment`

**Signature:**
```cpp
virtual TiXmlComment* ToComment();
```

**Returns:**
- `virtual TiXmlComment*`

---

(tounknown)=
## `ToUnknown`

**Signature:**
```cpp
virtual TiXmlUnknown* ToUnknown();
```

**Returns:**
- `virtual TiXmlUnknown*`

---

(totext)=
## `ToText`

**Signature:**
```cpp
virtual TiXmlText* ToText();
```

**Returns:**
- `virtual TiXmlText*`

---

(todeclaration)=
## `ToDeclaration`

**Signature:**
```cpp
virtual TiXmlDeclaration* ToDeclaration();
```

**Returns:**
- `virtual TiXmlDeclaration*`

---

(name)=
## `Name`

**Signature:**
```cpp
const char* Name();
```

**Returns:**
- `const char*`

---

(value)=
## `Value`

**Signature:**
```cpp
const char* Value();
```

**Returns:**
- `const char*`

---

(valuestr)=
## `ValueStr`

**Signature:**
```cpp
const std::string& ValueStr();
```

**Returns:**
- `const std::string&`

---

(nametstr)=
## `NameTStr`

**Signature:**
```cpp
const TIXML_STRING& NameTStr();
```

**Returns:**
- `const TIXML_STRING&`

---

(setname)=
## `SetName`

**Signature:**
```cpp
void SetName(const char* _name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `_name` | - |

---

(setvalue)=
## `SetValue`

**Signature:**
```cpp
void SetValue(const char* _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `_value` | - |

---

(setname)=
## `SetName`

STL std::string form.

**Signature:**
```cpp
void SetName(const std::string& _name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_name` | - |

---

(setvalue)=
## `SetValue`

STL std::string form.

**Signature:**
```cpp
void SetValue(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

---

(next)=
## `Next`

**Signature:**
```cpp
TiXmlAttribute* Next();
```

**Returns:**
- `TiXmlAttribute*`

---

(previous)=
## `Previous`

**Signature:**
```cpp
TiXmlAttribute* Previous();
```

**Returns:**
- `TiXmlAttribute*`

---

(operator)=
## `operator<`

**Signature:**
```cpp
bool operator<(const TiXmlAttribute& rhs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlAttribute&` | `rhs` | - |

**Returns:**
- `bool`

---

(operator)=
## `operator>`

**Signature:**
```cpp
bool operator>(const TiXmlAttribute& rhs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlAttribute&` | `rhs` | - |

**Returns:**
- `bool`

---

(print)=
## `Print`

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |

**Returns:**
- `virtual void`

---

(setdocument)=
## `SetDocument`

**Signature:**
```cpp
void SetDocument(TiXmlDocument* doc);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlDocument*` | `doc` | - |

---

(first)=
## `First`

**Signature:**
```cpp
const TiXmlAttribute* First();
```

**Returns:**
- `const TiXmlAttribute*`

---

(first)=
## `First`

**Signature:**
```cpp
TiXmlAttribute* First();
```

**Returns:**
- `TiXmlAttribute*`

---

(last)=
## `Last`

**Signature:**
```cpp
const TiXmlAttribute* Last();
```

**Returns:**
- `const TiXmlAttribute*`

---

(last)=
## `Last`

**Signature:**
```cpp
TiXmlAttribute* Last();
```

**Returns:**
- `TiXmlAttribute*`

---

(readtype)=
## `readType`

**Signature:**
```cpp
inline T readType(const std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |

**Returns:**
- `inline T`

---

(queryvalueattribute)=
## `QueryValueAttribute`

**Signature:**
```cpp
int QueryValueAttribute(const std::string& name, T* outValue);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `T*` | `outValue` | - |

**Returns:**
- `int`

---

(queryvalueattribute)=
## `QueryValueAttribute`

**Signature:**
```cpp
int QueryValueAttribute(const std::string& name, std::string* outValue);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `std::string*` | `outValue` | - |

**Returns:**
- `int`

---

(setattribute)=
## `SetAttribute`

**Signature:**
```cpp
void SetAttribute(const std::string& name, int _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `int` | `_value` | - |

---

(firstattribute)=
## `FirstAttribute`

**Signature:**
```cpp
const TiXmlAttribute* FirstAttribute();
```

**Returns:**
- `const TiXmlAttribute*`

---

(firstattribute)=
## `FirstAttribute`

**Signature:**
```cpp
TiXmlAttribute* FirstAttribute();
```

**Returns:**
- `TiXmlAttribute*`

---

(lastattribute)=
## `LastAttribute`

**Signature:**
```cpp
const TiXmlAttribute* LastAttribute();
```

**Returns:**
- `const TiXmlAttribute*`

---

(lastattribute)=
## `LastAttribute`

**Signature:**
```cpp
TiXmlAttribute* LastAttribute();
```

**Returns:**
- `TiXmlAttribute*`

---

(toelement)=
## `ToElement`

**Signature:**
```cpp
virtual const TiXmlElement* ToElement();
```

**Returns:**
- `virtual const TiXmlElement*`

---

(toelement)=
## `ToElement`

**Signature:**
```cpp
virtual TiXmlElement* ToElement();
```

**Returns:**
- `virtual TiXmlElement*`

---

(tocomment)=
## `ToComment`

**Signature:**
```cpp
virtual const TiXmlComment* ToComment();
```

**Returns:**
- `virtual const TiXmlComment*`

---

(tocomment)=
## `ToComment`

**Signature:**
```cpp
virtual TiXmlComment* ToComment();
```

**Returns:**
- `virtual TiXmlComment*`

---

(cdata)=
## `CDATA`

Queries whether this represents text using a CDATA section.

**Signature:**
```cpp
bool CDATA();
```

**Returns:**
- `bool`

---

(setcdata)=
## `SetCDATA`

Turns on or off a CDATA representation of text.

**Signature:**
```cpp
void SetCDATA(bool _cdata);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `_cdata` | - |

---

(totext)=
## `ToText`

**Signature:**
```cpp
virtual const TiXmlText* ToText();
```

**Returns:**
- `virtual const TiXmlText*`

---

(totext)=
## `ToText`

**Signature:**
```cpp
virtual TiXmlText* ToText();
```

**Returns:**
- `virtual TiXmlText*`

---

(print)=
## `Print`

**Signature:**
```cpp
virtual void Print(FILE* cfile, int depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FILE*` | `cfile` | - |
| `int` | `depth` | - |

**Returns:**
- `virtual void`

---

(todeclaration)=
## `ToDeclaration`

**Signature:**
```cpp
virtual const TiXmlDeclaration* ToDeclaration();
```

**Returns:**
- `virtual const TiXmlDeclaration*`

---

(todeclaration)=
## `ToDeclaration`

**Signature:**
```cpp
virtual TiXmlDeclaration* ToDeclaration();
```

**Returns:**
- `virtual TiXmlDeclaration*`

---

(tixmlunknown)=
## `TiXmlUnknown`

**Signature:**
```cpp
public: TiXmlUnknown() : TiXmlNode( TiXmlNode::TINYXML_UNKNOWN);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) : TiXmlNode( TiXmlNode::` | `TINYXML_UNKNOWN` | - |

**Returns:**
- `public:`

---

(tounknown)=
## `ToUnknown`

**Signature:**
```cpp
virtual const TiXmlUnknown* ToUnknown();
```

**Returns:**
- `virtual const TiXmlUnknown*`

---

(tounknown)=
## `ToUnknown`

**Signature:**
```cpp
virtual TiXmlUnknown* ToUnknown();
```

**Returns:**
- `virtual TiXmlUnknown*`

---

(rootelement)=
## `RootElement`

**Signature:**
```cpp
const TiXmlElement* RootElement();
```

**Returns:**
- `const TiXmlElement*`

---

(rootelement)=
## `RootElement`

**Signature:**
```cpp
TiXmlElement* RootElement();
```

**Returns:**
- `TiXmlElement*`

---

(error)=
## `Error`

**Signature:**
```cpp
bool Error();
```

**Returns:**
- `bool`

---

(errordesc)=
## `ErrorDesc`

Contains a textual (english) description of the error if one occurs.

**Signature:**
```cpp
const char * ErrorDesc();
```

**Returns:**
- `const char *`

---

(errorid)=
## `ErrorId`

**Signature:**
```cpp
int ErrorId();
```

**Returns:**
- `int`

---

(errorrow)=
## `ErrorRow`

**Signature:**
```cpp
int ErrorRow();
```

**Returns:**
- `int`

---

(errorcol)=
## `ErrorCol`

**Signature:**
```cpp
int ErrorCol();
```

**Returns:**
- `int`

---

(settabsize)=
## `SetTabSize`

**Signature:**
```cpp
void SetTabSize(int _tabsize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `_tabsize` | - |

---

(tabsize)=
## `TabSize`

**Signature:**
```cpp
int TabSize();
```

**Returns:**
- `int`

---

(clearerror)=
## `ClearError`

**Signature:**
```cpp
void ClearError();
```

---

(print)=
## `Print`

Write the document to standard out using formatted printing ("pretty print").

**Signature:**
```cpp
void Print();
```

---

(todocument)=
## `ToDocument`

**Signature:**
```cpp
virtual const TiXmlDocument* ToDocument();
```

**Returns:**
- `virtual const TiXmlDocument*`

---

(todocument)=
## `ToDocument`

**Signature:**
```cpp
virtual TiXmlDocument* ToDocument();
```

**Returns:**
- `virtual TiXmlDocument*`

---

(firstchild)=
## `FirstChild`

**Signature:**
```cpp
TiXmlHandle FirstChild(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlHandle`

---

(firstchildelement)=
## `FirstChildElement`

**Signature:**
```cpp
TiXmlHandle FirstChildElement(const std::string& _value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |

**Returns:**
- `TiXmlHandle`

---

(child)=
## `Child`

**Signature:**
```cpp
TiXmlHandle Child(const std::string& _value, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |
| `int` | `index` | - |

**Returns:**
- `TiXmlHandle`

---

(childelement)=
## `ChildElement`

**Signature:**
```cpp
TiXmlHandle ChildElement(const std::string& _value, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `_value` | - |
| `int` | `index` | - |

**Returns:**
- `TiXmlHandle`

---

(tonode)=
## `ToNode`

Return the handle as a TiXmlNode. This may return null.

**Signature:**
```cpp
TiXmlNode* ToNode();
```

**Returns:**
- `TiXmlNode*`

---

(toelement)=
## `ToElement`

Return the handle as a TiXmlElement. This may return null.

**Signature:**
```cpp
TiXmlElement* ToElement();
```

**Returns:**
- `TiXmlElement*`

---

(totext)=
## `ToText`

Return the handle as a TiXmlText. This may return null.

**Signature:**
```cpp
TiXmlText* ToText();
```

**Returns:**
- `TiXmlText*`

---

(tounknown)=
## `ToUnknown`

Return the handle as a TiXmlUnknown. This may return null.

**Signature:**
```cpp
TiXmlUnknown* ToUnknown();
```

**Returns:**
- `TiXmlUnknown*`

---

(node)=
## `Node`

**Signature:**
```cpp
TiXmlNode* Node();
```

**Returns:**
- `TiXmlNode*`

---

(element)=
## `Element`

**Signature:**
```cpp
TiXmlElement* Element();
```

**Returns:**
- `TiXmlElement*`

---

(text)=
## `Text`

**Signature:**
```cpp
TiXmlText* Text();
```

**Returns:**
- `TiXmlText*`

---

(unknown)=
## `Unknown`

**Signature:**
```cpp
TiXmlUnknown* Unknown();
```

**Returns:**
- `TiXmlUnknown*`

---

(tixmlprinter)=
## `TiXmlPrinter`

**Signature:**
```cpp
public: TiXmlPrinter() : depth( 0 ), simpleTextPrint( false ), buffer(), indent( " " ), lineBreak( "\n");
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) : depth( 0 )` | - | - |
| `simpleTextPrint( false )` | - | - |
| `buffer()` | - | - |
| `indent( " " )` | - | - |
| `lineBreak( "\n"` | - | - |

**Returns:**
- `public:`

---

(tab)=
## `tab`

Set the indent characters for printing. By default 4 spaces

**Signature:**
```cpp
but tab(\t) is also useful, or null/empty string for no indentation. */ void SetIndent( const char* _indent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `\t) is also` | `useful` | - |
| `or null/empty string for no indentation. */ void SetIndent( const char*` | `_indent` | - |

**Returns:**
- `but`

---

(indent)=
## `Indent`

Query the indention string.

**Signature:**
```cpp
const char* Indent();
```

**Returns:**
- `const char*`

---

(setlinebreak)=
## `SetLineBreak`

**Signature:**
```cpp
void SetLineBreak(const char* _lineBreak);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `_lineBreak` | - |

---

(linebreak)=
## `LineBreak`

Query the current line breaking string.

**Signature:**
```cpp
const char* LineBreak();
```

**Returns:**
- `const char*`

---

(setstreamprinting)=
## `SetStreamPrinting`

**Signature:**
```cpp
void SetStreamPrinting();
```

---

(cstr)=
## `CStr`

Return the result.

**Signature:**
```cpp
const char* CStr();
```

**Returns:**
- `const char*`

---

(size)=
## `Size`

Return the length of the result string.

**Signature:**
```cpp
size_t Size();
```

**Returns:**
- `size_t`

---

(str)=
## `Str`

Return the result.

**Signature:**
```cpp
const std::string& Str();
```

**Returns:**
- `const std::string&`

---

(doindent)=
## `DoIndent`

**Signature:**
```cpp
private: void DoIndent();
```

**Returns:**
- `private: void`

---

(dolinebreak)=
## `DoLineBreak`

**Signature:**
```cpp
void DoLineBreak();
```

---

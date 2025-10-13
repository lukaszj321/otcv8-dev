# src/framework/xml/tinyxml.h

```cpp
or the string class(TiXmlString in non-STL mode, std::string in STL mode.) Either or both cfile and str can be null. This is a formatted print, and will insert tabs and newlines. (For an unformatted stream, use the << operator.) */ virtual void Print( FILE* cfile, int depth);
```
All TinyXml classes can print themselves to a filestream

```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding /*= TIXML_ENCODING_UNKNOWN */);
```
```cpp
static void EncodeString(const TIXML_STRING& str, TIXML_STRING* out);
```
```cpp
protected: static const char* SkipWhiteSpace(const char*, TiXmlEncoding encoding);
```
```cpp
return IsWhiteSpace((char) c);
```
```cpp
static bool StreamWhiteSpace(std::istream * in, TIXML_STRING * tag);
```
```cpp
static bool StreamTo(std::istream * in, int character, TIXML_STRING * tag);
```
```cpp
static const char* ReadName(const char* p, TIXML_STRING* name, TiXmlEncoding encoding);
```
```cpp
static const char* GetEntity(const char* in, char* value, int* length, TiXmlEncoding encoding);
```
```cpp
return GetEntity(p, _value, length, encoding);
```
```cpp
static bool StringEqual(const char* p, const char* endTag, bool ignoreCase, TiXmlEncoding encoding);
```
```cpp
static int IsAlpha(unsigned char anyByte, TiXmlEncoding encoding);
```
```cpp
static int IsAlphaNum(unsigned char anyByte, TiXmlEncoding encoding);
```
```cpp
return tolower(v);
```
```cpp
static void ConvertUTF32ToUTF8(unsigned long input, char* output, int* length);
```
```cpp
friend std::ostream& operator<<(std::ostream& out, const TiXmlNode& base);
```
```cpp
friend std::string& operator<<(std::string& out, const TiXmlNode& base);
```
Appends the XML node or attribute to a std::string.

```cpp
void Clear();
```
Delete all the children of this node. Does not affect 'this'.

```cpp
const TiXmlNode* IterateChildren(const TiXmlNode* previous);
```
```cpp
const TiXmlNode* IterateChildren(const char * value, const TiXmlNode* previous);
```
This flavor of IterateChildren searches for children with a particular 'value'

```cpp
TiXmlNode* InsertEndChild(const TiXmlNode& addThis);
```
```cpp
henceforth owned(and deleted) by tinyXml. This method is efficient and avoids an extra copy, but should be used with care as it uses a different memory model than the other insert functions. @sa InsertEndChild */ TiXmlNode* LinkEndChild( TiXmlNode* addThis);
```
```cpp
TiXmlNode* InsertBeforeChild(TiXmlNode* beforeThis, const TiXmlNode& addThis);
```
```cpp
TiXmlNode* InsertAfterChild(TiXmlNode* afterThis, const TiXmlNode& addThis);
```
```cpp
TiXmlNode* ReplaceChild(TiXmlNode* replaceThis, const TiXmlNode& withThis);
```
```cpp
bool RemoveChild(TiXmlNode* removeThis);
```
Delete a child of this node.

```cpp
const TiXmlNode* PreviousSibling(const char *);
```
Navigate to a sibling node.

```cpp
const TiXmlNode* NextSibling(const char *);
```
Navigate to a sibling node with the given 'value'.

```cpp
const TiXmlElement* NextSiblingElement();
```
```cpp
const TiXmlElement* NextSiblingElement(const char *);
```
```cpp
const TiXmlElement* FirstChildElement();
```
Convenience function to get through elements.

```cpp
const TiXmlElement* FirstChildElement(const char * _value);
```
Convenience function to get through elements.

```cpp
const TiXmlDocument* GetDocument();
```
```cpp
virtual TiXmlNode* Clone();
```
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```
```cpp
protected: TiXmlNode(NodeType _type);
```
```cpp
void CopyTo(TiXmlNode* target);
```
```cpp
virtual void StreamIn(std::istream* in, TIXML_STRING* tag);
```
```cpp
TiXmlNode* Identify(const char* start, TiXmlEncoding encoding);
```
```cpp
int QueryIntValue(int* _value);
```
```cpp
int QueryDoubleValue(double* _value);
```
QueryDoubleValue examines the value string. See QueryIntValue().

```cpp
const TiXmlAttribute* Next();
```
Get the next sibling attribute in the DOM. Returns null at end.

```cpp
const TiXmlAttribute* Previous();
```
Get the previous sibling attribute in the DOM. Returns null at beginning.

```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
void Print(FILE* cfile, int depth, TIXML_STRING* str);
```
```cpp
public: TiXmlAttributeSet();
```
```cpp
void Add(TiXmlAttribute* attribute);
```
```cpp
void Remove(TiXmlAttribute* attribute);
```
```cpp
TiXmlAttribute* Find(const char* _name);
```
```cpp
TiXmlAttribute* FindOrCreate(const char* _name);
```
```cpp
TiXmlAttribute* Find(const std::string& _name);
```
```cpp
TiXmlAttribute* FindOrCreate(const std::string& _name);
```
```cpp
public: TiXmlElement(const std::string& _value);
```
```cpp
return T();
```
```cpp
std::stringstream sstream(node->ValueStr());
```
```cpp
std::string Attribute(const std::string& name);
```
```cpp
std::string Attribute(const std::string& name, int* i);
```
```cpp
std::string Attribute(const std::string& name, double* d);
```
```cpp
void SetAttribute(const std::string& name, const std::string& _value);
```
```cpp
void RemoveAttribute(const std::string& name);
```
```cpp
WARNING: GetText() accesses a child node - don't become confused with the similarly named TiXmlHandle::Text() and TiXmlNode::ToText() which are safe type casts on the referenced node. */ const char* GetText();
```
```cpp
virtual TiXmlNode* Clone();
```
Creates a new Element and returns it - the returned element is a copy.

```cpp
virtual void Print(FILE* cfile, int depth);
```
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```
Walk the XML tree visiting this node and all of its children.

```cpp
protected: void CopyTo(TiXmlElement* target);
```
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```
```cpp
const char* ReadValue(const char* in, TiXmlParsingData* prevData, TiXmlEncoding encoding);
```
```cpp
virtual TiXmlNode* Clone();
```
Returns a copy of this Comment.

```cpp
virtual void Print(FILE* cfile, int depth);
```
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```
Walk the XML tree visiting this node and all of its children.

```cpp
protected: void CopyTo(TiXmlComment* target);
```
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```
```cpp
virtual void Print(FILE* cfile, int depth);
```
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual bool Accept(TiXmlVisitor* content);
```
Walk the XML tree visiting this node and all of its children.

```cpp
virtual TiXmlNode* Clone();
```
[internal use] Creates a new Element and returns it.

```cpp
void CopyTo(TiXmlText* target);
```
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```
```cpp
virtual TiXmlNode* Clone();
```
Creates a copy of this Declaration and returns it.

```cpp
virtual void Print(FILE* cfile, int depth, TIXML_STRING* str);
```
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual bool Accept(TiXmlVisitor* visitor);
```
Walk the XML tree visiting this node and all of its children.

```cpp
protected: void CopyTo(TiXmlDeclaration* target);
```
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```
```cpp
virtual TiXmlNode* Clone();
```
Creates a copy of this Unknown and returns it.

```cpp
virtual void Print(FILE* cfile, int depth);
```
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual bool Accept(TiXmlVisitor* content);
```
Walk the XML tree visiting this node and all of its children.

```cpp
protected: void CopyTo(TiXmlUnknown* target);
```
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```
```cpp
bool LoadFile(TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
```cpp
bool SaveFile();
```
Save a file using the current document value. Returns true if successful.

```cpp
bool LoadFile(const char * filename, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
Load a file using the given filename. Returns true if successful.

```cpp
bool SaveFile(const char * filename);
```
Save a file using the given filename. Returns true if successful.

```cpp
bool LoadFile(FILE*, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
```cpp
bool SaveFile(FILE*);
```
Save a file using the given FILE*. Returns true if successful.

```cpp
return LoadFile(filename.c_str(), encoding);
```
```cpp
return SaveFile(filename.c_str());
```
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data = 0, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
```cpp
will allocate a character array(new char[]) and return it as a pointer. The calling code pust call delete[] on the return char* to avoid a memory leak. */ //char* PrintToMemory();
```
```cpp
virtual void Print(FILE* cfile, int depth = 0);
```
Print this Document to a FILE stream.

```cpp
void SetError(int err, const char* errorLocation, TiXmlParsingData* prevData, TiXmlEncoding encoding);
```
```cpp
virtual bool Accept(TiXmlVisitor* content);
```
Walk the XML tree visiting this node and all of its children.

```cpp
virtual TiXmlNode* Clone();
```
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```
```cpp
private: void CopyTo(TiXmlDocument* target);
```
```cpp
TiXmlHandle docHandle(&document);
```
```cpp
TiXmlHandle FirstChild();
```
Return a handle to the first child node.

```cpp
TiXmlHandle FirstChild(const char * value);
```
Return a handle to the first child node with the given name.

```cpp
TiXmlHandle FirstChildElement();
```
Return a handle to the first child element.

```cpp
TiXmlHandle FirstChildElement(const char * value);
```
Return a handle to the first child element with the given name.

```cpp
TiXmlHandle Child(const char* value, int index);
```
```cpp
TiXmlHandle Child(int index);
```
```cpp
TiXmlHandle ChildElement(const char* value, int index);
```
```cpp
TiXmlHandle ChildElement(int index);
```
```cpp
virtual bool VisitEnter(const TiXmlDocument& doc);
```
```cpp
virtual bool VisitExit(const TiXmlDocument& doc);
```
```cpp
virtual bool VisitEnter(const TiXmlElement& element, const TiXmlAttribute* firstAttribute);
```
```cpp
virtual bool VisitExit(const TiXmlElement& element);
```
```cpp
virtual bool Visit(const TiXmlDeclaration& declaration);
```
```cpp
virtual bool Visit(const TiXmlText& text);
```
```cpp
virtual bool Visit(const TiXmlComment& comment);
```
```cpp
virtual bool Visit(const TiXmlUnknown& unknown);
```
```cpp
void Clear();
```
```cpp
virtual bool VisitEnter(const TiXmlDocument& /*doc*/);
```
Visit a document.

```cpp
virtual bool VisitExit(const TiXmlDocument& /*doc*/);
```
Visit a document.

```cpp
virtual bool VisitEnter(const TiXmlElement& /*element*/, const TiXmlAttribute* /*firstAttribute*/);
```
Visit an element.

```cpp
virtual bool VisitExit(const TiXmlElement& /*element*/);
```
Visit an element.

```cpp
virtual bool Visit(const TiXmlDeclaration& /*declaration*/);
```
Visit a declaration

```cpp
virtual bool Visit(const TiXmlText& /*text*/);
```
Visit a text node

```cpp
virtual bool Visit(const TiXmlComment& /*comment*/);
```
Visit a comment node

```cpp
virtual bool Visit(const TiXmlUnknown& /*unknown*/);
```
Visit an unknown node

```cpp
static void SetCondenseWhiteSpace(bool condense);
```
```cpp
static bool IsWhiteSpaceCondensed();
```
Return the current white space setting.

```cpp
can be disabled if TiXmlDocument::SetTabSize() is called with 0 as the value. @sa TiXmlDocument::SetTabSize() */ int Row();
```
```cpp
int Column();
```
```cpp
void SetUserData(void* user);
```
```cpp
void* GetUserData();
```
```cpp
const void* GetUserData();
```
```cpp
inline static bool IsWhiteSpace(char c);
```
```cpp
inline static bool IsWhiteSpace(int c);
```
```cpp
inline static const char* GetChar(const char* p, char* _value, int* length, TiXmlEncoding encoding);
```
```cpp
else if(*length);
```
```cpp
inline static int ToLower(int v, TiXmlEncoding encoding);
```
```cpp
this is more efficient than calling Value(). Only available in STL mode. */ const std::string& ValueStr();
```
Return Value() as a std::string. If you only use STL,

```cpp
const TIXML_STRING& ValueTStr();
```
```cpp
void SetValue(const char * _value);
```
```cpp
void SetValue(const std::string& _value);
```
STL std::string form.

```cpp
TiXmlNode* Parent();
```
One step up the DOM.

```cpp
const TiXmlNode* Parent();
```
```cpp
const TiXmlNode* FirstChild();
```
```cpp
TiXmlNode* FirstChild();
```
```cpp
TiXmlNode* FirstChild(const char * _value);
```
The first child of this node with the matching 'value'. Will be null if none found.

```cpp
const TiXmlNode* LastChild();
```
```cpp
TiXmlNode* LastChild();
```
```cpp
TiXmlNode* LastChild(const char * _value);
```
```cpp
const TiXmlNode* FirstChild(const std::string& _value);
```
```cpp
TiXmlNode* FirstChild(const std::string& _value);
```
```cpp
const TiXmlNode* LastChild(const std::string& _value);
```
```cpp
TiXmlNode* LastChild(const std::string& _value);
```
```cpp
TiXmlNode* IterateChildren(const TiXmlNode* previous);
```
```cpp
TiXmlNode* IterateChildren(const char * _value, const TiXmlNode* previous);
```
```cpp
const TiXmlNode* IterateChildren(const std::string& _value, const TiXmlNode* previous);
```
```cpp
TiXmlNode* IterateChildren(const std::string& _value, const TiXmlNode* previous);
```
```cpp
const TiXmlNode* PreviousSibling();
```
Navigate to a sibling node.

```cpp
TiXmlNode* PreviousSibling();
```
```cpp
TiXmlNode* PreviousSibling(const char *_prev);
```
```cpp
const TiXmlNode* PreviousSibling(const std::string& _value);
```
```cpp
TiXmlNode* PreviousSibling(const std::string& _value);
```
```cpp
const TiXmlNode* NextSibling(const std::string& _value);
```
```cpp
TiXmlNode* NextSibling(const std::string& _value);
```
```cpp
const TiXmlNode* NextSibling();
```
Navigate to a sibling node.

```cpp
TiXmlNode* NextSibling();
```
```cpp
TiXmlNode* NextSibling(const char* _next);
```
```cpp
TiXmlElement* NextSiblingElement();
```
```cpp
TiXmlElement* NextSiblingElement(const char *_next);
```
```cpp
const TiXmlElement* NextSiblingElement(const std::string& _value);
```
```cpp
TiXmlElement* NextSiblingElement(const std::string& _value);
```
```cpp
TiXmlElement* FirstChildElement();
```
```cpp
TiXmlElement* FirstChildElement(const char * _value);
```
```cpp
const TiXmlElement* FirstChildElement(const std::string& _value);
```
```cpp
TiXmlElement* FirstChildElement(const std::string& _value);
```
```cpp
int Type();
```
```cpp
TiXmlDocument* GetDocument();
```
```cpp
bool NoChildren();
```
Returns true if this node has no children.

```cpp
virtual const TiXmlDocument* ToDocument();
```
```cpp
virtual const TiXmlElement* ToElement();
```
```cpp
virtual const TiXmlComment* ToComment();
```
```cpp
virtual const TiXmlUnknown* ToUnknown();
```
```cpp
virtual const TiXmlText* ToText();
```
```cpp
virtual const TiXmlDeclaration* ToDeclaration();
```
```cpp
virtual TiXmlDocument* ToDocument();
```
```cpp
virtual TiXmlElement* ToElement();
```
```cpp
virtual TiXmlComment* ToComment();
```
```cpp
virtual TiXmlUnknown* ToUnknown();
```
```cpp
virtual TiXmlText* ToText();
```
```cpp
virtual TiXmlDeclaration* ToDeclaration();
```
```cpp
const char* Name();
```
```cpp
const char* Value();
```
```cpp
const std::string& ValueStr();
```
```cpp
const TIXML_STRING& NameTStr();
```
```cpp
void SetName(const char* _name);
```
```cpp
void SetValue(const char* _value);
```
```cpp
void SetName(const std::string& _name);
```
STL std::string form.

```cpp
void SetValue(const std::string& _value);
```
STL std::string form.

```cpp
TiXmlAttribute* Next();
```
```cpp
TiXmlAttribute* Previous();
```
```cpp
bool operator<(const TiXmlAttribute& rhs);
```
```cpp
bool operator>(const TiXmlAttribute& rhs);
```
```cpp
virtual void Print(FILE* cfile, int depth);
```
```cpp
void SetDocument(TiXmlDocument* doc);
```
```cpp
const TiXmlAttribute* First();
```
```cpp
TiXmlAttribute* First();
```
```cpp
const TiXmlAttribute* Last();
```
```cpp
TiXmlAttribute* Last();
```
```cpp
inline T readType(const std::string& str);
```
```cpp
int QueryValueAttribute(const std::string& name, T* outValue);
```
```cpp
int QueryValueAttribute(const std::string& name, std::string* outValue);
```
```cpp
void SetAttribute(const std::string& name, int _value);
```
```cpp
const TiXmlAttribute* FirstAttribute();
```
```cpp
TiXmlAttribute* FirstAttribute();
```
```cpp
const TiXmlAttribute* LastAttribute();
```
```cpp
TiXmlAttribute* LastAttribute();
```
```cpp
virtual const TiXmlElement* ToElement();
```
```cpp
virtual TiXmlElement* ToElement();
```
```cpp
virtual const TiXmlComment* ToComment();
```
```cpp
virtual TiXmlComment* ToComment();
```
```cpp
bool CDATA();
```
Queries whether this represents text using a CDATA section.

```cpp
void SetCDATA(bool _cdata);
```
Turns on or off a CDATA representation of text.

```cpp
virtual const TiXmlText* ToText();
```
```cpp
virtual TiXmlText* ToText();
```
```cpp
virtual void Print(FILE* cfile, int depth);
```
```cpp
virtual const TiXmlDeclaration* ToDeclaration();
```
```cpp
virtual TiXmlDeclaration* ToDeclaration();
```
```cpp
public: TiXmlUnknown() : TiXmlNode( TiXmlNode::TINYXML_UNKNOWN);
```
```cpp
virtual const TiXmlUnknown* ToUnknown();
```
```cpp
virtual TiXmlUnknown* ToUnknown();
```
```cpp
const TiXmlElement* RootElement();
```
```cpp
TiXmlElement* RootElement();
```
```cpp
bool Error();
```
```cpp
const char * ErrorDesc();
```
Contains a textual (english) description of the error if one occurs.

```cpp
int ErrorId();
```
```cpp
int ErrorRow();
```
```cpp
int ErrorCol();
```
```cpp
void SetTabSize(int _tabsize);
```
```cpp
int TabSize();
```
```cpp
void ClearError();
```
```cpp
void Print();
```
Write the document to standard out using formatted printing ("pretty print").

```cpp
virtual const TiXmlDocument* ToDocument();
```
```cpp
virtual TiXmlDocument* ToDocument();
```
```cpp
TiXmlHandle FirstChild(const std::string& _value);
```
```cpp
TiXmlHandle FirstChildElement(const std::string& _value);
```
```cpp
TiXmlHandle Child(const std::string& _value, int index);
```
```cpp
TiXmlHandle ChildElement(const std::string& _value, int index);
```
```cpp
TiXmlNode* ToNode();
```
Return the handle as a TiXmlNode. This may return null.

```cpp
TiXmlElement* ToElement();
```
Return the handle as a TiXmlElement. This may return null.

```cpp
TiXmlText* ToText();
```
Return the handle as a TiXmlText. This may return null.

```cpp
TiXmlUnknown* ToUnknown();
```
Return the handle as a TiXmlUnknown. This may return null.

```cpp
TiXmlNode* Node();
```
```cpp
TiXmlElement* Element();
```
```cpp
TiXmlText* Text();
```
```cpp
TiXmlUnknown* Unknown();
```
```cpp
public: TiXmlPrinter() : depth( 0 ), simpleTextPrint( false ), buffer(), indent( " " ), lineBreak( "\n");
```
```cpp
but tab(\t) is also useful, or null/empty string for no indentation. */ void SetIndent( const char* _indent);
```
Set the indent characters for printing. By default 4 spaces

```cpp
const char* Indent();
```
Query the indention string.

```cpp
void SetLineBreak(const char* _lineBreak);
```
```cpp
const char* LineBreak();
```
Query the current line breaking string.

```cpp
void SetStreamPrinting();
```
```cpp
const char* CStr();
```
Return the result.

```cpp
size_t Size();
```
Return the length of the result string.

```cpp
const std::string& Str();
```
Return the result.

```cpp
private: void DoIndent();
```
```cpp
void DoLineBreak();
```
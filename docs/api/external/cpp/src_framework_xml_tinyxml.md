# src/framework/xml/tinyxml.h

```cpp
Original code by Lee Thomason(www.grinninglizard.com) This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software. Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions: 1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required. 2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software. 3. This notice may not be removed or altered from any source distribution. */ #ifndef TINYXML_INCLUDED #define TINYXML_INCLUDED #define TIXML_USE_STL // use STL strings instead #ifdef _MSC_VER #pragma warning( push ) #pragma warning( disable : 4530 ) #pragma warning( disable : 4786 ) #endif #include <ctype.h> #include <stdio.h> #include <stdlib.h> #include <string.h> #include <framework/const.h> #include <framework/stdext/cast.h> #include <framework/stdext/string.h> // Help out windows: #if defined( _DEBUG ) && !defined( DEBUG ) #define DEBUG #endif #ifdef TIXML_USE_STL #include <string> #include <iostream> #include <sstream> #define TIXML_STRING std::string #else #include "tinystr.h" #define TIXML_STRING TiXmlString #endif // Deprecated library function hell. Compilers want to use the // new safe versions. This probably doesn't fully address the problem, // but it gets closer. There are too many compilers for me to fully // test. If you get compilation troubles, undefine TIXML_SAFE #define TIXML_SAFE #ifdef TIXML_SAFE #if defined(_MSC_VER) && (_MSC_VER >= 1400 ) // Microsoft visual studio, version 2005 and higher. #define TIXML_SNPRINTF _snprintf_s #define TIXML_SSCANF sscanf_s #elif defined(_MSC_VER) && (_MSC_VER >= 1200 ) // Microsoft visual studio, version 6 and higher. //#pragma message( "Using _sn* functions." ) #define TIXML_SNPRINTF _snprintf #define TIXML_SSCANF sscanf #elif defined(__GNUC__) && (__GNUC__ >= 3 ) // GCC version 3 and higher.s //#warning( "Using sn* functions." ) #define TIXML_SNPRINTF snprintf #define TIXML_SSCANF sscanf #else #define TIXML_SNPRINTF snprintf #define TIXML_SSCANF sscanf #endif #endif class TiXmlDocument; class TiXmlElement; class TiXmlComment; class TiXmlUnknown; class TiXmlAttribute; class TiXmlText; class TiXmlDeclaration; class TiXmlParsingData; const int TIXML_MAJOR_VERSION = 2; const int TIXML_MINOR_VERSION = 6; const int TIXML_PATCH_VERSION = 2; /* Internal structure for tracking location of items in the XML file. */ struct TiXmlCursor { TiXmlCursor() { Clear();
```
```cpp
void Clear() { row = col = -1; } int row; // 0 based. int col; // 0 based. }; /** Implements the interface to the "Visitor pattern" (see the Accept() method.) If you call the Accept() method, it requires being passed a TiXmlVisitor class to handle callbacks. For nodes that contain other nodes (Document, Element) you will get called with a VisitEnter/VisitExit pair. Nodes that are always leaves are simply called with Visit(). If you return 'true' from a Visit method, recursive parsing will continue. If you return false, <b>no children of this node or its sibilings</b> will be Visited. All flavors of Visit methods have a default implementation that returns 'true' (continue visiting). You need to only override methods that are interesting to you. Generally Accept() is called on the TiXmlDocument, although all nodes suppert Visiting. You should never change the document from a callback. @sa TiXmlNode::Accept() */ class TiXmlVisitor { public: virtual ~TiXmlVisitor() {} /// Visit a document. virtual bool VisitEnter( const TiXmlDocument& /*doc*/ ) { return true; } /// Visit a document. virtual bool VisitExit( const TiXmlDocument& /*doc*/ ) { return true; } /// Visit an element. virtual bool VisitEnter( const TiXmlElement& /*element*/, const TiXmlAttribute* /*firstAttribute*/ ) { return true; } /// Visit an element. virtual bool VisitExit( const TiXmlElement& /*element*/ ) { return true; } /// Visit a declaration virtual bool Visit( const TiXmlDeclaration& /*declaration*/ ) { return true; } /// Visit a text node virtual bool Visit( const TiXmlText& /*text*/ ) { return true; } /// Visit a comment node virtual bool Visit( const TiXmlComment& /*comment*/ ) { return true; } /// Visit an unknown node virtual bool Visit( const TiXmlUnknown& /*unknown*/ ) { return true; } }; // Only used by Attribute::Query functions enum { TIXML_SUCCESS, TIXML_NO_ATTRIBUTE, TIXML_WRONG_TYPE }; // Used by the parsing routines. enum TiXmlEncoding { TIXML_ENCODING_UNKNOWN, TIXML_ENCODING_UTF8, TIXML_ENCODING_LEGACY }; static const TiXmlEncoding TIXML_DEFAULT_ENCODING = TIXML_ENCODING_UNKNOWN; /** TiXmlBase is a base class for every class in TinyXml. It does little except to establish that TinyXml classes can be printed and provide some utility functions. In XML, the document and elements can contain other elements and other types of nodes. @verbatim A Document can contain: Element (container or leaf) Comment (leaf) Unknown (leaf) Declaration( leaf ) An Element can contain: Element (container or leaf) Text (leaf) Attributes (not on tree) Comment (leaf) Unknown (leaf) A Decleration contains: Attributes (not on tree) @endverbatim */ class TiXmlBase { friend class TiXmlNode; friend class TiXmlElement; friend class TiXmlDocument; public: TiXmlBase( const TiXmlBase& ) = delete; void operator=( const TiXmlBase& base ) = delete; TiXmlBase() : userData(0) {} virtual ~TiXmlBase() {} /** All TinyXml classes can print themselves to a filestream or the string class (TiXmlString in non-STL mode, std::string in STL mode.) Either or both cfile and str can be null. This is a formatted print, and will insert tabs and newlines. (For an unformatted stream, use the << operator.) */ virtual void Print( FILE* cfile, int depth ) const = 0; /** The world does not agree on whether white space should be kept or not. In order to make everyone happy, these global, static functions are provided to set whether or not TinyXml will condense all white space into a single space or not. The default is to condense. Note changing this value is not thread safe. */ static void SetCondenseWhiteSpace( bool condense ) { condenseWhiteSpace = condense; } /// Return the current white space setting. static bool IsWhiteSpaceCondensed() { return condenseWhiteSpace; } /** Return the position, in the original source file, of this node or attribute. The row and column are 1-based. (That is the first row and first column is 1,1). If the returns values are 0 or less, then the parser does not have a row and column value. Generally, the row and column value will be set when the TiXmlDocument::Load(), TiXmlDocument::LoadFile(), or any TiXmlNode::Parse() is called. It will NOT be set when the DOM was created from operator>>. The values reflect the initial load. Once the DOM is modified programmatically (by adding or changing nodes and attributes) the new values will NOT update to reflect changes in the document. There is a minor performance cost to computing the row and column. Computation can be disabled if TiXmlDocument::SetTabSize() is called with 0 as the value. @sa TiXmlDocument::SetTabSize() */ int Row() const { return location.row + 1; } int Column() const { return location.col + 1; } ///< See Row() void SetUserData( void* user ) { userData = user; } ///< Set a pointer to arbitrary user data. void* GetUserData() { return userData; } ///< Get a pointer to arbitrary user data. const void* GetUserData() const { return userData; } ///< Get a pointer to arbitrary user data. // Table that returs, for a given lead byte, the total number of bytes // in the UTF-8 sequence. static const int utf8ByteTable[256]; virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding /*= TIXML_ENCODING_UNKNOWN */ ) = 0; /** Expands entities in a string. Note this should not contian the tag's '<', '>', etc, or they will be transformed into entities! */ static void EncodeString( const TIXML_STRING& str, TIXML_STRING* out);
```
```cpp
protected:

    static const char* SkipWhiteSpace(const char*, TiXmlEncoding encoding);
```
```cpp
inline static bool IsWhiteSpace(char c ) { return ( isspace( (unsigned char) c ) || c == '\n' || c == '\r');
```
```cpp
inline static bool IsWhiteSpace(int c ) { if ( c < 256 ) return IsWhiteSpace( (char) c);
```
```cpp
static bool    StreamWhiteSpace(std::istream * in, TIXML_STRING * tag);
```
```cpp
static bool StreamTo(std::istream * in, int character, TIXML_STRING * tag);
```
```cpp
static const char* ReadName(const char* p, TIXML_STRING* name, TiXmlEncoding encoding);
```
```cpp
static const char* ReadText(const char* in, // where to start TIXML_STRING* text, // the string read bool ignoreWhiteSpace, // whether to keep the white space const char* endTag, // what ends this text bool ignoreCase, // whether to ignore case in the end tag TiXmlEncoding encoding);
```
```cpp
static const char* GetEntity(const char* in, char* value, int* length, TiXmlEncoding encoding);
```
```cpp
inline static const char* GetChar(const char* p, char* _value, int* length, TiXmlEncoding encoding ) { VALIDATE( p);
```
```cpp
return GetEntity(p, _value, length, encoding);
```
```cpp
else if(*length ) { //strncpy( _value, p, *length);
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
inline static int ToLower(int v, TiXmlEncoding encoding ) { if ( encoding == TIXML_ENCODING_UTF8 ) { if ( v < 128 ) return tolower( v);
```
```cpp
return tolower(v);
```
```cpp
static void ConvertUTF32ToUTF8(unsigned long input, char* output, int* length);
```
```cpp
public:
    TiXmlNode(const TiXmlNode& ) = delete; void operator=( const TiXmlNode& base ) = delete; #ifdef TIXML_USE_STL /** An input stream operator, for every class. Tolerant of newlines and formatting, but doesn't expect them. */ friend std::istream& operator >> (std::istream& in, TiXmlNode& base);
```
```cpp
this is more efficient than calling Value(). Only available in STL mode. */ const std::string& ValueStr() const { return value; } #endif const TIXML_STRING& ValueTStr() const { return value; } /** Changes the value of the node. Defined as: @verbatim Document: filename of the xml file Element: name of the element Comment: the comment text Unknown: the tag contents Text: the text string @endverbatim */ void SetValue(const char * _value) { value = _value;} #ifdef TIXML_USE_STL /// STL std::string form. void SetValue( const std::string& _value ) { value = _value; } #endif /// Delete all the children of this node. Does not affect 'this'. void Clear();
```
Return Value() as a std::string. If you only use STL,

```cpp
TiXmlNode* Parent() { return parent; } const TiXmlNode* Parent() const { return parent; } const TiXmlNode* FirstChild() const { return firstChild; } ///< The first child of this node. Will be null if there are no children. TiXmlNode* FirstChild() { return firstChild; } const TiXmlNode* FirstChild( const char * value ) const; ///< The first child of this node with the matching 'value'. Will be null if none found. /// The first child of this node with the matching 'value'. Will be null if none found. TiXmlNode* FirstChild( const char * _value ) { // Call through to the const version - safe since nothing is changed. Exiting syntax: cast this to a const (always safe) // call the method, cast the return back to non-const. return const_cast< TiXmlNode* > ((const_cast< const TiXmlNode* >(this))->FirstChild( _value ));
```
One step up the DOM.

```cpp
const TiXmlNode* LastChild() const { return lastChild; } /// The last child of this node. Will be null if there are no children. TiXmlNode* LastChild() { return lastChild; } const TiXmlNode* LastChild( const char * value ) const; /// The last child of this node matching 'value'. Will be null if there are no children. TiXmlNode* LastChild( const char * _value ) { return const_cast< TiXmlNode* > ((const_cast< const TiXmlNode* >(this))->LastChild( _value ));
```
```cpp
const TiXmlNode* FirstChild(const std::string& _value ) const { return FirstChild (_value.c_str ());
```
```cpp
TiXmlNode* FirstChild(const std::string& _value ) { return FirstChild (_value.c_str ());
```
```cpp
const TiXmlNode* LastChild(const std::string& _value ) const { return LastChild (_value.c_str ());
```
```cpp
TiXmlNode* LastChild(const std::string& _value ) { return LastChild (_value.c_str ());
```
```cpp
const TiXmlNode* IterateChildren(const TiXmlNode* previous ) const; TiXmlNode* IterateChildren( const TiXmlNode* previous ) { return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->IterateChildren( previous ));
```
```cpp
const TiXmlNode* IterateChildren(const char * value, const TiXmlNode* previous ) const; TiXmlNode* IterateChildren( const char * _value, const TiXmlNode* previous ) { return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->IterateChildren( _value, previous ));
```
This flavor of IterateChildren searches for children with a particular 'value'

```cpp
const TiXmlNode* IterateChildren(const std::string& _value, const TiXmlNode* previous ) const { return IterateChildren (_value.c_str (), previous);
```
```cpp
TiXmlNode* IterateChildren(const std::string& _value, const TiXmlNode* previous ) { return IterateChildren (_value.c_str (), previous);
```
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
const TiXmlNode* PreviousSibling() const { return prev; } TiXmlNode* PreviousSibling() { return prev; } /// Navigate to a sibling node. const TiXmlNode* PreviousSibling( const char * ) const; TiXmlNode* PreviousSibling( const char *_prev ) { return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->PreviousSibling( _prev ));
```
Navigate to a sibling node.

```cpp
const TiXmlNode* PreviousSibling(const std::string& _value ) const { return PreviousSibling (_value.c_str ());
```
```cpp
TiXmlNode* PreviousSibling(const std::string& _value ) { return PreviousSibling (_value.c_str ());
```
```cpp
const TiXmlNode* NextSibling(const std::string& _value) const { return NextSibling (_value.c_str ());
```
```cpp
TiXmlNode* NextSibling(const std::string& _value) { return NextSibling (_value.c_str ());
```
```cpp
const TiXmlNode* NextSibling() const { return next; } TiXmlNode* NextSibling() { return next; } /// Navigate to a sibling node with the given 'value'. const TiXmlNode* NextSibling( const char * ) const; TiXmlNode* NextSibling( const char* _next ) { return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->NextSibling( _next ));
```
Navigate to a sibling node.

```cpp
const TiXmlElement* NextSiblingElement() const; TiXmlElement* NextSiblingElement() { return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->NextSiblingElement());
```
```cpp
const TiXmlElement* NextSiblingElement(const char * ) const; TiXmlElement* NextSiblingElement( const char *_next ) { return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->NextSiblingElement( _next ));
```
```cpp
const TiXmlElement* NextSiblingElement(const std::string& _value) const { return NextSiblingElement (_value.c_str ());
```
```cpp
TiXmlElement* NextSiblingElement(const std::string& _value) { return NextSiblingElement (_value.c_str ());
```
```cpp
const TiXmlElement* FirstChildElement() const; TiXmlElement* FirstChildElement() { return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->FirstChildElement());
```
Convenience function to get through elements.

```cpp
const TiXmlElement* FirstChildElement(const char * _value ) const; TiXmlElement* FirstChildElement( const char * _value ) { return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->FirstChildElement( _value ));
```
Convenience function to get through elements.

```cpp
const TiXmlElement* FirstChildElement(const std::string& _value ) const { return FirstChildElement (_value.c_str ());
```
```cpp
TiXmlElement* FirstChildElement(const std::string& _value ) { return FirstChildElement (_value.c_str ());
```
```cpp
int Type() const { return type; } /** Return a pointer to the Document this node lives in. Returns null if not in a document. */ const TiXmlDocument* GetDocument() const; TiXmlDocument* GetDocument() { return const_cast< TiXmlDocument* >( (const_cast< const TiXmlNode* >(this))->GetDocument());
```
```cpp
bool NoChildren() const { return !firstChild; } virtual const TiXmlDocument* ToDocument() const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual const TiXmlElement* ToElement() const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual const TiXmlComment* ToComment() const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual const TiXmlUnknown* ToUnknown() const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual const TiXmlText* ToText() const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual const TiXmlDeclaration* ToDeclaration() const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual TiXmlDocument* ToDocument() { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual TiXmlElement* ToElement() { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual TiXmlComment* ToComment() { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual TiXmlUnknown* ToUnknown() { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual TiXmlText* ToText() { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. virtual TiXmlDeclaration* ToDeclaration() { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type. /** Create an exact duplicate of this node and return it. The memory must be deleted by the caller. */ virtual TiXmlNode* Clone() const = 0; /** Accept a hierchical visit the nodes in the TinyXML DOM. Every node in the XML tree will be conditionally visited and the host will be called back via the TiXmlVisitor interface. This is essentially a SAX interface for TinyXML. (Note however it doesn't re-parse the XML for the callbacks, so the performance of TinyXML is unchanged by using this interface versus any other.) The interface has been based on ideas from: - http://www.saxproject.org/ - http://c2.com/cgi/wiki?HierarchicalVisitorPattern Which are both good references for "visiting". An example of using Accept(): @verbatim TiXmlPrinter printer; tinyxmlDoc.Accept( &printer);
```
Returns true if this node has no children.

```cpp
virtual bool Accept(TiXmlVisitor* visitor ) const = 0; protected: TiXmlNode( NodeType _type);
```
```cpp
void CopyTo(TiXmlNode* target ) const; #ifdef TIXML_USE_STL // The real work of the input operator. virtual void StreamIn( std::istream* in, TIXML_STRING* tag ) = 0; #endif // Figure out what is at *p, and parse it. Returns null if it is not an xml node. TiXmlNode* Identify( const char* start, TiXmlEncoding encoding);
```
```cpp
const char*        Name() const { return name.c_str();
```
```cpp
const char*        Value() const { return value.c_str();
```
```cpp
const std::string& ValueStr() const { return value; } ///< Return the value of this attribute. #endif int IntValue() const; ///< Return the value of this attribute, converted to an integer. double DoubleValue() const; ///< Return the value of this attribute, converted to a double. // Get the tinyxml string representation const TIXML_STRING& NameTStr() const { return name; } /** QueryIntValue examines the value string. It is an alternative to the IntValue() method with richer error checking. If the value is an integer, it is stored in 'value' and the call returns TIXML_SUCCESS. If it is not an integer, it returns TIXML_WRONG_TYPE. A specialized but useful call. Note that for success it returns 0, which is the opposite of almost all other TinyXml calls. */ int QueryIntValue( int* _value ) const; /// QueryDoubleValue examines the value string. See QueryIntValue(). int QueryDoubleValue( double* _value ) const; void SetName( const char* _name ) { name = _name; } ///< Set the name of this attribute. void SetValue( const char* _value ) { value = _value; } ///< Set the value. void SetIntValue( int _value);
```
```cpp
void SetDoubleValue(double _value);
```
```cpp
void SetName(const std::string& _name ) { name = _name; } /// STL std::string form. void SetValue( const std::string& _value ) { value = _value; } #endif /// Get the next sibling attribute in the DOM. Returns null at end. const TiXmlAttribute* Next() const; TiXmlAttribute* Next() { return const_cast< TiXmlAttribute* >( (const_cast< const TiXmlAttribute* >(this))->Next());
```
STL std::string form.

```cpp
const TiXmlAttribute* Previous() const; TiXmlAttribute* Previous() { return const_cast< TiXmlAttribute* >( (const_cast< const TiXmlAttribute* >(this))->Previous());
```
Get the previous sibling attribute in the DOM. Returns null at beginning.

```cpp
virtual void Print(FILE* cfile, int depth ) const { Print( cfile, depth, 0);
```
```cpp
void Print(FILE* cfile, int depth, TIXML_STRING* str ) const; // [internal use] // Set the document pointer so the attribute can report errors. void SetDocument( TiXmlDocument* doc ) { document = doc; } private: TiXmlAttribute( const TiXmlAttribute&);
```
```cpp
which has to implement a next() and previous() method. Which makes it a bit problematic and prevents the use of STL. This version is implemented with circular lists because: - I like circular lists - it demonstrates some independence from the (typical) doubly linked list. */ class TiXmlAttributeSet { public: TiXmlAttributeSet();
```
```cpp
void Add(TiXmlAttribute* attribute);
```
```cpp
void Remove(TiXmlAttribute* attribute);
```
```cpp
const TiXmlAttribute* First() const { return ( sentinel.next == &sentinel ) ? 0 : sentinel.next; } TiXmlAttribute* First() { return ( sentinel.next == &sentinel ) ? 0 : sentinel.next; } const TiXmlAttribute* Last() const { return ( sentinel.prev == &sentinel ) ? 0 : sentinel.prev; } TiXmlAttribute* Last() { return ( sentinel.prev == &sentinel ) ? 0 : sentinel.prev; } TiXmlAttribute* Find( const char* _name ) const; TiXmlAttribute* FindOrCreate( const char* _name);
```
```cpp
TiXmlAttribute*    Find(const std::string& _name ) const; TiXmlAttribute* FindOrCreate( const std::string& _name);
```
```cpp
public:
    TiXmlElement(const std::string& _value);
```
```cpp
inline T readType(const std::string& str) const { T ret; int r = QueryValueAttribute(str, &ret);
```
```cpp
return T();
```
```cpp
int QueryValueAttribute(const std::string& name, T* outValue ) const { const TiXmlAttribute* node = attributeSet.Find( name);
```
```cpp
std::stringstream sstream(node->ValueStr());
```
```cpp
int QueryValueAttribute(const std::string& name, std::string* outValue ) const { const TiXmlAttribute* node = attributeSet.Find( name);
```
```cpp
std::string Attribute(const std::string& name ) const; std::string Attribute( const std::string& name, int* i ) const; std::string Attribute( const std::string& name, double* d ) const; void SetAttribute( const std::string& name, const std::string& _value);
```
```cpp
void SetAttribute(const std::string& name, int _value) { SetAttribute(name, stdext::to_string(_value));
```
```cpp
void RemoveAttribute(const std::string& name);
```
```cpp
const TiXmlAttribute* FirstAttribute() const { return attributeSet.First();
```
```cpp
TiXmlAttribute* FirstAttribute() { return attributeSet.First();
```
```cpp
const TiXmlAttribute* LastAttribute() const { return attributeSet.Last();
```
```cpp
TiXmlAttribute* LastAttribute() { return attributeSet.Last();
```
```cpp
WARNING: GetText() accesses a child node - don't become confused with the similarly named TiXmlHandle::Text() and TiXmlNode::ToText() which are safe type casts on the referenced node. */ const char* GetText() const; /// Creates a new Element and returns it - the returned element is a copy. virtual TiXmlNode* Clone() const; // Print the Element to a FILE stream. virtual void Print( FILE* cfile, int depth ) const; /* Attribtue parsing starts: next char past '<' returns: next char past '>' */ virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual const TiXmlElement*     ToElement() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type. virtual TiXmlElement* ToElement() { return this; } ///< Cast to a more defined type. Will return null not of the requested type. /** Walk the XML tree visiting this node and all of its children. */ virtual bool Accept( TiXmlVisitor* visitor ) const; protected: void CopyTo( TiXmlElement* target ) const; void ClearThis();
```
```cpp
virtual void StreamIn(std::istream * in, TIXML_STRING * tag);
```
```cpp
const char* ReadValue(const char* in, TiXmlParsingData* prevData, TiXmlEncoding encoding);
```
```cpp
virtual TiXmlNode* Clone() const; // Write this Comment to a FILE stream. virtual void Print( FILE* cfile, int depth ) const; /* Attribtue parsing starts: at the ! of the !-- returns: next char past '>' */ virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
Returns a copy of this Comment.

```cpp
virtual const TiXmlComment*  ToComment() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type. virtual TiXmlComment* ToComment() { return this; } ///< Cast to a more defined type. Will return null not of the requested type. /** Walk the XML tree visiting this node and all of its children. */ virtual bool Accept( TiXmlVisitor* visitor ) const; protected: void CopyTo( TiXmlComment* target ) const; // used to be public #ifdef TIXML_USE_STL virtual void StreamIn( std::istream * in, TIXML_STRING * tag);
```
```cpp
virtual void Print(FILE* cfile, int depth ) const; /// Queries whether this represents text using a CDATA section. bool CDATA() const { return cdata; } /// Turns on or off a CDATA representation of text. void SetCDATA( bool _cdata ) { cdata = _cdata; } virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual const TiXmlText* ToText() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type. virtual TiXmlText* ToText() { return this; } ///< Cast to a more defined type. Will return null not of the requested type. /** Walk the XML tree visiting this node and all of its children. */ virtual bool Accept( TiXmlVisitor* content ) const; protected : /// [internal use] Creates a new Element and returns it. virtual TiXmlNode* Clone() const; void CopyTo( TiXmlText* target ) const; bool Blank() const; // returns true if all white space and new lines // [internal use] #ifdef TIXML_USE_STL virtual void StreamIn( std::istream * in, TIXML_STRING * tag);
```
```cpp
virtual TiXmlNode* Clone() const; // Print this declaration to a FILE stream. virtual void Print( FILE* cfile, int depth, TIXML_STRING* str ) const; virtual void Print( FILE* cfile, int depth ) const { Print( cfile, depth, 0);
```
Creates a copy of this Declaration and returns it.

```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
```cpp
virtual const TiXmlDeclaration* ToDeclaration() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type. virtual TiXmlDeclaration* ToDeclaration() { return this; } ///< Cast to a more defined type. Will return null not of the requested type. /** Walk the XML tree visiting this node and all of its children. */ virtual bool Accept( TiXmlVisitor* visitor ) const; protected: void CopyTo( TiXmlDeclaration* target ) const; // used to be public #ifdef TIXML_USE_STL virtual void StreamIn( std::istream * in, TIXML_STRING * tag);
```
```cpp
public:
    TiXmlUnknown() : TiXmlNode( TiXmlNode::TINYXML_UNKNOWN ) {} virtual ~TiXmlUnknown() {} TiXmlUnknown( const TiXmlUnknown& copy ) : TiXmlNode( TiXmlNode::TINYXML_UNKNOWN ) { copy.CopyTo( this);
```
```cpp
virtual TiXmlNode* Clone() const; // Print this Unknown to a FILE stream. virtual void Print( FILE* cfile, int depth ) const; virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding);
```
Creates a copy of this Unknown and returns it.

```cpp
virtual const TiXmlUnknown*     ToUnknown() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type. virtual TiXmlUnknown* ToUnknown() { return this; } ///< Cast to a more defined type. Will return null not of the requested type. /** Walk the XML tree visiting this node and all of its children. */ virtual bool Accept( TiXmlVisitor* content ) const; protected: void CopyTo( TiXmlUnknown* target ) const; #ifdef TIXML_USE_STL virtual void StreamIn( std::istream * in, TIXML_STRING * tag);
```
```cpp
bool LoadFile(TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
```cpp
bool SaveFile() const; /// Load a file using the given filename. Returns true if successful. bool LoadFile( const char * filename, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
Save a file using the current document value. Returns true if successful.

```cpp
bool SaveFile(const char * filename ) const; /** Load a file using the given FILE*. Returns true if successful. Note that this method doesn't stream - the entire object pointed at by the FILE* will be interpreted as an XML file. TinyXML doesn't stream in XML from the current file location. Streaming may be added in the future. */ bool LoadFile( FILE*, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
Save a file using the given filename. Returns true if successful.

```cpp
bool SaveFile(FILE* ) const; #ifdef TIXML_USE_STL bool LoadFile( const std::string& filename, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING ) ///< STL std::string version. { return LoadFile( filename.c_str(), encoding);
```
Save a file using the given FILE*. Returns true if successful.

```cpp
bool SaveFile(const std::string& filename ) const ///< STL std::string version. { return SaveFile( filename.c_str());
```
```cpp
virtual const char* Parse(const char* p, TiXmlParsingData* data = 0, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING);
```
```cpp
const TiXmlElement* RootElement() const { return FirstChildElement();
```
```cpp
TiXmlElement* RootElement() { return FirstChildElement();
```
```cpp
bool Error() const { return error; } /// Contains a textual (english) description of the error if one occurs. const char * ErrorDesc() const { return errorDesc.c_str ();
```
```cpp
int ErrorId() const { return errorId; } /** Returns the location (if known) of the error. The first column is column 1, and the first row is row 1. A value of 0 means the row and column wasn't applicable (memory errors, for example, have no row/column) or the parser lost the error. (An error in the error reporting, in that case.) @sa SetTabSize, Row, Column */ int ErrorRow() const { return errorLocation.row+1; } int ErrorCol() const { return errorLocation.col+1; } ///< The column where the error occured. See ErrorRow() /** SetTabSize() allows the error reporting functions (ErrorRow() and ErrorCol()) to report the correct values for row and column. It does not change the output or input in any way. By calling this method, with a tab size greater than 0, the row and column of each node and attribute is stored when the file is loaded. Very useful for tracking the DOM back in to the source file. The tab size is required for calculating the location of nodes. If not set, the default of 4 is used. The tabsize is set per document. Setting the tabsize to 0 disables row/column tracking. Note that row and column tracking is not supported when using operator>>. The tab size needs to be enabled before the parse or load. Correct usage: @verbatim TiXmlDocument doc; doc.SetTabSize( 8);
```
```cpp
void SetTabSize(int _tabsize ) { tabsize = _tabsize; } int TabSize() const { return tabsize; } /** If you have handled the error, it can be reset with this call. The error state is automatically cleared if you Parse a new XML block. */ void ClearError() { error = false; errorId = 0; errorDesc = ""; errorLocation.row = errorLocation.col = 0; //errorLocation.last = 0; } /** Write the document to standard out using formatted printing ("pretty print"). */ void Print() const { Print( stdout, 0);
```
```cpp
will allocate a character array(new char[]) and return it as a pointer. The calling code pust call delete[] on the return char* to avoid a memory leak. */ //char* PrintToMemory() const; /// Print this Document to a FILE stream. virtual void Print( FILE* cfile, int depth = 0 ) const; // [internal use] void SetError( int err, const char* errorLocation, TiXmlParsingData* prevData, TiXmlEncoding encoding);
```
```cpp
virtual const TiXmlDocument*    ToDocument() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type. virtual TiXmlDocument* ToDocument() { return this; } ///< Cast to a more defined type. Will return null not of the requested type. /** Walk the XML tree visiting this node and all of its children. */ virtual bool Accept( TiXmlVisitor* content ) const; protected : // [internal use] virtual TiXmlNode* Clone() const; #ifdef TIXML_USE_STL virtual void StreamIn( std::istream * in, TIXML_STRING * tag);
```
```cpp
private:
    void CopyTo(TiXmlDocument* target ) const; bool error; int errorId; TIXML_STRING errorDesc; int tabsize; TiXmlCursor errorLocation; bool useMicrosoftBOM; // the UTF-8 BOM were found when read. Note this, and try to write. }; /** A TiXmlHandle is a class that wraps a node pointer with null checks; this is an incredibly useful thing. Note that TiXmlHandle is not part of the TinyXml DOM structure. It is a separate utility class. Take an example: @verbatim <Document> <Element attributeA = "valueA"> <Child attributeB = "value1" /> <Child attributeB = "value2" /> </Element> <Document> @endverbatim Assuming you want the value of "attributeB" in the 2nd "Child" element, it's very easy to write a *lot* of code that looks like: @verbatim TiXmlElement* root = document.FirstChildElement( "Document");
```
```cpp
TiXmlHandle docHandle(&document);
```
```cpp
TiXmlHandle FirstChild() const; /// Return a handle to the first child node with the given name. TiXmlHandle FirstChild( const char * value ) const; /// Return a handle to the first child element. TiXmlHandle FirstChildElement() const; /// Return a handle to the first child element with the given name. TiXmlHandle FirstChildElement( const char * value ) const; /** Return a handle to the "index" child with the given name. The first child is 0, the second 1, etc. */ TiXmlHandle Child( const char* value, int index ) const; /** Return a handle to the "index" child. The first child is 0, the second 1, etc. */ TiXmlHandle Child( int index ) const; /** Return a handle to the "index" child element with the given name. The first child element is 0, the second 1, etc. Note that only TiXmlElements are indexed: other types are not counted. */ TiXmlHandle ChildElement( const char* value, int index ) const; /** Return a handle to the "index" child element. The first child element is 0, the second 1, etc. Note that only TiXmlElements are indexed: other types are not counted. */ TiXmlHandle ChildElement( int index ) const; #ifdef TIXML_USE_STL TiXmlHandle FirstChild( const std::string& _value ) const { return FirstChild( _value.c_str());
```
Return a handle to the first child node.

```cpp
TiXmlHandle FirstChildElement(const std::string& _value ) const { return FirstChildElement( _value.c_str());
```
```cpp
TiXmlHandle Child(const std::string& _value, int index ) const { return Child( _value.c_str(), index);
```
```cpp
TiXmlHandle ChildElement(const std::string& _value, int index ) const { return ChildElement( _value.c_str(), index);
```
```cpp
TiXmlNode* ToNode() const { return node; } /** Return the handle as a TiXmlElement. This may return null. */ TiXmlElement* ToElement() const { return ( ( node && node->ToElement() ) ? node->ToElement() : 0);
```
Return the handle as a TiXmlNode. This may return null.

```cpp
TiXmlText* ToText() const { return ( ( node && node->ToText() ) ? node->ToText() : 0);
```
Return the handle as a TiXmlText. This may return null.

```cpp
TiXmlUnknown* ToUnknown() const { return ( ( node && node->ToUnknown() ) ? node->ToUnknown() : 0);
```
Return the handle as a TiXmlUnknown. This may return null.

```cpp
TiXmlNode* Node() const { return ToNode();
```
```cpp
TiXmlElement* Element() const { return ToElement();
```
```cpp
TiXmlText* Text() const { return ToText();
```
```cpp
TiXmlUnknown* Unknown() const { return ToUnknown();
```
```cpp
Before calling Accept() you can call methods to control the printing of the XML document. After TiXmlNode::Accept() is called, the printed document can be accessed via the CStr(), Str(), and Size() methods. TiXmlPrinter uses the Visitor API. @verbatim TiXmlPrinter printer; printer.SetIndent( "\t");
```
```cpp
public:
    TiXmlPrinter() : depth( 0 ), simpleTextPrint( false ), buffer(), indent( " " ), lineBreak( "\n" ) {} virtual bool VisitEnter( const TiXmlDocument& doc);
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
but tab(\t) is also useful, or null/empty string for no indentation. */ void SetIndent( const char* _indent ) { indent = _indent ? _indent : "" ; } /// Query the indention string. const char* Indent() { return indent.c_str();
```
Set the indent characters for printing. By default 4 spaces

```cpp
void SetLineBreak(const char* _lineBreak ) { lineBreak = _lineBreak ? _lineBreak : ""; } /// Query the current line breaking string. const char* LineBreak() { return lineBreak.c_str();
```
```cpp
void SetStreamPrinting() { indent = ""; lineBreak = ""; } /// Return the result. const char* CStr() { return buffer.c_str();
```
```cpp
size_t Size() { return buffer.size();
```
Return the length of the result string.

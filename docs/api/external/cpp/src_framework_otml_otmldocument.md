# src/framework/otml/otmldocument.h

```cpp
static OTMLDocumentPtr create();
```
Create a new OTML document for filling it with nodes

```cpp
static OTMLDocumentPtr parse(const std::string& fileName);
```
Parse OTML from a file

```cpp
static OTMLDocumentPtr parseString(const std::string& data, const std::string& source);
```
Parse OTML from a string

```cpp
static OTMLDocumentPtr parse(std::istream& in, const std::string& source);
```
Parse OTML from input stream
@param source is the file name that will be used to show errors messages

```cpp
std::string emit();
```
Emits this document and all it's children to a std::string

```cpp
bool save(const std::string& fileName);
```
Save this document to a file

```cpp
private: OTMLDocument();
```
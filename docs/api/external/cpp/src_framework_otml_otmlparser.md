# src/framework/otml/otmlparser.h

```cpp
public:
    OTMLParser(OTMLDocumentPtr doc, std::istream& in);
```
```cpp
void parse();
```
Parse the entire document

```cpp
std::string getNextLine();
```
Retrieve next line from the input stream

```cpp
int getLineDepth(const std::string& line, bool multilining = false);
```
Counts depth of a line (every 2 spaces increments one depth)

```cpp
void parseLine(std::string line);
```
Parse each line of the input stream

```cpp
void parseNode(const std::string& data);
```
Parse nodes tag and value

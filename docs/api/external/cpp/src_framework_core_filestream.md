# src/framework/core/filestream.h

```cpp
public:
    FileStream(const std::string& name, PHYSFS_File *fileHandle, bool writeable);
```
```cpp
void close();
```
```cpp
void flush();
```
```cpp
void write(const void *buffer, uint count);
```
```cpp
int read(void *buffer, uint size, uint nmemb = 1);
```
```cpp
void seek(uint pos);
```
```cpp
void skip(uint len);
```
```cpp
uint size();
```
```cpp
uint tell();
```
```cpp
bool eof();
```
```cpp
std::string name() { return m_name; } uint8 getU8();
```
```cpp
uint16 getU16();
```
```cpp
uint32 getU32();
```
```cpp
uint64 getU64();
```
```cpp
int8 get8();
```
```cpp
int16 get16();
```
```cpp
int32 get32();
```
```cpp
int64 get64();
```
```cpp
std::string getString();
```
```cpp
BinaryTreePtr getBinaryTree();
```
```cpp
void startNode(uint8 n);
```
```cpp
void endNode();
```
```cpp
void addU8(uint8 v);
```
```cpp
void addU16(uint16 v);
```
```cpp
void addU32(uint32 v);
```
```cpp
void addU64(uint64 v);
```
```cpp
void add8(int8 v);
```
```cpp
void add16(int16 v);
```
```cpp
void add32(int32 v);
```
```cpp
void add64(int64 v);
```
```cpp
void addString(const std::string& v);
```
```cpp
void addPos(uint16 x, uint16 y, uint8 z) { addU16(x);
```
```cpp
void addPoint(const Point& p) { addU8(p.x);
```
```cpp
FileStreamPtr asFileStream() { return static_self_cast<FileStream>();
```
```cpp
private:
    bool initFromGzip(const std::string& buffer);
```
```cpp
void checkWrite();
```
```cpp
void throwError(const std::string& message, bool physfsError = false);
```
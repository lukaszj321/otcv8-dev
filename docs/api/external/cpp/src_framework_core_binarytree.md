# src/framework/core/binarytree.h

```cpp
public:
    BinaryTree(const FileStreamPtr& fin);
```
```cpp
void seek(uint pos);
```
```cpp
void skip(uint len);
```
```cpp
uint tell() { return m_pos; } uint size() { unserialize();
```
```cpp
uint8 getU8();
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
std::string getString(uint16 len = 0);
```
```cpp
Point getPoint();
```
```cpp
BinaryTreeVec getChildren();
```
```cpp
bool canRead() { unserialize();
```
```cpp
private:
    void unserialize();
```
```cpp
void skipNodes();
```
```cpp
public:
    OutputBinaryTree(const FileStreamPtr& finish);
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
void addString(const std::string& v);
```
```cpp
void addPos(uint16 x, uint16 y, uint8 z);
```
```cpp
void addPoint(const Point& point);
```
```cpp
void startNode(uint8 node);
```
```cpp
void endNode();
```
```cpp
protected:
    void write(const uint8* data, size_t size);
```
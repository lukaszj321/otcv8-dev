# src/framework/net/inputmessage.h

```cpp
void setBuffer(const std::string& buffer);
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
std::string getString();
```
```cpp
double getDouble();
```
```cpp
bool decryptRsa(int size);
```
```cpp
protected: void reset();
```
```cpp
void fillBuffer(uint8 *buffer, uint32 size);
```
```cpp
void setHeaderSize(uint32 size);
```
```cpp
bool readChecksum();
```
```cpp
void addZlibFooter();
```
```cpp
private: bool canRead(int bytes);
```
```cpp
void checkRead(int bytes);
```
```cpp
void checkWrite(int bytes);
```
```cpp
std::string getBuffer();
```
```cpp
std::string getBodyBuffer();
```
```cpp
void skipBytes(uint32 bytes);
```
```cpp
void setReadPos(uint32 readPos);
```
```cpp
uint8 peekU8();
```
```cpp
uint16 peekU16();
```
```cpp
uint32 peekU32();
```
```cpp
uint64 peekU64();
```
```cpp
uint32 getHeaderPos();
```
```cpp
uint32 getHeaderSize();
```
```cpp
int getReadSize();
```
```cpp
int getReadPos();
```
```cpp
int getUnreadSize();
```
```cpp
uint32 getMessageSize();
```
```cpp
bool eof();
```
```cpp
void setMessageSize(uint32 size);
```
```cpp
uint8* getReadBuffer();
```
```cpp
uint8* getHeaderBuffer();
```
```cpp
uint8* getDataBuffer();
```
```cpp
uint32 readSize(bool bigSize);
```
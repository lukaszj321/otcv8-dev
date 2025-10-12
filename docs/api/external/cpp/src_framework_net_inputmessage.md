# src/framework/net/inputmessage.h

```cpp
void setBuffer(const std::string& buffer);
```
```cpp
std::string getBuffer() { return std::string((char*)m_buffer + m_headerPos, m_messageSize);
```
```cpp
std::string getBodyBuffer() { return std::string((char*)m_buffer + MAX_HEADER_SIZE, m_messageSize - getHeaderSize());
```
```cpp
void skipBytes(uint32 bytes) { m_readPos += bytes; } void setReadPos(uint32 readPos) { m_readPos = readPos; } uint8 getU8();
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
uint8 peekU8() { uint8 v = getU8();
```
```cpp
uint16 peekU16() { uint16 v = getU16();
```
```cpp
uint32 peekU32() { uint32 v = getU32();
```
```cpp
uint64 peekU64() { uint64 v = getU64();
```
```cpp
bool decryptRsa(int size);
```
```cpp
uint32 getHeaderPos() { return m_headerPos; } uint32 getHeaderSize() { return (MAX_HEADER_SIZE - m_headerPos);
```
```cpp
int getReadSize() { return m_readPos - m_headerPos; } int getReadPos() { return m_readPos; } int getUnreadSize() { return m_messageSize - (m_readPos - m_headerPos);
```
```cpp
uint32 getMessageSize() { return m_messageSize; } bool eof() { return (m_readPos - m_headerPos) >= m_messageSize; } protected: void reset();
```
```cpp
void fillBuffer(uint8 *buffer, uint32 size);
```
```cpp
void setHeaderSize(uint32 size);
```
```cpp
void setMessageSize(uint32 size) { m_messageSize = size; } uint8* getReadBuffer() { return m_buffer + m_readPos; } uint8* getHeaderBuffer() { return m_buffer + m_headerPos; } uint8* getDataBuffer() { return m_buffer + MAX_HEADER_SIZE; } uint32 readSize(bool bigSize) { return bigSize ? getU32() : getU16();
```
```cpp
bool readChecksum();
```
```cpp
void addZlibFooter();
```
```cpp
private:
    bool canRead(int bytes);
```
```cpp
void checkRead(int bytes);
```
```cpp
void checkWrite(int bytes);
```
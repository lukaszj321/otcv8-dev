# src/framework/net/outputmessage.h

```cpp
void reset();
```
```cpp
void setBuffer(const std::string& buffer);
```
```cpp
std::string getBuffer() { return std::string((char*)m_buffer + m_headerPos, m_messageSize);
```
```cpp
void addU8(uint8 value);
```
```cpp
void addU16(uint16 value);
```
```cpp
void addU32(uint32 value);
```
```cpp
void addU64(uint64 value);
```
```cpp
void addString(const std::string& buffer);
```
```cpp
void addRawString(const std::string& buffer);
```
```cpp
void addPaddingBytes(int bytes, uint8 byte = 0);
```
```cpp
void encryptRsa();
```
```cpp
uint32 getWritePos() { return m_writePos; } uint32 getMessageSize() { return m_messageSize; } void setWritePos(uint32 writePos) { m_writePos = writePos; } void setMessageSize(uint32 messageSize) { m_messageSize = messageSize; } protected: uint8* getWriteBuffer() { return m_buffer + m_writePos; } uint8* getHeaderBuffer() { return m_buffer + m_headerPos; } uint8* getDataBuffer() { return m_buffer + MAX_HEADER_SIZE; } void writeChecksum();
```
```cpp
void writeSequence(uint32_t sequence);
```
```cpp
void writeMessageSize(bool bigSize);
```
```cpp
private:
    bool canWrite(int bytes);
```
```cpp
void checkWrite(int bytes);
```
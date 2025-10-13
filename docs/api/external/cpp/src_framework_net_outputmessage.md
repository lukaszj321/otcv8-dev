# src/framework/net/outputmessage.h

```cpp
void reset();
```
```cpp
void setBuffer(const std::string& buffer);
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
void writeChecksum();
```
```cpp
void writeSequence(uint32_t sequence);
```
```cpp
void writeMessageSize(bool bigSize);
```
```cpp
private: bool canWrite(int bytes);
```
```cpp
void checkWrite(int bytes);
```
```cpp
std::string getBuffer();
```
```cpp
uint32 getWritePos();
```
```cpp
uint32 getMessageSize();
```
```cpp
void setWritePos(uint32 writePos);
```
```cpp
void setMessageSize(uint32 messageSize);
```
```cpp
protected: uint8* getWriteBuffer();
```
```cpp
uint8* getHeaderBuffer();
```
```cpp
uint8* getDataBuffer();
```
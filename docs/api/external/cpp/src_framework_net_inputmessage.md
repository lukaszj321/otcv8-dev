---
title: "src/framework/net/inputmessage.h"
source_file: "src/framework/net/inputmessage.h"
generated_at: "2025-11-01T00:11:49.051Z"
doc_type: "cpp_api"
---

# src/framework/net/inputmessage.h

(setbuffer)=
## `setBuffer`

**Signature:**
```cpp
void setBuffer(const std::string& buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |

---

(getu8)=
## `getU8`

**Signature:**
```cpp
uint8 getU8();
```

**Returns:**
- `uint8`

---

(getu16)=
## `getU16`

**Signature:**
```cpp
uint16 getU16();
```

**Returns:**
- `uint16`

---

(getu32)=
## `getU32`

**Signature:**
```cpp
uint32 getU32();
```

**Returns:**
- `uint32`

---

(getu64)=
## `getU64`

**Signature:**
```cpp
uint64 getU64();
```

**Returns:**
- `uint64`

---

(getstring)=
## `getString`

**Signature:**
```cpp
std::string getString();
```

**Returns:**
- `std::string`

---

(getdouble)=
## `getDouble`

**Signature:**
```cpp
double getDouble();
```

**Returns:**
- `double`

---

(decryptrsa)=
## `decryptRsa`

**Signature:**
```cpp
bool decryptRsa(int size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `size` | - |

**Returns:**
- `bool`

---

(reset)=
## `reset`

**Signature:**
```cpp
protected: void reset();
```

---

(fillbuffer)=
## `fillBuffer`

**Signature:**
```cpp
void fillBuffer(uint8 *buffer, uint32 size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8 *buffer` | - | - |
| `uint32` | `size` | - |

---

(setheadersize)=
## `setHeaderSize`

**Signature:**
```cpp
void setHeaderSize(uint32 size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `size` | - |

---

(readchecksum)=
## `readChecksum`

**Signature:**
```cpp
bool readChecksum();
```

**Returns:**
- `bool`

---

(addzlibfooter)=
## `addZlibFooter`

**Signature:**
```cpp
void addZlibFooter();
```

---

(canread)=
## `canRead`

**Signature:**
```cpp
private: bool canRead(int bytes);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `bytes` | - |

**Returns:**
- `bool`

---

(checkread)=
## `checkRead`

**Signature:**
```cpp
void checkRead(int bytes);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `bytes` | - |

---

(checkwrite)=
## `checkWrite`

**Signature:**
```cpp
void checkWrite(int bytes);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `bytes` | - |

---

(getbuffer)=
## `getBuffer`

**Signature:**
```cpp
std::string getBuffer();
```

**Returns:**
- `std::string`

---

(getbodybuffer)=
## `getBodyBuffer`

**Signature:**
```cpp
std::string getBodyBuffer();
```

**Returns:**
- `std::string`

---

(skipbytes)=
## `skipBytes`

**Signature:**
```cpp
void skipBytes(uint32 bytes);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `bytes` | - |

---

(setreadpos)=
## `setReadPos`

**Signature:**
```cpp
void setReadPos(uint32 readPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `readPos` | - |

---

(peeku8)=
## `peekU8`

**Signature:**
```cpp
uint8 peekU8();
```

**Returns:**
- `uint8`

---

(peeku16)=
## `peekU16`

**Signature:**
```cpp
uint16 peekU16();
```

**Returns:**
- `uint16`

---

(peeku32)=
## `peekU32`

**Signature:**
```cpp
uint32 peekU32();
```

**Returns:**
- `uint32`

---

(peeku64)=
## `peekU64`

**Signature:**
```cpp
uint64 peekU64();
```

**Returns:**
- `uint64`

---

(getheaderpos)=
## `getHeaderPos`

**Signature:**
```cpp
uint32 getHeaderPos();
```

**Returns:**
- `uint32`

---

(getheadersize)=
## `getHeaderSize`

**Signature:**
```cpp
uint32 getHeaderSize();
```

**Returns:**
- `uint32`

---

(getreadsize)=
## `getReadSize`

**Signature:**
```cpp
int getReadSize();
```

**Returns:**
- `int`

---

(getreadpos)=
## `getReadPos`

**Signature:**
```cpp
int getReadPos();
```

**Returns:**
- `int`

---

(getunreadsize)=
## `getUnreadSize`

**Signature:**
```cpp
int getUnreadSize();
```

**Returns:**
- `int`

---

(getmessagesize)=
## `getMessageSize`

**Signature:**
```cpp
uint32 getMessageSize();
```

**Returns:**
- `uint32`

---

(eof)=
## `eof`

**Signature:**
```cpp
bool eof();
```

**Returns:**
- `bool`

---

(setmessagesize)=
## `setMessageSize`

**Signature:**
```cpp
void setMessageSize(uint32 size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `size` | - |

---

(getreadbuffer)=
## `getReadBuffer`

**Signature:**
```cpp
uint8* getReadBuffer();
```

**Returns:**
- `uint8*`

---

(getheaderbuffer)=
## `getHeaderBuffer`

**Signature:**
```cpp
uint8* getHeaderBuffer();
```

**Returns:**
- `uint8*`

---

(getdatabuffer)=
## `getDataBuffer`

**Signature:**
```cpp
uint8* getDataBuffer();
```

**Returns:**
- `uint8*`

---

(readsize)=
## `readSize`

**Signature:**
```cpp
uint32 readSize(bool bigSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `bigSize` | - |

**Returns:**
- `uint32`

---

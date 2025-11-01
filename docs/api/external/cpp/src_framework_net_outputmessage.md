---
title: "src/framework/net/outputmessage.h"
source_file: "src/framework/net/outputmessage.h"
generated_at: "2025-11-01T08:19:49.455Z"
doc_type: "cpp_api"
---

# src/framework/net/outputmessage.h

(reset)=
## `reset`

**Signature:**
```cpp
void reset();
```

---

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

(addu8)=
## `addU8`

**Signature:**
```cpp
void addU8(uint8 value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `value` | - |

---

(addu16)=
## `addU16`

**Signature:**
```cpp
void addU16(uint16 value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `value` | - |

---

(addu32)=
## `addU32`

**Signature:**
```cpp
void addU32(uint32 value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `value` | - |

---

(addu64)=
## `addU64`

**Signature:**
```cpp
void addU64(uint64 value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint64` | `value` | - |

---

(addstring)=
## `addString`

**Signature:**
```cpp
void addString(const std::string& buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |

---

(addrawstring)=
## `addRawString`

**Signature:**
```cpp
void addRawString(const std::string& buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |

---

(addpaddingbytes)=
## `addPaddingBytes`

**Signature:**
```cpp
void addPaddingBytes(int bytes, uint8 byte = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `bytes` |  | - |
| `uint8` | `byte` | `0` | - |

---

(encryptrsa)=
## `encryptRsa`

**Signature:**
```cpp
void encryptRsa();
```

---

(writechecksum)=
## `writeChecksum`

**Signature:**
```cpp
void writeChecksum();
```

---

(writesequence)=
## `writeSequence`

**Signature:**
```cpp
void writeSequence(uint32_t sequence);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `sequence` | - |

---

(writemessagesize)=
## `writeMessageSize`

**Signature:**
```cpp
void writeMessageSize(bool bigSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `bigSize` | - |

---

(canwrite)=
## `canWrite`

**Signature:**
```cpp
private: bool canWrite(int bytes);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `bytes` | - |

**Returns:**
- `bool`

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

(getwritepos)=
## `getWritePos`

**Signature:**
```cpp
uint32 getWritePos();
```

**Returns:**
- `uint32`

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

(setwritepos)=
## `setWritePos`

**Signature:**
```cpp
void setWritePos(uint32 writePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `writePos` | - |

---

(setmessagesize)=
## `setMessageSize`

**Signature:**
```cpp
void setMessageSize(uint32 messageSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `messageSize` | - |

---

(getwritebuffer)=
## `getWriteBuffer`

**Signature:**
```cpp
protected: uint8* getWriteBuffer();
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

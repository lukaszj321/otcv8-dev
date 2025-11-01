---
title: "src/framework/core/filestream.h"
source_file: "src/framework/core/filestream.h"
generated_at: "2025-11-01T08:19:49.435Z"
doc_type: "cpp_api"
---

# src/framework/core/filestream.h

(filestream)=
## `FileStream`

**Signature:**
```cpp
public: FileStream(const std::string& name, PHYSFS_File *fileHandle, bool writeable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `PHYSFS_File *fileHandle` | - | - |
| `bool` | `writeable` | - |

---

(close)=
## `close`

**Signature:**
```cpp
void close();
```

---

(flush)=
## `flush`

**Signature:**
```cpp
void flush();
```

---

(write)=
## `write`

**Signature:**
```cpp
void write(const void *buffer, uint count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const void *buffer` | - | - |
| `uint` | `count` | - |

---

(read)=
## `read`

**Signature:**
```cpp
int read(void *buffer, uint size, uint nmemb = 1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `void *buffer` | - |  | - |
| `uint` | `size` |  | - |
| `uint` | `nmemb` | `1` | - |

**Returns:**
- `int`

---

(seek)=
## `seek`

**Signature:**
```cpp
void seek(uint pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `pos` | - |

---

(skip)=
## `skip`

**Signature:**
```cpp
void skip(uint len);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `len` | - |

---

(size)=
## `size`

**Signature:**
```cpp
uint size();
```

**Returns:**
- `uint`

---

(tell)=
## `tell`

**Signature:**
```cpp
uint tell();
```

**Returns:**
- `uint`

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

(get8)=
## `get8`

**Signature:**
```cpp
int8 get8();
```

**Returns:**
- `int8`

---

(get16)=
## `get16`

**Signature:**
```cpp
int16 get16();
```

**Returns:**
- `int16`

---

(get32)=
## `get32`

**Signature:**
```cpp
int32 get32();
```

**Returns:**
- `int32`

---

(get64)=
## `get64`

**Signature:**
```cpp
int64 get64();
```

**Returns:**
- `int64`

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

(getbinarytree)=
## `getBinaryTree`

**Signature:**
```cpp
BinaryTreePtr getBinaryTree();
```

**Returns:**
- `BinaryTreePtr`

---

(startnode)=
## `startNode`

**Signature:**
```cpp
void startNode(uint8 n);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `n` | - |

---

(endnode)=
## `endNode`

**Signature:**
```cpp
void endNode();
```

---

(addu8)=
## `addU8`

**Signature:**
```cpp
void addU8(uint8 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `v` | - |

---

(addu16)=
## `addU16`

**Signature:**
```cpp
void addU16(uint16 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `v` | - |

---

(addu32)=
## `addU32`

**Signature:**
```cpp
void addU32(uint32 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `v` | - |

---

(addu64)=
## `addU64`

**Signature:**
```cpp
void addU64(uint64 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint64` | `v` | - |

---

(add8)=
## `add8`

**Signature:**
```cpp
void add8(int8 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int8` | `v` | - |

---

(add16)=
## `add16`

**Signature:**
```cpp
void add16(int16 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int16` | `v` | - |

---

(add32)=
## `add32`

**Signature:**
```cpp
void add32(int32 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int32` | `v` | - |

---

(add64)=
## `add64`

**Signature:**
```cpp
void add64(int64 v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int64` | `v` | - |

---

(addstring)=
## `addString`

**Signature:**
```cpp
void addString(const std::string& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `v` | - |

---

(initfromgzip)=
## `initFromGzip`

**Signature:**
```cpp
private: bool initFromGzip(const std::string& buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |

**Returns:**
- `bool`

---

(checkwrite)=
## `checkWrite`

**Signature:**
```cpp
void checkWrite();
```

---

(throwerror)=
## `throwError`

**Signature:**
```cpp
void throwError(const std::string& message, bool physfsError = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `message` |  | - |
| `bool` | `physfsError` | `false` | - |

---

(name)=
## `name`

**Signature:**
```cpp
std::string name();
```

**Returns:**
- `std::string`

---

(addpos)=
## `addPos`

**Signature:**
```cpp
void addPos(uint16 x, uint16 y, uint8 z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `x` | - |
| `uint16` | `y` | - |
| `uint8` | `z` | - |

---

(addpoint)=
## `addPoint`

**Signature:**
```cpp
void addPoint(const Point& p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `p` | - |

---

(asfilestream)=
## `asFileStream`

**Signature:**
```cpp
FileStreamPtr asFileStream();
```

**Returns:**
- `FileStreamPtr`

---

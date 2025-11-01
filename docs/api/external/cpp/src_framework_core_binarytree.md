---
title: "src/framework/core/binarytree.h"
source_file: "src/framework/core/binarytree.h"
generated_at: "2025-11-01T08:45:15.294Z"
doc_type: "cpp_api"
---

# src/framework/core/binarytree.h

(binarytree)=
## `BinaryTree`

**Signature:**
```cpp
public: BinaryTree(const FileStreamPtr& fin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FileStreamPtr&` | `fin` | - |

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
std::string getString(uint16 len = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `uint16` | `len` | `0` | - |

**Returns:**
- `std::string`

---

(getpoint)=
## `getPoint`

**Signature:**
```cpp
Point getPoint();
```

**Returns:**
- `Point`

---

(getchildren)=
## `getChildren`

**Signature:**
```cpp
BinaryTreeVec getChildren();
```

**Returns:**
- `BinaryTreeVec`

---

(unserialize)=
## `unserialize`

**Signature:**
```cpp
private: void unserialize();
```

---

(skipnodes)=
## `skipNodes`

**Signature:**
```cpp
void skipNodes();
```

---

(outputbinarytree)=
## `OutputBinaryTree`

**Signature:**
```cpp
public: OutputBinaryTree(const FileStreamPtr& finish);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FileStreamPtr&` | `finish` | - |

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
void addPoint(const Point& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |

---

(startnode)=
## `startNode`

**Signature:**
```cpp
void startNode(uint8 node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `node` | - |

---

(endnode)=
## `endNode`

**Signature:**
```cpp
void endNode();
```

---

(write)=
## `write`

**Signature:**
```cpp
protected: void write(const uint8* data, size_t size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uint8*` | `data` | - |
| `size_t` | `size` | - |

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

(size)=
## `size`

**Signature:**
```cpp
uint size();
```

**Returns:**
- `uint`

---

(canread)=
## `canRead`

**Signature:**
```cpp
bool canRead();
```

**Returns:**
- `bool`


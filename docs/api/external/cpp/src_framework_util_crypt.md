---
title: "src/framework/util/crypt.h"
source_file: "src/framework/util/crypt.h"
generated_at: "2025-11-01T08:45:15.328Z"
doc_type: "cpp_api"
---

# src/framework/util/crypt.h

(crypt)=
## `Crypt`

**Signature:**
```cpp
public: Crypt();
```

---

(base64encode)=
## `base64Encode`

**Signature:**
```cpp
std::string base64Encode(const std::string& decoded_string);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decoded_string` | - |

**Returns:**
- `std::string`

---

(base64decode)=
## `base64Decode`

**Signature:**
```cpp
std::string base64Decode(const std::string& encoded_string);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `encoded_string` | - |

**Returns:**
- `std::string`

---

(xorcrypt)=
## `xorCrypt`

**Signature:**
```cpp
std::string xorCrypt(const std::string& buffer, const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |
| `const std::string&` | `key` | - |

**Returns:**
- `std::string`

---

(genuuid)=
## `genUUID`

**Signature:**
```cpp
std::string genUUID();
```

**Returns:**
- `std::string`

---

(setmachineuuid)=
## `setMachineUUID`

**Signature:**
```cpp
bool setMachineUUID(std::string uuidstr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `uuidstr` | - |

**Returns:**
- `bool`

---

(getmachineuuid)=
## `getMachineUUID`

**Signature:**
```cpp
std::string getMachineUUID();
```

**Returns:**
- `std::string`

---

(md5encode)=
## `md5Encode`

**Signature:**
```cpp
std::string md5Encode(const std::string& decoded_string, bool upperCase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decoded_string` | - |
| `bool` | `upperCase` | - |

**Returns:**
- `std::string`

---

(sha1encode)=
## `sha1Encode`

**Signature:**
```cpp
std::string sha1Encode(const std::string& decoded_string, bool upperCase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decoded_string` | - |
| `bool` | `upperCase` | - |

**Returns:**
- `std::string`

---

(sha256encode)=
## `sha256Encode`

**Signature:**
```cpp
std::string sha256Encode(const std::string& decoded_string, bool upperCase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decoded_string` | - |
| `bool` | `upperCase` | - |

**Returns:**
- `std::string`

---

(sha512encode)=
## `sha512Encode`

**Signature:**
```cpp
std::string sha512Encode(const std::string& decoded_string, bool upperCase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decoded_string` | - |
| `bool` | `upperCase` | - |

**Returns:**
- `std::string`

---

(crc32)=
## `crc32`

**Signature:**
```cpp
std::string crc32(const std::string& decoded_string, bool upperCase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decoded_string` | - |
| `bool` | `upperCase` | - |

**Returns:**
- `std::string`

---

(rsageneratekey)=
## `rsaGenerateKey`

**Signature:**
```cpp
void rsaGenerateKey(int bits, int e);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `bits` | - |
| `int` | `e` | - |

---

(rsasetpublickey)=
## `rsaSetPublicKey`

**Signature:**
```cpp
void rsaSetPublicKey(const std::string& n, const std::string& e);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `n` | - |
| `const std::string&` | `e` | - |

---

(rsasetprivatekey)=
## `rsaSetPrivateKey`

**Signature:**
```cpp
void rsaSetPrivateKey(const std::string &p, const std::string &q, const std::string &d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string &p` | - | - |
| `const std::string &q` | - | - |
| `const std::string &d` | - | - |

---

(rsacheckkey)=
## `rsaCheckKey`

**Signature:**
```cpp
bool rsaCheckKey();
```

**Returns:**
- `bool`

---

(rsaencrypt)=
## `rsaEncrypt`

**Signature:**
```cpp
bool rsaEncrypt(unsigned char *msg, int size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `unsigned char *msg` | - | - |
| `int` | `size` | - |

**Returns:**
- `bool`

---

(rsadecrypt)=
## `rsaDecrypt`

**Signature:**
```cpp
bool rsaDecrypt(unsigned char *msg, int size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `unsigned char *msg` | - | - |
| `int` | `size` | - |

**Returns:**
- `bool`

---

(rsagetsize)=
## `rsaGetSize`

**Signature:**
```cpp
int rsaGetSize();
```

**Returns:**
- `int`

---

(bencrypt)=
## `bencrypt`

**Signature:**
```cpp
void bencrypt(uint8_t * buffer, int len, uint64_t k);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t *` | `buffer` | - |
| `int` | `len` | - |
| `uint64_t` | `k` | - |

---

(bdecrypt)=
## `bdecrypt`

**Signature:**
```cpp
void bdecrypt(uint8_t * buffer, int len, uint64_t k);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t *` | `buffer` | - |
| `int` | `len` | - |
| `uint64_t` | `k` | - |

---

(_encrypt)=
## `_encrypt`

**Signature:**
```cpp
private: std::string _encrypt(const std::string& decrypted_string, bool useMachineUUID);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decrypted_string` | - |
| `bool` | `useMachineUUID` | - |

**Returns:**
- `std::string`

---

(_decrypt)=
## `_decrypt`

**Signature:**
```cpp
std::string _decrypt(const std::string& encrypted_string, bool useMachineUUID);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `encrypted_string` | - |
| `bool` | `useMachineUUID` | - |

**Returns:**
- `std::string`

---

(getcryptkey)=
## `getCryptKey`

**Signature:**
```cpp
std::string getCryptKey(bool useMachineUUID);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `useMachineUUID` | - |

**Returns:**
- `std::string`

---

(encrypt)=
## `encrypt`

**Signature:**
```cpp
std::string encrypt(const std::string& decrypted_string);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `decrypted_string` | - |

**Returns:**
- `std::string`

---

(decrypt)=
## `decrypt`

**Signature:**
```cpp
std::string decrypt(const std::string& encrypted_string);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `encrypted_string` | - |

**Returns:**
- `std::string`

---

---
title: "src/framework/stdext/net.h"
source_file: "src/framework/stdext/net.h"
generated_at: "2025-11-01T08:19:49.468Z"
doc_type: "cpp_api"
---

# src/framework/stdext/net.h

(ip_to_string)=
## `ip_to_string`

**Signature:**
```cpp
std::string ip_to_string(uint32 ip);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `ip` | - |

**Returns:**
- `std::string`

---

(string_to_ip)=
## `string_to_ip`

**Signature:**
```cpp
uint32 string_to_ip(const std::string& string);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `string` | - |

**Returns:**
- `uint32`

---

(listsubnetaddresses)=
## `listSubnetAddresses`

**Signature:**
```cpp
std::vector<uint32> listSubnetAddresses(uint32 address, uint8 mask);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `address` | - |
| `uint8` | `mask` | - |

**Returns:**
- `std::vector&lt;uint32&gt;`

---

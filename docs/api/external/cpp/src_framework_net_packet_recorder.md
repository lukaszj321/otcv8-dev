---
title: "src/framework/net/packet_recorder.h"
source_file: "src/framework/net/packet_recorder.h"
generated_at: "2025-11-01T08:29:23.712Z"
doc_type: "cpp_api"
---

# src/framework/net/packet_recorder.h

(packetrecorder)=
## `PacketRecorder`

**Signature:**
```cpp
public: PacketRecorder(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(addinputpacket)=
## `addInputPacket`

**Signature:**
```cpp
void addInputPacket(const InputMessagePtr& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `packet` | - |

---

(addoutputpacket)=
## `addOutputPacket`

**Signature:**
```cpp
void addOutputPacket(const OutputMessagePtr& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OutputMessagePtr&` | `packet` | - |

---

---
title: "src/framework/net/packet_player.h"
source_file: "src/framework/net/packet_player.h"
generated_at: "2025-11-01T04:06:42.761Z"
doc_type: "cpp_api"
---

# src/framework/net/packet_player.h

(packetplayer)=
## `PacketPlayer`

**Signature:**
```cpp
public: PacketPlayer(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(start)=
## `start`

**Signature:**
```cpp
void start(std::function<void(std::shared_ptr<std::vector<uint8_t>>)> recvCallback, std::function<void(boost::system::error_code)> disconnectCallback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::function&lt;void(std::shared_ptr&lt;std::vector&lt;uint8_t&gt;&gt;)&gt;` | `recvCallback` | - |
| `std::function&lt;void(boost::system::error_code)&gt;` | `disconnectCallback` | - |

---

(stop)=
## `stop`

**Signature:**
```cpp
void stop();
```

---

(onoutputpacket)=
## `onOutputPacket`

**Signature:**
```cpp
void onOutputPacket(const OutputMessagePtr& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OutputMessagePtr&` | `packet` | - |

---

(process)=
## `process`

**Signature:**
```cpp
private: void process();
```

---

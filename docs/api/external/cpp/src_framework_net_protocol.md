---
title: "src/framework/net/protocol.h"
source_file: "src/framework/net/protocol.h"
generated_at: "2025-11-01T08:19:49.456Z"
doc_type: "cpp_api"
---

# src/framework/net/protocol.h

(protocol)=
## `Protocol`

**Signature:**
```cpp
public: Protocol();
```

---

(connect)=
## `connect`

**Signature:**
```cpp
void connect(const std::string& host, uint16 port);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `host` | - |
| `uint16` | `port` | - |

---

(disconnect)=
## `disconnect`

**Signature:**
```cpp
void disconnect();
```

---

(setrecorder)=
## `setRecorder`

**Signature:**
```cpp
void setRecorder(PacketRecorderPtr recorder);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `PacketRecorderPtr` | `recorder` | - |

---

(playrecord)=
## `playRecord`

**Signature:**
```cpp
void playRecord(PacketPlayerPtr player);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `PacketPlayerPtr` | `player` | - |

---

(isconnected)=
## `isConnected`

**Signature:**
```cpp
bool isConnected();
```

**Returns:**
- `bool`

---

(isconnecting)=
## `isConnecting`

**Signature:**
```cpp
bool isConnecting();
```

**Returns:**
- `bool`

---

(generatexteakey)=
## `generateXteaKey`

**Signature:**
```cpp
void generateXteaKey();
```

---

(setxteakey)=
## `setXteaKey`

**Signature:**
```cpp
void setXteaKey(uint32 a, uint32 b, uint32 c, uint32 d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `a` | - |
| `uint32` | `b` | - |
| `uint32` | `c` | - |
| `uint32` | `d` | - |

---

(getxteakey)=
## `getXteaKey`

**Signature:**
```cpp
std::vector<uint32> getXteaKey();
```

**Returns:**
- `std::vector&lt;uint32&gt;`

---

(send)=
## `send`

**Signature:**
```cpp
virtual void send(const OutputMessagePtr& outputMessage, bool rawPacket = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const OutputMessagePtr&` | `outputMessage` |  | - |
| `bool` | `rawPacket` | `false` | - |

---

(recv)=
## `recv`

**Signature:**
```cpp
virtual void recv();
```

---

(onconnect)=
## `onConnect`

**Signature:**
```cpp
protected: virtual void onConnect();
```

---

(onrecv)=
## `onRecv`

**Signature:**
```cpp
virtual void onRecv(const InputMessagePtr& inputMessage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `inputMessage` | - |

---

(onerror)=
## `onError`

**Signature:**
```cpp
virtual void onError(const boost::system::error_code& err);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `err` | - |

---

(onproxypacket)=
## `onProxyPacket`

**Signature:**
```cpp
void onProxyPacket(const std::shared_ptr<std::vector<uint8_t>>& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::shared_ptr&lt;std::vector&lt;uint8_t&gt;&gt;&` | `packet` | - |

---

(onplayerpacket)=
## `onPlayerPacket`

**Signature:**
```cpp
void onPlayerPacket(const std::shared_ptr<std::vector<uint8_t>>& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::shared_ptr&lt;std::vector&lt;uint8_t&gt;&gt;&` | `packet` | - |

---

(onlocaldisconnected)=
## `onLocalDisconnected`

**Signature:**
```cpp
void onLocalDisconnected(boost::system::error_code ec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `boost::system::error_code` | `ec` | - |

---

(internalrecvheader)=
## `internalRecvHeader`

**Signature:**
```cpp
private: void internalRecvHeader(uint8* buffer, uint32 size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8*` | `buffer` | - |
| `uint32` | `size` | - |

---

(internalrecvdata)=
## `internalRecvData`

**Signature:**
```cpp
void internalRecvData(uint8* buffer, uint32 size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8*` | `buffer` | - |
| `uint32` | `size` | - |

---

(xteadecrypt)=
## `xteaDecrypt`

**Signature:**
```cpp
bool xteaDecrypt(const InputMessagePtr& inputMessage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `inputMessage` | - |

**Returns:**
- `bool`

---

(xteaencrypt)=
## `xteaEncrypt`

**Signature:**
```cpp
void xteaEncrypt(const OutputMessagePtr& outputMessage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OutputMessagePtr&` | `outputMessage` | - |

---

(getelapsedtickssincelastread)=
## `getElapsedTicksSinceLastRead`

**Signature:**
```cpp
ticks_t getElapsedTicksSinceLastRead();
```

**Returns:**
- `ticks_t`

---

(getconnection)=
## `getConnection`

**Signature:**
```cpp
ConnectionPtr getConnection();
```

**Returns:**
- `ConnectionPtr`

---

(setconnection)=
## `setConnection`

**Signature:**
```cpp
void setConnection(const ConnectionPtr& connection);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ConnectionPtr&` | `connection` | - |

---

(enablexteaencryption)=
## `enableXteaEncryption`

**Signature:**
```cpp
void enableXteaEncryption();
```

---

(enablechecksum)=
## `enableChecksum`

**Signature:**
```cpp
void enableChecksum();
```

---

(enabledsequencedpackets)=
## `enabledSequencedPackets`

**Signature:**
```cpp
void enabledSequencedPackets();
```

---

(enablebigpackets)=
## `enableBigPackets`

**Signature:**
```cpp
void enableBigPackets();
```

---

(enablecompression)=
## `enableCompression`

**Signature:**
```cpp
void enableCompression();
```

---

(asprotocol)=
## `asProtocol`

**Signature:**
```cpp
ProtocolPtr asProtocol();
```

**Returns:**
- `ProtocolPtr`

---

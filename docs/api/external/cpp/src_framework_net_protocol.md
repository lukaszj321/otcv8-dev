# src/framework/net/protocol.h

```cpp
public: Protocol();
```
```cpp
void connect(const std::string& host, uint16 port);
```
```cpp
void disconnect();
```
```cpp
void setRecorder(PacketRecorderPtr recorder);
```
```cpp
void playRecord(PacketPlayerPtr player);
```
```cpp
bool isConnected();
```
```cpp
bool isConnecting();
```
```cpp
void generateXteaKey();
```
```cpp
void setXteaKey(uint32 a, uint32 b, uint32 c, uint32 d);
```
```cpp
std::vector<uint32> getXteaKey();
```
```cpp
virtual void send(const OutputMessagePtr& outputMessage, bool rawPacket = false);
```
```cpp
virtual void recv();
```
```cpp
protected: virtual void onConnect();
```
```cpp
virtual void onRecv(const InputMessagePtr& inputMessage);
```
```cpp
virtual void onError(const boost::system::error_code& err);
```
```cpp
void onProxyPacket(const std::shared_ptr<std::vector<uint8_t>>& packet);
```
```cpp
void onPlayerPacket(const std::shared_ptr<std::vector<uint8_t>>& packet);
```
```cpp
void onLocalDisconnected(boost::system::error_code ec);
```
```cpp
private: void internalRecvHeader(uint8* buffer, uint32 size);
```
```cpp
void internalRecvData(uint8* buffer, uint32 size);
```
```cpp
bool xteaDecrypt(const InputMessagePtr& inputMessage);
```
```cpp
void xteaEncrypt(const OutputMessagePtr& outputMessage);
```
```cpp
ticks_t getElapsedTicksSinceLastRead();
```
```cpp
ConnectionPtr getConnection();
```
```cpp
void setConnection(const ConnectionPtr& connection);
```
```cpp
void enableXteaEncryption();
```
```cpp
void enableChecksum();
```
```cpp
void enabledSequencedPackets();
```
```cpp
void enableBigPackets();
```
```cpp
void enableCompression();
```
```cpp
ProtocolPtr asProtocol();
```
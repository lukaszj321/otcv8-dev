# src/framework/net/packet_player.h

```cpp
public:
    PacketPlayer(const std::string& file);
```
```cpp
void start(std::function<void(std::shared_ptr<std::vector<uint8_t>>)> recvCallback, std::function<void(boost::system::error_code)> disconnectCallback);
```
```cpp
void stop();
```
```cpp
void onOutputPacket(const OutputMessagePtr& packet);
```
```cpp
private:
    void process();
```
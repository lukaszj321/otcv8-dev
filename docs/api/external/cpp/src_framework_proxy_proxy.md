# src/framework/proxy/proxy.h

```cpp
public:
    ProxyManager() : m_io(), m_guard(boost::asio::make_work_guard(m_io)) { } void init();
```
```cpp
void terminate();
```
```cpp
void clear();
```
```cpp
void setMaxActiveProxies(int value) { m_maxActiveProxies = value; if (m_maxActiveProxies < 1) m_maxActiveProxies = 1; } bool isActive();
```
```cpp
void addProxy(const std::string& host, uint16_t port, int priority);
```
```cpp
void removeProxy(const std::string& host, uint16_t port);
```
```cpp
uint32_t addSession(uint16_t port, std::function<void(ProxyPacketPtr)> recvCallback, std::function<void(boost::system::error_code)> disconnectCallback);
```
```cpp
void removeSession(uint32_t sessionId);
```
```cpp
void send(uint32_t sessionId, ProxyPacketPtr packet);
```
```cpp
int getPing();
```
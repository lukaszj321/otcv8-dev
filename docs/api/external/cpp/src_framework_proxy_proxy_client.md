# src/framework/proxy/proxy_client.h

```cpp
void start();
```
```cpp
void terminate();
```
```cpp
std::string getDebugInfo();
```
```cpp
void addSession(uint32_t id, int m_port);
```
```cpp
void removeSession(uint32_t id);
```
```cpp
void send(const ProxyPacketPtr& packet);
```
```cpp
private: void check(const boost::system::error_code& ec = boost::system::error_code());
```
```cpp
void connect();
```
```cpp
void disconnect();
```
```cpp
void ping();
```
```cpp
void onPing(uint32_t packetId);
```
```cpp
void readHeader();
```
```cpp
void onHeader(const boost::system::error_code& ec, std::size_t bytes_transferred);
```
```cpp
void onPacket(const boost::system::error_code& ec, std::size_t bytes_transferred);
```
```cpp
void onSent(const boost::system::error_code& ec, std::size_t bytes_transferred);
```
```cpp
void start(int maxConnections = 3);
```
```cpp
void terminate(boost::system::error_code ec = boost::asio::error::eof);
```
```cpp
void onPacket(const ProxyPacketPtr& packet);
```
```cpp
void onProxyPacket(uint32_t packetId, uint32_t lastRecivedPacketId, const ProxyPacketPtr& packet);
```
```cpp
private: void check(const boost::system::error_code& ec);
```
```cpp
void selectProxies();
```
```cpp
void readTibia12Header();
```
```cpp
void readHeader();
```
```cpp
void onHeader(const boost::system::error_code& ec, std::size_t bytes_transferred);
```
```cpp
void onBody(const boost::system::error_code& ec, std::size_t bytes_transferred);
```
```cpp
void onSent(const boost::system::error_code& ec, std::size_t bytes_transferred);
```
```cpp
public: Proxy(boost::asio::io_context& io, const std::string& host, uint16_t port, int priority) : m_io(io), m_timer(io), m_socket(io), m_resolver(io), m_state(STATE_NOT_CONNECTED);
```
```cpp
uint32_t getPing();
```
```cpp
uint32_t getRealPing();
```
```cpp
uint32_t getPriority();
```
```cpp
bool isConnected();
```
```cpp
std::string getHost();
```
```cpp
uint16_t getPort();
```
```cpp
bool isActive();
```
```cpp
public: Session(boost::asio::io_context& io, boost::asio::ip::tcp::socket socket, int port) : m_io(io), m_timer(io), m_socket(std::move(socket));
```
```cpp
uint32_t getId();
```
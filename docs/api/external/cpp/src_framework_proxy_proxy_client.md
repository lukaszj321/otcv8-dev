# src/framework/proxy/proxy_client.h

```cpp
public:
    Proxy(boost::asio::io_context& io, const std::string& host, uint16_t port, int priority) : m_io(io), m_timer(io), m_socket(io), m_resolver(io), m_state(STATE_NOT_CONNECTED) { m_host = host; m_port = port; m_priority = priority; } // thread-safe void start();
```
```cpp
void terminate();
```
```cpp
uint32_t getPing() { return m_ping + m_priority; } uint32_t getRealPing() { return m_ping; } uint32_t getPriority() { return m_priority; } bool isConnected() { return m_state == STATE_CONNECTED; } std::string getHost() { return m_host; } uint16_t getPort() { return m_port; } std::string getDebugInfo();
```
```cpp
bool isActive() { return m_sessions > 0; } // not thread-safe void addSession(uint32_t id, int m_port);
```
```cpp
void removeSession(uint32_t id);
```
```cpp
void send(const ProxyPacketPtr& packet);
```
```cpp
private:
    void check(const boost::system::error_code& ec = boost::system::error_code());
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
public:
    Session(boost::asio::io_context& io, boost::asio::ip::tcp::socket socket, int port) : m_io(io), m_timer(io), m_socket(std::move(socket)) { m_id = (std::chrono::high_resolution_clock::now().time_since_epoch().count()) & 0xFFFFFFFF; if (m_id == 0) m_id = 1; m_port = port; m_useSocket = true; } Session(boost::asio::io_context& io, int port, std::function<void(ProxyPacketPtr)> recvCallback, std::function<void(boost::system::error_code)> disconnectCallback) : m_io(io), m_timer(io), m_socket(io) { m_id = (std::chrono::high_resolution_clock::now().time_since_epoch().count()) & 0xFFFFFFFF; if (m_id == 0) m_id = 1; m_port = port; m_useSocket = false; m_recvCallback = recvCallback; m_disconnectCallback = disconnectCallback; } // thread safe uint32_t getId() { return m_id; } void start(int maxConnections = 3);
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
private:
    void check(const boost::system::error_code& ec);
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
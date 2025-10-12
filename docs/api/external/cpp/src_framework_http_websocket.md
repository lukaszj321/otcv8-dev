# src/framework/http/websocket.h

```cpp
public:

    WebsocketSession(boost::asio::io_service& service, const std::string& url, const std::string& agent, int timeout, HttpResult_ptr result, WebsocketSession_cb callback) : m_service(service), m_url(url), m_agent(agent), m_resolver(service), m_callback(callback), m_result(result), m_timer(service), m_timeout(timeout) { VALIDATE(m_callback);
```
```cpp
void start();
```
```cpp
void send(std::string data);
```
```cpp
void close();
```
```cpp
void on_resolve(const boost::system::error_code& ec, boost::asio::ip::tcp::resolver::iterator iterator);
```
```cpp
void on_connect(const boost::system::error_code& ec);
```
```cpp
void on_handshake(const boost::system::error_code& ec);
```
```cpp
void on_send(const boost::system::error_code& ec);
```
```cpp
void on_read(const boost::system::error_code& ec, size_t bytes_transferred);
```
```cpp
void onTimeout(const boost::system::error_code& error);
```
```cpp
void onError(const std::string& error, const std::string& details = "");
```
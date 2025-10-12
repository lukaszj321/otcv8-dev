# src/framework/http/session.h

```cpp
public:

    HttpSession(boost::asio::io_service& service, const std::string& url, const std::string& agent, int timeout, bool isJson, HttpResult_ptr result, HttpResult_cb callback) : m_service(service), m_url(url), m_agent(agent), m_socket(service), m_resolver(service), m_callback(callback), m_result(result), m_timer(service), m_timeout(timeout), m_isJson(isJson) { VALIDATE(m_callback);
```
```cpp
void start();
```
```cpp
void cancel() { onError("canceled");
```
```cpp
void on_resolve(const boost::system::error_code& ec, boost::asio::ip::tcp::resolver::iterator iterator);
```
```cpp
void on_connect(const boost::system::error_code& ec);
```
```cpp
void on_request_sent(const boost::system::error_code& ec);
```
```cpp
void on_read_header(const boost::system::error_code & ec, size_t bytes_transferred);
```
```cpp
void on_read(const boost::system::error_code& ec, size_t bytes_transferred);
```
```cpp
void close();
```
```cpp
void onTimeout(const boost::system::error_code& error);
```
```cpp
void onError(const std::string& error, const std::string& details = "");
```
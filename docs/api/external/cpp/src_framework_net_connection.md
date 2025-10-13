# src/framework/net/connection.h

```cpp
public: Connection();
```
```cpp
static void poll();
```
```cpp
static void terminate();
```
```cpp
void connect(const std::string& host, uint16 port, const std::function<void()>& connectCallback);
```
```cpp
void close();
```
```cpp
void write(uint8* buffer, size_t size);
```
```cpp
void read(uint32 bytes, const RecvCallback& callback);
```
```cpp
void read_until(const std::string& what, const RecvCallback& callback);
```
```cpp
void read_some(const RecvCallback& callback);
```
```cpp
int getIp();
```
```cpp
protected: void internal_connect(asio::ip::basic_resolver<asio::ip::tcp>::iterator endpointIterator);
```
```cpp
void internal_write();
```
```cpp
void onResolve(const boost::system::error_code& error, asio::ip::tcp::resolver::iterator endpointIterator);
```
```cpp
void onConnect(const boost::system::error_code& error);
```
```cpp
void onCanWrite(const boost::system::error_code& error);
```
```cpp
void onWrite(const boost::system::error_code& error, size_t writeSize, std::shared_ptr<asio::streambuf> outputStream);
```
```cpp
void onRecv(const boost::system::error_code& error, size_t recvSize);
```
```cpp
void onTimeout(const boost::system::error_code& error);
```
```cpp
void handleError(const boost::system::error_code& error);
```
```cpp
void setErrorCallback(const ErrorCallback& errorCallback);
```
```cpp
boost::system::error_code getError();
```
```cpp
bool isConnecting();
```
```cpp
bool isConnected();
```
```cpp
ticks_t getElapsedTicksSinceLastRead();
```
```cpp
ConnectionPtr asConnection();
```
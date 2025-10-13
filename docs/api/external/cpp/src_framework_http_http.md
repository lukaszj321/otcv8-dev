# src/framework/http/http.h

```cpp
void init();
```
```cpp
void terminate();
```
```cpp
int get(const std::string& url, int timeout = 5);
```
```cpp
int post(const std::string& url, const std::string& data, int timeout = 5, bool isJson = false);
```
```cpp
int download(const std::string& url, std::string path, int timeout = 5);
```
```cpp
int ws(const std::string& url, int timeout = 5);
```
```cpp
bool wsSend(int operationId, std::string message);
```
```cpp
bool wsClose(int operationId);
```
```cpp
bool cancel(int id);
```
```cpp
public: Http() : m_ios(), m_guard(boost::asio::make_work_guard(m_ios));
```
```cpp
void clearDownloads();
```
```cpp
HttpResult_ptr getFile(std::string path);
```
```cpp
void setUserAgent(const std::string& userAgent);
```
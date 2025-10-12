# src/framework/http/http.h

```cpp
public:
    Http() : m_ios(), m_guard(boost::asio::make_work_guard(m_ios)) {} void init();
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
void clearDownloads() { m_downloads.clear();
```
```cpp
HttpResult_ptr getFile(std::string path) { if (!path.empty() && path[0] == '/') path = path.substr(1);
```
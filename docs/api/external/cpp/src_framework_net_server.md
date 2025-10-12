# src/framework/net/server.h

```cpp
public:
    Server(int port);
```
```cpp
static ServerPtr create(int port);
```
```cpp
bool isOpen() { return m_isOpen; } void close();
```
```cpp
void acceptNext();
```
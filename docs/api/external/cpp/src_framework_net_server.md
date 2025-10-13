# src/framework/net/server.h

```cpp
public: Server(int port);
```
```cpp
static ServerPtr create(int port);
```
```cpp
void close();
```
```cpp
void acceptNext();
```
```cpp
bool isOpen();
```
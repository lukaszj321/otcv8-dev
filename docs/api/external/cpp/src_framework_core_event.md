# src/framework/core/event.h

```cpp
public: Event(const std::string& function, const std::function<void()>& callback, bool botSafe = false);
```
```cpp
virtual void execute();
```
```cpp
void cancel();
```
```cpp
bool isCanceled();
```
```cpp
bool isExecuted();
```
```cpp
bool isBotSafe();
```
```cpp
const std::string& getFunction();
```
# src/framework/core/asyncdispatcher.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void spawn_thread();
```
```cpp
void stop();
```
```cpp
std::lock_guard<std::mutex> lock(m_mutex);
```
```cpp
return std::shared_future<typename std::invoke_result<F>::type>(prom->get_future());
```
```cpp
std::lock_guard<std::mutex> lock(m_mutex);
```
```cpp
protected: void exec_loop();
```
```cpp
std::shared_future<typename std::invoke_result<F>::type> schedule(const F& task);
```
```cpp
void dispatch(std::function<void()> f);
```
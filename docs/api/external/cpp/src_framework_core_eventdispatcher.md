# src/framework/core/eventdispatcher.h

```cpp
public: void shutdown();
```
```cpp
void poll();
```
```cpp
EventPtr addEventEx(const std::string& function, const std::function<void()>& callback, bool pushFront = false);
```
```cpp
ScheduledEventPtr scheduleEventEx(const std::string& function, const std::function<void()>& callback, int delay);
```
```cpp
ScheduledEventPtr cycleEventEx(const std::string& function, const std::function<void()>& callback, int delay);
```
```cpp
bool isBotSafe();
```
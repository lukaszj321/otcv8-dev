# src/framework/core/scheduledevent.h

```cpp
public: ScheduledEvent(const std::string& function, const std::function<void()>& callback, int delay, int maxCycles, bool botSafe = false);
```
```cpp
void execute();
```
```cpp
bool nextCycle();
```
```cpp
int ticks();
```
```cpp
int remainingTicks();
```
```cpp
int delay();
```
```cpp
int cyclesExecuted();
```
```cpp
int maxCycles();
```
```cpp
bool operator()(const ScheduledEventPtr& a, const ScheduledEventPtr& b);
```
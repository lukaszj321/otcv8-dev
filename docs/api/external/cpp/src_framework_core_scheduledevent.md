# src/framework/core/scheduledevent.h

```cpp
public:
    ScheduledEvent(const std::string& function, const std::function<void()>& callback, int delay, int maxCycles, bool botSafe = false);
```
```cpp
void execute();
```
```cpp
bool nextCycle();
```
```cpp
int ticks() { return m_ticks; } int remainingTicks() { return m_ticks - g_clock.millis();
```
```cpp
int delay() { return m_delay; } int cyclesExecuted() { return m_cyclesExecuted; } int maxCycles() { return m_maxCycles; } private: ticks_t m_ticks; int m_delay; int m_maxCycles; int m_cyclesExecuted; }; struct lessScheduledEvent { bool operator()(const ScheduledEventPtr& a, const ScheduledEventPtr& b) { return b->ticks() < a->ticks();
```
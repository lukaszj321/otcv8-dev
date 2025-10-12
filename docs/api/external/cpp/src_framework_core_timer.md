# src/framework/core/timer.h

```cpp
public:
    Timer() { restart();
```
```cpp
void restart();
```
```cpp
void stop() { m_stopped = true; } void adjust(ticks_t value) { m_startTicks += value; } ticks_t startTicks() { return m_startTicks; } ticks_t ticksElapsed();
```
# src/framework/util/stats.h

```cpp
public:
    void add(int type, Stat* stats);
```
```cpp
std::string get(int type, int limit, bool pretty);
```
```cpp
void clear(int type);
```
```cpp
void clearAll();
```
```cpp
std::string getSlow(int type, int limit, unsigned int minTime, bool pretty);
```
```cpp
void clearSlow(int type);
```
```cpp
int types() { return STATS_LAST + 1; } int64_t getSleepTime() { return m_sleepTime; } void resetSleepTime() { m_sleepTime = 0; } int64_t m_sleepTime = 0; void addWidget(UIWidget* widget);
```
```cpp
void removeWidget(UIWidget* widget);
```
```cpp
std::string getWidgetsInfo(int limit, bool pretty);
```
```cpp
inline void addTexture() { createdTextures += 1; } inline void removeTexture() { destroyedTextures += 1; } inline void addThing() { createdThings += 1; } inline void removeThing() { destroyedThings += 1; } inline void addCreature() { createdCreatures += 1; } inline void removeCreature() { destroyedCreatures += 1; } private: struct { StatsMap data; StatsList slow; int64_t start = 0; } stats[STATS_LAST + 1]; std::set<UIWidget*> widgets; int createdWidgets = 0; int destroyedWidgets = 0; int createdTextures = 0; int destroyedTextures = 0; int createdThings = 0; int destroyedThings = 0; int createdCreatures = 0; int destroyedCreatures = 0; std::mutex m_mutex; }; extern Stats g_stats; class AutoStat { public: AutoStat(int type, const std::string& description, const std::string& extraDescription = "") : m_type(type), m_stat(new Stat(0, description, extraDescription)), m_timePoint(std::chrono::high_resolution_clock::now()) {} ~AutoStat() { m_stat->executionTime = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - m_timePoint).count();
```
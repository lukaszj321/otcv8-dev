# src/framework/sound/soundchannel.h

```cpp
public:
    SoundChannel(int id) : m_id(id), m_gain(1) { } SoundSourcePtr play(const std::string& filename, float fadetime = 0, float gain = 1.0f);
```
```cpp
void stop(float fadetime = 0);
```
```cpp
void enqueue(const std::string& filename, float fadetime = 0, float gain = 1.0f);
```
```cpp
void enable() { setEnabled(true);
```
```cpp
void disable() { setEnabled(false);
```
```cpp
void setGain(float gain);
```
```cpp
float getGain() { return m_gain; } void setEnabled(bool enable);
```
```cpp
bool isEnabled() { return m_enabled; } int getId() { return m_id; } protected: void update();
```
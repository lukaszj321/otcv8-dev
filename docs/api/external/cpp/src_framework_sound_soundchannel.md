# src/framework/sound/soundchannel.h

```cpp
SoundSourcePtr play(const std::string& filename, float fadetime = 0, float gain = 1.0f);
```
```cpp
void stop(float fadetime = 0);
```
```cpp
void enqueue(const std::string& filename, float fadetime = 0, float gain = 1.0f);
```
```cpp
void setGain(float gain);
```
```cpp
void setEnabled(bool enable);
```
```cpp
protected: void update();
```
```cpp
public: SoundChannel(int id) : m_id(id), m_gain(1);
```
```cpp
void enable();
```
```cpp
void disable();
```
```cpp
float getGain();
```
```cpp
bool isEnabled();
```
```cpp
int getId();
```
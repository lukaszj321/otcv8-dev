# src/framework/sound/soundsource.h

```cpp
protected:
    SoundSource(uint sourceId) : m_sourceId(sourceId) { } public: enum FadeState { NoFading, FadingOn, FadingOff }; SoundSource();
```
```cpp
virtual void play();
```
```cpp
virtual void stop();
```
```cpp
virtual bool isBuffering();
```
```cpp
virtual bool isPlaying() { return isBuffering();
```
```cpp
void setName(const std::string& name) { m_name = name; } virtual void setLooping(bool looping);
```
```cpp
virtual void setRelative(bool relative);
```
```cpp
virtual void setReferenceDistance(float distance);
```
```cpp
virtual void setGain(float gain);
```
```cpp
virtual void setPitch(float pitch);
```
```cpp
virtual void setPosition(const Point& pos);
```
```cpp
virtual void setVelocity(const Point& velocity);
```
```cpp
virtual void setFading(FadeState state, float fadetime);
```
```cpp
std::string getName() { return m_name; } uchar getChannel() { return m_channel; } float getGain() { return m_gain; } protected: void setBuffer(const SoundBufferPtr& buffer);
```
```cpp
void setChannel(uchar channel) { m_channel = channel; } virtual void update();
```
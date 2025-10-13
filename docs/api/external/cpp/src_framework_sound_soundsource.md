# src/framework/sound/soundsource.h

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
virtual void setLooping(bool looping);
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
protected: void setBuffer(const SoundBufferPtr& buffer);
```
```cpp
virtual void update();
```
```cpp
protected: SoundSource(uint sourceId) : m_sourceId(sourceId);
```
```cpp
virtual bool isPlaying();
```
```cpp
void setName(const std::string& name);
```
```cpp
std::string getName();
```
```cpp
uchar getChannel();
```
```cpp
float getGain();
```
```cpp
void setChannel(uchar channel);
```
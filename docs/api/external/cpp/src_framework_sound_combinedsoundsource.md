# src/framework/sound/combinedsoundsource.h

```cpp
public: CombinedSoundSource();
```
```cpp
void addSource(const SoundSourcePtr& source);
```
```cpp
void play();
```
```cpp
void stop();
```
```cpp
bool isBuffering();
```
```cpp
bool isPlaying();
```
```cpp
void setLooping(bool looping);
```
```cpp
void setRelative(bool relative);
```
```cpp
void setReferenceDistance(float distance);
```
```cpp
void setGain(float gain);
```
```cpp
void setPitch(float pitch);
```
```cpp
void setPosition(const Point& pos);
```
```cpp
void setVelocity(const Point& velocity);
```
```cpp
void setFading(FadeState state, float fadetime);
```
```cpp
protected: virtual void update();
```
```cpp
std::vector<SoundSourcePtr> getSources();
```
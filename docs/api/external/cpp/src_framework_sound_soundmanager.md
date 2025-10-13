# src/framework/sound/soundmanager.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void poll();
```
```cpp
void setAudioEnabled(bool enable);
```
```cpp
void stopAll();
```
```cpp
void preload(std::string filename);
```
```cpp
SoundSourcePtr play(std::string filename, float fadetime = 0, float gain = 0);
```
```cpp
SoundChannelPtr getChannel(int channel);
```
```cpp
std::string resolveSoundFile(std::string file);
```
```cpp
void ensureContext();
```
```cpp
private: SoundSourcePtr createSoundSource(const std::string& filename);
```
```cpp
bool isAudioEnabled();
```
```cpp
void enableAudio();
```
```cpp
void disableAudio();
```
# src/framework/sound/soundmanager.h

```cpp
public:
    void init();
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
bool isAudioEnabled() { return m_device && m_context && m_audioEnabled ; } void enableAudio() { setAudioEnabled(true);
```
```cpp
void disableAudio() { setAudioEnabled(true);
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
private:
    SoundSourcePtr createSoundSource(const std::string& filename);
```
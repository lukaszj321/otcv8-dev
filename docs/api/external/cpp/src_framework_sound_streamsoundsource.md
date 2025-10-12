# src/framework/sound/streamsoundsource.h

```cpp
void play();
```
```cpp
void stop();
```
```cpp
bool isPlaying() { return m_playing; } void setSoundFile(const SoundFilePtr& soundFile);
```
```cpp
void downMix(DownMix downMix);
```
```cpp
void update();
```
```cpp
private:
    void queueBuffers();
```
```cpp
void unqueueBuffers();
```
```cpp
bool fillBufferAndQueue(uint buffer);
```
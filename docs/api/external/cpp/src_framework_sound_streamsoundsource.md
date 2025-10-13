# src/framework/sound/streamsoundsource.h

```cpp
void play();
```
```cpp
void stop();
```
```cpp
void setSoundFile(const SoundFilePtr& soundFile);
```
```cpp
void downMix(DownMix downMix);
```
```cpp
void update();
```
```cpp
private: void queueBuffers();
```
```cpp
void unqueueBuffers();
```
```cpp
bool fillBufferAndQueue(uint buffer);
```
```cpp
bool isPlaying();
```
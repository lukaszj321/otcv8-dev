# src/framework/sound/soundbuffer.h

```cpp
public: SoundBuffer();
```
```cpp
bool fillBuffer(const SoundFilePtr& soundFile);
```
```cpp
bool fillBuffer(ALenum sampleFormat, const DataBuffer<char>& data, int size, int rate);
```
```cpp
uint getBufferId();
```
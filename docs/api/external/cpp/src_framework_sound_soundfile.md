# src/framework/sound/soundfile.h

```cpp
public: SoundFile(const FileStreamPtr& fileStream);
```
```cpp
static SoundFilePtr loadSoundFile(const std::string& filename);
```
```cpp
ALenum getSampleFormat();
```
```cpp
virtual int read(void *buffer, int bufferSize);
```
```cpp
virtual void reset();
```
```cpp
bool eof();
```
```cpp
int getChannels();
```
```cpp
int getRate();
```
```cpp
int getBps();
```
```cpp
int getSize();
```
```cpp
std::string getName();
```
# src/framework/sound/soundfile.h

```cpp
public:
    SoundFile(const FileStreamPtr& fileStream);
```
```cpp
static SoundFilePtr loadSoundFile(const std::string& filename);
```
```cpp
virtual int read(void *buffer, int bufferSize) { return -1; } virtual void reset() { } bool eof() { return m_file->eof();
```
```cpp
int getChannels() { return m_channels; } int getRate() { return m_rate; } int getBps() { return m_bps; } int getSize() { return m_size; } std::string getName() { return m_file ? m_file->name() : std::string();
```
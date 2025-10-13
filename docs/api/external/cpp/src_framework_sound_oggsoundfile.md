# src/framework/sound/oggsoundfile.h

```cpp
public: OggSoundFile(const FileStreamPtr& fileStream);
```
```cpp
bool prepareOgg();
```
```cpp
int read(void *buffer, int bufferSize);
```
```cpp
void reset();
```
```cpp
private: static size_t cb_read(void* ptr, size_t size, size_t nmemb, void* source);
```
```cpp
static int cb_seek(void* source, ogg_int64_t offset, int whence);
```
```cpp
static int cb_close(void* source);
```
```cpp
static long cb_tell(void* source);
```
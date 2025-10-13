# src/framework/graphics/framebuffermanager.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void clear();
```
```cpp
FrameBufferPtr createFrameBuffer(bool withDepth = false);
```
```cpp
const FrameBufferPtr& getTemporaryFrameBuffer();
```
```cpp
const FrameBufferPtr& getDrawQueueTemporaryFrameBuffer();
```
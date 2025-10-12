# src/framework/core/graphicalapplication.h

```cpp
public:
    void init(std::vector<std::string>& args);
```
```cpp
void deinit();
```
```cpp
void terminate();
```
```cpp
void run();
```
```cpp
void poll();
```
```cpp
void pollGraphics();
```
```cpp
void close();
```
```cpp
bool willRepaint() { return m_mustRepaint; } void repaint() { m_mustRepaint = true; } void setMaxFps(int maxFps) { m_maxFps = maxFps; } int getMaxFps() { return m_maxFps; } int getFps() { return m_graphicsFrames.getFps();
```
```cpp
int getGraphicsFps() { return m_graphicsFrames.getFps();
```
```cpp
int getProcessingFps() { return m_processingFrames.getFps();
```
```cpp
bool isOnInputEvent() { return m_onInputEvent; } int getIteration() { return m_iteration; } void doScreenshot(std::string file);
```
```cpp
void scaleUp();
```
```cpp
void scaleDown();
```
```cpp
void scale(float value);
```
```cpp
void setSmooth(bool value);
```
```cpp
void doMapScreenshot(std::string fileName);
```
```cpp
protected:
    void resize(const Size& size);
```
```cpp
void inputEvent(InputEvent event);
```
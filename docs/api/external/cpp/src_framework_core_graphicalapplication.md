# src/framework/core/graphicalapplication.h

```cpp
public: void init(std::vector<std::string>& args);
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
void doScreenshot(std::string file);
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
protected: void resize(const Size& size);
```
```cpp
void inputEvent(InputEvent event);
```
```cpp
bool willRepaint();
```
```cpp
void repaint();
```
```cpp
void setMaxFps(int maxFps);
```
```cpp
int getMaxFps();
```
```cpp
int getFps();
```
```cpp
int getGraphicsFps();
```
```cpp
int getProcessingFps();
```
```cpp
bool isOnInputEvent();
```
```cpp
int getIteration();
```
# src/framework/platform/sdlwindow.h

```cpp
void internalInitGL();
```
```cpp
void internalDestroyGL();
```
```cpp
void internalCheckGL();
```
```cpp
void internalChooseGL();
```
```cpp
void internalCreateGLContext();
```
```cpp
void internalDestroyGLContext();
```
```cpp
void internalConnectGLContext();
```
```cpp
public: SDLWindow();
```
```cpp
void init();
```
```cpp
void terminate();
```
```cpp
void move(const Point& pos);
```
```cpp
void resize(const Size& size);
```
```cpp
void show();
```
```cpp
void hide();
```
```cpp
void minimize();
```
```cpp
void maximize();
```
```cpp
void poll();
```
```cpp
void swapBuffers();
```
```cpp
void showMouse();
```
```cpp
void hideMouse();
```
```cpp
void setMouseCursor(int cursorId);
```
```cpp
void restoreMouseCursor();
```
```cpp
void setTitle(const std::string& title);
```
```cpp
void setMinimumSize(const Size& minimumSize);
```
```cpp
void setFullscreen(bool fullscreen);
```
```cpp
void setVerticalSync(bool enable);
```
```cpp
void setIcon(const std::string& iconFile);
```
```cpp
void setClipboardText(const std::string& text);
```
```cpp
Size getDisplaySize();
```
```cpp
std::string getClipboardText();
```
```cpp
std::string getPlatformType();
```
```cpp
void updateSize();
```
```cpp
void handleTextInput(std::string text);
```
```cpp
void openUrl(std::string url);
```
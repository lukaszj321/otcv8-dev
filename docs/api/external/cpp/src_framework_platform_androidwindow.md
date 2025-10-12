# src/framework/platform/androidwindow.h

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
public:
    AndroidWindow();
```
```cpp
void init();
```
```cpp
void init(struct android_app* app);
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
void displayFatalError(const std::string& message) override; void showTextEditor(const std::string& title, const std::string& description, const std::string& text, int flags) override; void handleCmd(int32_t cmd);
```
```cpp
int handleInput(AInputEvent* event);
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
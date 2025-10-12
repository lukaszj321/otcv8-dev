# src/framework/platform/win32window.h

```cpp
void internalSetupTimerAccuracy();
```
```cpp
void internalCreateWindow();
```
```cpp
void internalCreateGLContext();
```
```cpp
void internalDestroyGLContext();
```
```cpp
void internalRestoreGLContext();
```
```cpp
bool isExtensionSupported(const char *ext);
```
```cpp
LRESULT windowProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
```
```cpp
LRESULT dispatcherWindowProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
```
```cpp
Fw::Key retranslateVirtualKey(WPARAM wParam, LPARAM lParam);
```
```cpp
public:
    WIN32Window();
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
void displayFatalError(const std::string& message);
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
void setIcon(const std::string& file);
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
void flash() override; protected: int internalLoadMouseCursor(const ImagePtr& image, const Point& hotSpot);
```
```cpp
private:
    Rect getClientRect();
```
```cpp
Rect getWindowRect();
```
```cpp
Rect adjustWindowRect(const Rect& rect);
```
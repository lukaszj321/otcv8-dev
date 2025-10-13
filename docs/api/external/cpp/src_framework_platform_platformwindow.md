# src/framework/platform/platformwindow.h

```cpp
public: virtual void init();
```
```cpp
virtual void terminate();
```
```cpp
virtual void move(const Point& pos);
```
```cpp
virtual void resize(const Size& size);
```
```cpp
virtual void show();
```
```cpp
virtual void hide();
```
```cpp
virtual void minimize();
```
```cpp
virtual void maximize();
```
```cpp
virtual void poll();
```
```cpp
virtual void swapBuffers();
```
```cpp
virtual void showMouse();
```
```cpp
virtual void hideMouse();
```
```cpp
int loadMouseCursor(const std::string& file, const Point& hotSpot);
```
```cpp
virtual void setMouseCursor(int cursorId);
```
```cpp
virtual void restoreMouseCursor();
```
```cpp
virtual void setTitle(const std::string& title);
```
```cpp
virtual void setMinimumSize(const Size& minimumSize);
```
```cpp
virtual void setFullscreen(bool fullscreen);
```
```cpp
virtual void setVerticalSync(bool enable);
```
```cpp
virtual void setIcon(const std::string& iconFile);
```
```cpp
virtual void setClipboardText(const std::string& text);
```
```cpp
virtual Size getDisplaySize();
```
```cpp
virtual std::string getClipboardText();
```
```cpp
virtual std::string getPlatformType();
```
```cpp
virtual void flash();
```
```cpp
protected: virtual int internalLoadMouseCursor(const ImagePtr& image, const Point& hotSpot);
```
```cpp
void updateUnmaximizedCoords();
```
```cpp
void processKeyDown(Fw::Key keyCode);
```
```cpp
void processKeyUp(Fw::Key keyCode);
```
```cpp
void releaseAllKeys();
```
```cpp
void fireKeysPress();
```
```cpp
virtual void displayFatalError(const std::string& message);
```
```cpp
bool hasVerticalSync();
```
```cpp
int getDisplayWidth();
```
```cpp
int getDisplayHeight();
```
```cpp
Size getUnmaximizedSize();
```
```cpp
Size getSize();
```
```cpp
Size getMinimumSize();
```
```cpp
int getWidth();
```
```cpp
int getHeight();
```
```cpp
Point getUnmaximizedPos();
```
```cpp
Point getPosition();
```
```cpp
int getX();
```
```cpp
int getY();
```
```cpp
Point getMousePosition();
```
```cpp
int getKeyboardModifiers();
```
```cpp
bool isKeyPressed(Fw::Key keyCode);
```
```cpp
bool isMouseButtonPressed(Fw::MouseButton mouseButton);
```
```cpp
bool isVisible();
```
```cpp
bool isMaximized();
```
```cpp
bool isFullscreen();
```
```cpp
bool hasFocus();
```
```cpp
void setOnClose(const std::function<void()>& onClose);
```
```cpp
void setOnResize(const OnResizeCallback& onResize);
```
```cpp
void setOnInputEvent(const OnInputEventCallback& onInputEvent);
```
```cpp
virtual void showTextEditor(const std::string& title, const std::string& description, const std::string& text, int flags);
```
```cpp
virtual void handleTextInput(std::string text);
```
```cpp
void setScaling(float scaling);
```
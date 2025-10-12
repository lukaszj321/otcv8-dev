# src/framework/platform/platformwindow.h

```cpp
virtual void setMouseCursor(int cursorId) = 0; virtual void restoreMouseCursor() = 0; virtual void setTitle(const std::string& title) = 0; virtual void setMinimumSize(const Size& minimumSize) = 0; virtual void setFullscreen(bool fullscreen) = 0; virtual void setVerticalSync(bool enable) = 0; virtual void setIcon(const std::string& iconFile) = 0; virtual void setClipboardText(const std::string& text) = 0; bool hasVerticalSync() { return m_verticalSync; } virtual Size getDisplaySize() = 0; virtual std::string getClipboardText() = 0; virtual std::string getPlatformType() = 0; int getDisplayWidth() { return getDisplaySize().width();
```
```cpp
int getDisplayHeight() { return getDisplaySize().height();
```
```cpp
Size getUnmaximizedSize() { return m_unmaximizedSize; } Size getSize() { return m_size; } Size getMinimumSize() { return m_minimumSize; } int getWidth() { return m_size.width();
```
```cpp
int getHeight() { return m_size.height();
```
```cpp
Point getUnmaximizedPos() { return m_unmaximizedPos; } Point getPosition() { return m_position; } int getX() { return m_position.x; } int getY() { return m_position.y; } Point getMousePosition() { return m_inputEvent.mousePos; } int getKeyboardModifiers() { return m_inputEvent.keyboardModifiers; } bool isKeyPressed(Fw::Key keyCode) { return m_keysState[keyCode]; } bool isMouseButtonPressed(Fw::MouseButton mouseButton) { return m_mouseButtonStates[mouseButton]; } bool isVisible() { return m_visible; } bool isMaximized() { return m_maximized; } bool isFullscreen() { return m_fullscreen; } bool hasFocus() { return m_focused; } void setOnClose(const std::function<void()>& onClose) { m_onClose = onClose; } void setOnResize(const OnResizeCallback& onResize) { m_onResize = onResize; } void setOnInputEvent(const OnInputEventCallback& onInputEvent) { m_onInputEvent = onInputEvent; } virtual void showTextEditor(const std::string& title, const std::string& description, const std::string& text, int flags) {} virtual void handleTextInput(std::string text) {} // for android void setScaling(float scaling) { m_scaling = scaling; } virtual void flash();
```
```cpp
protected:
    virtual int internalLoadMouseCursor(const ImagePtr& image, const Point& hotSpot) = 0; void updateUnmaximizedCoords();
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
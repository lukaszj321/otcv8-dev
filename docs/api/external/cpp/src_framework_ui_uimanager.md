# src/framework/ui/uimanager.h

```cpp
public:
    void init();
```
```cpp
void terminate();
```
```cpp
void render(Fw::DrawPane drawPane);
```
```cpp
void resize(const Size& size);
```
```cpp
void inputEvent(const InputEvent& event);
```
```cpp
void updatePressedWidget(const Fw::MouseButton button, const UIWidgetPtr& newPressedWidget, const Point& clickedPos = Point(), bool fireClicks = true);
```
```cpp
bool updateDraggingWidget(const UIWidgetPtr& draggingWidget, const Point& clickedPos = Point());
```
```cpp
void updateHoveredWidget(bool now = false);
```
```cpp
void clearStyles();
```
```cpp
bool importStyle(std::string file);
```
```cpp
bool importStyleFromString(std::string data);
```
```cpp
void importStyleFromOTML(const OTMLNodePtr& styleNode);
```
```cpp
OTMLNodePtr getStyle(const std::string& styleName);
```
```cpp
std::string getStyleClass(const std::string& styleName);
```
```cpp
UIWidgetPtr loadUIFromString(const std::string& data, const UIWidgetPtr& parent);
```
```cpp
UIWidgetPtr loadUI(std::string file, const UIWidgetPtr& parent);
```
```cpp
UIWidgetPtr displayUI(const std::string& file) { return loadUI(file, m_rootWidget);
```
```cpp
UIWidgetPtr createWidget(const std::string& styleName, const UIWidgetPtr& parent);
```
```cpp
UIWidgetPtr createWidgetFromOTML(const OTMLNodePtr& widgetNode, const UIWidgetPtr& parent);
```
```cpp
void setMouseReceiver(const UIWidgetPtr& widget) { m_mouseReceiver = widget; } void setKeyboardReceiver(const UIWidgetPtr& widget) { m_keyboardReceiver = widget; } void setDebugBoxesDrawing(bool enabled) { m_drawDebugBoxes = enabled; } void resetMouseReceiver() { m_mouseReceiver = m_rootWidget; } void resetKeyboardReceiver() { m_keyboardReceiver = m_rootWidget; } UIWidgetPtr getMouseReceiver() { return m_mouseReceiver; } UIWidgetPtr getKeyboardReceiver() { return m_keyboardReceiver; } UIWidgetPtr getDraggingWidget() { return m_draggingWidget; } UIWidgetPtr getHoveredWidget() { return m_hoveredWidget; } UIWidgetPtr getPressedWidget() { return m_pressedWidget[Fw::MouseLeftButton]; } UIWidgetPtr getRootWidget() { return m_rootWidget; } bool isMouseGrabbed() { return m_mouseReceiver != m_rootWidget; } bool isKeyboardGrabbed() { return m_keyboardReceiver != m_rootWidget; } bool isDrawingDebugBoxes() { return m_drawDebugBoxes; } protected: void onWidgetAppear(const UIWidgetPtr& widget);
```
```cpp
void onWidgetDisappear(const UIWidgetPtr& widget);
```
```cpp
void onWidgetDestroy(const UIWidgetPtr& widget);
```
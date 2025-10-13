# src/framework/ui/uimanager.h

```cpp
public: void init();
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
UIWidgetPtr createWidget(const std::string& styleName, const UIWidgetPtr& parent);
```
```cpp
UIWidgetPtr createWidgetFromOTML(const OTMLNodePtr& widgetNode, const UIWidgetPtr& parent);
```
```cpp
protected: void onWidgetAppear(const UIWidgetPtr& widget);
```
```cpp
void onWidgetDisappear(const UIWidgetPtr& widget);
```
```cpp
void onWidgetDestroy(const UIWidgetPtr& widget);
```
```cpp
UIWidgetPtr displayUI(const std::string& file);
```
```cpp
void setMouseReceiver(const UIWidgetPtr& widget);
```
```cpp
void setKeyboardReceiver(const UIWidgetPtr& widget);
```
```cpp
void setDebugBoxesDrawing(bool enabled);
```
```cpp
void resetMouseReceiver();
```
```cpp
void resetKeyboardReceiver();
```
```cpp
UIWidgetPtr getMouseReceiver();
```
```cpp
UIWidgetPtr getKeyboardReceiver();
```
```cpp
UIWidgetPtr getDraggingWidget();
```
```cpp
UIWidgetPtr getHoveredWidget();
```
```cpp
UIWidgetPtr getPressedWidget();
```
```cpp
UIWidgetPtr getRootWidget();
```
```cpp
bool isMouseGrabbed();
```
```cpp
bool isKeyboardGrabbed();
```
```cpp
bool isDrawingDebugBoxes();
```
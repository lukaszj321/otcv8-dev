# src/framework/ui/uitextedit.h

```cpp
public: UITextEdit();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
private: void update(bool focusCursor = false);
```
```cpp
public: void setCursorPos(int pos);
```
```cpp
void setSelection(int start, int end);
```
```cpp
void setTextHidden(bool hidden);
```
```cpp
void setTextVirtualOffset(const Point& offset);
```
```cpp
void setPlaceholderFont(const std::string& fontName);
```
```cpp
void moveCursorHorizontally(bool right);
```
```cpp
void moveCursorVertically(bool up);
```
```cpp
void appendText(std::string text);
```
```cpp
void appendCharacter(char c);
```
```cpp
void removeCharacter(bool right);
```
```cpp
void blinkCursor();
```
```cpp
void del(bool right = false);
```
```cpp
void paste(const std::string& text);
```
```cpp
std::string copy();
```
```cpp
std::string cut();
```
```cpp
void wrapText();
```
```cpp
std::string getDisplayedText();
```
```cpp
std::string getSelection();
```
```cpp
int getTextPos(Point pos);
```
```cpp
protected: void updateText();
```
```cpp
virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
virtual void onGeometryChange(const Rect& oldRect, const Rect& newRect);
```
```cpp
virtual void onFocusChange(bool focused, Fw::FocusReason reason);
```
```cpp
virtual bool onKeyText(const std::string& keyText);
```
```cpp
virtual bool onKeyPress(uchar keyCode, int keyboardModifiers, int autoRepeatTicks);
```
```cpp
virtual bool onMousePress(const Point& mousePos, Fw::MouseButton button);
```
```cpp
virtual bool onMouseRelease(const Point& mousePos, Fw::MouseButton button);
```
```cpp
virtual bool onMouseMove(const Point& mousePos, const Point& mouseMoved);
```
```cpp
virtual bool onDoubleClick(const Point& mousePos);
```
```cpp
virtual void onTextAreaUpdate(const Point& vitualOffset, const Size& virtualSize, const Size& totalSize);
```
```cpp
void setCursorVisible(bool enable);
```
```cpp
void setValidCharacters(const std::string validCharacters);
```
```cpp
void setShiftNavigation(bool enable);
```
```cpp
void setMultiline(bool enable);
```
```cpp
void setMaxLength(uint maxLength);
```
```cpp
void setEditable(bool editable);
```
```cpp
void setSelectable(bool selectable);
```
```cpp
void setSelectionColor(const Color& color);
```
```cpp
void setSelectionBackgroundColor(const Color& color);
```
```cpp
void setAutoScroll(bool autoScroll);
```
```cpp
void setAutoSubmit(bool autoSubmit);
```
```cpp
void setPlaceholder(std::string placeholder);
```
```cpp
void setPlaceholderColor(const Color& color);
```
```cpp
void setPlaceholderAlign(Fw::AlignmentFlag align);
```
```cpp
void selectAll();
```
```cpp
void clearSelection();
```
```cpp
int getCursorPos();
```
```cpp
Point getTextVirtualOffset();
```
```cpp
Size getTextVirtualSize();
```
```cpp
Size getTextTotalSize();
```
```cpp
uint getMaxLength();
```
```cpp
int getSelectionStart();
```
```cpp
int getSelectionEnd();
```
```cpp
Color getSelectionColor();
```
```cpp
Color getSelectionBackgroundColor();
```
```cpp
bool hasSelection();
```
```cpp
bool isCursorVisible();
```
```cpp
bool isTextHidden();
```
```cpp
bool isShiftNavigation();
```
```cpp
bool isMultiline();
```
```cpp
bool isEditable();
```
```cpp
bool isSelectable();
```
```cpp
bool isAutoScrolling();
```
```cpp
private: void disableUpdates();
```
```cpp
void enableUpdates();
```
```cpp
void recacheGlyphs();
```
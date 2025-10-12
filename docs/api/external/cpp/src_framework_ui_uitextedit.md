# src/framework/ui/uitextedit.h

```cpp
public:
    UITextEdit();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
private:
    void update(bool focusCursor = false);
```
```cpp
public:
    void setCursorPos(int pos);
```
```cpp
void setSelection(int start, int end);
```
```cpp
void setCursorVisible(bool enable) { m_cursorVisible = enable; } void setTextHidden(bool hidden);
```
```cpp
void setValidCharacters(const std::string validCharacters) { m_validCharacters = validCharacters; } void setShiftNavigation(bool enable) { m_shiftNavigation = enable; } void setMultiline(bool enable) { m_multiline = enable; } void setMaxLength(uint maxLength) { m_maxLength = maxLength; } void setTextVirtualOffset(const Point& offset);
```
```cpp
void setEditable(bool editable) { m_editable = editable; } void setSelectable(bool selectable) { m_selectable = selectable; } void setSelectionColor(const Color& color) { m_selectionColor = color; } void setSelectionBackgroundColor(const Color& color) { m_selectionBackgroundColor = color; } void setAutoScroll(bool autoScroll) { m_autoScroll = autoScroll; } void setAutoSubmit(bool autoSubmit) { m_autoSubmit = autoSubmit; } void setPlaceholder(std::string placeholder) { m_placeholder = placeholder; } void setPlaceholderColor(const Color& color) { m_placeholderColor = color; } void setPlaceholderAlign(Fw::AlignmentFlag align) { m_placeholderAlign = align; } void setPlaceholderFont(const std::string& fontName);
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
void selectAll() { setSelection(0, m_text.length());
```
```cpp
void clearSelection() { setSelection(0, 0);
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
int getCursorPos() { return m_cursorPos; } Point getTextVirtualOffset() { return m_textVirtualOffset; } Size getTextVirtualSize() { return m_textVirtualSize; } Size getTextTotalSize() { return m_textTotalSize; } uint getMaxLength() { return m_maxLength; } int getSelectionStart() { return m_selectionStart; } int getSelectionEnd() { return m_selectionEnd; } Color getSelectionColor() { return m_selectionColor; } Color getSelectionBackgroundColor() { return m_selectionBackgroundColor; } bool hasSelection() { return m_selectionEnd - m_selectionStart > 0; } bool isCursorVisible() { return m_cursorVisible; } bool isTextHidden() { return m_textHidden; } bool isShiftNavigation() { return m_shiftNavigation; } bool isMultiline() { return m_multiline; } bool isEditable() { return m_editable; } bool isSelectable() { return m_selectable; } bool isAutoScrolling() { return m_autoScroll; } protected: void updateText();
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
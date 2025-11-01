---
title: "src/framework/ui/uitextedit.h"
source_file: "src/framework/ui/uitextedit.h"
generated_at: "2025-11-01T06:09:06.208Z"
doc_type: "cpp_api"
---

# src/framework/ui/uitextedit.h

(uitextedit)=
## `UITextEdit`

**Signature:**
```cpp
public: UITextEdit();
```

---

(drawself)=
## `drawSelf`

**Signature:**
```cpp
void drawSelf(Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::DrawPane` | `drawPane` | - |

---

(update)=
## `update`

**Signature:**
```cpp
private: void update(bool focusCursor = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `focusCursor` | `false` | - |

---

(setcursorpos)=
## `setCursorPos`

**Signature:**
```cpp
public: void setCursorPos(int pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `pos` | - |

---

(setselection)=
## `setSelection`

**Signature:**
```cpp
void setSelection(int start, int end);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `start` | - |
| `int` | `end` | - |

---

(settexthidden)=
## `setTextHidden`

**Signature:**
```cpp
void setTextHidden(bool hidden);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `hidden` | - |

---

(settextvirtualoffset)=
## `setTextVirtualOffset`

**Signature:**
```cpp
void setTextVirtualOffset(const Point& offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `offset` | - |

---

(setplaceholderfont)=
## `setPlaceholderFont`

**Signature:**
```cpp
void setPlaceholderFont(const std::string& fontName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fontName` | - |

---

(movecursorhorizontally)=
## `moveCursorHorizontally`

**Signature:**
```cpp
void moveCursorHorizontally(bool right);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `right` | - |

---

(movecursorvertically)=
## `moveCursorVertically`

**Signature:**
```cpp
void moveCursorVertically(bool up);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `up` | - |

---

(appendtext)=
## `appendText`

**Signature:**
```cpp
void appendText(std::string text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `text` | - |

---

(appendcharacter)=
## `appendCharacter`

**Signature:**
```cpp
void appendCharacter(char c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char` | `c` | - |

---

(removecharacter)=
## `removeCharacter`

**Signature:**
```cpp
void removeCharacter(bool right);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `right` | - |

---

(blinkcursor)=
## `blinkCursor`

**Signature:**
```cpp
void blinkCursor();
```

---

(del)=
## `del`

**Signature:**
```cpp
void del(bool right = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `right` | `false` | - |

---

(paste)=
## `paste`

**Signature:**
```cpp
void paste(const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |

---

(copy)=
## `copy`

**Signature:**
```cpp
std::string copy();
```

**Returns:**
- `std::string`

---

(cut)=
## `cut`

**Signature:**
```cpp
std::string cut();
```

**Returns:**
- `std::string`

---

(wraptext)=
## `wrapText`

**Signature:**
```cpp
void wrapText();
```

---

(getdisplayedtext)=
## `getDisplayedText`

**Signature:**
```cpp
std::string getDisplayedText();
```

**Returns:**
- `std::string`

---

(getselection)=
## `getSelection`

**Signature:**
```cpp
std::string getSelection();
```

**Returns:**
- `std::string`

---

(gettextpos)=
## `getTextPos`

**Signature:**
```cpp
int getTextPos(Point pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Point` | `pos` | - |

**Returns:**
- `int`

---

(updatetext)=
## `updateText`

**Signature:**
```cpp
protected: void updateText();
```

---

(onstyleapply)=
## `onStyleApply`

**Signature:**
```cpp
virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |
| `const OTMLNodePtr&` | `styleNode` | - |

---

(ongeometrychange)=
## `onGeometryChange`

**Signature:**
```cpp
virtual void onGeometryChange(const Rect& oldRect, const Rect& newRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `oldRect` | - |
| `const Rect&` | `newRect` | - |

---

(onfocuschange)=
## `onFocusChange`

**Signature:**
```cpp
virtual void onFocusChange(bool focused, Fw::FocusReason reason);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `focused` | - |
| `Fw::FocusReason` | `reason` | - |

---

(onkeytext)=
## `onKeyText`

**Signature:**
```cpp
virtual bool onKeyText(const std::string& keyText);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `keyText` | - |

**Returns:**
- `bool`

---

(onkeypress)=
## `onKeyPress`

**Signature:**
```cpp
virtual bool onKeyPress(uchar keyCode, int keyboardModifiers, int autoRepeatTicks);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar` | `keyCode` | - |
| `int` | `keyboardModifiers` | - |
| `int` | `autoRepeatTicks` | - |

**Returns:**
- `bool`

---

(onmousepress)=
## `onMousePress`

**Signature:**
```cpp
virtual bool onMousePress(const Point& mousePos, Fw::MouseButton button);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `Fw::MouseButton` | `button` | - |

**Returns:**
- `bool`

---

(onmouserelease)=
## `onMouseRelease`

**Signature:**
```cpp
virtual bool onMouseRelease(const Point& mousePos, Fw::MouseButton button);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `Fw::MouseButton` | `button` | - |

**Returns:**
- `bool`

---

(onmousemove)=
## `onMouseMove`

**Signature:**
```cpp
virtual bool onMouseMove(const Point& mousePos, const Point& mouseMoved);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `const Point&` | `mouseMoved` | - |

**Returns:**
- `bool`

---

(ondoubleclick)=
## `onDoubleClick`

**Signature:**
```cpp
virtual bool onDoubleClick(const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |

**Returns:**
- `bool`

---

(ontextareaupdate)=
## `onTextAreaUpdate`

**Signature:**
```cpp
virtual void onTextAreaUpdate(const Point& vitualOffset, const Size& virtualSize, const Size& totalSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `vitualOffset` | - |
| `const Size&` | `virtualSize` | - |
| `const Size&` | `totalSize` | - |

---

(setcursorvisible)=
## `setCursorVisible`

**Signature:**
```cpp
void setCursorVisible(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(setvalidcharacters)=
## `setValidCharacters`

**Signature:**
```cpp
void setValidCharacters(const std::string validCharacters);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string` | `validCharacters` | - |

---

(setshiftnavigation)=
## `setShiftNavigation`

**Signature:**
```cpp
void setShiftNavigation(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(setmultiline)=
## `setMultiline`

**Signature:**
```cpp
void setMultiline(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(setmaxlength)=
## `setMaxLength`

**Signature:**
```cpp
void setMaxLength(uint maxLength);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `maxLength` | - |

---

(seteditable)=
## `setEditable`

**Signature:**
```cpp
void setEditable(bool editable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `editable` | - |

---

(setselectable)=
## `setSelectable`

**Signature:**
```cpp
void setSelectable(bool selectable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `selectable` | - |

---

(setselectioncolor)=
## `setSelectionColor`

**Signature:**
```cpp
void setSelectionColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setselectionbackgroundcolor)=
## `setSelectionBackgroundColor`

**Signature:**
```cpp
void setSelectionBackgroundColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setautoscroll)=
## `setAutoScroll`

**Signature:**
```cpp
void setAutoScroll(bool autoScroll);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `autoScroll` | - |

---

(setautosubmit)=
## `setAutoSubmit`

**Signature:**
```cpp
void setAutoSubmit(bool autoSubmit);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `autoSubmit` | - |

---

(setplaceholder)=
## `setPlaceholder`

**Signature:**
```cpp
void setPlaceholder(std::string placeholder);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `placeholder` | - |

---

(setplaceholdercolor)=
## `setPlaceholderColor`

**Signature:**
```cpp
void setPlaceholderColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setplaceholderalign)=
## `setPlaceholderAlign`

**Signature:**
```cpp
void setPlaceholderAlign(Fw::AlignmentFlag align);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AlignmentFlag` | `align` | - |

---

(selectall)=
## `selectAll`

**Signature:**
```cpp
void selectAll();
```

---

(clearselection)=
## `clearSelection`

**Signature:**
```cpp
void clearSelection();
```

---

(getcursorpos)=
## `getCursorPos`

**Signature:**
```cpp
int getCursorPos();
```

**Returns:**
- `int`

---

(gettextvirtualoffset)=
## `getTextVirtualOffset`

**Signature:**
```cpp
Point getTextVirtualOffset();
```

**Returns:**
- `Point`

---

(gettextvirtualsize)=
## `getTextVirtualSize`

**Signature:**
```cpp
Size getTextVirtualSize();
```

**Returns:**
- `Size`

---

(gettexttotalsize)=
## `getTextTotalSize`

**Signature:**
```cpp
Size getTextTotalSize();
```

**Returns:**
- `Size`

---

(getmaxlength)=
## `getMaxLength`

**Signature:**
```cpp
uint getMaxLength();
```

**Returns:**
- `uint`

---

(getselectionstart)=
## `getSelectionStart`

**Signature:**
```cpp
int getSelectionStart();
```

**Returns:**
- `int`

---

(getselectionend)=
## `getSelectionEnd`

**Signature:**
```cpp
int getSelectionEnd();
```

**Returns:**
- `int`

---

(getselectioncolor)=
## `getSelectionColor`

**Signature:**
```cpp
Color getSelectionColor();
```

**Returns:**
- `Color`

---

(getselectionbackgroundcolor)=
## `getSelectionBackgroundColor`

**Signature:**
```cpp
Color getSelectionBackgroundColor();
```

**Returns:**
- `Color`

---

(hasselection)=
## `hasSelection`

**Signature:**
```cpp
bool hasSelection();
```

**Returns:**
- `bool`

---

(iscursorvisible)=
## `isCursorVisible`

**Signature:**
```cpp
bool isCursorVisible();
```

**Returns:**
- `bool`

---

(istexthidden)=
## `isTextHidden`

**Signature:**
```cpp
bool isTextHidden();
```

**Returns:**
- `bool`

---

(isshiftnavigation)=
## `isShiftNavigation`

**Signature:**
```cpp
bool isShiftNavigation();
```

**Returns:**
- `bool`

---

(ismultiline)=
## `isMultiline`

**Signature:**
```cpp
bool isMultiline();
```

**Returns:**
- `bool`

---

(iseditable)=
## `isEditable`

**Signature:**
```cpp
bool isEditable();
```

**Returns:**
- `bool`

---

(isselectable)=
## `isSelectable`

**Signature:**
```cpp
bool isSelectable();
```

**Returns:**
- `bool`

---

(isautoscrolling)=
## `isAutoScrolling`

**Signature:**
```cpp
bool isAutoScrolling();
```

**Returns:**
- `bool`

---

(disableupdates)=
## `disableUpdates`

**Signature:**
```cpp
private: void disableUpdates();
```

---

(enableupdates)=
## `enableUpdates`

**Signature:**
```cpp
void enableUpdates();
```

---

(recacheglyphs)=
## `recacheGlyphs`

**Signature:**
```cpp
void recacheGlyphs();
```

---

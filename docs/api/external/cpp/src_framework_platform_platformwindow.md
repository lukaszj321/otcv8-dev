---
title: "src/framework/platform/platformwindow.h"
source_file: "src/framework/platform/platformwindow.h"
generated_at: "2025-10-31T23:33:30.353Z"
doc_type: "cpp_api"
---

# src/framework/platform/platformwindow.h

(init)=
## `init`

**Signature:**
```cpp
public: virtual void init();
```

**Returns:**
- `public: virtual void`

---

(terminate)=
## `terminate`

**Signature:**
```cpp
virtual void terminate();
```

**Returns:**
- `virtual void`

---

(move)=
## `move`

**Signature:**
```cpp
virtual void move(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

**Returns:**
- `virtual void`

---

(resize)=
## `resize`

**Signature:**
```cpp
virtual void resize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

**Returns:**
- `virtual void`

---

(show)=
## `show`

**Signature:**
```cpp
virtual void show();
```

**Returns:**
- `virtual void`

---

(hide)=
## `hide`

**Signature:**
```cpp
virtual void hide();
```

**Returns:**
- `virtual void`

---

(minimize)=
## `minimize`

**Signature:**
```cpp
virtual void minimize();
```

**Returns:**
- `virtual void`

---

(maximize)=
## `maximize`

**Signature:**
```cpp
virtual void maximize();
```

**Returns:**
- `virtual void`

---

(poll)=
## `poll`

**Signature:**
```cpp
virtual void poll();
```

**Returns:**
- `virtual void`

---

(swapbuffers)=
## `swapBuffers`

**Signature:**
```cpp
virtual void swapBuffers();
```

**Returns:**
- `virtual void`

---

(showmouse)=
## `showMouse`

**Signature:**
```cpp
virtual void showMouse();
```

**Returns:**
- `virtual void`

---

(hidemouse)=
## `hideMouse`

**Signature:**
```cpp
virtual void hideMouse();
```

**Returns:**
- `virtual void`

---

(loadmousecursor)=
## `loadMouseCursor`

**Signature:**
```cpp
int loadMouseCursor(const std::string& file, const Point& hotSpot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |
| `const Point&` | `hotSpot` | - |

**Returns:**
- `int`

---

(setmousecursor)=
## `setMouseCursor`

**Signature:**
```cpp
virtual void setMouseCursor(int cursorId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `cursorId` | - |

**Returns:**
- `virtual void`

---

(restoremousecursor)=
## `restoreMouseCursor`

**Signature:**
```cpp
virtual void restoreMouseCursor();
```

**Returns:**
- `virtual void`

---

(settitle)=
## `setTitle`

**Signature:**
```cpp
virtual void setTitle(const std::string& title);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `title` | - |

**Returns:**
- `virtual void`

---

(setminimumsize)=
## `setMinimumSize`

**Signature:**
```cpp
virtual void setMinimumSize(const Size& minimumSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `minimumSize` | - |

**Returns:**
- `virtual void`

---

(setfullscreen)=
## `setFullscreen`

**Signature:**
```cpp
virtual void setFullscreen(bool fullscreen);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `fullscreen` | - |

**Returns:**
- `virtual void`

---

(setverticalsync)=
## `setVerticalSync`

**Signature:**
```cpp
virtual void setVerticalSync(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

**Returns:**
- `virtual void`

---

(seticon)=
## `setIcon`

**Signature:**
```cpp
virtual void setIcon(const std::string& iconFile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `iconFile` | - |

**Returns:**
- `virtual void`

---

(setclipboardtext)=
## `setClipboardText`

**Signature:**
```cpp
virtual void setClipboardText(const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |

**Returns:**
- `virtual void`

---

(getdisplaysize)=
## `getDisplaySize`

**Signature:**
```cpp
virtual Size getDisplaySize();
```

**Returns:**
- `virtual Size`

---

(getclipboardtext)=
## `getClipboardText`

**Signature:**
```cpp
virtual std::string getClipboardText();
```

**Returns:**
- `virtual std::string`

---

(getplatformtype)=
## `getPlatformType`

**Signature:**
```cpp
virtual std::string getPlatformType();
```

**Returns:**
- `virtual std::string`

---

(flash)=
## `flash`

**Signature:**
```cpp
virtual void flash();
```

**Returns:**
- `virtual void`

---

(internalloadmousecursor)=
## `internalLoadMouseCursor`

**Signature:**
```cpp
protected: virtual int internalLoadMouseCursor(const ImagePtr& image, const Point& hotSpot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ImagePtr&` | `image` | - |
| `const Point&` | `hotSpot` | - |

**Returns:**
- `protected: virtual int`

---

(updateunmaximizedcoords)=
## `updateUnmaximizedCoords`

**Signature:**
```cpp
void updateUnmaximizedCoords();
```

---

(processkeydown)=
## `processKeyDown`

**Signature:**
```cpp
void processKeyDown(Fw::Key keyCode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::Key` | `keyCode` | - |

---

(processkeyup)=
## `processKeyUp`

**Signature:**
```cpp
void processKeyUp(Fw::Key keyCode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::Key` | `keyCode` | - |

---

(releaseallkeys)=
## `releaseAllKeys`

**Signature:**
```cpp
void releaseAllKeys();
```

---

(firekeyspress)=
## `fireKeysPress`

**Signature:**
```cpp
void fireKeysPress();
```

---

(displayfatalerror)=
## `displayFatalError`

**Signature:**
```cpp
virtual void displayFatalError(const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `message` | - |

**Returns:**
- `virtual void`

---

(hasverticalsync)=
## `hasVerticalSync`

**Signature:**
```cpp
bool hasVerticalSync();
```

**Returns:**
- `bool`

---

(getdisplaywidth)=
## `getDisplayWidth`

**Signature:**
```cpp
int getDisplayWidth();
```

**Returns:**
- `int`

---

(getdisplayheight)=
## `getDisplayHeight`

**Signature:**
```cpp
int getDisplayHeight();
```

**Returns:**
- `int`

---

(getunmaximizedsize)=
## `getUnmaximizedSize`

**Signature:**
```cpp
Size getUnmaximizedSize();
```

**Returns:**
- `Size`

---

(getsize)=
## `getSize`

**Signature:**
```cpp
Size getSize();
```

**Returns:**
- `Size`

---

(getminimumsize)=
## `getMinimumSize`

**Signature:**
```cpp
Size getMinimumSize();
```

**Returns:**
- `Size`

---

(getwidth)=
## `getWidth`

**Signature:**
```cpp
int getWidth();
```

**Returns:**
- `int`

---

(getheight)=
## `getHeight`

**Signature:**
```cpp
int getHeight();
```

**Returns:**
- `int`

---

(getunmaximizedpos)=
## `getUnmaximizedPos`

**Signature:**
```cpp
Point getUnmaximizedPos();
```

**Returns:**
- `Point`

---

(getposition)=
## `getPosition`

**Signature:**
```cpp
Point getPosition();
```

**Returns:**
- `Point`

---

(getx)=
## `getX`

**Signature:**
```cpp
int getX();
```

**Returns:**
- `int`

---

(gety)=
## `getY`

**Signature:**
```cpp
int getY();
```

**Returns:**
- `int`

---

(getmouseposition)=
## `getMousePosition`

**Signature:**
```cpp
Point getMousePosition();
```

**Returns:**
- `Point`

---

(getkeyboardmodifiers)=
## `getKeyboardModifiers`

**Signature:**
```cpp
int getKeyboardModifiers();
```

**Returns:**
- `int`

---

(iskeypressed)=
## `isKeyPressed`

**Signature:**
```cpp
bool isKeyPressed(Fw::Key keyCode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::Key` | `keyCode` | - |

**Returns:**
- `bool`

---

(ismousebuttonpressed)=
## `isMouseButtonPressed`

**Signature:**
```cpp
bool isMouseButtonPressed(Fw::MouseButton mouseButton);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::MouseButton` | `mouseButton` | - |

**Returns:**
- `bool`

---

(isvisible)=
## `isVisible`

**Signature:**
```cpp
bool isVisible();
```

**Returns:**
- `bool`

---

(ismaximized)=
## `isMaximized`

**Signature:**
```cpp
bool isMaximized();
```

**Returns:**
- `bool`

---

(isfullscreen)=
## `isFullscreen`

**Signature:**
```cpp
bool isFullscreen();
```

**Returns:**
- `bool`

---

(hasfocus)=
## `hasFocus`

**Signature:**
```cpp
bool hasFocus();
```

**Returns:**
- `bool`

---

(setonclose)=
## `setOnClose`

**Signature:**
```cpp
void setOnClose(const std::function<void()>& onClose);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::function&lt;void()&gt;&` | `onClose` | - |

---

(setonresize)=
## `setOnResize`

**Signature:**
```cpp
void setOnResize(const OnResizeCallback& onResize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OnResizeCallback&` | `onResize` | - |

---

(setoninputevent)=
## `setOnInputEvent`

**Signature:**
```cpp
void setOnInputEvent(const OnInputEventCallback& onInputEvent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OnInputEventCallback&` | `onInputEvent` | - |

---

(showtexteditor)=
## `showTextEditor`

**Signature:**
```cpp
virtual void showTextEditor(const std::string& title, const std::string& description, const std::string& text, int flags);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `title` | - |
| `const std::string&` | `description` | - |
| `const std::string&` | `text` | - |
| `int` | `flags` | - |

**Returns:**
- `virtual void`

---

(handletextinput)=
## `handleTextInput`

**Signature:**
```cpp
virtual void handleTextInput(std::string text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `text` | - |

**Returns:**
- `virtual void`

---

(setscaling)=
## `setScaling`

**Signature:**
```cpp
void setScaling(float scaling);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `scaling` | - |

---

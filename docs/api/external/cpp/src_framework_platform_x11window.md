---
title: "src/framework/platform/x11window.h"
source_file: "src/framework/platform/x11window.h"
generated_at: "2025-11-01T08:19:49.461Z"
doc_type: "cpp_api"
---

# src/framework/platform/x11window.h

(internalopendisplay)=
## `internalOpenDisplay`

**Signature:**
```cpp
void internalOpenDisplay();
```

---

(internalcreatewindow)=
## `internalCreateWindow`

**Signature:**
```cpp
void internalCreateWindow();
```

---

(internalsetupwindowinput)=
## `internalSetupWindowInput`

**Signature:**
```cpp
bool internalSetupWindowInput();
```

**Returns:**
- `bool`

---

(internalcheckgl)=
## `internalCheckGL`

**Signature:**
```cpp
void internalCheckGL();
```

---

(internalchooseglvisual)=
## `internalChooseGLVisual`

**Signature:**
```cpp
void internalChooseGLVisual();
```

---

(internalcreateglcontext)=
## `internalCreateGLContext`

**Signature:**
```cpp
void internalCreateGLContext();
```

---

(internaldestroyglcontext)=
## `internalDestroyGLContext`

**Signature:**
```cpp
void internalDestroyGLContext();
```

---

(internalconnectglcontext)=
## `internalConnectGLContext`

**Signature:**
```cpp
void internalConnectGLContext();
```

---

(isextensionsupported)=
## `isExtensionSupported`

**Signature:**
```cpp
bool isExtensionSupported(const char *ext);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *ext` | - | - |

**Returns:**
- `bool`

---

(x11window)=
## `X11Window`

**Signature:**
```cpp
public: X11Window();
```

---

(init)=
## `init`

**Signature:**
```cpp
void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(move)=
## `move`

**Signature:**
```cpp
void move(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(resize)=
## `resize`

**Signature:**
```cpp
void resize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(show)=
## `show`

**Signature:**
```cpp
void show();
```

---

(hide)=
## `hide`

**Signature:**
```cpp
void hide();
```

---

(minimize)=
## `minimize`

**Signature:**
```cpp
void minimize();
```

---

(maximize)=
## `maximize`

**Signature:**
```cpp
void maximize();
```

---

(poll)=
## `poll`

**Signature:**
```cpp
void poll();
```

---

(swapbuffers)=
## `swapBuffers`

**Signature:**
```cpp
void swapBuffers();
```

---

(showmouse)=
## `showMouse`

**Signature:**
```cpp
void showMouse();
```

---

(hidemouse)=
## `hideMouse`

**Signature:**
```cpp
void hideMouse();
```

---

(setmousecursor)=
## `setMouseCursor`

**Signature:**
```cpp
void setMouseCursor(int cursorId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `cursorId` | - |

---

(restoremousecursor)=
## `restoreMouseCursor`

**Signature:**
```cpp
void restoreMouseCursor();
```

---

(settitle)=
## `setTitle`

**Signature:**
```cpp
void setTitle(const std::string& title);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `title` | - |

---

(setminimumsize)=
## `setMinimumSize`

**Signature:**
```cpp
void setMinimumSize(const Size& minimumSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `minimumSize` | - |

---

(setfullscreen)=
## `setFullscreen`

**Signature:**
```cpp
void setFullscreen(bool fullscreen);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `fullscreen` | - |

---

(setverticalsync)=
## `setVerticalSync`

**Signature:**
```cpp
void setVerticalSync(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(seticon)=
## `setIcon`

**Signature:**
```cpp
void setIcon(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(setclipboardtext)=
## `setClipboardText`

**Signature:**
```cpp
void setClipboardText(const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |

---

(getdisplaysize)=
## `getDisplaySize`

**Signature:**
```cpp
Size getDisplaySize();
```

**Returns:**
- `Size`

---

(getclipboardtext)=
## `getClipboardText`

**Signature:**
```cpp
std::string getClipboardText();
```

**Returns:**
- `std::string`

---

(getplatformtype)=
## `getPlatformType`

**Signature:**
```cpp
std::string getPlatformType();
```

**Returns:**
- `std::string`

---

(displayfatalerror)=
## `displayFatalError`

**Signature:**
```cpp
void displayFatalError(const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `message` | - |

---

(internalloadmousecursor)=
## `internalLoadMouseCursor`

**Signature:**
```cpp
protected: int internalLoadMouseCursor(const ImagePtr& image, const Point& hotSpot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ImagePtr&` | `image` | - |
| `const Point&` | `hotSpot` | - |

**Returns:**
- `int`

---

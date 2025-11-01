---
title: "src/framework/platform/win32window.h"
source_file: "src/framework/platform/win32window.h"
generated_at: "2025-11-01T08:45:15.316Z"
doc_type: "cpp_api"
---

# src/framework/platform/win32window.h

(internalsetuptimeraccuracy)=
## `internalSetupTimerAccuracy`

**Signature:**
```cpp
void internalSetupTimerAccuracy();
```

---

(internalcreatewindow)=
## `internalCreateWindow`

**Signature:**
```cpp
void internalCreateWindow();
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

(internalrestoreglcontext)=
## `internalRestoreGLContext`

**Signature:**
```cpp
void internalRestoreGLContext();
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

(windowproc)=
## `windowProc`

**Signature:**
```cpp
LRESULT windowProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `HWND` | `hWnd` | - |
| `UINT` | `uMsg` | - |
| `WPARAM` | `wParam` | - |
| `LPARAM` | `lParam` | - |

**Returns:**
- `LRESULT`

---

(dispatcherwindowproc)=
## `dispatcherWindowProc`

**Signature:**
```cpp
LRESULT dispatcherWindowProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `HWND` | `hWnd` | - |
| `UINT` | `uMsg` | - |
| `WPARAM` | `wParam` | - |
| `LPARAM` | `lParam` | - |

**Returns:**
- `LRESULT`

---

(retranslatevirtualkey)=
## `retranslateVirtualKey`

**Signature:**
```cpp
Fw::Key retranslateVirtualKey(WPARAM wParam, LPARAM lParam);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `WPARAM` | `wParam` | - |
| `LPARAM` | `lParam` | - |

**Returns:**
- `Fw::Key`

---

(win32window)=
## `WIN32Window`

**Signature:**
```cpp
public: WIN32Window();
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

(getclientrect)=
## `getClientRect`

**Signature:**
```cpp
private: Rect getClientRect();
```

**Returns:**
- `Rect`

---

(getwindowrect)=
## `getWindowRect`

**Signature:**
```cpp
Rect getWindowRect();
```

**Returns:**
- `Rect`

---

(adjustwindowrect)=
## `adjustWindowRect`

**Signature:**
```cpp
Rect adjustWindowRect(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

**Returns:**
- `Rect`


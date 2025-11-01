---
title: "src/framework/platform/androidwindow.h"
source_file: "src/framework/platform/androidwindow.h"
generated_at: "2025-11-01T04:06:42.764Z"
doc_type: "cpp_api"
---

# src/framework/platform/androidwindow.h

(internalinitgl)=
## `internalInitGL`

**Signature:**
```cpp
void internalInitGL();
```

---

(internaldestroygl)=
## `internalDestroyGL`

**Signature:**
```cpp
void internalDestroyGL();
```

---

(internalcheckgl)=
## `internalCheckGL`

**Signature:**
```cpp
void internalCheckGL();
```

---

(internalchoosegl)=
## `internalChooseGL`

**Signature:**
```cpp
void internalChooseGL();
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

(androidwindow)=
## `AndroidWindow`

**Signature:**
```cpp
public: AndroidWindow();
```

---

(init)=
## `init`

**Signature:**
```cpp
void init();
```

---

(init-1)=
## `init`

**Signature:**
```cpp
void init(struct android_app* app);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `struct android_app*` | `app` | - |

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
void setIcon(const std::string& iconFile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `iconFile` | - |

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

(handlecmd)=
## `handleCmd`

**Signature:**
```cpp
void handleCmd(int32_t cmd);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int32_t` | `cmd` | - |

---

(handleinput)=
## `handleInput`

**Signature:**
```cpp
int handleInput(AInputEvent* event);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `AInputEvent*` | `event` | - |

**Returns:**
- `int`

---

(updatesize)=
## `updateSize`

**Signature:**
```cpp
void updateSize();
```

---

(handletextinput)=
## `handleTextInput`

**Signature:**
```cpp
void handleTextInput(std::string text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `text` | - |

---

(openurl)=
## `openUrl`

**Signature:**
```cpp
void openUrl(std::string url);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `url` | - |

---

(getjnienv)=
## `getJNIEnv`

**Signature:**
```cpp
JNIEnv* getJNIEnv();
```

**Returns:**
- `JNIEnv*`

---

(getjavavm)=
## `getJavaVM`

**Signature:**
```cpp
JavaVM* getJavaVM();
```

**Returns:**
- `JavaVM*`

---

(getclazz)=
## `getClazz`

**Signature:**
```cpp
jobject getClazz();
```

**Returns:**
- `jobject`

---

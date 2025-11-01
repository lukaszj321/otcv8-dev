---
title: "src/framework/core/graphicalapplication.h"
source_file: "src/framework/core/graphicalapplication.h"
generated_at: "2025-11-01T08:45:15.296Z"
doc_type: "cpp_api"
---

# src/framework/core/graphicalapplication.h

(init)=
## `init`

**Signature:**
```cpp
public: void init(std::vector<std::string>& args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::vector&lt;std::string&gt;&` | `args` | - |

---

(deinit)=
## `deinit`

**Signature:**
```cpp
void deinit();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(run)=
## `run`

**Signature:**
```cpp
void run();
```

---

(poll)=
## `poll`

**Signature:**
```cpp
void poll();
```

---

(pollgraphics)=
## `pollGraphics`

**Signature:**
```cpp
void pollGraphics();
```

---

(close)=
## `close`

**Signature:**
```cpp
void close();
```

---

(doscreenshot)=
## `doScreenshot`

**Signature:**
```cpp
void doScreenshot(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

---

(scaleup)=
## `scaleUp`

**Signature:**
```cpp
void scaleUp();
```

---

(scaledown)=
## `scaleDown`

**Signature:**
```cpp
void scaleDown();
```

---

(scale)=
## `scale`

**Signature:**
```cpp
void scale(float value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `value` | - |

---

(setsmooth)=
## `setSmooth`

**Signature:**
```cpp
void setSmooth(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(domapscreenshot)=
## `doMapScreenshot`

**Signature:**
```cpp
void doMapScreenshot(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(resize)=
## `resize`

**Signature:**
```cpp
protected: void resize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(inputevent)=
## `inputEvent`

**Signature:**
```cpp
void inputEvent(InputEvent event);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `InputEvent` | `event` | - |

---

(willrepaint)=
## `willRepaint`

**Signature:**
```cpp
bool willRepaint();
```

**Returns:**
- `bool`

---

(repaint)=
## `repaint`

**Signature:**
```cpp
void repaint();
```

---

(setmaxfps)=
## `setMaxFps`

**Signature:**
```cpp
void setMaxFps(int maxFps);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `maxFps` | - |

---

(getmaxfps)=
## `getMaxFps`

**Signature:**
```cpp
int getMaxFps();
```

**Returns:**
- `int`

---

(getfps)=
## `getFps`

**Signature:**
```cpp
int getFps();
```

**Returns:**
- `int`

---

(getgraphicsfps)=
## `getGraphicsFps`

**Signature:**
```cpp
int getGraphicsFps();
```

**Returns:**
- `int`

---

(getprocessingfps)=
## `getProcessingFps`

**Signature:**
```cpp
int getProcessingFps();
```

**Returns:**
- `int`

---

(isoninputevent)=
## `isOnInputEvent`

**Signature:**
```cpp
bool isOnInputEvent();
```

**Returns:**
- `bool`

---

(getiteration)=
## `getIteration`

**Signature:**
```cpp
int getIteration();
```

**Returns:**
- `int`

---

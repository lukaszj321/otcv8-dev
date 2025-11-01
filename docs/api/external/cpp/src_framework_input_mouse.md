---
title: "src/framework/input/mouse.h"
source_file: "src/framework/input/mouse.h"
generated_at: "2025-11-01T00:11:49.047Z"
doc_type: "cpp_api"
---

# src/framework/input/mouse.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(loadcursors)=
## `loadCursors`

**Signature:**
```cpp
void loadCursors(std::string filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `filename` | - |

---

(addcursor)=
## `addCursor`

**Signature:**
```cpp
void addCursor(const std::string& name, const std::string& file, const Point& hotSpot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `const std::string&` | `file` | - |
| `const Point&` | `hotSpot` | - |

---

(pushcursor)=
## `pushCursor`

**Signature:**
```cpp
void pushCursor(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(popcursor)=
## `popCursor`

**Signature:**
```cpp
void popCursor(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(iscursorchanged)=
## `isCursorChanged`

**Signature:**
```cpp
bool isCursorChanged();
```

**Returns:**
- `bool`

---

(ispressed)=
## `isPressed`

**Signature:**
```cpp
bool isPressed(Fw::MouseButton mouseButton);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::MouseButton` | `mouseButton` | - |

**Returns:**
- `bool`

---

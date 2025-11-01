---
title: "src/client/uiitem.h"
source_file: "src/client/uiitem.h"
generated_at: "2025-11-01T04:06:42.735Z"
doc_type: "cpp_api"
---

# src/client/uiitem.h

(uiitem)=
## `UIItem`

**Signature:**
```cpp
public: UIItem();
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

(setitemid)=
## `setItemId`

**Signature:**
```cpp
void setItemId(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

---

(setitemcount)=
## `setItemCount`

**Signature:**
```cpp
void setItemCount(int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `count` | - |

---

(setitemsubtype)=
## `setItemSubType`

**Signature:**
```cpp
void setItemSubType(int subType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `subType` | - |

---

(setitem)=
## `setItem`

**Signature:**
```cpp
void setItem(const ItemPtr& item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |

---

(setitemshader)=
## `setItemShader`

**Signature:**
```cpp
void setItemShader(const std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |

---

(onstyleapply)=
## `onStyleApply`

**Signature:**
```cpp
protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |
| `const OTMLNodePtr&` | `styleNode` | - |

---

(cachecounttext)=
## `cacheCountText`

**Signature:**
```cpp
void cacheCountText();
```

---

(setitemvisible)=
## `setItemVisible`

**Signature:**
```cpp
void setItemVisible(bool visible);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `visible` | - |

---

(setvirtual)=
## `setVirtual`

**Signature:**
```cpp
void setVirtual(bool virt);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `virt` | - |

---

(clearitem)=
## `clearItem`

**Signature:**
```cpp
void clearItem();
```

---

(setshowcount)=
## `setShowCount`

**Signature:**
```cpp
void setShowCount(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(getitemid)=
## `getItemId`

**Signature:**
```cpp
int getItemId();
```

**Returns:**
- `int`

---

(getitemcount)=
## `getItemCount`

**Signature:**
```cpp
int getItemCount();
```

**Returns:**
- `int`

---

(getitemsubtype)=
## `getItemSubType`

**Signature:**
```cpp
int getItemSubType();
```

**Returns:**
- `int`

---

(getitemcountorsubtype)=
## `getItemCountOrSubType`

**Signature:**
```cpp
int getItemCountOrSubType();
```

**Returns:**
- `int`

---

(getitem)=
## `getItem`

**Signature:**
```cpp
ItemPtr getItem();
```

**Returns:**
- `ItemPtr`

---

(isvirtual)=
## `isVirtual`

**Signature:**
```cpp
bool isVirtual();
```

**Returns:**
- `bool`

---

(isitemvisible)=
## `isItemVisible`

**Signature:**
```cpp
bool isItemVisible();
```

**Returns:**
- `bool`

---

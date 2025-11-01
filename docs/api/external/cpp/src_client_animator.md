---
title: "src/client/animator.h"
source_file: "src/client/animator.h"
generated_at: "2025-11-01T08:29:23.672Z"
doc_type: "cpp_api"
---

# src/client/animator.h

(animator)=
## `Animator`

**Signature:**
```cpp
public: Animator();
```

---

(unserialize)=
## `unserialize`

**Signature:**
```cpp
void unserialize(int animationPhases, const FileStreamPtr& fin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `animationPhases` | - |
| `const FileStreamPtr&` | `fin` | - |

---

(serialize)=
## `serialize`

**Signature:**
```cpp
void serialize(const FileStreamPtr& fin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FileStreamPtr&` | `fin` | - |

---

(setphase)=
## `setPhase`

**Signature:**
```cpp
void setPhase(int phase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `phase` | - |

---

(getphase)=
## `getPhase`

**Signature:**
```cpp
int getPhase();
```

**Returns:**
- `int`

---

(getphaseat)=
## `getPhaseAt`

**Signature:**
```cpp
int getPhaseAt(Timer& timer, int lastPhase = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `Timer&` | `timer` |  | - |
| `int` | `lastPhase` | `0` | - |

**Returns:**
- `int`

---

(getstartphase)=
## `getStartPhase`

**Signature:**
```cpp
int getStartPhase();
```

**Returns:**
- `int`

---

(gettotalduration)=
## `getTotalDuration`

**Signature:**
```cpp
ticks_t getTotalDuration();
```

**Returns:**
- `ticks_t`

---

(resetanimation)=
## `resetAnimation`

**Signature:**
```cpp
void resetAnimation();
```

---

(getpingpongphase)=
## `getPingPongPhase`

**Signature:**
```cpp
private: int getPingPongPhase();
```

**Returns:**
- `int`

---

(getloopphase)=
## `getLoopPhase`

**Signature:**
```cpp
int getLoopPhase();
```

**Returns:**
- `int`

---

(getphaseduration)=
## `getPhaseDuration`

**Signature:**
```cpp
int getPhaseDuration(int phase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `phase` | - |

**Returns:**
- `int`

---

(calculatesynchronous)=
## `calculateSynchronous`

**Signature:**
```cpp
void calculateSynchronous();
```

---

(getanimationphases)=
## `getAnimationPhases`

**Signature:**
```cpp
int getAnimationPhases();
```

**Returns:**
- `int`

---

(isasync)=
## `isAsync`

**Signature:**
```cpp
bool isAsync();
```

**Returns:**
- `bool`

---

(iscomplete)=
## `isComplete`

**Signature:**
```cpp
bool isComplete();
```

**Returns:**
- `bool`

---

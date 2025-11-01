---
title: "src/framework/ui/uiwidget.h"
source_file: "src/framework/ui/uiwidget.h"
generated_at: "2025-11-01T08:29:23.725Z"
doc_type: "cpp_api"
---

# src/framework/ui/uiwidget.h

(uiwidget)=
## `UIWidget`

**Signature:**
```cpp
public: UIWidget();
```

---

(draw)=
## `draw`

**Signature:**
```cpp
virtual void draw(const Rect& visibleRect, Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `visibleRect` | - |
| `Fw::DrawPane` | `drawPane` | - |

---

(drawself)=
## `drawSelf`

**Signature:**
```cpp
protected: virtual void drawSelf(Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::DrawPane` | `drawPane` | - |

---

(drawchildren)=
## `drawChildren`

**Signature:**
```cpp
virtual void drawChildren(const Rect& visibleRect, Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `visibleRect` | - |
| `Fw::DrawPane` | `drawPane` | - |

---

(addchild)=
## `addChild`

**Signature:**
```cpp
public: void addChild(const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |

---

(onchildidchange)=
## `onChildIdChange`

**Signature:**
```cpp
void onChildIdChange(const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |

---

(insertchild)=
## `insertChild`

**Signature:**
```cpp
void insertChild(int index, const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `const UIWidgetPtr&` | `child` | - |

---

(removechild)=
## `removeChild`

**Signature:**
```cpp
void removeChild(UIWidgetPtr child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `child` | - |

---

(focuschild)=
## `focusChild`

**Signature:**
```cpp
void focusChild(const UIWidgetPtr& child, Fw::FocusReason reason);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |
| `Fw::FocusReason` | `reason` | - |

---

(focusnextchild)=
## `focusNextChild`

**Signature:**
```cpp
void focusNextChild(Fw::FocusReason reason, bool rotate = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `Fw::FocusReason` | `reason` |  | - |
| `bool` | `rotate` | `false` | - |

---

(focuspreviouschild)=
## `focusPreviousChild`

**Signature:**
```cpp
void focusPreviousChild(Fw::FocusReason reason, bool rotate = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `Fw::FocusReason` | `reason` |  | - |
| `bool` | `rotate` | `false` | - |

---

(lowerchild)=
## `lowerChild`

**Signature:**
```cpp
void lowerChild(UIWidgetPtr child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `child` | - |

---

(raisechild)=
## `raiseChild`

**Signature:**
```cpp
void raiseChild(UIWidgetPtr child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `child` | - |

---

(movechildtoindex)=
## `moveChildToIndex`

**Signature:**
```cpp
void moveChildToIndex(const UIWidgetPtr& child, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |
| `int` | `index` | - |

---

(reorderchildren)=
## `reorderChildren`

**Signature:**
```cpp
void reorderChildren(const std::vector<UIWidgetPtr>& childrens);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;UIWidgetPtr&gt;&` | `childrens` | - |

---

(lockchild)=
## `lockChild`

**Signature:**
```cpp
void lockChild(const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |

---

(unlockchild)=
## `unlockChild`

**Signature:**
```cpp
void unlockChild(const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |

---

(mergestyle)=
## `mergeStyle`

**Signature:**
```cpp
void mergeStyle(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

---

(applystyle)=
## `applyStyle`

**Signature:**
```cpp
void applyStyle(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

---

(addanchor)=
## `addAnchor`

**Signature:**
```cpp
void addAnchor(Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AnchorEdge` | `anchoredEdge` | - |
| `const std::string&` | `hookedWidgetId` | - |
| `Fw::AnchorEdge` | `hookedEdge` | - |

---

(removeanchor)=
## `removeAnchor`

**Signature:**
```cpp
void removeAnchor(Fw::AnchorEdge anchoredEdge);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AnchorEdge` | `anchoredEdge` | - |

---

(fill)=
## `fill`

**Signature:**
```cpp
void fill(const std::string& hookedWidgetId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `hookedWidgetId` | - |

---

(centerin)=
## `centerIn`

**Signature:**
```cpp
void centerIn(const std::string& hookedWidgetId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `hookedWidgetId` | - |

---

(breakanchors)=
## `breakAnchors`

**Signature:**
```cpp
void breakAnchors();
```

---

(updateparentlayout)=
## `updateParentLayout`

**Signature:**
```cpp
void updateParentLayout();
```

---

(updatelayout)=
## `updateLayout`

**Signature:**
```cpp
void updateLayout();
```

---

(lock)=
## `lock`

**Signature:**
```cpp
void lock();
```

---

(unlock)=
## `unlock`

**Signature:**
```cpp
void unlock();
```

---

(focus)=
## `focus`

**Signature:**
```cpp
void focus();
```

---

(recursivefocus)=
## `recursiveFocus`

**Signature:**
```cpp
void recursiveFocus(Fw::FocusReason reason);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::FocusReason` | `reason` | - |

---

(lower)=
## `lower`

**Signature:**
```cpp
void lower();
```

---

(raise)=
## `raise`

**Signature:**
```cpp
void raise();
```

---

(grabmouse)=
## `grabMouse`

**Signature:**
```cpp
void grabMouse();
```

---

(ungrabmouse)=
## `ungrabMouse`

**Signature:**
```cpp
void ungrabMouse();
```

---

(grabkeyboard)=
## `grabKeyboard`

**Signature:**
```cpp
void grabKeyboard();
```

---

(ungrabkeyboard)=
## `ungrabKeyboard`

**Signature:**
```cpp
void ungrabKeyboard();
```

---

(bindrecttoparent)=
## `bindRectToParent`

**Signature:**
```cpp
void bindRectToParent();
```

---

(destroy)=
## `destroy`

**Signature:**
```cpp
void destroy();
```

---

(destroychildren)=
## `destroyChildren`

**Signature:**
```cpp
void destroyChildren();
```

---

(setid)=
## `setId`

**Signature:**
```cpp
void setId(const std::string& id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `id` | - |

---

(setparent)=
## `setParent`

**Signature:**
```cpp
void setParent(const UIWidgetPtr& parent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `parent` | - |

---

(setlayout)=
## `setLayout`

**Signature:**
```cpp
void setLayout(const UILayoutPtr& layout);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UILayoutPtr&` | `layout` | - |

---

(setrect)=
## `setRect`

**Signature:**
```cpp
bool setRect(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

**Returns:**
- `bool`

---

(setstyle)=
## `setStyle`

**Signature:**
```cpp
void setStyle(const std::string& styleName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |

---

(setstylefromnode)=
## `setStyleFromNode`

**Signature:**
```cpp
void setStyleFromNode(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

---

(setenabled)=
## `setEnabled`

**Signature:**
```cpp
void setEnabled(bool enabled);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enabled` | - |

---

(setvisible)=
## `setVisible`

**Signature:**
```cpp
void setVisible(bool visible);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `visible` | - |

---

(setautodraw)=
## `setAutoDraw`

**Signature:**
```cpp
void setAutoDraw(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(seton)=
## `setOn`

**Signature:**
```cpp
void setOn(bool on);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `on` | - |

---

(setchecked)=
## `setChecked`

**Signature:**
```cpp
void setChecked(bool checked);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `checked` | - |

---

(setfocusable)=
## `setFocusable`

**Signature:**
```cpp
void setFocusable(bool focusable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `focusable` | - |

---

(setphantom)=
## `setPhantom`

**Signature:**
```cpp
void setPhantom(bool phantom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `phantom` | - |

---

(setdraggable)=
## `setDraggable`

**Signature:**
```cpp
void setDraggable(bool draggable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `draggable` | - |

---

(setfixedsize)=
## `setFixedSize`

**Signature:**
```cpp
void setFixedSize(bool fixed);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `fixed` | - |

---

(setlastfocusreason)=
## `setLastFocusReason`

**Signature:**
```cpp
void setLastFocusReason(Fw::FocusReason reason);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::FocusReason` | `reason` | - |

---

(setautofocuspolicy)=
## `setAutoFocusPolicy`

**Signature:**
```cpp
void setAutoFocusPolicy(Fw::AutoFocusPolicy policy);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AutoFocusPolicy` | `policy` | - |

---

(setvirtualoffset)=
## `setVirtualOffset`

**Signature:**
```cpp
void setVirtualOffset(const Point& offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `offset` | - |

---

(isanchored)=
## `isAnchored`

**Signature:**
```cpp
bool isAnchored();
```

**Returns:**
- `bool`

---

(ischildlocked)=
## `isChildLocked`

**Signature:**
```cpp
bool isChildLocked(const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |

**Returns:**
- `bool`

---

(haschild)=
## `hasChild`

**Signature:**
```cpp
bool hasChild(const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |

**Returns:**
- `bool`

---

(getchildindex)=
## `getChildIndex`

**Signature:**
```cpp
int getChildIndex(const UIWidgetPtr& child);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `child` | - |

**Returns:**
- `int`

---

(getpaddingrect)=
## `getPaddingRect`

**Signature:**
```cpp
Rect getPaddingRect();
```

**Returns:**
- `Rect`

---

(getmarginrect)=
## `getMarginRect`

**Signature:**
```cpp
Rect getMarginRect();
```

**Returns:**
- `Rect`

---

(getchildrenrect)=
## `getChildrenRect`

**Signature:**
```cpp
Rect getChildrenRect();
```

**Returns:**
- `Rect`

---

(getanchoredlayout)=
## `getAnchoredLayout`

**Signature:**
```cpp
UIAnchorLayoutPtr getAnchoredLayout();
```

**Returns:**
- `UIAnchorLayoutPtr`

---

(getrootparent)=
## `getRootParent`

**Signature:**
```cpp
UIWidgetPtr getRootParent();
```

**Returns:**
- `UIWidgetPtr`

---

(getchildafter)=
## `getChildAfter`

**Signature:**
```cpp
UIWidgetPtr getChildAfter(const UIWidgetPtr& relativeChild);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `relativeChild` | - |

**Returns:**
- `UIWidgetPtr`

---

(getchildbefore)=
## `getChildBefore`

**Signature:**
```cpp
UIWidgetPtr getChildBefore(const UIWidgetPtr& relativeChild);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `relativeChild` | - |

**Returns:**
- `UIWidgetPtr`

---

(getchildbyid)=
## `getChildById`

**Signature:**
```cpp
UIWidgetPtr getChildById(const std::string& childId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `childId` | - |

**Returns:**
- `UIWidgetPtr`

---

(getchildbypos)=
## `getChildByPos`

**Signature:**
```cpp
UIWidgetPtr getChildByPos(const Point& childPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `childPos` | - |

**Returns:**
- `UIWidgetPtr`

---

(getchildbyindex)=
## `getChildByIndex`

**Signature:**
```cpp
UIWidgetPtr getChildByIndex(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

**Returns:**
- `UIWidgetPtr`

---

(recursivegetchildbyid)=
## `recursiveGetChildById`

**Signature:**
```cpp
UIWidgetPtr recursiveGetChildById(const std::string& id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `id` | - |

**Returns:**
- `UIWidgetPtr`

---

(recursivegetchildbypos)=
## `recursiveGetChildByPos`

**Signature:**
```cpp
UIWidgetPtr recursiveGetChildByPos(const Point& childPos, bool wantsPhantom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `childPos` | - |
| `bool` | `wantsPhantom` | - |

**Returns:**
- `UIWidgetPtr`

---

(recursivegetchildren)=
## `recursiveGetChildren`

**Signature:**
```cpp
UIWidgetList recursiveGetChildren();
```

**Returns:**
- `UIWidgetList`

---

(recursivegetchildrenbypos)=
## `recursiveGetChildrenByPos`

**Signature:**
```cpp
UIWidgetList recursiveGetChildrenByPos(const Point& childPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `childPos` | - |

**Returns:**
- `UIWidgetList`

---

(recursivegetchildrenbymarginpos)=
## `recursiveGetChildrenByMarginPos`

**Signature:**
```cpp
UIWidgetList recursiveGetChildrenByMarginPos(const Point& childPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `childPos` | - |

**Returns:**
- `UIWidgetList`

---

(backwardsgetwidgetbyid)=
## `backwardsGetWidgetById`

**Signature:**
```cpp
UIWidgetPtr backwardsGetWidgetById(const std::string& id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `id` | - |

**Returns:**
- `UIWidgetPtr`

---

(setstate)=
## `setState`

**Signature:**
```cpp
protected: bool setState(Fw::WidgetState state, bool on);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::WidgetState` | `state` | - |
| `bool` | `on` | - |

**Returns:**
- `bool`

---

(hasstate)=
## `hasState`

**Signature:**
```cpp
bool hasState(Fw::WidgetState state);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::WidgetState` | `state` | - |

**Returns:**
- `bool`

---

(internaldestroy)=
## `internalDestroy`

**Signature:**
```cpp
private: void internalDestroy();
```

---

(updatestate)=
## `updateState`

**Signature:**
```cpp
void updateState(Fw::WidgetState state);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::WidgetState` | `state` | - |

---

(updatestates)=
## `updateStates`

**Signature:**
```cpp
void updateStates();
```

---

(updatechildrenindexstates)=
## `updateChildrenIndexStates`

**Signature:**
```cpp
void updateChildrenIndexStates();
```

---

(updatestyle)=
## `updateStyle`

**Signature:**
```cpp
void updateStyle();
```

---

(onstyleapply)=
## `onStyleApply`

**Signature:**
```cpp
protected: virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
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

(onlayoutupdate)=
## `onLayoutUpdate`

**Signature:**
```cpp
virtual void onLayoutUpdate();
```

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

(onchildfocuschange)=
## `onChildFocusChange`

**Signature:**
```cpp
virtual void onChildFocusChange(const UIWidgetPtr& focusedChild, const UIWidgetPtr& unfocusedChild, Fw::FocusReason reason);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `focusedChild` | - |
| `const UIWidgetPtr&` | `unfocusedChild` | - |
| `Fw::FocusReason` | `reason` | - |

---

(onhoverchange)=
## `onHoverChange`

**Signature:**
```cpp
virtual void onHoverChange(bool hovered);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `hovered` | - |

---

(onvisibilitychange)=
## `onVisibilityChange`

**Signature:**
```cpp
virtual void onVisibilityChange(bool visible);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `visible` | - |

---

(ondragenter)=
## `onDragEnter`

**Signature:**
```cpp
virtual bool onDragEnter(const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |

**Returns:**
- `bool`

---

(ondragleave)=
## `onDragLeave`

**Signature:**
```cpp
virtual bool onDragLeave(UIWidgetPtr droppedWidget, const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `droppedWidget` | - |
| `const Point&` | `mousePos` | - |

**Returns:**
- `bool`

---

(ondragmove)=
## `onDragMove`

**Signature:**
```cpp
virtual bool onDragMove(const Point& mousePos, const Point& mouseMoved);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `const Point&` | `mouseMoved` | - |

**Returns:**
- `bool`

---

(ondrop)=
## `onDrop`

**Signature:**
```cpp
virtual bool onDrop(UIWidgetPtr draggedWidget, const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `draggedWidget` | - |
| `const Point&` | `mousePos` | - |

**Returns:**
- `bool`

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

(onkeydown)=
## `onKeyDown`

**Signature:**
```cpp
virtual bool onKeyDown(uchar keyCode, int keyboardModifiers);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar` | `keyCode` | - |
| `int` | `keyboardModifiers` | - |

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

(onkeyup)=
## `onKeyUp`

**Signature:**
```cpp
virtual bool onKeyUp(uchar keyCode, int keyboardModifiers);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar` | `keyCode` | - |
| `int` | `keyboardModifiers` | - |

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

(onmousewheel)=
## `onMouseWheel`

**Signature:**
```cpp
virtual bool onMouseWheel(const Point& mousePos, Fw::MouseWheelDirection direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `Fw::MouseWheelDirection` | `direction` | - |

**Returns:**
- `bool`

---

(onclick)=
## `onClick`

**Signature:**
```cpp
virtual bool onClick(const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |

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

(propagateonkeytext)=
## `propagateOnKeyText`

**Signature:**
```cpp
bool propagateOnKeyText(const std::string& keyText);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `keyText` | - |

**Returns:**
- `bool`

---

(propagateonkeydown)=
## `propagateOnKeyDown`

**Signature:**
```cpp
bool propagateOnKeyDown(uchar keyCode, int keyboardModifiers);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar` | `keyCode` | - |
| `int` | `keyboardModifiers` | - |

**Returns:**
- `bool`

---

(propagateonkeypress)=
## `propagateOnKeyPress`

**Signature:**
```cpp
bool propagateOnKeyPress(uchar keyCode, int keyboardModifiers, int autoRepeatTicks);
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

(propagateonkeyup)=
## `propagateOnKeyUp`

**Signature:**
```cpp
bool propagateOnKeyUp(uchar keyCode, int keyboardModifiers);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar` | `keyCode` | - |
| `int` | `keyboardModifiers` | - |

**Returns:**
- `bool`

---

(propagateonmouseevent)=
## `propagateOnMouseEvent`

**Signature:**
```cpp
bool propagateOnMouseEvent(const Point& mousePos, UIWidgetList& widgetList);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `UIWidgetList&` | `widgetList` | - |

**Returns:**
- `bool`

---

(propagateonmousemove)=
## `propagateOnMouseMove`

**Signature:**
```cpp
bool propagateOnMouseMove(const Point& mousePos, const Point& mouseMoved, UIWidgetList& widgetList);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `const Point&` | `mouseMoved` | - |
| `UIWidgetList&` | `widgetList` | - |

**Returns:**
- `bool`

---

(initbasestyle)=
## `initBaseStyle`

**Signature:**
```cpp
private: void initBaseStyle();
```

---

(parsebasestyle)=
## `parseBaseStyle`

**Signature:**
```cpp
void parseBaseStyle(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

---

(drawbackground)=
## `drawBackground`

**Signature:**
```cpp
protected: void drawBackground(const Rect& screenCoords);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `screenCoords` | - |

---

(drawborder)=
## `drawBorder`

**Signature:**
```cpp
void drawBorder(const Rect& screenCoords);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `screenCoords` | - |

---

(drawicon)=
## `drawIcon`

**Signature:**
```cpp
void drawIcon(const Rect& screenCoords);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `screenCoords` | - |

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

(setcursor)=
## `setCursor`

**Signature:**
```cpp
void setCursor(const std::string& cursor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `cursor` | - |

---

(initimage)=
## `initImage`

**Signature:**
```cpp
private: void initImage();
```

---

(parseimagestyle)=
## `parseImageStyle`

**Signature:**
```cpp
void parseImageStyle(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

---

(drawimage)=
## `drawImage`

**Signature:**
```cpp
protected: void drawImage(const Rect& screenCoords);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `screenCoords` | - |

---

(setqrcode)=
## `setQRCode`

**Signature:**
```cpp
public: void setQRCode(const std::string& code, int border);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `code` | - |
| `int` | `border` | - |

---

(setimagesource)=
## `setImageSource`

**Signature:**
```cpp
void setImageSource(const std::string& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `source` | - |

---

(setimagesourcebase64)=
## `setImageSourceBase64`

**Signature:**
```cpp
void setImageSourceBase64(const std::string & data);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string &` | `data` | - |

---

(inittext)=
## `initText`

**Signature:**
```cpp
private: void initText();
```

---

(parsetextstyle)=
## `parseTextStyle`

**Signature:**
```cpp
void parseTextStyle(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

---

(updatetext)=
## `updateText`

**Signature:**
```cpp
protected: virtual void updateText();
```

---

(drawtext)=
## `drawText`

**Signature:**
```cpp
void drawText(const Rect& screenCoords);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `screenCoords` | - |

---

(ontextchange)=
## `onTextChange`

**Signature:**
```cpp
virtual void onTextChange(const std::string& text, const std::string& oldText);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |
| `const std::string&` | `oldText` | - |

---

(onfontchange)=
## `onFontChange`

**Signature:**
```cpp
virtual void onFontChange(const std::string& font);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `font` | - |

---

(settext)=
## `setText`

**Signature:**
```cpp
void setText(std::string text, bool dontFireLuaCall = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `std::string` | `text` |  | - |
| `bool` | `dontFireLuaCall` | `false` | - |

---

(setcoloredtext)=
## `setColoredText`

**Signature:**
```cpp
void setColoredText(const std::vector<std::string>& texts, bool dontFireLuaCall = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::vector&lt;std::string&gt;&` | `texts` |  | - |
| `bool` | `dontFireLuaCall` | `false` | - |

---

(setfont)=
## `setFont`

**Signature:**
```cpp
void setFont(const std::string& fontName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fontName` | - |

---

(set)=
## `set`

**Signature:**
```cpp
void set(T value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `value` | - |

---

(setclipping)=
## `setClipping`

**Signature:**
```cpp
void setClipping(bool clipping);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `clipping` | - |

---

(setautorepeatdelay)=
## `setAutoRepeatDelay`

**Signature:**
```cpp
void setAutoRepeatDelay(int delay);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `delay` | - |

---

(resize)=
## `resize`

**Signature:**
```cpp
public: void resize(int width, int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |
| `int` | `height` | - |

---

(move)=
## `move`

**Signature:**
```cpp
void move(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

---

(rotate)=
## `rotate`

**Signature:**
```cpp
void rotate(float degrees);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `degrees` | - |

---

(hide)=
## `hide`

**Signature:**
```cpp
void hide();
```

---

(show)=
## `show`

**Signature:**
```cpp
void show();
```

---

(disable)=
## `disable`

**Signature:**
```cpp
void disable();
```

---

(enable)=
## `enable`

**Signature:**
```cpp
void enable();
```

---

(isactive)=
## `isActive`

**Signature:**
```cpp
bool isActive();
```

**Returns:**
- `bool`

---

(isenabled)=
## `isEnabled`

**Signature:**
```cpp
bool isEnabled();
```

**Returns:**
- `bool`

---

(isdisabled)=
## `isDisabled`

**Signature:**
```cpp
bool isDisabled();
```

**Returns:**
- `bool`

---

(isfocused)=
## `isFocused`

**Signature:**
```cpp
bool isFocused();
```

**Returns:**
- `bool`

---

(ishovered)=
## `isHovered`

**Signature:**
```cpp
bool isHovered();
```

**Returns:**
- `bool`

---

(ispressed)=
## `isPressed`

**Signature:**
```cpp
bool isPressed();
```

**Returns:**
- `bool`

---

(isfirst)=
## `isFirst`

**Signature:**
```cpp
bool isFirst();
```

**Returns:**
- `bool`

---

(ismiddle)=
## `isMiddle`

**Signature:**
```cpp
bool isMiddle();
```

**Returns:**
- `bool`

---

(islast)=
## `isLast`

**Signature:**
```cpp
bool isLast();
```

**Returns:**
- `bool`

---

(isalternate)=
## `isAlternate`

**Signature:**
```cpp
bool isAlternate();
```

**Returns:**
- `bool`

---

(ischecked)=
## `isChecked`

**Signature:**
```cpp
bool isChecked();
```

**Returns:**
- `bool`

---

(ison)=
## `isOn`

**Signature:**
```cpp
bool isOn();
```

**Returns:**
- `bool`

---

(isdragging)=
## `isDragging`

**Signature:**
```cpp
bool isDragging();
```

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

(ishidden)=
## `isHidden`

**Signature:**
```cpp
bool isHidden();
```

**Returns:**
- `bool`

---

(isexplicitlyenabled)=
## `isExplicitlyEnabled`

**Signature:**
```cpp
bool isExplicitlyEnabled();
```

**Returns:**
- `bool`

---

(isexplicitlyvisible)=
## `isExplicitlyVisible`

**Signature:**
```cpp
bool isExplicitlyVisible();
```

**Returns:**
- `bool`

---

(isautodraw)=
## `isAutoDraw`

**Signature:**
```cpp
bool isAutoDraw();
```

**Returns:**
- `bool`

---

(isfocusable)=
## `isFocusable`

**Signature:**
```cpp
bool isFocusable();
```

**Returns:**
- `bool`

---

(isphantom)=
## `isPhantom`

**Signature:**
```cpp
bool isPhantom();
```

**Returns:**
- `bool`

---

(isdraggable)=
## `isDraggable`

**Signature:**
```cpp
bool isDraggable();
```

**Returns:**
- `bool`

---

(isfixedsize)=
## `isFixedSize`

**Signature:**
```cpp
bool isFixedSize();
```

**Returns:**
- `bool`

---

(isclipping)=
## `isClipping`

**Signature:**
```cpp
bool isClipping();
```

**Returns:**
- `bool`

---

(isdestroyed)=
## `isDestroyed`

**Signature:**
```cpp
bool isDestroyed();
```

**Returns:**
- `bool`

---

(haschildren)=
## `hasChildren`

**Signature:**
```cpp
bool hasChildren();
```

**Returns:**
- `bool`

---

(containsmarginpoint)=
## `containsMarginPoint`

**Signature:**
```cpp
bool containsMarginPoint(const Point& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |

**Returns:**
- `bool`

---

(containspaddingpoint)=
## `containsPaddingPoint`

**Signature:**
```cpp
bool containsPaddingPoint(const Point& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |

**Returns:**
- `bool`

---

(containspoint)=
## `containsPoint`

**Signature:**
```cpp
bool containsPoint(const Point& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |

**Returns:**
- `bool`

---

(getid)=
## `getId`

**Signature:**
```cpp
std::string getId();
```

**Returns:**
- `std::string`

---

(getsource)=
## `getSource`

**Signature:**
```cpp
std::string getSource();
```

**Returns:**
- `std::string`

---

(getparent)=
## `getParent`

**Signature:**
```cpp
UIWidgetPtr getParent();
```

**Returns:**
- `UIWidgetPtr`

---

(getparentid)=
## `getParentId`

**Signature:**
```cpp
std::string getParentId();
```

**Returns:**
- `std::string`

---

(getfocusedchild)=
## `getFocusedChild`

**Signature:**
```cpp
UIWidgetPtr getFocusedChild();
```

**Returns:**
- `UIWidgetPtr`

---

(getchildren)=
## `getChildren`

**Signature:**
```cpp
UIWidgetList getChildren();
```

**Returns:**
- `UIWidgetList`

---

(getfirstchild)=
## `getFirstChild`

**Signature:**
```cpp
UIWidgetPtr getFirstChild();
```

**Returns:**
- `UIWidgetPtr`

---

(getlastchild)=
## `getLastChild`

**Signature:**
```cpp
UIWidgetPtr getLastChild();
```

**Returns:**
- `UIWidgetPtr`

---

(getlayout)=
## `getLayout`

**Signature:**
```cpp
UILayoutPtr getLayout();
```

**Returns:**
- `UILayoutPtr`

---

(getstyle)=
## `getStyle`

**Signature:**
```cpp
OTMLNodePtr getStyle();
```

**Returns:**
- `OTMLNodePtr`

---

(getchildcount)=
## `getChildCount`

**Signature:**
```cpp
int getChildCount();
```

**Returns:**
- `int`

---

(getlastfocusreason)=
## `getLastFocusReason`

**Signature:**
```cpp
Fw::FocusReason getLastFocusReason();
```

**Returns:**
- `Fw::FocusReason`

---

(getautofocuspolicy)=
## `getAutoFocusPolicy`

**Signature:**
```cpp
Fw::AutoFocusPolicy getAutoFocusPolicy();
```

**Returns:**
- `Fw::AutoFocusPolicy`

---

(getautorepeatdelay)=
## `getAutoRepeatDelay`

**Signature:**
```cpp
int getAutoRepeatDelay();
```

**Returns:**
- `int`

---

(getvirtualoffset)=
## `getVirtualOffset`

**Signature:**
```cpp
Point getVirtualOffset();
```

**Returns:**
- `Point`

---

(getstylename)=
## `getStyleName`

**Signature:**
```cpp
std::string getStyleName();
```

**Returns:**
- `std::string`

---

(getlastclickposition)=
## `getLastClickPosition`

**Signature:**
```cpp
Point getLastClickPosition();
```

**Returns:**
- `Point`

---

(isrootchild)=
## `isRootChild`

**Signature:**
```cpp
bool isRootChild();
```

**Returns:**
- `bool`

---

(setrootchild)=
## `setRootChild`

**Signature:**
```cpp
void setRootChild(bool v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `v` | - |

---

(setx)=
## `setX`

**Signature:**
```cpp
public: void setX(int x);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |

---

(sety)=
## `setY`

**Signature:**
```cpp
void setY(int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `y` | - |

---

(setwidth)=
## `setWidth`

**Signature:**
```cpp
void setWidth(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setheight)=
## `setHeight`

**Signature:**
```cpp
void setHeight(int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `height` | - |

---

(setsize)=
## `setSize`

**Signature:**
```cpp
void setSize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(setposition)=
## `setPosition`

**Signature:**
```cpp
void setPosition(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(setcolor)=
## `setColor`

**Signature:**
```cpp
void setColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setbackgroundcolor)=
## `setBackgroundColor`

**Signature:**
```cpp
void setBackgroundColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setbackgroundoffsetx)=
## `setBackgroundOffsetX`

**Signature:**
```cpp
void setBackgroundOffsetX(int x);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |

---

(setbackgroundoffsety)=
## `setBackgroundOffsetY`

**Signature:**
```cpp
void setBackgroundOffsetY(int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `y` | - |

---

(setbackgroundoffset)=
## `setBackgroundOffset`

**Signature:**
```cpp
void setBackgroundOffset(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(setbackgroundwidth)=
## `setBackgroundWidth`

**Signature:**
```cpp
void setBackgroundWidth(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setbackgroundheight)=
## `setBackgroundHeight`

**Signature:**
```cpp
void setBackgroundHeight(int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `height` | - |

---

(setbackgroundsize)=
## `setBackgroundSize`

**Signature:**
```cpp
void setBackgroundSize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(setbackgroundrect)=
## `setBackgroundRect`

**Signature:**
```cpp
void setBackgroundRect(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(seticoncolor)=
## `setIconColor`

**Signature:**
```cpp
void setIconColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(seticonoffsetx)=
## `setIconOffsetX`

**Signature:**
```cpp
void setIconOffsetX(int x);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |

---

(seticonoffsety)=
## `setIconOffsetY`

**Signature:**
```cpp
void setIconOffsetY(int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `y` | - |

---

(seticonoffset)=
## `setIconOffset`

**Signature:**
```cpp
void setIconOffset(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(seticonwidth)=
## `setIconWidth`

**Signature:**
```cpp
void setIconWidth(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(seticonheight)=
## `setIconHeight`

**Signature:**
```cpp
void setIconHeight(int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `height` | - |

---

(seticonsize)=
## `setIconSize`

**Signature:**
```cpp
void setIconSize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(seticonrect)=
## `setIconRect`

**Signature:**
```cpp
void setIconRect(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(seticonclip)=
## `setIconClip`

**Signature:**
```cpp
void setIconClip(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(seticonalign)=
## `setIconAlign`

**Signature:**
```cpp
void setIconAlign(Fw::AlignmentFlag align);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AlignmentFlag` | `align` | - |

---

(setborderwidth)=
## `setBorderWidth`

**Signature:**
```cpp
void setBorderWidth(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setborderwidthtop)=
## `setBorderWidthTop`

**Signature:**
```cpp
void setBorderWidthTop(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setborderwidthright)=
## `setBorderWidthRight`

**Signature:**
```cpp
void setBorderWidthRight(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setborderwidthbottom)=
## `setBorderWidthBottom`

**Signature:**
```cpp
void setBorderWidthBottom(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setborderwidthleft)=
## `setBorderWidthLeft`

**Signature:**
```cpp
void setBorderWidthLeft(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setbordercolor)=
## `setBorderColor`

**Signature:**
```cpp
void setBorderColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setbordercolortop)=
## `setBorderColorTop`

**Signature:**
```cpp
void setBorderColorTop(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setbordercolorright)=
## `setBorderColorRight`

**Signature:**
```cpp
void setBorderColorRight(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setbordercolorbottom)=
## `setBorderColorBottom`

**Signature:**
```cpp
void setBorderColorBottom(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setbordercolorleft)=
## `setBorderColorLeft`

**Signature:**
```cpp
void setBorderColorLeft(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setmargin)=
## `setMargin`

**Signature:**
```cpp
void setMargin(int margin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `margin` | - |

---

(setmarginhorizontal)=
## `setMarginHorizontal`

**Signature:**
```cpp
void setMarginHorizontal(int margin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `margin` | - |

---

(setmarginvertical)=
## `setMarginVertical`

**Signature:**
```cpp
void setMarginVertical(int margin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `margin` | - |

---

(setmargintop)=
## `setMarginTop`

**Signature:**
```cpp
void setMarginTop(int margin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `margin` | - |

---

(setmarginright)=
## `setMarginRight`

**Signature:**
```cpp
void setMarginRight(int margin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `margin` | - |

---

(setmarginbottom)=
## `setMarginBottom`

**Signature:**
```cpp
void setMarginBottom(int margin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `margin` | - |

---

(setmarginleft)=
## `setMarginLeft`

**Signature:**
```cpp
void setMarginLeft(int margin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `margin` | - |

---

(setpadding)=
## `setPadding`

**Signature:**
```cpp
void setPadding(int padding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `padding` | - |

---

(setpaddinghorizontal)=
## `setPaddingHorizontal`

**Signature:**
```cpp
void setPaddingHorizontal(int padding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `padding` | - |

---

(setpaddingvertical)=
## `setPaddingVertical`

**Signature:**
```cpp
void setPaddingVertical(int padding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `padding` | - |

---

(setpaddingtop)=
## `setPaddingTop`

**Signature:**
```cpp
void setPaddingTop(int padding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `padding` | - |

---

(setpaddingright)=
## `setPaddingRight`

**Signature:**
```cpp
void setPaddingRight(int padding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `padding` | - |

---

(setpaddingbottom)=
## `setPaddingBottom`

**Signature:**
```cpp
void setPaddingBottom(int padding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `padding` | - |

---

(setpaddingleft)=
## `setPaddingLeft`

**Signature:**
```cpp
void setPaddingLeft(int padding);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `padding` | - |

---

(setopacity)=
## `setOpacity`

**Signature:**
```cpp
void setOpacity(float opacity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `opacity` | - |

---

(setrotation)=
## `setRotation`

**Signature:**
```cpp
void setRotation(float degrees);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `degrees` | - |

---

(setchangecursorimage)=
## `setChangeCursorImage`

**Signature:**
```cpp
void setChangeCursorImage(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

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

(getposition)=
## `getPosition`

**Signature:**
```cpp
Point getPosition();
```

**Returns:**
- `Point`

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

(getsize)=
## `getSize`

**Signature:**
```cpp
Size getSize();
```

**Returns:**
- `Size`

---

(getrect)=
## `getRect`

**Signature:**
```cpp
Rect getRect();
```

**Returns:**
- `Rect`

---

(getcolor)=
## `getColor`

**Signature:**
```cpp
Color getColor();
```

**Returns:**
- `Color`

---

(getbackgroundcolor)=
## `getBackgroundColor`

**Signature:**
```cpp
Color getBackgroundColor();
```

**Returns:**
- `Color`

---

(getbackgroundoffsetx)=
## `getBackgroundOffsetX`

**Signature:**
```cpp
int getBackgroundOffsetX();
```

**Returns:**
- `int`

---

(getbackgroundoffsety)=
## `getBackgroundOffsetY`

**Signature:**
```cpp
int getBackgroundOffsetY();
```

**Returns:**
- `int`

---

(getbackgroundoffset)=
## `getBackgroundOffset`

**Signature:**
```cpp
Point getBackgroundOffset();
```

**Returns:**
- `Point`

---

(getbackgroundwidth)=
## `getBackgroundWidth`

**Signature:**
```cpp
int getBackgroundWidth();
```

**Returns:**
- `int`

---

(getbackgroundheight)=
## `getBackgroundHeight`

**Signature:**
```cpp
int getBackgroundHeight();
```

**Returns:**
- `int`

---

(getbackgroundsize)=
## `getBackgroundSize`

**Signature:**
```cpp
Size getBackgroundSize();
```

**Returns:**
- `Size`

---

(getbackgroundrect)=
## `getBackgroundRect`

**Signature:**
```cpp
Rect getBackgroundRect();
```

**Returns:**
- `Rect`

---

(geticoncolor)=
## `getIconColor`

**Signature:**
```cpp
Color getIconColor();
```

**Returns:**
- `Color`

---

(geticonoffsetx)=
## `getIconOffsetX`

**Signature:**
```cpp
int getIconOffsetX();
```

**Returns:**
- `int`

---

(geticonoffsety)=
## `getIconOffsetY`

**Signature:**
```cpp
int getIconOffsetY();
```

**Returns:**
- `int`

---

(geticonoffset)=
## `getIconOffset`

**Signature:**
```cpp
Point getIconOffset();
```

**Returns:**
- `Point`

---

(geticonwidth)=
## `getIconWidth`

**Signature:**
```cpp
int getIconWidth();
```

**Returns:**
- `int`

---

(geticonheight)=
## `getIconHeight`

**Signature:**
```cpp
int getIconHeight();
```

**Returns:**
- `int`

---

(geticonsize)=
## `getIconSize`

**Signature:**
```cpp
Size getIconSize();
```

**Returns:**
- `Size`

---

(geticonrect)=
## `getIconRect`

**Signature:**
```cpp
Rect getIconRect();
```

**Returns:**
- `Rect`

---

(geticonclip)=
## `getIconClip`

**Signature:**
```cpp
Rect getIconClip();
```

**Returns:**
- `Rect`

---

(geticonpath)=
## `getIconPath`

**Signature:**
```cpp
std::string getIconPath();
```

**Returns:**
- `std::string`

---

(geticonalign)=
## `getIconAlign`

**Signature:**
```cpp
Fw::AlignmentFlag getIconAlign();
```

**Returns:**
- `Fw::AlignmentFlag`

---

(getbordertopcolor)=
## `getBorderTopColor`

**Signature:**
```cpp
Color getBorderTopColor();
```

**Returns:**
- `Color`

---

(getborderrightcolor)=
## `getBorderRightColor`

**Signature:**
```cpp
Color getBorderRightColor();
```

**Returns:**
- `Color`

---

(getborderbottomcolor)=
## `getBorderBottomColor`

**Signature:**
```cpp
Color getBorderBottomColor();
```

**Returns:**
- `Color`

---

(getborderleftcolor)=
## `getBorderLeftColor`

**Signature:**
```cpp
Color getBorderLeftColor();
```

**Returns:**
- `Color`

---

(getbordertopwidth)=
## `getBorderTopWidth`

**Signature:**
```cpp
int getBorderTopWidth();
```

**Returns:**
- `int`

---

(getborderrightwidth)=
## `getBorderRightWidth`

**Signature:**
```cpp
int getBorderRightWidth();
```

**Returns:**
- `int`

---

(getborderbottomwidth)=
## `getBorderBottomWidth`

**Signature:**
```cpp
int getBorderBottomWidth();
```

**Returns:**
- `int`

---

(getborderleftwidth)=
## `getBorderLeftWidth`

**Signature:**
```cpp
int getBorderLeftWidth();
```

**Returns:**
- `int`

---

(getmargintop)=
## `getMarginTop`

**Signature:**
```cpp
int getMarginTop();
```

**Returns:**
- `int`

---

(getmarginright)=
## `getMarginRight`

**Signature:**
```cpp
int getMarginRight();
```

**Returns:**
- `int`

---

(getmarginbottom)=
## `getMarginBottom`

**Signature:**
```cpp
int getMarginBottom();
```

**Returns:**
- `int`

---

(getmarginleft)=
## `getMarginLeft`

**Signature:**
```cpp
int getMarginLeft();
```

**Returns:**
- `int`

---

(getpaddingtop)=
## `getPaddingTop`

**Signature:**
```cpp
int getPaddingTop();
```

**Returns:**
- `int`

---

(getpaddingright)=
## `getPaddingRight`

**Signature:**
```cpp
int getPaddingRight();
```

**Returns:**
- `int`

---

(getpaddingbottom)=
## `getPaddingBottom`

**Signature:**
```cpp
int getPaddingBottom();
```

**Returns:**
- `int`

---

(getpaddingleft)=
## `getPaddingLeft`

**Signature:**
```cpp
int getPaddingLeft();
```

**Returns:**
- `int`

---

(getopacity)=
## `getOpacity`

**Signature:**
```cpp
float getOpacity();
```

**Returns:**
- `float`

---

(getrotation)=
## `getRotation`

**Signature:**
```cpp
float getRotation();
```

**Returns:**
- `float`

---

(ischangingcursorimage)=
## `isChangingCursorImage`

**Signature:**
```cpp
bool isChangingCursorImage();
```

**Returns:**
- `bool`

---

(updateimagecache)=
## `updateImageCache`

**Signature:**
```cpp
void updateImageCache();
```

---

(configureborderimage)=
## `configureBorderImage`

**Signature:**
```cpp
void configureBorderImage();
```

---

(setimageclip)=
## `setImageClip`

**Signature:**
```cpp
void setImageClip(const Rect& clipRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `clipRect` | - |

---

(setimageoffsetx)=
## `setImageOffsetX`

**Signature:**
```cpp
void setImageOffsetX(int x);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |

---

(setimageoffsety)=
## `setImageOffsetY`

**Signature:**
```cpp
void setImageOffsetY(int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `y` | - |

---

(setimageoffset)=
## `setImageOffset`

**Signature:**
```cpp
void setImageOffset(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(setimagewidth)=
## `setImageWidth`

**Signature:**
```cpp
void setImageWidth(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setimageheight)=
## `setImageHeight`

**Signature:**
```cpp
void setImageHeight(int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `height` | - |

---

(setimagesize)=
## `setImageSize`

**Signature:**
```cpp
void setImageSize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(setimagerect)=
## `setImageRect`

**Signature:**
```cpp
void setImageRect(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(setimagecolor)=
## `setImageColor`

**Signature:**
```cpp
void setImageColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setimagefixedratio)=
## `setImageFixedRatio`

**Signature:**
```cpp
void setImageFixedRatio(bool fixedRatio);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `fixedRatio` | - |

---

(setimagerepeated)=
## `setImageRepeated`

**Signature:**
```cpp
void setImageRepeated(bool repeated);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `repeated` | - |

---

(setimagesmooth)=
## `setImageSmooth`

**Signature:**
```cpp
void setImageSmooth(bool smooth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `smooth` | - |

---

(setimageautoresize)=
## `setImageAutoResize`

**Signature:**
```cpp
void setImageAutoResize(bool autoResize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `autoResize` | - |

---

(setimagebordertop)=
## `setImageBorderTop`

**Signature:**
```cpp
void setImageBorderTop(int border);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `border` | - |

---

(setimageborderright)=
## `setImageBorderRight`

**Signature:**
```cpp
void setImageBorderRight(int border);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `border` | - |

---

(setimageborderbottom)=
## `setImageBorderBottom`

**Signature:**
```cpp
void setImageBorderBottom(int border);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `border` | - |

---

(setimageborderleft)=
## `setImageBorderLeft`

**Signature:**
```cpp
void setImageBorderLeft(int border);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `border` | - |

---

(setimageborder)=
## `setImageBorder`

**Signature:**
```cpp
void setImageBorder(int border);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `border` | - |

---

(setimageshader)=
## `setImageShader`

**Signature:**
```cpp
void setImageShader(const std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |

---

(getimageclip)=
## `getImageClip`

**Signature:**
```cpp
Rect getImageClip();
```

**Returns:**
- `Rect`

---

(getimageoffsetx)=
## `getImageOffsetX`

**Signature:**
```cpp
int getImageOffsetX();
```

**Returns:**
- `int`

---

(getimageoffsety)=
## `getImageOffsetY`

**Signature:**
```cpp
int getImageOffsetY();
```

**Returns:**
- `int`

---

(getimageoffset)=
## `getImageOffset`

**Signature:**
```cpp
Point getImageOffset();
```

**Returns:**
- `Point`

---

(getimagewidth)=
## `getImageWidth`

**Signature:**
```cpp
int getImageWidth();
```

**Returns:**
- `int`

---

(getimageheight)=
## `getImageHeight`

**Signature:**
```cpp
int getImageHeight();
```

**Returns:**
- `int`

---

(getimagesize)=
## `getImageSize`

**Signature:**
```cpp
Size getImageSize();
```

**Returns:**
- `Size`

---

(getimagerect)=
## `getImageRect`

**Signature:**
```cpp
Rect getImageRect();
```

**Returns:**
- `Rect`

---

(getimagecolor)=
## `getImageColor`

**Signature:**
```cpp
Color getImageColor();
```

**Returns:**
- `Color`

---

(isimagefixedratio)=
## `isImageFixedRatio`

**Signature:**
```cpp
bool isImageFixedRatio();
```

**Returns:**
- `bool`

---

(isimagesmooth)=
## `isImageSmooth`

**Signature:**
```cpp
bool isImageSmooth();
```

**Returns:**
- `bool`

---

(isimageautoresize)=
## `isImageAutoResize`

**Signature:**
```cpp
bool isImageAutoResize();
```

**Returns:**
- `bool`

---

(getimagebordertop)=
## `getImageBorderTop`

**Signature:**
```cpp
int getImageBorderTop();
```

**Returns:**
- `int`

---

(getimageborderright)=
## `getImageBorderRight`

**Signature:**
```cpp
int getImageBorderRight();
```

**Returns:**
- `int`

---

(getimageborderbottom)=
## `getImageBorderBottom`

**Signature:**
```cpp
int getImageBorderBottom();
```

**Returns:**
- `int`

---

(getimageborderleft)=
## `getImageBorderLeft`

**Signature:**
```cpp
int getImageBorderLeft();
```

**Returns:**
- `int`

---

(getimagetexturewidth)=
## `getImageTextureWidth`

**Signature:**
```cpp
int getImageTextureWidth();
```

**Returns:**
- `int`

---

(getimagetextureheight)=
## `getImageTextureHeight`

**Signature:**
```cpp
int getImageTextureHeight();
```

**Returns:**
- `int`

---

(getimageshader)=
## `getImageShader`

**Signature:**
```cpp
std::string getImageShader();
```

**Returns:**
- `std::string`

---

(resizetotext)=
## `resizeToText`

**Signature:**
```cpp
public: void resizeToText();
```

---

(cleartext)=
## `clearText`

**Signature:**
```cpp
void clearText();
```

---

(settextalign)=
## `setTextAlign`

**Signature:**
```cpp
void setTextAlign(Fw::AlignmentFlag align);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AlignmentFlag` | `align` | - |

---

(settextoffset)=
## `setTextOffset`

**Signature:**
```cpp
void setTextOffset(const Point& offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `offset` | - |

---

(settextwrap)=
## `setTextWrap`

**Signature:**
```cpp
void setTextWrap(bool textWrap);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `textWrap` | - |

---

(settextautoresize)=
## `setTextAutoResize`

**Signature:**
```cpp
void setTextAutoResize(bool textAutoResize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `textAutoResize` | - |

---

(settexthorizontalautoresize)=
## `setTextHorizontalAutoResize`

**Signature:**
```cpp
void setTextHorizontalAutoResize(bool textAutoResize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `textAutoResize` | - |

---

(settextverticalautoresize)=
## `setTextVerticalAutoResize`

**Signature:**
```cpp
void setTextVerticalAutoResize(bool textAutoResize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `textAutoResize` | - |

---

(settextonlyuppercase)=
## `setTextOnlyUpperCase`

**Signature:**
```cpp
void setTextOnlyUpperCase(bool textOnlyUpperCase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `textOnlyUpperCase` | - |

---

(setshadow)=
## `setShadow`

**Signature:**
```cpp
void setShadow(bool shadow);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `shadow` | - |

---

(gettext)=
## `getText`

**Signature:**
```cpp
std::string getText();
```

**Returns:**
- `std::string`

---

(getdrawtext)=
## `getDrawText`

**Signature:**
```cpp
std::string getDrawText();
```

**Returns:**
- `std::string`

---

(gettextalign)=
## `getTextAlign`

**Signature:**
```cpp
Fw::AlignmentFlag getTextAlign();
```

**Returns:**
- `Fw::AlignmentFlag`

---

(gettextoffset)=
## `getTextOffset`

**Signature:**
```cpp
Point getTextOffset();
```

**Returns:**
- `Point`

---

(gettextwrap)=
## `getTextWrap`

**Signature:**
```cpp
bool getTextWrap();
```

**Returns:**
- `bool`

---

(getfont)=
## `getFont`

**Signature:**
```cpp
std::string getFont();
```

**Returns:**
- `std::string`

---

(gettextsize)=
## `getTextSize`

**Signature:**
```cpp
Size getTextSize();
```

**Returns:**
- `Size`

---

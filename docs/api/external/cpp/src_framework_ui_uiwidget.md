# src/framework/ui/uiwidget.h

```cpp
void set(T value) { top = right = bottom = left = value; } T top; T right; T bottom; T left; }; // @bindclass class UIWidget : public LuaObject { // widget core public: UIWidget();
```
```cpp
virtual void draw(const Rect& visibleRect, Fw::DrawPane drawPane);
```
```cpp
protected:
    virtual void drawSelf(Fw::DrawPane drawPane);
```
```cpp
virtual void drawChildren(const Rect& visibleRect, Fw::DrawPane drawPane);
```
```cpp
public:
    void addChild(const UIWidgetPtr& child);
```
```cpp
void onChildIdChange(const UIWidgetPtr& child);
```
```cpp
void insertChild(int index, const UIWidgetPtr& child);
```
```cpp
void removeChild(UIWidgetPtr child);
```
```cpp
void focusChild(const UIWidgetPtr& child, Fw::FocusReason reason);
```
```cpp
void focusNextChild(Fw::FocusReason reason, bool rotate = false);
```
```cpp
void focusPreviousChild(Fw::FocusReason reason, bool rotate = false);
```
```cpp
void lowerChild(UIWidgetPtr child);
```
```cpp
void raiseChild(UIWidgetPtr child);
```
```cpp
void moveChildToIndex(const UIWidgetPtr& child, int index);
```
```cpp
void reorderChildren(const std::vector<UIWidgetPtr>& childrens);
```
```cpp
void lockChild(const UIWidgetPtr& child);
```
```cpp
void unlockChild(const UIWidgetPtr& child);
```
```cpp
void mergeStyle(const OTMLNodePtr& styleNode);
```
```cpp
void applyStyle(const OTMLNodePtr& styleNode);
```
```cpp
void addAnchor(Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge);
```
```cpp
void removeAnchor(Fw::AnchorEdge anchoredEdge);
```
```cpp
void fill(const std::string& hookedWidgetId);
```
```cpp
void centerIn(const std::string& hookedWidgetId);
```
```cpp
void breakAnchors();
```
```cpp
void updateParentLayout();
```
```cpp
void updateLayout();
```
```cpp
void lock();
```
```cpp
void unlock();
```
```cpp
void focus();
```
```cpp
void recursiveFocus(Fw::FocusReason reason);
```
```cpp
void lower();
```
```cpp
void raise();
```
```cpp
void grabMouse();
```
```cpp
void ungrabMouse();
```
```cpp
void grabKeyboard();
```
```cpp
void ungrabKeyboard();
```
```cpp
void bindRectToParent();
```
```cpp
void destroy();
```
```cpp
void destroyChildren();
```
```cpp
void setId(const std::string& id);
```
```cpp
void setParent(const UIWidgetPtr& parent);
```
```cpp
void setLayout(const UILayoutPtr& layout);
```
```cpp
bool setRect(const Rect& rect);
```
```cpp
void setStyle(const std::string& styleName);
```
```cpp
void setStyleFromNode(const OTMLNodePtr& styleNode);
```
```cpp
void setEnabled(bool enabled);
```
```cpp
void setVisible(bool visible);
```
```cpp
void setAutoDraw(bool value);
```
```cpp
void setOn(bool on);
```
```cpp
void setChecked(bool checked);
```
```cpp
void setFocusable(bool focusable);
```
```cpp
void setPhantom(bool phantom);
```
```cpp
void setDraggable(bool draggable);
```
```cpp
void setFixedSize(bool fixed);
```
```cpp
void setClipping(bool clipping) { m_clipping = clipping; } void setLastFocusReason(Fw::FocusReason reason);
```
```cpp
void setAutoFocusPolicy(Fw::AutoFocusPolicy policy);
```
```cpp
void setAutoRepeatDelay(int delay) { m_autoRepeatDelay = delay; } void setVirtualOffset(const Point& offset);
```
```cpp
bool isAnchored();
```
```cpp
bool isChildLocked(const UIWidgetPtr& child);
```
```cpp
bool hasChild(const UIWidgetPtr& child);
```
```cpp
int getChildIndex(const UIWidgetPtr& child);
```
```cpp
Rect getPaddingRect();
```
```cpp
Rect getMarginRect();
```
```cpp
Rect getChildrenRect();
```
```cpp
UIAnchorLayoutPtr getAnchoredLayout();
```
```cpp
UIWidgetPtr getRootParent();
```
```cpp
UIWidgetPtr getChildAfter(const UIWidgetPtr& relativeChild);
```
```cpp
UIWidgetPtr getChildBefore(const UIWidgetPtr& relativeChild);
```
```cpp
UIWidgetPtr getChildById(const std::string& childId);
```
```cpp
UIWidgetPtr getChildByPos(const Point& childPos);
```
```cpp
UIWidgetPtr getChildByIndex(int index);
```
```cpp
UIWidgetPtr recursiveGetChildById(const std::string& id);
```
```cpp
UIWidgetPtr recursiveGetChildByPos(const Point& childPos, bool wantsPhantom);
```
```cpp
UIWidgetList recursiveGetChildren();
```
```cpp
UIWidgetList recursiveGetChildrenByPos(const Point& childPos);
```
```cpp
UIWidgetList recursiveGetChildrenByMarginPos(const Point& childPos);
```
```cpp
UIWidgetPtr backwardsGetWidgetById(const std::string& id);
```
```cpp
protected:
    bool setState(Fw::WidgetState state, bool on);
```
```cpp
bool hasState(Fw::WidgetState state);
```
```cpp
private:
    void internalDestroy();
```
```cpp
void updateState(Fw::WidgetState state);
```
```cpp
void updateStates();
```
```cpp
void updateChildrenIndexStates();
```
```cpp
void updateStyle();
```
```cpp
protected:
    virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
virtual void onGeometryChange(const Rect& oldRect, const Rect& newRect);
```
```cpp
virtual void onLayoutUpdate();
```
```cpp
virtual void onFocusChange(bool focused, Fw::FocusReason reason);
```
```cpp
virtual void onChildFocusChange(const UIWidgetPtr& focusedChild, const UIWidgetPtr& unfocusedChild, Fw::FocusReason reason);
```
```cpp
virtual void onHoverChange(bool hovered);
```
```cpp
virtual void onVisibilityChange(bool visible);
```
```cpp
virtual bool onDragEnter(const Point& mousePos);
```
```cpp
virtual bool onDragLeave(UIWidgetPtr droppedWidget, const Point& mousePos);
```
```cpp
virtual bool onDragMove(const Point& mousePos, const Point& mouseMoved);
```
```cpp
virtual bool onDrop(UIWidgetPtr draggedWidget, const Point& mousePos);
```
```cpp
virtual bool onKeyText(const std::string& keyText);
```
```cpp
virtual bool onKeyDown(uchar keyCode, int keyboardModifiers);
```
```cpp
virtual bool onKeyPress(uchar keyCode, int keyboardModifiers, int autoRepeatTicks);
```
```cpp
virtual bool onKeyUp(uchar keyCode, int keyboardModifiers);
```
```cpp
virtual bool onMousePress(const Point& mousePos, Fw::MouseButton button);
```
```cpp
virtual bool onMouseRelease(const Point& mousePos, Fw::MouseButton button);
```
```cpp
virtual bool onMouseMove(const Point& mousePos, const Point& mouseMoved);
```
```cpp
virtual bool onMouseWheel(const Point& mousePos, Fw::MouseWheelDirection direction);
```
```cpp
virtual bool onClick(const Point& mousePos);
```
```cpp
virtual bool onDoubleClick(const Point& mousePos);
```
```cpp
bool propagateOnKeyText(const std::string& keyText);
```
```cpp
bool propagateOnKeyDown(uchar keyCode, int keyboardModifiers);
```
```cpp
bool propagateOnKeyPress(uchar keyCode, int keyboardModifiers, int autoRepeatTicks);
```
```cpp
bool propagateOnKeyUp(uchar keyCode, int keyboardModifiers);
```
```cpp
bool propagateOnMouseEvent(const Point& mousePos, UIWidgetList& widgetList);
```
```cpp
bool propagateOnMouseMove(const Point& mousePos, const Point& mouseMoved, UIWidgetList& widgetList);
```
```cpp
public:
    void resize(int width, int height) { setRect(Rect(getPosition(), Size(width, height)));
```
```cpp
void move(int x, int y) { setRect(Rect(x, y, getSize()));
```
```cpp
void rotate(float degrees) { setRotation(degrees);
```
```cpp
void hide() { setVisible(false);
```
```cpp
void show() { setVisible(true);
```
```cpp
void disable() { setEnabled(false);
```
```cpp
void enable() { setEnabled(true);
```
```cpp
bool isActive() { return hasState(Fw::ActiveState);
```
```cpp
bool isEnabled() { return !hasState(Fw::DisabledState);
```
```cpp
bool isDisabled() { return hasState(Fw::DisabledState);
```
```cpp
bool isFocused() { return hasState(Fw::FocusState);
```
```cpp
bool isHovered() { return hasState(Fw::HoverState);
```
```cpp
bool isPressed() { return hasState(Fw::PressedState);
```
```cpp
bool isFirst() { return hasState(Fw::FirstState);
```
```cpp
bool isMiddle() { return hasState(Fw::MiddleState);
```
```cpp
bool isLast() { return hasState(Fw::LastState);
```
```cpp
bool isAlternate() { return hasState(Fw::AlternateState);
```
```cpp
bool isChecked() { return hasState(Fw::CheckedState);
```
```cpp
bool isOn() { return hasState(Fw::OnState);
```
```cpp
bool isDragging() { return hasState(Fw::DraggingState);
```
```cpp
bool isVisible() { return !hasState(Fw::HiddenState);
```
```cpp
bool isHidden() { return hasState(Fw::HiddenState);
```
```cpp
bool isExplicitlyEnabled() { return m_enabled; } bool isExplicitlyVisible() { return m_visible; } bool isAutoDraw() { return m_autoDraw; } bool isFocusable() { return m_focusable; } bool isPhantom() { return m_phantom; } bool isDraggable() { return m_draggable; } bool isFixedSize() { return m_fixedSize; } bool isClipping() { return m_clipping; } bool isDestroyed() { return m_destroyed; } bool hasChildren() { return m_children.size() > 0; } bool containsMarginPoint(const Point& point) { return getMarginRect().contains(point);
```
```cpp
bool containsPaddingPoint(const Point& point) { return getPaddingRect().contains(point);
```
```cpp
bool containsPoint(const Point& point) { return m_rect.contains(point);
```
```cpp
std::string getId() { return m_id; } std::string getSource() { return m_source; } UIWidgetPtr getParent() { return m_parent; } std::string getParentId() { return m_parentId; } UIWidgetPtr getFocusedChild() { return m_focusedChild; } UIWidgetList getChildren() { return m_children; } UIWidgetPtr getFirstChild() { return getChildByIndex(1);
```
```cpp
UIWidgetPtr getLastChild() { return getChildByIndex(-1);
```
```cpp
UILayoutPtr getLayout() { return m_layout; } OTMLNodePtr getStyle() { return m_style; } int getChildCount() { return m_children.size();
```
```cpp
Fw::FocusReason getLastFocusReason() { return m_lastFocusReason; } Fw::AutoFocusPolicy getAutoFocusPolicy() { return m_autoFocusPolicy; } int getAutoRepeatDelay() { return m_autoRepeatDelay; } Point getVirtualOffset() { return m_virtualOffset; } std::string getStyleName() { return m_style->tag();
```
```cpp
Point getLastClickPosition() { return m_lastClickPosition; } // for stats only bool isRootChild() { return m_isRootChild; } void setRootChild(bool v) { m_isRootChild = v; } // base style private: void initBaseStyle();
```
```cpp
void parseBaseStyle(const OTMLNodePtr& styleNode);
```
```cpp
protected:
    void drawBackground(const Rect& screenCoords);
```
```cpp
void drawBorder(const Rect& screenCoords);
```
```cpp
void drawIcon(const Rect& screenCoords);
```
```cpp
public:
    void setX(int x) { move(x, getY());
```
```cpp
void setY(int y) { move(getX(), y);
```
```cpp
void setWidth(int width) { resize(width, getHeight());
```
```cpp
void setHeight(int height) { resize(getWidth(), height);
```
```cpp
void setSize(const Size& size) { resize(size.width(), size.height());
```
```cpp
void setPosition(const Point& pos) { move(pos.x, pos.y);
```
```cpp
void setColor(const Color& color) { m_color = color; } void setBackgroundColor(const Color& color) { m_backgroundColor = color; } void setBackgroundOffsetX(int x) { m_backgroundRect.setX(x);
```
```cpp
void setBackgroundOffsetY(int y) { m_backgroundRect.setX(y);
```
```cpp
void setBackgroundOffset(const Point& pos) { m_backgroundRect.move(pos);
```
```cpp
void setBackgroundWidth(int width) { m_backgroundRect.setWidth(width);
```
```cpp
void setBackgroundHeight(int height) { m_backgroundRect.setHeight(height);
```
```cpp
void setBackgroundSize(const Size& size) { m_backgroundRect.resize(size);
```
```cpp
void setBackgroundRect(const Rect& rect) { m_backgroundRect = rect; } void setIcon(const std::string& iconFile);
```
```cpp
void setIconColor(const Color& color) { m_iconColor = color; } void setIconOffsetX(int x) { m_iconOffset.x = x; } void setIconOffsetY(int y) { m_iconOffset.y = y; } void setIconOffset(const Point& pos) { m_iconOffset = pos; } void setIconWidth(int width) { m_iconRect.setWidth(width);
```
```cpp
void setIconHeight(int height) { m_iconRect.setHeight(height);
```
```cpp
void setIconSize(const Size& size) { m_iconRect.resize(size);
```
```cpp
void setIconRect(const Rect& rect) { m_iconRect = rect; } void setIconClip(const Rect& rect) { m_iconClipRect = rect; } void setIconAlign(Fw::AlignmentFlag align) { m_iconAlign = align; } void setBorderWidth(int width) { m_borderWidth.set(width);
```
```cpp
void setBorderWidthTop(int width) { m_borderWidth.top = width; } void setBorderWidthRight(int width) { m_borderWidth.right = width; } void setBorderWidthBottom(int width) { m_borderWidth.bottom = width; } void setBorderWidthLeft(int width) { m_borderWidth.left = width; } void setBorderColor(const Color& color) { m_borderColor.set(color);
```
```cpp
void setBorderColorTop(const Color& color) { m_borderColor.top = color; } void setBorderColorRight(const Color& color) { m_borderColor.right = color; } void setBorderColorBottom(const Color& color) { m_borderColor.bottom = color; } void setBorderColorLeft(const Color& color) { m_borderColor.left = color; } void setMargin(int margin) { m_margin.set(margin);
```
```cpp
void setMarginHorizontal(int margin) { m_margin.right = m_margin.left = margin; updateParentLayout();
```
```cpp
void setMarginVertical(int margin) { m_margin.bottom = m_margin.top = margin; updateParentLayout();
```
```cpp
void setMarginTop(int margin) { m_margin.top = margin; updateParentLayout();
```
```cpp
void setMarginRight(int margin) { m_margin.right = margin; updateParentLayout();
```
```cpp
void setMarginBottom(int margin) { m_margin.bottom = margin; updateParentLayout();
```
```cpp
void setMarginLeft(int margin) { m_margin.left = margin; updateParentLayout();
```
```cpp
void setPadding(int padding) { m_padding.top = m_padding.right = m_padding.bottom = m_padding.left = padding; updateLayout();
```
```cpp
void setPaddingHorizontal(int padding) { m_padding.right = m_padding.left = padding; updateLayout();
```
```cpp
void setPaddingVertical(int padding) { m_padding.bottom = m_padding.top = padding; updateLayout();
```
```cpp
void setPaddingTop(int padding) { m_padding.top = padding; updateLayout();
```
```cpp
void setPaddingRight(int padding) { m_padding.right = padding; updateLayout();
```
```cpp
void setPaddingBottom(int padding) { m_padding.bottom = padding; updateLayout();
```
```cpp
void setPaddingLeft(int padding) { m_padding.left = padding; updateLayout();
```
```cpp
void setOpacity(float opacity) { m_opacity = stdext::clamp<float>(opacity, 0.0f, 1.0f);
```
```cpp
void setRotation(float degrees) { m_rotation = degrees; } void setChangeCursorImage(bool enable) { m_changeCursorImage = enable; } void setCursor(const std::string& cursor);
```
```cpp
int getX() { return m_rect.x();
```
```cpp
int getY() { return m_rect.y();
```
```cpp
Point getPosition() { return m_rect.topLeft();
```
```cpp
int getWidth() { return m_rect.width();
```
```cpp
int getHeight() { return m_rect.height();
```
```cpp
Size getSize() { return m_rect.size();
```
```cpp
Rect getRect() { return m_rect; } Color getColor() { return m_color; } Color getBackgroundColor() { return m_backgroundColor; } int getBackgroundOffsetX() { return m_backgroundRect.x();
```
```cpp
int getBackgroundOffsetY() { return m_backgroundRect.y();
```
```cpp
Point getBackgroundOffset() { return m_backgroundRect.topLeft();
```
```cpp
int getBackgroundWidth() { return m_backgroundRect.width();
```
```cpp
int getBackgroundHeight() { return m_backgroundRect.height();
```
```cpp
Size getBackgroundSize() { return m_backgroundRect.size();
```
```cpp
Rect getBackgroundRect() { return m_backgroundRect; } Color getIconColor() { return m_iconColor; } int getIconOffsetX() { return m_iconOffset.x; } int getIconOffsetY() { return m_iconOffset.y; } Point getIconOffset() { return m_iconOffset; } int getIconWidth() { return m_iconRect.width();
```
```cpp
int getIconHeight() { return m_iconRect.height();
```
```cpp
Size getIconSize() { return m_iconRect.size();
```
```cpp
Rect getIconRect() { return m_iconRect; } Rect getIconClip() { return m_iconClipRect; } std::string getIconPath() { return m_iconPath; } Fw::AlignmentFlag getIconAlign() { return m_iconAlign; } Color getBorderTopColor() { return m_borderColor.top; } Color getBorderRightColor() { return m_borderColor.right; } Color getBorderBottomColor() { return m_borderColor.bottom; } Color getBorderLeftColor() { return m_borderColor.left; } int getBorderTopWidth() { return m_borderWidth.top; } int getBorderRightWidth() { return m_borderWidth.right; } int getBorderBottomWidth() { return m_borderWidth.bottom; } int getBorderLeftWidth() { return m_borderWidth.left; } int getMarginTop() { return m_margin.top; } int getMarginRight() { return m_margin.right; } int getMarginBottom() { return m_margin.bottom; } int getMarginLeft() { return m_margin.left; } int getPaddingTop() { return m_padding.top; } int getPaddingRight() { return m_padding.right; } int getPaddingBottom() { return m_padding.bottom; } int getPaddingLeft() { return m_padding.left; } float getOpacity() { return m_opacity; } float getRotation() { return m_rotation; } bool isChangingCursorImage() { return m_changeCursorImage; } // image private: void initImage();
```
```cpp
void parseImageStyle(const OTMLNodePtr& styleNode);
```
```cpp
void updateImageCache() { m_imageMustRecache = true; } void configureBorderImage() { m_imageBordered = true; updateImageCache();
```
```cpp
protected:
    void drawImage(const Rect& screenCoords);
```
```cpp
public:
    void setQRCode(const std::string& code, int border);
```
```cpp
void setImageSource(const std::string& source);
```
```cpp
void setImageSourceBase64(const std::string & data);
```
```cpp
void setImageClip(const Rect& clipRect) { m_imageClipRect = clipRect; updateImageCache();
```
```cpp
void setImageOffsetX(int x) { m_imageRect.setX(x);
```
```cpp
void setImageOffsetY(int y) { m_imageRect.setY(y);
```
```cpp
void setImageOffset(const Point& pos) { m_imageRect.move(pos);
```
```cpp
void setImageWidth(int width) { m_imageRect.setWidth(width);
```
```cpp
void setImageHeight(int height) { m_imageRect.setHeight(height);
```
```cpp
void setImageSize(const Size& size) { m_imageRect.resize(size);
```
```cpp
void setImageRect(const Rect& rect) { m_imageRect = rect; updateImageCache();
```
```cpp
void setImageColor(const Color& color) { m_imageColor = color; updateImageCache();
```
```cpp
void setImageFixedRatio(bool fixedRatio) { m_imageFixedRatio = fixedRatio; updateImageCache();
```
```cpp
void setImageRepeated(bool repeated) { m_imageRepeated = repeated; updateImageCache();
```
```cpp
void setImageSmooth(bool smooth) { m_imageSmooth = smooth; } void setImageAutoResize(bool autoResize) { m_imageAutoResize = autoResize; } void setImageBorderTop(int border) { m_imageBorder.top = border; configureBorderImage();
```
```cpp
void setImageBorderRight(int border) { m_imageBorder.right = border; configureBorderImage();
```
```cpp
void setImageBorderBottom(int border) { m_imageBorder.bottom = border; configureBorderImage();
```
```cpp
void setImageBorderLeft(int border) { m_imageBorder.left = border; configureBorderImage();
```
```cpp
void setImageBorder(int border) { m_imageBorder.set(border);
```
```cpp
void setImageShader(const std::string& str) { m_shader = str; } Rect getImageClip() { return m_imageClipRect; } int getImageOffsetX() { return m_imageRect.x();
```
```cpp
int getImageOffsetY() { return m_imageRect.y();
```
```cpp
Point getImageOffset() { return m_imageRect.topLeft();
```
```cpp
int getImageWidth() { return m_imageRect.width();
```
```cpp
int getImageHeight() { return m_imageRect.height();
```
```cpp
Size getImageSize() { return m_imageRect.size();
```
```cpp
Rect getImageRect() { return m_imageRect; } Color getImageColor() { return m_imageColor; } bool isImageFixedRatio() { return m_imageFixedRatio; } bool isImageSmooth() { return m_imageSmooth; } bool isImageAutoResize() { return m_imageAutoResize; } int getImageBorderTop() { return m_imageBorder.top; } int getImageBorderRight() { return m_imageBorder.right; } int getImageBorderBottom() { return m_imageBorder.bottom; } int getImageBorderLeft() { return m_imageBorder.left; } int getImageTextureWidth() { return m_imageTexture ? m_imageTexture->getWidth() : 0; } int getImageTextureHeight() { return m_imageTexture ? m_imageTexture->getHeight() : 0; } std::string getImageShader() { return m_shader; } // text related private: void initText();
```
```cpp
void parseTextStyle(const OTMLNodePtr& styleNode);
```
```cpp
protected:
    virtual void updateText();
```
```cpp
void drawText(const Rect& screenCoords);
```
```cpp
virtual void onTextChange(const std::string& text, const std::string& oldText);
```
```cpp
virtual void onFontChange(const std::string& font);
```
```cpp
public:
    void resizeToText() { setSize(getTextSize());
```
```cpp
void clearText() { setText("");
```
```cpp
void setText(std::string text, bool dontFireLuaCall = false);
```
```cpp
void setColoredText(const std::vector<std::string>& texts, bool dontFireLuaCall = false);
```
```cpp
void setTextAlign(Fw::AlignmentFlag align) { m_textAlign = align; updateText();
```
```cpp
void setTextOffset(const Point& offset) { m_textOffset = offset; updateText();
```
```cpp
void setTextWrap(bool textWrap) { m_textWrap = textWrap; updateText();
```
```cpp
void setTextAutoResize(bool textAutoResize) { m_textHorizontalAutoResize = textAutoResize; m_textVerticalAutoResize = textAutoResize; updateText();
```
```cpp
void setTextHorizontalAutoResize(bool textAutoResize) { m_textHorizontalAutoResize = textAutoResize; updateText();
```
```cpp
void setTextVerticalAutoResize(bool textAutoResize) { m_textVerticalAutoResize = textAutoResize; updateText();
```
```cpp
void setTextOnlyUpperCase(bool textOnlyUpperCase) { m_textOnlyUpperCase = textOnlyUpperCase; setText(m_text);
```
```cpp
void setFont(const std::string& fontName);
```
```cpp
void setShadow(bool shadow) { m_shadow = shadow; } std::string getText() { return m_text; } std::string getDrawText() { return m_drawText; } Fw::AlignmentFlag getTextAlign() { return m_textAlign; } Point getTextOffset() { return m_textOffset; } bool getTextWrap() { return m_textWrap; } std::string getFont() { return m_font->getName();
```
```cpp
Size getTextSize() { return m_font->calculateTextRectSize(m_drawText);
```
# src/framework/ui/uiwidget.h

```cpp
public: UIWidget();
```
```cpp
virtual void draw(const Rect& visibleRect, Fw::DrawPane drawPane);
```
```cpp
protected: virtual void drawSelf(Fw::DrawPane drawPane);
```
```cpp
virtual void drawChildren(const Rect& visibleRect, Fw::DrawPane drawPane);
```
```cpp
public: void addChild(const UIWidgetPtr& child);
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
void setLastFocusReason(Fw::FocusReason reason);
```
```cpp
void setAutoFocusPolicy(Fw::AutoFocusPolicy policy);
```
```cpp
void setVirtualOffset(const Point& offset);
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
protected: bool setState(Fw::WidgetState state, bool on);
```
```cpp
bool hasState(Fw::WidgetState state);
```
```cpp
private: void internalDestroy();
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
protected: virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
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
private: void initBaseStyle();
```
```cpp
void parseBaseStyle(const OTMLNodePtr& styleNode);
```
```cpp
protected: void drawBackground(const Rect& screenCoords);
```
```cpp
void drawBorder(const Rect& screenCoords);
```
```cpp
void drawIcon(const Rect& screenCoords);
```
```cpp
void setIcon(const std::string& iconFile);
```
```cpp
void setCursor(const std::string& cursor);
```
```cpp
private: void initImage();
```
```cpp
void parseImageStyle(const OTMLNodePtr& styleNode);
```
```cpp
protected: void drawImage(const Rect& screenCoords);
```
```cpp
public: void setQRCode(const std::string& code, int border);
```
```cpp
void setImageSource(const std::string& source);
```
```cpp
void setImageSourceBase64(const std::string & data);
```
```cpp
private: void initText();
```
```cpp
void parseTextStyle(const OTMLNodePtr& styleNode);
```
```cpp
protected: virtual void updateText();
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
void setText(std::string text, bool dontFireLuaCall = false);
```
```cpp
void setColoredText(const std::vector<std::string>& texts, bool dontFireLuaCall = false);
```
```cpp
void setFont(const std::string& fontName);
```
```cpp
void set(T value);
```
```cpp
void setClipping(bool clipping);
```
```cpp
void setAutoRepeatDelay(int delay);
```
```cpp
public: void resize(int width, int height);
```
```cpp
void move(int x, int y);
```
```cpp
void rotate(float degrees);
```
```cpp
void hide();
```
```cpp
void show();
```
```cpp
void disable();
```
```cpp
void enable();
```
```cpp
bool isActive();
```
```cpp
bool isEnabled();
```
```cpp
bool isDisabled();
```
```cpp
bool isFocused();
```
```cpp
bool isHovered();
```
```cpp
bool isPressed();
```
```cpp
bool isFirst();
```
```cpp
bool isMiddle();
```
```cpp
bool isLast();
```
```cpp
bool isAlternate();
```
```cpp
bool isChecked();
```
```cpp
bool isOn();
```
```cpp
bool isDragging();
```
```cpp
bool isVisible();
```
```cpp
bool isHidden();
```
```cpp
bool isExplicitlyEnabled();
```
```cpp
bool isExplicitlyVisible();
```
```cpp
bool isAutoDraw();
```
```cpp
bool isFocusable();
```
```cpp
bool isPhantom();
```
```cpp
bool isDraggable();
```
```cpp
bool isFixedSize();
```
```cpp
bool isClipping();
```
```cpp
bool isDestroyed();
```
```cpp
bool hasChildren();
```
```cpp
bool containsMarginPoint(const Point& point);
```
```cpp
bool containsPaddingPoint(const Point& point);
```
```cpp
bool containsPoint(const Point& point);
```
```cpp
std::string getId();
```
```cpp
std::string getSource();
```
```cpp
UIWidgetPtr getParent();
```
```cpp
std::string getParentId();
```
```cpp
UIWidgetPtr getFocusedChild();
```
```cpp
UIWidgetList getChildren();
```
```cpp
UIWidgetPtr getFirstChild();
```
```cpp
UIWidgetPtr getLastChild();
```
```cpp
UILayoutPtr getLayout();
```
```cpp
OTMLNodePtr getStyle();
```
```cpp
int getChildCount();
```
```cpp
Fw::FocusReason getLastFocusReason();
```
```cpp
Fw::AutoFocusPolicy getAutoFocusPolicy();
```
```cpp
int getAutoRepeatDelay();
```
```cpp
Point getVirtualOffset();
```
```cpp
std::string getStyleName();
```
```cpp
Point getLastClickPosition();
```
```cpp
bool isRootChild();
```
```cpp
void setRootChild(bool v);
```
```cpp
public: void setX(int x);
```
```cpp
void setY(int y);
```
```cpp
void setWidth(int width);
```
```cpp
void setHeight(int height);
```
```cpp
void setSize(const Size& size);
```
```cpp
void setPosition(const Point& pos);
```
```cpp
void setColor(const Color& color);
```
```cpp
void setBackgroundColor(const Color& color);
```
```cpp
void setBackgroundOffsetX(int x);
```
```cpp
void setBackgroundOffsetY(int y);
```
```cpp
void setBackgroundOffset(const Point& pos);
```
```cpp
void setBackgroundWidth(int width);
```
```cpp
void setBackgroundHeight(int height);
```
```cpp
void setBackgroundSize(const Size& size);
```
```cpp
void setBackgroundRect(const Rect& rect);
```
```cpp
void setIconColor(const Color& color);
```
```cpp
void setIconOffsetX(int x);
```
```cpp
void setIconOffsetY(int y);
```
```cpp
void setIconOffset(const Point& pos);
```
```cpp
void setIconWidth(int width);
```
```cpp
void setIconHeight(int height);
```
```cpp
void setIconSize(const Size& size);
```
```cpp
void setIconRect(const Rect& rect);
```
```cpp
void setIconClip(const Rect& rect);
```
```cpp
void setIconAlign(Fw::AlignmentFlag align);
```
```cpp
void setBorderWidth(int width);
```
```cpp
void setBorderWidthTop(int width);
```
```cpp
void setBorderWidthRight(int width);
```
```cpp
void setBorderWidthBottom(int width);
```
```cpp
void setBorderWidthLeft(int width);
```
```cpp
void setBorderColor(const Color& color);
```
```cpp
void setBorderColorTop(const Color& color);
```
```cpp
void setBorderColorRight(const Color& color);
```
```cpp
void setBorderColorBottom(const Color& color);
```
```cpp
void setBorderColorLeft(const Color& color);
```
```cpp
void setMargin(int margin);
```
```cpp
void setMarginHorizontal(int margin);
```
```cpp
void setMarginVertical(int margin);
```
```cpp
void setMarginTop(int margin);
```
```cpp
void setMarginRight(int margin);
```
```cpp
void setMarginBottom(int margin);
```
```cpp
void setMarginLeft(int margin);
```
```cpp
void setPadding(int padding);
```
```cpp
void setPaddingHorizontal(int padding);
```
```cpp
void setPaddingVertical(int padding);
```
```cpp
void setPaddingTop(int padding);
```
```cpp
void setPaddingRight(int padding);
```
```cpp
void setPaddingBottom(int padding);
```
```cpp
void setPaddingLeft(int padding);
```
```cpp
void setOpacity(float opacity);
```
```cpp
void setRotation(float degrees);
```
```cpp
void setChangeCursorImage(bool enable);
```
```cpp
int getX();
```
```cpp
int getY();
```
```cpp
Point getPosition();
```
```cpp
int getWidth();
```
```cpp
int getHeight();
```
```cpp
Size getSize();
```
```cpp
Rect getRect();
```
```cpp
Color getColor();
```
```cpp
Color getBackgroundColor();
```
```cpp
int getBackgroundOffsetX();
```
```cpp
int getBackgroundOffsetY();
```
```cpp
Point getBackgroundOffset();
```
```cpp
int getBackgroundWidth();
```
```cpp
int getBackgroundHeight();
```
```cpp
Size getBackgroundSize();
```
```cpp
Rect getBackgroundRect();
```
```cpp
Color getIconColor();
```
```cpp
int getIconOffsetX();
```
```cpp
int getIconOffsetY();
```
```cpp
Point getIconOffset();
```
```cpp
int getIconWidth();
```
```cpp
int getIconHeight();
```
```cpp
Size getIconSize();
```
```cpp
Rect getIconRect();
```
```cpp
Rect getIconClip();
```
```cpp
std::string getIconPath();
```
```cpp
Fw::AlignmentFlag getIconAlign();
```
```cpp
Color getBorderTopColor();
```
```cpp
Color getBorderRightColor();
```
```cpp
Color getBorderBottomColor();
```
```cpp
Color getBorderLeftColor();
```
```cpp
int getBorderTopWidth();
```
```cpp
int getBorderRightWidth();
```
```cpp
int getBorderBottomWidth();
```
```cpp
int getBorderLeftWidth();
```
```cpp
int getMarginTop();
```
```cpp
int getMarginRight();
```
```cpp
int getMarginBottom();
```
```cpp
int getMarginLeft();
```
```cpp
int getPaddingTop();
```
```cpp
int getPaddingRight();
```
```cpp
int getPaddingBottom();
```
```cpp
int getPaddingLeft();
```
```cpp
float getOpacity();
```
```cpp
float getRotation();
```
```cpp
bool isChangingCursorImage();
```
```cpp
void updateImageCache();
```
```cpp
void configureBorderImage();
```
```cpp
void setImageClip(const Rect& clipRect);
```
```cpp
void setImageOffsetX(int x);
```
```cpp
void setImageOffsetY(int y);
```
```cpp
void setImageOffset(const Point& pos);
```
```cpp
void setImageWidth(int width);
```
```cpp
void setImageHeight(int height);
```
```cpp
void setImageSize(const Size& size);
```
```cpp
void setImageRect(const Rect& rect);
```
```cpp
void setImageColor(const Color& color);
```
```cpp
void setImageFixedRatio(bool fixedRatio);
```
```cpp
void setImageRepeated(bool repeated);
```
```cpp
void setImageSmooth(bool smooth);
```
```cpp
void setImageAutoResize(bool autoResize);
```
```cpp
void setImageBorderTop(int border);
```
```cpp
void setImageBorderRight(int border);
```
```cpp
void setImageBorderBottom(int border);
```
```cpp
void setImageBorderLeft(int border);
```
```cpp
void setImageBorder(int border);
```
```cpp
void setImageShader(const std::string& str);
```
```cpp
Rect getImageClip();
```
```cpp
int getImageOffsetX();
```
```cpp
int getImageOffsetY();
```
```cpp
Point getImageOffset();
```
```cpp
int getImageWidth();
```
```cpp
int getImageHeight();
```
```cpp
Size getImageSize();
```
```cpp
Rect getImageRect();
```
```cpp
Color getImageColor();
```
```cpp
bool isImageFixedRatio();
```
```cpp
bool isImageSmooth();
```
```cpp
bool isImageAutoResize();
```
```cpp
int getImageBorderTop();
```
```cpp
int getImageBorderRight();
```
```cpp
int getImageBorderBottom();
```
```cpp
int getImageBorderLeft();
```
```cpp
int getImageTextureWidth();
```
```cpp
int getImageTextureHeight();
```
```cpp
std::string getImageShader();
```
```cpp
public: void resizeToText();
```
```cpp
void clearText();
```
```cpp
void setTextAlign(Fw::AlignmentFlag align);
```
```cpp
void setTextOffset(const Point& offset);
```
```cpp
void setTextWrap(bool textWrap);
```
```cpp
void setTextAutoResize(bool textAutoResize);
```
```cpp
void setTextHorizontalAutoResize(bool textAutoResize);
```
```cpp
void setTextVerticalAutoResize(bool textAutoResize);
```
```cpp
void setTextOnlyUpperCase(bool textOnlyUpperCase);
```
```cpp
void setShadow(bool shadow);
```
```cpp
std::string getText();
```
```cpp
std::string getDrawText();
```
```cpp
Fw::AlignmentFlag getTextAlign();
```
```cpp
Point getTextOffset();
```
```cpp
bool getTextWrap();
```
```cpp
std::string getFont();
```
```cpp
Size getTextSize();
```
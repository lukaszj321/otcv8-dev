# src/framework/core/inputevent.h

```cpp
void reset(Fw::InputEventType eventType = Fw::NoInputEvent) { type = eventType; wheelDirection = Fw::MouseNoWheel; mouseButton = Fw::MouseNoButton; keyCode = Fw::KeyUnknown; keyText = ""; autoRepeatTicks = 0; mouseMoved = Point();
```
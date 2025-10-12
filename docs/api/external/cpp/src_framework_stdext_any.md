# src/framework/stdext/any.h

```cpp
virtual const std::type_info& type() const = 0; virtual placeholder* clone() const = 0; }; template<typename T> struct holder : public placeholder { holder(const T& value) : held(value) { } const std::type_info& type() const { return typeid(T);
```
```cpp
placeholder* clone() const { return new holder(held);
```
```cpp
const T& cast() const; const std::type_info & type() const { return content ? content->type() : typeid(void);
```
```cpp
const T& any_cast(const any& operand) { VALIDATE(operand.type() == typeid(T));
```
```cpp
return static_cast<any::holder<T>*>(operand.content)->held; } template<typename T> const T& any::cast() const { return any_cast<T>(*this);
```
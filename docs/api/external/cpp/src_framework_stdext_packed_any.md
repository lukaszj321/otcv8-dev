# src/framework/stdext/packed_any.h

```cpp
virtual const std::type_info& type() const = 0; virtual placeholder* clone() const = 0; }; template<typename T> struct holder : public placeholder { holder(const T& value) : held(value) { } const std::type_info& type() const { return typeid(T);
```
```cpp
placeholder* clone() const { return new holder(held);
```
```cpp
template<typename T>
    packed_any(const T& value, typename std::enable_if<(can_pack_in_any<T>::value)>::type* = nullptr) : content(reinterpret_cast<placeholder*>(static_cast<std::size_t>(value))), scalar(true) { } template<typename T> packed_any(const T& value, typename std::enable_if<!(can_pack_in_any<T>::value)>::type* = nullptr) : content(new holder<T>(value)), scalar(false) { } ~packed_any() { if(!scalar && content) delete content; } packed_any& swap(packed_any& rhs) { std::swap(content, rhs.content);
```
```cpp
bool empty() const { return !scalar && !content; } template<typename T> T cast() const; const std::type_info& type() const { if(!scalar) return content ? content->type() : typeid(void);
```
```cpp
else
            return typeid(std::size_t);
```
```cpp
return static_cast<packed_any::holder<T>*>(operand.content)->held; } template<typename T> T packed_any::cast() const { return packed_any_cast<T>(*this);
```
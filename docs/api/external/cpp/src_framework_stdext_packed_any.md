# src/framework/stdext/packed_any.h

```cpp
virtual const std::type_info& type();
```
```cpp
virtual placeholder* clone();
```
```cpp
template<typename T> T cast();
```
```cpp
else return typeid(std::size_t);
```
```cpp
const std::type_info& type();
```
```cpp
placeholder* clone();
```
```cpp
template<typename T> packed_any(const T& value, typename std::enable_if<(can_pack_in_any<T>::value)>::type* = nullptr) : content(reinterpret_cast<placeholder*>(static_cast<std::size_t>(value))), scalar(true);
```
```cpp
template<typename T> packed_any(const T& value, typename std::enable_if<!(can_pack_in_any<T>::value)>::type* = nullptr) : content(new holder<T>(value)), scalar(false);
```
```cpp
packed_any& swap(packed_any& rhs);
```
```cpp
bool empty();
```
```cpp
const std::type_info& type();
```
```cpp
template<typename T> T packed_any::cast();
```
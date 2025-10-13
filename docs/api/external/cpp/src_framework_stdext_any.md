# src/framework/stdext/any.h

```cpp
virtual const std::type_info& type();
```
```cpp
virtual placeholder* clone();
```
```cpp
const T& cast();
```
```cpp
const std::type_info& type();
```
```cpp
placeholder* clone();
```
```cpp
template<typename T> any(const T& value) : content(new holder<T>(value));
```
```cpp
any& swap(any& rhs);
```
```cpp
bool empty();
```
```cpp
const std::type_info & type();
```
```cpp
const T& any_cast(const any& operand);
```
```cpp
const T& any::cast();
```
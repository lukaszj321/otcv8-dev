# src/framework/stdext/shared_object.h

```cpp
stdext::shared_object_ptr<T> static_self_cast() { return stdext::shared_object_ptr<T>(static_cast<T*>(this));
```
```cpp
stdext::shared_object_ptr<T> dynamic_self_cast() { return stdext::shared_object_ptr<T>(dynamic_cast<T*>(this));
```
```cpp
stdext::shared_object_ptr<T> const_self_cast() { return stdext::shared_object_ptr<T>(const_cast<T*>(this));
```
```cpp
T* get_pointer(shared_object_ptr<T> const& p) { return p.get();
```
```cpp
shared_object_ptr<T> static_pointer_cast(shared_object_ptr<U> const& p) { return static_cast<T*>(p.get());
```
```cpp
shared_object_ptr<T> const_pointer_cast(shared_object_ptr<U> const& p) { return const_cast<T*>(p.get());
```
```cpp
shared_object_ptr<T> dynamic_pointer_cast(shared_object_ptr<U> const& p) { return dynamic_cast<T*>(p.get());
```
```cpp
stdext::shared_object_ptr<T> make_shared_object(Args... args) { return stdext::shared_object_ptr<T>(new T(args...));
```
```cpp
void swap(stdext::shared_object_ptr<T>& lhs, stdext::shared_object_ptr<T>& rhs) { lhs.swap(rhs);
```
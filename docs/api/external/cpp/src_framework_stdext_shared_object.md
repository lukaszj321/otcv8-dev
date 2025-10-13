# src/framework/stdext/shared_object.h

```cpp
public: shared_object() : refs(0);
```
```cpp
void add_ref();
```
```cpp
void dec_ref();
```
```cpp
refcount_t ref_count();
```
```cpp
stdext::shared_object_ptr<T> static_self_cast();
```
```cpp
stdext::shared_object_ptr<T> dynamic_self_cast();
```
```cpp
stdext::shared_object_ptr<T> const_self_cast();
```
```cpp
template<class U> shared_object_ptr(shared_object_ptr<U> const& rhs, typename std::enable_if<std::is_convertible<U*,T*>::value, U*>::type = nullptr) : px(rhs.get());
```
```cpp
void reset();
```
```cpp
void reset(T* rhs);
```
```cpp
void swap(shared_object_ptr& rhs);
```
```cpp
T* get();
```
```cpp
refcount_t use_count();
```
```cpp
bool is_unique();
```
```cpp
T& operator*();
```
```cpp
operator unspecified_bool_type();
```
```cpp
private: void add_ref();
```
```cpp
void dec_ref();
```
```cpp
bool operator<(shared_object_ptr<T> const& a, shared_object_ptr<T> const& b);
```
```cpp
T* get_pointer(shared_object_ptr<T> const& p);
```
```cpp
shared_object_ptr<T> static_pointer_cast(shared_object_ptr<U> const& p);
```
```cpp
shared_object_ptr<T> const_pointer_cast(shared_object_ptr<U> const& p);
```
```cpp
shared_object_ptr<T> dynamic_pointer_cast(shared_object_ptr<U> const& p);
```
```cpp
stdext::shared_object_ptr<T> make_shared_object(Args... args);
```
```cpp
void swap(stdext::shared_object_ptr<T>& lhs, stdext::shared_object_ptr<T>& rhs);
```
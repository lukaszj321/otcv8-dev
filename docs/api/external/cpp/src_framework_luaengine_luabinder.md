# src/framework/luaengine/luabinder.h

```cpp
return call_fun_and_push_result<Ret>(f, lua, args...);
```
```cpp
return bind_lambda_fun<F>::call(f);
```
```cpp
return bind_fun(std::function<Ret(Args...)>(f));
```
```cpp
throw LuaException("failed to call a member function because the passed object is nil");
```
```cpp
return mf(obj.get(), args...);
```
```cpp
throw LuaException("failed to call a member function because the passed object is nil");
```
```cpp
return mf(obj, lua);
```
```cpp
static void call(Tuple& tuple, LuaInterface* lua);
```
```cpp
static void call(Tuple& tuple, LuaInterface* lua);
```
```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args);
```
```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args);
```
```cpp
LuaCppFunction bind_fun_specializer(const F& f);
```
Bind different types of functions generating a lambda

```cpp
inline LuaCppFunction bind_fun(const std::function<int(LuaInterface*)>& f);
```
Bind a customized function

```cpp
LuaCppFunction bind_fun(const std::function<Ret(Args...)>& f);
```
Bind a std::function

```cpp
static LuaCppFunction call(const Lambda& f);
```
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, LuaCppFunction>::type bind_fun(const Lambda& f);
```
```cpp
LuaCppFunction bind_fun(Ret (*f)(Args...));
```
Convert to C++ functions pointers to std::function then bind

```cpp
LuaCppFunction bind_mem_fun(Ret (FC::* f)(Args...));
```
Bind member functions

```cpp
LuaCppFunction bind_singleton_mem_fun(Ret (FC::*f)(Args...), C *instance);
```
Bind singleton member functions

```cpp
LuaCppFunction bind_mem_fun(int (C::*f)(LuaInterface*));
```
Bind customized member functions

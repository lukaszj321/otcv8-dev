# src/framework/luaengine/luabinder.h

```cpp
static void call(Tuple& tuple, LuaInterface* lua) { typedef typename std::tuple_element<N-1, Tuple>::type ValueType; std::get<N-1>(tuple) = lua->polymorphicPop<ValueType>();
```
Pack arguments from lua stack into a tuple recursively

```cpp
static void call(Tuple& tuple, LuaInterface* lua) { } }; /// C++ function caller that can push results to lua template<typename Ret, typename F, typename... Args> typename std::enable_if<!std::is_void<Ret>::value, int>::type call_fun_and_push_result(const F& f, LuaInterface* lua, const Args&... args) { Ret ret = f(args...);
```
```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args) { return expand_fun_arguments<N-1,Ret>::call(tuple, f, lua, std::get<N-1>(tuple), args...);
```
C++ void function caller

```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args) { return call_fun_and_push_result<Ret>(f, lua, args...);
```
```cpp
LuaCppFunction bind_fun_specializer(const F& f) { enum { N = std::tuple_size<Tuple>::value }; return [=](LuaInterface* lua) -> int { while(lua->stackSize() != N) { if(lua->stackSize() < N) g_lua.pushNil();
```
Bind different types of functions generating a lambda

```cpp
inline
    LuaCppFunction bind_fun(const std::function<int(LuaInterface*)>& f) { return f; } /// Bind a std::function template<typename Ret, typename... Args> LuaCppFunction bind_fun(const std::function<Ret(Args...)>& f) { typedef typename std::tuple<typename stdext::remove_const_ref<Args>::type...> Tuple; return bind_fun_specializer<typename stdext::remove_const_ref<Ret>::type, decltype(f), Tuple>(f);
```
Bind a customized function

```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, LuaCppFunction>::type bind_fun(const Lambda& f) { typedef decltype(&Lambda::operator()) F; return bind_lambda_fun<F>::call(f);
```
```cpp
LuaCppFunction bind_fun(Ret (*f)(Args...)) { return bind_fun(std::function<Ret(Args...)>(f));
```
Convert to C++ functions pointers to std::function then bind

```cpp
LuaCppFunction bind_mem_fun(Ret (FC::* f)(Args...)) { typedef typename std::tuple<stdext::shared_object_ptr<FC>, typename stdext::remove_const_ref<Args>::type...> Tuple; auto lambda = make_mem_func<Ret,FC>(f);
```
Create member function lambdas

```cpp
LuaCppFunction bind_singleton_mem_fun(Ret (FC::*f)(Args...), C *instance) { typedef typename std::tuple<typename stdext::remove_const_ref<Args>::type...> Tuple; VALIDATE(instance);
```
Bind singleton member functions

```cpp
LuaCppFunction bind_mem_fun(int (C::*f)(LuaInterface*)) { auto mf = std::mem_fn(f);
```
Bind customized member functions

```cpp
return mf(obj, lua);
```
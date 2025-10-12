# src/framework/luaengine/luainterface.h

```cpp
public:
    LuaInterface();
```
```cpp
void init();
```
```cpp
void terminate();
```
```cpp
void registerFunctions();
```
Register core script functions

```cpp
void registerSingletonClass(const std::string& className);
```
```cpp
void registerClass(const std::string& className, const std::string& baseClass = "LuaObject");
```
```cpp
void registerClassStaticFunction(const std::string& className, const std::string& functionName, const LuaCppFunction& function);
```
```cpp
void registerClassMemberFunction(const std::string& className, const std::string& functionName, const LuaCppFunction& function);
```
```cpp
void registerClassMemberField(const std::string& className, const std::string& field, const LuaCppFunction& getFunction, const LuaCppFunction& setFunction);
```
```cpp
void registerGlobalFunction(const std::string& functionName, const LuaCppFunction& function);
```
```cpp
void registerClass() { registerClass(stdext::demangle_class<C>(), stdext::demangle_class<B>());
```
```cpp
void registerClassStaticFunction(const std::string& functionName, const LuaCppFunction& function) { registerClassStaticFunction(stdext::demangle_class<C>(), functionName, function);
```
```cpp
void registerClassMemberFunction(const std::string& functionName, const LuaCppFunction& function) { registerClassMemberFunction(stdext::demangle_class<C>(), functionName, function);
```
```cpp
void registerClassMemberField(const std::string& field, const LuaCppFunction& getFunction, const LuaCppFunction& setFunction) { registerClassMemberField(stdext::demangle_class<C>(), field, getFunction, setFunction);
```
```cpp
void bindSingletonFunction(const std::string& functionName, F C::*function, C *instance);
```
```cpp
void bindSingletonFunction(const std::string& className, const std::string& functionName, F C::* function, C* instance);
```
```cpp
void bindSingletonFunction(const std::string& className, const std::string& functionName, const F& function);
```
```cpp
void bindClassStaticFunction(const std::string& functionName, const F& function);
```
```cpp
void bindClassStaticFunction(const std::string& className, const std::string& functionName, const F& function);
```
```cpp
void bindClassMemberFunction(const std::string& functionName, F FC::*function);
```
```cpp
void bindClassMemberFunction(const std::string& className, const std::string& functionName, F FC::*function);
```
```cpp
void bindClassMemberField(const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```
```cpp
void bindClassMemberField(const std::string& className, const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```
```cpp
void bindClassMemberGetField(const std::string& fieldName, F FC::*getFunction);
```
```cpp
void bindClassMemberGetField(const std::string& className, const std::string& fieldName, F FC::*getFunction);
```
```cpp
void bindClassMemberSetField(const std::string& fieldName, F FC::*setFunction);
```
```cpp
void bindClassMemberSetField(const std::string& className, const std::string& fieldName, F FC::*setFunction);
```
```cpp
void bindGlobalFunction(const std::string& functionName, const F& function);
```
```cpp
static int luaObjectGetEvent(LuaInterface* lua);
```
Metamethod that will retrieve fields values (that include functions) from the object when using '.' or ':'

```cpp
static int luaObjectSetEvent(LuaInterface* lua);
```
Metamethod that is called when setting a field of the object by using the keyword '='

```cpp
static int luaObjectEqualEvent(LuaInterface* lua);
```
Metamethod that will check equality of objects by using the keyword '=='

```cpp
static int luaObjectCollectEvent(LuaInterface* lua);
```
Metamethod that is called every two lua garbage collections
for any LuaObject that have no references left in lua environment
anymore, thus this creates the possibility of holding an object
existence by lua until it got no references left

```cpp
bool safeRunScript(const std::string& fileName);
```
Loads and runs a script, any errors are printed to stdout and returns false

```cpp
void runScript(const std::string& fileName);
```
Loads and runs a script
@exception LuaException is thrown on any lua error

```cpp
void runBuffer(const std::string& buffer, const std::string& source);
```
Loads and runs the script from buffer
@exception LuaException is thrown on any lua error

```cpp
void loadScript(const std::string& fileName);
```
Loads a script file and pushes it's main function onto stack,
@exception LuaException is thrown on any lua error

```cpp
void loadFunction(const std::string& buffer, const std::string& source = "lua function buffer");
```
Loads a function from buffer and pushes it onto stack,
@exception LuaException is thrown on any lua error

```cpp
void evaluateExpression(const std::string& expression, const std::string& source = "lua expression");
```
Evaluates a lua expression and pushes the result value onto the stack
@exception LuaException is thrown on any lua error

```cpp
std::string traceback(const std::string& errorMessage = "", int level = 0);
```
Generates a traceback message for the current call stack
@param errorMessage is an additional error message
@param level is the level of the traceback, 0 means trace from calling function
@return the generated traceback message

```cpp
void throwError(const std::string& message);
```
Throw a lua error if inside a lua call or generates an C++ stdext::exception
@param message is the error message wich will be displayed before the error traceback
@exception stdext::exception is thrown with the error message if the error is not captured by lua

```cpp
std::string getCurrentSourcePath(int level = 0);
```
Searches for the source of the current running function

```cpp
std::string getCurrentFunction(int level = 0);
```
gets current function name

```cpp
int safeCall(int numArgs = 0, int numRets = -1, const std::shared_ptr<std::string>& error = nullptr);
```
@brief Calls a function
The function and arguments must be on top of the stack in order,
results are pushed onto the stack.
@exception LuaException is thrown on any lua error
@return number of results

```cpp
int signalCall(int numArgs = 0, int numRets = -1);
```
Same as safeCall but catches exceptions and can also calls a table of functions,
if any error occurs it will be reported to stdout and returns 0 results
@param requestedResults is the number of results requested to pushes onto the stack,
if supplied, the call will always pushes that number of results, even if it fails

```cpp
int newSandboxEnv();
```
@brief Creates a new environment table
The new environment table is redirected to the global environment (aka _G),
this allows to access global variables from _G in the new environment and
prevents new variables in this new environment to be set on the global environment

```cpp
int luaCallGlobalField(const std::string& global, const std::string& field, const T&... args);
```
```cpp
void callGlobalField(const std::string& global, const std::string& field, const T&... args);
```
```cpp
int polymorphicPush(const T& v, const Args&... args);
```
```cpp
int polymorphicPush() { return 0; } /// Casts a value from stack to any type /// @exception LuaBadValueCastException thrown if the cast fails template<class T> T castValue(int index = -1);
```
```cpp
int LuaInterface::polymorphicPush(const T& v, const Args&... args) { int r = push_luavalue(v);
```
Same as castValue but also pops

```cpp
void LuaInterface::bindSingletonFunction(const std::string& functionName, F C::*function, C *instance) { registerClassStaticFunction<C>(functionName, luabinder::bind_singleton_mem_fun(function, instance));
```
```cpp
void LuaInterface::bindSingletonFunction(const std::string& className, const std::string& functionName, F C::*function, C *instance) { registerClassStaticFunction(className, functionName, luabinder::bind_singleton_mem_fun(function, instance));
```
```cpp
void LuaInterface::bindSingletonFunction(const std::string& className, const std::string& functionName, const F& function) { registerClassStaticFunction(className, functionName, luabinder::bind_fun(function));
```
```cpp
void LuaInterface::bindClassStaticFunction(const std::string& functionName, const F& function) { registerClassStaticFunction<C>(functionName, luabinder::bind_fun(function));
```
```cpp
void LuaInterface::bindClassStaticFunction(const std::string& className, const std::string& functionName, const F& function) { registerClassStaticFunction(className, functionName, luabinder::bind_fun(function));
```
```cpp
void LuaInterface::bindClassMemberFunction(const std::string& functionName, F FC::*function) { registerClassMemberFunction<C>(functionName, luabinder::bind_mem_fun<C>(function));
```
```cpp
void LuaInterface::bindClassMemberFunction(const std::string& className, const std::string& functionName, F FC::*function) { registerClassMemberFunction(className, functionName, luabinder::bind_mem_fun<C>(function));
```
```cpp
void LuaInterface::bindClassMemberField(const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction) { registerClassMemberField<C>(fieldName, luabinder::bind_mem_fun<C>(getFunction), luabinder::bind_mem_fun<C>(setFunction));
```
```cpp
void LuaInterface::bindClassMemberField(const std::string& className, const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction) { registerClassMemberField(className, fieldName, luabinder::bind_mem_fun<C>(getFunction), luabinder::bind_mem_fun<C>(setFunction));
```
```cpp
void LuaInterface::bindClassMemberGetField(const std::string& fieldName, F FC::*getFunction) { registerClassMemberField<C>(fieldName, luabinder::bind_mem_fun<C>(getFunction), LuaCppFunction());
```
```cpp
void LuaInterface::bindClassMemberGetField(const std::string& className, const std::string& fieldName, F FC::*getFunction) { registerClassMemberField(className, fieldName, luabinder::bind_mem_fun<C>(getFunction), LuaCppFunction());
```
```cpp
void LuaInterface::bindClassMemberSetField(const std::string& fieldName, F FC::*setFunction) { registerClassMemberField<C>(fieldName, LuaCppFunction(), luabinder::bind_mem_fun<C>(setFunction));
```
```cpp
void LuaInterface::bindClassMemberSetField(const std::string& className, const std::string& fieldName, F FC::*setFunction) { registerClassMemberField(className, fieldName, LuaCppFunction(), luabinder::bind_mem_fun<C>(setFunction));
```
```cpp
void LuaInterface::bindGlobalFunction(const std::string& functionName, const F& function) { registerGlobalFunction(functionName, luabinder::bind_fun(function));
```
```cpp
int LuaInterface::luaCallGlobalField(const std::string& global, const std::string& field, const T&... args) { AutoStat s(STATS_LUA, std::string(global) + ":" + field);
```
```cpp
void LuaInterface::callGlobalField(const std::string& global, const std::string& field, const T&... args) { int rets = luaCallGlobalField(global, field, args...);
```
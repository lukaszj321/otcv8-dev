# src/framework/luaengine/luainterface.h

```cpp
typedef int(*LuaCFunction) (lua_State *L);
```
```cpp
public: LuaInterface();
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
static int luaScriptLoader(lua_State* L);
```
Load scripts requested by lua 'require'

```cpp
static int lua_dofile(lua_State* L);
```
Run scripts requested by lua 'dofile'

```cpp
static int lua_dofiles(lua_State* L);
```
Run scripts requested by lua 'dofiles'

```cpp
static int lua_loadfile(lua_State* L);
```
Run scripts requested by lua 'dofiles'

```cpp
static int luaErrorHandler(lua_State* L);
```
Handle lua errors from safeCall

```cpp
static int luaCppFunctionCallback(lua_State* L);
```
Handle bound cpp functions callbacks

```cpp
static int luaCollectCppFunction(lua_State* L);
```
Collect bound cpp function pointers

```cpp
public: void createLuaState();
```
```cpp
void closeLuaState();
```
```cpp
void collectGarbage();
```
```cpp
void loadBuffer(const std::string& buffer, const std::string& source);
```
```cpp
std::string generateByteCode(const std::string & buffer, std::string source);
```
```cpp
int pcall(int numArgs = 0, int numRets = 0, int errorFuncIndex = 0);
```
```cpp
void call(int numArgs = 0, int numRets = 0);
```
```cpp
void error();
```
```cpp
int ref();
```
```cpp
int weakRef();
```
```cpp
void unref(int ref);
```
```cpp
const char* typeName(int index = -1);
```
```cpp
std::string functionSourcePath();
```
```cpp
std::string functionSource();
```
```cpp
void insert(int index);
```
```cpp
void remove(int index);
```
```cpp
bool next(int index = -2);
```
```cpp
void getStackFunction(int level = 0);
```
```cpp
void getRef(int ref);
```
```cpp
void getWeakRef(int weakRef);
```
```cpp
void setGlobalEnvironment(int env);
```
```cpp
void setMetatable(int index = -2);
```
```cpp
void getMetatable(int index = -1);
```
```cpp
void getField(const char* key, int index = -1);
```
```cpp
void setField(const char* key, int index = -2);
```
```cpp
void getTable(int index = -2);
```
```cpp
void setTable(int index = -3);
```
```cpp
void clearTable(int index = -1);
```
```cpp
void getEnv(int index = -1);
```
```cpp
void setEnv(int index = -2);
```
```cpp
void getGlobal(const std::string& key);
```
```cpp
void getGlobalField(const std::string& globalKey, const std::string& fieldKey);
```
```cpp
void setGlobal(const std::string& key);
```
```cpp
void rawGet(int index = -1);
```
```cpp
void rawGeti(int n, int index = -1);
```
```cpp
void rawSet(int index = -3);
```
```cpp
void rawSeti(int n, int index = -2);
```
```cpp
void newTable();
```
```cpp
void createTable(int narr, int nrec);
```
```cpp
void* newUserdata(int size);
```
```cpp
void pop(int n = 1);
```
```cpp
long popInteger();
```
```cpp
double popNumber();
```
```cpp
bool popBoolean();
```
```cpp
std::string popString();
```
```cpp
void* popUserdata();
```
```cpp
void* popUpvalueUserdata();
```
```cpp
LuaObjectPtr popObject();
```
```cpp
void pushNil();
```
```cpp
void pushInteger(long v);
```
```cpp
void pushNumber(double v);
```
```cpp
void pushBoolean(bool v);
```
```cpp
void pushCString(const char* v);
```
```cpp
void pushString(const std::string& v);
```
```cpp
void pushLightUserdata(void* p);
```
```cpp
void pushThread();
```
```cpp
void pushValue(int index = -1);
```
```cpp
void pushObject(const LuaObjectPtr& obj);
```
```cpp
void pushCFunction(LuaCFunction func, int n = 0);
```
```cpp
void pushCppFunction(const LuaCppFunction& func);
```
```cpp
bool isNil(int index = -1);
```
```cpp
bool isBoolean(int index = -1);
```
```cpp
bool isNumber(int index = -1);
```
```cpp
bool isString(int index = -1);
```
```cpp
bool isTable(int index = -1);
```
```cpp
bool isFunction(int index = -1);
```
```cpp
bool isCFunction(int index = -1);
```
```cpp
bool isUserdata(int index = -1);
```
```cpp
bool toBoolean(int index = -1);
```
```cpp
int toInteger(int index = -1);
```
```cpp
double toNumber(int index = -1);
```
```cpp
const char* toCString(int index = -1);
```
```cpp
std::string toString(int index = -1);
```
```cpp
void* toUserdata(int index = -1);
```
```cpp
LuaObjectPtr toObject(int index = -1);
```
```cpp
int getTop();
```
```cpp
std::string getSource(int level = 2);
```
```cpp
void loadFiles(std::string directory, bool recursive = false, std::string contains = "");
```
```cpp
int polymorphicPush(const T& v, const Args&... args);
```
Pushes any type onto the stack

```cpp
template<class T> T castValue(int index = -1);
```
Casts a value from stack to any type
@exception LuaBadValueCastException thrown if the cast fails

```cpp
throw LuaBadValueCastException(typeName(index), stdext::demangle_type<T>());
```
```cpp
AutoStat s(STATS_LUA, std::string(global) + ":" + field);
```
```cpp
void registerClass();
```
```cpp
void registerClassStaticFunction(const std::string& functionName, const LuaCppFunction& function);
```
```cpp
void registerClassMemberFunction(const std::string& functionName, const LuaCppFunction& function);
```
```cpp
void registerClassMemberField(const std::string& field, const LuaCppFunction& getFunction, const LuaCppFunction& setFunction);
```
```cpp
bool isInCppCallback();
```
```cpp
void useValue();
```
```cpp
void checkStack();
```
```cpp
int getGlobalEnvironment();
```
```cpp
void resetGlobalEnvironment();
```
```cpp
void getField(const std::string& key, int index = -1);
```
```cpp
void setField(const std::string& key, int index = -2);
```
```cpp
bool isLuaFunction(int index = -1);
```
```cpp
int stackSize();
```
```cpp
void clearStack();
```
```cpp
bool hasIndex(int index);
```
```cpp
int polymorphicPush();
```
```cpp
template<class T> T polymorphicPop();
```
Same as castValue but also pops

```cpp
int LuaInterface::polymorphicPush(const T& v, const Args&... args);
```
```cpp
void LuaInterface::bindSingletonFunction(const std::string& functionName, F C::*function, C *instance);
```
```cpp
void LuaInterface::bindSingletonFunction(const std::string& className, const std::string& functionName, F C::*function, C *instance);
```
```cpp
void LuaInterface::bindSingletonFunction(const std::string& className, const std::string& functionName, const F& function);
```
```cpp
void LuaInterface::bindClassStaticFunction(const std::string& functionName, const F& function);
```
```cpp
void LuaInterface::bindClassStaticFunction(const std::string& className, const std::string& functionName, const F& function);
```
```cpp
void LuaInterface::bindClassMemberFunction(const std::string& functionName, F FC::*function);
```
```cpp
void LuaInterface::bindClassMemberFunction(const std::string& className, const std::string& functionName, F FC::*function);
```
```cpp
void LuaInterface::bindClassMemberField(const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```
```cpp
void LuaInterface::bindClassMemberField(const std::string& className, const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```
```cpp
void LuaInterface::bindClassMemberGetField(const std::string& fieldName, F FC::*getFunction);
```
```cpp
void LuaInterface::bindClassMemberGetField(const std::string& className, const std::string& fieldName, F FC::*getFunction);
```
```cpp
void LuaInterface::bindClassMemberSetField(const std::string& fieldName, F FC::*setFunction);
```
```cpp
void LuaInterface::bindClassMemberSetField(const std::string& className, const std::string& fieldName, F FC::*setFunction);
```
```cpp
void LuaInterface::bindGlobalFunction(const std::string& functionName, const F& function);
```
```cpp
template<class T> T LuaInterface::castValue(int index);
```
```cpp
int LuaInterface::luaCallGlobalField(const std::string& global, const std::string& field, const T&... args);
```
```cpp
void LuaInterface::callGlobalField(const std::string& global, const std::string& field, const T&... args);
```
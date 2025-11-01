---
title: "src/framework/luaengine/luainterface.h"
source_file: "src/framework/luaengine/luainterface.h"
generated_at: "2025-11-01T08:29:23.708Z"
doc_type: "cpp_api"
---

# src/framework/luaengine/luainterface.h

(int)=
## `int`

**Signature:**
```cpp
typedef int(*LuaCFunction) (lua_State *L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `*LuaCFunction) (lua_State *L` | - | - |

**Returns:**
- `typedef`

---

(luainterface)=
## `LuaInterface`

**Signature:**
```cpp
public: LuaInterface();
```

---

(init)=
## `init`

**Signature:**
```cpp
void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(registerfunctions)=
## `registerFunctions`

Register core script functions

**Signature:**
```cpp
void registerFunctions();
```

---

(registersingletonclass)=
## `registerSingletonClass`

**Signature:**
```cpp
void registerSingletonClass(const std::string& className);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |

---

(registerclass)=
## `registerClass`

**Signature:**
```cpp
void registerClass(const std::string& className, const std::string& baseClass = "LuaObject");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `className` |  | - |
| `const std::string&` | `baseClass` | `"LuaObject"` | - |

---

(registerclassstaticfunction)=
## `registerClassStaticFunction`

**Signature:**
```cpp
void registerClassStaticFunction(const std::string& className, const std::string& functionName, const LuaCppFunction& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `const LuaCppFunction&` | `function` | - |

---

(registerclassmemberfunction)=
## `registerClassMemberFunction`

**Signature:**
```cpp
void registerClassMemberFunction(const std::string& className, const std::string& functionName, const LuaCppFunction& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `const LuaCppFunction&` | `function` | - |

---

(registerclassmemberfield)=
## `registerClassMemberField`

**Signature:**
```cpp
void registerClassMemberField(const std::string& className, const std::string& field, const LuaCppFunction& getFunction, const LuaCppFunction& setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `field` | - |
| `const LuaCppFunction&` | `getFunction` | - |
| `const LuaCppFunction&` | `setFunction` | - |

---

(registerglobalfunction)=
## `registerGlobalFunction`

**Signature:**
```cpp
void registerGlobalFunction(const std::string& functionName, const LuaCppFunction& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `const LuaCppFunction&` | `function` | - |

---

(bindsingletonfunction)=
## `bindSingletonFunction`

**Signature:**
```cpp
void bindSingletonFunction(const std::string& functionName, F C::*function, C *instance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `F C::*function` | - | - |
| `C *instance` | - | - |

---

(bindsingletonfunction-1)=
## `bindSingletonFunction`

**Signature:**
```cpp
void bindSingletonFunction(const std::string& className, const std::string& functionName, F C::* function, C* instance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `F C::*` | `function` | - |
| `C*` | `instance` | - |

---

(bindsingletonfunction-2)=
## `bindSingletonFunction`

**Signature:**
```cpp
void bindSingletonFunction(const std::string& className, const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(bindclassstaticfunction)=
## `bindClassStaticFunction`

**Signature:**
```cpp
void bindClassStaticFunction(const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(bindclassstaticfunction-1)=
## `bindClassStaticFunction`

**Signature:**
```cpp
void bindClassStaticFunction(const std::string& className, const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(bindclassmemberfunction)=
## `bindClassMemberFunction`

**Signature:**
```cpp
void bindClassMemberFunction(const std::string& functionName, F FC::*function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `F FC::*function` | - | - |

---

(bindclassmemberfunction-1)=
## `bindClassMemberFunction`

**Signature:**
```cpp
void bindClassMemberFunction(const std::string& className, const std::string& functionName, F FC::*function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `F FC::*function` | - | - |

---

(bindclassmemberfield)=
## `bindClassMemberField`

**Signature:**
```cpp
void bindClassMemberField(const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fieldName` | - |
| `F1 FC::*getFunction` | - | - |
| `F2 FC::*setFunction` | - | - |

---

(bindclassmemberfield-1)=
## `bindClassMemberField`

**Signature:**
```cpp
void bindClassMemberField(const std::string& className, const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `fieldName` | - |
| `F1 FC::*getFunction` | - | - |
| `F2 FC::*setFunction` | - | - |

---

(bindclassmembergetfield)=
## `bindClassMemberGetField`

**Signature:**
```cpp
void bindClassMemberGetField(const std::string& fieldName, F FC::*getFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fieldName` | - |
| `F FC::*getFunction` | - | - |

---

(bindclassmembergetfield-1)=
## `bindClassMemberGetField`

**Signature:**
```cpp
void bindClassMemberGetField(const std::string& className, const std::string& fieldName, F FC::*getFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `fieldName` | - |
| `F FC::*getFunction` | - | - |

---

(bindclassmembersetfield)=
## `bindClassMemberSetField`

**Signature:**
```cpp
void bindClassMemberSetField(const std::string& fieldName, F FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fieldName` | - |
| `F FC::*setFunction` | - | - |

---

(bindclassmembersetfield-1)=
## `bindClassMemberSetField`

**Signature:**
```cpp
void bindClassMemberSetField(const std::string& className, const std::string& fieldName, F FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `fieldName` | - |
| `F FC::*setFunction` | - | - |

---

(bindglobalfunction)=
## `bindGlobalFunction`

**Signature:**
```cpp
void bindGlobalFunction(const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(luaobjectgetevent)=
## `luaObjectGetEvent`

Metamethod that will retrieve fields values (that include functions) from the object when using '.' or ':'

**Signature:**
```cpp
static int luaObjectGetEvent(LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `LuaInterface*` | `lua` | - |

**Returns:**
- `int`

---

(luaobjectsetevent)=
## `luaObjectSetEvent`

Metamethod that is called when setting a field of the object by using the keyword '='

**Signature:**
```cpp
static int luaObjectSetEvent(LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `LuaInterface*` | `lua` | - |

**Returns:**
- `int`

---

(luaobjectequalevent)=
## `luaObjectEqualEvent`

Metamethod that will check equality of objects by using the keyword '=='

**Signature:**
```cpp
static int luaObjectEqualEvent(LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `LuaInterface*` | `lua` | - |

**Returns:**
- `int`

---

(luaobjectcollectevent)=
## `luaObjectCollectEvent`

Metamethod that is called every two lua garbage collections
for any LuaObject that have no references left in lua environment
anymore, thus this creates the possibility of holding an object
existence by lua until it got no references left

**Signature:**
```cpp
static int luaObjectCollectEvent(LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `LuaInterface*` | `lua` | - |

**Returns:**
- `int`

---

(saferunscript)=
## `safeRunScript`

Loads and runs a script, any errors are printed to stdout and returns false

**Signature:**
```cpp
bool safeRunScript(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `bool`

---

(runscript)=
## `runScript`

Loads and runs a script
@exception LuaException is thrown on any lua error

**Signature:**
```cpp
void runScript(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(runbuffer)=
## `runBuffer`

Loads and runs the script from buffer
@exception LuaException is thrown on any lua error

**Signature:**
```cpp
void runBuffer(const std::string& buffer, const std::string& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |
| `const std::string&` | `source` | - |

---

(loadscript)=
## `loadScript`

Loads a script file and pushes it's main function onto stack,
@exception LuaException is thrown on any lua error

**Signature:**
```cpp
void loadScript(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(loadfunction)=
## `loadFunction`

Loads a function from buffer and pushes it onto stack,
@exception LuaException is thrown on any lua error

**Signature:**
```cpp
void loadFunction(const std::string& buffer, const std::string& source = "lua function buffer");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `buffer` |  | - |
| `const std::string&` | `source` | `"lua function buffer"` | - |

---

(evaluateexpression)=
## `evaluateExpression`

Evaluates a lua expression and pushes the result value onto the stack
@exception LuaException is thrown on any lua error

**Signature:**
```cpp
void evaluateExpression(const std::string& expression, const std::string& source = "lua expression");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `expression` |  | - |
| `const std::string&` | `source` | `"lua expression"` | - |

---

(traceback)=
## `traceback`

Generates a traceback message for the current call stack
@param errorMessage is an additional error message
@param level is the level of the traceback, 0 means trace from calling function
@return the generated traceback message

**Signature:**
```cpp
std::string traceback(const std::string& errorMessage = "", int level = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `errorMessage` | `""` | - |
| `int` | `level` | `0` | - |

**Returns:**
- `std::string`

---

(throwerror)=
## `throwError`

Throw a lua error if inside a lua call or generates an C++ stdext::exception
@param message is the error message wich will be displayed before the error traceback
@exception stdext::exception is thrown with the error message if the error is not captured by lua

**Signature:**
```cpp
void throwError(const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `message` | - |

---

(getcurrentsourcepath)=
## `getCurrentSourcePath`

Searches for the source of the current running function

**Signature:**
```cpp
std::string getCurrentSourcePath(int level = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `level` | `0` | - |

**Returns:**
- `std::string`

---

(getcurrentfunction)=
## `getCurrentFunction`

gets current function name

**Signature:**
```cpp
std::string getCurrentFunction(int level = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `level` | `0` | - |

**Returns:**
- `std::string`

---

(safecall)=
## `safeCall`

@brief Calls a function
The function and arguments must be on top of the stack in order,
results are pushed onto the stack.
@exception LuaException is thrown on any lua error
@return number of results

**Signature:**
```cpp
int safeCall(int numArgs = 0, int numRets = -1, const std::shared_ptr<std::string>& error = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `numArgs` | `0` | - |
| `int` | `numRets` | `-1` | - |
| `const std::shared_ptr&lt;std::string&gt;&` | `error` | `nullptr` | - |

**Returns:**
- `int`

---

(signalcall)=
## `signalCall`

Same as safeCall but catches exceptions and can also calls a table of functions,
if any error occurs it will be reported to stdout and returns 0 results
@param requestedResults is the number of results requested to pushes onto the stack,
if supplied, the call will always pushes that number of results, even if it fails

**Signature:**
```cpp
int signalCall(int numArgs = 0, int numRets = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `numArgs` | `0` | - |
| `int` | `numRets` | `-1` | - |

**Returns:**
- `int`

---

(newsandboxenv)=
## `newSandboxEnv`

@brief Creates a new environment table
The new environment table is redirected to the global environment (aka _G),
this allows to access global variables from _G in the new environment and
prevents new variables in this new environment to be set on the global environment

**Signature:**
```cpp
int newSandboxEnv();
```

**Returns:**
- `int`

---

(luacallglobalfield)=
## `luaCallGlobalField`

**Signature:**
```cpp
int luaCallGlobalField(const std::string& global, const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `global` | - |
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

**Returns:**
- `int`

---

(callglobalfield)=
## `callGlobalField`

**Signature:**
```cpp
void callGlobalField(const std::string& global, const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `global` | - |
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

---

(luascriptloader)=
## `luaScriptLoader`

Load scripts requested by lua 'require'

**Signature:**
```cpp
static int luaScriptLoader(lua_State* L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `lua_State*` | `L` | - |

**Returns:**
- `int`

---

(lua_dofile)=
## `lua_dofile`

Run scripts requested by lua 'dofile'

**Signature:**
```cpp
static int lua_dofile(lua_State* L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `lua_State*` | `L` | - |

**Returns:**
- `int`

---

(lua_dofiles)=
## `lua_dofiles`

Run scripts requested by lua 'dofiles'

**Signature:**
```cpp
static int lua_dofiles(lua_State* L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `lua_State*` | `L` | - |

**Returns:**
- `int`

---

(lua_loadfile)=
## `lua_loadfile`

Run scripts requested by lua 'dofiles'

**Signature:**
```cpp
static int lua_loadfile(lua_State* L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `lua_State*` | `L` | - |

**Returns:**
- `int`

---

(luaerrorhandler)=
## `luaErrorHandler`

Handle lua errors from safeCall

**Signature:**
```cpp
static int luaErrorHandler(lua_State* L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `lua_State*` | `L` | - |

**Returns:**
- `int`

---

(luacppfunctioncallback)=
## `luaCppFunctionCallback`

Handle bound cpp functions callbacks

**Signature:**
```cpp
static int luaCppFunctionCallback(lua_State* L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `lua_State*` | `L` | - |

**Returns:**
- `int`

---

(luacollectcppfunction)=
## `luaCollectCppFunction`

Collect bound cpp function pointers

**Signature:**
```cpp
static int luaCollectCppFunction(lua_State* L);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `lua_State*` | `L` | - |

**Returns:**
- `int`

---

(createluastate)=
## `createLuaState`

**Signature:**
```cpp
public: void createLuaState();
```

---

(closeluastate)=
## `closeLuaState`

**Signature:**
```cpp
void closeLuaState();
```

---

(collectgarbage)=
## `collectGarbage`

**Signature:**
```cpp
void collectGarbage();
```

---

(loadbuffer)=
## `loadBuffer`

**Signature:**
```cpp
void loadBuffer(const std::string& buffer, const std::string& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |
| `const std::string&` | `source` | - |

---

(generatebytecode)=
## `generateByteCode`

**Signature:**
```cpp
std::string generateByteCode(const std::string & buffer, std::string source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string &` | `buffer` | - |
| `std::string` | `source` | - |

**Returns:**
- `std::string`

---

(pcall)=
## `pcall`

**Signature:**
```cpp
int pcall(int numArgs = 0, int numRets = 0, int errorFuncIndex = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `numArgs` | `0` | - |
| `int` | `numRets` | `0` | - |
| `int` | `errorFuncIndex` | `0` | - |

**Returns:**
- `int`

---

(call)=
## `call`

**Signature:**
```cpp
void call(int numArgs = 0, int numRets = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `numArgs` | `0` | - |
| `int` | `numRets` | `0` | - |

---

(error)=
## `error`

**Signature:**
```cpp
void error();
```

---

(ref)=
## `ref`

**Signature:**
```cpp
int ref();
```

**Returns:**
- `int`

---

(weakref)=
## `weakRef`

**Signature:**
```cpp
int weakRef();
```

**Returns:**
- `int`

---

(unref)=
## `unref`

**Signature:**
```cpp
void unref(int ref);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `ref` | - |

---

(typename)=
## `typeName`

**Signature:**
```cpp
const char* typeName(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `const char*`

---

(functionsourcepath)=
## `functionSourcePath`

**Signature:**
```cpp
std::string functionSourcePath();
```

**Returns:**
- `std::string`

---

(functionsource)=
## `functionSource`

**Signature:**
```cpp
std::string functionSource();
```

**Returns:**
- `std::string`

---

(insert)=
## `insert`

**Signature:**
```cpp
void insert(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

---

(remove)=
## `remove`

**Signature:**
```cpp
void remove(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

---

(next)=
## `next`

**Signature:**
```cpp
bool next(int index = -2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-2` | - |

**Returns:**
- `bool`

---

(getstackfunction)=
## `getStackFunction`

**Signature:**
```cpp
void getStackFunction(int level = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `level` | `0` | - |

---

(getref)=
## `getRef`

**Signature:**
```cpp
void getRef(int ref);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `ref` | - |

---

(getweakref)=
## `getWeakRef`

**Signature:**
```cpp
void getWeakRef(int weakRef);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `weakRef` | - |

---

(setglobalenvironment)=
## `setGlobalEnvironment`

**Signature:**
```cpp
void setGlobalEnvironment(int env);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `env` | - |

---

(setmetatable)=
## `setMetatable`

**Signature:**
```cpp
void setMetatable(int index = -2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-2` | - |

---

(getmetatable)=
## `getMetatable`

**Signature:**
```cpp
void getMetatable(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

---

(getfield)=
## `getField`

**Signature:**
```cpp
void getField(const char* key, int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const char*` | `key` |  | - |
| `int` | `index` | `-1` | - |

---

(setfield)=
## `setField`

**Signature:**
```cpp
void setField(const char* key, int index = -2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const char*` | `key` |  | - |
| `int` | `index` | `-2` | - |

---

(gettable)=
## `getTable`

**Signature:**
```cpp
void getTable(int index = -2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-2` | - |

---

(settable)=
## `setTable`

**Signature:**
```cpp
void setTable(int index = -3);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-3` | - |

---

(cleartable)=
## `clearTable`

**Signature:**
```cpp
void clearTable(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

---

(getenv)=
## `getEnv`

**Signature:**
```cpp
void getEnv(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

---

(setenv)=
## `setEnv`

**Signature:**
```cpp
void setEnv(int index = -2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-2` | - |

---

(getglobal)=
## `getGlobal`

**Signature:**
```cpp
void getGlobal(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

---

(getglobalfield)=
## `getGlobalField`

**Signature:**
```cpp
void getGlobalField(const std::string& globalKey, const std::string& fieldKey);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `globalKey` | - |
| `const std::string&` | `fieldKey` | - |

---

(setglobal)=
## `setGlobal`

**Signature:**
```cpp
void setGlobal(const std::string& key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `key` | - |

---

(rawget)=
## `rawGet`

**Signature:**
```cpp
void rawGet(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

---

(rawgeti)=
## `rawGeti`

**Signature:**
```cpp
void rawGeti(int n, int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `n` |  | - |
| `int` | `index` | `-1` | - |

---

(rawset)=
## `rawSet`

**Signature:**
```cpp
void rawSet(int index = -3);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-3` | - |

---

(rawseti)=
## `rawSeti`

**Signature:**
```cpp
void rawSeti(int n, int index = -2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `n` |  | - |
| `int` | `index` | `-2` | - |

---

(newtable)=
## `newTable`

**Signature:**
```cpp
void newTable();
```

---

(createtable)=
## `createTable`

**Signature:**
```cpp
void createTable(int narr, int nrec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `narr` | - |
| `int` | `nrec` | - |

---

(newuserdata)=
## `newUserdata`

**Signature:**
```cpp
void* newUserdata(int size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `size` | - |

**Returns:**
- `void*`

---

(pop)=
## `pop`

**Signature:**
```cpp
void pop(int n = 1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `n` | `1` | - |

---

(popinteger)=
## `popInteger`

**Signature:**
```cpp
long popInteger();
```

**Returns:**
- `long`

---

(popnumber)=
## `popNumber`

**Signature:**
```cpp
double popNumber();
```

**Returns:**
- `double`

---

(popboolean)=
## `popBoolean`

**Signature:**
```cpp
bool popBoolean();
```

**Returns:**
- `bool`

---

(popstring)=
## `popString`

**Signature:**
```cpp
std::string popString();
```

**Returns:**
- `std::string`

---

(popuserdata)=
## `popUserdata`

**Signature:**
```cpp
void* popUserdata();
```

**Returns:**
- `void*`

---

(popupvalueuserdata)=
## `popUpvalueUserdata`

**Signature:**
```cpp
void* popUpvalueUserdata();
```

**Returns:**
- `void*`

---

(popobject)=
## `popObject`

**Signature:**
```cpp
LuaObjectPtr popObject();
```

**Returns:**
- `LuaObjectPtr`

---

(pushnil)=
## `pushNil`

**Signature:**
```cpp
void pushNil();
```

---

(pushinteger)=
## `pushInteger`

**Signature:**
```cpp
void pushInteger(long v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `long` | `v` | - |

---

(pushnumber)=
## `pushNumber`

**Signature:**
```cpp
void pushNumber(double v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `v` | - |

---

(pushboolean)=
## `pushBoolean`

**Signature:**
```cpp
void pushBoolean(bool v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `v` | - |

---

(pushcstring)=
## `pushCString`

**Signature:**
```cpp
void pushCString(const char* v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `v` | - |

---

(pushstring)=
## `pushString`

**Signature:**
```cpp
void pushString(const std::string& v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `v` | - |

---

(pushlightuserdata)=
## `pushLightUserdata`

**Signature:**
```cpp
void pushLightUserdata(void* p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void*` | `p` | - |

---

(pushthread)=
## `pushThread`

**Signature:**
```cpp
void pushThread();
```

---

(pushvalue)=
## `pushValue`

**Signature:**
```cpp
void pushValue(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

---

(pushobject)=
## `pushObject`

**Signature:**
```cpp
void pushObject(const LuaObjectPtr& obj);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const LuaObjectPtr&` | `obj` | - |

---

(pushcfunction)=
## `pushCFunction`

**Signature:**
```cpp
void pushCFunction(LuaCFunction func, int n = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `LuaCFunction` | `func` |  | - |
| `int` | `n` | `0` | - |

---

(pushcppfunction)=
## `pushCppFunction`

**Signature:**
```cpp
void pushCppFunction(const LuaCppFunction& func);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const LuaCppFunction&` | `func` | - |

---

(isnil)=
## `isNil`

**Signature:**
```cpp
bool isNil(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(isboolean)=
## `isBoolean`

**Signature:**
```cpp
bool isBoolean(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(isnumber)=
## `isNumber`

**Signature:**
```cpp
bool isNumber(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(isstring)=
## `isString`

**Signature:**
```cpp
bool isString(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(istable)=
## `isTable`

**Signature:**
```cpp
bool isTable(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(isfunction)=
## `isFunction`

**Signature:**
```cpp
bool isFunction(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(iscfunction)=
## `isCFunction`

**Signature:**
```cpp
bool isCFunction(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(isuserdata)=
## `isUserdata`

**Signature:**
```cpp
bool isUserdata(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(toboolean)=
## `toBoolean`

**Signature:**
```cpp
bool toBoolean(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(tointeger)=
## `toInteger`

**Signature:**
```cpp
int toInteger(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `int`

---

(tonumber)=
## `toNumber`

**Signature:**
```cpp
double toNumber(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `double`

---

(tocstring)=
## `toCString`

**Signature:**
```cpp
const char* toCString(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `const char*`

---

(tostring)=
## `toString`

**Signature:**
```cpp
std::string toString(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `std::string`

---

(touserdata)=
## `toUserdata`

**Signature:**
```cpp
void* toUserdata(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `void*`

---

(toobject)=
## `toObject`

**Signature:**
```cpp
LuaObjectPtr toObject(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `LuaObjectPtr`

---

(gettop)=
## `getTop`

**Signature:**
```cpp
int getTop();
```

**Returns:**
- `int`

---

(getsource)=
## `getSource`

**Signature:**
```cpp
std::string getSource(int level = 2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `level` | `2` | - |

**Returns:**
- `std::string`

---

(loadfiles)=
## `loadFiles`

**Signature:**
```cpp
void loadFiles(std::string directory, bool recursive = false, std::string contains = "");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `std::string` | `directory` |  | - |
| `bool` | `recursive` | `false` | - |
| `std::string` | `contains` | `""` | - |

---

(polymorphicpush)=
## `polymorphicPush`

Pushes any type onto the stack

**Signature:**
```cpp
int polymorphicPush(const T& v, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `v` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(castvalue)=
## `castValue`

Casts a value from stack to any type
@exception LuaBadValueCastException thrown if the cast fails

**Signature:**
```cpp
template<class T> T castValue(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `template&lt;class T&gt; T`

---

(luabadvaluecastexception)=
## `LuaBadValueCastException`

**Signature:**
```cpp
throw LuaBadValueCastException(typeName(index), stdext::demangle_type<T>());
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `typeName(index)` | - | - |
| `stdext::demangle_type&lt;T&gt;()` | - | - |

**Returns:**
- `throw`

---

(s)=
## `s`

**Signature:**
```cpp
AutoStat s(STATS_LUA, std::string(global) + ":" + field);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `STATS_LUA` | - | - |
| `std::string(global) + ":" +` | `field` | - |

**Returns:**
- `AutoStat`

---

(registerclass-1)=
## `registerClass`

**Signature:**
```cpp
void registerClass();
```

---

(registerclassstaticfunction-1)=
## `registerClassStaticFunction`

**Signature:**
```cpp
void registerClassStaticFunction(const std::string& functionName, const LuaCppFunction& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `const LuaCppFunction&` | `function` | - |

---

(registerclassmemberfunction-1)=
## `registerClassMemberFunction`

**Signature:**
```cpp
void registerClassMemberFunction(const std::string& functionName, const LuaCppFunction& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `const LuaCppFunction&` | `function` | - |

---

(registerclassmemberfield-1)=
## `registerClassMemberField`

**Signature:**
```cpp
void registerClassMemberField(const std::string& field, const LuaCppFunction& getFunction, const LuaCppFunction& setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `field` | - |
| `const LuaCppFunction&` | `getFunction` | - |
| `const LuaCppFunction&` | `setFunction` | - |

---

(isincppcallback)=
## `isInCppCallback`

**Signature:**
```cpp
bool isInCppCallback();
```

**Returns:**
- `bool`

---

(usevalue)=
## `useValue`

**Signature:**
```cpp
void useValue();
```

---

(checkstack)=
## `checkStack`

**Signature:**
```cpp
void checkStack();
```

---

(getglobalenvironment)=
## `getGlobalEnvironment`

**Signature:**
```cpp
int getGlobalEnvironment();
```

**Returns:**
- `int`

---

(resetglobalenvironment)=
## `resetGlobalEnvironment`

**Signature:**
```cpp
void resetGlobalEnvironment();
```

---

(getfield-1)=
## `getField`

**Signature:**
```cpp
void getField(const std::string& key, int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `key` |  | - |
| `int` | `index` | `-1` | - |

---

(setfield-1)=
## `setField`

**Signature:**
```cpp
void setField(const std::string& key, int index = -2);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `key` |  | - |
| `int` | `index` | `-2` | - |

---

(isluafunction)=
## `isLuaFunction`

**Signature:**
```cpp
bool isLuaFunction(int index = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `index` | `-1` | - |

**Returns:**
- `bool`

---

(stacksize)=
## `stackSize`

**Signature:**
```cpp
int stackSize();
```

**Returns:**
- `int`

---

(clearstack)=
## `clearStack`

**Signature:**
```cpp
void clearStack();
```

---

(hasindex)=
## `hasIndex`

**Signature:**
```cpp
bool hasIndex(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

**Returns:**
- `bool`

---

(polymorphicpush-1)=
## `polymorphicPush`

**Signature:**
```cpp
int polymorphicPush();
```

**Returns:**
- `int`

---

(polymorphicpop)=
## `polymorphicPop`

Same as castValue but also pops

**Signature:**
```cpp
template<class T> T polymorphicPop();
```

**Returns:**
- `template&lt;class T&gt; T`

---

(luainterfacepolymorphicpush)=
## `LuaInterface::polymorphicPush`

**Signature:**
```cpp
int LuaInterface::polymorphicPush(const T& v, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `v` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(luainterfacebindsingletonfunction)=
## `LuaInterface::bindSingletonFunction`

**Signature:**
```cpp
void LuaInterface::bindSingletonFunction(const std::string& functionName, F C::*function, C *instance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `F C::*function` | - | - |
| `C *instance` | - | - |

---

(luainterfacebindsingletonfunction-1)=
## `LuaInterface::bindSingletonFunction`

**Signature:**
```cpp
void LuaInterface::bindSingletonFunction(const std::string& className, const std::string& functionName, F C::*function, C *instance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `F C::*function` | - | - |
| `C *instance` | - | - |

---

(luainterfacebindsingletonfunction-2)=
## `LuaInterface::bindSingletonFunction`

**Signature:**
```cpp
void LuaInterface::bindSingletonFunction(const std::string& className, const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(luainterfacebindclassstaticfunction)=
## `LuaInterface::bindClassStaticFunction`

**Signature:**
```cpp
void LuaInterface::bindClassStaticFunction(const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(luainterfacebindclassstaticfunction-1)=
## `LuaInterface::bindClassStaticFunction`

**Signature:**
```cpp
void LuaInterface::bindClassStaticFunction(const std::string& className, const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(luainterfacebindclassmemberfunction)=
## `LuaInterface::bindClassMemberFunction`

**Signature:**
```cpp
void LuaInterface::bindClassMemberFunction(const std::string& functionName, F FC::*function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `F FC::*function` | - | - |

---

(luainterfacebindclassmemberfunction-1)=
## `LuaInterface::bindClassMemberFunction`

**Signature:**
```cpp
void LuaInterface::bindClassMemberFunction(const std::string& className, const std::string& functionName, F FC::*function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `functionName` | - |
| `F FC::*function` | - | - |

---

(luainterfacebindclassmemberfield)=
## `LuaInterface::bindClassMemberField`

**Signature:**
```cpp
void LuaInterface::bindClassMemberField(const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fieldName` | - |
| `F1 FC::*getFunction` | - | - |
| `F2 FC::*setFunction` | - | - |

---

(luainterfacebindclassmemberfield-1)=
## `LuaInterface::bindClassMemberField`

**Signature:**
```cpp
void LuaInterface::bindClassMemberField(const std::string& className, const std::string& fieldName, F1 FC::*getFunction, F2 FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `fieldName` | - |
| `F1 FC::*getFunction` | - | - |
| `F2 FC::*setFunction` | - | - |

---

(luainterfacebindclassmembergetfield)=
## `LuaInterface::bindClassMemberGetField`

**Signature:**
```cpp
void LuaInterface::bindClassMemberGetField(const std::string& fieldName, F FC::*getFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fieldName` | - |
| `F FC::*getFunction` | - | - |

---

(luainterfacebindclassmembergetfield-1)=
## `LuaInterface::bindClassMemberGetField`

**Signature:**
```cpp
void LuaInterface::bindClassMemberGetField(const std::string& className, const std::string& fieldName, F FC::*getFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `fieldName` | - |
| `F FC::*getFunction` | - | - |

---

(luainterfacebindclassmembersetfield)=
## `LuaInterface::bindClassMemberSetField`

**Signature:**
```cpp
void LuaInterface::bindClassMemberSetField(const std::string& fieldName, F FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fieldName` | - |
| `F FC::*setFunction` | - | - |

---

(luainterfacebindclassmembersetfield-1)=
## `LuaInterface::bindClassMemberSetField`

**Signature:**
```cpp
void LuaInterface::bindClassMemberSetField(const std::string& className, const std::string& fieldName, F FC::*setFunction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `className` | - |
| `const std::string&` | `fieldName` | - |
| `F FC::*setFunction` | - | - |

---

(luainterfacebindglobalfunction)=
## `LuaInterface::bindGlobalFunction`

**Signature:**
```cpp
void LuaInterface::bindGlobalFunction(const std::string& functionName, const F& function);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `functionName` | - |
| `const F&` | `function` | - |

---

(luainterfacecastvalue)=
## `LuaInterface::castValue`

**Signature:**
```cpp
template<class T> T LuaInterface::castValue(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

**Returns:**
- `template&lt;class T&gt; T`

---

(luainterfaceluacallglobalfield)=
## `LuaInterface::luaCallGlobalField`

**Signature:**
```cpp
int LuaInterface::luaCallGlobalField(const std::string& global, const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `global` | - |
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

**Returns:**
- `int`

---

(luainterfacecallglobalfield)=
## `LuaInterface::callGlobalField`

**Signature:**
```cpp
void LuaInterface::callGlobalField(const std::string& global, const std::string& field, const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `global` | - |
| `const std::string&` | `field` | - |
| `const T&...` | `args` | - |

---

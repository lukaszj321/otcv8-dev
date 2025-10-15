---
doc_id: "authoring.15_vc16.index"
source_path: "vc16/**"
source_sha: "HEAD"
last_sync_iso: "2025-10-15T22:21:56Z"
doc_class: "guide"
language: "pl"
title: "VC16 / ANGLE — Build Windows i distribucja runtime"
summary: "Przewodnik po projekcie Visual C++ 2019 dla OTClient v8: solucje, konfiguracje (Debug/Release), toolset v142, ANGLE (libGLESv2/libEGL) i deployment na Windows 7-11."
tags: ["otclient", "vc16", "visual-studio", "angle", "opengl-es", "windows", "build", "rag"]
---

# VC16 / ANGLE — Build Windows i distribucja runtime

**Cel rozdziału:** Udokumentować projekt Visual C++ 2019 (VC16) dla OTClient v8: struktura solucji, konfiguracje build (Debug/Release/x86/x64), integracja ANGLE (OpenGL ES na Direct3D), zależności biblioteczne i deployment na różne wersje Windows.

```{contents} Spis treści
:depth: 3
:local:
```

:::{admonition} TL;DR
:class: tip
Projekt VC16 używa Visual Studio 2019 (toolset v142) i ANGLE do renderowania OpenGL ES przez Direct3D 11. Wymaga dystrybucji `libEGL.dll` i `libGLESv2.dll` wraz z EXE.
:::

## Wprowadzenie domenowe

Port Windows OTClient v8 to **natywna aplikacja Win32/x64** kompilowana Visual C++ 2019 (v142). Kluczowe cechy:

1. **ANGLE integration** - OpenGL ES → DirectX translation layer
2. **Multi-config** - Debug/Release, x86/x64 (4 kombinacje)
3. **Static/Dynamic linking** - zależności mogą być static (.lib) lub dynamic (.dll)
4. **Windows SDK 10.0** - target platform Windows 7-11

### Komponenty projektu

```
vc16/
  otclient.sln           # Solution file (Visual Studio)
  otclient.vcxproj       # Project file (C++ settings)
  otclient.vcxproj.filters  # Folder organization in IDE
  settings.props         # Shared property sheet (paths, defines)
  angle/                 # ANGLE libraries and headers
    include/             # EGL, GLES2, GLES3 headers
    lib/                 # libEGL.dll, libGLESv2.dll + .lib
```

## Architektura / Przepływ

### Diagram build pipeline

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
flowchart TD
    SRC[src/** C++ sources]
    VCXPROJ[otclient.vcxproj]
    MSBUILD[MSBuild.exe]
    
    SRC --> VCXPROJ
    VCXPROJ --> MSBUILD
    
    MSBUILD -->|x86 Debug| D32[otclient_d_x86.exe]
    MSBUILD -->|x86 Release| R32[otclient_x86.exe]
    MSBUILD -->|x64 Debug| D64[otclient_d_x64.exe]
    MSBUILD -->|x64 Release| R64[otclient_x64.exe]
    
    ANGLE[vc16/angle/lib/]
    ANGLE --> LIBGL[libEGL.dll<br/>libGLESv2.dll]
    
    LIBGL --> DIST[Distribution folder]
    R64 --> DIST
    
    DIST --> ZIP[otclient-win64.zip]
```

### Diagram dependency graph

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph TD
    EXE[otclient.exe]
    
    EXE --> LIBEGL[libEGL.dll]
    EXE --> LIBGLES[libGLESv2.dll]
    EXE --> VCRUNTIME[vcruntime140.dll<br/>msvcp140.dll]
    EXE --> UCRT[ucrtbase.dll<br/>api-ms-win-*.dll]
    
    LIBEGL --> D3D11[d3d11.dll<br/>System32]
    LIBGLES --> D3D11
    LIBGLES --> D3DCOMPILER[d3dcompiler_47.dll]
    
    VCRUNTIME --> SYSTEM[Windows System32]
    UCRT --> SYSTEM
```

### Diagram ANGLE rendering path

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd' } }}%%
sequenceDiagram
    participant APP as OTClient.exe
    participant EGL as libEGL.dll
    participant GLES as libGLESv2.dll
    participant DX as Direct3D 11
    participant GPU as GPU Driver
    
    APP->>EGL: eglInitialize()
    EGL->>DX: CreateDevice()
    DX->>GPU: Init D3D11 context
    GPU-->>EGL: Ready
    EGL-->>APP: Context created
    
    APP->>GLES: glClear(), glDrawArrays()
    GLES->>DX: Translate to D3D11 commands
    DX->>GPU: Execute
    GPU->>DX: Render frame
    DX->>GLES: Present
    GLES->>APP: Frame complete
```

## Datasets

### vc16_projects.csv — Projekty w solucji

*Facet:* [`15_vc16.vc16_projects`](#facet-15_vc16.vc16_projects)

| solution | project | config | platform | toolset | runtime_lib | output_type | output_name | note |
|---|---|---|---|---|---|---|---|---|
| otclient.sln | otclient | Debug | Win32 | v142 | MDd | Application | otclient_d_x86.exe | debug x86 |
| otclient.sln | otclient | Debug | x64 | v142 | MDd | Application | otclient_d_x64.exe | debug x64 |
| otclient.sln | otclient | Release | Win32 | v142 | MD | Application | otclient_x86.exe | release x86 |
| otclient.sln | otclient | Release | x64 | v142 | MD | Application | otclient_x64.exe | release x64 |

```{csv-table} vc16_projects
:header-rows: 1
:file: ./datasets/vc16_projects.csv
:widths: auto
```

**Toolset explained:**
- `v142` - Visual Studio 2019 compiler
- `v141` - Visual Studio 2017 (backward compat)
- `v140` - Visual Studio 2015 (legacy)

**Runtime library:**
- `MD` - Multi-threaded DLL (Release)
- `MDd` - Multi-threaded Debug DLL (Debug)
- `MT` - Multi-threaded static (not used)

### vc16_includes.csv — Include directories

*Facet:* [`15_vc16.vc16_includes`](#facet-15_vc16.vc16_includes)

| project | config | platform | include_path | purpose | note |
|---|---|---|---|---|---|
| otclient | all | all | vc16/angle/include | ANGLE headers (EGL, GLES) | OpenGL ES |
| otclient | all | all | src/ | OTClient source tree | code base |
| otclient | all | all | $(WindowsSdkDir)Include\$(WindowsSDKVersion)ucrt | Universal C Runtime | Windows SDK |
| otclient | all | all | $(WindowsSdkDir)Include\$(WindowsSDKVersion)um | Windows API headers | Win32 API |

```{csv-table} vc16_includes
:header-rows: 1
:file: ./datasets/vc16_includes.csv
:widths: auto
```

### vc16_libs.csv — Biblioteki linkowane

*Facet:* [`15_vc16.vc16_libs`](#facet-15_vc16.vc16_libs)

| project | config | platform | lib_name | lib_path | link_type | purpose | note |
|---|---|---|---|---|---|---|---|
| otclient | all | all | libEGL.dll.lib | vc16/angle/lib/ | import | ANGLE EGL | OpenGL ES context |
| otclient | all | all | libGLESv2.dll.lib | vc16/angle/lib/ | import | ANGLE GLES2 | OpenGL ES rendering |
| otclient | all | all | kernel32.lib | Windows SDK | import | Windows kernel | system calls |
| otclient | all | all | user32.lib | Windows SDK | import | Windows user | GUI, input |
| otclient | all | all | gdi32.lib | Windows SDK | import | Windows GDI | graphics device |

```{csv-table} vc16_libs
:header-rows: 1
:file: ./datasets/vc16_libs.csv
:widths: auto
```

**Link types:**
- `import` - import library (.lib) for DLL
- `static` - static library (.lib) embedded in EXE
- `system` - provided by OS

### angle_headers.csv — ANGLE header files

*Facet:* [`15_vc16.angle_headers`](#facet-15_vc16.angle_headers)

| header_path | group | purpose | api_version | note |
|---|---|---|---|---|
| EGL/egl.h | EGL | EGL core API | 1.5 | context creation, surfaces |
| EGL/eglext.h | EGL | EGL extensions | - | platform-specific extensions |
| EGL/eglplatform.h | EGL | Platform types | - | Windows-specific types |
| GLES2/gl2.h | GLES2 | OpenGL ES 2.0 API | 2.0 | core rendering functions |
| GLES2/gl2ext.h | GLES2 | GLES2 extensions | 2.0 | additional features |
| GLES3/gl3.h | GLES3 | OpenGL ES 3.0 API | 3.0 | advanced features |
| GLES3/gl31.h | GLES3 | OpenGL ES 3.1 API | 3.1 | compute shaders |
| KHR/khrplatform.h | KHR | Khronos platform types | - | shared types |

```{csv-table} angle_headers
:header-rows: 1
:file: ./datasets/angle_headers.csv
:widths: auto
```

### angle_libs.csv — ANGLE DLL files

*Facet:* [`15_vc16.angle_libs`](#facet-15_vc16.angle_libs)

| dll_name | lib_name | version | size_kb | ship_required | purpose | note |
|---|---|---|---|---|---|---|
| libEGL.dll | libEGL.dll.lib | 1.5 | 110 | yes | EGL implementation | context management |
| libGLESv2.dll | libGLESv2.dll.lib | 3.1 | 6140 | yes | GLES2/3 implementation | rendering engine |
| d3dcompiler_47.dll | - | 47 | 3610 | optional | Shader compiler | may be in System32 |

```{csv-table} angle_libs
:header-rows: 1
:file: ./datasets/angle_libs.csv
:widths: auto
```

**Ship requirements:**
- `yes` - must be distributed with EXE
- `optional` - usually in System32, but ship for safety
- `no` - provided by Windows

## Blueprints — Wzorce VC16

### Blueprint 1: Property sheet (settings.props)

**Plik:** `vc16/settings.props`

```xml
<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ImportGroup Label="PropertySheets" />
  
  <PropertyGroup Label="UserMacros">
    <ProjectRoot>$(MSBuildThisFileDirectory)..</ProjectRoot>
    <AnglePath>$(MSBuildThisFileDirectory)angle</AnglePath>
  </PropertyGroup>
  
  <PropertyGroup>
    <!-- Output directories -->
    <OutDir>$(ProjectRoot)\bin\$(Platform)\$(Configuration)\</OutDir>
    <IntDir>$(ProjectRoot)\obj\$(Platform)\$(Configuration)\</IntDir>
  </PropertyGroup>
  
  <ItemDefinitionGroup>
    <ClCompile>
      <!-- Include paths -->
      <AdditionalIncludeDirectories>
        $(AnglePath)\include;
        $(ProjectRoot)\src;
        %(AdditionalIncludeDirectories)
      </AdditionalIncludeDirectories>
      
      <!-- Preprocessor defines -->
      <PreprocessorDefinitions>
        WIN32;
        _WINDOWS;
        _CRT_SECURE_NO_WARNINGS;
        UNICODE;
        _UNICODE;
        %(PreprocessorDefinitions)
      </PreprocessorDefinitions>
      
      <!-- C++ standard -->
      <LanguageStandard>stdcpp17</LanguageStandard>
      
      <!-- Warnings -->
      <WarningLevel>Level3</WarningLevel>
    </ClCompile>
    
    <Link>
      <!-- Library paths -->
      <AdditionalLibraryDirectories>
        $(AnglePath)\lib;
        %(AdditionalLibraryDirectories)
      </AdditionalLibraryDirectories>
      
      <!-- Libraries -->
      <AdditionalDependencies>
        libEGL.dll.lib;
        libGLESv2.dll.lib;
        kernel32.lib;
        user32.lib;
        gdi32.lib;
        %(AdditionalDependencies)
      </AdditionalDependencies>
    </Link>
  </ItemDefinitionGroup>
</Project>
```

### Blueprint 2: Post-build event (copy ANGLE DLLs)

**W otclient.vcxproj:**

```xml
<ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
  <PostBuildEvent>
    <Command>
      echo Copying ANGLE DLLs...
      copy /Y "$(SolutionDir)vc16\angle\lib\libEGL.dll" "$(OutDir)"
      copy /Y "$(SolutionDir)vc16\angle\lib\libGLESv2.dll" "$(OutDir)"
      copy /Y "$(SolutionDir)d3dcompiler_47.dll" "$(OutDir)"
      echo Copying assets...
      xcopy /E /I /Y "$(SolutionDir)data" "$(OutDir)data\"
      xcopy /E /I /Y "$(SolutionDir)modules" "$(OutDir)modules\"
    </Command>
  </PostBuildEvent>
</ItemDefinitionGroup>
```

### Blueprint 3: CMakeLists.txt for VC16 (alternative build)

**Plik:** `CMakeLists.txt`

```cmake
cmake_minimum_required(VERSION 3.15)
project(otclient)

# Require C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Windows-specific flags
if(WIN32)
    add_definitions(-DWIN32 -D_WINDOWS -DUNICODE -D_UNICODE)
endif()

# Find ANGLE
set(ANGLE_DIR "${CMAKE_SOURCE_DIR}/vc16/angle")
include_directories(${ANGLE_DIR}/include)
link_directories(${ANGLE_DIR}/lib)

# Collect source files
file(GLOB_RECURSE SOURCES src/*.cpp src/*.h)

# Create executable
add_executable(otclient WIN32 ${SOURCES})

# Link ANGLE and Windows libraries
target_link_libraries(otclient
    libEGL.dll.lib
    libGLESv2.dll.lib
    kernel32
    user32
    gdi32
)

# Copy DLLs to output directory
add_custom_command(TARGET otclient POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${ANGLE_DIR}/lib/libEGL.dll"
        $<TARGET_FILE_DIR:otclient>
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${ANGLE_DIR}/lib/libGLESv2.dll"
        $<TARGET_FILE_DIR:otclient>
)
```

### Blueprint 4: Installer script (NSIS)

**Plik:** `installer/otclient.nsi`

```nsis
; OTClient Windows Installer Script (NSIS)

!define PRODUCT_NAME "OTClient V8"
!define PRODUCT_VERSION "1.0.0"
!define PRODUCT_PUBLISHER "OTClient Team"

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "otclient-setup-${PRODUCT_VERSION}.exe"
InstallDir "$PROGRAMFILES64\OTClient"

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  
  ; Executable and DLLs
  File "..\bin\x64\Release\otclient.exe"
  File "..\vc16\angle\lib\libEGL.dll"
  File "..\vc16\angle\lib\libGLESv2.dll"
  File "..\d3dcompiler_47.dll"
  
  ; Assets
  File /r "..\data"
  File /r "..\modules"
  File "..\init.lua"
  
  ; VC++ Redistributable (if needed)
  File "vc_redist.x64.exe"
  ExecWait '"$INSTDIR\vc_redist.x64.exe" /quiet /norestart'
  Delete "$INSTDIR\vc_redist.x64.exe"
  
  ; Shortcuts
  CreateDirectory "$SMPROGRAMS\${PRODUCT_NAME}"
  CreateShortCut "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\otclient.exe"
  CreateShortCut "$DESKTOP\${PRODUCT_NAME}.lnk" "$INSTDIR\otclient.exe"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\otclient.exe"
  Delete "$INSTDIR\*.dll"
  RMDir /r "$INSTDIR\data"
  RMDir /r "$INSTDIR\modules"
  RMDir "$INSTDIR"
  
  Delete "$SMPROGRAMS\${PRODUCT_NAME}\*.*"
  RMDir "$SMPROGRAMS\${PRODUCT_NAME}"
  Delete "$DESKTOP\${PRODUCT_NAME}.lnk"
SectionEnd
```

### Blueprint 5: C++ code using ANGLE

**Plik:** `src/framework/graphics/graphics.cpp`

```cpp
#include <EGL/egl.h>
#include <GLES2/gl2.h>

class Graphics {
private:
    EGLDisplay display;
    EGLContext context;
    EGLSurface surface;
    
public:
    bool initialize(HWND hwnd) {
        // Get EGL display
        display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
        if (display == EGL_NO_DISPLAY) {
            return false;
        }
        
        // Initialize EGL
        if (!eglInitialize(display, nullptr, nullptr)) {
            return false;
        }
        
        // Choose config
        EGLint attribs[] = {
            EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
            EGL_BLUE_SIZE, 8,
            EGL_GREEN_SIZE, 8,
            EGL_RED_SIZE, 8,
            EGL_ALPHA_SIZE, 8,
            EGL_DEPTH_SIZE, 24,
            EGL_STENCIL_SIZE, 8,
            EGL_NONE
        };
        
        EGLConfig config;
        EGLint numConfigs;
        eglChooseConfig(display, attribs, &config, 1, &numConfigs);
        
        // Create window surface
        surface = eglCreateWindowSurface(display, config, hwnd, nullptr);
        
        // Create context
        EGLint contextAttribs[] = {
            EGL_CONTEXT_CLIENT_VERSION, 2,
            EGL_NONE
        };
        context = eglCreateContext(display, config, EGL_NO_CONTEXT, contextAttribs);
        
        // Make current
        eglMakeCurrent(display, surface, surface, context);
        
        // Initialize OpenGL ES
        glViewport(0, 0, width, height);
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        
        return true;
    }
    
    void swapBuffers() {
        eglSwapBuffers(display, surface);
    }
    
    void terminate() {
        eglMakeCurrent(display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
        eglDestroyContext(display, context);
        eglDestroySurface(display, surface);
        eglTerminate(display);
    }
};
```

## How-to / Playbook

### Procedura 1: Build z Visual Studio IDE

**Krok 1:** Otwórz solution
```
Visual Studio 2019 → File → Open → Project/Solution
Select: vc16/otclient.sln
```

**Krok 2:** Wybierz konfigurację
```
Configuration: Release
Platform: x64
```

**Krok 3:** Build
```
Build → Build Solution (Ctrl+Shift+B)
# Output: bin/x64/Release/otclient.exe
```

**Krok 4:** Weryfikuj DLLs
```
# Sprawdź czy ANGLE DLLs zostały skopiowane
dir bin\x64\Release\
# Powinny być: otclient.exe, libEGL.dll, libGLESv2.dll
```

**Krok 5:** Uruchom
```
Debug → Start Without Debugging (Ctrl+F5)
# Lub: bin\x64\Release\otclient.exe
```

### Procedura 2: Build z wiersza poleceń (MSBuild)

**Krok 1:** Otwórz Developer Command Prompt for VS 2019
```cmd
Start Menu → Visual Studio 2019 → Developer Command Prompt
```

**Krok 2:** Navigate to project
```cmd
cd C:\path\to\otcv8-dev
```

**Krok 3:** Build
```cmd
msbuild vc16\otclient.sln /p:Configuration=Release /p:Platform=x64 /m
# /m = parallel build (faster)
```

**Krok 4:** Alternatywnie z CMake
```cmd
mkdir build && cd build
cmake .. -G "Visual Studio 16 2019" -A x64
cmake --build . --config Release
```

### Procedura 3: Deploy / Packaging

**Krok 1:** Collect runtime files
```cmd
mkdir dist
copy bin\x64\Release\otclient.exe dist\
copy vc16\angle\lib\libEGL.dll dist\
copy vc16\angle\lib\libGLESv2.dll dist\
copy d3dcompiler_47.dll dist\
```

**Krok 2:** Copy assets
```cmd
xcopy /E /I data dist\data
xcopy /E /I modules dist\modules
copy init.lua dist\
```

**Krok 3:** Collect VC++ redistributables (optional)
```cmd
# Jeśli używasz runtime MD (dynamic), ship redistributable
# Pobierz: https://aka.ms/vs/16/release/vc_redist.x64.exe
copy vc_redist.x64.exe dist\
```

**Krok 4:** Create ZIP
```cmd
powershell Compress-Archive -Path dist\* -DestinationPath otclient-win64.zip
```

**Krok 5:** Alternatywnie, stwórz installer
```cmd
# Użyj NSIS (Nullsoft Scriptable Install System)
makensis installer\otclient.nsi
# Output: installer\otclient-setup-1.0.0.exe
```

### Procedura 4: Debug z Visual Studio

**Krok 1:** Ustaw breakpoint
```
Otwórz plik src/main.cpp
Kliknij na marginesie przy linii (lub F9)
```

**Krok 2:** Start debugging
```
Debug → Start Debugging (F5)
```

**Krok 3:** Inspect variables
```
Debug → Windows → Locals (pokazuje zmienne lokalne)
Debug → Windows → Call Stack (pokazuje stos wywołań)
```

**Krok 4:** Step through code
```
F10 - Step Over (execute line, don't enter functions)
F11 - Step Into (enter function)
Shift+F11 - Step Out (exit function)
```

**Krok 5:** Memory/Performance profiling
```
Debug → Performance Profiler
Select: CPU Usage, Memory Usage, GPU Usage
Click: Start
# Run application, then stop profiling to see results
```

### Procedura 5: Troubleshooting missing DLLs

**Krok 1:** Check dependencies with Dependency Walker
```
# Download: https://www.dependencywalker.com/
depends.exe bin\x64\Release\otclient.exe
# Shows missing DLLs highlighted in red
```

**Krok 2:** Use dumpbin (MSVC tool)
```cmd
dumpbin /dependents bin\x64\Release\otclient.exe
# Lists all DLL dependencies
```

**Krok 3:** Ship missing DLLs
```cmd
# If missing vcruntime140.dll, msvcp140.dll:
# Ship VC++ redistributable installer
# Or copy DLLs from:
# C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Redist\MSVC\<version>\x64\Microsoft.VC142.CRT\
```

**Krok 4:** Verify ANGLE DLLs version
```cmd
# Check if ANGLE DLLs are 32-bit or 64-bit
dumpbin /headers vc16\angle\lib\libEGL.dll | findstr machine
# Should output: 8664 machine (x64)
```

## Integracje / Pułapki

### Pułapka 1: Architecture mismatch

**Problem:**
```
# EXE compiled for x64, but ANGLE DLLs are x86 (32-bit)
# Error: The application was unable to start correctly (0xc000007b)
```

**Remedium:**
```cmd
# Verify architecture of all files
dumpbin /headers otclient.exe | findstr machine
# Output: 8664 machine (x64)

dumpbin /headers libEGL.dll | findstr machine
# Output: 8664 machine (x64) - OK!
# Output: 14C machine (x86) - BŁĄD! Use 64-bit DLLs
```

### Pułapka 2: Missing Visual C++ Redistributable

**Problem:**
```
# System error: VCRUNTIME140.dll was not found
# User doesn't have VC++ 2019 redistributable installed
```

**Remedium:**
```
# Option 1: Ship redistributable installer
- Include vc_redist.x64.exe in your package
- Prompt user to install it

# Option 2: Static linking
# In Project Properties → C/C++ → Code Generation
# Runtime Library: Multi-threaded (/MT) instead of Multi-threaded DLL (/MD)
# Warning: Increases EXE size significantly
```

### Pułapka 3: d3dcompiler_47.dll not found

**Problem:**
```
# ANGLE requires d3dcompiler_47.dll for shader compilation
# Missing on some Windows 7/8 systems
```

**Remedium:**
```cmd
# Ship d3dcompiler_47.dll with your application
copy "C:\Windows\System32\d3dcompiler_47.dll" dist\

# Or download from:
# https://www.microsoft.com/en-us/download/details.aspx?id=35
```

### Pułapka 4: Unicode vs ANSI build

**Problem:**
```cpp
// Project configured for UNICODE, but some APIs use ANSI
CreateWindowA("MyClass", "Title", ...);  // BŁĄD: incompatible
```

**Remedium:**
```cpp
// Use generic macros (automatically ANSI or Unicode)
CreateWindow(TEXT("MyClass"), TEXT("Title"), ...);

// Or explicit Unicode
CreateWindowW(L"MyClass", L"Title", ...);

// Verify project settings
// Properties → General → Character Set → Use Unicode Character Set
```

### Pułapka 5: Debug/Release mismatch

**Problem:**
```
# Linking Release EXE with Debug libraries (or vice versa)
# Causes crashes or heap corruption
```

**Remedium:**
```
# Always match configuration:
# Debug EXE → link with Debug libs (*_d.lib)
# Release EXE → link with Release libs (*.lib)

# In vcxproj, use conditional ItemGroup:
<ItemDefinitionGroup Condition="'$(Configuration)'=='Debug'">
  <Link>
    <AdditionalDependencies>somelib_d.lib;%(AdditionalDependencies)</AdditionalDependencies>
  </Link>
</ItemDefinitionGroup>

<ItemDefinitionGroup Condition="'$(Configuration)'=='Release'">
  <Link>
    <AdditionalDependencies>somelib.lib;%(AdditionalDependencies)</AdditionalDependencies>
  </Link>
</ItemDefinitionGroup>
```

## QA & Checklists

### Checklist: Build successful

- [ ] Solution opens without errors in VS 2019
- [ ] All projects compile without errors
- [ ] No linker errors
- [ ] Output EXE created in bin/<platform>/<config>/
- [ ] ANGLE DLLs copied to output directory
- [ ] Assets (data/, modules/) accessible from EXE location

### Checklist: Deployment package

- [ ] otclient.exe (Release build)
- [ ] libEGL.dll (ANGLE)
- [ ] libGLESv2.dll (ANGLE)
- [ ] d3dcompiler_47.dll (shader compiler)
- [ ] VC++ redistributable (or static link)
- [ ] data/ folder (complete assets)
- [ ] modules/ folder (Lua scripts)
- [ ] init.lua (entry point)
- [ ] README.txt (instructions)

### Checklist: Testing

- [ ] Runs on Windows 7 SP1 (x64)
- [ ] Runs on Windows 10 (x64)
- [ ] Runs on Windows 11 (x64)
- [ ] No missing DLL errors
- [ ] Graphics render correctly (ANGLE → D3D11)
- [ ] Audio playback works
- [ ] Input (keyboard/mouse) responsive
- [ ] No crashes during 30min gameplay

### Link-lint OK

```bash
python docs/authoring/_tools/link_lint.py --chapter 15_vc16
# Expected: 0 errors
```

### Diagram-lint OK

```bash
python docs/authoring/_tools/diagram_lint.py --chapter 15_vc16
# Expected: all diagrams have %%{init: ...}%% header
```

### Dataset-sanity OK

```bash
python docs/authoring/_tools/csv_schema_check.py --chapter 15_vc16
# Expected:
# - headers match schema
# - no empty rows
# - no NaN values
```

### Idempotency OK

```bash
python docs/authoring/_tools/vc16_scan.py --output /tmp/run1/
python docs/authoring/_tools/vc16_scan.py --output /tmp/run2/
diff -r /tmp/run1/ /tmp/run2/
# Expected: no differences
```

## See Also

### Crosslinks do innych rozdziałów

- **`01_core`** — C++ engine kompilowany w VC16
- **`11_data`** — Assety dystrybuowane z EXE
- **`14_android`** — Porównanie build pipeline (Android vs Windows)

### Narzędzia

- `docs/authoring/_tools/vc16_scan.py` - skaner projektów VC16
- Visual Studio 2019 - IDE
- MSBuild - command-line build tool
- Dependency Walker - DLL dependency analyzer

## Appendix / Facets

(facet-15_vc16.vc16_projects)=
### Facet: `15_vc16.vc16_projects`
Type: dataset
Schema: `solution, project, config, platform, toolset, runtime_lib, output_type, output_name, note`

(facet-15_vc16.vc16_includes)=
### Facet: `15_vc16.vc16_includes`
Type: dataset
Schema: `project, config, platform, include_path, purpose, note`

(facet-15_vc16.vc16_libs)=
### Facet: `15_vc16.vc16_libs`
Type: dataset
Schema: `project, config, platform, lib_name, lib_path, link_type, purpose, note`

(facet-15_vc16.angle_headers)=
### Facet: `15_vc16.angle_headers`
Type: dataset
Schema: `header_path, group, purpose, api_version, note`

(facet-15_vc16.angle_libs)=
### Facet: `15_vc16.angle_libs`
Type: dataset
Schema: `dll_name, lib_name, version, size_kb, ship_required, purpose, note`

(facet-15_vc16.build_pipeline)=
### Facet: `15_vc16.build_pipeline`
Type: diagram
Format: mermaid (flowchart TD)

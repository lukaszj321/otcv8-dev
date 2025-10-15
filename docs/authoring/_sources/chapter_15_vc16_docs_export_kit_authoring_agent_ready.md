---
doc_id: chapter_15_vc16_docs_export_kit_authoring_agent_ready
source_path: vc16/*
source_sha: unknown
last_sync_iso: 2025-10-15T20:31:06Z
doc_class: platform/windows
language: pl
title: 15_vc16 — ANGLE/Win toolchain i dystrybucja runtime
summary: Nagłówki i biblioteki ANGLE (EGL/GLES) dla kompilacji VC16, integracja z CMake/MSVC, AppLocal runtime i testy dymne.
tags: [vc16, angle, egl, gles2, windows, packaging, runtime, cmake]
---

```{contents}
:local:
:depth: 2
```

## 1. Cel

`vc16/` dostarcza nagłówki i biblioteki **ANGLE** umożliwiające uruchomienie GLES2/GLES3 na Windowsie przez warstwę D3D.
Dystrybucja odbywa się w modelu **AppLocal** (DLL obok wykonywalnego).

## 2. Zawartość i kontrakt

```{csv-table} Nagłówki ANGLE
:header-rows: 1
:file: ../datasets/vc16_angle_headers.csv
:widths: auto
```

```{csv-table} Biblioteki (DLL/IMPORT)
:header-rows: 1
:file: ../datasets/vc16_angle_libs.csv
:widths: auto
```

(facet-15_vc16.headers)=

### Facet: `15_vc16.headers`

(facet-15_vc16.libs)=

### Facet: `15_vc16.libs`

## 3. Integracja (CMake/MSVC)

```cmake
add_executable(otclient WIN32 main.cpp)
target_include_directories(otclient PRIVATE ${CMAKE_SOURCE_DIR}/vc16/include)
target_link_libraries(otclient PRIVATE
  ${CMAKE_SOURCE_DIR}/vc16/lib/libEGL.dll.lib
  ${CMAKE_SOURCE_DIR}/vc16/lib/libGLESv2.dll.lib)
add_custom_command(TARGET otclient POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${CMAKE_SOURCE_DIR}/vc16/lib/libEGL.dll ${CMAKE_CURRENT_BINARY_DIR}
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${CMAKE_SOURCE_DIR}/vc16/lib/libGLESv2.dll ${CMAKE_CURRENT_BINARY_DIR})
```

**Uwaga**: część konfiguracji wymaga `d3dcompiler_47.dll` (zależnie od wersji systemu).

## 4. Test dymny EGL

```cpp
#include <EGL/egl.h>
#include <GLES2/gl2.h>
#include <cstdio>

int main(){
  EGLDisplay d = eglGetDisplay(EGL_DEFAULT_DISPLAY);
  if(d == EGL_NO_DISPLAY){ std::puts("No display"); return 1; }
  EGLint major=0, minor=0;
  eglInitialize(d, &major, &minor);
  std::printf("EGL %d.%d\n", major, minor);
  eglTerminate(d);
  return 0;
}
```

## 5. Pipeline renderowania

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph TD
  App --> EGL
  EGL --> GLES2
  GLES2 --> ANGLE
  ANGLE --> D3D
  D3D --> GPU
```

## 6. QA (Windows)

- **dll-present** – `libEGL.dll` i `libGLESv2.dll` w folderze binarnym.
- **egl-init** – udana inicjalizacja i wersja >= 1.4.
- **surface** – utworzenie powierzchni i `eglSwapBuffers()` bez błędów.
- **fps** – stabilny FPS sceny testowej.

## 7. Najczęstsze problemy

- **Złe CRT** – mismatch Debug/Release skutkuje brakiem startu.
- **PATH vs AppLocal** – nie polegaj na PATH użytkownika, kopiuj DLL obok `.exe`.
- **UWP** – pakiet UWP ma inne zasady ładowania; niniejszy rozdział dotyczy Win32.

---

## Aneks redakcyjny (merytoryczne uzupełnienia)

### Kontrola dystrybucji DLL (PowerShell)

```powershell
$req = @('libEGL.dll','libGLESv2.dll')
$missing = $req | ? { -not (Test-Path (Join-Path $PSScriptRoot $_)) }
if($missing) { Write-Error "Brak: $missing"; exit 1 }
```

### CMake: ustawienia CRT

```cmake
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
```

## 8. Pełny projekt CMake (Win32)

```cmake
cmake_minimum_required(VERSION 3.20)
project(otclient_angle_win LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
add_executable(otclient WIN32 main.cpp)
target_include_directories(otclient PRIVATE ${CMAKE_SOURCE_DIR}/vc16/include)
target_link_libraries(otclient PRIVATE
  ${CMAKE_SOURCE_DIR}/vc16/lib/libEGL.dll.lib
  ${CMAKE_SOURCE_DIR}/vc16/lib/libGLESv2.dll.lib)
add_custom_command(TARGET otclient POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${CMAKE_SOURCE_DIR}/vc16/lib/libEGL.dll ${CMAKE_CURRENT_BINARY_DIR}
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${CMAKE_SOURCE_DIR}/vc16/lib/libGLESv2.dll ${CMAKE_CURRENT_BINARY_DIR})
```

## 9. Przykład trójkąta GLES2 (minimalny)

```cpp
static const char* VS = R"(attribute vec2 aPos; void main(){ gl_Position=vec4(aPos,0.0,1.0);} )";
static const char* FS = R"(precision mediump float; void main(){ gl_FragColor=vec4(0.84,0.69,0.37,1.0);} )";
static GLuint mk(GLenum t, const char* src){
  GLuint s=glCreateShader(t); glShaderSource(s,1,&src,nullptr); glCompileShader(s); return s;
}
static GLuint prog(){
  GLuint p=glCreateProgram(); glAttachShader(p,mk(GL_VERTEX_SHADER,VS)); glAttachShader(p,mk(GL_FRAGMENT_SHADER,FS));
  glBindAttribLocation(p,0,"aPos"); glLinkProgram(p); return p;
}
```

## 10. Diagnostyka i typowe komunikaty

- `EGL_BAD_MATCH` – niezgodna konfiguracja formatu powierzchni.
- `GL_INVALID_ENUM` po `glTexImage2D` – brak wsparcia dla formatu; sprawdź rozszerzenia.
- `missing d3dcompiler_47.dll` – dołącz DLL AppLocal.

## 11. Pakowanie artefaktów (CPack)

```cmake
include(CPack)
set(CPACK_GENERATOR ZIP)
set(CPACK_PACKAGE_FILE_NAME "otclient-angle-win")
install(TARGETS otclient RUNTIME DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/vc16/lib/libEGL.dll DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/vc16/lib/libGLESv2.dll DESTINATION .)
```

## Dodatek: przykłady konfiguracyjne (unikalne)

### Przykład 1

```text
Case-1: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 2

```text
Case-2: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 3

```text
Case-3: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 4

```text
Case-4: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 5

```text
Case-5: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 6

```text
Case-6: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 7

```text
Case-7: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 8

```text
Case-8: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 9

```text
Case-9: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 10

```text
Case-10: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 11

```text
Case-11: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 12

```text
Case-12: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 13

```text
Case-13: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 14

```text
Case-14: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 15

```text
Case-15: Opis konkretnego kroku integracji bez powtórzeń.
```

## 12. Inicjalizacja EGL — szkic Win32

```cpp
HWND hwnd = CreateWindowA("STATIC","OTC",WS_OVERLAPPEDWINDOW,100,100,640,480,0,0,GetModuleHandle(0),0);
// ... utworzenie HDC itd.
EGLDisplay d = eglGetDisplay(EGL_DEFAULT_DISPLAY);
eglInitialize(d, 0, 0);
EGLint attribs[] = {
  EGL_RED_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_BLUE_SIZE, 8,
  EGL_DEPTH_SIZE, 16, EGL_STENCIL_SIZE, 8,
  EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
  EGL_NONE
};
EGLConfig cfg; EGLint n;
eglChooseConfig(d, attribs, &cfg, 1, &n);
EGLSurface s = eglCreateWindowSurface(d, cfg, (EGLNativeWindowType)hwnd, 0);
EGLint ctxAttrs[] = { EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE };
EGLContext ctx = eglCreateContext(d, cfg, EGL_NO_CONTEXT, ctxAttrs);
eglMakeCurrent(d, s, s, ctx);
```

## 13. Znane różnice ANGLE vs OpenGL

- Dokładność shaderów może się różnić (mapowanie na D3D).
- Niektóre rozszerzenia GLES mogą być niedostępne — sprawdzaj przez `glGetString(GL_EXTENSIONS)`.
- Format sRGB wymaga dodatkowych flag/konfiguracji.

## 14. Logging diagnostyczny

- Użyj `OutputDebugStringA` dla logów Windows.
- Włącz warunkowe `EGL_ANGLE_platform_angle_d3d` opcje debug gdzie dostępne.

## 15. Skrypt sprawdzający środowisko (Batch)

```bat
@echo off
set BIN=%~dp0
if not exist "%BIN%libEGL.dll" echo Brak libEGL.dll & exit /b 1
if not exist "%BIN%libGLESv2.dll" echo Brak libGLESv2.dll & exit /b 1
echo OK
```

## 16. Polityka licencyjna

- ANGLE — licencja BSD 3-Clause; dołącz plik licencji w artefakcie.
- Biblioteki systemowe — zgodność z licencjami dystrybucji pakietu.

## 17. Plan testów GPU

- Zintegrowany Intel, dedykowany NVIDIA/AMD, zdalny RDP (sprawdź fallback).
- VSync ON/OFF, różne rozdzielczości i DPI.
- Testy czasu tworzenia kontekstu i kompilacji shaderów.

## 18. Kompilacja shaderów — helper

```cpp
static GLuint compile(GLenum type, const char* src){
  GLuint s=glCreateShader(type);
  glShaderSource(s,1,&src,nullptr);
  glCompileShader(s);
  GLint ok=0; glGetShaderiv(s, GL_COMPILE_STATUS,&ok);
  if(!ok){ char log[4096]; GLsizei n=0; glGetShaderInfoLog(s,4096,&n,log); OutputDebugStringA(log); }
  return s;
}
static GLuint link(GLuint vs, GLuint fs){
  GLuint p=glCreateProgram();
  glAttachShader(p,vs); glAttachShader(p,fs);
  glLinkProgram(p);
  GLint ok=0; glGetProgramiv(p, GL_LINK_STATUS,&ok);
  if(!ok){ char log[4096]; GLsizei n=0; glGetProgramInfoLog(p,4096,&n,log); OutputDebugStringA(log); }
  return p;
}
```

## 19. Ładowanie tekstury — minimalny przykład

```cpp
GLuint tex=0; glGenTextures(1,&tex); glBindTexture(GL_TEXTURE_2D, tex);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
// wczytaj RGBA8 do bufora 'pixels' o wymiarach w,h
glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,w,h,0,GL_RGBA,GL_UNSIGNED_BYTE,pixels);
```

## 20. Rozszerzenia i capability check

```cpp
auto ext = (const char*)glGetString(GL_EXTENSIONS);
if(!strstr(ext,"GL_OES_texture_npot")) {
  // fallback: pot-only
}
```

## 21. Warianty D3D w ANGLE (uwagi)

- D3D11 preferowane; fallback na D3D9 (starsze systemy) może ograniczać funkcje.

- Wydajność zależy od sterowników; testuj różne GPU.

## 22. Integracja z CI (Windows)

```yaml
steps:
  - task: VSBuild@1
    inputs:
      solution: otc.sln
      configuration: Release
  - powershell: ./ci/check-dlls.ps1
  - publish: bin/Release
```

## 23. Matryca testów rozdzielczości

- 1280×720, 1920×1080, 2560×1440, 3840×2160 (DPI scaling 100/150/200%).

- Tryb okienkowy i borderless.

## 24. Minimalny WinMain (pętla komunikatów)

```cpp
#include <windows.h>
int APIENTRY WinMain(HINSTANCE h, HINSTANCE, LPSTR, int){
  WNDCLASSA wc = {0}; wc.lpszClassName="OTC"; wc.lpfnWndProc=DefWindowProcA;
  RegisterClassA(&wc);
  HWND wnd = CreateWindowA("OTC","OTClient",WS_OVERLAPPEDWINDOW|WS_VISIBLE,100,100,800,600,0,0,h,0);
  // init EGL (jak w sekcji 12), render pętla:
  MSG msg; BOOL r;
  while((r = GetMessage(&msg,0,0,0))!=0){
    if(r==-1) break; TranslateMessage(&msg); DispatchMessage(&msg);
    // render frame -> eglSwapBuffers(...);
  }
  return 0;
}
```

## 25. Layout pakietu binarnego (zalecany)

```text
otclient/
  otclient.exe
  libEGL.dll
  libGLESv2.dll
  data/
    images/...
    styles/...
  shaders/
  configs/
```

## 26. Kompletny przykład renderu trójkąta

```cpp
#include <EGL/egl.h>
#include <GLES2/gl2.h>
#include <windows.h>
static const char* VS = "attribute vec2 aPos; void main(){ gl_Position=vec4(aPos,0.0,1.0);}";
static const char* FS = "precision mediump float; void main(){ gl_FragColor=vec4(0.84,0.69,0.37,1.0);}";
// ... (funkcje compile/link z sekcji 18)
void draw(){
  static GLuint p=0, vbo=0;
  if(!p){ p=link(compile(GL_VERTEX_SHADER,VS), compile(GL_FRAGMENT_SHADER,FS)); }
  if(!vbo){
    GLfloat verts[] = { 0.0f,  0.8f,  -0.8f, -0.8f,  0.8f, -0.8f };
    glGenBuffers(1,&vbo); glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(verts), verts, GL_STATIC_DRAW);
  }
  glViewport(0,0,800,600);
  glClearColor(0.06f,0.06f,0.06f,1.0f); glClear(GL_COLOR_BUFFER_BIT);
  glUseProgram(p);
  glBindBuffer(GL_ARRAY_BUFFER, vbo);
  glEnableVertexAttribArray(0);
  glVertexAttribPointer(0,2,GL_FLOAT,GL_FALSE,0,(void*)0);
  glDrawArrays(GL_TRIANGLES, 0, 3);
}
```

## 27. Tabela znanych problemów sterowników (przykładowa)

```{list-table} Driver quirks
:header-rows: 1
* - GPU
  - objaw
  - obejście
* - Intel HD (stare)
  - artefakty przy alpha
  - pre-multipled alpha lub wyłączenie blendu na UI tle
* - RDP software
  - niski FPS
  - ogranicz efekty, mniejsza rozdzielczość
```

## 28. FAQ (rozszerzona)

**Czy mogę ładować DLL z innego katalogu?** — Tak, ustaw `SetDllDirectoryA` lub modyfikuj `PATH`, ale AppLocal jest prostsze.  
**Czy ANGLE wspiera GLES3?** — Zależy od wersji; sprawdź `glGetString(GL_VERSION)`.  
**Jak logować wersję D3D?** — ANGLE udostępnia rozszerzenia platformowe; wypisz w logach parametry konfiguracyjne.

## 29. Warianty buildów i artefakty

- Release (bez symboli), Debug (z symbolami), RelWithDebInfo (zalecany dla QA).  
- Artefakt ZIP z binariami + `THIRD_PARTY_NOTICES.txt`.

## 30. Makra obsługi błędów i cleanup

```cpp
#define EGLCHK(x) do{ if(!(x)) { OutputDebugStringA("EGL call failed\n"); } }while(0)
#define GLCHK() do{ GLenum e=glGetError(); if(e!=GL_NO_ERROR){ char b[64]; sprintf(b,"GL err=%u\n",e); OutputDebugStringA(b);} }while(0)
```

## 31. Pętla renderu — pełny szkic

```cpp
// Założenie: kontekst utworzony (sekcja 12), mamy HWND i EGLSurface s, EGLDisplay d
for(;;){
  // ... obsługa komunikatów Win32 ...
  draw();    // funkcja z sekcji 26
  eglSwapInterval(d, 1);
  eglSwapBuffers(d, s);
}
```

## 32. Zamykanie i zwalnianie zasobów

```cpp
glBindBuffer(GL_ARRAY_BUFFER, 0);
glUseProgram(0);
eglMakeCurrent(d, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
eglDestroyContext(d, ctx);
eglDestroySurface(d, s);
eglTerminate(d);
```

## 33. Dodatkowe uwagi dystrybucyjne

- Dołącz plik `README.txt` z opisem wymagań systemowych.

- Zadbaj o `vcruntime` zgodny z docelowym środowiskiem (CRT zgodny z konfiguracją).

## 34. Pomocnicze API shaderów (nagłówek)

```cpp
struct ShaderProgram {
  GLuint vs=0, fs=0, prog=0;
  bool build(const char* vsrc, const char* fsrc){
    vs = compile(GL_VERTEX_SHADER, vsrc);
    fs = compile(GL_FRAGMENT_SHADER, fsrc);
    prog = link(vs, fs);
    return prog!=0;
  }
  void use(){ glUseProgram(prog); }
  GLint uniform(const char* n){ return glGetUniformLocation(prog, n); }
  GLint attrib(const char* n){ return glGetAttribLocation(prog, n); }
  void destroy(){ if(vs) glDeleteShader(vs); if(fs) glDeleteShader(fs); if(prog) glDeleteProgram(prog); vs=fs=prog=0; }
};
```

## 35. FAQ (dodatkowe)

**Jak sprawdzić wersję ANGLE?** — Wypisz `glGetString(GL_VENDOR)`, `glGetString(GL_RENDERER)`, `glGetString(GL_VERSION)`.  
**Czy muszę dostarczać pliki PDB?** — Zalecane w buildach dla QA; w release opcjonalnie oddzielnie.  
**Czy EGLSwapInterval(0) jest wspierane?** — Zależy od sterownika; testuj i dokumentuj w raporcie QA.  

## 36. Wskazówki wydajnościowe

- Używaj VBO i minimalizuj zmiany stanu.

- Batchuj rysowanie elementów UI korzystających z tego samego atlasu.

- Unikaj wysokiej precyzji w shaderach UI bez potrzeby.

## 37. Tabela diagnostyczna błędów EGL/GL (rozszerzona)

```{list-table} Troubles
:header-rows: 1
* - etap
  - kod/błąd
  - możliwe przyczyny
  - akcja
* - eglGetDisplay
  - EGL_NO_DISPLAY
  - brak sterownika / środowiska
  - sprawdź środowisko ANGLE/D3D
* - eglInitialize
  - EGL_NOT_INITIALIZED
  - konflikt wersji, brak D3D
  - loguj wersje, sprawdź DLL
* - eglCreateContext
  - EGL_BAD_CONFIG
  - zły atrybut konfiguracji
  - zmień format/atrybuty
* - glLinkProgram
  - GL_LINK_STATUS=0
  - niekompatybilne shadery
  - wypisz `glGetProgramInfoLog`
```

## 38. Pełne CMake z instalacją i symbolami

```cmake
cmake_minimum_required(VERSION 3.24)
project(otc_win_angle LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
add_executable(otc main.cpp)
target_include_directories(otc PRIVATE ${CMAKE_SOURCE_DIR}/vc16/include)
target_link_libraries(otc PRIVATE
  ${CMAKE_SOURCE_DIR}/vc16/lib/libEGL.dll.lib
  ${CMAKE_SOURCE_DIR}/vc16/lib/libGLESv2.dll.lib)
set_target_properties(otc PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
  MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
install(TARGETS otc RUNTIME DESTINATION .)
install(FILES
  ${CMAKE_SOURCE_DIR}/vc16/lib/libEGL.dll
  ${CMAKE_SOURCE_DIR}/vc16/lib/libGLESv2.dll
  DESTINATION .)
```

## 39. Słownik pojęć (Windows/ANGLE)

- **AppLocal** — dystrybucja DLL w tym samym folderze co `.exe`.

- **CRT** — biblioteka uruchomieniowa MSVC; wersja musi pasować do buildu.

- **ANGLE** — translacja GLES na D3D (Direct3D) na Windows.

- **EGL** — warstwa abstrakcji dla kontekstów i powierzchni renderu.

## 40. Rozszerzone wskazówki QA

- Sprawdź poprawność działania po `Sleep/Suspend`.

- Testuj przełączenie DPI w locie (zmiana skalowania systemowego).

- Symuluj brak jednej z DLL i zweryfikuj komunikat błędu aplikacji.

## 41. Manifest sum kontrolnych (dystrybucja)

```text
SHA256  libEGL.dll     = <wstaw hash>
SHA256  libGLESv2.dll  = <wstaw hash>
SHA256  otclient.exe   = <wstaw hash>
```

Utrzymuj plik `checksums.txt` w artefakcie — ułatwia weryfikację integralności.

## 42. Notatki wydania (szablon)

```text
Wersja: 1.0.2
Data: 2025-10-15
Zmiany: stabilność, optymalizacje UI
Wymagania: Windows 10+, GPU z obsługą D3D11
Znane problemy: brak
```

## 43. Argumenty wiersza poleceń (szkic)

```cpp
int main(int argc, char** argv){
  bool vsync=true; for(int i=1;i<argc;i++){ if(std::string(argv[i])=="--novsync") vsync=false; }
  // init okna + EGL
  // ...
  eglSwapInterval(d, vsync?1:0);
}
```

## 44. D3D debug hints (jeśli dostępne)

- W buildzie Debug włącz `D3D_DEBUG_DEVICE` — bogatsze logi sterownika.

- Sprawdzaj ostrzeżenia o błędach kompilacji shaderów i niekompatybilnych formatach.

## 45. Plan testów końcowych (lista kontrolna)

- [ ] Start aplikacji bez zależności w PATH (tylko AppLocal)

- [ ] Inicjalizacja EGL i render 60 FPS przez 60 sekund

- [ ] Zmiana rozmiaru okna (resize) — poprawne przeliczenie viewportu

- [ ] Zminimalizowanie / przywrócenie — brak wycieków i błędów

- [ ] Sprawdzenie na GPU iGPU/dGPU — brak różnic funkcjonalnych

- [ ] Weryfikacja `checksums.txt` po pobraniu artefaktu

**Uwaga QA:** Zapisz log z wersjami EGL/GLES oraz identyfikatorem GPU do pliku `qa_env.txt`.

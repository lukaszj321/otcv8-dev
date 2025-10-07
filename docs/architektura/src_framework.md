# src framework
## PoniÄąÄ˝ej znajduje siÄ™ kompletna dokumentacja techniczna dla repozytorium, src/framework
## Opis ogĂłlny

Plik `const.h` peÄąâ€šni rolÄ™ centralnego repozytorium dla staÄąâ€šych, makr i typĂłw wyliczeniowych (enum) uÄąÄ˝ywanych w caÄąâ€šym frameworku. Definiuje on kluczowe wartoÄąâ€şci, takie jak kody klawiszy, poziomy logowania, flagi wyrĂłwnania, przyciski myszy, a takÄąÄ˝e staÄąâ€še matematyczne i makra kompilacji. Jest to fundamentalny plik nagÄąâ€šĂłwkowy, ktĂłry zapewnia spĂłjnoÄąâ€şÄ‡ i czytelnoÄąâ€şÄ‡ kodu poprzez zdefiniowanie nazwanych staÄąâ€šych zamiast "magicznych liczb".
## Definicje i Makra
## Makra matematyczne

-   `DEG_TO_RAD`: SÄąâ€šuÄąÄ˝y do konwersji stopni na radiany.
`$fenceInfo
# define DEG_TO_RAD (acos(-1)/180.0)
```
-   `RAD_TO_DEC`: SÄąâ€šuÄąÄ˝y do konwersji radianĂłw na stopnie.
`$fenceInfo
# define RAD_TO_DEC (180.0/acos(-1))
```
## Makra budowania (Build Macros)

Makra te sÄ… definiowane podczas kompilacji i dostarczajÄ… informacji o wersji i Äąâ€şrodowisku budowania.

-   `BUILD_COMMIT`: Przechowuje hash commita Git. DomyÄąâ€şlnie "dev".
`$fenceInfo
# ifndef BUILD_COMMIT
# define BUILD_COMMIT "dev"
# endif
```
-   `BUILD_REVISION`: Przechowuje numer rewizji. DomyÄąâ€şlnie 0.
`$fenceInfo
# ifndef BUILD_REVISION
# define BUILD_REVISION 0
# endif
```
-   `BUILD_TYPE`: OkreÄąâ€şla typ budowania (np. "release", "debug"). DomyÄąâ€şlnie "unknown".
`$fenceInfo
# ifndef BUILD_TYPE
# define BUILD_TYPE "unknown"
# endif
```
-   `BUILD_ARCH`: OkreÄąâ€şla architekturÄ™ procesora (x64, x86). Wykrywane automatycznie, jeÄąâ€şli nie jest zdefiniowane.
`$fenceInfo
# ifndef BUILD_ARCH
# if defined(__amd64) || defined(_M_X64)
# define BUILD_ARCH "x64"
# elif defined(__i386) || defined(_M_IX86) || defined(_X86_)
# define BUILD_ARCH "x86"
# else
# define BUILD_ARCH "unknown"
# endif
# endif
```
## Namespace `Fw`

PrzestrzeÄąâ€ž nazw `Fw` (skrĂłt od Framework) grupuje wszystkie staÄąâ€še i typy wyliczeniowe, aby uniknÄ…Ä‡ konfliktĂłw nazw w globalnej przestrzeni nazw.
## Zmienne globalne

-   `pi`: StaÄąâ€ša matematyczna przechowujÄ…ca przybliÄąÄ˝onÄ… wartoÄąâ€şÄ‡ liczby Pi.
`$fenceInfo
    static const float pi = 3.14159265;
```
-   `MIN_ALPHA`: Minimalna wartoÄąâ€şÄ‡ alfa (przezroczystoÄąâ€şci), poniÄąÄ˝ej ktĂłrej obiekty mogÄ… byÄ‡ uznawane za w peÄąâ€šni przezroczyste.
`$fenceInfo
    static const float MIN_ALPHA = 0.003f;
```
## Typy wyliczeniowe (Enums)
## `enum Key`

Definiuje kody klawiszy klawiatury. WartoÄąâ€şci liczbowe dla klawiszy drukowalnych odpowiadajÄ… ich kodom ASCII.

| Nazwa | WartoÄąâ€şÄ‡ | Opis |
| :--- | :--- | :--- |
| `KeyUnknown` | 0 | Nieznany klawisz |
| `KeyEscape` | 1 | Klawisz Escape |
| `KeyTab` | 2 | Klawisz Tab |
| `KeyBackspace` | 3 | Klawisz Backspace |
| `KeyEnter` | 5 | Klawisz Enter/Return |
| ... | ... | ... |
| `KeyNumpad9` | 150 | Klawisz 9 na klawiaturze numerycznej |
## `enum LogLevel`

Definiuje poziomy waÄąÄ˝noÄąâ€şci dla komunikatĂłw w systemie logowania.

| Nazwa | WartoÄąâ€şÄ‡ | Opis |
| :--- | :--- | :--- |
| `LogDebug` | 0 | WiadomoÄąâ€şci debugowania |
| `LogInfo` | 1 | Informacje ogĂłlne |
| `LogWarning` | 2 | OstrzeÄąÄ˝enia |
| `LogError` | 3 | BÄąâ€šÄ™dy |
| `LogFatal` | 4 | BÄąâ€šÄ™dy krytyczne, powodujÄ…ce zamkniÄ™cie aplikacji |
## `enum AspectRatioMode`

OkreÄąâ€şla, w jaki sposĂłb zachowaÄ‡ proporcje obrazu podczas skalowania.

| Nazwa | Opis |
| :--- | :--- |
| `IgnoreAspectRatio` | Ignoruje proporcje, rozciÄ…gajÄ…c obraz do peÄąâ€šnego rozmiaru. |
| `KeepAspectRatio` | Zachowuje proporcje, dopasowujÄ…c obraz do mniejszego wymiaru. |
| `KeepAspectRatioByExpanding` | Zachowuje proporcje, wypeÄąâ€šniajÄ…c caÄąâ€šy obszar (moÄąÄ˝e przyciÄ…Ä‡ obraz). |
## `enum AlignmentFlag`

Flagi bitowe uÄąÄ˝ywane do okreÄąâ€şlania wyrĂłwnania tekstu lub widgetĂłw w kontenerze. MoÄąÄ˝na je Äąâ€šÄ…czyÄ‡ za pomocÄ… operatora `|`.

| Nazwa | WartoÄąâ€şÄ‡ | Opis |
| :--- | :--- | :--- |
| `AlignNone` | 0 | Brak wyrĂłwnania |
| `AlignLeft` | 1 | WyrĂłwnanie do lewej |
| `AlignRight` | 2 | WyrĂłwnanie do prawej |
| `AlignTop` | 4 | WyrĂłwnanie do gĂłry |
| `AlignBottom` | 8 | WyrĂłwnanie do doÄąâ€šu |
| `AlignHorizontalCenter` | 16 | WyÄąâ€şrodkowanie w poziomie |
| `AlignVerticalCenter` | 32 | WyÄąâ€şrodkowanie w pionie |
| `AlignCenter` | 48 | PeÄąâ€šne wyÄąâ€şrodkowanie (kombinacja `HorizontalCenter` i `VerticalCenter`) |
| ... | ... | Inne kombinacje |
## `enum AnchorEdge`

Definiuje krawÄ™dzie, do ktĂłrych moÄąÄ˝na "zakotwiczyÄ‡" widget w layoucie typu `UIAnchorLayout`.

| Nazwa | Opis |
| :--- | :--- |
| `AnchorNone` | Brak zakotwiczenia |
| `AnchorTop` | GĂłrna krawÄ™dÄąĹź |
| `AnchorBottom` | Dolna krawÄ™dÄąĹź |
| ... | ... |
## `enum FocusReason`

OkreÄąâ€şla przyczynÄ™, dla ktĂłrej widget otrzymaÄąâ€š fokus.

| Nazwa | Opis |
| :--- | :--- |
| `MouseFocusReason` | Fokus uzyskany przez klikniÄ™cie myszÄ…. |
| `KeyboardFocusReason` | Fokus uzyskany przez nawigacjÄ™ klawiaturÄ… (np. Tab). |
| `ActiveFocusReason` | Fokus ustawiony programowo. |
| `OtherFocusReason` | Inna przyczyna. |
## `enum AutoFocusPolicy`

Definiuje, jak widget-rodzic powinien automatycznie ustawiaÄ‡ fokus na swoich dzieciach.

| Nazwa | Opis |
| :--- | :--- |
| `AutoFocusNone` | Brak automatycznego fokusa. |
| `AutoFocusFirst` | Ustawia fokus na pierwszym dziecku, ktĂłre moÄąÄ˝e go otrzymaÄ‡. |
| `AutoFocusLast` | Ustawia fokus na ostatnim dziecku, ktĂłre moÄąÄ˝e go otrzymaÄ‡. |
## `enum InputEventType`

Definiuje typy zdarzeÄąâ€ž wejÄąâ€şciowych (klawiatura, mysz).

| Nazwa | Opis |
| :--- | :--- |
| `NoInputEvent` | Brak zdarzenia. |
| `KeyTextInputEvent` | Zdarzenie wprowadzenia tekstu. |
| `KeyDownInputEvent` | Zdarzenie wciÄąâ€şniÄ™cia klawisza. |
| `KeyPressInputEvent` | Zdarzenie przytrzymania klawisza (auto-powtarzanie). |
| ... | ... |
## `enum MouseButton`

Definiuje przyciski myszy oraz dotyk.

| Nazwa | Opis |
| :--- | :--- |
| `MouseNoButton` | Brak przycisku. |
| `MouseLeftButton` | Lewy przycisk myszy. |
| ... | ... |
## `enum MouseWheelDirection`

Definiuje kierunek przewijania kĂłÄąâ€škiem myszy.

| Nazwa | Opis |
| :--- | :--- |
| `MouseNoWheel` | Brak przewijania. |
| `MouseWheelUp` | Przewijanie w gĂłrÄ™. |
| `MouseWheelDown` | Przewijanie w dĂłÄąâ€š. |
## `enum KeyboardModifier`

Flagi bitowe dla klawiszy modyfikujÄ…cych (Ctrl, Alt, Shift).

| Nazwa | WartoÄąâ€şÄ‡ | Opis |
| :--- | :--- | :--- |
| `KeyboardNoModifier` | 0 | Brak modyfikatora. |
| `KeyboardCtrlModifier` | 1 | WciÄąâ€şniÄ™ty Ctrl. |
| `KeyboardAltModifier` | 2 | WciÄąâ€şniÄ™ty Alt. |
| `KeyboardShiftModifier` | 4 | WciÄąâ€şniÄ™ty Shift. |
## `enum WidgetState`

Flagi bitowe definiujÄ…ce stan widgetu (np. aktywny, najechany, wciÄąâ€şniÄ™ty). UÄąÄ˝ywane do dynamicznego stylowania widgetĂłw.

| Nazwa | WartoÄąâ€şÄ‡ | Opis |
| :--- | :--- | :--- |
| `InvalidState` | -1 | NieprawidÄąâ€šowy stan. |
| `DefaultState` | 0 | Stan domyÄąâ€şlny. |
| `ActiveState` | 1 | Widget jest aktywny. |
| `FocusState` | 2 | Widget ma fokus. |
| `HoverState` | 4 | Kursor myszy jest nad widgetem. |
| ... | ... | ... |
## `enum DrawPane`

OkreÄąâ€şla warstwÄ™ rysowania dla widgetĂłw, co pozwala na kontrolowanie kolejnoÄąâ€şci renderowania.

| Nazwa | WartoÄąâ€şÄ‡ | Opis |
| :--- | :--- | :--- |
| `ForegroundPane` | 1 | Warstwa pierwszoplanowa (interfejs uÄąÄ˝ytkownika). |
| `MapBackgroundPane` | 2 | TÄąâ€šo mapy gry. |
| `MapForegroundPane` | 3 | Pierwszy plan mapy gry (np. efekty nad postaciami). |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/stdext/compiler.h`: Plik ten dostarcza makr i definicji specyficznych dla kompilatora (np. `BUILD_COMPILER`).

---
# Ä‘Ĺşâ€śâ€ž CMakeLists.txt
## Opis ogĂłlny

Plik `CMakeLists.txt` jest gÄąâ€šĂłwnym skryptem konfiguracyjnym dla systemu budowania CMake. Jego rolÄ… jest zdefiniowanie, jak projekt `otclient` ma byÄ‡ kompilowany. OkreÄąâ€şla on flagi kompilatora, zaleÄąÄ˝noÄąâ€şci od bibliotek zewnÄ™trznych, listÄ™ plikĂłw ÄąĹźrĂłdÄąâ€šowych oraz opcje konfiguracyjne, ktĂłre pozwalajÄ… dostosowaÄ‡ proces budowania do rĂłÄąÄ˝nych platform (Windows, Linux, Apple, WebAssembly) i potrzeb (np. wÄąâ€šÄ…czenie/wyÄąâ€šÄ…czenie obsÄąâ€šugi dÄąĹźwiÄ™ku, grafiki, sieci).
## Opcje budowania

Skrypt definiuje kilka opcji, ktĂłre moÄąÄ˝na kontrolowaÄ‡ podczas generowania projektu.

| Opcja | DomyÄąâ€şlnie | Opis |
| :--- | :--- | :--- |
| `LUAJIT` | `ON` | UÄąÄ˝ywa LuaJIT zamiast standardowej biblioteki Lua. |
| `CRASH_HANDLER` | `ON` (poza Apple) | WÄąâ€šÄ…cza generowanie raportĂłw po awarii aplikacji. |
| `USE_STATIC_LIBS`| `ON` (poza Apple) | Linkuje biblioteki statycznie zamiast dynamicznie (DLL). |
| `USE_LIBCPP` | `OFF` (dla Apple `ON`)| UÄąÄ˝ywa `libc++` zamiast `stdc++`. |
| `USE_LTO` | `OFF` | WÄąâ€šÄ…cza optymalizacje w czasie linkowania (Link Time Optimizations). |
| `OPENGLES` | `OFF` | UÄąÄ˝ywa OpenGL ES zamiast standardowego OpenGL. DostÄ™pne wersje "1.0", "2.0". |
| `WINDOWS_CONSOLE`| `OFF` | WÄąâ€šÄ…cza okno konsoli w systemie Windows. |
## Flagi frameworka

Skrypt uÄąÄ˝ywa flag preprocesora do warunkowej kompilacji moduÄąâ€šĂłw:
-   `FRAMEWORK_SOUND`: WÄąâ€šÄ…cza kompilacjÄ™ moduÄąâ€šu dÄąĹźwiÄ™ku.
-   `FRAMEWORK_GRAPHICS`: WÄąâ€šÄ…cza kompilacjÄ™ moduÄąâ€šu grafiki.
-   `FRAMEWORK_NET`: WÄąâ€šÄ…cza kompilacjÄ™ moduÄąâ€šu sieciowego.
-   `FRAMEWORK_XML`: WÄąâ€šÄ…cza kompilacjÄ™ moduÄąâ€šu do parsowania XML (TinyXML).
-   `FRAMEWORK_THREAD_SAFE`: Dodaje definicjÄ™ `THREAD_SAFE`, prawdopodobnie dla kodu wielowÄ…tkowego.
## Struktura projektu (pliki ÄąĹźrĂłdÄąâ€šowe)

Plik definiuje listÄ™ wszystkich plikĂłw ÄąĹźrĂłdÄąâ€šowych (`.h`, `.cpp`, `.c`) skÄąâ€šadajÄ…cych siÄ™ na framework. SÄ… one pogrupowane w logiczne moduÄąâ€šy:

-   **GÄąâ€šĂłwne pliki**: `const.h`, `global.h`, `pch.h`, `luafunctions.cpp`
-   **`util`**: NarzÄ™dzia pomocnicze (kolory, kryptografia, obsÄąâ€šuga PNG, struktury danych jak `Rect`, `Point`).
-   **`stdext`**: Rozszerzenia standardowej biblioteki C++ (obsÄąâ€šuga stringĂłw, czasu, rzutowania typĂłw, wÄ…tkĂłw).
-   **`core`**: RdzeÄąâ€ž aplikacji (pÄ™tla gÄąâ€šĂłwna, obsÄąâ€šuga zdarzeÄąâ€ž, logowanie, zarzÄ…dzanie moduÄąâ€šami i zasobami).
-   **`luaengine`**: Silnik Lua i mechanizmy bindowania C++ do Lua.
-   **`otml`**: Parser i emiter dla jÄ™zyka OTML (OTClient Markup Language).
-   **`platform`**: Kod specyficzny dla platformy (obsÄąâ€šuga okien, obsÄąâ€šuga awarii).
-   **`graphics` (warunkowo)**: Silnik graficzny (OpenGL, shadery, tekstury, fonty, UI).
-   **`sound` (warunkowo)**: Silnik dÄąĹźwiÄ™ku (OpenAL, obsÄąâ€šuga OGG Vorbis).
-   **`net` (warunkowo)**: ObsÄąâ€šuga sieci (poÄąâ€šÄ…czenia, protokoÄąâ€šy, serwer, proxy).
-   **`xml` (warunkowo)**: Parser TinyXML.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

Skrypt wyszukuje i linkuje nastÄ™pujÄ…ce biblioteki zewnÄ™trzne:
-   **Boost** (`system`, `filesystem`): UÄąÄ˝ywane do operacji na systemie plikĂłw i innych podstawowych funkcjonalnoÄąâ€şci.
-   **ZLIB, BZip2, LibZip**: Do kompresji i dekompresji danych.
-   **LuaJIT** lub **Lua**: Silnik skryptowy.
-   **PhysFS**: Wirtualny system plikĂłw, do obsÄąâ€šugi zasobĂłw w archiwach.
-   **OpenSSL**: Do funkcji kryptograficznych (RSA, SHA, MD5).
-   **OpenGL/OpenGLES, EGL**: Do renderowania grafiki.
-   **GLEW**: Do zarzÄ…dzania rozszerzeniami OpenGL.
-   **OpenAL, Vorbis, Ogg**: Do obsÄąâ€šugi dÄąĹźwiÄ™ku.
## Konfiguracja dla WebAssembly (WASM)
Specjalny blok `if(WASM)` dostosowuje kompilacjÄ™ dla platformy WebAssembly przy uÄąÄ˝yciu Emscripten. Ustawia specyficzne flagi (`-s USE_ZLIB=1`, etc.), linkuje prekompilowane biblioteki (`.a`) i doÄąâ€šÄ…cza ÄąĹźrĂłdÄąâ€ša Lua bezpoÄąâ€şrednio do projektu, zamiast linkowaÄ‡ je jako zewnÄ™trznÄ… bibliotekÄ™.
## Flagi kompilatora
Skrypt ustawia rĂłÄąÄ˝ne flagi kompilatora w zaleÄąÄ˝noÄąâ€şci od typu budowania (`CMAKE_BUILD_TYPE`):
-   **Debug**: `-O0 -g` (niska optymalizacja, peÄąâ€šne informacje debugowania).
-   **Release**: `-O2` (wysoka optymalizacja, brak informacji debugowania).
-   **RelWithDebInfo**: `-O1 -g` (Äąâ€şrednia optymalizacja z informacjami debugowania).
-   **Performance**: `-Ofast -march=native` (najwyÄąÄ˝sze optymalizacje, specyficzne dla architektury).

---
# Ä‘Ĺşâ€śâ€ž global.h
## Opis ogĂłlny

Plik `global.h` jest jednym z kluczowych plikĂłw nagÄąâ€šĂłwkowych w frameworku. Jego gÄąâ€šĂłwnym zadaniem jest wÄąâ€šÄ…czenie najwaÄąÄ˝niejszych, globalnie uÄąÄ˝ywanych definicji i nagÄąâ€šĂłwkĂłw w jednym miejscu. DziÄ™ki temu inne pliki mogÄ… doÄąâ€šÄ…czyÄ‡ tylko ten jeden plik, aby uzyskaÄ‡ dostÄ™p do podstawowych typĂłw danych, staÄąâ€šych, makr i narzÄ™dzi.
## Definicje i Makra
## `VALIDATE(expression)`

Jest to makro asercji, ktĂłre jest aktywne tylko w trybie debugowania (gdy `NDEBUG` nie jest zdefiniowane). JeÄąâ€şli wyraÄąÄ˝enie (expression) jest faÄąâ€šszywe, makro wywoÄąâ€šuje funkcjÄ™ `fatalError`, ktĂłra przerywa dziaÄąâ€šanie programu i wyÄąâ€şwietla komunikat o bÄąâ€šÄ™dzie zawierajÄ…cy nazwÄ™ pliku i numer linii. W trybie wydajnoÄąâ€şciowym (`NDEBUG` zdefiniowane) makro jest puste i nie generuje ÄąÄ˝adnego kodu.

`$fenceInfo
# if defined(NDEBUG)
# define VALIDATE(expression) ((void)0)
# else
extern void fatalError(const char* error, const char* file, int line);
# define VALIDATE(expression) { if(!(expression)) fatalError(#expression, __FILE__, __LINE__); };
# endif
```
-   **UÄąÄ˝ycie**: SÄąâ€šuÄąÄ˝y do sprawdzania warunkĂłw, ktĂłre muszÄ… byÄ‡ zawsze prawdziwe w trakcie dziaÄąâ€šania programu, np. sprawdzania, czy wskaÄąĹźnik nie jest `nullptr`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

Plik `global.h` wÄąâ€šÄ…cza nastÄ™pujÄ…ce nagÄąâ€šĂłwki, udostÄ™pniajÄ…c ich zawartoÄąâ€şÄ‡ wszystkim plikom, ktĂłre go doÄąâ€šÄ…czajÄ…:

-   `framework/stdext/compiler.h`: Zawiera definicje specyficzne dla kompilatora.
-   `framework/pch.h`: Prekompilowany nagÄąâ€šĂłwek, ktĂłry zawiera standardowe biblioteki C/C++ oraz biblioteki firm trzecich, takie jak Boost.
-   `framework/const.h`: Definiuje globalne staÄąâ€še, makra i typy wyliczeniowe (enumy).
-   `framework/stdext/stdext.h`: Zawiera rozszerzenia standardowej biblioteki C++, takie jak dodatkowe algorytmy.
-   `framework/util/point.h`, `color.h`, `rect.h`, `size.h`, `matrix.h`: DefiniujÄ… podstawowe struktury danych uÄąÄ˝ywane w grafice i logice.
-   `framework/core/logger.h`: UdostÄ™pnia globalny obiekt `g_logger` do logowania komunikatĂłw.

DziÄ™ki temu `global.h` dziaÄąâ€ša jako centralny punkt dostÄ™pu do najczÄ™Äąâ€şciej uÄąÄ˝ywanych elementĂłw frameworka.

---
# Ä‘Ĺşâ€śâ€ž pch.h
## Opis ogĂłlny

`pch.h` (Precompiled Header) to plik nagÄąâ€šĂłwkowy, ktĂłrego celem jest przyspieszenie procesu kompilacji. Zawiera on dyrektywy `#include` dla nagÄąâ€šĂłwkĂłw, ktĂłre sÄ… czÄ™sto uÄąÄ˝ywane w caÄąâ€šym projekcie, ale rzadko siÄ™ zmieniajÄ…. Kompilator moÄąÄ˝e wstÄ™pnie przetworzyÄ‡ ten plik i zapisaÄ‡ jego stan, co pozwala na ponowne wykorzystanie go podczas kompilacji innych plikĂłw ÄąĹźrĂłdÄąâ€šowych, zamiast parsowaÄ‡ te same nagÄąâ€šĂłwki wielokrotnie.
## ZawartoÄąâ€şÄ‡ pliku

Plik ten jest podzielony na kilka sekcji, grupujÄ…cych nagÄąâ€šĂłwki wedÄąâ€šug ich pochodzenia i przeznaczenia.
## Standardowe nagÄąâ€šĂłwki C

Zawiera podstawowe nagÄąâ€šĂłwki z biblioteki standardowej C, takie jak `cstdio`, `cstdlib`, `cstring`, `cmath`.

`$fenceInfo
# include <cstdio>
# include <cstdlib>
# include <cstddef>
# include <cstring>
# include <cmath>
```
## Standardowe nagÄąâ€šĂłwki STL (C++)

WÄąâ€šÄ…cza najwaÄąÄ˝niejsze i najczÄ™Äąâ€şciej uÄąÄ˝ywane kontenery, strumienie i algorytmy z biblioteki standardowej C++.

`$fenceInfo
# include <iostream>
# include <sstream>
# include <string>
# include <vector>
# include <set>
# include <list>
# include <deque>
# include <map>
# include <algorithm>
# include <functional>
# include <array>
# include <unordered_map>
# include <unordered_set>
# include <tuple>
# include <iomanip>
# include <typeinfo>
```
## Nowoczesne nagÄąâ€šĂłwki C++ (C++11 i nowsze)

WÄąâ€šÄ…cza nagÄąâ€šĂłwki zwiÄ…zane z wielowÄ…tkowoÄąâ€şciÄ…, inteligentnymi wskaÄąĹźnikami, czasem i losowoÄąâ€şciÄ…, wprowadzone w nowszych standardach C++. Plik `filesystem` jest doÄąâ€šÄ…czany warunkowo (poza Androidem).

`$fenceInfo
# include <thread>
# include <memory>
# include <functional>
# include <condition_variable>
# include <mutex>
# include <future>
# include <chrono>
# include <random>
# ifndef ANDROID
# include <filesystem>
# endif
```
## Biblioteka Boost

WÄąâ€šÄ…cza nagÄąâ€šĂłwki z biblioteki Boost, gÄąâ€šĂłwnie z moduÄąâ€šĂłw **Asio** (do operacji sieciowych) i **Beast** (do obsÄąâ€šugi protokoÄąâ€šĂłw HTTP i WebSocket).

-   `boost/system/config.hpp`, `error_code.hpp`: Podstawowe elementy systemu Boost.
-   `boost/asio.hpp`, `beast.hpp`: GÄąâ€šĂłwne nagÄąâ€šĂłwki dla Asio i Beast.
-   NagÄąâ€šĂłwki warunkowe dla SSL (`__EMSCRIPTEN__` wyÄąâ€šÄ…cza je, poniewaÄąÄ˝ obsÄąâ€šuga SSL w przeglÄ…darce jest inna).
-   `boost/algorithm/hex.hpp`: Do operacji na systemie szesnastkowym.

`$fenceInfo
# ifdef ANDROID
# define BOOST_UUID_RANDOM_PROVIDER_FORCE_POSIX
# endif
# include <boost/system/config.hpp>
// ... (inne nagÄąâ€šĂłwki boost)
```
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

Plik `pch.h` jest plikiem "liÄąâ€şciem" w hierarchii zaleÄąÄ˝noÄąâ€şci â€” sam nie zaleÄąÄ˝y od innych plikĂłw projektu. JednakÄąÄ˝e, jest on doÄąâ€šÄ…czany przez `global.h`, co czyni go poÄąâ€şredniÄ… zaleÄąÄ˝noÄąâ€şciÄ… dla niemal kaÄąÄ˝dego pliku w projekcie. Zapewnia on dostÄ™p do szerokiej gamy narzÄ™dzi z biblioteki standardowej C++ i Boost.

---
# Ä‘Ĺşâ€śâ€ž luafunctions.cpp
## Opis ogĂłlny

Plik `luafunctions.cpp` implementuje metodÄ™ `Application::registerLuaFunctions()`, ktĂłra jest kluczowym elementem integracji silnika C++ z Lua. Funkcja ta jest odpowiedzialna za zarejestrowanie (zbindowanie) klas, funkcji i obiektĂłw singletonowych z C++ w globalnym Äąâ€şrodowisku Lua. DziÄ™ki temu skrypty Lua mogÄ… wywoÄąâ€šywaÄ‡ funkcje C++, tworzyÄ‡ obiekty C++ (np. widgety UI) i manipulowaÄ‡ nimi, co stanowi podstawÄ™ modularnoÄąâ€şci i rozszerzalnoÄąâ€şci klienta.
## `Application::registerLuaFunctions()`
## Opis semantyczny

Metoda ta jest wywoÄąâ€šywana jednorazowo podczas inicjalizacji aplikacji (`Application::init`). Przechodzi przez wszystkie gÄąâ€šĂłwne moduÄąâ€šy frameworka (takie jak `Platform`, `Application`, `Crypt`, `ResourceManager`, `UIManager` itd.) i udostÄ™pnia ich publiczne API w Äąâ€şrodowisku Lua. KaÄąÄ˝dy zarejestrowany element staje siÄ™ dostÄ™pny w Lua jako zmienna globalna (np. `g_app`, `g_crypt`) lub jako klasa (np. `UIWidget`).
## Zarejestrowane elementy

PoniÄąÄ˝ej znajduje siÄ™ lista zarejestrowanych elementĂłw pogrupowanych wedÄąâ€šug moduÄąâ€šĂłw.
## Konwersje i narzÄ™dzia globalne

Rejestruje globalne funkcje pomocnicze w Lua do konwersji typĂłw danych miÄ™dzy stringami a obiektami C++ oraz inne narzÄ™dzia.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `torect` | `stdext::from_string<Rect>` | Konwertuje string na obiekt `Rect`. |
| `topoint` | `stdext::from_string<Point>` | Konwertuje string na obiekt `Point`. |
| `ucwords` | `stdext::ucwords` | Zamienia pierwszÄ… literÄ™ kaÄąÄ˝dego sÄąâ€šowa na wielkÄ…. |
| `regexMatch` | `lambda` | Wyszukuje dopasowania wyraÄąÄ˝eÄąâ€ž regularnych w stringu. |
| ... | ... | ... |
## Platform (`g_platform`)

UdostÄ™pnia funkcje zwiÄ…zane z systemem operacyjnym. NiektĂłre funkcje sÄ… dostÄ™pne tylko gdy zdefiniowano `UNSAFE_LUA_FUNCTIONS`.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `spawnProcess` | `Platform::spawnProcess` | Uruchamia nowy proces (niebezpieczne). |
| `getProcessId` | `Platform::getProcessId` | Zwraca ID bieÄąÄ˝Ä…cego procesu. |
| `openUrl` | `Platform::openUrl` | Otwiera podany URL w domyÄąâ€şlnej przeglÄ…darce. |
| `getOSName` | `Platform::getOSName` | Zwraca nazwÄ™ systemu operacyjnego. |
| ... | ... | ... |
## Application (`g_app`)

UdostÄ™pnia API do zarzÄ…dzania gÄąâ€šĂłwnym obiektem aplikacji.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `setName` | `Application::setName` | Ustawia nazwÄ™ aplikacji. |
| `isRunning` | `Application::isRunning` | Sprawdza, czy aplikacja jest uruchomiona. |
| `exit` | `Application::exit` | Inicjuje proces zamykania aplikacji. |
| `getBuildCompiler`| `Application::getBuildCompiler`| Zwraca nazwÄ™ kompilatora uÄąÄ˝ytego do budowy. |
| `isMobile` | `Application::isMobile` | Sprawdza, czy aplikacja dziaÄąâ€ša w trybie mobilnym. |
| ... | ... | ... |
## Crypt (`g_crypt`)

UdostÄ™pnia funkcje kryptograficzne.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `genUUID` | `Crypt::genUUID` | Generuje unikalny identyfikator UUID. |
| `sha1Encode` | `Crypt::sha1Encode` | Koduje string za pomocÄ… SHA1. |
| `rsaGenerateKey`| `Crypt::rsaGenerateKey` | Generuje klucze RSA. |
| ... | ... | ... |
## Clock (`g_clock`)

UdostÄ™pnia funkcje zwiÄ…zane z czasem i zegarem systemowym.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `micros` | `Clock::micros` | Zwraca czas w mikrosekundach od uruchomienia aplikacji. |
| `millis` | `Clock::millis` | Zwraca czas w milisekundach. |
| `seconds` | `Clock::seconds` | Zwraca czas w sekundach. |
| ... | ... | ... |
## ConfigManager (`g_configs`)

API do zarzÄ…dzania plikami konfiguracyjnymi.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `getSettings` | `ConfigManager::getSettings` | Zwraca gÄąâ€šĂłwny obiekt konfiguracyjny. |
| `load` | `ConfigManager::load` | ÄąÂaduje plik konfiguracyjny. |
| ... | ... | ... |
## Logger (`g_logger`)

API do logowania wiadomoÄąâ€şci.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `log` | `Logger::log` | Loguje wiadomoÄąâ€şÄ‡ z podanym poziomem. |
| `debug` | `Logger::debug` | Loguje wiadomoÄąâ€şÄ‡ na poziomie `LogDebug`. |
| ... | ... | ... |
## ResourceManager (`g_resources`)

ZarzÄ…dzanie plikami i zasobami.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `fileExists` | `ResourceManager::fileExists` | Sprawdza, czy plik istnieje. |
| `readFileContents`| `ResourceManager::readFileContentsSafe` | Odczytuje zawartoÄąâ€şÄ‡ pliku. |
| `writeFileContents`|`ResourceManager::writeFileContents` | Zapisuje zawartoÄąâ€şÄ‡ do pliku. |
| `createArchive` | `ResourceManager::createArchive` | Tworzy archiwum ZIP z podanych plikĂłw. |
| ... | ... | ... |
## UI i Grafika (zaleÄąÄ˝ne od `FW_GRAPHICS`)

Rejestruje klasy i funkcje zwiÄ…zane z interfejsem uÄąÄ˝ytkownika, oknem, grafikÄ… i fontami. To najobszerniejsza sekcja.

-   **`g_app` (metody graficzne)**: `setMaxFps`, `getFps`, `doScreenshot`
-   **`g_window`**: ZarzÄ…dzanie oknem aplikacji (`move`, `resize`, `setTitle`, `setFullscreen`).
-   **`g_mouse`**: ZarzÄ…dzanie kursorami myszy.
-   **`g_graphics`**: Informacje o sterowniku graficznym.
-   **`g_textures`**: ZarzÄ…dzanie teksturami.
-   **`g_shaders`**: Tworzenie i zarzÄ…dzanie shaderami.
-   **`g_ui`**: GÄąâ€šĂłwny menedÄąÄ˝er UI (`loadUI`, `createWidget`).
-   **`g_fonts`**: ZarzÄ…dzanie fontami.
-   **`UIWidget`**: Rejestracja klasy bazowej dla wszystkich widgetĂłw z ogromnÄ… liczbÄ… metod (np. `addChild`, `setRect`, `setText`, `setImageSource`).
-   **`UILayout` i pochodne**: Rejestracja klas layoutĂłw (`UIBoxLayout`, `UIVerticalLayout`, `UIGridLayout`, `UIAnchorLayout`).
-   **`UITextEdit`**: Rejestracja widgetu do edycji tekstu.
## SieÄ‡ (zaleÄąÄ˝ne od `FW_NET`)

Rejestruje klasy do obsÄąâ€šugi sieci.

-   **`Server`**: Do tworzenia serwerĂłw nasÄąâ€šuchujÄ…cych.
-   **`Connection`**: Reprezentuje poÄąâ€šÄ…czenie TCP.
-   **`Protocol`**: Implementuje protokĂłÄąâ€š komunikacyjny.
-   **`InputMessage` / `OutputMessage`**: Do odczytu i zapisu pakietĂłw.
-   **`g_proxy`**: MenedÄąÄ˝er proxy.
-   **`g_http`**: Do zapytaÄąâ€ž HTTP/HTTPS i WebSocket.
## DÄąĹźwiÄ™k (zaleÄąÄ˝ne od `FW_SOUND`)

Rejestruje klasy i funkcje do obsÄąâ€šugi dÄąĹźwiÄ™ku.

-   **`g_sounds`**: MenedÄąÄ˝er dÄąĹźwiÄ™ku (`play`, `stopAll`).
-   **`SoundChannel`**: KanaÄąâ€šy dÄąĹźwiÄ™kowe.
-   **`SoundSource`**: ÄąÄ…rĂłdÄąâ€ša dÄąĹźwiÄ™ku.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

Plik ten jest silnie powiÄ…zany z praktycznie kaÄąÄ˝dym moduÄąâ€šem frameworka, poniewaÄąÄ˝ jego zadaniem jest udostÄ™pnienie ich funkcjonalnoÄąâ€şci w Lua. WÄąâ€šÄ…cza nagÄąâ€šĂłwki z:
-   `framework/core`
-   `framework/luaengine`
-   `framework/otml`
-   `framework/util`
-   `framework/graphics` (jeÄąâ€şli `FW_GRAPHICS` jest zdefiniowane)
-   `framework/sound` (jeÄąâ€şli `FW_SOUND` jest zdefiniowane)
-   `framework/net`
-   `framework/http`
-   `framework/proxy`
-   `framework/input`

Jest to centralny punkt Äąâ€šÄ…czÄ…cy warstwÄ™ C++ z warstwÄ… skryptowÄ… Lua.

---
# Ä‘Ĺşâ€śâ€ž resourcemanager.h
## Opis ogĂłlny

Plik `resourcemanager.h` deklaruje klasÄ™ `ResourceManager`, ktĂłra jest singletonem (`g_resources`) odpowiedzialnym za zarzÄ…dzanie wszystkimi zasobami plikĂłw w aplikacji. Abstrakcjonuje dostÄ™p do plikĂłw, umoÄąÄ˝liwiajÄ…c ich odczyt zarĂłwno z fizycznego systemu plikĂłw, jak i z wirtualnych archiwĂłw (np. `data.zip`) lub nawet z pamiÄ™ci (dane wbudowane w plik wykonywalny). Jest to kluczowy element, ktĂłry umoÄąÄ˝liwia Äąâ€šatwe zarzÄ…dzanie zasobami gry, takimi jak grafiki, dÄąĹźwiÄ™ki, skrypty i pliki konfiguracyjne.
## Klasa `ResourceManager`
## Opis semantyczny

`ResourceManager` inicjalizuje wirtualny system plikĂłw oparty na bibliotece **PhysFS**. OkreÄąâ€şla on katalogi robocze (`work dir`) i katalogi do zapisu (`write dir`), montuje archiwa z danymi i dostarcza ujednolicony interfejs do operacji na plikach. Klasa ta obsÄąâ€šuguje rĂłwnieÄąÄ˝ szyfrowanie i deszyfrowanie plikĂłw w locie oraz mechanizmy aktualizacji klienta.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init(const char *argv0)` | Inicjalizuje PhysFS i ustawia Äąâ€şcieÄąÄ˝kÄ™ do pliku binarnego aplikacji. |
| `terminate()` | Deinicjalizuje PhysFS. |
| `launchCorrect(...)` | Sprawdza, czy istnieje nowsza wersja pliku wykonywalnego w katalogu zapisu i jÄ… uruchamia (tylko Windows). |
| `setupWriteDir(...)` | Konfiguruje i montuje katalog zapisu dla danych uÄąÄ˝ytkownika. |
| `setup()` | Wyszukuje i montuje gÄąâ€šĂłwny katalog roboczy (np. z plikiem `init.lua` lub archiwum `data.zip`). |
| `loadDataFromSelf(...)` | PrĂłbuje zaÄąâ€šadowaÄ‡ dane (archiwum) wbudowane w sam plik wykonywalny. |
| `fileExists(...)` | Sprawdza, czy plik istnieje w wirtualnym systemie plikĂłw. |
| `directoryExists(...)` | Sprawdza, czy katalog istnieje. |
| `readFileContents(...)` | Odczytuje zawartoÄąâ€şÄ‡ pliku jako string, opcjonalnie deszyfrujÄ…c go. |
| `writeFileContents(...)` | Zapisuje string do pliku w katalogu zapisu. |
| `openFile(...)` | Otwiera plik i zwraca wskaÄąĹźnik do `FileStream` do odczytu. |
| `createFile(...)` | Tworzy plik i zwraca wskaÄąĹźnik do `FileStream` do zapisu. |
| `deleteFile(...)` | Usuwa plik. |
| `makeDir(...)` | Tworzy katalog. |
| `listDirectoryFiles(...)` | Zwraca listÄ™ plikĂłw w danym katalogu. |
| `resolvePath(...)` | TÄąâ€šumaczy Äąâ€şcieÄąÄ˝kÄ™ relatywnÄ… (np. wzglÄ™dem bieÄąÄ˝Ä…cego skryptu Lua) na Äąâ€şcieÄąÄ˝kÄ™ absolutnÄ… w wirtualnym systemie plikĂłw. |
| `getWorkDir()` | Zwraca gÄąâ€šĂłwny katalog roboczy (zawsze "/"). |
| `getWriteDir()` | Zwraca Äąâ€şcieÄąÄ˝kÄ™ do katalogu zapisu. |
| `getBinaryName()` | Zwraca nazwÄ™ pliku wykonywalnego aplikacji. |
| `fileChecksum(...)` | Oblicza sumÄ™ kontrolnÄ… CRC32 dla pliku. |
| `filesChecksums()` | Zwraca mapÄ™ sum kontrolnych dla wszystkich plikĂłw w zamontowanym archiwum. |
| `selfChecksum()` | Oblicza sumÄ™ kontrolnÄ… CRC32 dla samego pliku wykonywalnego. |
| `updateData(...)` | Aktualizuje pliki w gÄąâ€šĂłwnym archiwum `data.zip`. |
| `updateExecutable(...)` | ZastÄ™puje plik wykonywalny nowÄ… wersjÄ… (np. po aktualizacji). |
| `createArchive(...)` | Tworzy archiwum ZIP w pamiÄ™ci z podanej mapy plikĂłw. |
| `decompressArchive(...)` | Dekompresuje archiwum ZIP (z pliku lub danych w pamiÄ™ci) i zwraca mapÄ™ plikĂłw. |
| `encrypt(...)` | (Tylko z `WITH_ENCRYPTION`) Szyfruje pliki w katalogach `data`, `modules` itp. |
| `setLayout(...)` | Ustawia aktywny layout UI, co wpÄąâ€šywa na rozwiÄ…zywanie Äąâ€şcieÄąÄ˝ek do zasobĂłw. |
## Zmienne prywatne

-   `m_binaryPath`: ÄąĹˇcieÄąÄ˝ka do pliku wykonywalnego.
-   `m_writeDir`: ÄąĹˇcieÄąÄ˝ka do katalogu zapisu.
-   `m_loadedFromMemory`: Flaga wskazujÄ…ca, czy zasoby zostaÄąâ€šy zaÄąâ€šadowane z pamiÄ™ci.
-   `m_loadedFromArchive`: Flaga wskazujÄ…ca, czy zasoby zostaÄąâ€šy zaÄąâ€šadowane z archiwum.
-   `m_memoryData`: WskaÄąĹźnik na dane archiwum w pamiÄ™ci.
-   `m_customEncryption`: Klucz do niestandardowego szyfrowania.
-   `m_layout`: Nazwa aktywnego layoutu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Definicje podstawowych typĂłw w rdzeniu frameworka.
-   **PhysFS**: Biblioteka do obsÄąâ€šugi wirtualnego systemu plikĂłw jest kluczowÄ… zaleÄąÄ˝noÄąâ€şciÄ….
-   **ZLIB, LibZip**: UÄąÄ˝ywane do obsÄąâ€šugi archiwĂłw ZIP.
-   `FileStream`: Klasa `ResourceManager` tworzy i zwraca obiekty `FileStream` do operacji na plikach.
-   `Application`: UÄąÄ˝ywane do sprawdzania stanu aplikacji (np. czy jest zamykana).
-   `Logger`: Do logowania bÄąâ€šÄ™dĂłw i informacji.
-   `Crypt`: Do obliczania sum kontrolnych i (de)szyfrowania.
-   `Http`: UÄąÄ˝ywane w kontekÄąâ€şcie pobierania plikĂłw (`/downloads`).

---
# Ä‘Ĺşâ€śâ€ž adaptiverenderer.cpp
## Opis ogĂłlny

Plik `adaptiverenderer.cpp` zawiera implementacjÄ™ klasy `AdaptiveRenderer`, ktĂłra jest odpowiedzialna za dynamiczne dostosowywanie jakoÄąâ€şci i wydajnoÄąâ€şci renderowania grafiki w zaleÄąÄ˝noÄąâ€şci od aktualnej liczby klatek na sekundÄ™ (FPS). Celem tego mechanizmu jest utrzymanie pÄąâ€šynnoÄąâ€şci dziaÄąâ€šania aplikacji, zwÄąâ€šaszcza na sÄąâ€šabszych komputerach, poprzez redukcjÄ™ liczby renderowanych obiektĂłw lub obniÄąÄ˝enie czÄ™stotliwoÄąâ€şci aktualizacji, gdy FPS spada.
## Zmienne globalne
## `g_adaptiveRenderer`

Globalna instancja klasy `AdaptiveRenderer`, dostÄ™pna w caÄąâ€šym projekcie.

`$fenceInfo
AdaptiveRenderer g_adaptiveRenderer;
```
## Klasa `AdaptiveRenderer`
## `void newFrame()`
## Opis semantyczny
Metoda wywoÄąâ€šywana na poczÄ…tku kaÄąÄ˝dej klatki renderowania. Rejestruje czas bieÄąÄ˝Ä…cej klatki i na podstawie liczby klatek z ostatnich 5 sekund decyduje, czy naleÄąÄ˝y zmieniÄ‡ poziom wydajnoÄąâ€şci (zwiÄ™kszyÄ‡ lub zmniejszyÄ‡).
## DziaÄąâ€šanie
1.  Dodaje bieÄąÄ˝Ä…cy czas (w milisekundach) do kolejki `m_frames`.
2.  Usuwa z kolejki klatki starsze niÄąÄ˝ 5 sekund.
3.  JeÄąâ€şli poziom wydajnoÄąâ€şci jest narzucony (`m_forcedSpeed`), metoda koÄąâ€žczy dziaÄąâ€šanie.
4.  Co 5 sekund (`m_update + 5000 > now`):
    -   Pobiera maksymalny docelowy FPS z `g_app.getMaxFps()`.
    -   JeÄąâ€şli aktualna liczba klatek jest niÄąÄ˝sza niÄąÄ˝ prĂłg, zwiÄ™ksza poziom `m_speed` (obniÄąÄ˝a jakoÄąâ€şÄ‡).
    -   JeÄąâ€şli aktualna liczba klatek jest wyÄąÄ˝sza niÄąÄ˝ prĂłg, zmniejsza poziom `m_speed` (zwiÄ™ksza jakoÄąâ€şÄ‡).
    -   Poziom `m_speed` jest ograniczony do przedziaÄąâ€šu `[1, RenderSpeeds - 1]`.
## `void refresh()`
## Opis semantyczny
Resetuje czas ostatniej aktualizacji poziomu wydajnoÄąâ€şci, co powoduje, ÄąÄ˝e kolejna ocena FPS nastÄ…pi dopiero za 5 sekund.

`$fenceInfo
void AdaptiveRenderer::refresh() {
    m_update = stdext::millis();
}
```
## Metody limitujÄ…ce
## Opis semantyczny
Grupa metod zwracajÄ…cych limity dla rĂłÄąÄ˝nych aspektĂłw renderowania w zaleÄąÄ˝noÄąâ€şci od aktualnego poziomu `m_speed`. Im wyÄąÄ˝szy `m_speed`, tym niÄąÄ˝sze limity i wiÄ™ksze interwaÄąâ€šy, co przekÄąâ€šada siÄ™ na mniejsze obciÄ…ÄąÄ˝enie procesora i karty graficznej.

-   **`effetsLimit()`**: Zwraca maksymalnÄ… liczbÄ™ efektĂłw do renderowania.
-   **`creaturesLimit()`**: Zwraca maksymalnÄ… liczbÄ™ stworzeÄąâ€ž.
-   **`itemsLimit()`**: Zwraca maksymalnÄ… liczbÄ™ przedmiotĂłw.
-   **`mapRenderInterval()`**: Zwraca interwaÄąâ€š (w milisekundach) ponownego renderowania mapy. `0` oznacza renderowanie w kaÄąÄ˝dej klatce.
-   **`textsLimit()`**: Zwraca maksymalnÄ… liczbÄ™ tekstĂłw.
-   **`creaturesRenderInterval()`**: Zwraca interwaÄąâ€š renderowania stworzeÄąâ€ž (obecnie nieuÄąÄ˝ywane).
-   **`allowFading()`**: Zwraca `true`, jeÄąâ€şli dozwolone jest pÄąâ€šynne zanikanie/pojawianie siÄ™ obiektĂłw (tylko na wyÄąÄ˝szych poziomach jakoÄąâ€şci).
-   **`foregroundUpdateInterval()`**: Zwraca interwaÄąâ€š aktualizacji pierwszego planu.
## `std::string getDebugInfo()`
## Opis semantyczny
Zwraca sformatowany ciÄ…g znakĂłw z informacjami debugowania, takimi jak aktualna liczba klatek, bieÄąÄ˝Ä…cy poziom `m_speed` i narzucony poziom `m_forcedSpeed`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/graphicalapplication.h`: UÄąÄ˝ywa `g_app.getMaxFps()` do okreÄąâ€şlenia docelowej liczby klatek.
-   `framework/stdext/format.h`: Do formatowania stringa w `getDebugInfo`.
-   `framework/util/extras.h`: Potencjalnie do flag debugowania.
-   `framework/core/logger.h`: Do logowania.

---
# Ä‘Ĺşâ€śâ€ž adaptiverenderer.h
## Opis ogĂłlny

Plik `adaptiverenderer.h` jest plikiem nagÄąâ€šĂłwkowym dla klasy `AdaptiveRenderer`. Deklaruje on interfejs tej klasy, staÄąâ€še oraz globalnÄ… instancjÄ™ `g_adaptiveRenderer`. UmoÄąÄ˝liwia to innym czÄ™Äąâ€şciom systemu odpytywanie o aktualne limity i ustawienia wydajnoÄąâ€şci renderowania.
## Definicje i Makra
## `constexpr int RenderSpeeds`

Definiuje liczbÄ™ dostÄ™pnych poziomĂłw wydajnoÄąâ€şci renderowania.

`$fenceInfo
constexpr int RenderSpeeds = 5;
```
## Klasa `AdaptiveRenderer`
## Opis semantyczny
Klasa `AdaptiveRenderer` zarzÄ…dza dynamicznym skalowaniem jakoÄąâ€şci grafiki w celu utrzymania pÄąâ€šynnoÄąâ€şci dziaÄąâ€šania aplikacji. Implementuje mechanizm, ktĂłry na podstawie bieÄąÄ˝Ä…cej liczby klatek na sekundÄ™ (FPS) dostosowuje rĂłÄąÄ˝ne parametry renderowania, takie jak limity renderowanych obiektĂłw czy czÄ™stotliwoÄąâ€şÄ‡ odÄąâ€şwieÄąÄ˝ania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void newFrame()` | Rejestruje nowÄ… klatkÄ™ i aktualizuje poziom wydajnoÄąâ€şci, jeÄąâ€şli to konieczne. |
| `void refresh()` | Resetuje zegar aktualizacji, opĂłÄąĹźniajÄ…c nastÄ™pnÄ… ocenÄ™ wydajnoÄąâ€şci. |
| `int effetsLimit()` | Zwraca limit dla renderowanych efektĂłw. |
| `int creaturesLimit()` | Zwraca limit dla renderowanych stworzeÄąâ€ž. |
| `int itemsLimit()` | Zwraca limit dla renderowanych przedmiotĂłw. |
| `int textsLimit()` | Zwraca limit dla renderowanych tekstĂłw. |
| `int mapRenderInterval()` | Zwraca interwaÄąâ€š (opĂłÄąĹźnienie) ponownego renderowania mapy. |
| `int creaturesRenderInterval()` | Zwraca interwaÄąâ€š renderowania stworzeÄąâ€ž. |
| `bool allowFading()` | Sprawdza, czy dozwolone jest renderowanie efektĂłw przejÄąâ€şcia (fading). |
| `int getLevel()` | Zwraca aktualny poziom wydajnoÄąâ€şci (`m_speed`). |
| `int foregroundUpdateInterval()` | Zwraca interwaÄąâ€š aktualizacji pierwszego planu. |
| `std::string getDebugInfo()` | Zwraca informacje debugowania jako string. |
| `void setForcedLevel(int value)` | UmoÄąÄ˝liwia rÄ™czne ustawienie (narzucenie) poziomu wydajnoÄąâ€şci. |
## Zmienne prywatne

-   `m_forcedSpeed`: Narzucony poziom wydajnoÄąâ€şci (-1 oznacza automatyczny).
-   `m_speed`: Aktualny, automatycznie wyliczony poziom wydajnoÄąâ€şci (od 0 do `RenderSpeeds-1`).
-   `m_update`: Czas ostatniej aktualizacji poziomu wydajnoÄąâ€şci.
-   `m_frames`: Lista czasĂłw ostatnich klatek, uÄąÄ˝ywana do obliczania FPS.
## Zmienne globalne

-   `g_adaptiveRenderer`: Globalna instancja klasy `AdaptiveRenderer`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Plik wÄąâ€šÄ…cza `<list>` do przechowywania czasĂłw klatek.
-   Klasa jest uÄąÄ˝ywana przez silnik renderujÄ…cy (np. w `client/mapview.cpp` - niezaÄąâ€šÄ…czony, ale moÄąÄ˝na siÄ™ domyÄąâ€şlaÄ‡), aby dynamicznie ograniczaÄ‡ liczbÄ™ rysowanych obiektĂłw.

---
# Ä‘Ĺşâ€śâ€ž application.cpp
## Opis ogĂłlny

Plik `application.cpp` zawiera implementacjÄ™ klasy `Application`, ktĂłra jest bazowÄ… klasÄ… dla caÄąâ€šej aplikacji. Odpowiada za podstawowy cykl ÄąÄ˝ycia programu, w tym inicjalizacjÄ™, de-inicjalizacjÄ™, obsÄąâ€šugÄ™ sygnaÄąâ€šĂłw systemowych oraz zarzÄ…dzanie gÄąâ€šĂłwnymi komponentami frameworka, takimi jak menedÄąÄ˝er zasobĂłw, menedÄąÄ˝er moduÄąâ€šĂłw, silnik Lua i poÄąâ€šÄ…czenia sieciowe.
## Funkcje globalne
## `exitSignalHandler(int sig)`

Funkcja obsÄąâ€šugujÄ…ca sygnaÄąâ€šy systemowe `SIGTERM` i `SIGINT` (np. zamkniÄ™cie terminala lub Ctrl+C). Po otrzymaniu sygnaÄąâ€šu, dodaje do kolejki zdarzeÄąâ€ž wywoÄąâ€šanie metody `Application::close()`, co pozwala na bezpieczne zamkniÄ™cie aplikacji.

`$fenceInfo
void exitSignalHandler(int sig)
{
    static bool signaled = false;
    switch(sig) {
        case SIGTERM:
        case SIGINT:
            if(!signaled && !g_app.isStopping() && !g_app.isTerminated()) {
                signaled = true;
                g_dispatcher.addEvent(std::bind(&Application::close, &g_app));
}
            break;
}
}
```
## Klasa `Application`
## `Application::Application()`

Konstruktor, ktĂłry ustawia domyÄąâ€şlne wartoÄąâ€şci dla nazwy aplikacji, wersji, kodowania znakĂłw oraz flag stanu. Wykrywa rĂłwnieÄąÄ˝, czy aplikacja dziaÄąâ€ša na platformie mobilnej (Android).
## `void Application::init(std::vector<std::string>& args)`
## Opis semantyczny
Metoda inicjalizujÄ…ca kluczowe komponenty aplikacji. Jest wywoÄąâ€šywana na samym poczÄ…tku dziaÄąâ€šania programu.
## DziaÄąâ€šanie
1.  Rejestruje `exitSignalHandler` do obsÄąâ€šugi sygnaÄąâ€šĂłw zamkniÄ™cia.
2.  Ustawia globalne locale.
3.  Przetwarza argumenty wiersza poleceÄąâ€ž za pomocÄ… `g_platform`.
4.  Inicjalizuje `g_asyncDispatcher` do zadaÄąâ€ž asynchronicznych.
5.  Zapisuje opcje startowe i sprawdza, czy wÄąâ€šÄ…czono tryb mobilny (`-mobile`).
6.  Inicjalizuje menedÄąÄ˝era konfiguracji (`g_configs`).
7.  Inicjalizuje silnik Lua (`g_lua`) i rejestruje funkcje C++ (`registerLuaFunctions`).
8.  Inicjalizuje menedÄąÄ˝era proxy (`g_proxy`).
## `void Application::deinit()`
## Opis semantyczny
Metoda de-inicjalizujÄ…ca, wywoÄąâ€šywana przed zamkniÄ™ciem aplikacji. Dba o poprawne zwolnienie zasobĂłw w odwrotnej kolejnoÄąâ€şci do inicjalizacji.
## DziaÄąâ€šanie
1.  WywoÄąâ€šuje lua `g_app.onTerminate`.
2.  OdÄąâ€šadowuje wszystkie moduÄąâ€šy.
3.  Uruchamia garbage collector Lua, aby zwolniÄ‡ referencje do obiektĂłw.
4.  Przetwarza pozostaÄąâ€še zdarzenia z kolejki.
5.  WyÄąâ€šÄ…cza `g_dispatcher`.
## `void Application::terminate()`
## Opis semantyczny
Finalny etap zamykania aplikacji. Zwalnia zasoby, ktĂłre muszÄ… byÄ‡ zwolnione jako ostatnie.
## DziaÄąâ€šanie
1.  Zamyka wszystkie poÄąâ€šÄ…czenia sieciowe.
2.  Terminuje menedÄąÄ˝era konfiguracji.
3.  Terminuje menedÄąÄ˝era zasobĂłw.
4.  Terminuje silnik Lua.
5.  Terminuje menedÄąÄ˝era proxy.
6.  Resetuje obsÄąâ€šugÄ™ sygnaÄąâ€šĂłw systemowych do domyÄąâ€şlnej.
## `void Application::poll()`
## Opis semantyczny
Przetwarza zdarzenia sieciowe i zdarzenia z gÄąâ€šĂłwnej kolejki (`g_dispatcher`). Jest to serce pÄ™tli zdarzeÄąâ€ž aplikacji.
## `void Application::exit()`

Inicjuje proces zamykania aplikacji poprzez ustawienie flagi `m_stopping` i wywoÄąâ€šanie lua `g_app.onExit`.
## `void Application::quick_exit()`

Natychmiastowo zamyka aplikacjÄ™ z kodem 0, bez zwalniania zasobĂłw.
## `void Application::close()`

PrĂłbuje zamknÄ…Ä‡ aplikacjÄ™, wywoÄąâ€šujÄ…c lua `g_app.onClose`. JeÄąâ€şli skrypt zwrĂłci `false` (lub nic), wywoÄąâ€šywana jest metoda `exit()`.
## `void Application::restart()` i `void Application::restartArgs(const std::vector<std::string>& args)`

Metody do restartowania aplikacji. UruchamiajÄ… nowÄ… instancjÄ™ procesu i natychmiast zamykajÄ… bieÄąÄ˝Ä…cÄ…. UÄąÄ˝ywajÄ… `boost::process` do stworzenia nowego procesu. NiedostÄ™pne na Androidzie i w wersji `FREE_VERSION`.
## `std::string Application::getOs()`

Zwraca nazwÄ™ bieÄąÄ˝Ä…cego systemu operacyjnego ("android", "windows", "mac", "linux").
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/clock.h`: Do operacji na czasie.
-   `framework/core/resourcemanager.h`, `modulemanager.h`, `eventdispatcher.h`, `configmanager.h`: GÄąâ€šĂłwne moduÄąâ€šy frameworka, ktĂłrymi zarzÄ…dza.
-   `asyncdispatcher.h`: Do obsÄąâ€šugi zadaÄąâ€ž w tle.
-   `framework/luaengine/luainterface.h`: Do interakcji z Lua.
-   `framework/platform/platform.h`: Do operacji specyficznych dla platformy.
-   `framework/http/http.h`: Do obsÄąâ€šugi HTTP.
-   `framework/net/connection.h`: Do zarzÄ…dzania poÄąâ€šÄ…czeniami sieciowymi.
-   `framework/proxy/proxy.h`: Do zarzÄ…dzania proxy.
-   `boost/process.hpp`: Do restartowania aplikacji.

---
# Ä‘Ĺşâ€śâ€ž application.h
## Opis ogĂłlny

Plik `application.h` jest plikiem nagÄąâ€šĂłwkowym dla klasy `Application`. Deklaruje on interfejs tej klasy, jej skÄąâ€šadowe oraz zawiera dyrektywy doÄąâ€šÄ…czajÄ…ce jednÄ… z dwĂłch moÄąÄ˝liwych implementacji aplikacji: `GraphicalApplication` lub `ConsoleApplication`, w zaleÄąÄ˝noÄąâ€şci od tego, czy zdefiniowano flagÄ™ `FW_GRAPHICS`.
## Klasa `Application`
## Opis semantyczny
`Application` jest abstrakcyjnÄ… klasÄ… bazowÄ…, ktĂłra definiuje podstawowy interfejs i cykl ÄąÄ˝ycia aplikacji. Zawiera metody do inicjalizacji, de-inicjalizacji, zamykania, restartowania oraz dostarcza informacji o samej aplikacji, takich jak nazwa, wersja czy system operacyjny.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `virtual void init(...)` | Inicjalizuje aplikacjÄ™. |
| `virtual void deinit()` | Zwalnia zasoby przed zamkniÄ™ciem. |
| `virtual void terminate()` | Finalizuje zamykanie aplikacji. |
| `virtual void run() = 0` | Czysto wirtualna metoda, ktĂłra musi byÄ‡ zaimplementowana przez klasy pochodne. Zawiera gÄąâ€šĂłwnÄ… pÄ™tlÄ™ programu. |
| `virtual void poll()` | Przetwarza zdarzenia. |
| `virtual void exit()` | Rozpoczyna proces zamykania. |
| `virtual void quick_exit()` | Natychmiastowe zamkniÄ™cie programu. |
| `virtual void close()` | PrĂłbuje zamknÄ…Ä‡ program (moÄąÄ˝e byÄ‡ przerwane przez skrypt Lua). |
| `void restart()` | Restartuje aplikacjÄ™. |
| `void restartArgs(...)` | Restartuje aplikacjÄ™ z nowymi argumentami. |
| `void setName(...)` | Ustawia nazwÄ™ aplikacji. |
| `void setCompactName(...)` | Ustawia skrĂłconÄ… nazwÄ™ aplikacji. |
| `void setVersion(...)` | Ustawia wersjÄ™ aplikacji. |
| `bool isRunning()` | Zwraca `true`, jeÄąâ€şli aplikacja jest w gÄąâ€šĂłwnej pÄ™tli. |
| `bool isStopping()` | Zwraca `true`, jeÄąâ€şli trwa proces zamykania. |
| `bool isTerminated()`| Zwraca `true`, jeÄąâ€şli aplikacja zostaÄąâ€ša zakoÄąâ€žczona. |
| `const std::string& getName()` | Zwraca nazwÄ™ aplikacji. |
| `std::string getBuildCompiler()` | Zwraca informacje o kompilatorze. |
| `std::string getBuildDate()` | Zwraca datÄ™ kompilacji. |
| `std::string getBuildRevision()` | Zwraca numer rewizji. |
| `std::string getBuildCommit()` | Zwraca hash commita Git. |
| `std::string getBuildType()` | Zwraca typ budowania. |
| `std::string getBuildArch()` | Zwraca architekturÄ™. |
| `std::string getAuthor()` | Zwraca autora. |
| `std::string getOs()` | Zwraca nazwÄ™ systemu operacyjnego. |
| `std::string getStartupOptions()` | Zwraca opcje startowe. |
| `bool isMobile()` | Zwraca `true`, jeÄąâ€şli aplikacja dziaÄąâ€ša w trybie mobilnym. |
## Metody chronione

-   `void registerLuaFunctions()`: Deklaracja metody odpowiedzialnej za bindowanie funkcji C++ do Lua.
## Zmienne chronione

-   `m_charset`: Kodowanie znakĂłw.
-   `m_appName`, `m_appCompactName`, `m_appVersion`: Informacje o aplikacji.
-   `m_startupOptions`: Opcje startowe.
-   `m_running`, `m_stopping`, `m_terminated`, `m_mobile`: Flagi stanu aplikacji.
## DoÄąâ€šÄ…czanie implementacji

W zaleÄąÄ˝noÄąâ€şci od flagi `FW_GRAPHICS`, doÄąâ€šÄ…czany jest jeden z dwĂłch plikĂłw:
-   `graphicalapplication.h`: JeÄąâ€şli `FW_GRAPHICS` jest zdefiniowane, aplikacja bÄ™dzie miaÄąâ€ša interfejs graficzny.
-   `consoleapplication.h`: W przeciwnym razie, bÄ™dzie to aplikacja konsolowa.

`$fenceInfo
# ifdef FW_GRAPHICS
# include "graphicalapplication.h"
# else
# include "consoleapplication.h"
# endif
```
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Zawiera podstawowe definicje i nagÄąâ€šĂłwki uÄąÄ˝ywane w caÄąâ€šym projekcie.
-   Klasa jest oznaczona adnotacjÄ… `@bindsingleton g_app`, co sugeruje, ÄąÄ˝e jej instancja bÄ™dzie dostÄ™pna w Lua pod globalnÄ… nazwÄ… `g_app`.

---
# Ä‘Ĺşâ€śâ€ž asyncdispatcher.h
## Opis ogĂłlny

Plik `asyncdispatcher.h` deklaruje klasÄ™ `AsyncDispatcher`, ktĂłra zarzÄ…dza pulÄ… wÄ…tkĂłw roboczych do wykonywania zadaÄąâ€ž asynchronicznie. Jest to kluczowy komponent do odciÄ…ÄąÄ˝enia gÄąâ€šĂłwnego wÄ…tku aplikacji (wÄ…tku zdarzeÄąâ€ž) z operacji, ktĂłre mogÄ… zajÄ…Ä‡ duÄąÄ˝o czasu, takich jak operacje wejÄąâ€şcia/wyjÄąâ€şcia na plikach, zapytania sieciowe czy intensywne obliczenia.
## Klasa `AsyncDispatcher`
## Opis semantyczny
`AsyncDispatcher` implementuje prosty model producent-konsument. Zadania (funkcje do wykonania) sÄ… dodawane do kolejki, a wÄ…tki robocze pobierajÄ… je i wykonujÄ…. Klasa uÄąÄ˝ywa `std::thread`, `std::mutex` i `std::condition_variable` do synchronizacji.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje dyspozytor i tworzy pierwszy wÄ…tek roboczy. |
| `void terminate()` | Zatrzymuje wszystkie wÄ…tki i czyÄąâ€şci kolejkÄ™ zadaÄąâ€ž. |
| `void spawn_thread()` | Tworzy i uruchamia nowy wÄ…tek roboczy. |
| `void stop()` | Zatrzymuje dziaÄąâ€šanie wszystkich wÄ…tkĂłw roboczych. |
| `template<class F> schedule(const F& task)` | Planuje wykonanie zadania i zwraca `std::shared_future`, ktĂłre pozwoli uzyskaÄ‡ wynik zadania w przyszÄąâ€šoÄąâ€şci. UÄąÄ˝ywa `std::promise` do przekazania wyniku. |
| `void dispatch(std::function<void()> f)` | Dodaje zadanie do kolejki bez oczekiwania na wynik (fire-and-forget). |
## PrzykÄąâ€šad uÄąÄ˝ycia `schedule`
`$fenceInfo
// WÄ…tek gÄąâ€šĂłwny
auto future = g_asyncDispatcher.schedule([]() -> int {
    // DÄąâ€šugotrwaÄąâ€ša operacja
    std::this_thread::sleep_for(std::chrono::seconds(2));
    return 42;
});

// PĂłÄąĹźniej, w wÄ…tku gÄąâ€šĂłwnym
int result = future.get(); // Czeka na zakoÄąâ€žczenie zadania i pobiera wynik
```
## PrzykÄąâ€šad uÄąÄ˝ycia `dispatch`
`$fenceInfo
// WÄ…tek gÄąâ€šĂłwny
g_asyncDispatcher.dispatch([]() {
    // Operacja w tle, ktĂłrej wynik nie jest bezpoÄąâ€şrednio potrzebny
    save_game_state();
});
```
## Metody chronione

-   `void exec_loop()`: GÄąâ€šĂłwna pÄ™tla wykonywana przez kaÄąÄ˝dy wÄ…tek roboczy. Czeka na zadania w kolejce i wykonuje je.
## Zmienne prywatne

-   `m_tasks`: Lista (kolejka) zadaÄąâ€ž do wykonania.
-   `m_threads`: Lista wÄ…tkĂłw roboczych.
-   `m_mutex`: Mutex do ochrony dostÄ™pu do `m_tasks`.
-   `m_condition`: Zmienna warunkowa do powiadamiania wÄ…tkĂłw o nowych zadaniach.
-   `m_running`: Flaga kontrolujÄ…ca, czy wÄ…tki powinny kontynuowaÄ‡ pracÄ™.
## Zmienne globalne

-   `g_asyncDispatcher`: Globalna instancja klasy `AsyncDispatcher`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Podstawowe deklaracje frameworka.
-   `framework/stdext/thread.h`: Zawiera nagÄąâ€šĂłwki `<thread>`, `<mutex>`, `<condition_variable>`.
-   Jest uÄąÄ˝ywany przez inne moduÄąâ€šy do wykonywania operacji w tle, np. `ResourceManager` do zapisu zrzutĂłw ekranu, czy `Http` do zapytaÄąâ€ž sieciowych (chociaÄąÄ˝ `Http` uÄąÄ˝ywa wÄąâ€šasnego `io_service` Boost.Asio, `AsyncDispatcher` moÄąÄ˝e byÄ‡ uÄąÄ˝ywany do przetwarzania wynikĂłw).

---
# Ä‘Ĺşâ€śâ€ž binarytree.cpp
## Opis ogĂłlny

Plik `binarytree.cpp` zawiera implementacjÄ™ klas `BinaryTree` i `OutputBinaryTree`. Te klasy sÄąâ€šuÄąÄ˝Ä… do odczytu i zapisu danych w niestandardowym, hierarchicznym formacie binarnym, ktĂłry przypomina drzewo. Format ten jest uÄąÄ˝ywany w kliencie Tibii do przechowywania danych, np. plikĂłw map (`.otbm`).
## Klasa `BinaryTree`
## `BinaryTree::BinaryTree(const FileStreamPtr& fin)`

Konstruktor, ktĂłry przyjmuje wskaÄąĹźnik do strumienia pliku (`FileStream`) i zapamiÄ™tuje pozycjÄ™ startowÄ…, od ktĂłrej zaczyna siÄ™ wÄ™zeÄąâ€š drzewa.
## `void BinaryTree::skipNodes()`

Metoda pomocnicza, ktĂłra przeskakuje przez zagnieÄąÄ˝dÄąÄ˝one wÄ™zÄąâ€šy w strumieniu danych, aby szybko przejÄąâ€şÄ‡ do koÄąâ€žca bieÄąÄ˝Ä…cego wÄ™zÄąâ€ša bez potrzeby jego peÄąâ€šnego parsowania.
## `void BinaryTree::unserialize()`
## Opis semantyczny
To kluczowa metoda, ktĂłra odczytuje "pÄąâ€šaskie" dane (wÄąâ€šaÄąâ€şciwoÄąâ€şci) bieÄąÄ˝Ä…cego wÄ™zÄąâ€ša ze strumienia pliku i zapisuje je do wewnÄ™trznego bufora (`m_buffer`). Operacja ta jest wykonywana tylko raz (lazy loading), przy pierwszym dostÄ™pie do danych wÄ™zÄąâ€ša. Deserializacja polega na odczytywaniu bajtĂłw aÄąÄ˝ do napotkania znacznika koÄąâ€žca wÄ™zÄąâ€ša (`BINARYTREE_NODE_END`), z uwzglÄ™dnieniem znakĂłw specjalnych (`BINARYTREE_ESCAPE_CHAR`).
## `BinaryTreeVec BinaryTree::getChildren()`

Zwraca wektor wskaÄąĹźnikĂłw do `BinaryTree`, reprezentujÄ…cych wszystkie bezpoÄąâ€şrednie dzieci bieÄąÄ˝Ä…cego wÄ™zÄąâ€ša. Przeszukuje strumieÄąâ€ž w poszukiwaniu znacznikĂłw poczÄ…tku wÄ™zÄąâ€ša (`BINARYTREE_NODE_START`).
## Metody odczytu danych (`getU8`, `getU16`, `getString`, etc.)

SÄ… to metody do odczytywania konkretnych typĂłw danych z wewnÄ™trznego, zdeserializowanego bufora. KaÄąÄ˝de wywoÄąâ€šanie przesuwa wskaÄąĹźnik odczytu (`m_pos`). JeÄąâ€şli bufor nie zostaÄąâ€š jeszcze wypeÄąâ€šniony, najpierw wywoÄąâ€šywana jest metoda `unserialize()`.
## Klasa `OutputBinaryTree`
## `OutputBinaryTree::OutputBinaryTree(const FileStreamPtr& fin)`

Konstruktor, ktĂłry przyjmuje strumieÄąâ€ž pliku do zapisu i natychmiast rozpoczyna nowy wÄ™zeÄąâ€š, zapisujÄ…c znacznik `BINARYTREE_NODE_START`.
## Metody zapisu danych (`addU8`, `addU16`, `addString`, etc.)

Metody te sÄąâ€šuÄąÄ˝Ä… do zapisywania danych do strumienia. UÄąÄ˝ywajÄ… metody `write`, aby zapewniÄ‡ poprawne "uciekanie" (escaping) znakĂłw specjalnych (`0xFD`, `0xFE`, `0xFF`).
## `void OutputBinaryTree::startNode(uint8 node)`

Rozpoczyna nowy, zagnieÄąÄ˝dÄąÄ˝ony wÄ™zeÄąâ€š wewnÄ…trz bieÄąÄ˝Ä…cego wÄ™zÄąâ€ša.
## `void OutputBinaryTree::endNode()`

KoÄąâ€žczy bieÄąÄ˝Ä…cy wÄ™zeÄąâ€š, zapisujÄ…c znacznik `BINARYTREE_NODE_END`.
## `void OutputBinaryTree::write(const uint8* data, size_t size)`

Prywatna metoda pomocnicza, ktĂłra zapisuje surowe dane do strumienia, dodajÄ…c znak `BINARYTREE_ESCAPE_CHAR` przed kaÄąÄ˝dym bajtem, ktĂłry jest znakiem specjalnym.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/binarytree.h`: Plik nagÄąâ€šĂłwkowy dla tych klas.
-   `framework/core/filestream.h`: UÄąÄ˝ywa `FileStream` do operacji na plikach.
-   Format danych, ktĂłry obsÄąâ€šugujÄ… te klasy, jest specyficzny dla klienta Tibii i jest uÄąÄ˝ywany m.in. do parsowania plikĂłw `.otbm` (mapy).

---
# Ä‘Ĺşâ€śâ€ž asyncdispatcher.cpp
## Opis ogĂłlny

Plik `asyncdispatcher.cpp` zawiera implementacjÄ™ klasy `AsyncDispatcher`, ktĂłra zarzÄ…dza asynchronicznym wykonywaniem zadaÄąâ€ž w tle. Jest to realizacja mechanizmu puli wÄ…tkĂłw, ktĂłry pozwala na odciÄ…ÄąÄ˝enie gÄąâ€šĂłwnego wÄ…tku aplikacji.
## Zmienne globalne
## `g_asyncDispatcher`

Globalna instancja klasy `AsyncDispatcher`, zapewniajÄ…ca scentralizowany dostÄ™p do puli wÄ…tkĂłw z dowolnego miejsca w aplikacji.

`$fenceInfo
AsyncDispatcher g_asyncDispatcher;
```
## Klasa `AsyncDispatcher`
## `void AsyncDispatcher::init()`
## Opis semantyczny
Inicjalizuje dyspozytor, wywoÄąâ€šujÄ…c `spawn_thread()` w celu utworzenia i uruchomienia pierwszego wÄ…tku roboczego.
## `void AsyncDispatcher::terminate()`
## Opis semantyczny
Zamyka dyspozytor. Zatrzymuje wszystkie wÄ…tki robocze i czyÄąâ€şci kolejkÄ™ zadaÄąâ€ž.
## `void AsyncDispatcher::spawn_thread()`
## Opis semantyczny
Tworzy nowy `std::thread`, ktĂłry rozpoczyna wykonywanie pÄ™tli `exec_loop()`. WÄ…tek jest dodawany do listy `m_threads`. Ustawia flagÄ™ `m_running` na `true`.
## `void AsyncDispatcher::stop()`
## Opis semantyczny
Bezpiecznie zatrzymuje wszystkie wÄ…tki robocze. Ustawia flagÄ™ `m_running` na `false`, powiadamia wszystkie oczekujÄ…ce wÄ…tki za pomocÄ… `m_condition.notify_all()`, a nastÄ™pnie czeka na ich zakoÄąâ€žczenie za pomocÄ… `thread.join()`.
## `void AsyncDispatcher::exec_loop()`
## Opis semantyczny
Jest to gÄąâ€šĂłwna funkcja pÄ™tli dla kaÄąÄ˝dego wÄ…tku roboczego.
## DziaÄąâ€šanie
1.  WÄ…tek wchodzi w nieskoÄąâ€žczonÄ… pÄ™tlÄ™ i blokuje mutex `m_mutex`.
2.  Czeka na zmiennej warunkowej `m_condition`, aÄąÄ˝ w kolejce `m_tasks` pojawi siÄ™ zadanie lub flaga `m_running` zostanie ustawiona na `false`.
3.  Gdy zostanie obudzony i flaga `m_running` jest `true`, pobiera pierwsze zadanie z kolejki `m_tasks`.
4.  Odblokowuje mutex, aby inne wÄ…tki mogÄąâ€šy dodawaÄ‡ lub pobieraÄ‡ zadania.
5.  Wykonuje pobrane zadanie (`task()`).
6.  Ponownie blokuje mutex i wraca na poczÄ…tek pÄ™tli.
7.  JeÄąâ€şli flaga `m_running` jest `false`, wÄ…tek koÄąâ€žczy dziaÄąâ€šanie.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `asyncdispatcher.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   Klasa intensywnie korzysta z narzÄ™dzi wielowÄ…tkowoÄąâ€şci z biblioteki standardowej C++ (`<thread>`, `<mutex>`, `<condition_variable>`).
-   Jest uÄąÄ˝ywana przez rĂłÄąÄ˝ne moduÄąâ€šy, ktĂłre potrzebujÄ… wykonywaÄ‡ operacje w tle, np. `ResourceManager` do zapisu plikĂłw, `Http` do przetwarzania pobranych danych.

---
# Ä‘Ĺşâ€śâ€ž clock.h
## Opis ogĂłlny

Plik `clock.h` deklaruje klasÄ™ `Clock`, ktĂłra jest singletonem (`g_clock`) odpowiedzialnym za zarzÄ…dzanie czasem w aplikacji. Zapewnia buforowany, spĂłjny czas dla jednej klatki oraz dostÄ™p do "rzeczywistego" czasu systemowego.
## Klasa `Clock`
## Opis semantyczny
Klasa `Clock` ma dwa gÄąâ€šĂłwne zadania:
1.  DostarczaÄ‡ "buforowany" czas, ktĂłry jest staÄąâ€šy w obrÄ™bie jednej iteracji gÄąâ€šĂłwnej pÄ™tli. Metoda `update()` jest wywoÄąâ€šywana raz na klatkÄ™, a metody `micros()`, `millis()`, `seconds()` zwracajÄ… tÄ™ samÄ…, zapisanÄ… wartoÄąâ€şÄ‡ czasu przez caÄąâ€šÄ… klatkÄ™. Zapewnia to spĂłjnoÄąâ€şÄ‡ obliczeÄąâ€ž zaleÄąÄ˝nych od czasu.
2.  DostarczaÄ‡ "rzeczywisty" czas systemowy za pomocÄ… metod `realMicros()` i `realMillis()`, ktĂłre zawsze odczytujÄ… aktualny czas systemowy.

Wszystkie skÄąâ€šadowe przechowujÄ…ce czas sÄ… typu `std::atomic`, co zapewnia bezpieczeÄąâ€žstwo wÄ…tkowe przy odczycie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Clock()` | Konstruktor, inicjalizuje czas na 0. |
| `void update()` | Aktualizuje buforowany czas (`m_currentMicros`, `m_currentMillis`, `m_currentSeconds`) na podstawie aktualnego czasu systemowego. Powinna byÄ‡ wywoÄąâ€šywana raz na klatkÄ™. |
| `ticks_t micros()` | Zwraca buforowany czas w mikrosekundach. |
| `ticks_t millis()` | Zwraca buforowany czas w milisekundach. |
| `float seconds()` | Zwraca buforowany czas w sekundach (jako `float`). |
| `ticks_t realMicros()` | Zwraca aktualny, "rzeczywisty" czas systemowy w mikrosekundach. |
| `ticks_t realMillis()` | Zwraca aktualny, "rzeczywisty" czas systemowy w milisekundach. |
## Zmienne prywatne

-   `m_currentMicros`: Atomowy licznik przechowujÄ…cy buforowany czas w mikrosekundach.
-   `m_currentMillis`: Atomowy licznik przechowujÄ…cy buforowany czas w milisekundach.
-   `m_currentSeconds`: Atomowa zmienna przechowujÄ…ca buforowany czas w sekundach.
## Zmienne globalne

-   `g_clock`: Globalna instancja klasy `Clock`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Definicje podstawowych typĂłw, w tym `ticks_t`.
-   `framework/stdext/time.h`: UÄąÄ˝ywa funkcji `stdext::micros()` i `stdext::millis()` do pobierania czasu systemowego.
-   Klasa jest kluczowa dla caÄąâ€šego systemu, szczegĂłlnie dla `EventDispatcher` (do planowania zdarzeÄąâ€ž), animacji i logiki gry. Metoda `update()` jest wywoÄąâ€šywana w gÄąâ€šĂłwnej pÄ™tli aplikacji (w `GraphicalApplication::run()` i `ConsoleApplication::run()`).

---
# Ä‘Ĺşâ€śâ€ž binarytree.h
## Opis ogĂłlny

Plik `binarytree.h` deklaruje interfejsy dla klas `BinaryTree` i `OutputBinaryTree`. Klasy te sÄąâ€šuÄąÄ˝Ä… do obsÄąâ€šugi niestandardowego, hierarchicznego formatu binarnego, uÄąÄ˝ywanego do serializacji danych w strukturze drzewa. Format ten jest charakterystyczny dla plikĂłw `.otbm` (OTClient Binary Map).
## Definicje i Makra
## Znaczniki binarne

Zdefiniowano trzy specjalne bajty, ktĂłre kontrolujÄ… strukturÄ™ drzewa w strumieniu binarnym:
-   `BINARYTREE_ESCAPE_CHAR` (0xFD): Znak "ucieczki", uÄąÄ˝ywany do kodowania bajtĂłw, ktĂłre majÄ… takÄ… samÄ… wartoÄąâ€şÄ‡ jak inne znaki specjalne.
-   `BINARYTREE_NODE_START` (0xFE): Znacznik poczÄ…tku nowego wÄ™zÄąâ€ša (dziecka).
-   `BINARYTREE_NODE_END` (0xFF): Znacznik koÄąâ€žca bieÄąÄ˝Ä…cego wÄ™zÄąâ€ša.
## Klasa `BinaryTree`
## Opis semantyczny
Klasa `BinaryTree` reprezentuje pojedynczy wÄ™zeÄąâ€š w drzewie danych i sÄąâ€šuÄąÄ˝y do **odczytu** danych z tego wÄ™zÄąâ€ša. DziaÄąâ€ša na strumieniu `FileStream` i implementuje mechanizm leniwego odczytu (lazy loading) â€“ dane wÄąâ€šaÄąâ€şciwoÄąâ€şci wÄ™zÄąâ€ša sÄ… deserializowane do wewnÄ™trznego bufora dopiero przy pierwszej prĂłbie dostÄ™pu do nich.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `BinaryTree(const FileStreamPtr& fin)` | Konstruktor, przyjmuje strumieÄąâ€ž wejÄąâ€şciowy. |
| `seek(uint pos)` | Ustawia pozycjÄ™ odczytu w zdeserializowanym buforze. |
| `skip(uint len)` | Przeskakuje o `len` bajtĂłw w buforze. |
| `tell()` | Zwraca bieÄąÄ˝Ä…cÄ… pozycjÄ™ odczytu w buforze. |
| `size()` | Zwraca rozmiar zdeserializowanych danych wÄ™zÄąâ€ša. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | OdczytujÄ… liczby caÄąâ€škowite bez znaku. |
| `getString(uint16 len = 0)` | Odczytuje ciÄ…g znakĂłw (dÄąâ€šugoÄąâ€şÄ‡ podana lub odczytana jako U16). |
| `getPoint()` | Odczytuje obiekt `Point`. |
| `getChildren()` | Zwraca wektor `BinaryTreePtr` zawierajÄ…cy wszystkie dzieci bieÄąÄ˝Ä…cego wÄ™zÄąâ€ša. |
| `canRead()` | Sprawdza, czy moÄąÄ˝na jeszcze odczytywaÄ‡ dane z bufora. |
## Klasa `OutputBinaryTree`
## Opis semantyczny
Klasa `OutputBinaryTree` jest odpowiednikiem `BinaryTree` do **zapisu** danych w formacie drzewa binarnego. UmoÄąÄ˝liwia tworzenie wÄ™zÄąâ€šĂłw i zapisywanie do nich wÄąâ€šaÄąâ€şciwoÄąâ€şci, dbajÄ…c o poprawne formatowanie i "uciekanie" (escaping) znakĂłw specjalnych.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OutputBinaryTree(const FileStreamPtr& fin)` | Konstruktor, przyjmuje strumieÄąâ€ž wyjÄąâ€şciowy. |
| `addU8()`, `addU16()`, `addU32()` | ZapisujÄ… liczby caÄąâ€škowite bez znaku. |
| `addString(const std::string& v)` | Zapisuje ciÄ…g znakĂłw (z dÄąâ€šugoÄąâ€şciÄ…). |
| `addPos(uint16 x, uint16 y, uint8 z)` | Zapisuje pozycjÄ™ (x, y, z). |
| `addPoint(const Point& point)` | Zapisuje obiekt `Point`. |
| `startNode(uint8 node)` | Rozpoczyna nowy zagnieÄąÄ˝dÄąÄ˝ony wÄ™zeÄąâ€š z danym typem (atrybutem). |
| `endNode()` | KoÄąâ€žczy bieÄąÄ˝Ä…cy wÄ™zeÄąâ€š. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Definicje wskaÄąĹźnikĂłw, np. `FileStreamPtr`.
-   `framework/util/databuffer.h`: WewnÄ™trzny bufor w `BinaryTree` jest typu `DataBuffer`.
-   Jest uÄąÄ˝ywana przez moduÄąâ€šy, ktĂłre muszÄ… przetwarzaÄ‡ dane w formacie `.otbm`, np. edytor map lub sam klient do wczytywania mapy gry.

---
# Ä‘Ĺşâ€śâ€ž config.cpp
## Opis ogĂłlny

Plik `config.cpp` zawiera implementacjÄ™ klasy `Config`, ktĂłra jest opakowaniem na dokument OTML (`OTMLDocument`). SÄąâ€šuÄąÄ˝y do zarzÄ…dzania pojedynczym plikiem konfiguracyjnym, umoÄąÄ˝liwiajÄ…c Äąâ€šatwy odczyt, zapis i modyfikacjÄ™ wartoÄąâ€şci w formacie `key-value` oraz bardziej zÄąâ€šoÄąÄ˝onych struktur zagnieÄąÄ˝dÄąÄ˝onych.
## Klasa `Config`
## `Config::Config()`

Konstruktor. Inicjalizuje pusty dokument OTML (`m_confsDoc`) i zeruje nazwÄ™ pliku (`m_fileName`).
## `bool Config::load(const std::string& file)`
## Opis semantyczny
ÄąÂaduje i parsuje plik konfiguracyjny w formacie OTML.
## DziaÄąâ€šanie
1.  ZapamiÄ™tuje nazwÄ™ pliku w `m_fileName`.
2.  Sprawdza, czy plik istnieje za pomocÄ… `g_resources.fileExists`.
3.  JeÄąâ€şli plik istnieje, parsuje go za pomocÄ… `OTMLDocument::parse`.
4.  W przypadku sukcesu, zastÄ™puje wewnÄ™trzny dokument (`m_confsDoc`) nowo sparsowanym.
5.  W przypadku bÄąâ€šÄ™du parsowania, loguje bÄąâ€šÄ…d i zwraca `false`.
## `bool Config::unload()`

Zwalnia wewnÄ™trzny dokument OTML i resetuje nazwÄ™ pliku. Zwraca `true`, jeÄąâ€şli obiekt byÄąâ€š zaÄąâ€šadowany.
## `bool Config::save()`

Zapisuje bieÄąÄ˝Ä…cÄ… zawartoÄąâ€şÄ‡ dokumentu OTML do pliku, ktĂłrego nazwa jest przechowywana w `m_fileName`. UÄąÄ˝ywa do tego metody `m_confsDoc->save()`.
## `void Config::clear()`

CzyÄąâ€şci wszystkie wÄ™zÄąâ€šy z wewnÄ™trznego dokumentu OTML.
## `void Config::setValue(const std::string& key, const std::string& value)`

Ustawia wartoÄąâ€şÄ‡ dla danego klucza. JeÄąâ€şli wartoÄąâ€şÄ‡ jest pusta, klucz jest usuwany. W przeciwnym razie tworzony jest nowy wÄ™zeÄąâ€š OTML (`OTMLNode`) i dodawany do dokumentu. IstniejÄ…ce wÄ™zÄąâ€šy o tym samym kluczu sÄ… nadpisywane.
## `void Config::setList(const std::string& key, const std::vector<std::string>& list)`

Zapisuje wektor stringĂłw jako listÄ™ w dokumencie OTML. Tworzy wÄ™zeÄąâ€š gÄąâ€šĂłwny o nazwie `key`, a nastÄ™pnie dodaje kaÄąÄ˝dy element wektora jako jego dziecko bez nazwy.
## `bool Config::exists(const std::string& key)`

Sprawdza, czy w dokumencie istnieje wÄ™zeÄąâ€š o podanym kluczu.
## `std::string Config::getValue(const std::string& key)`

Zwraca wartoÄąâ€şÄ‡ stringowÄ… dla podanego klucza. JeÄąâ€şli klucz nie istnieje, zwraca pusty string.
## `std::vector<std::string> Config::getList(const std::string& key)`

Odczytuje listÄ™ stringĂłw z wÄ™zÄąâ€ša o podanym kluczu. Zwraca pusty wektor, jeÄąâ€şli klucz nie istnieje.
## `void Config::remove(const std::string& key)`

Usuwa wÄ™zeÄąâ€š o podanym kluczu z dokumentu.
## `void Config::setNode(const std::string& key, const OTMLNodePtr& node)`

ZastÄ™puje istniejÄ…cy wÄ™zeÄąâ€š nowym wÄ™zÄąâ€šem OTML. Najpierw usuwa stary wÄ™zeÄąâ€š, a nastÄ™pnie dodaje sklonowanÄ… wersjÄ™ nowego.
## `void Config::mergeNode(const std::string& key, const OTMLNodePtr& node)`

ÄąÂÄ…czy podany wÄ™zeÄąâ€š z istniejÄ…cym (lub tworzy nowy). DziaÄąâ€ša podobnie do `setNode`, ale jest uÄąÄ˝ywane do dodawania/aktualizowania danych bez usuwania caÄąâ€šego wÄ™zÄąâ€ša.
## `OTMLNodePtr Config::getNode(const std::string& key)`

Zwraca wskaÄąĹźnik do wÄ™zÄąâ€ša OTML o podanym kluczu.
## `int Config::getNodeSize(const std::string& key)`

Zwraca liczbÄ™ dzieci wÄ™zÄąâ€ša o podanym kluczu. Zwraca 0, jeÄąâ€şli wÄ™zeÄąâ€š nie istnieje.
## `bool Config::isLoaded()`

Zwraca `true`, jeÄąâ€şli obiekt `Config` jest powiÄ…zany z plikiem i ma zaÄąâ€šadowanÄ… zawartoÄąâ€şÄ‡.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/config.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   `framework/core/resourcemanager.h`: UÄąÄ˝ywany do sprawdzania istnienia plikĂłw.
-   `framework/core/configmanager.h`: `ConfigManager` zarzÄ…dza instancjami klasy `Config`.
-   `framework/otml/otml.h`: Intensywnie korzysta z `OTMLDocument` i `OTMLNode` do przechowywania i manipulowania danymi konfiguracyjnymi.

---
# Ä‘Ĺşâ€śâ€ž configmanager.cpp
## Opis ogĂłlny

Plik `configmanager.cpp` zawiera implementacjÄ™ klasy `ConfigManager`, ktĂłra jest singletonem (`g_configs`) sÄąâ€šuÄąÄ˝Ä…cym do zarzÄ…dzania wieloma plikami konfiguracyjnymi (`Config`) w aplikacji. UmoÄąÄ˝liwia Äąâ€šadowanie, tworzenie, pobieranie i zwalnianie konfiguracji na ÄąÄ˝Ä…danie.
## Zmienne globalne
## `g_configs`

Globalna instancja `ConfigManager`, zapewniajÄ…ca centralny punkt dostÄ™pu do wszystkich konfiguracji.

`$fenceInfo
ConfigManager g_configs;
```
## Klasa `ConfigManager`
## `void ConfigManager::init()`
## Opis semantyczny
Inicjalizuje menedÄąÄ˝era. Tworzy gÄąâ€šĂłwny obiekt konfiguracyjny, zwany "settings" (`m_settings`), ktĂłry jest przeznaczony do przechowywania ustawieÄąâ€ž samej aplikacji.
## `void ConfigManager::terminate()`
## Opis semantyczny
Zwalnia wszystkie zarzÄ…dzane obiekty `Config`. Zapewnia, ÄąÄ˝e gÄąâ€šĂłwna konfiguracja (`m_settings`) jest zapisywana przed zamkniÄ™ciem.
## DziaÄąâ€šanie
1.  Zapisuje gÄąâ€šĂłwny plik ustawieÄąâ€ž (`m_settings->save()`).
2.  OdÄąâ€šadowuje (`unload()`) gÄąâ€šĂłwny obiekt ustawieÄąâ€ž.
3.  Iteruje po wszystkich pozostaÄąâ€šych zaÄąâ€šadowanych konfiguracjach i je odÄąâ€šadowuje.
4.  CzyÄąâ€şci listÄ™ `m_configs`.
## `ConfigPtr ConfigManager::getSettings()`

Zwraca wskaÄąĹźnik do gÄąâ€šĂłwnego obiektu konfiguracyjnego `m_settings`.
## `ConfigPtr ConfigManager::get(const std::string& file)`

Wyszukuje i zwraca wskaÄąĹźnik do juÄąÄ˝ zaÄąâ€šadowanego obiektu `Config` na podstawie nazwy pliku. JeÄąâ€şli konfiguracja nie jest zaÄąâ€šadowana, zwraca `nullptr`.
## `ConfigPtr ConfigManager::loadSettings(const std::string file)`

ÄąÂaduje gÄąâ€šĂłwny plik ustawieÄąâ€ž z podanej Äąâ€şcieÄąÄ˝ki. ZastÄ™puje domyÄąâ€şlny, pusty obiekt `m_settings`.
## `ConfigPtr ConfigManager::create(const std::string& file)`

ÄąÂaduje plik konfiguracyjny, a jeÄąâ€şli on nie istnieje, tworzy go. Jest to przydatne do tworzenia domyÄąâ€şlnych plikĂłw konfiguracyjnych przy pierwszym uruchomieniu.
## DziaÄąâ€šanie
1.  PrĂłbuje zaÄąâ€šadowaÄ‡ plik za pomocÄ… `load(file)`.
2.  JeÄąâ€şli Äąâ€šadowanie siÄ™ nie powiedzie (plik nie istnieje), tworzy nowy obiekt `Config`, Äąâ€šaduje go (co tworzy pusty dokument), zapisuje go na dysku (tworzÄ…c plik) i dodaje do listy zarzÄ…dzanych konfiguracji.
## `ConfigPtr ConfigManager::load(const std::string& file)`

ÄąÂaduje plik konfiguracyjny. JeÄąâ€şli plik byÄąâ€š juÄąÄ˝ zaÄąâ€šadowany, zwraca istniejÄ…cÄ… instancjÄ™. W przeciwnym razie tworzy nowy obiekt `Config`, prĂłbuje zaÄąâ€šadowaÄ‡ plik z dysku i, jeÄąâ€şli siÄ™ powiedzie, dodaje go do listy zarzÄ…dzanych konfiguracji.
## `bool ConfigManager::unload(const std::string& file)`

Znajduje obiekt `Config` po nazwie pliku, odÄąâ€šadowuje go (zwalniajÄ…c pamiÄ™Ä‡) i usuwa z listy zarzÄ…dzanych konfiguracji.
## `void ConfigManager::remove(const ConfigPtr config)`

Usuwa podany obiekt `Config` z listy `m_configs`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/configmanager.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   `framework/core/config.h`: `ConfigManager` zarzÄ…dza obiektami typu `Config`.
-   `framework/core/logger.h`: UÄąÄ˝ywany do logowania bÄąâ€šÄ™dĂłw, np. gdy nie moÄąÄ˝na zaÄąâ€šadowaÄ‡ pliku.
-   Jest kluczowym komponentem rdzenia aplikacji, uÄąÄ˝ywanym przez moduÄąâ€šy do odczytu i zapisu swoich konfiguracji.

---
# Ä‘Ĺşâ€śâ€ž configmanager.h
## Opis ogĂłlny

Plik `configmanager.h` deklaruje interfejs klasy `ConfigManager`, ktĂłra peÄąâ€šni rolÄ™ centralnego menedÄąÄ˝era plikĂłw konfiguracyjnych w formacie OTML. UmoÄąÄ˝liwia zarzÄ…dzanie cyklem ÄąÄ˝ycia wielu obiektĂłw `Config`, w tym ich Äąâ€šadowanie, tworzenie i zwalnianie.
## Klasa `ConfigManager`
## Opis semantyczny
`ConfigManager` to klasa singletonowa (`g_configs`), ktĂłra przechowuje listÄ™ wszystkich aktywnych obiektĂłw `Config`. WyrĂłÄąÄ˝nia jeden specjalny obiekt konfiguracyjny, `m_settings`, przeznaczony na gÄąâ€šĂłwne ustawienia aplikacji. PozostaÄąâ€še konfiguracje sÄ… zarzÄ…dzane w liÄąâ€şcie `m_configs` i identyfikowane po nazwie pliku.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedÄąÄ˝era, tworzÄ…c domyÄąâ€şlny obiekt `m_settings`. |
| `void terminate()` | Zwalnia wszystkie zaÄąâ€šadowane konfiguracje, zapisujÄ…c wczeÄąâ€şniej `m_settings`. |
| `ConfigPtr getSettings()` | Zwraca wskaÄąĹźnik do gÄąâ€šĂłwnego obiektu ustawieÄąâ€ž aplikacji. |
| `ConfigPtr get(const std::string& file)` | Wyszukuje i zwraca wskaÄąĹźnik do zaÄąâ€šadowanej konfiguracji o podanej nazwie pliku. |
| `ConfigPtr create(const std::string& file)` | ÄąÂaduje konfiguracjÄ™ z pliku lub tworzy nowy, pusty plik, jeÄąâ€şli nie istnieje. |
| `ConfigPtr loadSettings(const std::string file)` | ÄąÂaduje gÄąâ€šĂłwny plik ustawieÄąâ€ž aplikacji z podanej Äąâ€şcieÄąÄ˝ki. |
| `ConfigPtr load(const std::string& file)` | ÄąÂaduje dodatkowy plik konfiguracyjny. |
| `bool unload(const std::string& file)` | Zwalnia i usuwa z menedÄąÄ˝era konfiguracjÄ™ o podanej nazwie pliku. |
| `void remove(const ConfigPtr config)` | Usuwa podany obiekt `Config` z wewnÄ™trznej listy. |
## Zmienne chronione

-   `m_settings`: WskaÄąĹźnik na gÄąâ€šĂłwny obiekt `Config` przechowujÄ…cy ustawienia aplikacji.
## Zmienne prywatne

-   `m_configs`: Lista wskaÄąĹźnikĂłw na wszystkie dodatkowe zaÄąâ€šadowane obiekty `Config`.
## Zmienne globalne

-   `g_configs`: Globalna instancja singletonu `ConfigManager`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/config.h`: Deklaracja klasy `Config`, ktĂłrÄ… zarzÄ…dza `ConfigManager`.
-   Jest oznaczona adnotacjÄ… `@bindsingleton g_configs`, co oznacza, ÄąÄ˝e jej funkcjonalnoÄąâ€şÄ‡ jest dostÄ™pna w skryptach Lua pod globalnÄ… nazwÄ… `g_configs`.
-   WspĂłÄąâ€špracuje z `Application` (ktĂłra wywoÄąâ€šuje `init` i `terminate`) oraz z moduÄąâ€šami, ktĂłre potrzebujÄ… dostÄ™pu do swoich plikĂłw konfiguracyjnych.

---
# Ä‘Ĺşâ€śâ€ž config.h
## Opis ogĂłlny

Plik `config.h` deklaruje klasÄ™ `Config`, ktĂłra jest obiektowym interfejsem do odczytu, zapisu i manipulacji danymi w plikach konfiguracyjnych formatu OTML. Klasa ta dziedziczy po `LuaObject`, co oznacza, ÄąÄ˝e jej instancje mogÄ… byÄ‡ tworzone i uÄąÄ˝ywane w skryptach Lua.
## Klasa `Config`
## Opis semantyczny
`Config` dziaÄąâ€ša jako opakowanie (wrapper) na `OTMLDocument`. KaÄąÄ˝da instancja tej klasy reprezentuje jeden plik konfiguracyjny. UmoÄąÄ˝liwia operacje takie jak ustawianie wartoÄąâ€şci (`setValue`), list (`setList`), a takÄąÄ˝e bardziej zÄąâ€šoÄąÄ˝onych struktur (`setNode`, `mergeNode`). Wszystkie dane sÄ… przechowywane wewnÄ™trznie jako drzewo wÄ™zÄąâ€šĂłw OTML.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Config()` | Konstruktor domyÄąâ€şlny. |
| `bool load(const std::string& file)` | ÄąÂaduje i parsuje konfiguracjÄ™ z pliku OTML. |
| `bool unload()` | Zwalnia zaÄąâ€šadowanÄ… konfiguracjÄ™. |
| `bool save()` | Zapisuje bieÄąÄ˝Ä…cy stan konfiguracji do pliku. |
| `void clear()` | Usuwa wszystkie dane z konfiguracji. |
| `void setValue(...)` | Ustawia wartoÄąâ€şÄ‡ dla danego klucza. |
| `void setList(...)` | Ustawia listÄ™ wartoÄąâ€şci dla danego klucza. |
| `std::string getValue(...)` | Odczytuje wartoÄąâ€şÄ‡ dla danego klucza. |
| `std::vector<std::string> getList(...)` | Odczytuje listÄ™ wartoÄąâ€şci dla danego klucza. |
| `void setNode(...)` | ZastÄ™puje wÄ™zeÄąâ€š o danym kluczu nowym wÄ™zÄąâ€šem OTML. |
| `void mergeNode(...)` | ÄąÂÄ…czy (merge) podany wÄ™zeÄąâ€š z istniejÄ…cym wÄ™zÄąâ€šem o danym kluczu. |
| `OTMLNodePtr getNode(...)` | Zwraca wskaÄąĹźnik do wÄ™zÄąâ€ša OTML o podanym kluczu. |
| `int getNodeSize(...)` | Zwraca liczbÄ™ dzieci wÄ™zÄąâ€ša o danym kluczu. |
| `bool exists(const std::string& key)` | Sprawdza, czy klucz istnieje. |
| `void remove(const std::string& key)` | Usuwa klucz i jego wartoÄąâ€şÄ‡. |
| `std::string getFileName()` | Zwraca nazwÄ™ pliku powiÄ…zanego z tÄ… konfiguracjÄ…. |
| `bool isLoaded()` | Zwraca `true`, jeÄąâ€şli konfiguracja zostaÄąâ€ša zaÄąâ€šadowana z pliku. |
| `ConfigPtr asConfig()` | Zwraca `shared_ptr` do siebie (`static_self_cast`). |
## Zmienne prywatne

-   `m_fileName`: Nazwa pliku konfiguracyjnego.
-   `m_confsDoc`: WskaÄąĹźnik na `OTMLDocument`, ktĂłry przechowuje dane konfiguracyjne.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Deklaracje typĂłw, w tym `ConfigPtr`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`, aby byÄ‡ dostÄ™pnÄ… w Lua.
-   `framework/otml/declarations.h`: UÄąÄ˝ywa `OTMLDocumentPtr` i `OTMLNodePtr` do przechowywania danych.
-   Jest oznaczona jako `@bindclass`, co oznacza, ÄąÄ˝e metody tej klasy sÄ… dostÄ™pne do wywoÄąâ€šania z poziomu skryptĂłw Lua na instancjach obiektĂłw `Config`.
-   Instancje tej klasy sÄ… tworzone i zarzÄ…dzane przez `ConfigManager`.

---
# Ä‘Ĺşâ€śâ€ž clock.cpp
## Opis ogĂłlny

Plik `clock.cpp` zawiera implementacjÄ™ metod klasy `Clock`. Odpowiada za dostarczanie mechanizmĂłw pomiaru czasu, ktĂłre sÄ… kluczowe dla pÄ™tli gÄąâ€šĂłwnej aplikacji, planowania zdarzeÄąâ€ž i animacji.
## Zmienne globalne
## `g_clock`

Globalna instancja klasy `Clock`, ktĂłra jest uÄąÄ˝ywana w caÄąâ€šym frameworku do uzyskiwania spĂłjnych informacji o czasie.

`$fenceInfo
Clock g_clock;
```
## Klasa `Clock`
## `Clock::Clock()`

Konstruktor klasy. Inicjalizuje wszystkie liczniki czasu na 0.
## `void Clock::update()`
## Opis semantyczny
Aktualizuje wewnÄ™trzne, "buforowane" liczniki czasu. Ta metoda powinna byÄ‡ wywoÄąâ€šywana raz na kaÄąÄ˝dÄ… iteracjÄ™ gÄąâ€šĂłwnej pÄ™tli aplikacji. DziÄ™ki temu wszystkie operacje wewnÄ…trz jednej klatki (np. logika gry, animacje, fizyka) bazujÄ… na tej samej wartoÄąâ€şci czasu, co zapobiega niespĂłjnoÄąâ€şciom.
## DziaÄąâ€šanie
1.  Pobiera aktualny czas systemowy w mikrosekundach za pomocÄ… `stdext::micros()`.
2.  Zapisuje tÄ™ wartoÄąâ€şÄ‡ do atomowej zmiennej `m_currentMicros`.
3.  Oblicza i zapisuje czas w milisekundach (`m_currentMillis`) i sekundach (`m_currentSeconds`).
## `ticks_t Clock::realMicros()`

Zwraca "na ÄąÄ˝ywo" aktualny czas systemowy w mikrosekundach. W przeciwieÄąâ€žstwie do `micros()`, ta metoda nie korzysta z buforowanej wartoÄąâ€şci i przy kaÄąÄ˝dym wywoÄąâ€šaniu odpytuje system operacyjny.
## `ticks_t Clock::realMillis()`

Zwraca "na ÄąÄ˝ywo" aktualny czas systemowy w milisekundach. Podobnie jak `realMicros()`, odczytuje aktualny czas.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/clock.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   `framework/stdext/time.h`: UÄąÄ˝ywa funkcji `stdext::micros()` i `stdext::millis()`, ktĂłre sÄ… opakowaniem na `std::chrono` do pobierania czasu o wysokiej precyzji.
-   Jest uÄąÄ˝ywana przez `EventDispatcher` do planowania zdarzeÄąâ€ž, `GraphicalApplication` do synchronizacji pÄ™tli renderowania oraz przez wiele innych komponentĂłw do mierzenia czasu trwania operacji.

---
# Ä‘Ĺşâ€śâ€ž consoleapplication.h
## Opis ogĂłlny

Plik `consoleapplication.h` deklaruje klasÄ™ `ConsoleApplication`, ktĂłra jest konkretnÄ… implementacjÄ… klasy `Application` dla aplikacji dziaÄąâ€šajÄ…cej w trybie konsolowym, bez interfejsu graficznego. Jest uÄąÄ˝ywana, gdy flaga `FW_GRAPHICS` nie jest zdefiniowana podczas kompilacji.
## Klasa `ConsoleApplication`
## Opis semantyczny
`ConsoleApplication` dziedziczy po `Application` i implementuje jej czysto wirtualnÄ… metodÄ™ `run()`. Ta implementacja zawiera prostÄ… pÄ™tlÄ™ gÄąâ€šĂłwnÄ…, ktĂłra przetwarza zdarzenia i usypia wÄ…tek na krĂłtki czas, aby uniknÄ…Ä‡ 100% uÄąÄ˝ycia procesora.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void run()` | Implementuje gÄąâ€šĂłwnÄ… pÄ™tlÄ™ aplikacji konsolowej. |
## Zmienne globalne

-   `g_app`: Globalna instancja `ConsoleApplication`, ktĂłra staje siÄ™ gÄąâ€šĂłwnym obiektem aplikacji, gdy kompilacja odbywa siÄ™ bez wsparcia dla grafiki.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/application.h`: Klasa bazowa, z ktĂłrej dziedziczy `ConsoleApplication`.
-   Jest to jedna z dwĂłch moÄąÄ˝liwych implementacji aplikacji, wybierana w `application.h` za pomocÄ… dyrektyw preprocesora.

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## Opis ogĂłlny

Plik `declarations.h` w module `core` jest plikiem nagÄąâ€šĂłwkowym sÄąâ€šuÄąÄ˝Ä…cym do wczesnych deklaracji (forward declarations) klas i definicji typĂłw wskaÄąĹźnikĂłw (`typedef`) dla rdzennych komponentĂłw frameworka. Jego celem jest rozwiÄ…zanie problemu zaleÄąÄ˝noÄąâ€şci cyklicznych miÄ™dzy plikami nagÄąâ€šĂłwkowymi oraz zmniejszenie iloÄąâ€şci doÄąâ€šÄ…czanych nagÄąâ€šĂłwkĂłw w plikach, ktĂłre potrzebujÄ… jedynie znaÄ‡ istnienie danego typu, a nie jego peÄąâ€šnÄ… definicjÄ™.
## Wczesne deklaracje (Forward Declarations)

Plik deklaruje istnienie nastÄ™pujÄ…cych klas, nie definiujÄ…c ich zawartoÄąâ€şci:

-   `ConfigManager`
-   `ModuleManager`
-   `ResourceManager`
-   `Module`
-   `Config`
-   `Event`
-   `ScheduledEvent`
-   `FileStream`
-   `BinaryTree`
-   `OutputBinaryTree`
## Definicje typĂłw (Typedefs)

Na podstawie wczesnych deklaracji, plik definiuje typy inteligentnych wskaÄąĹźnikĂłw (`shared_object_ptr`), ktĂłre sÄ… uÄąÄ˝ywane w caÄąâ€šym frameworku. Upraszcza to skÄąâ€šadniÄ™ i zapewnia spĂłjnoÄąâ€şÄ‡.

-   `ModulePtr`: `stdext::shared_object_ptr<Module>`
-   `ConfigPtr`: `stdext::shared_object_ptr<Config>`
-   `EventPtr`: `stdext::shared_object_ptr<Event>`
-   `ScheduledEventPtr`: `stdext::shared_object_ptr<ScheduledEvent>`
-   `FileStreamPtr`: `stdext::shared_object_ptr<FileStream>`
-   `BinaryTreePtr`: `stdext::shared_object_ptr<BinaryTree>`
-   `OutputBinaryTreePtr`: `stdext::shared_object_ptr<OutputBinaryTree>`
-   `BinaryTreeVec`: `std::vector<BinaryTreePtr>`
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Zawiera podstawowe definicje i typy, w tym `stdext::shared_object_ptr`.
-   Ten plik jest doÄąâ€šÄ…czany przez wiele innych plikĂłw nagÄąâ€šĂłwkowych w module `core` i poza nim, aby umoÄąÄ˝liwiÄ‡ deklarowanie zmiennych i parametrĂłw funkcji bez koniecznoÄąâ€şci doÄąâ€šÄ…czania peÄąâ€šnych definicji klas.

---
# Ä‘Ĺşâ€śâ€ž event.cpp
## Opis ogĂłlny

Plik `event.cpp` zawiera implementacjÄ™ klasy `Event`, ktĂłra jest podstawowym obiektem reprezentujÄ…cym jednorazowe, opĂłÄąĹźnione lub cykliczne zdarzenie w systemie.
## Klasa `Event`
## `Event::Event(const std::string& function, const std::function<void()>& callback, bool botSafe)`

Konstruktor, ktĂłry inicjalizuje zdarzenie.

-   **Parametry**:
    -   `function`: Nazwa funkcji (lub opis), uÄąÄ˝ywana do celĂłw debugowania i statystyk.
    -   `callback`: Funkcja (lambda lub `std::function`), ktĂłra zostanie wykonana.
    -   `botSafe`: Flaga okreÄąâ€şlajÄ…ca, czy zdarzenie moÄąÄ˝e byÄ‡ wywoÄąâ€šane przez bota (uÄąÄ˝ywane do filtrowania w niektĂłrych kontekstach).
-   **DziaÄąâ€šanie**: Inicjalizuje flagi `m_canceled` i `m_executed` na `false` oraz przechowuje podane parametry.
## `Event::~Event()`

Destruktor. W trybie debugowania, `VALIDATE(m_callback == nullptr)` sprawdza, czy `callback` zostaÄąâ€š poprawnie zwolniony, aby zapobiec wyciekom pamiÄ™ci lub wiszÄ…cym referencjom.
## `void Event::execute()`
## Opis semantyczny
Wykonuje `callback` powiÄ…zany ze zdarzeniem.
## DziaÄąâ€šanie
1.  Sprawdza, czy zdarzenie nie zostaÄąâ€šo anulowane (`!m_canceled`) i czy nie zostaÄąâ€šo juÄąÄ˝ wykonane (`!m_executed`).
2.  JeÄąâ€şli warunki sÄ… speÄąâ€šnione i `callback` istnieje, wywoÄąâ€šuje go.
3.  Ustawia flagÄ™ `m_executed` na `true`.
4.  Resetuje `m_callback` do `nullptr`, aby zwolniÄ‡ wszelkie zasoby (np. obiekty przechwycone przez lambdÄ™).
## `void Event::cancel()`
## Opis semantyczny
Anuluje zdarzenie, zapobiegajÄ…c jego przyszÄąâ€šemu wykonaniu.
## DziaÄąâ€šanie
1.  Ustawia flagÄ™ `m_canceled` na `true`.
2.  Resetuje `m_callback` do `nullptr`, aby natychmiast zwolniÄ‡ zasoby.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/event.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   Jest klasÄ… bazowÄ… dla `ScheduledEvent`.
-   Jest zarzÄ…dzana przez `EventDispatcher`, ktĂłry przechowuje instancje `Event` w kolejce i wywoÄąâ€šuje ich metodÄ™ `execute()`.

---
# Ä‘Ĺşâ€śâ€ž event.h
## Opis ogĂłlny

Plik `event.h` deklaruje klasÄ™ `Event`, ktĂłra jest podstawowÄ… klasÄ… do obsÄąâ€šugi zdarzeÄąâ€ž w systemie opartym na kolejce zdarzeÄąâ€ž. Reprezentuje pojedyncze zadanie, ktĂłre ma zostaÄ‡ wykonane w przyszÄąâ€šoÄąâ€şci przez `EventDispatcher`.
## Klasa `Event`
## Opis semantyczny
`Event` to obiekt, ktĂłry enkapsuluje funkcjÄ™ zwrotnÄ… (`callback`) do wykonania. Dziedziczy po `LuaObject`, co pozwala na przekazywanie go do skryptĂłw Lua. Posiada mechanizmy do wykonania, anulowania i sprawdzania jego stanu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Event(...)` | Konstruktor. |
| `virtual ~Event()` | Destruktor. |
| `virtual void execute()` | Wykonuje `callback`, jeÄąâ€şli zdarzenie nie jest anulowane. |
| `void cancel()` | Anuluje zdarzenie, zapobiegajÄ…c jego wykonaniu. |
| `bool isCanceled()` | Zwraca `true`, jeÄąâ€şli zdarzenie zostaÄąâ€šo anulowane. |
| `bool isExecuted()` | Zwraca `true`, jeÄąâ€şli zdarzenie zostaÄąâ€šo juÄąÄ˝ wykonane. |
| `bool isBotSafe()` | Zwraca `true`, jeÄąâ€şli zdarzenie jest bezpieczne do wykonania w kontekÄąâ€şcie bota. |
| `const std::string& getFunction()` | Zwraca nazwÄ™/opis funkcji powiÄ…zanej ze zdarzeniem. |
## Zmienne chronione

-   `m_function`: `std::string` przechowujÄ…ca nazwÄ™ funkcji dla celĂłw debugowania.
-   `m_callback`: `std::function<void()>` zawierajÄ…ca kod do wykonania.
-   `m_canceled`: Flaga wskazujÄ…ca, czy zdarzenie zostaÄąâ€šo anulowane.
-   `m_executed`: Flaga wskazujÄ…za, czy zdarzenie zostaÄąâ€šo wykonane.
-   `m_botSafe`: Flaga bezpieczeÄąâ€žstwa.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/luaengine/luaobject.h`: Jest klasÄ… pochodnÄ… `LuaObject`.
-   Jest uÄąÄ˝ywana przez `EventDispatcher` do tworzenia i zarzÄ…dzania kolejkÄ… zdarzeÄąâ€ž.
-   Jest klasÄ… bazowÄ… dla `ScheduledEvent`.
-   Oznaczona jako `@bindclass`, co oznacza, ÄąÄ˝e jest dostÄ™pna w Lua, a jej metody (`cancel`, `execute` itd.) mogÄ… byÄ‡ wywoÄąâ€šywane ze skryptĂłw.

---
# Ä‘Ĺşâ€śâ€ž eventdispatcher.cpp
## Opis ogĂłlny

Plik `eventdispatcher.cpp` zawiera implementacjÄ™ klasy `EventDispatcher`, ktĂłra jest sercem systemu zdarzeÄąâ€ž. Odpowiada za zarzÄ…dzanie kolejkÄ… zdarzeÄąâ€ž natychmiastowych oraz kolejkÄ… priorytetowÄ… zdarzeÄąâ€ž zaplanowanych w czasie.
## Zmienne globalne

-   `g_dispatcher`: Globalna instancja `EventDispatcher` dla gÄąâ€šĂłwnego wÄ…tku aplikacji (logika gry, sieÄ‡).
-   `g_graphicsDispatcher`: Globalna instancja `EventDispatcher` dla wÄ…tku graficznego.
-   `g_mainThreadId`, `g_graphicsThreadId`, `g_dispatcherThreadId`: PrzechowujÄ… identyfikatory wÄ…tkĂłw w celu weryfikacji, czy dana operacja jest wykonywana w odpowiednim wÄ…tku.
## Klasa `EventDispatcher`
## `void EventDispatcher::shutdown()`
## Opis semantyczny
Zamyka dyspozytor, przetwarzajÄ…c wszystkie pozostaÄąâ€še zdarzenia i anulujÄ…c zaplanowane.
## DziaÄąâ€šanie
1.  Przetwarza wszystkie zdarzenia z `m_eventList` za pomocÄ… `poll()`.
2.  Iteruje po wszystkich zdarzeniach w `m_scheduledEventList`, anuluje je i usuwa z kolejki.
3.  Ustawia flagÄ™ `m_disabled` na `true`, aby zapobiec dodawaniu nowych zdarzeÄąâ€ž.
## `void EventDispatcher::poll()`
## Opis semantyczny
GÄąâ€šĂłwna metoda przetwarzajÄ…ca zdarzenia. WywoÄąâ€šywana regularnie w pÄ™tli aplikacji.
## DziaÄąâ€šanie
1.  **Przetwarzanie zdarzeÄąâ€ž zaplanowanych (`m_scheduledEventList`)**:
    -   Sprawdza kolejkÄ™ priorytetowÄ… i wykonuje wszystkie zdarzenia, dla ktĂłrych minÄ…Äąâ€š czas (`remainingTicks() <= 0`).
    -   JeÄąâ€şli zdarzenie jest cykliczne (`nextCycle()` zwraca `true`), jest ponownie dodawane do kolejki z nowym czasem wykonania.
2.  **Przetwarzanie zdarzeÄąâ€ž natychmiastowych (`m_eventList`)**:
    -   Wchodzi w pÄ™tlÄ™, ktĂłra wykonuje wszystkie zdarzenia z `m_eventList`.
    -   PÄ™tla jest powtarzana, jeÄąâ€şli w trakcie wykonywania zdarzeÄąâ€ž zostaÄąâ€šy dodane nowe (np. zdarzenie A dodaje zdarzenie B), aby zapewniÄ‡, ÄąÄ˝e wszystkie zdarzenia zwiÄ…zane z bieÄąÄ˝Ä…cÄ… klatkÄ… zostanÄ… wykonane przed jej zakoÄąâ€žczeniem.
    -   Posiada zabezpieczenie przed nieskoÄąâ€žczonÄ… pÄ™tlÄ… (jeÄąâ€şli zdarzenia ciÄ…gle dodajÄ… nowe zdarzenia).
3.  Zapisuje statystyki dotyczÄ…ce liczby przetworzonych zdarzeÄąâ€ž.
## `ScheduledEventPtr EventDispatcher::scheduleEventEx(...)`

Tworzy i dodaje do kolejki priorytetowej nowe jednorazowe zdarzenie zaplanowane, ktĂłre zostanie wykonane po upÄąâ€šywie `delay` milisekund.
## `ScheduledEventPtr EventDispatcher::cycleEventEx(...)`

Tworzy i dodaje do kolejki priorytetowej nowe cykliczne zdarzenie zaplanowane, ktĂłre bÄ™dzie wykonywane co `delay` milisekund.
## `EventPtr EventDispatcher::addEventEx(...)`

Dodaje nowe zdarzenie do kolejki zdarzeÄąâ€ž natychmiastowych. JeÄąâ€şli `pushFront` jest `true`, zdarzenie jest dodawane na poczÄ…tek kolejki, co gwarantuje jego wykonanie w bieÄąÄ˝Ä…cej iteracji pÄ™tli `poll()`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/eventdispatcher.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/clock.h`: UÄąÄ˝ywa `g_clock` do sprawdzania czasu dla zdarzeÄąâ€ž zaplanowanych.
-   `framework/core/graphicalapplication.h`: UÄąÄ˝ywa `g_app.isOnInputEvent()` do oznaczenia, czy zdarzenie zostaÄąâ€šo wywoÄąâ€šane w trakcie obsÄąâ€šugi zdarzenia wejÄąâ€şciowego.
-   `framework/graphics/graph.h`: Zapisuje statystyki do `g_graphs`.
-   `framework/util/stats.h`: UÄąÄ˝ywa `AutoStat` do profilowania.
-   `framework/core/timer.h`: UÄąÄ˝ywany do zabezpieczenia przed nieskoÄąâ€žczonymi pÄ™tlami.
-   Jest kluczowym komponentem, uÄąÄ˝ywanym przez niemal kaÄąÄ˝dÄ… czÄ™Äąâ€şÄ‡ aplikacji do planowania i wykonywania operacji w sposĂłb asynchroniczny (wzglÄ™dem gÄąâ€šĂłwnej pÄ™tli).

---
# Ä‘Ĺşâ€śâ€ž eventdispatcher.h
## Opis ogĂłlny

Plik `eventdispatcher.h` deklaruje interfejs klasy `EventDispatcher` oraz powiÄ…zane z niÄ… globalne instancje i makra. Definiuje on publiczne API do zarzÄ…dzania kolejkÄ… zdarzeÄąâ€ž w aplikacji.
## Definicje i Makra
## Makra pomocnicze do dodawania zdarzeÄąâ€ž

UpraszczajÄ… one wywoÄąâ€šania metod `...Ex`, automatycznie dodajÄ…c nazwÄ™ bieÄąÄ˝Ä…cej funkcji (`__FUNCTION__`) jako opis zdarzenia dla celĂłw debugowania.

-   `addEvent(...)`: Opakowanie na `addEventEx(__FUNCTION__, ...)`
-   `scheduleEvent(...)`: Opakowanie na `scheduleEventEx(__FUNCTION__, ...)`
-   `cycleEvent(...)`: Opakowanie na `cycleEventEx(__FUNCTION__, ...)`
## Makra do walidacji wÄ…tkĂłw

SÄąâ€šuÄąÄ˝Ä… do sprawdzania, czy dana funkcja jest wywoÄąâ€šywana w odpowiednim wÄ…tku, co jest kluczowe dla bezpieczeÄąâ€žstwa w Äąâ€şrodowisku wielowÄ…tkowym.

-   `VALIDATE_GRAPHICS_THREAD()`: Sprawdza, czy bieÄąÄ˝Ä…cy wÄ…tek to wÄ…tek graficzny.
-   `VALIDATE_DISPATCHER_THREAD()`: Sprawdza, czy bieÄąÄ˝Ä…cy wÄ…tek to wÄ…tek dyspozytora (gÄąâ€šĂłwny wÄ…tek logiki).
## Klasa `EventDispatcher`
## Opis semantyczny
`EventDispatcher` jest centralnym mechanizmem do zarzÄ…dzania i wykonywania zadaÄąâ€ž w sposĂłb asynchroniczny, ale w ramach jednego, okreÄąâ€şlonego wÄ…tku. Posiada dwie kolejki: jednÄ… dla zdarzeÄąâ€ž natychmiastowych i drugÄ… (priorytetowÄ…) dla zdarzeÄąâ€ž zaplanowanych w czasie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void shutdown()` | Zamyka dyspozytor, czyszczÄ…c i anulujÄ…c wszystkie zdarzenia. |
| `void poll()` | Przetwarza zdarzenia, ktĂłre sÄ… gotowe do wykonania. |
| `EventPtr addEventEx(...)` | Dodaje zdarzenie do wykonania w nastÄ™pnej iteracji pÄ™tli `poll()`. |
| `ScheduledEventPtr scheduleEventEx(...)` | Planuje jednorazowe wykonanie zdarzenia po okreÄąâ€şlonym czasie. |
| `ScheduledEventPtr cycleEventEx(...)` | Planuje cykliczne wykonywanie zdarzenia co okreÄąâ€şlony czas. |
| `bool isBotSafe()` | Zwraca, czy aktualnie wykonywane zdarzenie jest oznaczone jako "bezpieczne dla bota". |
## Zmienne prywatne

-   `m_eventList`: Lista (`std::list`) zdarzeÄąâ€ž do natychmiastowego wykonania.
-   `m_pollEventsSize`: Rozmiar `m_eventList` na poczÄ…tku pÄ™tli `poll()`, aby obsÄąâ€šuÄąÄ˝yÄ‡ zdarzenia dodane w trakcie.
-   `m_disabled`: Flaga blokujÄ…ca dodawanie nowych zdarzeÄąâ€ž po wywoÄąâ€šaniu `shutdown()`.
-   `m_botSafe`: Flaga stanu dla aktualnie wykonywanego zdarzenia.
-   `m_mutex`: Mutex rekurencyjny do ochrony kolejek.
-   `m_scheduledEventList`: Kolejka priorytetowa (`std::priority_queue`) dla zdarzeÄąâ€ž zaplanowanych w czasie.
## Zmienne globalne

-   `g_dispatcher`: Globalny dyspozytor dla gÄąâ€šĂłwnego wÄ…tku.
-   `g_graphicsDispatcher`: Globalny dyspozytor dla wÄ…tku graficznego.
-   `g_mainThreadId`, `g_dispatcherThreadId`, `g_graphicsThreadId`: Identyfikatory wÄ…tkĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/clock.h`: Wymagany do obsÄąâ€šugi czasu.
-   `framework/core/scheduledevent.h`: Definicja `ScheduledEvent` i komparatora `lessScheduledEvent`.
-   `<queue>`: UÄąÄ˝ywany do implementacji kolejki priorytetowej.

---
# Ä‘Ĺşâ€śâ€ž filestream.cpp
## Opis ogĂłlny

Plik `filestream.cpp` zawiera implementacjÄ™ klasy `FileStream`, ktĂłra jest opakowaniem (wrapperem) na operacje plikowe, gÄąâ€šĂłwnie z wykorzystaniem biblioteki **PhysFS**. UmoÄąÄ˝liwia zarĂłwno odczyt z plikĂłw na dysku, jak i z danych w pamiÄ™ci (np. z wbudowanego archiwum lub zdekompresowanych danych).
## Klasa `FileStream`
## Konstruktory

-   **`FileStream::FileStream(const std::string& name, PHYSFS_File *fileHandle, bool writeable)`**: Tworzy strumieÄąâ€ž na podstawie otwartego uchwytu pliku PhysFS.
-   **`FileStream::FileStream(const std::string& name, std::string&& buffer)`**: Tworzy strumieÄąâ€ž na podstawie bufora danych w pamiÄ™ci (`std::string`). PrĂłbuje rĂłwnieÄąÄ˝ zdekompresowaÄ‡ bufor, jeÄąâ€şli jest on w formacie GZIP.
## `bool FileStream::initFromGzip(const std::string& buffer)`

Prywatna metoda pomocnicza, ktĂłra sprawdza, czy bufor danych jest skompresowany za pomocÄ… GZIP (na podstawie "magicznych bajtĂłw"). JeÄąâ€şli tak, dekompresuje go za pomocÄ… biblioteki ZLIB i zapisuje wynik do wewnÄ™trznego bufora `m_data`.
## `FileStream::~FileStream()` i `void FileStream::close()`

Destruktor i metoda `close()` zwalniajÄ… zasoby. JeÄąâ€şli strumieÄąâ€ž byÄąâ€š otwarty z pliku PhysFS, zamyka uchwyt `m_fileHandle`. CzyÄąâ€şci rĂłwnieÄąÄ˝ wewnÄ™trzne bufory danych (`m_data`, `m_strData`).
## `void FileStream::flush()`

W przypadku strumienia do zapisu, zapisuje zawartoÄąâ€şÄ‡ bufora `m_data` na dysk za pomocÄ… `PHYSFS_writeBytes`.
## `int FileStream::read(void* buffer, uint32 size, uint32 nmemb)`

Odczytuje dane ze strumienia. JeÄąâ€şli strumieÄąâ€ž jest oparty na pliku, uÄąÄ˝ywa `PHYSFS_readBytes`. JeÄąâ€şli na buforze w pamiÄ™ci, kopiuje dane z `m_strData` lub `m_data` i przesuwa wskaÄąĹźnik odczytu `m_pos`.
## `void FileStream::write(const void *buffer, uint32 count)`

Zapisuje dane do strumienia. Dla plikĂłw uÄąÄ˝ywa `PHYSFS_writeBytes`, a dla buforĂłw w pamiÄ™ci dodaje dane do `m_data`.
## `seek`, `skip`, `size`, `tell`, `eof`

Implementacje standardowych operacji na strumieniach, ktĂłre delegujÄ… wywoÄąâ€šania do odpowiednich funkcji PhysFS lub operujÄ… na wewnÄ™trznym wskaÄąĹźniku `m_pos` i rozmiarze bufora.
## Metody odczytu typĂłw (`getU8`, `getU16`, `getString`, etc.)

Metody te sÄąâ€šuÄąÄ˝Ä… do odczytywania konkretnych typĂłw danych ze strumienia. DziaÄąâ€šajÄ… zarĂłwno na plikach PhysFS, jak i na buforach w pamiÄ™ci. WykonujÄ… konwersjÄ™ z porzÄ…dku bajtĂłw Little Endian.
## `BinaryTreePtr FileStream::getBinaryTree()`

Rozpoczyna odczyt zagnieÄąÄ˝dÄąÄ˝onej struktury `BinaryTree` ze strumienia, sprawdzajÄ…c najpierw znacznik poczÄ…tku wÄ™zÄąâ€ša.
## Metody zapisu typĂłw (`addU8`, `addU16`, `addString`, etc.)

SÄąâ€šuÄąÄ˝Ä… do zapisywania danych do strumienia.
## `void FileStream::throwError(...)`

Metoda pomocnicza do generowania wyjÄ…tkĂłw z dodatkowymi informacjami o nazwie pliku i bÄąâ€šÄ™dzie PhysFS.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/filestream.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   `framework/core/binarytree.h`: UÄąÄ˝ywana do odczytu i zapisu struktur `BinaryTree`.
-   `framework/core/application.h`: UÄąÄ˝ywana do sprawdzania, czy aplikacja jest w trakcie zamykania.
-   **PhysFS**: Kluczowa zaleÄąÄ˝noÄąâ€şÄ‡ do operacji na plikach w wirtualnym systemie plikĂłw.
-   **ZLIB**: UÄąÄ˝ywana do dekompresji GZIP.
-   Jest tworzona i zarzÄ…dzana przez `ResourceManager` i uÄąÄ˝ywana w caÄąâ€šym projekcie do odczytu zasobĂłw.

---
# Ä‘Ĺşâ€śâ€ž filestream.h
## Opis ogĂłlny

Plik `filestream.h` deklaruje klasÄ™ `FileStream`, ktĂłra jest kluczowym elementem systemu zarzÄ…dzania zasobami. Stanowi ona abstrakcjÄ™ nad strumieniem danych, ktĂłry moÄąÄ˝e pochodziÄ‡ z pliku na dysku (obsÄąâ€šugiwanego przez PhysFS) lub bezpoÄąâ€şrednio z bufora w pamiÄ™ci. Klasa dziedziczy po `LuaObject`, dziÄ™ki czemu moÄąÄ˝e byÄ‡ uÄąÄ˝ywana w skryptach Lua.
## Klasa `FileStream`
## Opis semantyczny
`FileStream` dostarcza interfejs podobny do standardowych strumieni plikĂłw, umoÄąÄ˝liwiajÄ…c sekwencyjny odczyt i zapis rĂłÄąÄ˝nych typĂłw danych (liczby caÄąâ€škowite, stringi, dane binarne). Jest to podstawowe narzÄ™dzie do parsowania plikĂłw binarnych i tekstowych w caÄąâ€šym projekcie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `FileStream(...)` | Konstruktory tworzÄ…ce strumieÄąâ€ž z uchwytu pliku PhysFS lub z bufora w pamiÄ™ci. |
| `~FileStream()` | Destruktor. |
| `close()` | Zamyka strumieÄąâ€ž i zwalnia zasoby. |
| `flush()` | Wymusza zapis buforowanych danych do pliku (dla strumieni do zapisu). |
| `write(...)` | Zapisuje blok danych do strumienia. |
| `read(...)` | Odczytuje blok danych ze strumienia. |
| `seek(uint pos)` | Ustawia pozycjÄ™ wskaÄąĹźnika w strumieniu. |
| `skip(uint len)` | Przesuwa wskaÄąĹźnik o `len` bajtĂłw. |
| `size()` | Zwraca caÄąâ€škowity rozmiar strumienia. |
| `tell()` | Zwraca bieÄąÄ˝Ä…cÄ… pozycjÄ™ wskaÄąĹźnika. |
| `eof()` | Zwraca `true`, jeÄąâ€şli osiÄ…gniÄ™to koniec strumienia. |
| `name()` | Zwraca nazwÄ™/ÄąĹźrĂłdÄąâ€šo strumienia. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | OdczytujÄ… liczby caÄąâ€škowite bez znaku. |
| `get8()`, `get16()`, `get32()`, `get64()` | OdczytujÄ… liczby caÄąâ€škowite ze znakiem. |
| `getString()` | Odczytuje string (poprzedzony 2-bajtowÄ… dÄąâ€šugoÄąâ€şciÄ…). |
| `getBinaryTree()` | Odczytuje i zwraca obiekt `BinaryTree`. |
| `startNode(uint8 n)` | Rozpoczyna zapis nowego wÄ™zÄąâ€ša w formacie `BinaryTree`. |
| `endNode()` | KoÄąâ€žczy zapis wÄ™zÄąâ€ša. |
| `addU8()`, ..., `addString()` | ZapisujÄ… rĂłÄąÄ˝ne typy danych do strumienia. |
| `asFileStream()` | Zwraca `shared_ptr` do siebie (`static_self_cast`). |
## Zmienne prywatne

-   `m_name`: Nazwa pliku lub ÄąĹźrĂłdÄąâ€ša danych.
-   `m_fileHandle`: WskaÄąĹźnik na uchwyt pliku PhysFS (jeÄąâ€şli dotyczy).
-   `m_pos`: BieÄąÄ˝Ä…ca pozycja odczytu/zapisu w buforze pamiÄ™ci.
-   `m_writeable`: Flaga wskazujÄ…ca, czy strumieÄąâ€ž jest otwarty do zapisu.
-   `m_caching`: Flaga wskazujÄ…ca, czy strumieÄąâ€ž operuje na buforze w pamiÄ™ci.
-   `m_data`: Bufor danych (`DataBuffer<uint8_t>`) dla strumieni w pamiÄ™ci.
-   `m_strData`: Bufor danych (`std::string`) dla strumieni w pamiÄ™ci.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Definicje typĂłw, np. `BinaryTreePtr`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   `framework/util/databuffer.h`: UÄąÄ˝ywa `DataBuffer` do przechowywania danych.
-   `framework/util/point.h`: Do zapisu i odczytu obiektĂłw `Point`.
-   `physfs.h`: Wymagany do deklaracji `PHYSFS_File`.
-   Klasa jest oznaczona jako `@bindclass`, co oznacza, ÄąÄ˝e jest dostÄ™pna w Lua. Jest to kluczowe dla moduÄąâ€šĂłw, ktĂłre muszÄ… parsowaÄ‡ niestandardowe formaty plikĂłw ze skryptĂłw.

---
# Ä‘Ĺşâ€śâ€ž graphicalapplication.cpp
## Opis ogĂłlny

Plik `graphicalapplication.cpp` zawiera implementacjÄ™ klasy `GraphicalApplication`, ktĂłra jest konkretnÄ… implementacjÄ… `Application` dla aplikacji z interfejsem graficznym. Odpowiada za inicjalizacjÄ™, zarzÄ…dzanie i zamykanie wszystkich podsystemĂłw graficznych, a takÄąÄ˝e za implementacjÄ™ gÄąâ€šĂłwnej pÄ™tli renderowania i logiki.
## Zmienne globalne
## `g_app`

Globalna instancja `GraphicalApplication`, ktĂłra jest gÄąâ€šĂłwnym obiektem aplikacji, gdy kompilacja odbywa siÄ™ z flagÄ… `FW_GRAPHICS`.

`$fenceInfo
GraphicalApplication g_app;
```
## Klasa `GraphicalApplication`
## `void GraphicalApplication::init(std::vector<std::string>& args)`
## Opis semantyczny
Inicjalizuje aplikacjÄ™ graficznÄ…. WywoÄąâ€šuje najpierw `Application::init()`, a nastÄ™pnie inicjalizuje wszystkie komponenty zwiÄ…zane z grafikÄ….
## DziaÄąâ€šanie
1.  WywoÄąâ€šuje `Application::init(args)`.
2.  Inicjalizuje okno platformy (`g_window.init()`).
3.  Ustawia callbacki dla okna: `onResize`, `onInputEvent`, `onClose`.
4.  Inicjalizuje menedÄąÄ˝era myszy (`g_mouse.init()`).
5.  Inicjalizuje menedÄąÄ˝era UI (`g_ui.init()`).
6.  Inicjalizuje silnik graficzny (`g_graphics.init()`).
7.  WywoÄąâ€šuje pierwsze zdarzenie zmiany rozmiaru.
8.  Inicjalizuje menedÄąÄ˝era dÄąĹźwiÄ™ku (`g_sounds.init()`), jeÄąâ€şli `FW_SOUND` jest zdefiniowane.
## `void GraphicalApplication::deinit()`

Deinicjalizuje aplikacjÄ™ w odwrotnej kolejnoÄąâ€şci, ukrywajÄ…c okno i zwalniajÄ…c zasoby.
## `void GraphicalApplication::terminate()`

Finalizuje zamykanie podsystemĂłw graficznych, w tym `g_ui`, `g_sounds`, `g_mouse` i `g_graphics`.
## `void GraphicalApplication::run()`
## Opis semantyczny
Implementuje gÄąâ€šĂłwnÄ… pÄ™tlÄ™ aplikacji, ktĂłra jest podzielona na dwa rĂłwnolegÄąâ€še wÄ…tki:
1.  **WÄ…tek logiki (`worker`)**: Odpowiada za aktualizacjÄ™ stanu gry, przetwarzanie zdarzeÄąâ€ž i przygotowywanie kolejek rysowania (`DrawQueue`).
2.  **WÄ…tek renderowania (gÄąâ€šĂłwny wÄ…tek)**: Odpowiada za przetwarzanie zdarzeÄąâ€ž okna, renderowanie zawartoÄąâ€şci przygotowanych kolejek na ekranie i synchronizacjÄ™ klatek.
## DziaÄąâ€šanie wÄ…tku logiki (`worker`)
-   W nieskoÄąâ€žczonej pÄ™tli:
    -   Aktualizuje zegar (`g_clock.update()`).
    -   Przetwarza zdarzenia (`poll()`).
    -   Czeka, jeÄąâ€şli poprzednia klatka nie zostaÄąâ€ša jeszcze wyrenderowana.
    -   Renderuje UI do trzech osobnych kolejek: `MapBackgroundPane`, `MapForegroundPane`, `ForegroundPane`.
    -   Przekazuje gotowe kolejki do wÄ…tku renderowania za pomocÄ… mutexu.
    -   Usypia na 1ms, jeÄąâ€şli `m_maxFps > 0` lub wÄąâ€šÄ…czona jest synchronizacja pionowa.
## DziaÄąâ€šanie wÄ…tku renderowania (gÄąâ€šĂłwnego)
-   W nieskoÄąâ€žczonej pÄ™tli:
    -   Aktualizuje zegar i przetwarza zdarzenia graficzne (`pollGraphics()`).
    -   Czeka na gotowe kolejki rysowania z wÄ…tku logiki.
    -   Aktualizuje `AdaptiveRenderer`.
    -   Synchronizuje klatki zgodnie z `m_maxFps`.
    -   Ustawia `FrameBuffer` do renderowania poza ekranem, jeÄąâ€şli skalowanie jest wÄąâ€šÄ…czone.
    -   Renderuje tÄąâ€šo mapy do `m_mapFramebuffer`.
    -   Renderuje wÄąâ€šaÄąâ€şciwÄ… scenÄ™, Äąâ€šÄ…czÄ…c tÄąâ€šo mapy, pierwszy plan mapy i interfejs uÄąÄ˝ytkownika.
    -   JeÄąâ€şli wÄąâ€šÄ…czono skalowanie, rysuje zawartoÄąâ€şÄ‡ `m_framebuffer` na ekranie.
    -   Rysuje grafy debugowania.
    -   Zamienia bufory (`g_window.swapBuffers()`).
## `void GraphicalApplication::poll()` i `void GraphicalApplication::pollGraphics()`

Metody pomocnicze wywoÄąâ€šywane w odpowiednich wÄ…tkach do przetwarzania zdarzeÄąâ€ž. `poll()` obsÄąâ€šuguje dÄąĹźwiÄ™k i logikÄ™, a `pollGraphics()` obsÄąâ€šuguje zdarzenia okna i aktualizacjÄ™ tekstĂłw.
## Inne metody

-   `close()`: WywoÄąâ€šywana przy zamykaniu okna.
-   `resize()`: WywoÄąâ€šywana przy zmianie rozmiaru okna.
-   `inputEvent()`: Przekazuje zdarzenia wejÄąâ€şciowe do `UIManager`.
-   `doScreenshot()`: Robi zrzut ekranu i zapisuje go do pliku asynchronicznie.
-   `scaleUp()`, `scaleDown()`, `scale()`: ZarzÄ…dzajÄ… skalowaniem interfejsu.
-   `setSmooth()`: WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza wygÄąâ€šadzanie dla `m_mapFramebuffer`.
-   `doMapScreenshot()`: Robi zrzut ekranu samej mapy.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to centralna klasa, ktĂłra integruje prawie wszystkie moduÄąâ€šy graficzne i rdzenia.
-   ZaleÄąÄ˝y od `Application`, `PlatformWindow`, `UIManager`, `Graphics`, `TextureManager`, `Painter`, `SoundManager` i innych.
-   UÄąÄ˝ywa `std::thread` i `std::mutex` do implementacji wielowÄ…tkowej pÄ™tli.

---
# Ä‘Ĺşâ€śâ€ž inputevent.h
## Opis ogĂłlny

Plik `inputevent.h` deklaruje strukturÄ™ `InputEvent`, ktĂłra jest uÄąÄ˝ywana do przekazywania informacji o zdarzeniach wejÄąâ€şciowych (z klawiatury i myszy) w systemie. Jest to prosta struktura danych, ktĂłra agreguje wszystkie moÄąÄ˝liwe parametry zdarzenia.
## Struktura `InputEvent`
## Opis semantyczny
Struktura `InputEvent` jest uniwersalnym kontenerem na dane o zdarzeniach. W zaleÄąÄ˝noÄąâ€şci od pola `type`, inne pola przechowujÄ… odpowiednie informacje. Na przykÄąâ€šad, dla zdarzenia klawiatury (`KeyDownInputEvent`), pole `keyCode` bÄ™dzie miaÄąâ€šo znaczenie, a dla zdarzenia myszy (`MouseMoveInputEvent`) - `mousePos` i `mouseMoved`.
## Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `type` | `Fw::InputEventType` | Typ zdarzenia (np. wciÄąâ€şniÄ™cie klawisza, ruch myszy). |
| `wheelDirection` | `Fw::MouseWheelDirection` | Kierunek przewijania kĂłÄąâ€škiem myszy (`MouseWheelUp` lub `MouseWheelDown`). |
| `mouseButton` | `Fw::MouseButton` | Przycisk myszy, ktĂłry wywoÄąâ€šaÄąâ€š zdarzenie. |
| `keyCode` | `Fw::Key` | Kod wciÄąâ€şniÄ™tego klawisza. |
| `keyText` | `std::string` | Znak tekstowy odpowiadajÄ…cy wciÄąâ€şniÄ™temu klawiszowi (dla `KeyTextInputEvent`). |
| `keyboardModifiers`| `int` | Flagi bitowe dla klawiszy modyfikujÄ…cych (Ctrl, Alt, Shift). |
| `mousePos` | `Point` | Aktualna pozycja kursora myszy. |
| `mouseMoved` | `Point` | Wektor przesuniÄ™cia kursora myszy od ostatniego zdarzenia. |
| `autoRepeatTicks`| `int` | Czas (w milisekundach), przez jaki klawisz jest przytrzymywany (dla `KeyPressInputEvent`). |
## Metody

-   **`InputEvent()`**: Konstruktor, inicjalizuje strukturÄ™.
-   **`reset(Fw::InputEventType eventType = Fw::NoInputEvent)`**: Resetuje wszystkie pola do wartoÄąâ€şci domyÄąâ€şlnych i ustawia nowy typ zdarzenia.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Podstawowe deklaracje.
-   Struktura ta jest tworzona w klasie `PlatformWindow` (np. `win32window.cpp`) na podstawie zdarzeÄąâ€ž systemowych, a nastÄ™pnie przekazywana do `GraphicalApplication` i dalej do `UIManager`, ktĂłry rozsyÄąâ€ša je do odpowiednich widgetĂłw.

---
# Ä‘Ĺşâ€śâ€ž graphicalapplication.h
## Opis ogĂłlny

Plik `graphicalapplication.h` deklaruje klasÄ™ `GraphicalApplication`, ktĂłra jest implementacjÄ… `Application` dla aplikacji z interfejsem graficznym. Jest to gÄąâ€šĂłwna klasa zarzÄ…dzajÄ…ca pÄ™tlÄ… renderowania, zdarzeniami wejÄąâ€şciowymi i komponentami graficznymi.
## Klasa `GraphicalApplication`
## Opis semantyczny
Dziedziczy po `Application` i implementuje jej metody wirtualne, dodajÄ…c funkcjonalnoÄąâ€şÄ‡ specyficznÄ… dla aplikacji graficznej. Odpowiada za koordynacjÄ™ miÄ™dzy oknem (`PlatformWindow`), menedÄąÄ˝erem UI (`UIManager`), silnikiem renderujÄ…cym (`Painter`) i innymi systemami. Implementuje wielowÄ…tkowÄ… pÄ™tlÄ™ gÄąâ€šĂłwnÄ…, gdzie logika jest oddzielona od renderowania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init(...)` | Inicjalizuje podsystemy graficzne. |
| `void deinit()` | Zwalnia zasoby graficzne przed zamkniÄ™ciem. |
| `void terminate()` | Finalizuje zamykanie podsystemĂłw graficznych. |
| `void run()` | Uruchamia gÄąâ€šĂłwnÄ…, wielowÄ…tkowÄ… pÄ™tlÄ™ aplikacji. |
| `void poll()` | Przetwarza zdarzenia logiki i dÄąĹźwiÄ™ku. |
| `void pollGraphics()` | Przetwarza zdarzenia okna i grafiki. |
| `void close()` | ObsÄąâ€šuguje zdarzenie zamkniÄ™cia okna. |
| `bool willRepaint()` | Zwraca `true`, jeÄąâ€şli zaplanowano przemalowanie ekranu. |
| `void repaint()` | Wymusza przemalowanie ekranu w nastÄ™pnej klatce. |
| `void setMaxFps(int maxFps)` | Ustawia maksymalnÄ… liczbÄ™ klatek na sekundÄ™. |
| `int getMaxFps()` | Zwraca ustawiony limit FPS. |
| `int getFps()` | Zwraca aktualny FPS renderowania. |
| `int getGraphicsFps()` | Zwraca FPS wÄ…tku graficznego. |
| `int getProcessingFps()` | Zwraca FPS wÄ…tku logiki. |
| `bool isOnInputEvent()` | Zwraca `true`, jeÄąâ€şli aplikacja jest w trakcie przetwarzania zdarzenia wejÄąâ€şciowego. |
| `int getIteration()` | Zwraca licznik iteracji gÄąâ€šĂłwnej pÄ™tli. |
| `void doScreenshot(...)` | Robi zrzut caÄąâ€šego ekranu. |
| `void scaleUp()` / `scaleDown()` / `scale()` | ZarzÄ…dzajÄ… skalowaniem interfejsu. |
| `void setSmooth(bool value)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza wygÄąâ€šadzanie dla bufora ramki mapy. |
| `void doMapScreenshot(...)` | Robi zrzut ekranu samej mapy gry. |
## Metody chronione

-   `void resize(const Size& size)`: ObsÄąâ€šuguje zdarzenie zmiany rozmiaru okna.
-   `void inputEvent(InputEvent event)`: Otrzymuje i przekazuje zdarzenia wejÄąâ€şciowe.
## Zmienne prywatne

-   `m_iteration`: Licznik klatek.
-   `m_scaling`, `m_lastScaling`: Aktualne i poprzednie skalowanie UI.
-   `m_maxFps`: Maksymalny limit FPS.
-   `m_onInputEvent`: Flaga aktywna podczas obsÄąâ€šugi zdarzenia wejÄąâ€şciowego.
-   `m_mustRepaint`: Flaga wymuszajÄ…ca przemalowanie.
-   `m_framebuffer`, `m_mapFramebuffer`: Bufory ramki do renderowania poza ekranem (off-screen rendering).
-   `m_graphicsFrames`, `m_processingFrames`: Liczniki klatek dla wÄ…tku graficznego i logiki.
-   `m_windowPollTimer`: Timer do ograniczania czÄ™stotliwoÄąâ€şci odpytywania okna.
## Zmienne globalne

-   `g_app`: Globalna instancja `GraphicalApplication`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/application.h`: Klasa bazowa.
-   `framework/graphics/declarations.h`: Deklaracje typĂłw graficznych (np. `FrameBufferPtr`).
-   `framework/core/inputevent.h`: Struktura `InputEvent`.
-   `framework/core/adaptiverenderer.h`: UÄąÄ˝ywa `AdaptiveRenderer` do dynamicznego dostosowywania wydajnoÄąâ€şci.
-   `framework/util/framecounter.h`: UÄąÄ˝ywa `FrameCounter` do Äąâ€şledzenia FPS.

---
# Ä‘Ĺşâ€śâ€ž logger.h
## Opis ogĂłlny

Plik `logger.h` deklaruje klasÄ™ `Logger`, ktĂłra implementuje system logowania dla caÄąâ€šej aplikacji. Jest to singleton (`g_logger`) zapewniajÄ…cy scentralizowany i bezpieczny wÄ…tkowo mechanizm do zapisywania komunikatĂłw o rĂłÄąÄ˝nym poziomie waÄąÄ˝noÄąâ€şci (debug, info, warning, error, fatal).
## Struktura `LogMessage`

Prosta struktura przechowujÄ…ca pojedynczÄ… wiadomoÄąâ€şÄ‡ logu.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `level` | `Fw::LogLevel` | Poziom waÄąÄ˝noÄąâ€şci wiadomoÄąâ€şci. |
| `message`| `std::string` | TreÄąâ€şÄ‡ wiadomoÄąâ€şci. |
| `when` | `std::size_t` | Czas (timestamp) utworzenia wiadomoÄąâ€şci. |
## Klasa `Logger`
## Opis semantyczny
`Logger` umoÄąÄ˝liwia logowanie komunikatĂłw do standardowego wyjÄąâ€şcia (konsola), opcjonalnego pliku oraz przekazywanie ich do zarejestrowanego `callbacka` (np. w celu wyÄąâ€şwietlenia w interfejsie uÄąÄ˝ytkownika). Przechowuje rĂłwnieÄąÄ˝ historiÄ™ ostatnich `MAX_LOG_HISTORY` wiadomoÄąâ€şci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void log(...)` | GÄąâ€šĂłwna metoda logujÄ…ca wiadomoÄąâ€şÄ‡ z okreÄąâ€şlonym poziomem. |
| `void logFunc(...)` | Loguje wiadomoÄąâ€şÄ‡ wraz z informacjÄ… o funkcji, z ktĂłrej zostaÄąâ€ša wywoÄąâ€šana (`__PRETTY_FUNCTION__`). |
| `void debug(..)` | SkrĂłt do `log(Fw::LogDebug, ...)`. |
| `void info(...)` | SkrĂłt do `log(Fw::LogInfo, ...)`. |
| `void warning(...)` | SkrĂłt do `log(Fw::LogWarning, ...)`. |
| `void error(...)` | SkrĂłt do `log(Fw::LogError, ...)`. |
| `void fatal(...)` | SkrĂłt do `log(Fw::LogFatal, ...)`, ktĂłry dodatkowo powoduje zamkniÄ™cie aplikacji. |
| `void fireOldMessages()` | WywoÄąâ€šuje `callback` `m_onLog` dla wszystkich historycznych wiadomoÄąâ€şci. |
| `void setLogFile(...)` | Ustawia plik, do ktĂłrego bÄ™dÄ… zapisywane logi. |
| `void setOnLog(...)` | Rejestruje funkcjÄ™ zwrotnÄ…, ktĂłra bÄ™dzie wywoÄąâ€šywana dla kaÄąÄ˝dej nowej wiadomoÄąâ€şci. |
| `std::string getLastLog()` | Zwraca ostatnio zalogowanÄ… wiadomoÄąâ€şÄ‡. |
| `void setTestingMode()` | Ustawia tryb testowy, w ktĂłrym bÄąâ€šÄ™dy (`LogError`) dziaÄąâ€šajÄ… jak bÄąâ€šÄ™dy krytyczne (`LogFatal`). |
## Zmienne prywatne

-   `m_logMessages`: Lista ostatnich wiadomoÄąâ€şci.
-   `m_onLog`: WskaÄąĹźnik na funkcjÄ™ zwrotnÄ….
-   `m_outFile`: StrumieÄąâ€ž pliku do zapisu logĂłw.
-   `m_mutex`: Mutex rekurencyjny zapewniajÄ…cy bezpieczeÄąâ€žstwo wÄ…tkowe.
-   `m_lastLog`: Przechowuje ostatniÄ… wiadomoÄąâ€şÄ‡.
-   `m_testingMode`: Flaga trybu testowego.
## Makra pomocnicze

Plik definiuje makra uÄąâ€šatwiajÄ…ce logowanie z dodatkowymi informacjami o kontekÄąâ€şcie.

-   `trace()`: Loguje nazwÄ™ bieÄąÄ˝Ä…cej funkcji.
-   `traceDebug(a)`, `traceInfo(a)`, ...: LogujÄ… wiadomoÄąâ€şÄ‡ `a` wraz z nazwÄ… funkcji i Äąâ€şladem stosu.
-   `logTraceCounter()`: Loguje licznik wywoÄąâ€šaÄąâ€ž co sekundÄ™.
-   `logTraceFrameCounter()`: Loguje licznik wywoÄąâ€šaÄąâ€ž co klatkÄ™.
## Zmienne globalne

-   `g_logger`: Globalna instancja `Logger`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/stdext/thread.h`: Zawiera `<mutex>` do synchronizacji.
-   `<fstream>`: Do obsÄąâ€šugi zapisu do pliku.
-   Jest uÄąÄ˝ywany w caÄąâ€šym projekcie do raportowania stanu, bÄąâ€šÄ™dĂłw i informacji debugowania.

---
# Ä‘Ĺşâ€śâ€ž module.cpp
## Opis ogĂłlny

Plik `module.cpp` zawiera implementacjÄ™ klasy `Module`, ktĂłra reprezentuje pojedynczy, Äąâ€šadowalny moduÄąâ€š funkcjonalnoÄąâ€şci w aplikacji. ModuÄąâ€šy sÄ… podstawÄ… architektury wtyczek, pozwalajÄ…c na dynamiczne Äąâ€šadowanie, odÄąâ€šadowywanie i ponowne Äąâ€šadowanie kodu (gÄąâ€šĂłwnie skryptĂłw Lua) w trakcie dziaÄąâ€šania programu.
## Klasa `Module`
## `Module::Module(const std::string& name)`

Konstruktor. Ustawia nazwÄ™ moduÄąâ€šu i tworzy dla niego nowe, odizolowane Äąâ€şrodowisko Lua (piaskownicÄ™ - sandbox) za pomocÄ… `g_lua.newSandboxEnv()`.
## `bool Module::load()`
## Opis semantyczny
GÄąâ€šĂłwna metoda Äąâ€šadujÄ…ca moduÄąâ€š. Jest odpowiedzialna za sprawdzenie i zaÄąâ€šadowanie zaleÄąÄ˝noÄąâ€şci, a nastÄ™pnie wykonanie skryptĂłw moduÄąâ€šu.
## DziaÄąâ€šanie
1.  Sprawdza, czy moduÄąâ€š nie jest juÄąÄ˝ zaÄąâ€šadowany.
2.  Definiuje `errorHandler` do obsÄąâ€šugi bÄąâ€šÄ™dĂłw Äąâ€šadowania.
3.  Dodaje Äąâ€şrodowisko moduÄąâ€šu do `package.loaded` w Lua, aby `require` dziaÄąâ€šaÄąâ€šo poprawnie.
4.  Iteruje po zaleÄąÄ˝noÄąâ€şciach (`m_dependencies`):
    -   Sprawdza, czy moduÄąâ€š nie zaleÄąÄ˝y sam od siebie.
    -   Sprawdza, czy zaleÄąÄ˝noÄąâ€şÄ‡ istnieje.
    -   Sprawdza, czy nie ma zaleÄąÄ˝noÄąâ€şci cyklicznych.
    -   JeÄąâ€şli zaleÄąÄ˝noÄąâ€şÄ‡ nie jest zaÄąâ€šadowana, prĂłbuje jÄ… zaÄąâ€šadowaÄ‡.
5.  JeÄąâ€şli moduÄąâ€š jest w piaskownicy (`m_sandboxed`), ustawia jego Äąâ€şrodowisko jako globalne w Lua.
6.  Wykonuje wszystkie skrypty z listy `m_scripts`.
7.  Wykonuje skrypt z `m_onLoadFunc`, jeÄąâ€şli jest zdefiniowany.
8.  JeÄąâ€şli wystÄ…piÄąâ€š bÄąâ€šÄ…d, wywoÄąâ€šuje `errorHandler` i zwraca `false`.
9.  Przywraca globalne Äąâ€şrodowisko Lua, jeÄąâ€şli byÄąâ€šo zmienione.
10. Ustawia flagÄ™ `m_loaded` na `true` i aktualizuje kolejnoÄąâ€şÄ‡ Äąâ€šadowania moduÄąâ€šĂłw.
11. ÄąÂaduje moduÄąâ€šy z listy `m_loadLaterModules`.
## `void Module::unload()`
## Opis semantyczny
OdÄąâ€šadowuje moduÄąâ€š, wykonujÄ…c jego skrypt `onUnload` i czyszczÄ…c jego Äąâ€şrodowisko Lua.
## DziaÄąâ€šanie
1.  Sprawdza, czy moduÄąâ€š jest zaÄąâ€šadowany.
2.  JeÄąâ€şli tak, wykonuje skrypt `onUnload` (`m_onUnloadFunc`).
3.  CzyÄąâ€şci caÄąâ€šÄ… tabelÄ™ Äąâ€şrodowiska Lua moduÄąâ€šu, aby zwolniÄ‡ wszystkie referencje.
4.  Usuwa moduÄąâ€š z `package.loaded` w Lua.
5.  Ustawia flagÄ™ `m_loaded` na `false`.
## `bool Module::reload()`

OdÄąâ€šadowuje i ponownie Äąâ€šaduje moduÄąâ€š.
## `bool Module::isDependent()`

Sprawdza, czy jakikolwiek inny zaÄąâ€šadowany moduÄąâ€š zaleÄąÄ˝y od tego moduÄąâ€šu. Jest to uÄąÄ˝ywane do okreÄąâ€şlenia, czy moduÄąâ€š moÄąÄ˝na bezpiecznie odÄąâ€šadowaÄ‡.
## `bool Module::hasDependency(const std::string& name, bool recursive)`

Sprawdza, czy moduÄąâ€š ma zaleÄąÄ˝noÄąâ€şÄ‡ o podanej nazwie. Opcja `recursive` pozwala na sprawdzanie zaleÄąÄ˝noÄąâ€şci poÄąâ€şrednich.
## `int Module::getSandbox(LuaInterface* lua)`

Zwraca na stos Lua tabelÄ™ Äąâ€şrodowiska (piaskownicÄ™) tego moduÄąâ€šu.
## `void Module::discover(const OTMLNodePtr& moduleNode)`

Parsuje wÄ™zeÄąâ€š OTML (z pliku `.otmod`) i inicjalizuje pola moduÄąâ€šu, takie jak opis, autor, wersja, zaleÄąÄ˝noÄąâ€şci, lista skryptĂłw, oraz skrypty `onLoad` i `onUnload`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/module.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/modulemanager.h`: WspĂłÄąâ€špracuje z `ModuleManager` do zarzÄ…dzania zaleÄąÄ˝noÄąâ€şciami i kolejnoÄąâ€şciÄ… Äąâ€šadowania.
-   `framework/core/resourcemanager.h`: UÄąÄ˝ywany do rozwiÄ…zywania Äąâ€şcieÄąÄ˝ek do skryptĂłw.
-   `framework/otml/otml.h`: UÄąÄ˝ywa `OTMLNode` do odczytu metadanych moduÄąâ€šu.
-   `framework/luaengine/luainterface.h`: Intensywnie korzysta z `g_lua` do zarzÄ…dzania Äąâ€şrodowiskiem i wykonywania skryptĂłw.

---
# Ä‘Ĺşâ€śâ€ž modulemanager.cpp
## Opis ogĂłlny

Plik `modulemanager.cpp` zawiera implementacjÄ™ klasy `ModuleManager`, ktĂłra jest singletonem (`g_modules`) odpowiedzialnym za zarzÄ…dzanie wszystkimi moduÄąâ€šami w aplikacji. Odpowiada za ich odkrywanie, Äąâ€šadowanie, odÄąâ€šadowywanie i ponowne Äąâ€šadowanie, a takÄąÄ˝e za zarzÄ…dzanie zaleÄąÄ˝noÄąâ€şciami miÄ™dzy nimi.
## Zmienne globalne
## `g_modules`

Globalna instancja `ModuleManager`.

`$fenceInfo
ModuleManager g_modules;
```
## Klasa `ModuleManager`
## `void ModuleManager::clear()`

CzyÄąâ€şci wszystkie dane menedÄąÄ˝era, usuwajÄ…c listÄ™ moduÄąâ€šĂłw i moduÄąâ€šĂłw do automatycznego Äąâ€šadowania.
## `void ModuleManager::discoverModules()`
## Opis semantyczny
Przeszukuje wirtualny system plikĂłw (katalogi `/modules` i `/mods`) w poszukiwaniu plikĂłw `.otmod`, parsuje je i tworzy obiekty `Module` dla kaÄąÄ˝dego znalezionego moduÄąâ€šu. ModuÄąâ€šy oznaczone jako `autoload` sÄ… dodawane do specjalnej listy.
## `void ModuleManager::autoLoadModules(int maxPriority)`

ÄąÂaduje wszystkie moduÄąâ€šy z listy `m_autoLoadModules`, ktĂłrych priorytet jest mniejszy lub rĂłwny `maxPriority`. ModuÄąâ€šy sÄ… Äąâ€šadowane w kolejnoÄąâ€şci rosnÄ…cego priorytetu.
## `ModulePtr ModuleManager::discoverModule(const std::string& moduleFile)`

Parsuje pojedynczy plik `.otmod`, tworzy lub aktualizuje obiekt `Module` i dodaje go do listy `m_modules`.
## `void ModuleManager::ensureModuleLoaded(const std::string& moduleName)`

Sprawdza, czy moduÄąâ€š o podanej nazwie jest zaÄąâ€šadowany. JeÄąâ€şli nie, prĂłbuje go zaÄąâ€šadowaÄ‡. JeÄąâ€şli Äąâ€šadowanie siÄ™ nie powiedzie, aplikacja jest zamykana z bÄąâ€šÄ™dem krytycznym.
## `void ModuleManager::unloadModules()`

OdÄąâ€šadowuje wszystkie zaÄąâ€šadowane moduÄąâ€šy. UÄąÄ˝ywa kopii listy moduÄąâ€šĂłw, aby uniknÄ…Ä‡ problemĂłw z iteratorami podczas usuwania.
## `void ModuleManager::reloadModules()`
## Opis semantyczny
Implementuje mechanizm "hot-reloading" moduÄąâ€šĂłw.
## DziaÄąâ€šanie
1.  Tworzy listÄ™ moduÄąâ€šĂłw do ponownego zaÄąâ€šadowania (`toLoadList`).
2.  W pÄ™tli (do 10 prĂłb) prĂłbuje odÄąâ€šadowaÄ‡ wszystkie moduÄąâ€šy, ktĂłre mogÄ… byÄ‡ odÄąâ€šadowane (`canUnload()`). ModuÄąâ€šy sÄ… odÄąâ€šadowywane w odwrotnej kolejnoÄąâ€şci zaleÄąÄ˝noÄąâ€şci.
3.  Po odÄąâ€šadowaniu, Äąâ€šaduje ponownie moduÄąâ€šy z `toLoadList`.
## `ModulePtr ModuleManager::getModule(const std::string& moduleName)`

Wyszukuje i zwraca wskaÄąĹźnik do moduÄąâ€šu o podanej nazwie.
## `void ModuleManager::updateModuleLoadOrder(ModulePtr module)`

Aktualizuje wewnÄ™trznÄ… listÄ™ moduÄąâ€šĂłw (`m_modules`), aby zaÄąâ€šadowane moduÄąâ€šy znajdowaÄąâ€šy siÄ™ na jej poczÄ…tku. Zapewnia to poprawnÄ… kolejnoÄąâ€şÄ‡ odÄąâ€šadowywania (odwrotnÄ… do Äąâ€šadowania).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/modulemanager.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/resourcemanager.h`: UÄąÄ˝ywany do przeszukiwania katalogĂłw z moduÄąâ€šami.
-   `framework/otml/otml.h`: Do parsowania plikĂłw `.otmod`.
-   `framework/core/application.h`: Do obsÄąâ€šugi bÄąâ€šÄ™dĂłw krytycznych.
-   Jest centralnym elementem architektury wtyczek i Äąâ€şciÄąâ€şle wspĂłÄąâ€špracuje z klasÄ… `Module`.

---
# Ä‘Ĺşâ€śâ€ž logger.cpp
## Opis ogĂłlny

Plik `logger.cpp` zawiera implementacjÄ™ klasy `Logger`, ktĂłra jest odpowiedzialna za system logowania w aplikacji. Zapewnia mechanizmy do zapisywania komunikatĂłw o rĂłÄąÄ˝nym poziomie waÄąÄ˝noÄąâ€şci do konsoli, pliku oraz przekazywania ich do zarejestrowanych funkcji zwrotnych (callbackĂłw).
## Zmienne globalne
## `g_logger`

Globalna, jedyna instancja klasy `Logger`.

`$fenceInfo
Logger g_logger;
```
## Funkcje globalne
## `void fatalError(const char* error, const char* file, int line)`

Funkcja wywoÄąâ€šywana przez makro `VALIDATE`. Loguje bÄąâ€šÄ…d krytyczny za pomocÄ… `g_logger.fatal`, zawierajÄ…cy komunikat, plik i numer linii, a nastÄ™pnie przerywa dziaÄąâ€šanie aplikacji.
## Klasa `Logger`
## `void Logger::log(Fw::LogLevel level, const std::string& message)`
## Opis semantyczny
GÄąâ€šĂłwna, prywatna metoda logujÄ…ca. Jest bezpieczna wÄ…tkowo dziÄ™ki uÄąÄ˝yciu `std::recursive_mutex`.
## DziaÄąâ€šanie
1.  Blokuje mutex, aby zapewniÄ‡ wyÄąâ€šÄ…czny dostÄ™p.
2.  W trybie `NDEBUG` (wydajnoÄąâ€şciowym) ignoruje wiadomoÄąâ€şci o poziomie `LogDebug`.
3.  Dodaje odpowiedni prefiks do wiadomoÄąâ€şci (np. "WARNING: ", "ERROR: ").
4.  Wypisuje sformatowanÄ… wiadomoÄąâ€şÄ‡ na standardowe wyjÄąâ€şcie (`std::cout`) lub `__android_log_print` na Androidzie.
5.  JeÄąâ€şli ustawiono plik logu, zapisuje wiadomoÄąâ€şÄ‡ do pliku.
6.  Dodaje wiadomoÄąâ€şÄ‡ do wewnÄ™trznej historii `m_logMessages`.
7.  JeÄąâ€şli zarejestrowano `callback` (`m_onLog`), dodaje zdarzenie do `g_dispatcher`, ktĂłre wywoÄąâ€ša ten `callback` w gÄąâ€šĂłwnym wÄ…tku.
8.  JeÄąâ€şli poziom to `LogFatal` (lub `LogError` w trybie testowym), wyÄąâ€şwietla okno bÄąâ€šÄ™du (w wersji graficznej) i natychmiast koÄąâ€žczy aplikacjÄ™.
## `void Logger::logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction)`

Metoda pomocnicza, ktĂłra wzbogaca wiadomoÄąâ€şÄ‡ o informacje o funkcji, z ktĂłrej zostaÄąâ€ša wywoÄąâ€šana, oraz o Äąâ€şlad stosu (traceback) z Lua i C++. UÄąÄ˝ywana przez makra takie jak `traceError`.
## `void Logger::fireOldMessages()`

WywoÄąâ€šuje `callback` `m_onLog` dla wszystkich wiadomoÄąâ€şci, ktĂłre zostaÄąâ€šy zalogowane przed jego zarejestrowaniem. Przydatne do wyÄąâ€şwietlania wczesnych logĂłw w UI, gdy UI jest juÄąÄ˝ gotowe.
## `void Logger::setLogFile(const std::string& file)`

Otwiera podany plik do zapisu logĂłw. Przed otwarciem do dopisywania, odczytuje ostatnie 100 KB z istniejÄ…cego pliku do `m_lastLog`, aby moÄąÄ˝na byÄąâ€šo przejrzeÄ‡ logi z poprzedniej sesji.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/logger.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/eventdispatcher.h`: UÄąÄ˝ywa `g_dispatcher` do bezpiecznego wywoÄąâ€šywania `callbackĂłw` w gÄąâ€šĂłwnym wÄ…tku.
-   `framework/core/resourcemanager.h`: Potencjalnie uÄąÄ˝ywany do rozwiÄ…zywania Äąâ€şcieÄąÄ˝ek do plikĂłw logĂłw.
-   `framework/core/graphicalapplication.h`: W wersji graficznej, `g_window` jest uÄąÄ˝ywane do wyÄąâ€şwietlania okna bÄąâ€šÄ™du krytycznego.
-   `framework/platform/platform.h`: UÄąÄ˝ywa `g_platform` do generowania Äąâ€şladu stosu C++.
-   `framework/luaengine/luainterface.h`: UÄąÄ˝ywa `g_lua` do generowania Äąâ€şladu stosu Lua.

---
# Ä‘Ĺşâ€śâ€ž module.h
## Opis ogĂłlny

Plik `module.h` deklaruje klasÄ™ `Module`, ktĂłra jest podstawowym elementem systemu modularnoÄąâ€şci aplikacji. KaÄąÄ˝dy moduÄąâ€š reprezentuje logicznie oddzielonÄ… czÄ™Äąâ€şÄ‡ funkcjonalnoÄąâ€şci (np. interfejs, mini-mapa, bot), ktĂłra moÄąÄ˝e byÄ‡ dynamicznie Äąâ€šadowana i odÄąâ€šadowywana.
## Klasa `Module`
## Opis semantyczny
`Module` enkapsuluje zestaw skryptĂłw Lua, metadane (nazwa, autor, wersja), zaleÄąÄ˝noÄąâ€şci od innych moduÄąâ€šĂłw oraz wÄąâ€šasne, izolowane Äąâ€şrodowisko Lua (piaskownicÄ™ - sandbox). Dziedziczy po `LuaObject`, dziÄ™ki czemu moÄąÄ˝e byÄ‡ zarzÄ…dzany z poziomu skryptĂłw Lua.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Module(const std::string& name)` | Konstruktor. |
| `bool load()` | ÄąÂaduje moduÄąâ€š, wykonujÄ…c jego skrypty i zaleÄąÄ˝noÄąâ€şci. |
| `void unload()` | OdÄąâ€šadowuje moduÄąâ€š, wykonujÄ…c skrypt `onUnload`. |
| `bool reload()` | Ponownie Äąâ€šaduje moduÄąâ€š. |
| `bool canUnload()` | Zwraca `true`, jeÄąâ€şli moduÄąâ€š jest przeÄąâ€šadowywalny i ÄąÄ˝aden inny moduÄąâ€š od niego nie zaleÄąÄ˝y. |
| `bool canReload()` | Zwraca `true`, jeÄąâ€şli moduÄąâ€š jest przeÄąâ€šadowywalny i nie ma zaleÄąÄ˝noÄąâ€şci. |
| `bool isLoaded()` | Zwraca `true`, jeÄąâ€şli moduÄąâ€š jest zaÄąâ€šadowany. |
| `bool isReloadable()` | Zwraca `true`, jeÄąâ€şli moduÄąâ€š moÄąÄ˝na przeÄąâ€šadowaÄ‡. |
| `bool isDependent()` | Sprawdza, czy inny zaÄąâ€šadowany moduÄąâ€š zaleÄąÄ˝y od tego moduÄąâ€šu. |
| `bool isSandboxed()` | Zwraca `true`, jeÄąâ€şli moduÄąâ€š dziaÄąâ€ša w odizolowanym Äąâ€şrodowisku Lua. |
| `bool hasDependency(...)` | Sprawdza, czy moduÄąâ€š ma danÄ… zaleÄąÄ˝noÄąâ€şÄ‡ (opcjonalnie rekurencyjnie). |
| `int getSandbox(LuaInterface *lua)` | Umieszcza na stosie Lua tabelÄ™ Äąâ€şrodowiska tego moduÄąâ€šu. |
| `std::string getDescription()`, `getName()`, `getAuthor()`, `getWebsite()`, `getVersion()` | ZwracajÄ… metadane moduÄąâ€šu. |
| `bool isAutoLoad()` | Zwraca `true`, jeÄąâ€şli moduÄąâ€š powinien byÄ‡ Äąâ€šadowany automatycznie. |
| `int getAutoLoadPriority()` | Zwraca priorytet automatycznego Äąâ€šadowania. |
## Metody chronione

-   `void discover(const OTMLNodePtr& moduleNode)`: Metoda wywoÄąâ€šywana przez `ModuleManager` do wczytania metadanych moduÄąâ€šu z pliku `.otmod`.
## Zmienne prywatne

-   `m_loaded`, `m_autoLoad`, `m_reloadable`, `m_sandboxed`: Flagi stanu.
-   `m_autoLoadPriority`: Priorytet Äąâ€šadowania.
-   `m_sandboxEnv`: Referencja do Äąâ€şrodowiska Lua (piaskownicy).
-   `m_onLoadFunc`, `m_onUnloadFunc`: PrzechowujÄ… kod skryptĂłw `onLoad` i `onUnload`.
-   `m_name`, `m_description`, ...: Metadane moduÄąâ€šu.
-   `m_dependencies`, `m_scripts`, `m_loadLaterModules`: Listy zaleÄąÄ˝noÄąâ€şci i skryptĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/declarations.h`: Definicje wskaÄąĹźnikĂłw.
-   `framework/otml/declarations.h`: UÄąÄ˝ywa `OTMLNodePtr` do parsowania metadanych.
-   `framework/luaengine/luaobject.h`: Jest klasÄ… pochodnÄ… `LuaObject`.
-   Jest oznaczona jako `@bindclass`, co pozwala na interakcjÄ™ z obiektami `Module` z poziomu Lua.
-   Jest zarzÄ…dzana przez `ModuleManager`.

---
# Ä‘Ĺşâ€śâ€ž modulemanager.h
## Opis ogĂłlny

Plik `modulemanager.h` deklaruje klasÄ™ `ModuleManager`, ktĂłra jest singletonem (`g_modules`) odpowiedzialnym za zarzÄ…dzanie cyklem ÄąÄ˝ycia wszystkich moduÄąâ€šĂłw w aplikacji.
## Klasa `ModuleManager`
## Opis semantyczny
`ModuleManager` peÄąâ€šni rolÄ™ centralnego rejestru moduÄąâ€šĂłw. Odpowiada za ich odkrywanie (przez skanowanie katalogĂłw w poszukiwaniu plikĂłw `.otmod`), Äąâ€šadowanie w odpowiedniej kolejnoÄąâ€şci (z uwzglÄ™dnieniem zaleÄąÄ˝noÄąâ€şci i priorytetĂłw), a takÄąÄ˝e za ich odÄąâ€šadowywanie i ponowne Äąâ€šadowanie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void clear()` | CzyÄąâ€şci listÄ™ moduÄąâ€šĂłw. |
| `void discoverModules()` | Przeszukuje system plikĂłw w poszukiwaniu plikĂłw `.otmod` i tworzy dla nich obiekty `Module`. |
| `void autoLoadModules(int maxPriority)` | ÄąÂaduje wszystkie moduÄąâ€šy, ktĂłre majÄ… flagÄ™ `autoload` i priorytet nie wiÄ™kszy niÄąÄ˝ podany. |
| `ModulePtr discoverModule(...)` | Parsuje pojedynczy plik `.otmod` i tworzy lub aktualizuje obiekt `Module`. |
| `void ensureModuleLoaded(...)` | Upewnia siÄ™, ÄąÄ˝e dany moduÄąâ€š jest zaÄąâ€šadowany; jeÄąâ€şli nie, prĂłbuje go zaÄąâ€šadowaÄ‡, a w razie poraÄąÄ˝ki koÄąâ€žczy aplikacjÄ™. |
| `void unloadModules()` | OdÄąâ€šadowuje wszystkie zaÄąâ€šadowane moduÄąâ€šy. |
| `void reloadModules()` | PrĂłbuje odÄąâ€šadowaÄ‡ i ponownie zaÄąâ€šadowaÄ‡ wszystkie moduÄąâ€šy, ktĂłre na to pozwalajÄ…. |
| `ModulePtr getModule(...)` | Zwraca wskaÄąĹźnik do moduÄąâ€šu o podanej nazwie. |
| `std::deque<ModulePtr> getModules()` | Zwraca listÄ™ wszystkich odkrytych moduÄąâ€šĂłw. |
## Metody chronione

-   `void updateModuleLoadOrder(ModulePtr module)`: Aktualizuje wewnÄ™trznÄ… kolejkÄ™ moduÄąâ€šĂłw, aby zachowaÄ‡ poprawnÄ… kolejnoÄąâ€şÄ‡ Äąâ€šadowania/odÄąâ€šadowywania.
## Zmienne prywatne

-   `m_modules`: Kolejka (`std::deque`) wszystkich odkrytych moduÄąâ€šĂłw. ZaÄąâ€šadowane moduÄąâ€šy sÄ… na poczÄ…tku.
-   `m_autoLoadModules`: Mapa (`std::multimap`) przechowujÄ…ca moduÄąâ€šy do automatycznego zaÄąâ€šadowania, posortowane wedÄąâ€šug priorytetu.
## Zmienne globalne

-   `g_modules`: Globalna instancja `ModuleManager`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/module.h`: Definicja klasy `Module`, ktĂłrÄ… zarzÄ…dza `ModuleManager`.
-   Jest oznaczona jako `@bindsingleton g_modules`, co udostÄ™pnia jej API w skryptach Lua.
-   WspĂłÄąâ€špracuje z `ResourceManager` do przeszukiwania systemu plikĂłw i z `Application` do inicjalizacji i zamykania.

---
# Ä‘Ĺşâ€śâ€ž scheduledevent.cpp
## Opis ogĂłlny

Plik `scheduledevent.cpp` zawiera implementacjÄ™ klasy `ScheduledEvent`, ktĂłra reprezentuje zdarzenie zaplanowane do wykonania w przyszÄąâ€šoÄąâ€şci.
## Klasa `ScheduledEvent`
## `ScheduledEvent::ScheduledEvent(...)`

Konstruktor, ktĂłry dziedziczy po `Event` i dodatkowo inicjalizuje parametry zwiÄ…zane z czasem.

-   **Parametry**:
    -   `function`, `callback`, `botSafe`: Przekazywane do konstruktora klasy bazowej `Event`.
    -   `delay`: Czas w milisekundach, po ktĂłrym zdarzenie ma zostaÄ‡ wykonane po raz pierwszy.
    -   `maxCycles`: Maksymalna liczba wykonaÄąâ€ž. `0` oznacza nieskoÄąâ€žczonoÄąâ€şÄ‡.
-   **DziaÄąâ€šanie**:
    -   Oblicza czas pierwszego wykonania: `m_ticks = g_clock.millis() + delay`.
    -   Zapisuje opĂłÄąĹźnienie, maksymalnÄ… liczbÄ™ cykli i zeruje licznik wykonanych cykli.
## `void ScheduledEvent::execute()`
## Opis semantyczny
Wykonuje `callback` zdarzenia, jeÄąâ€şli warunki sÄ… speÄąâ€šnione.
## DziaÄąâ€šanie
1.  Sprawdza, czy zdarzenie nie jest anulowane, czy `callback` istnieje i czy nie przekroczono `maxCycles`.
2.  JeÄąâ€şli warunki sÄ… speÄąâ€šnione, wykonuje `callback` i ustawia `m_executed` na `true`. W przeciwieÄąâ€žstwie do `Event`, nie resetuje `callback`, poniewaÄąÄ˝ moÄąÄ˝e byÄ‡ on potrzebny w nastÄ™pnym cyklu.
3.  JeÄąâ€şli warunki nie sÄ… speÄąâ€šnione (np. zdarzenie jednorazowe zostaÄąâ€šo wykonane), resetuje `callback` do `nullptr`.
4.  Inkrementuje licznik `m_cyclesExecuted`.
## `bool ScheduledEvent::nextCycle()`
## Opis semantyczny
Przygotowuje zdarzenie do nastÄ™pnego cyklu. Jest wywoÄąâ€šywana przez `EventDispatcher` po wykonaniu zdarzenia.
## DziaÄąâ€šanie
1.  Sprawdza, czy zdarzenie powinno byÄ‡ wykonane ponownie (nieanulowane, nie przekroczono `maxCycles`).
2.  JeÄąâ€şli tak, przesuwa czas nastÄ™pnego wykonania o `m_delay`: `m_ticks += m_delay` i zwraca `true`.
3.  JeÄąâ€şli nie, resetuje `callback` do `nullptr` i zwraca `false`, co powoduje usuniÄ™cie zdarzenia z kolejki dyspozytora.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/scheduledevent.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/clock.h`: UÄąÄ˝ywa `g_clock.millis()` do pobierania bieÄąÄ˝Ä…cego czasu.
-   Jest tworzona i zarzÄ…dzana przez `EventDispatcher`.

---
# Ä‘Ĺşâ€śâ€ž resourcemanager.cpp
## Opis ogĂłlny

Plik `resourcemanager.cpp` zawiera implementacjÄ™ klasy `ResourceManager`, ktĂłra jest sercem systemu zarzÄ…dzania zasobami aplikacji. Implementuje ona logikÄ™ wyszukiwania, Äąâ€šadowania, odczytu i zapisu plikĂłw, abstrakcjonujÄ…c ÄąĹźrĂłdÄąâ€šo danych (dysk, archiwum, pamiÄ™Ä‡).
## Klasa `ResourceManager`
## `void ResourceManager::init(const char *argv0)`

Inicjalizuje bibliotekÄ™ PhysFS i ustala Äąâ€şcieÄąÄ˝kÄ™ do pliku wykonywalnego aplikacji na podstawie argumentu `argv0`.
## `bool ResourceManager::setupWriteDir(...)`

Konfiguruje katalog zapisu dla aplikacji, uÄąÄ˝ywajÄ…c `PHYSFS_getPrefDir`. Ten katalog jest zazwyczaj zlokalizowany w folderze danych uÄąÄ˝ytkownika (np. `%APPDATA%` na Windows, `~/.local/share` na Linux). Montuje ten katalog i ustawia go jako domyÄąâ€şlny katalog do zapisu.
## `bool ResourceManager::setup()`

Kluczowa metoda, ktĂłra prĂłbuje zlokalizowaÄ‡ i zamontowaÄ‡ gÄąâ€šĂłwny katalog roboczy aplikacji. Przeszukuje kilka potencjalnych lokalizacji w nastÄ™pujÄ…cej kolejnoÄąâ€şci:
1.  Katalogi na dysku (katalog zapisu, bieÄąÄ˝Ä…cy katalog, katalog bazowy).
2.  Archiwum `data.zip` w tych samych lokalizacjach.
3.  Dane wbudowane w sam plik wykonywalny (`loadDataFromSelf`).
## `std::string ResourceManager::getCompactName()`

Metoda prĂłbujÄ…ca odgadnÄ…Ä‡ "skrĂłconÄ… nazwÄ™" aplikacji na podstawie zawartoÄąâ€şci pliku `init.lua`, ktĂłry powinien zawieraÄ‡ definicjÄ™ `APP_NAME`. Jest to uÄąÄ˝ywane m.in. do tworzenia katalogu zapisu.
## `bool ResourceManager::loadDataFromSelf(...)`

Przeszukuje plik binarny aplikacji w poszukiwaniu sygnatury archiwum ZIP (`PK..`). JeÄąâ€şli znajdzie, traktuje resztÄ™ pliku jako archiwum i montuje je w pamiÄ™ci za pomocÄ… `PHYSFS_mountMemory`.
## `std::string ResourceManager::readFileContents(...)`

Odczytuje zawartoÄąâ€şÄ‡ pliku. Po odczytaniu surowych bajtĂłw, prĂłbuje je zdeszyfrowaÄ‡ za pomocÄ… `decryptBuffer`. ObsÄąâ€šuguje rĂłwnieÄąÄ˝ specjalny wirtualny katalog `/downloads` do odczytu plikĂłw pobranych przez `Http`.
## `bool ResourceManager::decryptBuffer(std::string& buffer)`

Deszyfruje bufor, jeÄąâ€şli jest on zaszyfrowany (rozpoznaje po nagÄąâ€šĂłwku "ENC3"). Proces deszyfracji obejmuje:
1.  Odczytanie metadanych (klucz, rozmiary, suma kontrolna).
2.  DeszyfracjÄ™ za pomocÄ… algorytmu `bdecrypt` (odmiana TEA/XTEA).
3.  DekompresjÄ™ za pomocÄ… ZLIB.
4.  WeryfikacjÄ™ sumy kontrolnej Adler-32.
## `bool ResourceManager::encryptBuffer(...)`

Szyfruje bufor, wykonujÄ…c operacje odwrotne do `decryptBuffer`: kompresja, szyfrowanie i dodanie nagÄąâ€šĂłwka. DostÄ™pne tylko z flagÄ… `WITH_ENCRYPTION`.
## `std::string ResourceManager::resolvePath(std::string path)`

Konwertuje Äąâ€şcieÄąÄ˝kÄ™ wzglÄ™dnÄ… na Äąâ€şcieÄąÄ˝kÄ™ absolutnÄ… w wirtualnym systemie plikĂłw. ObsÄąâ€šuguje Äąâ€şcieÄąÄ˝ki wzglÄ™dne do bieÄąÄ˝Ä…cego skryptu Lua oraz specjalne Äąâ€şcieÄąÄ˝ki dla layoutĂłw UI (np. `/layouts/nazwa_layoutu/...`).
## `updateData(...)` i `updateExecutable(...)`

Metody sÄąâ€šuÄąÄ˝Ä…ce do aktualizacji klienta. `updateData` przebudowuje archiwum `data.zip` na podstawie pobranych plikĂłw, a `updateExecutable` zastÄ™puje plik binarny nowÄ… wersjÄ….
## `createArchive(...)` i `decompressArchive(...)`

Metody pomocnicze do tworzenia i rozpakowywania archiwĂłw ZIP w pamiÄ™ci przy uÄąÄ˝yciu biblioteki `libzip`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/resourcemanager.h`: Plik nagÄąâ€šĂłwkowy.
-   **PhysFS**: Podstawowa zaleÄąÄ˝noÄąâ€şÄ‡ do obsÄąâ€šugi wirtualnego systemu plikĂłw.
-   **ZLIB, LibZip**: Do obsÄąâ€šugi kompresji i archiwĂłw.
-   `framework/platform/platform.h`: Do operacji specyficznych dla systemu, jak pobieranie bieÄąÄ˝Ä…cego katalogu.
-   `framework/util/crypt.h`: Do szyfrowania, deszyfrowania i obliczania sum kontrolnych.
-   `framework/http/http.h`: Do obsÄąâ€šugi wirtualnego katalogu `/downloads`.
-   `boost/process.hpp`: Do uruchamiania nowszej wersji klienta.

---
# Ä‘Ĺşâ€śâ€ž scheduledevent.h
## Opis ogĂłlny

Plik `scheduledevent.h` deklaruje klasÄ™ `ScheduledEvent`, ktĂłra rozszerza funkcjonalnoÄąâ€şÄ‡ `Event`, dodajÄ…c moÄąÄ˝liwoÄąâ€şÄ‡ planowania wykonania w czasie, cyklicznoÄąâ€şci oraz obsÄąâ€šugi opĂłÄąĹźnieÄąâ€ž.
## Klasa `ScheduledEvent`
## Opis semantyczny
`ScheduledEvent` to zdarzenie, ktĂłre nie jest wykonywane natychmiast, lecz po upÄąâ€šywie okreÄąâ€şlonego czasu (`delay`). MoÄąÄ˝e byÄ‡ jednorazowe lub cykliczne (`maxCycles`). Jest zarzÄ…dzane przez `EventDispatcher` w kolejce priorytetowej, gdzie priorytetem jest czas wykonania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `ScheduledEvent(...)` | Konstruktor, ustawia parametry czasowe zdarzenia. |
| `void execute()` | Wykonuje `callback` i inkrementuje licznik wykonanych cykli. |
| `bool nextCycle()` | Przygotowuje zdarzenie do nastÄ™pnego cyklu, aktualizujÄ…c czas wykonania. Zwraca `false`, jeÄąâ€şli zdarzenie nie powinno byÄ‡ ponownie wykonane. |
| `int ticks()` | Zwraca absolutny czas (w tickach), w ktĂłrym zdarzenie ma zostaÄ‡ wykonane. |
| `int remainingTicks()` | Zwraca czas pozostaÄąâ€šy do wykonania zdarzenia. |
| `int delay()` | Zwraca opĂłÄąĹźnienie miÄ™dzy cyklami. |
| `int cyclesExecuted()` | Zwraca liczbÄ™ dotychczasowych wykonaÄąâ€ž. |
| `int maxCycles()` | Zwraca maksymalnÄ… liczbÄ™ wykonaÄąâ€ž (0 dla nieskoÄąâ€žczonoÄąâ€şci). |
## Zmienne prywatne

-   `m_ticks`: Czas (w tickach systemowych), w ktĂłrym ma nastÄ…piÄ‡ nastÄ™pne wykonanie.
-   `m_delay`: OpĂłÄąĹźnienie miÄ™dzy kolejnymi wykonaniami.
-   `m_maxCycles`: Maksymalna liczba wykonaÄąâ€ž.
-   `m_cyclesExecuted`: Licznik wykonanych cykli.
## Struktura `lessScheduledEvent`

Funktor (obiekt funkcyjny) uÄąÄ˝ywany przez `std::priority_queue` w `EventDispatcher` do sortowania zdarzeÄąâ€ž. Zapewnia, ÄąÄ˝e zdarzenia z najwczeÄąâ€şniejszym czasem wykonania majÄ… najwyÄąÄ˝szy priorytet.

`$fenceInfo
struct lessScheduledEvent {
    bool operator()(const ScheduledEventPtr& a, const ScheduledEventPtr& b) {
        return  b->ticks() < a->ticks();
}
};
```
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/core/event.h`: Klasa bazowa `Event`.
-   `framework/core/clock.h`: UÄąÄ˝ywa `g_clock` do pobierania bieÄąÄ˝Ä…cego czasu.
-   Jest tworzona przez `EventDispatcher` i zarzÄ…dzana w jego kolejce priorytetowej.
-   Oznaczona jako `@bindclass`, co pozwala na interakcjÄ™ z obiektami tego typu z poziomu Lua.

---
# Ä‘Ĺşâ€śâ€ž timer.cpp
## Opis ogĂłlny

Plik `timer.cpp` zawiera implementacjÄ™ prostych metod klasy `Timer`, ktĂłra sÄąâ€šuÄąÄ˝y do mierzenia upÄąâ€šywu czasu.
## Klasa `Timer`
## `void Timer::restart()`
## Opis semantyczny
Resetuje timer, ustawiajÄ…c jego punkt startowy na bieÄąÄ˝Ä…cy czas.
## DziaÄąâ€šanie
1.  Pobiera aktualny czas w milisekundach za pomocÄ… `g_clock.millis()`.
2.  Zapisuje tÄ™ wartoÄąâ€şÄ‡ do `m_startTicks`.
3.  Ustawia flagÄ™ `m_stopped` na `false`.
## `ticks_t Timer::ticksElapsed()`
## Opis semantyczny
Oblicza i zwraca czas, jaki upÄąâ€šynÄ…Äąâ€š od ostatniego zresetowania timera.
## DziaÄąâ€šanie
-   Zwraca rĂłÄąÄ˝nicÄ™ miÄ™dzy aktualnym czasem (`g_clock.millis()`) a zapisanym czasem startowym (`m_startTicks`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/timer.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   `framework/core/clock.h`: UÄąÄ˝ywa `g_clock` do pobierania bieÄąÄ˝Ä…cego czasu, co zapewnia spĂłjnoÄąâ€şÄ‡ z buforowanym czasem klatki.

---
# Ä‘Ĺşâ€śâ€ž timer.h
## Opis ogĂłlny

Plik `timer.h` deklaruje klasÄ™ `Timer`, ktĂłra jest prostym, ale uÄąÄ˝ytecznym narzÄ™dziem do mierzenia upÄąâ€šywajÄ…cego czasu. Jest to klasa pomocnicza, szeroko stosowana w caÄąâ€šym frameworku do obsÄąâ€šugi opĂłÄąĹźnieÄąâ€ž, animacji i synchronizacji.
## Klasa `Timer`
## Opis semantyczny
`Timer` dziaÄąâ€ša jak stoper. Po utworzeniu lub zresetowaniu (`restart()`) zapamiÄ™tuje punkt w czasie. NastÄ™pnie moÄąÄ˝na w dowolnym momencie sprawdziÄ‡, ile czasu upÄąâ€šynÄ™Äąâ€šo od tego punktu za pomocÄ… metod `ticksElapsed()` lub `timeElapsed()`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Timer()` | Konstruktor, ktĂłry natychmiast wywoÄąâ€šuje `restart()`. |
| `void restart()` | Resetuje timer, ustawiajÄ…c jego punkt startowy na bieÄąÄ˝Ä…cy czas. |
| `void stop()` | Zatrzymuje timer (ustawia flagÄ™ `m_stopped`). |
| `void adjust(ticks_t value)` | Przesuwa punkt startowy o podanÄ… wartoÄąâ€şÄ‡, efektywnie "dodajÄ…c" lub "odejmujÄ…c" czas. |
| `ticks_t startTicks()` | Zwraca punkt startowy timera w tickach. |
| `ticks_t ticksElapsed()` | Zwraca czas, jaki upÄąâ€šynÄ…Äąâ€š od startu, w milisekundach. |
| `float timeElapsed()` | Zwraca czas, jaki upÄąâ€šynÄ…Äąâ€š od startu, w sekundach. |
| `bool running()` | Zwraca `true`, jeÄąâ€şli timer nie zostaÄąâ€š zatrzymany. |
## Zmienne prywatne

-   `m_startTicks`: Czas (w tickach/milisekundach), w ktĂłrym timer zostaÄąâ€š uruchomiony/zresetowany.
-   `m_stopped`: Flaga wskazujÄ…ca, czy timer jest zatrzymany.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Zawiera podstawowe definicje, w tym `ticks_t`.
-   UÄąÄ˝ywa `g_clock` (poprzez `ticksElapsed`) do pomiaru czasu.
-   Jest wykorzystywana w wielu miejscach, np. w `UIWidget` do obsÄąâ€šugi podwĂłjnego klikniÄ™cia (`m_clickTimer`), w `PlatformWindow` do ograniczania czÄ™stotliwoÄąâ€şci sprawdzania klawiszy (`m_keyPressTimer`), oraz w animacjach.

---
# Ä‘Ĺşâ€śâ€ž consoleapplication.cpp
## Opis ogĂłlny

Plik `consoleapplication.cpp` zawiera implementacjÄ™ klasy `ConsoleApplication`, ktĂłra jest wersjÄ… aplikacji przeznaczonÄ… do dziaÄąâ€šania w trybie tekstowym, bez interfejsu graficznego. Jest ona uÄąÄ˝ywana, gdy projekt jest kompilowany bez flagi `FW_GRAPHICS`.
## Zmienne globalne
## `g_app`

Globalna instancja `ConsoleApplication`. Gdy framework jest kompilowany w trybie konsolowym, ta instancja staje siÄ™ gÄąâ€šĂłwnym obiektem aplikacji.

`$fenceInfo
ConsoleApplication g_app;
```
## Klasa `ConsoleApplication`
## `void ConsoleApplication::run()`
## Opis semantyczny
Implementuje gÄąâ€šĂłwnÄ… pÄ™tlÄ™ aplikacji konsolowej. W przeciwieÄąâ€žstwie do `GraphicalApplication`, jest to prosta pÄ™tla, ktĂłra regularnie przetwarza zdarzenia i usypia wÄ…tek, aby nie zuÄąÄ˝ywaÄ‡ 100% zasobĂłw procesora.
## DziaÄąâ€šanie
1.  Ustawia flagÄ™ `m_running` na `true`.
2.  Wykonuje pierwsze wywoÄąâ€šanie `poll()`, aby przetworzyÄ‡ ewentualne poczÄ…tkowe zdarzenia.
3.  Aktualizuje zegar (`g_clock.update()`).
4.  WywoÄąâ€šuje funkcjÄ™ `onRun` w globalnym skrypcie Lua (`g_app.onRun`).
5.  Wchodzi w pÄ™tlÄ™, ktĂłra trwa, dopĂłki flaga `m_stopping` nie zostanie ustawiona na `true`.
6.  W kaÄąÄ˝dej iteracji pÄ™tli:
    -   WywoÄąâ€šuje `poll()` do przetworzenia zdarzeÄąâ€ž (np. sieciowych, zaplanowanych).
    -   Usypia gÄąâ€šĂłwny wÄ…tek na 1 milisekundÄ™ (`stdext::millisleep(1)`).
    -   Aktualizuje zegar (`g_clock.update()`).
    -   Aktualizuje licznik klatek/iteracji (`m_frameCounter.update()`).
7.  Po wyjÄąâ€şciu z pÄ™tli, resetuje flagi `m_stopping` i `m_running`.

> **NOTE:** Pomimo braku grafiki, wciÄ…ÄąÄ˝ istnieje pojÄ™cie "klatki" lub iteracji, ktĂłre jest Äąâ€şledzone przez `m_frameCounter`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/consoleapplication.h`: Plik nagÄąâ€šĂłwkowy dla tej klasy.
-   `framework/core/clock.h`: UÄąÄ˝ywa `g_clock` do aktualizacji czasu w kaÄąÄ˝dej iteracji.
-   `framework/luaengine/luainterface.h`: UÄąÄ˝ywa `g_lua` do wywoÄąâ€šania `onRun`.
-   `framework/net/connection.h`: Metoda `poll()` wywoÄąâ€šuje m.in. `Connection::poll()`, wiÄ™c aplikacja konsolowa moÄąÄ˝e obsÄąâ€šugiwaÄ‡ sieÄ‡.

---
# Ä‘Ĺşâ€śâ€ž shaderprogram.h
## Opis ogĂłlny

Plik `shaderprogram.h` deklaruje klasÄ™ `ShaderProgram`, ktĂłra jest obiektowym opakowaniem na program shadera w OpenGL. ZarzÄ…dza ona kompilacjÄ…, linkowaniem i aktywacjÄ… shaderĂłw wierzchoÄąâ€škĂłw i fragmentĂłw.
## Klasa `ShaderProgram`
## Opis semantyczny
`ShaderProgram` agreguje obiekty `Shader` (reprezentujÄ…ce pojedyncze shadery, np. wierzchoÄąâ€škĂłw lub fragmentĂłw), linkuje je w jeden wykonywalny program, ktĂłry moÄąÄ˝e byÄ‡ uÄąÄ˝yty w potoku renderowania OpenGL, i dostarcza interfejs do ustawiania uniformĂłw i atrybutĂłw. Dziedziczy po `LuaObject`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `ShaderProgram(const std::string& name)` | Konstruktor, tworzy program shadera. |
| `static PainterShaderProgramPtr create(...)` | Statyczna metoda fabryczna do tworzenia `PainterShaderProgram`. |
| `bool addShader(...)` | Dodaje skompilowany obiekt `Shader` do programu. |
| `bool addShaderFromSourceCode(...)` | Tworzy, kompiluje i dodaje shader z kodu ÄąĹźrĂłdÄąâ€šowego. |
| `bool addShaderFromSourceFile(...)` | Tworzy, kompiluje i dodaje shader z pliku. |
| `void removeShader(...)` | Usuwa shader z programu. |
| `bool link()` | Linkuje wszystkie dodane shadery w jeden program. |
| `bool bind()` | Aktywuje ten program shadera w kontekÄąâ€şcie OpenGL. |
| `static void release()` | Deaktywuje jakikolwiek aktywny program shadera. |
| `std::string log()` | Zwraca logi z procesu linkowania. |
| `static void disableAttributeArray(...)` | WyÄąâ€šÄ…cza tablicÄ™ atrybutĂłw wierzchoÄąâ€škĂłw. |
| `static void enableAttributeArray(...)` | WÄąâ€šÄ…cza tablicÄ™ atrybutĂłw wierzchoÄąâ€škĂłw. |
| `int getAttributeLocation(...)` | Pobiera lokalizacjÄ™ atrybutu o danej nazwie. |
| `void bindAttributeLocation(...)` | Przypisuje lokalizacjÄ™ do atrybutu (przed linkowaniem). |
| `void bindUniformLocation(...)` | Wyszukuje i buforuje lokalizacjÄ™ uniformu. |
| `void setAttributeArray(...)` | Ustawia wskaÄąĹźnik na dane dla tablicy atrybutĂłw. |
| `void setAttributeValue(...)` | Ustawia wartoÄąâ€şÄ‡ dla pojedynczego atrybutu. |
| `void setUniformValue(...)` | Ustawia wartoÄąâ€şÄ‡ dla uniformu (przeciÄ…ÄąÄ˝ona dla rĂłÄąÄ˝nych typĂłw: `int`, `float`, `Color`, `Matrix`). |
| `bool isLinked()` | Zwraca `true`, jeÄąâ€şli program zostaÄąâ€š pomyÄąâ€şlnie zlinkowany. |
| `uint getProgramId()` | Zwraca ID programu OpenGL. |
| `ShaderList getShaders()` | Zwraca listÄ™ powiÄ…zanych shaderĂłw. |
| `std::string getName()` | Zwraca nazwÄ™ programu. |
## Zmienne prywatne

-   `m_name`: Nazwa programu (dla celĂłw identyfikacji).
-   `m_linked`: Flaga wskazujÄ…ca, czy program jest zlinkowany.
-   `m_programId`: ID programu w OpenGL.
-   `m_currentProgram`: Statyczna zmienna Äąâ€şledzÄ…ca aktualnie aktywny program.
-   `m_shaders`: Lista powiÄ…zanych obiektĂłw `Shader`.
-   `m_uniformLocations`: Tablica przechowujÄ…ca zbuforowane lokalizacje uniformĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/shader.h`: Definicja klasy `Shader`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Jest klasÄ… bazowÄ… dla `PainterShaderProgram`, ktĂłra rozszerza jÄ… o uniformy specyficzne dla `Painter`.
-   Jest zarzÄ…dzana przez `ShaderManager`.
-   Jest oznaczona jako `@bindclass`, co pozwala na interakcjÄ™ z obiektami tego typu z poziomu Lua.

---
# Ä‘Ĺşâ€śâ€ž animatedtexture.cpp
## Opis ogĂłlny

Plik `animatedtexture.cpp` zawiera implementacjÄ™ klasy `AnimatedTexture`, ktĂłra reprezentuje teksturÄ™ skÄąâ€šadajÄ…cÄ… siÄ™ z wielu klatek, odtwarzanych w pÄ™tli. Jest to podklasa `Texture`.
## Klasa `AnimatedTexture`
## `AnimatedTexture::AnimatedTexture(...)`

Konstruktor, ktĂłry tworzy animowanÄ… teksturÄ™.

-   **Parametry**:
    -   `size`: Rozmiar pojedynczej klatki.
    -   `frames`: Wektor wskaÄąĹźnikĂłw na obiekty `Image`, reprezentujÄ…ce poszczegĂłlne klatki animacji.
    -   `framesDelay`: Wektor czasĂłw (w milisekundach), jak dÄąâ€šugo kaÄąÄ˝da klatka ma byÄ‡ wyÄąâ€şwietlana.
    -   `buildMipmaps`, `compress`: Flagi przekazywane do konstruktora `Texture` dla kaÄąÄ˝dej klatki.
-   **DziaÄąâ€šanie**:
    1.  Iteruje przez wektor `frames` i dla kaÄąÄ˝dego `Image` tworzy nowy obiekt `Texture`, ktĂłry jest przechowywany w `m_frames`.
    2.  Inicjalizuje timer `m_animTimer` i ustawia bieÄąÄ˝Ä…cÄ… klatkÄ™ na 0.
## `bool AnimatedTexture::buildHardwareMipmaps()`

WÄąâ€šÄ…cza generowanie mipmap dla wszystkich klatek animacji.
## `void AnimatedTexture::setSmooth(bool smooth)` i `void AnimatedTexture::setRepeat(bool repeat)`

UstawiajÄ… odpowiednio flagi wygÄąâ€šadzania i powtarzania dla wszystkich tekstur-klatek.
## `void AnimatedTexture::update()`
## Opis semantyczny
Aktualizuje stan animacji. Ta metoda jest kluczowa i musi byÄ‡ wywoÄąâ€šywana przed kaÄąÄ˝dym uÄąÄ˝yciem tekstury w pÄ™tli renderowania.
## DziaÄąâ€šanie
1.  Sprawdza, czy czas, jaki upÄąâ€šynÄ…Äąâ€š od ostatniej zmiany klatki (`m_animTimer.ticksElapsed()`) jest wiÄ™kszy lub rĂłwny czasowi opĂłÄąĹźnienia dla bieÄąÄ˝Ä…cej klatki (`m_framesDelay[m_currentFrame]`).
2.  JeÄąâ€şli tak, przechodzi do nastÄ™pnej klatki, zapÄ™tlajÄ…c animacjÄ™ (`m_currentFrame = (m_currentFrame + 1) % m_frames.size()`), i resetuje timer.
3.  WywoÄąâ€šuje `update()` na teksturze bieÄąÄ˝Ä…cej klatki.
4.  Aktualizuje ID tekstury (`m_id`) i unikalne ID (`m_uniqueId`) klasy bazowej `Texture` na wartoÄąâ€şci z bieÄąÄ˝Ä…cej klatki. DziÄ™ki temu reszta systemu renderujÄ…cego moÄąÄ˝e traktowaÄ‡ `AnimatedTexture` jak zwykÄąâ€šÄ…, statycznÄ… teksturÄ™, nie wiedzÄ…c, ÄąÄ˝e jej ID zmienia siÄ™ w czasie.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/animatedtexture.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/graphics.h`: Do operacji na OpenGL.
-   `framework/core/eventdispatcher.h`: Potencjalnie do planowania aktualizacji.
-   Jest tworzona i zarzÄ…dzana przez `TextureManager` podczas Äąâ€šadowania animowanych plikĂłw PNG (APNG).

---
# Ä‘Ĺşâ€śâ€ž animatedtexture.h
## Opis ogĂłlny

Plik `animatedtexture.h` deklaruje klasÄ™ `AnimatedTexture`, ktĂłra jest specjalizacjÄ… klasy `Texture`. Reprezentuje ona teksturÄ™, ktĂłra zmienia swĂłj wyglÄ…d w czasie, odtwarzajÄ…c sekwencjÄ™ klatek.
## Klasa `AnimatedTexture`
## Opis semantyczny
`AnimatedTexture` dziedziczy po `Texture` i przechowuje kolekcjÄ™ tekstur (`std::vector<TexturePtr>`), ktĂłre reprezentujÄ… poszczegĂłlne klatki animacji. WewnÄ™trzny timer (`m_animTimer`) kontroluje, ktĂłra klatka jest aktualnie aktywna. Metoda `update()` jest odpowiedzialna za przeÄąâ€šÄ…czanie klatek i aktualizowanie ID tekstury w klasie bazowej, dziÄ™ki czemu dla systemu renderujÄ…cego wyglÄ…da ona jak pojedyncza, dynamicznie zmieniajÄ…ca siÄ™ tekstura.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `AnimatedTexture(...)` | Konstruktor, tworzy animowanÄ… teksturÄ™ z wektora obrazĂłw i czasĂłw opĂłÄąĹźnieÄąâ€ž. |
| `virtual ~AnimatedTexture()` | Destruktor. |
| `void replace(const ImagePtr& image)` | Pusta implementacja; zastÄ™powanie animowanej tekstury pojedynczym obrazem nie jest obsÄąâ€šugiwane w ten sposĂłb. |
| `void update()` | Aktualizuje bieÄąÄ˝Ä…cÄ… klatkÄ™ animacji. |
| `virtual bool isAnimatedTexture()` | Zwraca `true`, odrĂłÄąÄ˝niajÄ…c tÄ™ klasÄ™ od `Texture`. |
## Metody chronione

-   `virtual bool buildHardwareMipmaps()`: WÄąâ€šÄ…cza mipmapping dla wszystkich klatek.
-   `virtual void setSmooth(bool smooth)`: Ustawia wygÄąâ€šadzanie dla wszystkich klatek.
-   `virtual void setRepeat(bool repeat)`: Ustawia powtarzanie dla wszystkich klatek.
## Zmienne prywatne

-   `m_frames`: Wektor wskaÄąĹźnikĂłw na tekstury poszczegĂłlnych klatek.
-   `m_framesDelay`: Wektor czasĂłw opĂłÄąĹźnieÄąâ€ž dla kaÄąÄ˝dej klatki.
-   `m_currentFrame`: Indeks bieÄąÄ˝Ä…cej klatki.
-   `m_animTimer`: Timer do Äąâ€şledzenia czasu wyÄąâ€şwietlania klatki.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/texture.h`: Klasa bazowa `Texture`.
-   `framework/core/timer.h`: UÄąÄ˝ywa `Timer` do zarzÄ…dzania animacjÄ….
-   Jest tworzona przez `TextureManager` podczas Äąâ€šadowania plikĂłw APNG (Animated PNG).

---
# Ä‘Ĺşâ€śâ€ž apngloader.cpp
## Opis ogĂłlny

Plik `apngloader.cpp` zawiera implementacjÄ™ funkcji do Äąâ€šadowania animowanych plikĂłw PNG (APNG) oraz do zapisu standardowych plikĂłw PNG. Kod jest oparty na bibliotece APNG Disassembler 2.3 autorstwa Maxa Stepina i zostaÄąâ€š dostosowany do potrzeb frameworka.
## Funkcje
## `load_apng(std::stringstream& file, struct apng_data *apng)`
## Opis semantyczny
GÄąâ€šĂłwna funkcja do parsowania pliku w formacie APNG. Odczytuje ona poszczegĂłlne "chunki" (fragmenty) pliku PNG, takie jak `IHDR` (nagÄąâ€šĂłwek), `PLTE` (paleta), `tRNS` (przezroczystoÄąâ€şÄ‡), `acTL` (nagÄąâ€šĂłwek animacji), `fcTL` (kontrola klatki) oraz `IDAT`/`fdAT` (dane obrazu).
## DziaÄąâ€šanie
1.  Sprawdza sygnaturÄ™ pliku PNG.
2.  Odczytuje nagÄąâ€šĂłwek `IHDR` w celu uzyskania wymiarĂłw, gÄąâ€šÄ™bi kolorĂłw i innych podstawowych informacji.
3.  Alokuje bufory na zdekompresowane dane obrazu.
4.  W pÄ™tli odczytuje kolejne chunki:
    -   `PLTE` i `tRNS`: Wczytuje paletÄ™ kolorĂłw i informacje o przezroczystoÄąâ€şci.
    -   `acTL`: Identyfikuje plik jako animowany, odczytuje liczbÄ™ klatek i zapÄ™tleÄąâ€ž.
    -   `fcTL`: Odczytuje metadane dla pojedynczej klatki, takie jak wymiary, przesuniÄ™cie, czas trwania i operacje mieszania (`blend_op`) oraz usuwania (`dispose_op`).
    -   `IDAT` i `fdAT`: Gromadzi skompresowane dane obrazu dla klatki.
5.  Po odczytaniu danych dla klatki (`fcTL` lub `IEND`), dekompresuje je za pomocÄ… ZLIB (`inflate`), a nastÄ™pnie odfiltrowuje (usuwa filtry PNG takie jak Sub, Up, Average, Paeth).
6.  Komponuje finalny obraz klatki na podstawie poprzedniej klatki, stosujÄ…c operacje `dispose_op` (np. zostaw, wyczyÄąâ€şÄ‡ do tÄąâ€ša) i `blend_op` (np. zastÄ…p, naÄąâ€šĂłÄąÄ˝).
7.  Wynikowe dane klatki w formacie RGBA sÄ… zapisywane do bufora w strukturze `apng_data`.
8.  Zwraca 0 w przypadku sukcesu, -1 w przypadku bÄąâ€šÄ™du.
## `save_png(std::stringstream& f, unsigned int width, unsigned int height, int channels, unsigned char *pixels)`
## Opis semantyczny
Zapisuje dane obrazu do formatu PNG. Implementuje podstawowÄ… kompresjÄ™ z filtrowaniem, dynamicznie wybierajÄ…c najlepszy filtr dla kaÄąÄ˝dej linii obrazu w celu uzyskania lepszej kompresji.
## DziaÄąâ€šanie
1.  Zapisuje sygnaturÄ™ PNG i nagÄąâ€šĂłwek `IHDR`.
2.  Inicjalizuje strumienie kompresji ZLIB.
3.  Dla kaÄąÄ˝dej linii obrazu:
    -   Testuje piÄ™Ä‡ rĂłÄąÄ˝nych filtrĂłw PNG (None, Sub, Up, Average, Paeth).
    -   Wybiera filtr, ktĂłry generuje dane o najmniejszej sumie wartoÄąâ€şci bezwzglÄ™dnych bajtĂłw (co zwykle prowadzi do lepszej kompresji).
    -   Kompresuje przefiltrowanÄ… liniÄ™ za pomocÄ… `deflate`.
4.  Zapisuje skompresowane dane w chunkach `IDAT`.
5.  Zapisuje chunk koÄąâ€žcowy `IEND`.
## Funkcje pomocnicze

Plik zawiera wiele funkcji pomocniczych, m.in.:
-   `read32`, `read16`: Do odczytu liczb w porzÄ…dku big-endian.
-   `read_sub_row`, `read_up_row`, `read_average_row`, `read_paeth_row`: Do odfiltrowywania danych obrazu PNG.
-   `compose0`, `compose2`, `compose3`, `compose4`, `compose6`: Do kompozycji klatek animacji, konwertujÄ…c rĂłÄąÄ˝ne formaty pikseli na RGBA i stosujÄ…c operacje mieszania.
-   `unpack`: Dekompresuje i odfiltrowuje dane jednej klatki.
-   `write_chunk`, `write_IDATs`: Do zapisu chunkĂłw PNG.
-   `free_apng`: Zwalnia pamiÄ™Ä‡ zaalokowanÄ… w strukturze `apng_data`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/apngloader.h`: Plik nagÄąâ€šĂłwkowy.
-   **ZLIB**: UÄąÄ˝ywana do kompresji i dekompresji danych obrazu.
-   Jest uÄąÄ˝ywana przez `Image::loadPNG` do Äąâ€šadowania obrazĂłw i `Image::savePNG` do ich zapisu.

---
# Ä‘Ĺşâ€śâ€ž apngloader.h
## Opis ogĂłlny

Plik `apngloader.h` jest plikiem nagÄąâ€šĂłwkowym, ktĂłry deklaruje struktury danych i funkcje do obsÄąâ€šugi plikĂłw w formacie APNG (Animated PNG). Definiuje on publiczny interfejs do Äąâ€šadowania, zapisywania i zwalniania danych obrazu.
## Struktura `apng_data`
## Opis semantyczny
Struktura ta przechowuje wszystkie zdekompresowane i sparsowane dane z pliku APNG.
## Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `pdata` | `unsigned char *` | WskaÄąĹźnik na surowe dane pikseli wszystkich klatek, w formacie RGBA, jedna po drugiej. |
| `width` | `unsigned int` | SzerokoÄąâ€şÄ‡ obrazu w pikselach. |
| `height` | `unsigned int` | WysokoÄąâ€şÄ‡ obrazu w pikselach. |
| `first_frame`| `unsigned int` | Indeks pierwszej klatki animacji (zwykle 0). |
| `last_frame` | `unsigned int` | Indeks ostatniej klatki animacji. |
| `bpp` | `unsigned char` | Liczba bajtĂłw na piksel. |
| `coltype` | `unsigned char` | Typ koloru z nagÄąâ€šĂłwka PNG. |
| `num_frames` | `unsigned int` | CaÄąâ€škowita liczba klatek w animacji. |
| `num_plays` | `unsigned int` | Liczba powtĂłrzeÄąâ€ž animacji (0 oznacza nieskoÄąâ€žczonoÄąâ€şÄ‡). |
| `frames_delay`| `unsigned short *` | Tablica czasĂłw wyÄąâ€şwietlania dla kaÄąÄ˝dej klatki, w milisekundach. |
## Funkcje publiczne

| Funkcja | Opis |
| :--- | :--- |
| `int load_apng(std::stringstream& file, struct apng_data *apng)` | ÄąÂaduje i parsuje dane APNG ze strumienia `file` i zapisuje wyniki w strukturze `apng`. Zwraca 0 w przypadku sukcesu, -1 w przypadku bÄąâ€šÄ™du. |
| `void save_png(std::stringstream& file, ...)` | Zapisuje dane obrazu (pojedynczej klatki) do strumienia `file` w formacie PNG. |
| `void free_apng(struct apng_data *apng)` | Zwalnia pamiÄ™Ä‡ zaalokowanÄ… dynamicznie w strukturze `apng_data` (tj. `pdata` i `frames_delay`). |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `<sstream>`: UÄąÄ˝ywa `std::stringstream` jako ÄąĹźrĂłdÄąâ€ša danych wejÄąâ€şciowych i wyjÄąâ€şciowych.
-   Funkcje te sÄ… wykorzystywane przez klasÄ™ `Image` do implementacji metod `loadPNG` i `savePNG`.

---
# Ä‘Ĺşâ€śâ€ž atlas.cpp
## Opis ogĂłlny

Plik `atlas.cpp` implementuje klasÄ™ `Atlas`, ktĂłra zarzÄ…dza tzw. "atlasem tekstur". Jest to technika optymalizacyjna, polegajÄ…ca na Äąâ€šÄ…czeniu wielu maÄąâ€šych tekstur w jednÄ… duÄąÄ˝Ä… teksturÄ™, aby zminimalizowaÄ‡ liczbÄ™ zmian stanu w potoku renderowania grafiki (zmiana tekstury jest kosztownÄ… operacjÄ…).
## Zmienne globalne
## `g_atlas`

Globalna instancja klasy `Atlas`, zapewniajÄ…ca scentralizowany dostÄ™p do mechanizmu cachowania tekstur.

`$fenceInfo
Atlas g_atlas;
```
## Klasa `Atlas`
## `void Atlas::init()`
## Opis semantyczny
Inicjalizuje atlas.
## DziaÄąâ€šanie
1.  OkreÄąâ€şla maksymalny rozmiar tekstury atlasu, biorÄ…c pod uwagÄ™ ograniczenia karty graficznej (`g_graphics.getMaxTextureSize()`), ale nie przekraczajÄ…c `4096x4096`.
2.  Tworzy dwa obiekty `FrameBuffer`:
    -   `m_atlas[0]`: GÄąâ€šĂłwny atlas dla ogĂłlnych tekstur.
    -   `m_atlas[1]`: Atlas dla tekstur fontĂłw.
3.  WiÄ…ÄąÄ˝e tekstury atlasĂłw do jednostek teksturujÄ…cych `GL_TEXTURE6` i `GL_TEXTURE7`, aby byÄąâ€šy globalnie dostÄ™pne dla shaderĂłw.
4.  Resetuje oba atlasy, przygotowujÄ…c je do uÄąÄ˝ycia.
## `void Atlas::reset()` i `void Atlas::resetAtlas(int location)`

Metody do czyszczenia atlasu. `reset()` czyÄąâ€şci gÄąâ€šĂłwny atlas i bufor `m_cache`. `resetAtlas()` przygotowuje konkretny atlas do ponownego uÄąÄ˝ycia, czyszczÄ…c jego zawartoÄąâ€şÄ‡ (wypeÄąâ€šniajÄ…c przezroczystoÄąâ€şciÄ…) i resetujÄ…c informacje o wolnych przestrzeniach (`m_locations`).
## `void Atlas::terminate()`

Zwalnia obiekty `FrameBuffer` atlasĂłw.
## `Point Atlas::cache(uint64_t hash, const Size& size, bool& draw)`
## Opis semantyczny
GÄąâ€šĂłwna metoda do cachowania tekstury. Sprawdza, czy tekstura o danym hashu jest juÄąÄ˝ w atlasie. JeÄąâ€şli nie, znajduje dla niej wolne miejsce.
## DziaÄąâ€šanie
1.  JeÄąâ€şli `m_doReset` jest `true`, najpierw resetuje atlas.
2.  Sprawdza, czy hash istnieje w `m_cache`. JeÄąâ€şli tak, zwraca zapisanÄ… pozycjÄ™.
3.  JeÄąâ€şli nie, oblicza, jakiego rozmiaru bloku potrzebuje tekstura (`calculateIndex`).
4.  JeÄąâ€şli tekstura jest za duÄąÄ˝a, zwraca `Point(-1, -1)`.
5.  PrĂłbuje znaleÄąĹźÄ‡ wolne miejsce w `m_locations`. JeÄąâ€şli go nie ma, wywoÄąâ€šuje `findSpace` w celu podziaÄąâ€šu wiÄ™kszego bloku.
6.  JeÄąâ€şli nie ma miejsca, ustawia `m_doReset = true` i zwraca `Point(-1, -1)`.
7.  JeÄąâ€şli miejsce siÄ™ znajdzie, zapisuje pozycjÄ™ w `m_cache`, ustawia `draw = true` (sygnalizujÄ…c, ÄąÄ˝e tekstura musi zostaÄ‡ narysowana w atlasie) i zwraca pozycjÄ™.
## `void Atlas::bind()` i `void Atlas::release()`

Metody do bindowania i zwalniania `FrameBuffer` gÄąâ€šĂłwnego atlasu, aby umoÄąÄ˝liwiÄ‡ rysowanie w nim nowych tekstur.
## `Point Atlas::cacheFont(const TexturePtr& fontTexture)`

Specjalna metoda do cachowania tekstur fontĂłw w drugim atlasie (`m_atlas[1]`). DziaÄąâ€ša podobnie do `cache`, ale od razu rysuje teksturÄ™ fontu w znalezionym miejscu.
## `int Atlas::calculateIndex(const Size& size)`

Oblicza indeks (od 0 do 6) odpowiadajÄ…cy rozmiarowi bloku potrzebnego do przechowania tekstury (np. 32x32, 64x64, ..., 2048x2048).
## `bool Atlas::findSpace(int location, int index)`

Rekurencyjna metoda, ktĂłra prĂłbuje znaleÄąĹźÄ‡ wolne miejsce dla bloku o danym `index`. JeÄąâ€şli nie ma wolnych blokĂłw tego rozmiaru, prĂłbuje znaleÄąĹźÄ‡ i podzieliÄ‡ wiÄ™kszy blok (o `index + 1`).
## `std::string Atlas::getStats()`

Zwraca informacje debugowania o liczbie wolnych miejsc w poszczegĂłlnych blokach atlasu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/atlas.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/framebuffermanager.h`: UÄąÄ˝ywa `FrameBufferManager` do tworzenia `FrameBuffer` dla atlasĂłw.
-   `framework/graphics/painter.h`: UÄąÄ˝ywa `Painter` do rysowania w atlasie.
-   `framework/graphics/graphics.h`: Do pobierania maksymalnego rozmiaru tekstury.
-   Jest uÄąÄ˝ywany przez `DrawQueue` i `DrawCache` do optymalizacji renderowania.

---
# Ä‘Ĺşâ€śâ€ž bitmapfont.cpp
## Opis ogĂłlny

Plik `bitmapfont.cpp` zawiera implementacjÄ™ klasy `BitmapFont`, ktĂłra zarzÄ…dza fontami opartymi na bitmapach (obrazach). Taki font skÄąâ€šada siÄ™ z pojedynczej tekstury zawierajÄ…cej wszystkie glify (znaki) uÄąâ€šoÄąÄ˝one w siatce.
## Klasa `BitmapFont`
## `void BitmapFont::load(const OTMLNodePtr& fontNode)`
## Opis semantyczny
ÄąÂaduje definicjÄ™ fontu z wÄ™zÄąâ€ša OTML (zazwyczaj z pliku `.otfont`).
## DziaÄąâ€šanie
1.  Odczytuje z wÄ™zÄąâ€ša OTML podstawowe atrybuty fontu:
    -   `texture`: ÄąĹˇcieÄąÄ˝ka do pliku z obrazem fontu.
    -   `glyph-size`: Rozmiar pojedynczego glifu w siatce.
    -   `height`: Rzeczywista wysokoÄąâ€şÄ‡ glifu.
    -   `y-offset`: PrzesuniÄ™cie w osi Y.
    -   `first-glyph`: Kod ASCII pierwszego znaku w siatce (zwykle 32 - spacja).
    -   `spacing`: OdstÄ™py miÄ™dzy glifami.
2.  Oblicza szerokoÄąâ€şci poszczegĂłlnych glifĂłw:
    -   JeÄąâ€şli zdefiniowano `fixed-glyph-width`, wszystkie glify majÄ… tÄ™ samÄ… szerokoÄąâ€şÄ‡.
    -   W przeciwnym razie wywoÄąâ€šuje `calculateGlyphsWidthsAutomatically`, aby automatycznie wykryÄ‡ szerokoÄąâ€şÄ‡ kaÄąÄ˝dego znaku.
3.  Ustawia specjalne szerokoÄąâ€şci dla spacji (32) i znaku nowej linii (`\n`).
4.  ÄąÂaduje teksturÄ™ fontu za pomocÄ… `g_textures.getTexture()`.
5.  JeÄąâ€şli fonty sÄ… cachowane w atlasie (`!DONT_CACHE_FONTS`), wywoÄąâ€šuje `g_atlas.cacheFont()` i ustawia teksturÄ™ atlasu jako ÄąĹźrĂłdÄąâ€šowÄ….
6.  Oblicza i zapisuje wspĂłÄąâ€šrzÄ™dne tekstury dla kaÄąÄ˝dego glifu w `m_glyphsTextureCoords`.
## `void BitmapFont::drawText(...)`

Metody te nie rysujÄ… tekstu bezpoÄąâ€şrednio, lecz dodajÄ… zadanie rysowania do globalnej kolejki `g_drawQueue`.

-   **`drawText(..., const Color& color, ...)`**: Dodaje zadanie rysowania tekstu jednokolorowego.
-   **`drawColoredText(..., const std::vector<std::pair<int, Color>>& colors, ...)`**: Dodaje zadanie rysowania tekstu z wieloma kolorami.
## `void BitmapFont::calculateDrawTextCoords(...)`

Oblicza wspĂłÄąâ€šrzÄ™dne ekranowe i tekstury dla kaÄąÄ˝dego glifu w podanym tekÄąâ€şcie, uwzglÄ™dniajÄ…c wyrĂłwnanie i przycinanie do podanego prostokÄ…ta. Wyniki sÄ… zapisywane w `CoordsBuffer`.
## `const std::vector<Point>& BitmapFont::calculateGlyphsPositions(...)`

Oblicza pozycje (lewy gĂłrny rĂłg) kaÄąÄ˝dego glifu w tekÄąâ€şcie, uwzglÄ™dniajÄ…d wyrĂłwnanie. UÄąÄ˝ywa statycznych, lokalnych dla wÄ…tku wektorĂłw w celu optymalizacji. Zwraca rĂłwnieÄąÄ˝ obliczony rozmiar caÄąâ€šego bloku tekstu.
## `Size BitmapFont::calculateTextRectSize(const std::string& text)`

Zwraca rozmiar prostokÄ…ta, jaki zajmie podany tekst, uÄąÄ˝ywajÄ…c `calculateGlyphsPositions`.
## `std::string BitmapFont::wrapText(...)`

Implementuje zawijanie tekstu. Dzieli tekst na linie, tak aby ÄąÄ˝adna nie przekraczaÄąâ€ša `maxWidth`. ObsÄąâ€šuguje rĂłwnieÄąÄ˝ przenoszenie definicji kolorĂłw (`m_textColors`) do nowych linii.
## `void BitmapFont::calculateGlyphsWidthsAutomatically(...)`

Prywatna metoda, ktĂłra analizuje obraz tekstury fontu piksel po pikselu. Dla kaÄąÄ˝dego glifu znajduje ostatniÄ… nieprzezroczystÄ… kolumnÄ™ pikseli, aby precyzyjnie okreÄąâ€şliÄ‡ jego szerokoÄąâ€şÄ‡.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/atlas.h`: UÄąÄ˝ywa `g_atlas` do cachowania tekstur fontĂłw.
-   `framework/graphics/bitmapfont.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/texturemanager.h`: UÄąÄ˝ywa `g_textures` do Äąâ€šadowania obrazu fontu.
-   `framework/graphics/image.h`: UÄąÄ˝ywa `Image` do analizy pikseli w `calculateGlyphsWidthsAutomatically`.
-   `framework/graphics/drawqueue.h`: Dodaje zadania rysowania tekstu do `g_drawQueue`.
-   Jest zarzÄ…dzana przez `FontManager`.

---
# Ä‘Ĺşâ€śâ€ž atlas.h
## Opis ogĂłlny

Plik `atlas.h` deklaruje interfejs klasy `Atlas`, ktĂłra implementuje mechanizm atlasu tekstur. Celem atlasu jest optymalizacja renderowania poprzez grupowanie wielu maÄąâ€šych tekstur w jednÄ… duÄąÄ˝Ä… teksturÄ™, co redukuje liczbÄ™ wywoÄąâ€šaÄąâ€ž `glBindTexture` w OpenGL.
## Klasa `Atlas`
## Opis semantyczny
`Atlas` zarzÄ…dza jednym lub kilkoma duÄąÄ˝ymi obiektami `FrameBuffer`, ktĂłre dziaÄąâ€šajÄ… jak "pÄąâ€šĂłtna". Kiedy system renderujÄ…cy potrzebuje narysowaÄ‡ maÄąâ€šÄ… teksturÄ™, `Atlas` znajduje dla niej wolne miejsce w jednym z pÄąâ€šĂłcien, kopiuje tam jej zawartoÄąâ€şÄ‡ (jeÄąâ€şli jeszcze jej tam nie ma) i zwraca wspĂłÄąâ€šrzÄ™dne wewnÄ…trz atlasu. PĂłÄąĹźniejsze odwoÄąâ€šania do tej samej tekstury uÄąÄ˝ywajÄ… juÄąÄ˝ skopiowanej wersji z atlasu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje atlas, tworzÄ…c `FrameBuffer` o maksymalnym moÄąÄ˝liwym rozmiarze. |
| `void terminate()` | Zwalnia zasoby atlasu. |
| `void reload()` | Resetuje i czyÄąâ€şci zawartoÄąâ€şÄ‡ atlasĂłw. |
| `Point cache(uint64_t hash, const Size& size, bool& draw)` | GÄąâ€šĂłwna metoda cachujÄ…ca. Sprawdza, czy tekstura o danym hashu jest juÄąÄ˝ w atlasie. JeÄąâ€şli nie, znajduje wolne miejsce i zwraca jego koordynaty. Parametr `draw` jest ustawiany na `true`, jeÄąâ€şli teksturÄ™ trzeba narysowaÄ‡ w atlasie. |
| `Point cacheFont(const TexturePtr& fontTexture)` | Specjalna metoda do cachowania tekstur fontĂłw w dedykowanym atlasie. |
| `TexturePtr get(int location)` | Zwraca wskaÄąĹźnik na teksturÄ™ atlasu o danym indeksie (0 - gÄąâ€šĂłwny, 1 - fonty). |
| `void bind()` | Bindowanie `FrameBuffer` atlasu jako celu renderowania. |
| `void release()` | Odpinanie `FrameBuffer` atlasu. |
| `std::string getStats()` | Zwraca informacje diagnostyczne o stanie atlasu. |
## Zmienne prywatne

-   `m_atlas[2]`: Tablica wskaÄąĹźnikĂłw na `FrameBuffer` (dla ogĂłlnych tekstur i fontĂłw).
-   `m_cache`: Mapa (`std::map`) przechowujÄ…ca hashe skachowanych tekstur i ich pozycje w atlasie.
-   `m_locations[2][7]`: Tablica list przechowujÄ…ca pozycje wolnych blokĂłw o rĂłÄąÄ˝nych rozmiarach (od 32x32 do 2048x2048) dla obu atlasĂłw.
-   `m_size`: Rozmiar boku tekstury atlasu.
-   `m_doReset`: Flaga sygnalizujÄ…ca koniecznoÄąâ€şÄ‡ zresetowania atlasu (gdy zabraknie miejsca).
## Zmienne globalne

-   `g_atlas`: Globalna instancja `Atlas`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/drawqueue.h`: Potencjalnie uÄąÄ˝ywany, ale gÄąâ€šĂłwnie to `DrawQueue` uÄąÄ˝ywa `Atlas`.
-   `framework/graphics/framebuffer.h`: UÄąÄ˝ywa `FrameBuffer` jako "pÄąâ€šĂłtna" dla atlasu.
-   UÄąÄ˝ywany przez system renderowania (`DrawQueue`, `DrawCache`) do optymalizacji rysowania.
-   `FontManager` uÄąÄ˝ywa go do cachowania tekstur fontĂłw.

---
# Ä‘Ĺşâ€śâ€ž bitmapfont.h
## Opis ogĂłlny

Plik `bitmapfont.h` deklaruje klasÄ™ `BitmapFont`, ktĂłra reprezentuje font oparty na bitmapie. Jest to kluczowy element systemu renderowania tekstu w aplikacji.
## Klasa `BitmapFont`
## Opis semantyczny
`BitmapFont` zarzÄ…dza pojedynczym fontem, ktĂłry jest zdefiniowany jako obraz (tekstura) zawierajÄ…cy siatkÄ™ znakĂłw (glifĂłw). Klasa przechowuje informacje o rozmiarze glifĂłw, ich pozycjach na teksturze oraz szerokoÄąâ€şciach poszczegĂłlnych znakĂłw. Dostarcza metody do rysowania tekstu (ktĂłre w rzeczywistoÄąâ€şci delegujÄ… zadanie do `DrawQueue`) oraz do obliczania wymiarĂłw i zawijania tekstu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `BitmapFont(const std::string& name)` | Konstruktor, ustawia nazwÄ™ fontu i unikalne ID. |
| `void load(const OTMLNodePtr& fontNode)` | ÄąÂaduje definicjÄ™ fontu z wÄ™zÄąâ€ša OTML. |
| `void drawText(...)` | Dodaje do kolejki renderowania zadanie narysowania tekstu. |
| `void drawColoredText(...)` | Dodaje zadanie narysowania tekstu z wieloma kolorami. |
| `void calculateDrawTextCoords(...)` | Oblicza wspĂłÄąâ€šrzÄ™dne wierzchoÄąâ€škĂłw i tekstur dla renderowanego tekstu. |
| `const std::vector<Point>& calculateGlyphsPositions(...)` | Oblicza pozycje poszczegĂłlnych glifĂłw w tekÄąâ€şcie. |
| `Size calculateTextRectSize(...)` | Oblicza rozmiar prostokÄ…ta zajmowanego przez tekst. |
| `std::string wrapText(...)` | ZÄąâ€šamuje tekst na wiele linii, aby zmieÄąâ€şciÄąâ€š siÄ™ w podanej szerokoÄąâ€şci. |
| `int getId()` | Zwraca unikalne ID fontu. |
| `std::string getName()` | Zwraca nazwÄ™ fontu. |
| `int getGlyphHeight()` | Zwraca wysokoÄąâ€şÄ‡ glifĂłw. |
| `const Rect* getGlyphsTextureCoords()` | Zwraca tablicÄ™ wspĂłÄąâ€šrzÄ™dnych tekstur dla wszystkich glifĂłw. |
| `const Size* getGlyphsSize()` | Zwraca tablicÄ™ rozmiarĂłw dla wszystkich glifĂłw. |
| `const TexturePtr& getTexture()` | Zwraca teksturÄ™ fontu (moÄąÄ˝e to byÄ‡ tekstura atlasu). |
| `int getYOffset()` | Zwraca przesuniÄ™cie Y. |
| `Size getGlyphSpacing()` | Zwraca odstÄ™py miÄ™dzy glifami. |
## Zmienne prywatne

-   `m_name`: Nazwa fontu.
-   `m_glyphHeight`: WysokoÄąâ€şÄ‡ glifu.
-   `m_firstGlyph`: Kod ASCII pierwszego znaku.
-   `m_yOffset`: PrzesuniÄ™cie w osi Y.
-   `m_id`: Unikalne ID fontu.
-   `m_glyphSpacing`: OdstÄ™py miÄ™dzy glifami.
-   `m_texture`: WskaÄąĹźnik na teksturÄ™ fontu.
-   `m_glyphsTextureCoords[256]`: Tablica wspĂłÄąâ€šrzÄ™dnych tekstur dla kaÄąÄ˝dego glifu.
-   `m_glyphsSize[256]`: Tablica rozmiarĂłw dla kaÄąÄ˝dego glifu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Deklaracje typĂłw graficznych.
-   `framework/graphics/texture.h`: UÄąÄ˝ywa `Texture` do przechowywania obrazu fontu.
-   `framework/otml/declarations.h`: UÄąÄ˝ywa `OTMLNodePtr` w metodzie `load`.
-   `framework/graphics/coordsbuffer.h`: UÄąÄ˝ywa `CoordsBuffer` do przechowywania geometrii tekstu.
-   Jest zarzÄ…dzana przez `FontManager`.
-   Jest uÄąÄ˝ywana przez `UIWidget` i inne komponenty do renderowania tekstu.

---
# Ä‘Ĺşâ€śâ€ž cachedtext.cpp
## Opis ogĂłlny

Plik `cachedtext.cpp` zawiera implementacjÄ™ klasy `CachedText`, ktĂłra sÄąâ€šuÄąÄ˝y do optymalizacji renderowania tekstu, ktĂłry nie zmienia siÄ™ czÄ™sto.
## Klasa `CachedText`
## `CachedText::CachedText()`

Konstruktor. Inicjalizuje domyÄąâ€şlny font, wyrĂłwnanie do Äąâ€şrodka (`Fw::AlignCenter`) i inne wartoÄąâ€şci domyÄąâ€şlne.
## `void CachedText::draw(const Rect& rect, const Color& color)`
## Opis semantyczny
GÄąâ€šĂłwna metoda rysujÄ…ca. Renderuje tekst w podanym prostokÄ…cie z danym kolorem.
## DziaÄąâ€šanie
1.  Sprawdza, czy font jest ustawiony.
2.  Sprawdza, czy tekst musi zostaÄ‡ "przekeshowany" (`m_textMustRecache`) lub czy zmieniÄąâ€š siÄ™ prostokÄ…t docelowy (`m_textCachedScreenCoords`). JeÄąâ€şli tak, aktualizuje buforowane koordynaty.
3.  WywoÄąâ€šuje metodÄ™ `m_font->drawText()` lub `m_font->drawColoredText()` w celu dodania zadania rysowania do `DrawQueue`.

> NOTE: Nazwa "cached" moÄąÄ˝e byÄ‡ nieco mylÄ…ca. Klasa nie renderuje tekstu do tekstury. Zamiast tego, "keszuje" obliczenia zwiÄ…zane z pozycjonowaniem glifĂłw, ale samo rysowanie odbywa siÄ™ dynamicznie w kaÄąÄ˝dej klatce za pomocÄ… `BitmapFont::drawText`.
## `void CachedText::setColoredText(const std::vector<std::string>& texts)`

Ustawia tekst skÄąâ€šadajÄ…cy siÄ™ z fragmentĂłw o rĂłÄąÄ˝nych kolorach. Parsuje wektor, tworzÄ…c wewnÄ™trznÄ… reprezentacjÄ™ `m_text` i `m_textColors`, a nastÄ™pnie wywoÄąâ€šuje `update()`.
## `void CachedText::update()`

Prywatna metoda pomocnicza. Oblicza rozmiar tekstu za pomocÄ… `m_font->calculateTextRectSize()` i ustawia flagÄ™ `m_textMustRecache` na `true`, co wymusza przeliczenie geometrii przy nastÄ™pnym wywoÄąâ€šaniu `draw()`.
## `void CachedText::wrapText(int maxWidth)`

Zawija tekst, aby zmieÄąâ€şciÄąâ€š siÄ™ w podanej szerokoÄąâ€şci, uÄąÄ˝ywajÄ…c metody `m_font->wrapText()`, a nastÄ™pnie wywoÄąâ€šuje `update()`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/cachedtext.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/painter.h`: PoÄąâ€şrednio, poprzez `BitmapFont`.
-   `framework/graphics/fontmanager.h`: UÄąÄ˝ywa `g_fonts` do pobrania domyÄąâ€şlnego fontu.
-   `framework/graphics/bitmapfont.h`: Kluczowa zaleÄąÄ˝noÄąâ€şÄ‡; uÄąÄ˝ywa `BitmapFont` do wszystkich operacji na tekÄąâ€şcie.

---
# Ä‘Ĺşâ€śâ€ž colorarray.h
## Opis ogĂłlny

Plik `colorarray.h` deklaruje klasÄ™ `ColorArray`, ktĂłra jest prostym kontenerem na tablicÄ™ kolorĂłw w formacie `float`. Jest uÄąÄ˝ywana do przekazywania kolorĂłw dla poszczegĂłlnych wierzchoÄąâ€škĂłw do systemu renderujÄ…cego.
## Klasa `ColorArray`
## Opis semantyczny
`ColorArray` dziaÄąâ€ša jako bufor dla kolorĂłw. KaÄąÄ˝dy kolor jest reprezentowany przez cztery wartoÄąâ€şci `float` (R, G, B, A) w zakresie od 0.0 do 1.0. Klasa udostÄ™pnia metody do dodawania kolorĂłw i dostÄ™pu do surowego wskaÄąĹźnika na dane, co jest potrzebne do przekazania ich do OpenGL.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void addColor(float r, float g, float b, float a)` | Dodaje kolor do bufora, podajÄ…c skÄąâ€šadowe jako `float`. |
| `void addColor(const Color& c)` | Dodaje kolor do bufora, pobierajÄ…c skÄąâ€šadowe z obiektu `Color`. |
| `void clear()` | CzyÄąâ€şci bufor. |
| `float *colors() const` | Zwraca wskaÄąĹźnik na poczÄ…tek danych (alias dla `data()`). |
| `float *data() const` | Zwraca wskaÄąĹźnik na surowe dane bufora. |
| `int colorCount() const` | Zwraca liczbÄ™ peÄąâ€šnych kolorĂłw w buforze (alias dla `count()`). |
| `int count() const` | Zwraca liczbÄ™ kolorĂłw. |
| `int size() const` | Zwraca caÄąâ€škowitÄ… liczbÄ™ wartoÄąâ€şci `float` w buforze (tj. `colorCount() * 4`). |
## Zmienne prywatne

-   `m_buffer`: Obiekt `DataBuffer<float>`, ktĂłry przechowuje dane kolorĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: UÄąÄ˝ywa `DataBuffer` jako wewnÄ™trznego kontenera.
-   Jest uÄąÄ˝ywana przez `Painter` do przekazywania tablicy kolorĂłw do shadera, co pozwala na rysowanie gradientĂłw lub wielokolorowych ksztaÄąâ€štĂłw.

---
# Ä‘Ĺşâ€śâ€ž cachedtext.h
## Opis ogĂłlny

Plik `cachedtext.h` deklaruje klasÄ™ `CachedText`, ktĂłra jest opakowaniem (wrapperem) uÄąâ€šatwiajÄ…cym zarzÄ…dzanie i renderowanie tekstu, ktĂłry moÄąÄ˝e byÄ‡ keszowany.
## Klasa `CachedText`
## Opis semantyczny
Klasa `CachedText` przechowuje tekst, font, wyrĂłwnanie i inne wÄąâ€šaÄąâ€şciwoÄąâ€şci. Jej gÄąâ€šĂłwnym celem jest optymalizacja renderowania poprzez unikanie ponownych obliczeÄąâ€ž geometrii tekstu w kaÄąÄ˝dej klatce. Kiedy tekst lub jego parametry siÄ™ zmieniajÄ…, metoda `update()` jest wywoÄąâ€šywana, aby przeliczyÄ‡ rozmiar i ustawiÄ‡ flagÄ™ koniecznoÄąâ€şci ponownego buforowania wspĂłÄąâ€šrzÄ™dnych.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CachedText()` | Konstruktor. |
| `void draw(const Rect& rect, const Color& color)` | Rysuje skeszowany tekst w podanym prostokÄ…cie. |
| `void wrapText(int maxWidth)` | Zawija tekst do podanej szerokoÄąâ€şci. |
| `void setFont(...)` | Ustawia font i aktualizuje tekst. |
| `void setText(...)` | Ustawia tekst i aktualizuje go. |
| `void setColoredText(...)` | Ustawia tekst skÄąâ€šadajÄ…cy siÄ™ z fragmentĂłw o rĂłÄąÄ˝nych kolorach. |
| `void setAlign(...)` | Ustawia wyrĂłwnanie tekstu. |
| `Size getTextSize()` | Zwraca obliczony rozmiar tekstu. |
| `std::string getText() const` | Zwraca przechowywany tekst. |
| `BitmapFontPtr getFont() const` | Zwraca uÄąÄ˝ywany font. |
| `Fw::AlignmentFlag getAlign() const` | Zwraca wyrĂłwnanie. |
| `bool hasText()` | Zwraca `true`, jeÄąâ€şli tekst nie jest pusty. |
## Zmienne prywatne

-   `m_text`: GÄąâ€šĂłwny, niezmieniony tekst.
-   `m_textColors`: Wektor par przechowujÄ…cy pozycje i kolory dla tekstu wielokolorowego.
-   `m_textSize`: Obliczony rozmiar tekstu.
-   `m_textMustRecache`: Flaga wskazujÄ…ca, ÄąÄ˝e geometria tekstu musi zostaÄ‡ przeliczona.
-   `m_textCachedScreenCoords`: Ostatni prostokÄ…t, w ktĂłrym tekst byÄąâ€š rysowany.
-   `m_font`: UÄąÄ˝ywany `BitmapFont`.
-   `m_align`: WyrĂłwnanie tekstu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/graphics/coordsbuffer.h`: PoÄąâ€şrednio, przez `BitmapFont`.
-   `framework/graphics/drawqueue.h`: PoÄąâ€şrednio, przez `BitmapFont`.
-   Klasa ta jest prawdopodobnie uÄąÄ˝ywana w komponentach UI, ktĂłre wyÄąâ€şwietlajÄ… tekst, aby uproÄąâ€şciÄ‡ i zoptymalizowaÄ‡ jego renderowanie.

---
# Ä‘Ĺşâ€śâ€ž coordsbuffer.h
## Opis ogĂłlny

Plik `coordsbuffer.h` deklaruje klasÄ™ `CoordsBuffer`, ktĂłra jest specjalizowanym kontenerem do przechowywania wspĂłÄąâ€šrzÄ™dnych wierzchoÄąâ€škĂłw (`vertex`) i tekstur (`texture coord`). Jest to kluczowy element optymalizacyjny, pozwalajÄ…cy na grupowanie geometrii wielu obiektĂłw i rysowanie ich w jednym wywoÄąâ€šaniu (batching).
## Klasa `CoordsBuffer`
## Opis semantyczny
`CoordsBuffer` przechowuje dwie tablice wierzchoÄąâ€škĂłw (`VertexArray`): jednÄ… dla pozycji na ekranie i drugÄ… dla pozycji na teksturze. Dostarcza metody do dodawania prostych prymitywĂłw geometrycznych (trĂłjkÄ…ty, prostokÄ…ty). Posiada mechanizm "keszowania" danych w sprzÄ™towym buforze VBO (Vertex Buffer Object) w celu dalszej optymalizacji.

> **NOTE**: Mimo nazwy, `CoordsBuffer` jest jednorazowego uÄąÄ˝ytku dla `DrawQueue`. Po przekazaniu do kolejki, jego zawartoÄąâ€şÄ‡ jest przenoszona (`std::move`), a oryginaÄąâ€š staje siÄ™ pusty. To zachowanie jest wymuszone przez usuniÄ™cie konstruktora kopiujÄ…cego i operatora przypisania, a zdefiniowanie konstruktora przenoszÄ…cego.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CoordsBuffer()` | Konstruktor, tworzy wewnÄ™trzne obiekty `VertexArray`. |
| `~CoordsBuffer()` | Destruktor. |
| `CoordsBuffer(CoordsBuffer&& c)` | Konstruktor przenoszÄ…cy. |
| `void clear()` | CzyÄąâ€şci oba bufory wierzchoÄąâ€škĂłw. |
| `void addTriangle(...)` | Dodaje trĂłjkÄ…t (tylko wspĂłÄąâ€šrzÄ™dne wierzchoÄąâ€škĂłw). |
| `void addRect(const Rect& dest)` | Dodaje prostokÄ…t (tylko wspĂłÄąâ€šrzÄ™dne wierzchoÄąâ€škĂłw). |
| `void addRect(const Rect& dest, const Rect& src)` | Dodaje prostokÄ…t z teksturÄ…. |
| `void addQuad(...)`, `addUpsideDownQuad(...)` | Dodaje czworokÄ…t (quad) - przydatne do renderowania w trybie `TriangleStrip`. |
| `void addBoudingRect(...)` | Dodaje geometriÄ™ ramki o okreÄąâ€şlonej gruboÄąâ€şci. |
| `void addRepeatedRects(...)` | WypeÄąâ€šnia prostokÄ…t docelowy powtarzajÄ…cÄ… siÄ™ teksturÄ…. |
| `float *getVertexArray()` | Zwraca wskaÄąĹźnik na dane wierzchoÄąâ€škĂłw. |
| `float *getTextureCoordArray()` | Zwraca wskaÄąĹźnik na dane wspĂłÄąâ€šrzÄ™dnych tekstury. |
| `int getVertexCount()` | Zwraca liczbÄ™ wierzchoÄąâ€škĂłw. |
| `HardwareBuffer* getVertexHardwareCache()` | Zwraca wskaÄąĹźnik na sprzÄ™towy bufor VBO dla wierzchoÄąâ€škĂłw (jeÄąâ€şli istnieje). |
| `void cache()` | Tworzy i wypeÄąâ€šnia sprzÄ™towe bufory VBO na podstawie bieÄąÄ˝Ä…cych danych. |
| `Rect getTextureRect()`| Oblicza i zwraca prostokÄ…t ograniczajÄ…cy wszystkie wspĂłÄąâ€šrzÄ™dne tekstury. |
## Zmienne prywatne

-   `m_locked`: Flaga uÄąÄ˝ywana do optymalizacji (zapobiega niepotrzebnemu kopiowaniu danych).
-   `m_vertexArray`: WskaÄąĹźnik na `VertexArray` przechowujÄ…cy pozycje.
-   `m_textureCoordArray`: WskaÄąĹźnik na `VertexArray` przechowujÄ…cy wspĂłÄąâ€šrzÄ™dne tekstury.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/vertexarray.h`: UÄąÄ˝ywa `VertexArray` jako podstawowego kontenera na dane.
-   Jest intensywnie uÄąÄ˝ywana przez `UIWidget` i jego podklasy do generowania geometrii, ktĂłra nastÄ™pnie jest przekazywana do `DrawQueue` w celu renderowania.

---
# Ä‘Ĺşâ€śâ€ž deptharray.h
## Opis ogĂłlny

Plik `deptharray.h` deklaruje klasÄ™ `DepthArray`, ktĂłra jest prostym kontenerem na tablicÄ™ wartoÄąâ€şci gÄąâ€šÄ™bokoÄąâ€şci (depth) w formacie `float`. Jest to prawdopodobnie czÄ™Äąâ€şÄ‡ eksperymentalnego lub nie w peÄąâ€šni zaimplementowanego mechanizmu renderowania 3D lub sortowania gÄąâ€šÄ™bokoÄąâ€şci.
## Klasa `DepthArray`
## Opis semantyczny
`DepthArray` dziaÄąâ€ša jako bufor dla wartoÄąâ€şci gÄąâ€šÄ™bokoÄąâ€şci (wspĂłÄąâ€šrzÄ™dna Z). KaÄąÄ˝da wartoÄąâ€şÄ‡ `float` w buforze odpowiada jednemu wierzchoÄąâ€škowi. Klasa udostÄ™pnia metody do dodawania wartoÄąâ€şci i dostÄ™pu do surowego wskaÄąĹźnika na dane, co jest potrzebne do przekazania ich do OpenGL jako atrybut wierzchoÄąâ€ška.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void addDepth(float depth)` | Dodaje nowÄ… wartoÄąâ€şÄ‡ gÄąâ€šÄ™bokoÄąâ€şci do bufora. |
| `void clear()` | CzyÄąâ€şci bufor. |
| `float *depths() const` | Zwraca wskaÄąĹźnik na poczÄ…tek danych (alias dla `data()`). |
| `float *data() const` | Zwraca wskaÄąĹźnik na surowe dane bufora. |
| `int depthCount() const` | Zwraca liczbÄ™ wartoÄąâ€şci w buforze (alias dla `count()`). |
| `int count() const` | Zwraca liczbÄ™ wartoÄąâ€şci. |
| `int size() const` | Zwraca liczbÄ™ wartoÄąâ€şci. |
## Zmienne prywatne

-   `m_buffer`: Obiekt `DataBuffer<float>`, ktĂłry przechowuje dane gÄąâ€šÄ™bokoÄąâ€şci.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: UÄąÄ˝ywa `DataBuffer` jako wewnÄ™trznego kontenera.
-   W obecnym kodzie jest uÄąÄ˝ywana w `Painter`, ale funkcjonalnoÄąâ€şÄ‡ zwiÄ…zana z buforem gÄąâ€šÄ™bi jest wykomentowana lub nie w peÄąâ€šni zaimplementowana (`WITH_DEPTH_BUFFER`).

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## Opis ogĂłlny

Plik `declarations.h` w module `graphics` sÄąâ€šuÄąÄ˝y jako centralny punkt dla wczesnych deklaracji (forward declarations) i definicji typĂłw (`typedef`) zwiÄ…zanych z systemem graficznym. Jego gÄąâ€šĂłwnym celem jest unikanie zaleÄąÄ˝noÄąâ€şci cyklicznych miÄ™dzy plikami nagÄąâ€šĂłwkowymi i minimalizowanie liczby doÄąâ€šÄ…czanych plikĂłw.
## Wczesne deklaracje (Forward Declarations)

Plik deklaruje istnienie nastÄ™pujÄ…cych klas, co pozwala na uÄąÄ˝ywanie wskaÄąĹźnikĂłw i referencji do nich bez potrzeby doÄąâ€šÄ…czania ich peÄąâ€šnych definicji:

-   `Texture`
-   `TextureManager`
-   `Image`
-   `AnimatedTexture`
-   `BitmapFont`
-   `CachedText`
-   `FrameBuffer`
-   `FrameBufferManager`
-   `Shader`
-   `ShaderProgram`
-   `PainterShaderProgram`
## Definicje typĂłw (Typedefs)

Plik definiuje aliasy dla inteligentnych wskaÄąĹźnikĂłw (`shared_object_ptr`) do klas graficznych, co uÄąâ€šatwia ich uÄąÄ˝ycie i poprawia czytelnoÄąâ€şÄ‡ kodu.

-   `ImagePtr`: `stdext::shared_object_ptr<Image>`
-   `TexturePtr`: `stdext::shared_object_ptr<Texture>`
-   `AnimatedTexturePtr`: `stdext::shared_object_ptr<AnimatedTexture>`
-   `BitmapFontPtr`: `stdext::shared_object_ptr<BitmapFont>`
-   `CachedTextPtr`: `stdext::shared_object_ptr<CachedText>`
-   `FrameBufferPtr`: `stdext::shared_object_ptr<FrameBuffer>`
-   `ShaderPtr`: `stdext::shared_object_ptr<Shader>`
-   `ShaderProgramPtr`: `stdext::shared_object_ptr<ShaderProgram>`
-   `PainterShaderProgramPtr`: `stdext::shared_object_ptr<PainterShaderProgram>`
-   `ShaderList`: `std::vector<ShaderPtr>`
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: DoÄąâ€šÄ…cza podstawowe definicje i typy, w tym `stdext::shared_object_ptr`.
-   `framework/graphics/glutil.h`: DoÄąâ€šÄ…cza nagÄąâ€šĂłwki OpenGL/GLES.
-   Ten plik jest intensywnie uÄąÄ˝ywany w caÄąâ€šym module graficznym i w innych moduÄąâ€šach, ktĂłre wchodzÄ… w interakcjÄ™ z grafikÄ… (np. `UI`).

---
# Ä‘Ĺşâ€śâ€ž coordsbuffer.cpp
## Opis ogĂłlny

Plik `coordsbuffer.cpp` zawiera implementacjÄ™ metod klasy `CoordsBuffer`, ktĂłra jest buforem na dane geometryczne do renderowania.
## Klasa `CoordsBuffer`
## `CoordsBuffer::CoordsBuffer()`

Konstruktor. Inicjalizuje dwa wewnÄ™trzne bufory: `m_vertexArray` (dla wspĂłÄąâ€šrzÄ™dnych pozycji) i `m_textureCoordArray` (dla wspĂłÄąâ€šrzÄ™dnych tekstury).
## `void CoordsBuffer::addBoudingRect(const Rect& dest, int innerLineWidth)`

Dodaje geometriÄ™ czterech prostokÄ…tĂłw, ktĂłre razem tworzÄ… ramkÄ™ (border) wewnÄ…trz podanego prostokÄ…ta `dest` o gruboÄąâ€şci `innerLineWidth`.
## `void CoordsBuffer::addRepeatedRects(const Rect& dest, const Rect& src)`

WypeÄąâ€šnia prostokÄ…t docelowy (`dest`) powtarzajÄ…cym siÄ™ wzorem z tekstury (`src`). Dzieli obszar `dest` na mniejsze prostokÄ…ty o rozmiarze `src` i dodaje je do bufora, odpowiednio przycinajÄ…c wspĂłÄąâ€šrzÄ™dne tekstury na krawÄ™dziach.
## `void CoordsBuffer::unlock(bool clear)`

Metoda zwiÄ…zana z wewnÄ™trznym mechanizmem "blokowania" bufora. Kiedy bufor jest zablokowany (`m_locked`), kaÄąÄ˝da operacja dodawania geometrii powoduje jego odblokowanie. Odblokowanie tworzy kopiÄ™ wewnÄ™trznych `VertexArray`, aby zapobiec modyfikacji danych, ktĂłre mogÄąâ€šy juÄąÄ˝ zostaÄ‡ przesÄąâ€šane do VBO. JeÄąâ€şli `clear` jest `true`, zamiast kopiowania tworzone sÄ… nowe, puste `VertexArray`.
## `Rect CoordsBuffer::getTextureRect()`

Przechodzi przez wszystkie wspĂłÄąâ€šrzÄ™dne tekstury w buforze, aby znaleÄąĹźÄ‡ minimalny i maksymalny punkt, a nastÄ™pnie zwraca prostokÄ…t ograniczajÄ…cy (bounding box) dla uÄąÄ˝ywanego fragmentu tekstury.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/coordsbuffer.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/graphics.h`: Potencjalnie do funkcji zwiÄ…zanych z grafikÄ….
-   Jest uÄąÄ˝ywana do budowania geometrii przez klasy takie jak `UIWidget`, a nastÄ™pnie konsumowana przez `DrawQueue` i `Painter` do renderowania.

---
# Ä‘Ĺşâ€śâ€ž drawcache.cpp
## Opis ogĂłlny

Plik `drawcache.cpp` implementuje klasÄ™ `DrawCache`, ktĂłra jest kluczowym elementem systemu optymalizacji renderowania. Jej zadaniem jest grupowanie (batching) operacji rysowania, ktĂłre uÄąÄ˝ywajÄ… tej samej tekstury (atlasu), aby zminimalizowaÄ‡ liczbÄ™ wywoÄąâ€šaÄąâ€ž rysujÄ…cych (draw calls) do OpenGL.
## Zmienne globalne
## `g_drawCache`

Globalna instancja `DrawCache`, uÄąÄ˝ywana przez `DrawQueue` do buforowania operacji.

`$fenceInfo
DrawCache g_drawCache;
```
## Klasa `DrawCache`
## `void DrawCache::draw()`
## Opis semantyczny
Wykonuje zgrupowane operacje rysowania.
## DziaÄąâ€šanie
1.  Upewnia siÄ™, ÄąÄ˝e atlas tekstur jest odÄąâ€šÄ…czony (`release()`).
2.  JeÄąâ€şli bufor nie jest pusty (`m_size > 0`), wywoÄąâ€šuje `g_painter->drawCache()`, przekazujÄ…c jej wszystkie zebrane dane wierzchoÄąâ€škĂłw, wspĂłÄąâ€šrzÄ™dnych tekstur i kolorĂłw.
3.  Resetuje licznik `m_size` do zera.
## `void DrawCache::bind()` i `void DrawCache::release()`

Metody te zarzÄ…dzajÄ… bindowaniem i zwalnianiem `FrameBuffer` atlasu. `bind()` jest wywoÄąâ€šywane, gdy do atlasu musi zostaÄ‡ narysowana nowa tekstura. `release()` jest wywoÄąâ€šywane przed wykonaniem `draw()`.
## Metody dodawania do bufora

-   **`addRect(const Rect& dest, const Color& color)`**: Dodaje prostokÄ…t wypeÄąâ€šniony jednolitym kolorem. WspĂłÄąâ€šrzÄ™dne tekstury sÄ… ustawiane na `(-10, -10)`, co jest sygnaÄąâ€šem dla shadera, aby nie uÄąÄ˝ywaÄąâ€š tekstury.
-   **`addTexturedRect(const Rect& dest, const Rect& src, const Color& color)`**: Dodaje teksturowany prostokÄ…t.
-   **`addCoords(CoordsBuffer& coords, const Color& color)`**: Dodaje geometriÄ™ z `CoordsBuffer` (bez tekstury).
-   **`addTexturedCoords(CoordsBuffer& coords, const Point& offset, const Color& color)`**: Dodaje geometriÄ™ z `CoordsBuffer` z teksturÄ…. Przesuwa wspĂłÄąâ€šrzÄ™dne tekstury o podany `offset`, ktĂłry jest pozycjÄ… tekstury w atlasie.
## Metody pomocnicze (`addRectRaw`, `addColorRaw`)

Prywatne metody `inline` do szybkiego zapisu danych do wewnÄ™trznych wektorĂłw (`m_destCoord`, `m_srcCoord`, `m_color`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/drawcache.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/atlas.h`: ÄąĹˇciÄąâ€şle wspĂłÄąâ€špracuje z `g_atlas` w celu bindowania i zwalniania bufora ramki atlasu.
-   `framework/graphics/painter.h`: WywoÄąâ€šuje `g_painter->drawCache()` do finalnego narysowania zgrupowanej geometrii.
-   Jest uÄąÄ˝ywana przez `DrawQueueItem`, aby sprĂłbowaÄ‡ zbuforowaÄ‡ operacjÄ™ rysowania zamiast wykonywaÄ‡ jÄ… natychmiast.

---
# Ä‘Ĺşâ€śâ€ž drawcache.h
## Opis ogĂłlny

Plik `drawcache.h` deklaruje klasÄ™ `DrawCache`, ktĂłra sÄąâ€šuÄąÄ˝y jako bufor dla operacji rysowania. Jest to mechanizm optymalizacyjny, ktĂłry agreguje wiele maÄąâ€šych operacji rysowania (np. prostokÄ…tĂłw) w jedno duÄąÄ˝e wywoÄąâ€šanie, co znaczÄ…co poprawia wydajnoÄąâ€şÄ‡ renderowania.
## Klasa `DrawCache`
## Opis semantyczny
`DrawCache` przechowuje trzy duÄąÄ˝e, prealokowane wektory: na wspĂłÄąâ€šrzÄ™dne wierzchoÄąâ€škĂłw (`m_destCoord`), wspĂłÄąâ€šrzÄ™dne tekstur (`m_srcCoord`) i kolory (`m_color`). Metody `add...` dodajÄ… dane do tych buforĂłw. Gdy bufor jest peÄąâ€šny lub gdy operacja rysowania nie moÄąÄ˝e byÄ‡ zbuforowana, metoda `draw()` jest wywoÄąâ€šywana, aby oprĂłÄąÄ˝niÄ‡ bufor i narysowaÄ‡ jego zawartoÄąâ€şÄ‡ za pomocÄ… jednego wywoÄąâ€šania `g_painter->drawCache()`.
## StaÄąâ€še

-   `MAX_SIZE`: Maksymalna liczba wierzchoÄąâ€škĂłw, jakÄ… moÄąÄ˝e przechowaÄ‡ bufor (65536).
-   `HALF_MAX_SIZE`: PoÄąâ€šowa maksymalnego rozmiaru, uÄąÄ˝ywana jako prĂłg do oprĂłÄąÄ˝nienia bufora.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void draw()` | Rysuje zawartoÄąâ€şÄ‡ bufora na ekranie i go czyÄąâ€şci. |
| `void bind()` | Bindowanie `FrameBuffer` atlasu (gdy trzeba do niego coÄąâ€ş dorysowaÄ‡). |
| `void release()` | Odpinanie `FrameBuffer` atlasu. |
| `bool hasSpace(int size)` | Sprawdza, czy w buforze jest wystarczajÄ…co miejsca na `size` wierzchoÄąâ€škĂłw. |
| `inline int getSize()` | Zwraca aktualnÄ… liczbÄ™ wierzchoÄąâ€škĂłw w buforze. |
| `void addRect(...)` | Dodaje prostokÄ…t wypeÄąâ€šniony kolorem. |
| `void addTexturedRect(...)` | Dodaje teksturowany prostokÄ…t. |
| `void addCoords(...)` | Dodaje geometriÄ™ z `CoordsBuffer` (bez tekstury). |
| `void addTexturedCoords(...)` | Dodaje geometriÄ™ z `CoordsBuffer` (z teksturÄ…). |
## Zmienne prywatne

-   `m_destCoord`: Wektor na wspĂłÄąâ€šrzÄ™dne docelowe (pozycji).
-   `m_srcCoord`: Wektor na wspĂłÄąâ€šrzÄ™dne ÄąĹźrĂłdÄąâ€šowe (tekstury).
-   `m_color`: Wektor na kolory wierzchoÄąâ€škĂłw.
-   `m_bound`: Flaga wskazujÄ…ca, czy atlas jest zbindowany.
-   `m_size`: Aktualna liczba wierzchoÄąâ€škĂłw w buforze.
## Zmienne globalne

-   `g_drawCache`: Globalna instancja `DrawCache`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/atlas.h`: Do zarzÄ…dzania atlasem tekstur.
-   `framework/graphics/coordsbuffer.h`: Do przyjmowania geometrii.
-   `framework/graphics/graphics.h`, `painter.h`: Do operacji renderowania.
-   Jest uÄąÄ˝ywana przez `DrawQueue`, aby grupowaÄ‡ operacje rysowania.

---
# Ä‘Ĺşâ€śâ€ž drawqueue.cpp
## Opis ogĂłlny

Plik `drawqueue.cpp` implementuje logikÄ™ dla `DrawQueue` oraz poszczegĂłlnych typĂłw zadaÄąâ€ž rysowania (`DrawQueueItem`). Jest to centralny element systemu renderowania, ktĂłry kolekcjonuje wszystkie operacje rysowania w jednej klatce, a nastÄ™pnie wykonuje je w odpowiedniej kolejnoÄąâ€şci, z uwzglÄ™dnieniem warunkĂłw takich jak przycinanie, przezroczystoÄąâ€şÄ‡ czy rotacja.
## Zmienne globalne
## `g_drawQueue`

Globalny wskaÄąĹźnik na aktualnie aktywnÄ… kolejkÄ™ rysowania. WÄ…tek logiki tworzy nowe instancje `DrawQueue`, wypeÄąâ€šnia je i przypisuje do tego wskaÄąĹźnika, a wÄ…tek renderowania je konsumuje.
## Klasy `DrawQueueItem` (implementacje)

KaÄąÄ˝da klasa dziedziczÄ…ca po `DrawQueueItem` implementuje dwie kluczowe metody:

-   **`draw()`**: Wykonuje faktycznÄ… operacjÄ™ rysowania za pomocÄ… `g_painter`.
-   **`cache()`**: PrĂłbuje zoptymalizowaÄ‡ operacjÄ™, dodajÄ…c jÄ… do `g_drawCache` zamiast rysowaÄ‡ natychmiast. Zwraca `true`, jeÄąâ€şli keszowanie siÄ™ powiodÄąâ€šo.
## PrzykÄąâ€šady implementacji:

-   **`DrawQueueItemTextureCoords::cache()`**:
    1.  Sprawdza, czy tekstura moÄąÄ˝e byÄ‡ skeszowana.
    2.  Pobiera pozycjÄ™ dla tekstury w atlasie za pomocÄ… `g_atlas.cache()`.
    3.  JeÄąâ€şli tekstury nie byÄąâ€šo w atlasie (`drawNow == true`), rysuje jÄ… do atlasu.
    4.  JeÄąâ€şli w `g_drawCache` jest miejsce, dodaje do niego geometriÄ™ z przesuniÄ™tymi wspĂłÄąâ€šrzÄ™dnymi tekstury.

-   **`DrawQueueItemFilledRect::cache()`**:
    1.  Sprawdza, czy jest miejsce w `g_drawCache`.
    2.  JeÄąâ€şli tak, dodaje prostokÄ…t za pomocÄ… `g_drawCache.addRect()`.

-   **`DrawQueueItemText::draw()`**: WywoÄąâ€šuje `g_text.drawText()`, ktĂłra jest zoptymalizowana do renderowania tekstu.

-   **`DrawQueueCondition...::start()` i `end()`**: ImplementujÄ… zmiany stanu `g_painter` na poczÄ…tku i na koÄąâ€žcu bloku warunkowego. Na przykÄąâ€šad `DrawQueueConditionClip` zmienia i przywraca prostokÄ…t przycinania.
## Klasa `DrawQueue`
## `void DrawQueue::setFrameBuffer(...)`

Konfiguruje `DrawQueue` do renderowania do bufora ramki (off-screen). Ustawia docelowy i ÄąĹźrĂłdÄąâ€šowy prostokÄ…t oraz oblicza skalowanie, jeÄąâ€şli rozmiar bufora przekracza `2048x2048`.
## `void DrawQueue::addText(...)` i `void DrawQueue::addColoredText(...)`

TworzÄ… zadanie rysowania tekstu. Najpierw dodajÄ… tekst do `g_text` (systemu keszujÄ…cego geometriÄ™ tekstu), uzyskujÄ…c hash, a nastÄ™pnie tworzÄ… odpowiedni `DrawQueueItemText`.
## `void DrawQueue::correctOutfit(...)`

Specjalna metoda do skalowania i pozycjonowania wielu `DrawQueueItem` (czÄ™Äąâ€şci stroju postaci), tak aby caÄąâ€šoÄąâ€şÄ‡ zmieÄąâ€şciÄąâ€ša siÄ™ w podanym prostokÄ…cie docelowym, zachowujÄ…c proporcje.
## `void DrawQueue::draw(DrawType drawType)`
## Opis semantyczny
GÄąâ€šĂłwna metoda wykonujÄ…ca wszystkie zebrane zadania rysowania.
## DziaÄąâ€šanie
1.  OkreÄąâ€şla zakres zadaÄąâ€ž do narysowania na podstawie `drawType` (wszystkie, przed mapÄ…, po mapie).
2.  Sortuje warunki (`m_conditions`) po ich pozycjach poczÄ…tkowych.
3.  JeÄąâ€şli ustawiono skalowanie, modyfikuje macierz projekcji `g_painter`.
4.  Iteruje po zadaniach w kolejce (`m_queue`):
    -   Przed kaÄąÄ˝dym zadaniem, aktywuje i dezaktywuje odpowiednie warunki (`start()`/`end()`).
    -   PrĂłbuje skeszowaÄ‡ zadanie za pomocÄ… `item->cache()`.
    -   JeÄąâ€şli keszowanie siÄ™ nie powiedzie, oprĂłÄąÄ˝nia `g_drawCache` i prĂłbuje ponownie.
    -   JeÄąâ€şli ponowne keszowanie siÄ™ nie powiedzie, wykonuje `item->draw()`.
    -   Regularnie oprĂłÄąÄ˝nia `g_drawCache`, gdy osiÄ…gnie poÄąâ€šowÄ™ pojemnoÄąâ€şci.
5.  Po zakoÄąâ€žczeniu pÄ™tli, oprĂłÄąÄ˝nia `g_drawCache` i deaktywuje wszystkie pozostaÄąâ€še warunki.
6.  Przywraca oryginalnÄ… macierz projekcji i stan `g_painter`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   ÄąĹˇciÄąâ€şle wspĂłÄąâ€špracuje z `g_painter`, `g_atlas`, `g_drawCache` i `g_text`, orkiestrujÄ…c proces renderowania.
-   Jest tworzona i wypeÄąâ€šniana przez `UIManager` i inne moduÄąâ€šy logiki gry.
-   Jest konsumowana przez `GraphicalApplication` w wÄ…tku renderowania.

---
# Ä‘Ĺşâ€śâ€ž fontmanager.cpp
## Opis ogĂłlny

Plik `fontmanager.cpp` zawiera implementacjÄ™ klasy `FontManager`, ktĂłra jest singletonem (`g_fonts`) odpowiedzialnym za zarzÄ…dzanie wszystkimi fontami bitmapowymi w aplikacji.
## Zmienne globalne
## `g_fonts`

Globalna instancja `FontManager`.

`$fenceInfo
FontManager g_fonts;
```
## Klasa `FontManager`
## `FontManager::FontManager()`

Konstruktor. Inicjalizuje domyÄąâ€şlny font (`m_defaultFont`) jako pusty obiekt `BitmapFont`, aby uniknÄ…Ä‡ bÄąâ€šÄ™dĂłw, gdy ÄąÄ˝aden font nie zostaÄąâ€š jeszcze zaÄąâ€šadowany.
## `void FontManager::terminate()`

Zwalnia wszystkie zaÄąâ€šadowane fonty, czyszczÄ…c wektor `m_fonts` i resetujÄ…c wskaÄąĹźnik na domyÄąâ€şlny font.
## `void FontManager::clearFonts()`

CzyÄąâ€şci wszystkie zaÄąâ€šadowane fonty i przywraca pusty font domyÄąâ€şlny. UÄąÄ˝ywane np. przy przeÄąâ€šadowywaniu zasobĂłw.
## `void FontManager::importFont(std::string file)`
## Opis semantyczny
ÄąÂaduje definicjÄ™ fontu z pliku `.otfont`. Metoda jest bezpieczna wÄ…tkowo â€“ jeÄąâ€şli jest wywoÄąâ€šana z innego wÄ…tku niÄąÄ˝ graficzny, deleguje zadanie do `g_graphicsDispatcher`.
## DziaÄąâ€šanie
1.  RozwiÄ…zuje Äąâ€şcieÄąÄ˝kÄ™ do pliku.
2.  Parsuje plik OTML.
3.  Odczytuje nazwÄ™ fontu z wÄ™zÄąâ€ša `Font`.
4.  Sprawdza, czy font o tej nazwie juÄąÄ˝ nie istnieje.
5.  Tworzy nowy obiekt `BitmapFont` i wywoÄąâ€šuje jego metodÄ™ `load()`.
6.  Dodaje nowo zaÄąâ€šadowany font do wektora `m_fonts`.
7.  JeÄąâ€şli font jest oznaczony jako domyÄąâ€şlny (`default="true"`), ustawia go jako `m_defaultFont`.
## `bool FontManager::fontExists(const std::string& fontName)`

Sprawdza, czy font o podanej nazwie zostaÄąâ€š juÄąÄ˝ zaÄąâ€šadowany.
## `BitmapFontPtr FontManager::getFont(const std::string& fontName)`

Wyszukuje i zwraca wskaÄąĹźnik do fontu o podanej nazwie. JeÄąâ€şli font nie zostanie znaleziony, loguje bÄąâ€šÄ…d i zwraca font domyÄąâ€şlny, aby zapobiec awarii.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/fontmanager.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/atlas.h`: PoÄąâ€şrednio, przez `BitmapFont`, ktĂłry uÄąÄ˝ywa atlasu do cachowania.
-   `framework/core/eventdispatcher.h`: UÄąÄ˝ywa `g_graphicsDispatcher` do zapewnienia bezpieczeÄąâ€žstwa wÄ…tkowego.
-   `framework/core/resourcemanager.h`: Do znajdowania i odczytywania plikĂłw `.otfont`.
-   `framework/otml/otml.h`: Do parsowania plikĂłw definicji fontĂłw.
-   Jest uÄąÄ˝ywany przez `UIManager` i `UIWidget` do uzyskiwania dostÄ™pu do fontĂłw potrzebnych do renderowania tekstu.

---
# Ä‘Ĺşâ€śâ€ž drawqueue.h
## Opis ogĂłlny

Plik `drawqueue.h` deklaruje hierarchiÄ™ klas `DrawQueueItem` oraz klasÄ™ `DrawQueue`, ktĂłre razem tworzÄ… system kolejkowania operacji rysowania. Jest to centralny mechanizm, ktĂłry pozwala na zbieranie wszystkich poleceÄąâ€ž rysowania w jednej klatce, a nastÄ™pnie ich zoptymalizowane wykonanie.
## Typ wyliczeniowy `DrawType`

OkreÄąâ€şla, ktĂłra czÄ™Äąâ€şÄ‡ kolejki ma zostaÄ‡ narysowana. UÄąÄ˝ywane do renderowania warstwowego (np. interfejs za mapÄ… i przed mapÄ…).

| WartoÄąâ€şÄ‡ | Opis |
| :--- | :--- |
| `DRAW_ALL` | Rysuje caÄąâ€šÄ… kolejkÄ™. |
| `DRAW_BEFORE_MAP` | Rysuje zadania dodane przed `markMapPosition()`. |
| `DRAW_AFTER_MAP` | Rysuje zadania dodane po `markMapPosition()`. |
## Hierarchia klas `DrawQueueItem`
## `struct DrawQueueItem` (baza)
Abstrakcyjna klasa bazowa dla wszystkich zadaÄąâ€ž w kolejce.

-   **`virtual void draw()`**: Metoda wirtualna do wykonania operacji rysowania.
-   **`virtual bool cache()`**: Metoda wirtualna do prĂłby zbuforowania operacji w `DrawCache`.
## Klasy pochodne

KaÄąÄ˝da klasa reprezentuje konkretnÄ… operacjÄ™ rysowania:
-   `DrawQueueItemTexturedRect`: Rysowanie prostokÄ…ta z teksturÄ….
-   `DrawQueueItemTextureCoords`: Rysowanie geometrii z `CoordsBuffer` z teksturÄ….
-   `DrawQueueItemColoredTextureCoords`: Rysowanie geometrii z teksturÄ… i wieloma kolorami.
-   `DrawQueueItemImageWithShader`: Rysowanie geometrii z teksturÄ… i niestandardowym shaderem.
-   `DrawQueueItemFilledRect`: Rysowanie wypeÄąâ€šnionego prostokÄ…ta.
-   `DrawQueueItemClearRect`: Czyszczenie prostokÄ…tnego obszaru.
-   `DrawQueueItemFillCoords`: WypeÄąâ€šnianie geometrii z `CoordsBuffer` kolorem.
-   `DrawQueueItemText`, `DrawQueueItemTextColored`: Rysowanie tekstu.
-   `DrawQueueItemLine`: Rysowanie linii.
## Hierarchia klas `DrawQueueCondition`
## `struct DrawQueueCondition` (baza)
Abstrakcyjna klasa bazowa dla warunkĂłw modyfikujÄ…cych stan renderowania dla grupy zadaÄąâ€ž.

-   **`m_start`, `m_end`**: Indeksy w `DrawQueue` okreÄąâ€şlajÄ…ce zakres dziaÄąâ€šania warunku.
-   **`virtual void start(DrawQueue*)`**: Metoda wywoÄąâ€šywana przed pierwszym zadaniem objÄ™tym warunkiem.
-   **`virtual void end(DrawQueue*)`**: Metoda wywoÄąâ€šywana po ostatnim zadaniu objÄ™tym warunkiem.
## Klasy pochodne

-   `DrawQueueConditionClip`: Ustawia prostokÄ…t przycinania (clipping).
-   `DrawQueueConditionRotation`: Stosuje transformacjÄ™ rotacji.
-   `DrawQueueConditionMark`: Specjalny warunek do rysowania zaznaczenia (np. na przedmiotach).
## Klasa `DrawQueue`
## Opis semantyczny
GÄąâ€šĂłwna klasa zarzÄ…dzajÄ…ca kolejkÄ…. Przechowuje listÄ™ zadaÄąâ€ž (`m_queue`) i warunkĂłw (`m_conditions`). Dostarcza metody do dodawania rĂłÄąÄ˝nych operacji rysowania i do finalnego wykonania caÄąâ€šej kolejki.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void draw(DrawType)` | Wykonuje wszystkie (lub czÄ™Äąâ€şÄ‡) operacje rysowania z kolejki. |
| `add...(...)` | Metody do dodawania rĂłÄąÄ˝nych typĂłw `DrawQueueItem` do kolejki. |
| `setFrameBuffer(...)` | Konfiguruje renderowanie do bufora ramki. |
| `setOpacity(start, opacity)` | Stosuje przezroczystoÄąâ€şÄ‡ do zadaÄąâ€ž od indeksu `start`. |
| `setClip(start, clip)` | Dodaje warunek `DrawQueueConditionClip` dla zadaÄąâ€ž od `start`. |
# Ä‘Ĺşâ€śâ€ž framebuffer.cpp
## Opis ogĂłlny

Plik `framebuffer.cpp` zawiera implementacjÄ™ klasy `FrameBuffer`, ktĂłra jest opakowaniem (wrapperem) na obiekt bufora ramki (FBO) w OpenGL. UmoÄąÄ˝liwia renderowanie sceny do tekstury zamiast bezpoÄąâ€şrednio na ekran (tzw. off-screen rendering), co jest kluczowe dla efektĂłw post-processingu, skalowania interfejsu i implementacji atlasu tekstur.
## Zmienne globalne
## `uint FrameBuffer::boundFbo`

Statyczna zmienna czÄąâ€šonkowska, ktĂłra Äąâ€şledzi ID aktualnie zwiÄ…zanego (aktywnego) FBO. SÄąâ€šuÄąÄ˝y do optymalizacji poprzez unikanie zbÄ™dnych wywoÄąâ€šaÄąâ€žsk `glBindFramebuffer`, jeÄąâ€şli ten sam FBO jest juÄąÄ˝ aktywny.

`$fenceInfo
uint FrameBuffer::boundFbo = 0;
```
## Klasa `FrameBuffer`
## `FrameBuffer::FrameBuffer(bool withDepth)`

Konstruktor. WywoÄąâ€šuje `internalCreate()` w celu utworzenia zasobĂłw OpenGL.
-   **Parametr `withDepth`**: JeÄąâ€şli `true` i zdefiniowano `WITH_DEPTH_BUFFER`, tworzony jest rĂłwnieÄąÄ˝ bufor gÄąâ€šÄ™bi, co pozwala na testowanie gÄąâ€šÄ™bi podczas renderowania do tego bufora.
## `FrameBuffer::~FrameBuffer()`

Destruktor. Zwalnia zasoby OpenGL (`glDeleteFramebuffers`, `glDeleteRenderbuffers`) w sposĂłb bezpieczny wÄ…tkowo, dodajÄ…c zadanie do kolejki dyspozytora graficznego (`g_graphicsDispatcher`).
## `void FrameBuffer::resize(const Size& size)`
## Opis semantyczny
Zmienia rozmiar bufora ramki. Tworzy nowÄ… teksturÄ™ o podanych wymiarach, ktĂłra bÄ™dzie sÄąâ€šuÄąÄ˝yÄ‡ jako "pÄąâ€šĂłtno" do rysowania.
## DziaÄąâ€šanie
1.  Sprawdza, czy zmiana rozmiaru jest konieczna.
2.  Tworzy nowy obiekt `Texture` o podanym rozmiarze.
3.  JeÄąâ€şli bufor gÄąâ€šÄ™bi jest wÄąâ€šÄ…czony, alokuje dla niego pamiÄ™Ä‡ (`glRenderbufferStorage`).
4.  WiÄ…ÄąÄ˝e FBO, a nastÄ™pnie doÄąâ€šÄ…cza do niego nowÄ… teksturÄ™ jako bufor koloru (`glFramebufferTexture2D`) oraz opcjonalnie bufor gÄąâ€šÄ™bi (`glFramebufferRenderbuffer`).
5.  Sprawdza status FBO (`glCheckFramebufferStatus`), aby upewniÄ‡ siÄ™, ÄąÄ˝e jest on kompletny i gotowy do uÄąÄ˝ycia.
## `void FrameBuffer::bind(const FrameBufferPtr& depthFramebuffer)`

Aktywuje bufor ramki jako cel renderowania. Wszystkie kolejne operacje rysowania bÄ™dÄ… kierowane do tekstury tego bufora.
-   Zapisuje i resetuje stan `Painter`.
-   WywoÄąâ€šuje `internalBind()`.
-   Ustawia rozdzielczoÄąâ€şÄ‡ `Painter` na rozmiar bufora.
## `void FrameBuffer::release()`

Deaktywuje bufor ramki i przywraca poprzedni cel renderowania (zazwyczaj bufor ekranu).
-   WywoÄąâ€šuje `internalRelease()`.
-   Przywraca poprzedni stan `Painter`.
## `void FrameBuffer::draw(...)`

Metody te sÄąâ€šuÄąÄ˝Ä… do rysowania *zawartoÄąâ€şci* (tekstury) bufora ramki na aktualnie aktywnym celu renderowania.
-   `draw()`: Rysuje caÄąâ€šÄ… teksturÄ™.
-   `draw(const Rect& dest, const Rect& src)`: Rysuje fragment (`src`) tekstury w docelowym prostokÄ…cie (`dest`).
## `void FrameBuffer::doScreenshot(std::string fileName)`

Odczytuje zawartoÄąâ€şÄ‡ pikseli z bufora ramki za pomocÄ… `glReadPixels`, a nastÄ™pnie w osobnym wÄ…tku (`g_asyncDispatcher`) zapisuje je do pliku PNG, odwracajÄ…c obraz w osi Y (konwersja z ukÄąâ€šadu wspĂłÄąâ€šrzÄ™dnych OpenGL).
## Metody `internal...`

-   `internalCreate()`: Generuje obiekty FBO i RBO.
-   `internalBind()` / `internalRelease()`: BezpoÄąâ€şrednio wywoÄąâ€šujÄ… `glBindFramebuffer` i zarzÄ…dzajÄ… statycznÄ… zmiennÄ… `boundFbo`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/framebuffer.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bÄąâ€šÄ™dĂłw OpenGL i dostÄ™pu do `g_graphics`.
-   `framework/graphics/texture.h`: `FrameBuffer` uÄąÄ˝ywa obiektu `Texture` jako swojego bufora koloru.
-   `framework/platform/platformwindow.h`: DostÄ™p do `g_window` (potencjalnie).
-   `framework/core/asyncdispatcher.h`: UÄąÄ˝ywany do asynchronicznego zapisu zrzutĂłw ekranu.
-   Jest zarzÄ…dzana przez `FrameBufferManager`.

---
# Ä‘Ĺşâ€śâ€ž framebuffer.h
## Opis ogĂłlny

Plik `framebuffer.h` deklaruje klasÄ™ `FrameBuffer`, ktĂłra jest obiektowym interfejsem do zarzÄ…dzania buforami ramki (FBO) w OpenGL. Pozwala na renderowanie sceny do tekstury zamiast bezpoÄąâ€şrednio na ekran.
## Klasa `FrameBuffer`
## Opis semantyczny
`FrameBuffer` enkapsuluje obiekt FBO z OpenGL oraz powiÄ…zanÄ… z nim teksturÄ™ (jako bufor koloru) i opcjonalnie bufor gÄąâ€šÄ™bi. UdostÄ™pnia metody do bindowania (aktywacji), zwalniania, zmiany rozmiaru i rysowania zawartoÄąâ€şci bufora.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `FrameBuffer(bool withDepth = false)` | Konstruktor. |
| `virtual ~FrameBuffer()` | Destruktor. |
| `void resize(const Size& size)` | Zmienia rozmiar bufora i powiÄ…zanej tekstury. |
| `void bind(...)` | Ustawia ten bufor jako aktywny cel renderowania. |
| `void release()` | Przywraca poprzedni cel renderowania. |
| `void draw()` / `draw(const Rect& dest)` / `draw(...)` | Rysuje teksturÄ™ tego bufora na aktualnie aktywnym celu. |
| `void setSmooth(bool enabled)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza wygÄąâ€šadzanie (filtrowanie liniowe) dla tekstury bufora. |
| `TexturePtr getTexture()` | Zwraca wskaÄąĹźnik do tekstury, do ktĂłrej renderuje bufor. |
| `Size getSize()` | Zwraca rozmiar bufora. |
| `bool isSmooth()` | Zwraca stan wygÄąâ€šadzania. |
| `uint getDepthRenderBuffer()` | (Tylko z `WITH_DEPTH_BUFFER`) Zwraca ID bufora gÄąâ€šÄ™bi. |
| `bool hasDepth()` | (Tylko z `WITH_DEPTH_BUFFER`) Zwraca `true`, jeÄąâ€şli bufor posiada bufor gÄąâ€šÄ™bi. |
| `std::vector<uint32_t> readPixels()` | Odczytuje zawartoÄąâ€şÄ‡ bufora do pamiÄ™ci systemowej. |
| `void doScreenshot(std::string fileName)` | Zapisuje zawartoÄąâ€şÄ‡ bufora do pliku PNG. |
## Zmienne prywatne

-   `m_texture`: WskaÄąĹźnik na obiekt `Texture` uÄąÄ˝ywany jako bufor koloru.
-   `m_fbo`: ID obiektu FBO w OpenGL.
-   `m_prevBoundFbo`: Przechowuje ID poprzednio aktywnego FBO, aby moÄąÄ˝na byÄąâ€šo go przywrĂłciÄ‡.
-   `m_smooth`: Flaga wygÄąâ€šadzania.
-   `m_depthRbo`, `m_depth`: (Tylko z `WITH_DEPTH_BUFFER`) ID bufora gÄąâ€šÄ™bi i flaga jego istnienia.
-   `boundFbo`: Statyczna zmienna Äąâ€şledzÄ…ca globalnie aktywny FBO.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Definicje typĂłw, np. `TexturePtr`.
-   `framework/graphics/texture.h`: Wymaga peÄąâ€šnej definicji `Texture`.
-   Jest tworzona i zarzÄ…dzana przez `FrameBufferManager`. UÄąÄ˝ywana przez `Painter`, `Atlas` i w gÄąâ€šĂłwnej pÄ™tli renderowania w `GraphicalApplication`.

---
# Ä‘Ĺşâ€śâ€ž framebuffermanager.cpp
## Opis ogĂłlny

Plik `framebuffermanager.cpp` zawiera implementacjÄ™ klasy `FrameBufferManager`, ktĂłra jest singletonem (`g_framebuffers`) odpowiedzialnym za tworzenie i zarzÄ…dzanie obiektami `FrameBuffer`.
## Zmienne globalne
## `g_framebuffers`

Globalna instancja `FrameBufferManager`.

`$fenceInfo
FrameBufferManager g_framebuffers;
```
## Klasa `FrameBufferManager`
## `void FrameBufferManager::init()`
## Opis semantyczny
Inicjalizuje menedÄąÄ˝era. Tworzy dwa predefiniowane, "tymczasowe" bufory ramki, ktĂłre mogÄ… byÄ‡ uÄąÄ˝ywane przez rĂłÄąÄ˝ne czÄ™Äąâ€şci systemu do krĂłtkotrwaÄąâ€šych operacji renderowania poza ekranem, bez potrzeby tworzenia i niszczenia wÄąâ€šasnych buforĂłw.

-   `m_temporaryFramebuffer`: OgĂłlnego przeznaczenia.
-   `m_drawQueueTemporaryFramebuffer`: Prawdopodobnie uÄąÄ˝ywany przez `DrawQueue` do specyficznych operacji.
## `void FrameBufferManager::terminate()`

Zwalnia wszystkie utworzone bufory ramki, w tym tymczasowe, czyszczÄ…c listÄ™ `m_framebuffers`.
## `FrameBufferPtr FrameBufferManager::createFrameBuffer(bool withDepth)`
## Opis semantyczny
Metoda fabryczna do tworzenia nowych obiektĂłw `FrameBuffer`.
## DziaÄąâ€šanie
1.  Tworzy nowÄ… instancjÄ™ `FrameBuffer`, przekazujÄ…c flagÄ™ `withDepth`.
2.  Dodaje nowo utworzony bufor do wewnÄ™trznej listy `m_framebuffers` w celu Äąâ€şledzenia.
3.  Zwraca wskaÄąĹźnik na nowo utworzony obiekt.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/framebuffermanager.h`: Plik nagÄąâ€šĂłwkowy.
-   Klasa ta jest uÄąÄ˝ywana przez `Atlas` do tworzenia swoich "pÄąâ€šĂłcien" oraz przez `GraphicalApplication` do tworzenia buforĂłw dla gÄąâ€šĂłwnej sceny i mapy.

---
# Ä‘Ĺşâ€śâ€ž graph.cpp
## Opis ogĂłlny

Plik `graph.cpp` implementuje klasÄ™ `Graph`, ktĂłra sÄąâ€šuÄąÄ˝y do wizualizacji danych w czasie rzeczywistym w formie prostego wykresu liniowego. Jest to narzÄ™dzie gÄąâ€šĂłwnie do celĂłw debugowania i profilowania wydajnoÄąâ€şci.
## Zmienne globalne
## `g_graphs[GRAPH_LAST + 1]`

Globalna tablica instancji `Graph`, gdzie kaÄąÄ˝da instancja odpowiada za Äąâ€şledzenie i rysowanie innego parametru (np. czasu klatki, liczby wywoÄąâ€šaÄąâ€ž rysujÄ…cych, opĂłÄąĹźnienia sieciowego).

`$fenceInfo
Graph g_graphs[GRAPH_LAST + 1] = {
    {"Total frame time"},
    // ... inne definicje
};
```
## Klasa `Graph`
## `Graph::Graph(const std::string& name, size_t capacity)`

Konstruktor. Inicjalizuje wykres z podanÄ… nazwÄ… i maksymalnÄ… liczbÄ… prĂłbek do przechowywania.
## `void Graph::draw(const Rect& dest)`
## Opis semantyczny
Rysuje wykres w podanym prostokÄ…cie ekranu. Metoda musi byÄ‡ wywoÄąâ€šywana z wÄ…tku graficznego.
## DziaÄąâ€šanie
1.  Rysuje tÄąâ€šo i ramkÄ™ wykresu.
2.  Rysuje nazwÄ™ wykresu.
3.  Pobiera `elements` ostatnich prĂłbek z `m_values` (tyle, ile zmieÄąâ€şci siÄ™ w `dest`).
4.  Znajduje minimalnÄ… i maksymalnÄ… wartoÄąâ€şÄ‡ w pobranym zakresie.
5.  Normalizuje wartoÄąâ€şci i tworzy geometriÄ™ linii wykresu.
6.  Rysuje etykiety z wartoÄąâ€şciÄ… minimalnÄ…, maksymalnÄ… i ostatniÄ….
7.  Rysuje liniÄ™ wykresu za pomocÄ… `g_painter->drawLine()`.
## `void Graph::clear()`

CzyÄąâ€şci wszystkie zebrane dane z wykresu.
## `void Graph::addValue(int value, bool ignoreSmallValues)`
## Opis semantyczny
Dodaje nowÄ… prĂłbkÄ™ danych do wykresu. Metoda jest bezpieczna wÄ…tkowo dziÄ™ki uÄąÄ˝yciu `std::mutex`.
## DziaÄąâ€šanie
1.  Opcjonalnie ignoruje maÄąâ€še, powtarzajÄ…ce siÄ™ wartoÄąâ€şci, aby wykres byÄąâ€š bardziej czytelny.
2.  Dodaje nowÄ… wartoÄąâ€şÄ‡ na koniec kolejki `m_values`.
3.  JeÄąâ€şli kolejka przekracza pojemnoÄąâ€şÄ‡, usuwa najstarszÄ… wartoÄąâ€şÄ‡.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/graph.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/painter.h`: UÄąÄ˝ywa `g_painter` do rysowania.
-   `framework/graphics/textrender.h`: UÄąÄ˝ywa `g_text` do rysowania etykiet.
-   `framework/core/eventdispatcher.h`: UÄąÄ˝ywany do walidacji wÄ…tku.
-   Jest uÄąÄ˝ywana w rĂłÄąÄ˝nych czÄ™Äąâ€şciach aplikacji (`GraphicalApplication`, `Protocol`) do zbierania danych o wydajnoÄąâ€şci, ktĂłre sÄ… nastÄ™pnie rysowane w gÄąâ€šĂłwnej pÄ™tli renderowania.

---
# Ä‘Ĺşâ€śâ€ž graph.h
## Opis ogĂłlny

Plik `graph.h` deklaruje klasÄ™ `Graph` oraz powiÄ…zane z niÄ… typy wyliczeniowe. Jest to narzÄ™dzie do wizualizacji danych w czasie rzeczywistym, przeznaczone do debugowania i profilowania.
## Typ wyliczeniowy `GraphType`

Definiuje staÄąâ€še dla rĂłÄąÄ˝nych typĂłw wykresĂłw, ktĂłre mogÄ… byÄ‡ Äąâ€şledzone w aplikacji.

| Nazwa | Opis |
| :--- | :--- |
| `GRAPH_TOTAL_FRAME_TIME` | CaÄąâ€škowity czas klatki. |
| `GRAPH_CPU_FRAME_TIME` | Czas renderowania po stronie CPU. |
| `GRAPH_GPU_CALLS` | Liczba wywoÄąâ€šaÄąâ€ž do API graficznego. |
| `GRAPH_GPU_DRAWS` | Liczba operacji rysowania. |
| `GRAPH_PROCESSING_POLL` | Czas przetwarzania zdarzeÄąâ€ž w wÄ…tku logiki. |
| `GRAPH_GRAPHICS_POLL` | Czas przetwarzania zdarzeÄąâ€ž w wÄ…tku graficznym. |
| `GRAPH_DISPATCHER_EVENTS` | Liczba zdarzeÄąâ€ž w gÄąâ€šĂłwnym dyspozytorze. |
| `GRAPH_GRAPHICS_EVENTS` | Liczba zdarzeÄąâ€ž w dyspozytorze graficznym. |
| `GRAPH_LATENCY` | OpĂłÄąĹźnienie sieciowe (ping). |
## Klasa `Graph`
## Opis semantyczny
Klasa `Graph` przechowuje kolejkÄ™ (`std::deque`) ostatnich wartoÄąâ€şci liczbowych i udostÄ™pnia metodÄ™ do narysowania ich w postaci prostego wykresu liniowego. Jest bezpieczna wÄ…tkowo przy dodawaniu wartoÄąâ€şci.
## StaÄąâ€še

-   `MAX_CAPACITY`: Maksymalna liczba prĂłbek, jakÄ… moÄąÄ˝e przechowaÄ‡ wykres.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Graph(...)` | Konstruktor. |
| `void draw(const Rect& dest)` | Rysuje wykres w podanym prostokÄ…cie. |
| `void clear()` | CzyÄąâ€şci dane wykresu. |
| `void addValue(int value, bool ignoreSmallValues = false)` | Dodaje nowÄ… wartoÄąâ€şÄ‡ do wykresu. |
## Zmienne prywatne

-   `m_name`: Nazwa wykresu, wyÄąâ€şwietlana jako tytuÄąâ€š.
-   `m_capacity`: Maksymalna liczba przechowywanych prĂłbek.
-   `m_ignores`: Licznik ignorowanych maÄąâ€šych wartoÄąâ€şci.
-   `m_values`: Kolejka przechowujÄ…ca dane.
-   `m_mutex`: Mutex chroniÄ…cy dostÄ™p do `m_values`.
## Zmienne globalne

-   `g_graphs[GRAPH_LAST + 1]`: Globalna tablica, w ktĂłrej przechowywane sÄ… instancje `Graph` dla kaÄąÄ˝dego typu z `GraphType`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   Jest uÄąÄ˝ywana przez `GraphicalApplication` do rysowania informacji debugowania. Dane sÄ… do niej dodawane z rĂłÄąÄ˝nych czÄ™Äąâ€şci systemu, np. z pÄ™tli gÄąâ€šĂłwnej, `Painter`, `EventDispatcher`, `Protocol`.

---
# Ä‘Ĺşâ€śâ€ž glutil.h
## Opis ogĂłlny

Plik `glutil.h` (GL Utility) jest plikiem nagÄąâ€šĂłwkowym, ktĂłrego jedynym zadaniem jest wÄąâ€šÄ…czenie odpowiednich nagÄąâ€šĂłwkĂłw OpenGL, OpenGL ES, EGL lub GLEW, w zaleÄąÄ˝noÄąâ€şci od platformy i opcji kompilacji. DziaÄąâ€ša jako centralny punkt doÄąâ€šÄ…czania bibliotek graficznych, co upraszcza zarzÄ…dzanie zaleÄąÄ˝noÄąâ€şciami w innych plikach.
## Logika warunkowego doÄąâ€šÄ…czania

Plik uÄąÄ˝ywa dyrektyw preprocesora do wyboru odpowiednich nagÄąâ€šĂłwkĂłw:

1.  **Android lub Emscripten (`ANDROID` || `__EMSCRIPTEN__`)**:
    -   DoÄąâ€šÄ…czane sÄ… nagÄąâ€šĂłwki **OpenGL ES 2.0** (`<GLES2/gl2.h>`, `<GLES2/gl2ext.h>`) oraz **EGL** (`<EGL/egl.h>`, `<EGL/eglext.h>`). EGL jest interfejsem, ktĂłry Äąâ€šÄ…czy API renderowania (jak OpenGL ES) z natywnym systemem okienkowym platformy.

2.  **Inne platformy z `OPENGL_ES`**:
    -   Podobnie jak wyÄąÄ˝ej, doÄąâ€šÄ…czane sÄ… nagÄąâ€šĂłwki OpenGL ES 2.0 i EGL. Definiowane sÄ… rĂłwnieÄąÄ˝ makra `GL_GLEXT_PROTOTYPES`, `EGL_EGL_PROTOTYPES`, aby zapewniÄ‡ dostÄ™p do prototypĂłw funkcji.

3.  **DomyÄąâ€şlnie (Desktop - Windows/Linux/macOS)**:
    -   DoÄąâ€šÄ…czana jest biblioteka **GLEW** (`<GL/glew.h>`). GLEW (OpenGL Extension Wrangler) jest bibliotekÄ…, ktĂłra upraszcza zarzÄ…dzanie i Äąâ€šadowanie rozszerzeÄąâ€ž OpenGL, co jest konieczne na platformach desktopowych.
    -   Na systemach innych niÄąÄ˝ Windows, `GLEW_STATIC` jest definiowane, aby linkowaÄ‡ GLEW statycznie.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Ten plik nie ma zaleÄąÄ˝noÄąâ€şci od innych plikĂłw projektu.
-   Jest doÄąâ€šÄ…czany przez `framework/graphics/declarations.h`, co sprawia, ÄąÄ˝e definicje OpenGL sÄ… dostÄ™pne we wszystkich plikach moduÄąâ€šu graficznego.

---
# Ä‘Ĺşâ€śâ€ž graphics.cpp
## Opis ogĂłlny

Plik `graphics.cpp` zawiera implementacjÄ™ klasy `Graphics`, ktĂłra jest singletonem (`g_graphics`) odpowiedzialnym za inicjalizacjÄ™ i zarzÄ…dzanie globalnym stanem silnika graficznego opartego na OpenGL.
## Zmienne globalne
## `g_graphics`

Globalna instancja `Graphics`.

`$fenceInfo
Graphics g_graphics;
```
## Klasa `Graphics`
## `Graphics::Graphics()`

Konstruktor. Inicjalizuje domyÄąâ€şlnÄ… maksymalnÄ… wielkoÄąâ€şÄ‡ tekstury na `2048`.
## `void Graphics::init()`
## Opis semantyczny
GÄąâ€šĂłwna metoda inicjalizujÄ…ca. Uruchamia i konfiguruje kontekst OpenGL oraz inicjalizuje wszystkie pod-menedÄąÄ˝ery graficzne.
## DziaÄąâ€šanie
1.  Odczytuje i zapisuje informacje o sterowniku graficznym (`GL_VENDOR`, `GL_RENDERER`, `GL_VERSION`, `GL_EXTENSIONS`) za pomocÄ… `glGetString`.
2.  Loguje te informacje.
3.  **Na platformach desktopowych**:
    -   Sprawdza, czy wersja OpenGL jest co najmniej 2.0.
    -   Inicjalizuje GLEW (`glewInit()`).
    -   Sprawdza, czy dostÄ™pne sÄ… rozszerzenia FBO (Framebuffer Object) i w razie potrzeby mapuje funkcje `...EXT` na standardowe nazwy.
4.  WÄąâ€šÄ…cza globalnie mieszanie kolorĂłw (`glEnable(GL_BLEND)`).
5.  Pobiera maksymalny obsÄąâ€šugiwany rozmiar tekstury z `GL_MAX_TEXTURE_SIZE`.
6.  (Opcjonalnie) Sprawdza wsparcie dla bufora gÄąâ€šÄ™bi.
7.  Ustawia flagÄ™ `m_ok` na `true`, sygnalizujÄ…c pomyÄąâ€şlnÄ… inicjalizacjÄ™.
8.  Tworzy i bindowanie globalny obiekt `Painter`.
9.  Inicjalizuje menedÄąÄ˝ery: `g_textures`, `g_framebuffers`, `g_atlas`, `g_text`.
## `void Graphics::terminate()`

Zwalnia zasoby w odwrotnej kolejnoÄąâ€şci do inicjalizacji, wywoÄąâ€šujÄ…c `terminate()` na wszystkich pod-menedÄąÄ˝erach oraz niszczÄ…c obiekt `Painter`.
## `void Graphics::resize(const Size& size)`

Aktualizuje rozmiar viewportu. Ustawia `m_viewportSize` i przekazuje nowy rozmiar do `g_painter`, ktĂłry z kolei aktualizuje macierz projekcji i `glViewport`.
## `void Graphics::checkForError(...)`

Metoda pomocnicza, ktĂłra sprawdza bÄąâ€šÄ™dy OpenGL za pomocÄ… `glGetError()`. JeÄąâ€şli wystÄ…piÄąâ€š bÄąâ€šÄ…d, loguje go wraz z informacjÄ… o funkcji, pliku i numerze linii, w ktĂłrej zostaÄąâ€š wykryty. W trybie debugowania powoduje to bÄąâ€šÄ…d krytyczny.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/graphics.h`: Plik nagÄąâ€šĂłwkowy.
-   `fontmanager.h`, `painter.h`, `atlas.h`, `texturemanager.h`, `framebuffermanager.h`, `textrender.h`: Inicjalizuje i zarzÄ…dza tymi kluczowymi komponentami graficznymi.
-   `framework/platform/platformwindow.h`: PoÄąâ€şrednio, poprzez `g_window`, od ktĂłrego zaleÄąÄ˝y kontekst OpenGL.
-   Jest to centralna klasa-menedÄąÄ˝er dla caÄąâ€šego podsystemu graficznego.

---
# Ä‘Ĺşâ€śâ€ž graphics.h
## Opis ogĂłlny

Plik `graphics.h` deklaruje interfejs klasy `Graphics`, ktĂłra jest singletonem (`g_graphics`) zarzÄ…dzajÄ…cym globalnym stanem i inicjalizacjÄ… silnika graficznego.
## Klasa `Graphics`
## Opis semantyczny
`Graphics` peÄąâ€šni rolÄ™ gÄąâ€šĂłwnego menedÄąÄ˝era podsystemu graficznego. Odpowiada za inicjalizacjÄ™ OpenGL/GLES, odpytywanie o moÄąÄ˝liwoÄąâ€şci sprzÄ™towe (wersja, rozszerzenia, maksymalny rozmiar tekstury) oraz za zarzÄ…dzanie cyklem ÄąÄ˝ycia innych menedÄąÄ˝erĂłw graficznych, takich jak `Painter`, `TextureManager` czy `FontManager`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Graphics()` | Konstruktor. |
| `void init()` | Inicjalizuje silnik graficzny (kontekst OpenGL, menedÄąÄ˝ery). |
| `void terminate()` | Zwalnia zasoby silnika graficznego. |
| `void resize(const Size& size)` | Aktualizuje rozmiar viewportu. |
| `void checkDepthSupport()`| Sprawdza wsparcie dla bufora gÄąâ€šÄ™bi. |
| `int getMaxTextureSize()` | Zwraca maksymalny obsÄąâ€šugiwany rozmiar tekstury. |
| `const Size& getViewportSize()` | Zwraca aktualny rozmiar viewportu (okna/ekranu). |
| `std::string getVendor()` | Zwraca nazwÄ™ producenta karty graficznej. |
| `std::string getRenderer()` | Zwraca nazwÄ™ modelu karty graficznej/sterownika. |
| `std::string getVersion()` | Zwraca wersjÄ™ OpenGL. |
| `std::string getExtensions()` | Zwraca listÄ™ dostÄ™pnych rozszerzeÄąâ€ž OpenGL. |
| `bool ok()` | Zwraca `true`, jeÄąâ€şli inicjalizacja grafiki przebiegÄąâ€ša pomyÄąâ€şlnie. |
| `void checkForError(...)` | Sprawdza i loguje bÄąâ€šÄ™dy OpenGL. |
## Zmienne prywatne

-   `m_viewportSize`: Aktualny rozmiar obszaru renderowania.
-   `m_vendor`, `m_renderer`, `m_version`, `m_extensions`: Informacje o sterowniku graficznym.
-   `m_maxTextureSize`: Maksymalny rozmiar tekstury obsÄąâ€šugiwany przez sprzÄ™t.
-   `m_ok`: Flaga pomyÄąâ€şlnej inicjalizacji.
## Zmienne globalne

-   `g_graphics`: Globalna instancja `Graphics`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`, `painter.h`: Podstawowe deklaracje i klasa `Painter`.
-   Jest oznaczona jako `@bindsingleton g_graphics`, co udostÄ™pnia jej metody (np. `getVendor`) w Lua.
-   Jest inicjalizowana i zamykana przez `GraphicalApplication`.

---
# Ä‘Ĺşâ€śâ€ž image.cpp
## Opis ogĂłlny

Plik `image.cpp` zawiera implementacjÄ™ klasy `Image`, ktĂłra reprezentuje obraz rastrowy w pamiÄ™ci RAM. Jest to podstawowa klasa do Äąâ€šadowania, manipulowania i zapisywania danych obrazĂłw, zanim zostanÄ… one przesÄąâ€šane do pamiÄ™ci karty graficznej jako tekstury.
## Klasa `Image`
## `Image::Image(const Size& size, int bpp, uint8 *pixels)`

Konstruktor. Tworzy obiekt `Image` o podanych wymiarach i gÄąâ€šÄ™bi bitowej (bpp - bits per pixel). Opcjonalnie kopiuje dane pikseli z podanego bufora.
## `ImagePtr Image::load(std::string file)`

Statyczna metoda fabryczna do Äąâ€šadowania obrazu z pliku. Obecnie obsÄąâ€šuguje tylko format PNG, wywoÄąâ€šujÄ…c `loadPNG`.
## `ImagePtr Image::loadPNG(...)`

Statyczne metody do Äąâ€šadowania obrazu w formacie PNG z pliku lub z bufora w pamiÄ™ci. UÄąÄ˝ywajÄ… funkcji `load_apng` z `apngloader.cpp` do parsowania danych.
## `void Image::savePNG(const std::string& fileName)`

Zapisuje obraz do pliku w formacie PNG, uÄąÄ˝ywajÄ…c funkcji `save_png` z `apngloader.cpp`.
## `void Image::blit(const Point& dest, const ImagePtr& other)`

Kopiuje piksele z innego obrazu (`other`) do tego obrazu w podane miejsce (`dest`). Kopiowanie odbywa siÄ™ z uwzglÄ™dnieniem przezroczystoÄąâ€şci â€“ piksele w peÄąâ€šni przezroczyste w obrazie ÄąĹźrĂłdÄąâ€šowym nie sÄ… kopiowane.
## `void Image::paste(const ImagePtr& other)`

NakÄąâ€šada inny obraz (`other`) na ten obraz, zastÄ™pujÄ…c istniejÄ…ce piksele. Nie uwzglÄ™dnia przezroczystoÄąâ€şci.
## `ImagePtr Image::upscale()`

Tworzy i zwraca nowy obraz, ktĂłry jest dwukrotnie wiÄ™kszy od oryginalnego. KaÄąÄ˝dy piksel z obrazu ÄąĹźrĂłdÄąâ€šowego jest powielany do bloku 2x2 w obrazie docelowym (skalowanie metodÄ… "najbliÄąÄ˝szego sÄ…siada").
## `bool Image::nextMipmap()`

Generuje nastÄ™pny, mniejszy poziom mipmapy na podstawie bieÄąÄ˝Ä…cych danych pikseli. Oblicza Äąâ€şredniÄ… z bloku 2x2 pikseli, aby stworzyÄ‡ jeden piksel dla mniejszego obrazu. Jest to prosta implementacja filtrowania biliniowego. Zwraca `false`, gdy obraz osiÄ…gnie rozmiar 1x1.
## `ImagePtr Image::fromQRCode(const std::string& code, int border)`

Statyczna metoda fabryczna, ktĂłra generuje obraz kodu QR na podstawie podanego tekstu, uÄąÄ˝ywajÄ…c biblioteki `qrcodegen`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/image.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/resourcemanager.h`: Do otwierania i odczytywania plikĂłw obrazĂłw.
-   `framework/graphics/apngloader.h`: Do obsÄąâ€šugi formatu PNG/APNG.
-   `framework/util/qrcodegen.h`: Do generowania kodĂłw QR.
-   Obiekty `Image` sÄ… zazwyczaj krĂłtkotrwaÄąâ€še â€“ istniejÄ… od momentu zaÄąâ€šadowania z pliku do momentu utworzenia z nich obiektu `Texture` i przesÄąâ€šania danych do GPU.

---
# Ä‘Ĺşâ€śâ€ž hardwarebuffer.h
## Opis ogĂłlny

Plik `hardwarebuffer.h` deklaruje klasÄ™ `HardwareBuffer`, ktĂłra jest opakowaniem na sprzÄ™towe bufory wierzchoÄąâ€škĂłw (Vertex Buffer Objects - VBO) w OpenGL. UmoÄąÄ˝liwia przechowywanie danych geometrycznych (np. wspĂłÄąâ€šrzÄ™dnych wierzchoÄąâ€škĂłw) w pamiÄ™ci karty graficznej w celu uzyskania wysokiej wydajnoÄąâ€şci renderowania.
## Klasa `HardwareBuffer`
## Opis semantyczny
`HardwareBuffer` enkapsuluje ID bufora VBO w OpenGL i dostarcza podstawowe metody do jego obsÄąâ€šugi: bindowania, odpinania i zapisu danych. UÄąÄ˝ycie VBO jest znacznie wydajniejsze niÄąÄ˝ przesyÄąâ€šanie danych wierzchoÄąâ€škĂłw z pamiÄ™ci RAM do GPU w kaÄąÄ˝dej klatce.
## Typy wyliczeniowe (Enums)

-   **`enum Type`**: OkreÄąâ€şla typ bufora.
    -   `VertexBuffer` (`GL_ARRAY_BUFFER`): Przechowuje atrybuty wierzchoÄąâ€škĂłw (np. pozycje, kolory, wspĂłÄąâ€šrzÄ™dne tekstur).
    -   `IndexBuffer` (`GL_ELEMENT_ARRAY_BUFFER`): Przechowuje indeksy wierzchoÄąâ€škĂłw (nieuÄąÄ˝ywane w tym kodzie).
-   **`enum UsagePattern`**: WskazĂłwka dla sterownika OpenGL, jak dane bÄ™dÄ… uÄąÄ˝ywane.
    -   `StreamDraw` (`GL_STREAM_DRAW`): Dane zmieniane czÄ™sto, uÄąÄ˝ywane rzadko.
    -   `StaticDraw` (`GL_STATIC_DRAW`): Dane ustawiane raz, uÄąÄ˝ywane czÄ™sto.
    -   `DynamicDraw` (`GL_DYNAMIC_DRAW`): Dane zmieniane i uÄąÄ˝ywane czÄ™sto.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `HardwareBuffer(Type type)` | Konstruktor, tworzy nowy obiekt bufora w OpenGL (`glGenBuffers`). |
| `~HardwareBuffer()` | Destruktor, zwalnia obiekt bufora (`glDeleteBuffers`). |
| `void bind()` | Bindowanie (aktywuje) bufor w kontekÄąâ€şcie OpenGL (`glBindBuffer`). |
| `static void unbind(Type type)` | Odpina jakikolwiek bufor danego typu. |
| `void write(...)` | Kopiuje dane z pamiÄ™ci RAM do bufora w pamiÄ™ci GPU (`glBufferData`). |
## Zmienne prywatne

-   `m_type`: Typ bufora (`VertexBuffer` lub `IndexBuffer`).
-   `m_id`: ID (uchwyt) bufora w OpenGL.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Zawiera `glutil.h` z definicjami OpenGL.
-   Jest uÄąÄ˝ywana przez `VertexArray` (w `coordsbuffer.h`) do opcjonalnego keszowania geometrii na GPU.
-   `Painter` uÄąÄ˝ywa `HardwareBuffer` do ustawiania atrybutĂłw wierzchoÄąâ€škĂłw podczas rysowania.

---
# Ä‘Ĺşâ€śâ€ž image.h
## Opis ogĂłlny

Plik `image.h` deklaruje klasÄ™ `Image`, ktĂłra reprezentuje obraz rastrowy przechowywany w pamiÄ™ci systemowej (RAM). Jest to podstawowa struktura danych do manipulacji pikselami przed ich wysÄąâ€šaniem do karty graficznej jako tekstura.
## Klasa `Image`
## Opis semantyczny
`Image` to kontener na surowe dane pikseli. Przechowuje wymiary obrazu, liczbÄ™ bitĂłw na piksel oraz sam bufor pikseli. UdostÄ™pnia metody do Äąâ€šadowania obrazĂłw z plikĂłw, zapisywania ich, a takÄąÄ˝e do podstawowych operacji graficznych, takich jak kopiowanie fragmentĂłw (`blit`), generowanie mipmap czy skalowanie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Image(...)` | Konstruktor. |
| `static ImagePtr load(...)` | Statyczna metoda fabryczna do Äąâ€šadowania obrazu z pliku (obecnie tylko PNG). |
| `static ImagePtr loadPNG(...)` | ÄąÂaduje obraz PNG z pliku lub bufora w pamiÄ™ci. |
| `void savePNG(...)` | Zapisuje obraz do pliku w formacie PNG. |
| `void blit(...)` | Kopiuje inny obraz na ten obraz z uwzglÄ™dnieniem przezroczystoÄąâ€şci. |
| `void paste(...)` | NakÄąâ€šada inny obraz na ten obraz, zastÄ™pujÄ…c piksele. |
| `ImagePtr upscale()` | Zwraca nowÄ…, dwukrotnie wiÄ™kszÄ… wersjÄ™ obrazu. |
| `void resize(...)` | Zmienia rozmiar obrazu, realokujÄ…c bufor pikseli. |
| `bool nextMipmap()` | Generuje kolejny poziom mipmapy, zmniejszajÄ…c obraz o poÄąâ€šowÄ™. |
| `void setPixel(...)` | Ustawia kolor pojedynczego piksela. |
| `std::vector<uint8>& getPixels()` | Zwraca referencjÄ™ do wektora pikseli. |
| `uint8* getPixelData()` | Zwraca surowy wskaÄąĹźnik na dane pikseli. |
| `int getPixelCount()` | Zwraca liczbÄ™ pikseli. |
| `const Size& getSize()` | Zwraca wymiary obrazu. |
| `int getBpp()` | Zwraca liczbÄ™ bajtĂłw na piksel. |
| `static ImagePtr fromQRCode(...)` | Tworzy obraz z kodu QR. |
## Zmienne prywatne

-   `m_pixels`: Wektor przechowujÄ…cy dane pikseli.
-   `m_size`: Wymiary obrazu.
-   `m_bpp`: Liczba bajtĂłw na piksel.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: Potencjalnie, chociaÄąÄ˝ tutaj uÄąÄ˝ywa `std::vector`.
-   Jest uÄąÄ˝ywana przez `Texture` i `AnimatedTexture` jako ÄąĹźrĂłdÄąâ€šo danych pikseli podczas tworzenia tekstur.
-   Wykorzystywana przez `PlatformWindow` do Äąâ€šadowania ikon i kursorĂłw.

---
# Ä‘Ĺşâ€śâ€ž framebuffermanager.h
## Opis ogĂłlny

Plik `framebuffermanager.h` deklaruje klasÄ™ `FrameBufferManager`, ktĂłra jest singletonem (`g_framebuffers`) sÄąâ€šuÄąÄ˝Ä…cym do zarzÄ…dzania i tworzenia obiektĂłw `FrameBuffer`.
## Klasa `FrameBufferManager`
## Opis semantyczny
`FrameBufferManager` peÄąâ€šni rolÄ™ fabryki i menedÄąÄ˝era dla obiektĂłw `FrameBuffer`. Upraszcza ich tworzenie i zarzÄ…dzanie cyklem ÄąÄ˝ycia. UdostÄ™pnia rĂłwnieÄąÄ˝ dwa predefiniowane, "tymczasowe" bufory, ktĂłre mogÄ… byÄ‡ uÄąÄ˝ywane w caÄąâ€šym systemie do krĂłtkotrwaÄąâ€šych operacji renderowania poza ekranem, co pozwala uniknÄ…Ä‡ kosztownego tworzenia i niszczenia FBO.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedÄąÄ˝era i tworzy tymczasowe bufory ramki. |
| `void terminate()` | Zwalnia wszystkie zarzÄ…dzane bufory ramki. |
| `void clear()` | (Brak implementacji) Prawdopodobnie miaÄąâ€ša sÄąâ€šuÄąÄ˝yÄ‡ do zwolnienia wszystkich buforĂłw poza tymczasowymi. |
| `FrameBufferPtr createFrameBuffer(bool withDepth = false)` | Metoda fabryczna tworzÄ…ca i zwracajÄ…ca nowy obiekt `FrameBuffer`. |
| `const FrameBufferPtr& getTemporaryFrameBuffer()` | Zwraca wskaÄąĹźnik do pierwszego tymczasowego bufora. |
| `const FrameBufferPtr& getDrawQueueTemporaryFrameBuffer()` | Zwraca wskaÄąĹźnik do drugiego tymczasowego bufora, prawdopodobnie uÄąÄ˝ywanego przez `DrawQueue`. |
## Zmienne chronione

-   `m_temporaryFramebuffer`: Pierwszy tymczasowy `FrameBuffer`.
-   `m_drawQueueTemporaryFramebuffer`: Drugi tymczasowy `FrameBuffer`.
-   `m_framebuffers`: Wektor przechowujÄ…cy wskaÄąĹźniki do wszystkich utworzonych (i niezwolnionych) buforĂłw ramki. |
## Zmienne globalne

-   `g_framebuffers`: Globalna instancja `FrameBufferManager`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/framebuffer.h`: Deklaracja klasy `FrameBuffer`.
-   Jest to kluczowy komponent, od ktĂłrego zaleÄąÄ˝Ä… inne czÄ™Äąâ€şci systemu graficznego, takie jak `Atlas` i `GraphicalApplication`, ktĂłre potrzebujÄ… tworzyÄ‡ wÄąâ€šasne bufory ramki.

---
# Ä‘Ĺşâ€śâ€ž painter.h
## Opis ogĂłlny

Plik `painter.h` deklaruje klasÄ™ `Painter`, ktĂłra jest centralnym interfejsem do wszystkich operacji rysowania w 2D. Abstrakcjonuje ona niskopoziomowe wywoÄąâ€šania OpenGL, dostarczajÄ…c prostsze API do rysowania prostokÄ…tĂłw, tekstur, linii i zarzÄ…dzania stanem renderowania.
## Klasa `Painter`
## Opis semantyczny
`Painter` dziaÄąâ€ša jak maszyna stanĂłw. Przechowuje aktualny stan renderowania, taki jak macierze transformacji, kolor, tryb mieszania, aktywny shader, tekstura, itp. KaÄąÄ˝da operacja rysowania jest wykonywana w kontekÄąâ€şcie tego stanu. `Painter` zarzÄ…dza rĂłwnieÄąÄ˝ wÄąâ€šasnymi, domyÄąâ€şlnymi programami shaderĂłw do podstawowych operacji.
## Typy wyliczeniowe (Enums)

-   `BlendEquation`: OkreÄąâ€şla, jak kolory sÄ… mieszane (np. dodawanie, odejmowanie).
-   `CompositionMode`: Definiuje predefiniowane tryby mieszania (`glBlendFunc`), np. normalne (z przezroczystoÄąâ€şciÄ…), addytywne, mnoÄąÄ˝enie.
-   `DepthFunc`: OkreÄąâ€şla funkcjÄ™ testu gÄąâ€šÄ™bi.
-   `DrawMode`: OkreÄąâ€şla prymityw do rysowania (trĂłjkÄ…ty, paski trĂłjkÄ…tĂłw).
## Struktura `PainterState`

Przechowuje peÄąâ€šny stan `Painter`, co pozwala na jego zapisywanie i przywracanie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **ZarzÄ…dzanie stanem** | |
| `resetState()` | Przywraca wszystkie ustawienia do wartoÄąâ€şci domyÄąâ€şlnych. |
| `saveState()` / `restoreSavedState()` | Zapisuje/przywraca stan na wewnÄ™trznym stosie. |
| `setTransformMatrix(...)`, `setProjectionMatrix(...)`, ... | UstawiajÄ… poszczegĂłlne elementy stanu (macierze, tryb mieszania, etc.). |
| `scale()`, `translate()`, `rotate()` | ModyfikujÄ… bieÄąÄ˝Ä…cÄ… macierz transformacji. |
| **Operacje rysowania** | |
| `clear(const Color& color)` | CzyÄąâ€şci caÄąâ€šy bufor ramki. |
| `drawCoords(...)` | Niskopoziomowa metoda rysujÄ…ca geometriÄ™ z `CoordsBuffer`. |
| `drawFilledRect(const Rect& dest)` | Rysuje wypeÄąâ€šniony prostokÄ…t. |
| `drawTexturedRect(...)` | Rysuje prostokÄ…t z teksturÄ…. |
| `drawText(...)` | Rysuje tekst (przez `TextRender`). |
| `drawLine(...)` | Rysuje liniÄ™. |
| `drawCache(...)` | Rysuje dane zbuforowane w `DrawCache`. |
| **Gettery** | |
| `getTransformMatrix()`, `getColor()`, `getClipRect()`, ... | ZwracajÄ… aktualne wartoÄąâ€şci stanu. |
| `draws()`, `calls()` | ZwracajÄ… statystyki renderowania dla bieÄąÄ˝Ä…cej klatki. |
## Zmienne chronione/prywatne

-   `m_transformMatrix`, `m_projectionMatrix`, ...: Zmienne przechowujÄ…ce aktualny stan.
-   `m_transformMatrixStack`: Stos do zapisywania macierzy transformacji.
-   `m_olderStates`: Stos do zapisywania peÄąâ€šnego stanu `PainterState`.
-   `m_draw...Program`: WskaÄąĹźniki na domyÄąâ€şlne programy shaderĂłw.
## Zmienne globalne

-   `g_painter`: Globalny wskaÄąĹźnik na instancjÄ™ `Painter`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`, `coordsbuffer.h`, `paintershaderprogram.h`, `texture.h`, `colorarray.h`, `drawqueue.h`: Deklaracje typĂłw, z ktĂłrymi `Painter` wspĂłÄąâ€špracuje.
-   Jest to centralny komponent renderujÄ…cy, uÄąÄ˝ywany bezpoÄąâ€şrednio lub poÄąâ€şrednio przez `DrawQueue`, `UIWidget`, `TextRender` i inne.

---
# Ä‘Ĺşâ€śâ€ž painter.cpp
## Opis ogĂłlny

Plik `painter.cpp` zawiera implementacjÄ™ klasy `Painter`, ktĂłra jest sercem silnika renderujÄ…cego. Odpowiada za bezpoÄąâ€şredniÄ… komunikacjÄ™ z API graficznym (OpenGL) w celu rysowania prymitywĂłw 2D.
## Zmienne globalne
## `g_painter`

Globalny wskaÄąĹźnik na jedynÄ… instancjÄ™ `Painter`. Jest inicjalizowany w `Graphics::init()`.

`$fenceInfo
Painter* g_painter = nullptr;
```
## Klasa `Painter`
## `Painter::Painter()`

Konstruktor. Inicjalizuje domyÄąâ€şlne wartoÄąâ€şci stanu, takie jak macierze, kolory i tryby mieszania. Co najwaÄąÄ˝niejsze, tworzy i kompiluje zestaw domyÄąâ€şlnych programĂłw shaderĂłw, ktĂłre sÄ… uÄąÄ˝ywane do podstawowych operacji rysowania:
-   `m_drawTexturedProgram`: Do rysowania tekstur.
-   `m_drawSolidColorProgram`: Do rysowania jednolitych kolorĂłw.
-   `m_drawSolidColorOnTextureProgram`: Do rysowania jednolitego koloru na wierzchu tekstury.
-   `m_drawOutfitLayersProgram`: Specjalny shader do rysowania strojĂłw postaci z kolorowaniem.
-   `m_drawNewProgram`: Shader uÄąÄ˝ywany przez `DrawCache` do zoptymalizowanego rysowania wsadowego.
-   `m_drawTextProgram`, `m_drawLineProgram`: Specjalne shadery do rysowania tekstu i linii.
## `void Painter::bind()` i `void Painter::unbind()`

Metody wywoÄąâ€šywane na poczÄ…tku i na koÄąâ€žcu cyklu ÄąÄ˝ycia `Painter`. `bind()` wÄąâ€šÄ…cza podstawowe atrybuty wierzchoÄąâ€škĂłw, ktĂłre sÄ… zawsze aktywne.
## `void Painter::resetState()`

Przywraca wszystkie parametry `Painter` (kolor, macierze, tryby mieszania itp.) do ich wartoÄąâ€şci domyÄąâ€şlnych.
## `void Painter::saveState()` i `void Painter::restoreSavedState()`

ImplementujÄ… mechanizm stosu do zapisywania i przywracania stanu renderowania. Pozwala to na tymczasowÄ… zmianÄ™ stanu (np. ustawienie przycinania) i Äąâ€šatwy powrĂłt do poprzedniego stanu.
## Metody `updateGl...()`

Prywatne metody pomocnicze (`updateGlTexture`, `updateGlCompositionMode`, `updateGlClipRect` itd.), ktĂłre aplikujÄ… zmiany stanu `Painter` do rzeczywistego stanu OpenGL. SÄ… wywoÄąâ€šywane, gdy odpowiednia wÄąâ€šaÄąâ€şciwoÄąâ€şÄ‡ `Painter` (np. `m_compositionMode`) ulega zmianie.
## `void Painter::setResolution(const Size& resolution)`

Aktualizuje rozdzielczoÄąâ€şÄ‡ renderowania. NajwaÄąÄ˝niejszÄ… czÄ™Äąâ€şciÄ… jest przeliczenie macierzy projekcji (`m_projectionMatrix`), ktĂłra mapuje wspĂłÄąâ€šrzÄ™dne w pikselach na znormalizowane wspĂłÄąâ€šrzÄ™dne urzÄ…dzenia OpenGL (-1 do 1).
## `void Painter::drawCoords(...)`

Niskopoziomowa metoda, ktĂłra jest podstawÄ… wiÄ™kszoÄąâ€şci operacji rysowania.
1.  Bindowanie i konfiguruje odpowiedni program shadera.
2.  Przekazuje do shadera uniformy (macierze, kolor, czas itp.).
3.  Ustawia wskaÄąĹźniki na dane atrybutĂłw wierzchoÄąâ€škĂłw (pozycja, wspĂłÄąâ€šrzÄ™dne tekstury, kolor).
4.  WywoÄąâ€šuje `glDrawArrays` w celu narysowania geometrii.
5.  Zlicza statystyki (`m_draws`, `m_calls`).
## Metody `draw...Rect(...)` i `draw...Coords(...)`

Wysokopoziomowe metody rysujÄ…ce, ktĂłre przygotowujÄ… `CoordsBuffer` z odpowiedniÄ… geometriÄ…, a nastÄ™pnie wywoÄąâ€šujÄ… `drawCoords` do jej narysowania.
## `void Painter::drawCache(...)`

Specjalna, zoptymalizowana metoda do rysowania duÄąÄ˝ej liczby wierzchoÄąâ€škĂłw na raz. UÄąÄ˝ywa dedykowanego shadera (`m_drawNewProgram`), ktĂłry pobiera pozycjÄ™, wspĂłÄąâ€šrzÄ™dne tekstury i kolor jako osobne atrybuty dla kaÄąÄ˝dego wierzchoÄąâ€ška.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to klasa niskiego poziomu, ktĂłra bezpoÄąâ€şrednio zaleÄąÄ˝y od API graficznego (OpenGL/GLES/GLEW).
-   `framework/graphics/shaders/shaders.h`: Zawiera kod ÄąĹźrĂłdÄąâ€šowy domyÄąâ€şlnych shaderĂłw.
-   WspĂłÄąâ€špracuje z `Texture`, `CoordsBuffer`, `ShaderProgram`, `DrawCache`, `TextRender` i innymi komponentami graficznymi.
-   Jest uÄąÄ˝ywana przez `DrawQueue` do wykonywania wszystkich operacji rysowania.

---
# Ä‘Ĺşâ€śâ€ž hardwarebuffer.cpp
## Opis ogĂłlny

Plik `hardwarebuffer.cpp` zawiera implementacjÄ™ klasy `HardwareBuffer`, ktĂłra jest opakowaniem na bufory VBO (Vertex Buffer Object) w OpenGL.
## Klasa `HardwareBuffer`
## `HardwareBuffer::HardwareBuffer(Type type)`

Konstruktor.
-   **Parametr `type`**: OkreÄąâ€şla, czy ma to byÄ‡ bufor na wierzchoÄąâ€ški (`VertexBuffer`) czy indeksy (`IndexBuffer`).
-   **DziaÄąâ€šanie**:
    1.  ZapamiÄ™tuje typ bufora.
    2.  WywoÄąâ€šuje `glGenBuffers(1, &m_id)` w celu wygenerowania nowego, unikalnego ID dla bufora w kontekÄąâ€şcie OpenGL.
    3.  Sprawdza, czy operacja siÄ™ powiodÄąâ€ša; w przeciwnym razie koÄąâ€žczy aplikacjÄ™ bÄąâ€šÄ™dem krytycznym.
## `HardwareBuffer::~HardwareBuffer()`

Destruktor.
-   **DziaÄąâ€šanie**:
    1.  Zwalnia zasĂłb OpenGL w sposĂłb bezpieczny wÄ…tkowo.
    2.  Zamiast bezpoÄąâ€şrednio wywoÄąâ€šywaÄ‡ `glDeleteBuffers`, dodaje zadanie do kolejki dyspozytora graficznego (`g_graphicsDispatcher`). Gwarantuje to, ÄąÄ˝e operacja usuniÄ™cia zostanie wykonana w wÄ…tku, ktĂłry ma aktywny kontekst OpenGL, nawet jeÄąâ€şli destruktor jest wywoÄąâ€šywany z innego wÄ…tku.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/hardwarebuffer.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bÄąâ€šÄ™dĂłw OpenGL.
-   `framework/core/application.h`, `eventdispatcher.h`, `logger.h`: Do walidacji, planowania zdarzeÄąâ€ž i logowania.
-   Jest uÄąÄ˝ywana przez `VertexArray` (w `coordsbuffer.h`) do przechowywania danych geometrycznych w pamiÄ™ci karty graficznej, co znacznie przyspiesza renderowanie.

---
# Ä‘Ĺşâ€śâ€ž paintershaderprogram.cpp
## Opis ogĂłlny

Plik `paintershaderprogram.cpp` zawiera implementacjÄ™ klasy `PainterShaderProgram`, ktĂłra jest specjalizacjÄ… `ShaderProgram`. Jest ona dostosowana do wspĂłÄąâ€špracy z klasÄ… `Painter`, udostÄ™pniajÄ…c standardowy zestaw uniformĂłw i atrybutĂłw uÄąÄ˝ywanych w procesie renderowania 2D.
## Klasa `PainterShaderProgram`
## `PainterShaderProgram::PainterShaderProgram(const std::string& name)`

Konstruktor. WywoÄąâ€šuje konstruktor klasy bazowej i inicjalizuje dodatkowe zmienne, takie jak `m_startTime`, ktĂłry jest uÄąÄ˝ywany do animacji opartych na czasie w shaderach.
## `void PainterShaderProgram::setupUniforms()`
## Opis semantyczny
Wirtualna metoda, ktĂłra po zlinkowaniu programu shadera wyszukuje lokalizacje standardowych uniformĂłw (`u_TransformMatrix`, `u_ProjectionMatrix`, `u_Color`, `u_Tex0` itd.) i przypisuje im domyÄąâ€şlne wartoÄąâ€şci.
## `bool PainterShaderProgram::link()`

PrzesÄąâ€šania metodÄ™ z `ShaderProgram`.
1.  Ustawia `m_startTime`.
2.  WiÄ…ÄąÄ˝e standardowe lokalizacje atrybutĂłw (`VERTEX_ATTR`, `TEXCOORD_ATTR`, etc.) z ich nazwami w shaderze.
3.  WywoÄąâ€šuje `ShaderProgram::link()`.
4.  JeÄąâ€şli linkowanie siÄ™ powiedzie, bindowanie program i wywoÄąâ€šuje `setupUniforms()`.
## Metody `set...()`

SÄ… to metody do ustawiania wartoÄąâ€şci uniformĂłw. KaÄąÄ˝da z nich:
1.  Sprawdza, czy nowa wartoÄąâ€şÄ‡ rĂłÄąÄ˝ni siÄ™ od aktualnie przechowywanej, aby uniknÄ…Ä‡ zbÄ™dnych wywoÄąâ€šaÄąâ€ž `glUniform...`.
2.  Bindowanie program shadera (`bind()`).
3.  Ustawia nowÄ… wartoÄąâ€şÄ‡ uniformu w OpenGL.
4.  Aktualizuje przechowywanÄ… wartoÄąâ€şÄ‡.

-   `setTransformMatrix`, `setProjectionMatrix`, `setTextureMatrix`: UstawiajÄ… macierze.
-   `setColor`: Ustawia gÄąâ€šĂłwny kolor.
-   `setMatrixColor`: Ustawia macierz kolorĂłw (dla shadera strojĂłw).
-   `setResolution`: Ustawia rozdzielczoÄąâ€şÄ‡ (przydatne do efektĂłw zaleÄąÄ˝nych od pikseli).
-   ... i inne.
## `void PainterShaderProgram::updateTime()`

Aktualizuje uniform `u_Time`, przekazujÄ…c do shadera czas, jaki upÄąâ€šynÄ…Äąâ€š od jego utworzenia. Pozwala to na tworzenie animowanych efektĂłw w shaderach.
## `void PainterShaderProgram::addMultiTexture(...)` i `void PainterShaderProgram::bindMultiTextures()`

Metody do obsÄąâ€šugi dodatkowych tekstur (multi-texturing). `addMultiTexture` Äąâ€šaduje teksturÄ™ i dodaje jÄ… do listy. `bindMultiTextures` aktywuje te tekstury na kolejnych jednostkach teksturujÄ…cych (od `GL_TEXTURE1` wzwyÄąÄ˝), aby mogÄąâ€šy byÄ‡ uÄąÄ˝ywane w shaderze.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/paintershaderprogram.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/painter.h`: ÄąĹˇciÄąâ€şle wspĂłÄąâ€špracuje z `Painter`, ktĂłry ustawia jej uniformy.
-   `framework/graphics/texture.h`, `texturemanager.h`: Do Äąâ€šadowania i zarzÄ…dzania dodatkowymi teksturami.
-   `framework/core/clock.h`: Do Äąâ€şledzenia czasu dla animacji.

---
# Ä‘Ĺşâ€śâ€ž paintershaderprogram.h
## Opis ogĂłlny

Plik `paintershaderprogram.h` deklaruje klasÄ™ `PainterShaderProgram`, ktĂłra jest wyspecjalizowanÄ… wersjÄ… `ShaderProgram`, dostosowanÄ… do potrzeb `Painter`. Definiuje ona standardowy zestaw uniformĂłw i atrybutĂłw uÄąÄ˝ywanych w shaderach 2D.
## Klasa `PainterShaderProgram`
## Opis semantyczny
`PainterShaderProgram` dziedziczy po `ShaderProgram` i dodaje do niej warstwÄ™ abstrakcji specyficznÄ… dla `Painter`. Zamiast odwoÄąâ€šywaÄ‡ siÄ™ do uniformĂłw po nazwach (stringach), udostÄ™pnia dedykowane metody `set...()`, ktĂłre operujÄ… na predefiniowanych, zbuforowanych lokalizacjach. Upraszcza to kod `Painter` i potencjalnie zwiÄ™ksza wydajnoÄąâ€şÄ‡.
## Typy wyliczeniowe (Enums)

Definiuje staÄąâ€še dla lokalizacji standardowych atrybutĂłw i uniformĂłw, co pozwala na ich efektywne buforowanie.

-   **Atrybuty**: `VERTEX_ATTR`, `TEXCOORD_ATTR`, ...
-   **Uniformy**: `PROJECTION_MATRIX_UNIFORM`, `TEXTURE_MATRIX_UNIFORM`, `COLOR_UNIFORM`, `TEX0_UNIFORM`, ...
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PainterShaderProgram(...)`| Konstruktor. |
| `bool link()` | PrzesÄąâ€šania metodÄ™ bazowÄ…, aby dodatkowo zmapowaÄ‡ standardowe atrybuty i uniformy. |
| `setTransformMatrix(...)` | Ustawia macierz transformacji. |
| `setProjectionMatrix(...)`| Ustawia macierz projekcji. |
| `setTextureMatrix(...)` | Ustawia macierz tekstury. |
| `setColor(...)` | Ustawia gÄąâ€šĂłwny kolor. |
| `setMatrixColor(...)` | Ustawia macierz kolorĂłw (dla shadera strojĂłw). |
| `setDepth(...)` | Ustawia wartoÄąâ€şÄ‡ gÄąâ€šÄ™bi. |
| `setResolution(...)` | Ustawia rozdzielczoÄąâ€şÄ‡ renderowania. |
| `setOffset(...)` | Ustawia przesuniÄ™cie (offset). |
| `updateTime()` | Aktualizuje uniform czasu. |
| `addMultiTexture(...)` | Dodaje dodatkowÄ… teksturÄ™ do shadera. |
| `bindMultiTextures()` | Bindowanie wszystkie dodatkowe tekstury. |
| `clearMultiTextures()` | CzyÄąâ€şci listÄ™ dodatkowych tekstur. |
| `enableColorMatrix()` | WÄąâ€šÄ…cza tryb macierzy kolorĂłw (dla shadera strojĂłw). |
## Zmienne prywatne

-   `m_startTime`: Czas utworzenia shadera.
-   `m_color`, `m_depth`, `m_transformMatrix`, ...: PrzechowujÄ… aktualne wartoÄąâ€şci uniformĂłw, aby uniknÄ…Ä‡ zbÄ™dnych wywoÄąâ€šaÄąâ€ž `glUniform...`.
-   `m_multiTextures`: Wektor dodatkowych tekstur.
-   `m_useColorMatrix`: Flaga wskazujÄ…ca, czy `u_Color` jest macierzÄ… 4x4.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/shaderprogram.h`: Klasa bazowa.
-   `framework/graphics/coordsbuffer.h`: PoÄąâ€şrednio, poprzez `Painter`.
-   Jest uÄąÄ˝ywana przez `Painter` jako podstawa dla wszystkich operacji rysowania opartych na shaderach.

---
# Ä‘Ĺşâ€śâ€ž shader.cpp
## Opis ogĂłlny

Plik `shader.cpp` zawiera implementacjÄ™ klasy `Shader`, ktĂłra jest opakowaniem na pojedynczy obiekt shadera w OpenGL (np. shader wierzchoÄąâ€škĂłw lub shader fragmentĂłw).
## Klasa `Shader`
## `Shader::Shader(Shader::ShaderType shaderType)`

Konstruktor.
-   **Parametr `shaderType`**: OkreÄąâ€şla, czy tworzony jest shader wierzchoÄąâ€škĂłw (`Vertex`) czy fragmentĂłw (`Fragment`).
-   **DziaÄąâ€šanie**: WywoÄąâ€šuje `glCreateShader` z odpowiednim typem, aby utworzyÄ‡ obiekt shadera w sterowniku graficznym. W przypadku bÄąâ€šÄ™du, koÄąâ€žczy aplikacjÄ™.
## `Shader::~Shader()`

Destruktor. Zwalnia zasĂłb shadera w OpenGL, wywoÄąâ€šujÄ…c `glDeleteShader`.
## `bool Shader::compileSourceCode(const std::string& sourceCode)`
## Opis semantyczny
Kompiluje kod ÄąĹźrĂłdÄąâ€šowy shadera.
## DziaÄąâ€šanie
1.  Dla OpenGL ES, dodaje na poczÄ…tku kodu dyrektywÄ™ `precision highp float;`.
2.  Przekazuje kod ÄąĹźrĂłdÄąâ€šowy do sterownika za pomocÄ… `glShaderSource`.
3.  Kompiluje shader za pomocÄ… `glCompileShader`.
4.  Sprawdza status kompilacji za pomocÄ… `glGetShaderiv`.
5.  Zwraca `true` w przypadku sukcesu, `false` w przeciwnym razie.
## `bool Shader::compileSourceFile(const std::string& sourceFile)`

ÄąÂaduje kod ÄąĹźrĂłdÄąâ€šowy z pliku za pomocÄ… `g_resources`, a nastÄ™pnie wywoÄąâ€šuje `compileSourceCode`.
## `std::string Shader::log()`

Pobiera i zwraca logi kompilatora shadera (`glGetShaderInfoLog`), ktĂłre zawierajÄ… informacje o bÄąâ€šÄ™dach lub ostrzeÄąÄ˝eniach.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/shader.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/graphics.h`: Do dostÄ™pu do funkcji OpenGL.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   `framework/core/resourcemanager.h`: Do Äąâ€šadowania shaderĂłw z plikĂłw.
-   Obiekty `Shader` sÄ… tworzone i zarzÄ…dzane przez `ShaderProgram` (lub `PainterShaderProgram`), ktĂłry nastÄ™pnie linkuje je w kompletny program shadera.

---
# Ä‘Ĺşâ€śâ€ž shadermanager.h
## Opis ogĂłlny

Plik `shadermanager.h` deklaruje klasÄ™ `ShaderManager`, ktĂłra jest singletonem (`g_shaders`) odpowiedzialnym za zarzÄ…dzanie niestandardowymi programami shaderĂłw tworzonymi w skryptach Lua.
## Klasa `ShaderManager`
## Opis semantyczny
`ShaderManager` dziaÄąâ€ša jako repozytorium dla `PainterShaderProgram` tworzonych dynamicznie. Przechowuje je w mapie pod unikalnymi nazwami, co pozwala na ich pĂłÄąĹźniejsze pobieranie i uÄąÄ˝ywanie w trakcie renderowania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedÄąÄ˝era. |
| `void terminate()` | CzyÄąâ€şci i zwalnia wszystkie zaÄąâ€šadowane shadery. |
| `void createShader(...)` | Tworzy, kompiluje i linkuje nowy `PainterShaderProgram` z podanego kodu ÄąĹźrĂłdÄąâ€šowego (lub plikĂłw). Zapisuje go pod danÄ… nazwÄ…. |
| `void createOutfitShader(...)` | SkrĂłt do `createShader` z wÄąâ€šÄ…czonÄ… opcjÄ… macierzy kolorĂłw, specjalnie dla shaderĂłw strojĂłw. |
| `void addTexture(...)` | Dodaje dodatkowÄ… teksturÄ™ do istniejÄ…cego programu shadera. |
| `PainterShaderProgramPtr getShader(...)` | Wyszukuje i zwraca wskaÄąĹźnik do programu shadera o podanej nazwie. |
## Zmienne prywatne

-   `m_shaders`: Mapa (`std::unordered_map`) przechowujÄ…ca wszystkie niestandardowe programy shaderĂłw.
## Zmienne globalne

-   `g_shaders`: Globalna instancja `ShaderManager`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`, `paintershaderprogram.h`: Deklaracje klas shaderĂłw.
-   Jest oznaczona jako `@bindsingleton g_shaders`, co udostÄ™pnia jej API (`createShader`, `addTexture`) w skryptach Lua.
-   Jest uÄąÄ˝ywana przez `UIWidget` (w `uiwidgetimage.cpp`) do rysowania obrazĂłw z niestandardowymi shaderami.
-   Wszystkie operacje tworzenia i modyfikacji shaderĂłw sÄ… delegowane do wÄ…tku graficznego za pomocÄ… `g_graphicsDispatcher`, aby zapewniÄ‡ bezpieczeÄąâ€žstwo wÄ…tkowe.

---
# Ä‘Ĺşâ€śâ€ž shadermanager.cpp
## Opis ogĂłlny

Plik `shadermanager.cpp` zawiera implementacjÄ™ klasy `ShaderManager`, ktĂłra zarzÄ…dza niestandardowymi programami shaderĂłw.
## Zmienne globalne
## `g_shaders`

Globalna instancja `ShaderManager`.

`$fenceInfo
ShaderManager g_shaders;
```
## Klasa `ShaderManager`
## `void ShaderManager::init()`

Inicjalizuje menedÄąÄ˝era. W obecnej implementacji wywoÄąâ€šuje `PainterShaderProgram::release()`, aby upewniÄ‡ siÄ™, ÄąÄ˝e ÄąÄ˝aden shader nie jest aktywny.
## `void ShaderManager::terminate()`

CzyÄąâ€şci mapÄ™ `m_shaders`, co powoduje zwolnienie wszystkich niestandardowych programĂłw shaderĂłw.
## `void ShaderManager::createShader(const std::string& name, std::string vertex, std::string fragment, bool colorMatrix)`
## Opis semantyczny
Tworzy nowy program shadera. Metoda jest asynchroniczna - dodaje zadanie do dyspozytora graficznego.
## DziaÄąâ€šanie
1.  Sprawdza, czy podane stringi `vertex` i `fragment` sÄ… kodem ÄąĹźrĂłdÄąâ€šowym (zawierajÄ… znak nowej linii) czy Äąâ€şcieÄąÄ˝kami do plikĂłw.
2.  JeÄąâ€şli sÄ… to Äąâ€şcieÄąÄ˝ki, odczytuje zawartoÄąâ€şÄ‡ plikĂłw za pomocÄ… `g_resources`.
3.  Dodaje do `g_graphicsDispatcher` zadanie (lambda), ktĂłre:
    -   WywoÄąâ€šuje `PainterShaderProgram::create` w celu skompilowania i zlinkowania shadera.
    -   JeÄąâ€şli operacja siÄ™ powiedzie, dodaje nowo utworzony program do mapy `m_shaders`.
## `void ShaderManager::addTexture(const std::string& name, const std::string& file)`

Dodaje dodatkowÄ… teksturÄ™ do istniejÄ…cego shadera. Podobnie jak `createShader`, operacja jest wykonywana asynchronicznie w wÄ…tku graficznym.
## `PainterShaderProgramPtr ShaderManager::getShader(const std::string& name)`

Wyszukuje i zwraca program shadera o podanej nazwie. Ta metoda musi byÄ‡ wywoÄąâ€šywana z wÄ…tku graficznego, co jest zapewnione przez `VALIDATE_GRAPHICS_THREAD()`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/shadermanager.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/paintershaderprogram.h`: Do tworzenia obiektĂłw shaderĂłw.
-   `framework/core/resourcemanager.h`: Do Äąâ€šadowania kodu shaderĂłw z plikĂłw.
-   `framework/core/eventdispatcher.h`: Do zapewnienia, ÄąÄ˝e operacje na OpenGL sÄ… wykonywane w wÄ…tku graficznym.

---
# Ä‘Ĺşâ€śâ€ž shader.h
## Opis ogĂłlny

Plik `shader.h` deklaruje klasÄ™ `Shader`, ktĂłra reprezentuje pojedynczy, skompilowany obiekt shadera w OpenGL (np. shader wierzchoÄąâ€škĂłw lub fragmentĂłw), ale jeszcze nie zlinkowany w peÄąâ€šny program.
## Klasa `Shader`
## Opis semantyczny
`Shader` jest niskopoziomowym opakowaniem na ID obiektu shadera w OpenGL. Jego gÄąâ€šĂłwnym zadaniem jest przyjÄ™cie kodu ÄąĹźrĂłdÄąâ€šowego, skompilowanie go i przechowanie wyniku. Obiekty tej klasy sÄ… nastÄ™pnie Äąâ€šÄ…czone w `ShaderProgram`.
## Typ wyliczeniowy `ShaderType`

-   `Vertex`: Oznacza shader wierzchoÄąâ€škĂłw (`GL_VERTEX_SHADER`).
-   `Fragment`: Oznacza shader fragmentĂłw/pikseli (`GL_FRAGMENT_SHADER`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Shader(ShaderType shaderType)` | Konstruktor, tworzy obiekt shadera w OpenGL. |
| `~Shader()` | Destruktor, zwalnia obiekt shadera. |
| `bool compileSourceCode(...)` | Kompiluje shader z podanego kodu ÄąĹźrĂłdÄąâ€šowego. |
| `bool compileSourceFile(...)` | ÄąÂaduje kod z pliku i go kompiluje. |
| `std::string log()` | Zwraca logi kompilatora shadera. |
| `uint getShaderId()` | Zwraca ID obiektu shadera w OpenGL. |
| `ShaderType getShaderType()` | Zwraca typ shadera. |
## Zmienne prywatne

-   `m_shaderId`: ID obiektu shadera w OpenGL.
-   `m_shaderType`: Typ shadera.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   Jest tworzona i uÄąÄ˝ywana przez `ShaderProgram` w procesie budowania kompletnego programu shadera.

---
# Ä‘Ĺşâ€śâ€ž textrender.cpp
## Opis ogĂłlny

Plik `textrender.cpp` implementuje klasÄ™ `TextRender`, ktĂłra jest systemem do optymalizacji renderowania tekstu. DziaÄąâ€ša jako globalny cache dla geometrii tekstu, aby uniknÄ…Ä‡ ponownego obliczania pozycji glifĂłw w kaÄąÄ˝dej klatce dla tekstĂłw, ktĂłre siÄ™ nie zmieniajÄ….
## Zmienne globalne
## `g_text`

Globalna instancja `TextRender`.

`$fenceInfo
TextRender g_text;
```
## Klasa `TextRender`
## Opis semantyczny
`TextRender` przechowuje mapÄ™ (`m_cache`), w ktĂłrej kluczem jest hash wygenerowany na podstawie treÄąâ€şci tekstu, jego rozmiaru, wyrĂłwnania i fontu. WartoÄąâ€şciÄ… jest obiekt `TextRenderCache`, ktĂłry przechowuje `CoordsBuffer` z gotowÄ… geometriÄ… tekstu. Przy pierwszym ÄąÄ˝Ä…daniu narysowania danego tekstu, geometria jest obliczana i zapisywana w cache. Przy kolejnych ÄąÄ˝Ä…daniach, uÄąÄ˝ywana jest juÄąÄ˝ istniejÄ…ca geometria. System posiada rĂłwnieÄąÄ˝ mechanizm czyszczenia nieuÄąÄ˝ywanych wpisĂłw z cache.
## `void TextRender::init()` i `void TextRender::terminate()`

Metody inicjalizujÄ…ce i zwalniajÄ…ce cache.
## `void TextRender::poll()`

Metoda wywoÄąâ€šywana okresowo. Jej zadaniem jest czyszczenie cache z wpisĂłw, ktĂłre nie byÄąâ€šy uÄąÄ˝ywane od pewnego czasu. Implementuje prosty mechanizm LRU (Least Recently Used) oparty na czasie ostatniego uÄąÄ˝ycia (`lastUse`).
## `uint64_t TextRender::addText(...)`

Generuje unikalny hash dla kombinacji (font, tekst, rozmiar, wyrĂłwnanie) i tworzy dla niego wpis w cache, jeÄąâ€şli jeszcze nie istnieje. Zwraca wygenerowany hash.
## `void TextRender::drawText(...)`

Wysokopoziomowa metoda do rysowania tekstu. Najpierw wywoÄąâ€šuje `addText`, aby uzyskaÄ‡/stworzyÄ‡ wpis w cache, a nastÄ™pnie wywoÄąâ€šuje drugÄ… wersjÄ™ `drawText` z hashem.
## `void TextRender::drawText(const Point& pos, uint64_t hash, ...)`

GÄąâ€šĂłwna metoda rysujÄ…ca.
1.  Znajduje wpis w cache na podstawie hasha.
2.  JeÄąâ€şli wpis jest nowy (`it->font` nie jest `nullptr`), wywoÄąâ€šuje `font->calculateDrawTextCoords`, aby wygenerowaÄ‡ geometriÄ™, keszuje jÄ… w `CoordsBuffer` (`it->coords.cache()`) i zwalnia referencje do fontu i tekstu, aby oszczÄ™dzaÄ‡ pamiÄ™Ä‡.
3.  WywoÄąâ€šuje `g_painter->drawText`, przekazujÄ…c mu gotowy `CoordsBuffer` z geometriÄ….
4.  ObsÄąâ€šuguje rĂłwnieÄąÄ˝ rysowanie cienia.
## `void TextRender::drawColoredText(...)`

DziaÄąâ€ša analogicznie do `drawText`, ale wywoÄąâ€šuje `g_painter->drawText` w wersji dla tekstu wielokolorowego.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/textrender.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/painter.h`: UÄąÄ˝ywa `g_painter` do finalnego rysowania.
-   `framework/core/eventdispatcher.h`: Do walidacji wÄ…tku.
-   Jest uÄąÄ˝ywana przez `DrawQueueItemText` do renderowania tekstu.

---
# Ä‘Ĺşâ€śâ€ž shaderprogram.cpp
## Opis ogĂłlny

Plik `shaderprogram.cpp` zawiera implementacjÄ™ klasy `ShaderProgram`, ktĂłra jest podstawowym obiektem do zarzÄ…dzania programami shaderĂłw w OpenGL.
## Zmienne globalne
## `uint ShaderProgram::m_currentProgram`

Statyczna zmienna czÄąâ€šonkowska, ktĂłra przechowuje ID aktualnie aktywnego (zbindowanego) programu shadera. SÄąâ€šuÄąÄ˝y do unikania zbÄ™dnych wywoÄąâ€šaÄąâ€ž `glUseProgram`, jeÄąâ€şli ten sam program jest juÄąÄ˝ aktywny.
## Klasa `ShaderProgram`
## `ShaderProgram::ShaderProgram(const std::string& name)`

Konstruktor. Inicjalizuje nazwÄ™, ustawia flagÄ™ `m_linked` na `false` i tworzy nowy, pusty obiekt programu shadera w OpenGL za pomocÄ… `glCreateProgram()`.
## `ShaderProgram::~ShaderProgram()`

Destruktor. Zwalnia zasĂłb programu shadera, wywoÄąâ€šujÄ…c `glDeleteProgram()`.
## `PainterShaderProgramPtr ShaderProgram::create(...)`

Statyczna metoda fabryczna, ktĂłra tworzy i konfiguruje `PainterShaderProgram`. Jest to gÄąâ€šĂłwny sposĂłb tworzenia shaderĂłw w tym frameworku.
## DziaÄąâ€šanie
1.  Tworzy nowy obiekt `PainterShaderProgram`.
2.  Dodaje i kompiluje shadery wierzchoÄąâ€škĂłw i fragmentĂłw.
3.  Opcjonalnie wÄąâ€šÄ…cza tryb macierzy kolorĂłw.
4.  Linkuje program.
5.  W przypadku bÄąâ€šÄ™dĂłw kompilacji lub linkowania, loguje szczegĂłÄąâ€šowe informacje i zwraca `nullptr`.
## `bool ShaderProgram::addShader(...)`

DoÄąâ€šÄ…cza wczeÄąâ€şniej skompilowany obiekt `Shader` do programu za pomocÄ… `glAttachShader`.
## `bool ShaderProgram::addShaderFromSourceCode(...)` i `addShaderFromSourceFile(...)`

Metody pomocnicze, ktĂłre tworzÄ… obiekt `Shader`, kompilujÄ… go z kodu ÄąĹźrĂłdÄąâ€šowego lub pliku, a nastÄ™pnie dodajÄ… do programu.
## `bool ShaderProgram::link()`
## Opis semantyczny
Linkuje wszystkie doÄąâ€šÄ…czone shadery w jeden wykonywalny program.
## DziaÄąâ€šanie
1.  WywoÄąâ€šuje `glLinkProgram()`.
2.  Sprawdza status linkowania za pomocÄ… `glGetProgramiv`.
3.  JeÄąâ€şli wystÄ…pi bÄąâ€šÄ…d, pobiera i loguje szczegĂłÄąâ€šowy komunikat bÄąâ€šÄ™du z `glGetProgramInfoLog`.
4.  Zwraca `true` w przypadku sukcesu.
## `bool ShaderProgram::bind()`

Aktywuje program shadera w potoku renderowania OpenGL za pomocÄ… `glUseProgram`. DziÄ™ki `m_currentProgram`, faktyczne wywoÄąâ€šanie `glUseProgram` nastÄ™puje tylko wtedy, gdy zmieniany jest program.
## `void ShaderProgram::release()`

Deaktywuje jakikolwiek aktywny program shadera (`glUseProgram(0)`).
## Metody `...Location(...)` i `set...Value(...)`

ImplementujÄ… interfejs do pracy z atrybutami i uniformami w shaderze, opakowujÄ…c odpowiednie funkcje OpenGL (`glGetAttribLocation`, `glBindAttribLocation`, `glGetUniformLocation`, `glUniform...`, `glVertexAttrib...`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/shaderprogram.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bÄąâ€šÄ™dĂłw i dostÄ™pu do informacji o sterowniku.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   Jest klasÄ… bazowÄ… dla `PainterShaderProgram`.
-   Jest zarzÄ…dzana przez `ShaderManager`.

---
# Ä‘Ĺşâ€śâ€ž texture.cpp
## Opis ogĂłlny

Plik `texture.cpp` zawiera implementacjÄ™ klasy `Texture`, ktĂłra jest obiektowym opakowaniem na teksturÄ™ w OpenGL. Odpowiada za tworzenie, Äąâ€šadowanie danych, ustawianie parametrĂłw i zwalnianie zasobĂłw tekstury w pamiÄ™ci karty graficznej.
## Zmienne globalne
## `uint Texture::uniqueId`

Statyczny licznik uÄąÄ˝ywany do przypisywania unikalnego ID kaÄąÄ˝dej nowo utworzonej teksturze. Jest to przydatne do szybkiego porĂłwnywania tekstur.
## Klasa `Texture`
## `Texture::Texture(...)`

Konstruktory.
-   **`Texture(const Size& size, ...)`**: Tworzy pustÄ… teksturÄ™ o podanych wymiarach.
-   **`Texture(const ImagePtr& image, ...)`**: Tworzy teksturÄ™ na podstawie obiektu `Image`.
-   **DziaÄąâ€šanie**: InicjalizujÄ… pola, przypisujÄ… unikalne ID i zwiÄ™kszajÄ… globalny licznik tekstur w `g_stats`.
## `Texture::~Texture()`

Destruktor. Dodaje zadanie usuniÄ™cia tekstury z pamiÄ™ci GPU do kolejki dyspozytora graficznego (`g_graphicsDispatcher`), co zapewnia bezpieczeÄąâ€žstwo wÄ…tkowe. Zmniejsza globalny licznik tekstur.
## `void Texture::replace(const ImagePtr& image)`

ZastÄ™puje zawartoÄąâ€şÄ‡ tekstury nowym obrazem. Stara tekstura w OpenGL jest zwalniana, a nowa zostanie utworzona przy nastÄ™pnym wywoÄąâ€šaniu `update()`.
## `void Texture::resize(const Size& size)`

Zmienia rozmiar istniejÄ…cej tekstury, ponownie alokujÄ…c dla niej pamiÄ™Ä‡ w GPU za pomocÄ… `glTexImage2D` z `nullptr` jako danymi pikseli.
## `void Texture::update()`
## Opis semantyczny
Kluczowa metoda, ktĂłra dba o to, aby obiekt tekstury w OpenGL byÄąâ€š poprawnie zainicjalizowany i skonfigurowany. Musi byÄ‡ wywoÄąâ€šywana przed pierwszym uÄąÄ˝yciem tekstury.
## DziaÄąâ€šanie
1.  **JeÄąâ€şli tekstura nie istnieje (`m_id == 0`)**:
    -   Generuje nowe ID tekstury (`glGenTextures`).
    -   Bindowanie teksturÄ™.
    -   JeÄąâ€şli `m_image` istnieje, przesyÄąâ€ša jego dane pikseli do GPU za pomocÄ… `setupPixels`, generujÄ…c mipmapy, jeÄąâ€şli to wymagane. NastÄ™pnie zwalnia `m_image`, aby oszczÄ™dzaÄ‡ RAM.
    -   JeÄąâ€şli nie ma obrazu, tworzy pustÄ… teksturÄ™.
2.  **JeÄąâ€şli `m_needsUpdate` jest `true`**:
    -   Bindowanie teksturÄ™.
    -   Ustawia parametry zawijania (`setupWrap`).
    -   Ustawia parametry filtrowania (`setupFilters`).
    -   Aktualizuje macierz transformacji (`setupTranformMatrix`).
    -   Resetuje flagÄ™ `m_needsUpdate`.
## `void Texture::setSmooth(bool smooth)` i `void Texture::setRepeat(bool repeat)`

UstawiajÄ… flagi, ktĂłre zostanÄ… zastosowane do parametrĂłw tekstury (`GL_TEXTURE_MIN/MAG_FILTER`, `GL_TEXTURE_WRAP_S/T`) podczas nastÄ™pnego wywoÄąâ€šania `update()`.
## Metody `setup...()`

Prywatne metody pomocnicze, ktĂłre wywoÄąâ€šujÄ… odpowiednie funkcje OpenGL do konfiguracji tekstury:
-   `setupSize()`: Sprawdza, czy rozmiar nie przekracza limitĂłw GPU.
-   `setupWrap()`: Ustawia `glTexParameteri` dla `GL_TEXTURE_WRAP_S/T`.
-   `setupFilters()`: Ustawia `glTexParameteri` dla `GL_TEXTURE_MIN/MAG_FILTER`.
-   `setupTranformMatrix()`: Oblicza macierz do transformacji wspĂłÄąâ€šrzÄ™dnych tekstury (np. w celu odwrĂłcenia jej w osi Y).
-   `setupPixels()`: WywoÄąâ€šuje `glTexImage2D` do przesÄąâ€šania danych pikseli.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/texture.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/graphics.h`: Do operacji OpenGL i sprawdzania limitĂłw.
-   `framework/graphics/image.h`: UÄąÄ˝ywana jako ÄąĹźrĂłdÄąâ€šo danych pikseli.
-   Jest klasÄ… bazowÄ… dla `AnimatedTexture`.
-   Jest tworzona i zarzÄ…dzana przez `TextureManager`.

---
# Ä‘Ĺşâ€śâ€ž texture.h
## Opis ogĂłlny

Plik `texture.h` deklaruje klasÄ™ `Texture`, ktĂłra jest obiektowym interfejsem do zarzÄ…dzania teksturami w OpenGL.
## Klasa `Texture`
## Opis semantyczny
`Texture` enkapsuluje ID tekstury w OpenGL oraz jej wÄąâ€šaÄąâ€şciwoÄąâ€şci, takie jak rozmiar, wygÄąâ€šadzanie (filtrowanie), powtarzanie (wrapping) i mipmapy. Dostarcza metody do tworzenia tekstury z obiektu `Image` lub jako pustej tekstury (np. dla bufora ramki). Metoda `update()` jest kluczowa i synchronizuje stan obiektu C++ z rzeczywistym stanem tekstury w pamiÄ™ci GPU.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Texture(...)` | Konstruktory. |
| `virtual ~Texture()` | Destruktor. |
| `virtual void replace(...)` | ZastÄ™puje zawartoÄąâ€şÄ‡ tekstury nowym obrazem. |
| `void resize(...)` | Zmienia rozmiar tekstury. |
| `virtual void update()` | Tworzy lub aktualizuje parametry tekstury w OpenGL. |
| `virtual void setUpsideDown(...)` | Ustawia, czy tekstura ma byÄ‡ odwrĂłcona. |
| `virtual void setSmooth(...)` | Ustawia wygÄąâ€šadzanie (filtrowanie liniowe/najbliÄąÄ˝szego sÄ…siada). |
| `virtual void setRepeat(...)` | Ustawia tryb powtarzania. |
| `virtual bool buildHardwareMipmaps()` | WÄąâ€šÄ…cza generowanie mipmap przez GPU. |
| `uint getId()` | Zwraca ID tekstury w OpenGL. |
| `uint getUniqueId()` | Zwraca unikalne ID obiektu w aplikacji. |
| `const Size& getSize()` | Zwraca rozmiar tekstury. |
| `const Matrix3& getTransformMatrix()` | Zwraca macierz transformacji dla wspĂłÄąâ€šrzÄ™dnych tekstury. |
| `bool isEmpty()` | Sprawdza, czy tekstura jest pusta. |
| `bool canCache()` | Zwraca `true`, jeÄąâ€şli teksturÄ™ moÄąÄ˝na umieÄąâ€şciÄ‡ w atlasie. |
| `virtual bool isAnimatedTexture()` | Zwraca `false` (przesÄąâ€šaniane przez `AnimatedTexture`). |
## Zmienne chronione

-   `m_id`: ID tekstury w OpenGL.
-   `m_uniqueId`: Unikalne ID w aplikacji.
-   `m_size`: Rozmiar tekstury.
-   `m_transformMatrix`: Macierz transformacji.
-   `m_hasMipmaps`, `m_smooth`, `m_upsideDown`, `m_repeat`, ...: Flagi stanu.
-   `m_image`: WskaÄąĹźnik na `Image`, uÄąÄ˝ywany tylko podczas tworzenia tekstury.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Definicje typĂłw, np. `ImagePtr`.
-   Jest klasÄ… bazowÄ… dla `AnimatedTexture`.
-   Jest tworzona i zarzÄ…dzana przez `TextureManager`.
-   Jest uÄąÄ˝ywana przez `Painter`, `FrameBuffer`, `UIWidget` i inne komponenty do rysowania.

---
# Ä‘Ĺşâ€śâ€ž texturemanager.cpp
## Opis ogĂłlny

Plik `texturemanager.cpp` zawiera implementacjÄ™ klasy `TextureManager`, ktĂłra jest singletonem (`g_textures`) odpowiedzialnym za zarzÄ…dzanie teksturami w aplikacji. DziaÄąâ€ša jako cache, aby zapobiec wielokrotnemu Äąâ€šadowaniu tych samych tekstur z dysku.
## Zmienne globalne
## `g_textures`

Globalna instancja `TextureManager`.

`$fenceInfo
TextureManager g_textures;
```
## Klasa `TextureManager`
## `void TextureManager::init()` i `void TextureManager::terminate()`

Metody do inicjalizacji i zwalniania menedÄąÄ˝era. `terminate()` czyÄąâ€şci wszystkie zbuforowane tekstury.
## `void TextureManager::clearCache()`

CzyÄąâ€şci wszystkie zbuforowane tekstury, w tym animowane.
## `void TextureManager::reload()`

PrzeÄąâ€šadowuje wszystkie zaÄąâ€šadowane tekstury z ich oryginalnych plikĂłw. Jest to przydatne do "hot-reloading" zasobĂłw.
## `TexturePtr TextureManager::getTexture(const std::string& fileName)`
## Opis semantyczny
GÄąâ€šĂłwna metoda do pobierania tekstury. DziaÄąâ€ša jak "get-or-load".
## DziaÄąâ€šanie
1.  Sprawdza, czy tekstura o podanej nazwie (`fileName`) jest juÄąÄ˝ w cache (`m_textures`). JeÄąâ€şli tak, zwraca jÄ….
2.  JeÄąâ€şli nie, rozwiÄ…zuje peÄąâ€šnÄ… Äąâ€şcieÄąÄ˝kÄ™ do pliku za pomocÄ… `g_resources`.
3.  Ponownie sprawdza cache, tym razem z peÄąâ€šnÄ… Äąâ€şcieÄąÄ˝kÄ….
4.  JeÄąâ€şli tekstury wciÄ…ÄąÄ˝ nie ma, prĂłbuje jÄ… zaÄąâ€šadowaÄ‡ z pliku:
    -   Odczytuje plik do strumienia w pamiÄ™ci.
    -   WywoÄąâ€šuje `loadTexture()`, aby sparsowaÄ‡ dane (APNG) i utworzyÄ‡ obiekt `Texture` lub `AnimatedTexture`.
5.  JeÄąâ€şli Äąâ€šadowanie siÄ™ powiedzie, dodaje nowÄ… teksturÄ™ do cache pod obiema nazwami (oryginalnÄ… i peÄąâ€šnÄ… Äąâ€şcieÄąÄ˝kÄ…) i zwraca jÄ….
6.  W przypadku bÄąâ€šÄ™du, loguje go i zwraca `nullptr`.
## `TexturePtr TextureManager::loadTexture(std::stringstream& file, const std::string& source)`

Metoda pomocnicza, ktĂłra parsuje strumieÄąâ€ž danych APNG za pomocÄ… `load_apng`.
-   JeÄąâ€şli plik zawiera jednÄ… klatkÄ™, tworzy `Texture`.
-   JeÄąâ€şli plik zawiera wiele klatek, tworzy `AnimatedTexture`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/texturemanager.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/animatedtexture.h`, `image.h`: Do tworzenia obiektĂłw tekstur.
-   `framework/core/resourcemanager.h`: Do odczytywania plikĂłw tekstur.
-   `framework/graphics/apngloader.h`: Do parsowania formatu APNG.
-   Jest uÄąÄ˝ywana przez `UIWidget`, `BitmapFont` i inne komponenty, ktĂłre potrzebujÄ… wyÄąâ€şwietlaÄ‡ obrazy.

---
# Ä‘Ĺşâ€śâ€ž vertexarray.h
## Opis ogĂłlny

Plik `vertexarray.h` deklaruje klasÄ™ `VertexArray`, ktĂłra jest prostym, dynamicznym buforem na wspĂłÄąâ€šrzÄ™dne wierzchoÄąâ€škĂłw (`float`). SÄąâ€šuÄąÄ˝y do gromadzenia geometrii przed wysÄąâ€šaniem jej do renderowania.
## Klasa `VertexArray`
## Opis semantyczny
`VertexArray` to opakowanie na `DataBuffer<float>`, zoptymalizowane do przechowywania par wspĂłÄąâ€šrzÄ™dnych (X, Y). UdostÄ™pnia metody do dodawania popularnych prymitywĂłw 2D (trĂłjkÄ…ty, prostokÄ…ty) i moÄąÄ˝e opcjonalnie przenieÄąâ€şÄ‡ swoje dane do sprzÄ™towego bufora VBO (`HardwareBuffer`) w celu zwiÄ™kszenia wydajnoÄąâ€şci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `VertexArray()` | Konstruktor. |
| `~VertexArray()` | Destruktor, zwalnia `m_hardwareBuffer`. |
| `VertexArray(VertexArray& c)` | Konstruktor kopiujÄ…cy (kopiuje tylko dane z `m_buffer`, nie `m_hardwareBuffer`). |
| `void addVertex(float x, float y)` | Dodaje pojedynczy wierzchoÄąâ€šek. |
| `void addTriangle(...)` | Dodaje trzy wierzchoÄąâ€ški tworzÄ…ce trĂłjkÄ…t. |
| `void addRect(...)` | Dodaje szeÄąâ€şÄ‡ wierzchoÄąâ€škĂłw tworzÄ…cych dwa trĂłjkÄ…ty (prostokÄ…t). |
| `void addQuad(...)` | Dodaje cztery wierzchoÄąâ€ški tworzÄ…ce czworokÄ…t (dla `TriangleStrip`). |
| `void clear()` | CzyÄąâ€şci bufor. |
| `float *vertices() const` | Zwraca wskaÄąĹźnik na surowe dane. |
| `int vertexCount() const` | Zwraca liczbÄ™ wierzchoÄąâ€škĂłw. |
| `void cache()` | Kopiuje dane z bufora RAM do bufora VBO na karcie graficznej. |
| `bool isCached()` | Zwraca `true`, jeÄąâ€şli dane zostaÄąâ€šy skopiowane do VBO. |
| `HardwareBuffer* getHardwareCache()` | Zwraca wskaÄąĹźnik na obiekt `HardwareBuffer`. |
## Zmienne prywatne

-   `m_buffer`: Bufor `DataBuffer<float>` przechowujÄ…cy wspĂłÄąâ€šrzÄ™dne.
-   `m_hardwareBuffer`: WskaÄąĹźnik na opcjonalny bufor VBO.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/graphics/hardwarebuffer.h`: Do sprzÄ™towego keszowania.
-   `framework/util/databuffer.h`: UÄąÄ˝ywana jako wewnÄ™trzny kontener.
-   Jest podstawowym skÄąâ€šadnikiem `CoordsBuffer`, ktĂłry uÄąÄ˝ywa dwĂłch instancji `VertexArray` (jednej na pozycje, drugiej na wspĂłÄąâ€šrzÄ™dne tekstur).

---
# Ä‘Ĺşâ€śâ€ž texturemanager.h
## Opis ogĂłlny

Plik `texturemanager.h` deklaruje klasÄ™ `TextureManager`, ktĂłra jest singletonem (`g_textures`) odpowiedzialnym za zarzÄ…dzanie (Äąâ€šadowanie, cachowanie, zwalnianie) teksturami w aplikacji.
## Klasa `TextureManager`
## Opis semantyczny
`TextureManager` dziaÄąâ€ša jako centralne repozytorium tekstur. Gdy jakaÄąâ€ş czÄ™Äąâ€şÄ‡ kodu prosi o teksturÄ™ z pliku, menedÄąÄ˝er najpierw sprawdza, czy nie zostaÄąâ€ša ona juÄąÄ˝ zaÄąâ€šadowana. JeÄąâ€şli tak, zwraca istniejÄ…cÄ… instancjÄ™. JeÄąâ€şli nie, Äąâ€šaduje jÄ… z dysku, zapisuje w swojej pamiÄ™ci podrÄ™cznej (cache) i zwraca. Zapobiega to wielokrotnemu Äąâ€šadowaniu tych samych zasobĂłw i marnowaniu pamiÄ™ci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedÄąÄ˝era. |
| `void terminate()` | Zwalnia wszystkie zaÄąâ€šadowane tekstury. |
| `void clearCache()` | CzyÄąâ€şci pamiÄ™Ä‡ podrÄ™cznÄ… tekstur. |
| `void reload()` | PrzeÄąâ€šadowuje wszystkie tekstury z plikĂłw, umoÄąÄ˝liwiajÄ…c "hot-reloading". |
| `void preload(const std::string& fileName)` | SkrĂłt do `getTexture`, ktĂłry Äąâ€šaduje teksturÄ™ do cache, ale nie zwraca jej. |
| `TexturePtr getTexture(const std::string& fileName)` | Pobiera teksturÄ™. JeÄąâ€şli nie ma jej w cache, Äąâ€šaduje jÄ…. |
| `TexturePtr loadTexture(...)` | Niskopoziomowa metoda do tworzenia tekstury ze strumienia danych. |
## Zmienne prywatne

-   `m_textures`: Mapa (`std::unordered_map`) przechowujÄ…ca zaÄąâ€šadowane tekstury, gdzie kluczem jest nazwa pliku.
-   `m_animatedTextures`: Wektor przechowujÄ…cy wskaÄąĹźniki do animowanych tekstur, prawdopodobnie w celu ich aktualizacji.
-   `m_liveReloadEvent`: WskaÄąĹźnik na zdarzenie, prawdopodobnie do implementacji "live reload".
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/texture.h`: Definicja `Texture`.
-   `framework/core/declarations.h`: Deklaracje `ScheduledEventPtr`.
-   Jest to kluczowy menedÄąÄ˝er w systemie graficznym, uÄąÄ˝ywany przez wszystkie komponenty, ktĂłre muszÄ… wyÄąâ€şwietlaÄ‡ obrazy, takie jak `UIWidget` czy `BitmapFont`.

---
# Ä‘Ĺşâ€śâ€ž textrender.h
## Opis ogĂłlny

Plik `textrender.h` deklaruje klasÄ™ `TextRender`, ktĂłra jest systemem do optymalizacji renderowania tekstu. DziaÄąâ€ša jako globalny cache dla geometrii tekstu.
## Struktura `TextRenderCache`

Przechowuje wszystkie informacje potrzebne do narysowania tekstu, w tym gotowy `CoordsBuffer` z geometriÄ….

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `font` | `BitmapFontPtr` | Font uÄąÄ˝yty do wygenerowania geometrii (zwalniany po pierwszym uÄąÄ˝yciu). |
| `text` | `std::string` | Tekst (zwalniany po pierwszym uÄąÄ˝yciu). |
| `size` | `Size` | Rozmiar obszaru, w ktĂłrym tekst ma byÄ‡ rysowany. |
| `align` | `Fw::AlignmentFlag` | WyrĂłwnanie tekstu. |
| `texture` | `TexturePtr` | Tekstura fontu. |
| `coords` | `CoordsBuffer` | Zbuforowana geometria tekstu. |
| `lastUse` | `ticks_t` | Czas ostatniego uÄąÄ˝ycia (do czyszczenia cache). |
## Klasa `TextRender`
## Opis semantyczny
`TextRender` minimalizuje narzut na CPU zwiÄ…zany z obliczaniem pozycji poszczegĂłlnych glifĂłw dla czÄ™sto wyÄąâ€şwietlanych tekstĂłw. Zamiast przeliczaÄ‡ geometriÄ™ w kaÄąÄ˝dej klatce, robi to tylko raz, a nastÄ™pnie przechowuje wynik w cache.
## StaÄąâ€še

-   `INDEXES`: Liczba "kubeÄąâ€škĂłw" w hash mapie. UÄąÄ˝ycie wielu map z osobnymi mutexami ma na celu zmniejszenie rywalizacji o zasoby w Äąâ€şrodowisku wielowÄ…tkowym.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` / `terminate()` | Inicjalizuje i zwalnia system. |
| `void poll()` | CzyÄąâ€şci cache z nieuÄąÄ˝ywanych wpisĂłw. |
| `uint64_t addText(...)` | Generuje hash dla tekstu i tworzy dla niego wpis w cache. |
| `void drawText(...)` | Rysuje tekst, uÄąÄ˝ywajÄ…c skeszowanej geometrii. |
| `void drawColoredText(...)` | Rysuje tekst wielokolorowy. |
## Zmienne prywatne

-   `m_cache[INDEXES]`: Tablica map, ktĂłra przechowuje skeszowane dane.
-   `m_mutex[INDEXES]`: Tablica mutexĂłw, po jednym dla kaÄąÄ˝dej mapy w `m_cache`.
## Zmienne globalne

-   `g_text`: Globalna instancja `TextRender`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/graphics/bitmapfont.h`, `coordsbuffer.h`: Kluczowe struktury danych.
-   `framework/core/clock.h`: Do Äąâ€şledzenia czasu ostatniego uÄąÄ˝ycia.
-   Jest uÄąÄ˝ywana przez `DrawQueueItemText` do renderowania tekstu w zoptymalizowany sposĂłb.

---
# Ä‘Ĺşâ€śâ€ž outfits.h
## Opis ogĂłlny

Plik `outfits.h` zawiera kod ÄąĹźrĂłdÄąâ€šowy shaderĂłw w postaci staÄąâ€šych stringĂłw, ktĂłre sÄ… uÄąÄ˝ywane do renderowania strojĂłw postaci z niestandardowymi kolorami.
## Shadery
## `glslAdvancedOutfitVertexShader`
## Opis
Shader wierzchoÄąâ€škĂłw dla zaawansowanego renderowania strojĂłw.
## DziaÄąâ€šanie
1.  **Atrybuty**: Przyjmuje pozycjÄ™ wierzchoÄąâ€ška (`a_Vertex`) i jego wspĂłÄąâ€šrzÄ™dne na teksturze (`a_TexCoord`).
2.  **Uniformy**:
    -   `u_ProjectionMatrix`, `u_TransformMatrix`: Standardowe macierze do transformacji pozycji.
    -   `u_TextureMatrix`: Do transformacji wspĂłÄąâ€šrzÄ™dnych tekstury.
    -   `u_Offset`, `u_Resolution`: Dodatkowe dane, prawdopodobnie do efektĂłw.
3.  **Varying**:
    -   Przekazuje do shadera fragmentĂłw trzy zestawy wspĂłÄąâ€šrzÄ™dnych tekstury:
        -   `v_TexCoord`: Podstawowe.
        -   `v_TexCoord2`: PrzesuniÄ™te o `u_Offset`.
        -   `v_TexCoord3`: WspĂłÄąâ€šrzÄ™dne oparte na rozdzielczoÄąâ€şci.
4.  Oblicza finalnÄ… pozycjÄ™ wierzchoÄąâ€ška na ekranie (`gl_Position`).
## `glslAdvancedOutfitFragmentShader`
## Opis
Shader fragmentĂłw (pikseli) dla zaawansowanego renderowania strojĂłw.
## DziaÄąâ€šanie
1.  Pobiera kolor piksela z gÄąâ€šĂłwnej tekstury (`u_Tex0`) na podstawie `v_TexCoord`.
2.  Sprawdza kolor piksela z tej samej tekstury, ale w przesuniÄ™tym miejscu (`v_TexCoord2`). JeÄąâ€şli alfa tego piksela jest wiÄ™ksza od progu, mnoÄąÄ˝y finalny kolor przez ÄąÄ˝ĂłÄąâ€šty (`vec4(1.0, 1.0, 0.0, 1.0)`), tworzÄ…c efekt podÄąâ€şwietlenia lub konturu.
3.  Odrzuca piksel (`discard`), jeÄąâ€şli jego alfa jest zbyt niska.

> **NOTE**: Kod shaderĂłw w tym pliku wydaje siÄ™ byÄ‡ eksperymentalny lub nie w peÄąâ€šni zaimplementowany w reszcie kodu. Prawdziwy shader do strojĂłw znajduje siÄ™ w `shadersources.h`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest doÄąâ€šÄ…czany przez `shaders.h`.
-   Kod jest przeznaczony do uÄąÄ˝ycia przez `PainterShaderProgram`.

---
# Ä‘Ĺşâ€śâ€ž newshader.h
## Opis ogĂłlny

Plik `newshader.h` zawiera kod ÄąĹźrĂłdÄąâ€šowy dla nowego, zoptymalizowanego systemu renderowania opartego na `DrawCache`. Definiuje shadery wierzchoÄąâ€škĂłw i fragmentĂłw do rysowania geometrii wsadowej, tekstu i linii.
## Shadery
## `newVertexShader`
## Opis
Shader wierzchoÄąâ€škĂłw dla `DrawCache`.
## DziaÄąâ€šanie
1.  **Atrybuty**: Przyjmuje pozycjÄ™ (`a_Vertex`), wspĂłÄąâ€šrzÄ™dne tekstury (`a_TexCoord`) i **kolor (`a_Color`)** dla kaÄąÄ˝dego wierzchoÄąâ€ška.
2.  **Varying**: Przekazuje wspĂłÄąâ€šrzÄ™dne tekstury i kolor do shadera fragmentĂłw.
3.  Oblicza pozycjÄ™ wierzchoÄąâ€ška.
## `newFragmentShader`
## Opis
Shader fragmentĂłw dla `DrawCache`.
## DziaÄąâ€šanie
1.  Sprawdza, czy wspĂłÄąâ€šrzÄ™dna X tekstury jest mniejsza od 0. JeÄąâ€şli tak, oznacza to, ÄąÄ˝e wierzchoÄąâ€šek nie ma tekstury i jego kolorem jest po prostu `v_Color`.
2.  W przeciwnym razie, pobiera kolor z tekstury atlasu (`u_Atlas`) i mnoÄąÄ˝y go przez kolor wierzchoÄąâ€ška (`v_Color`).
## `textVertexShader` i `textFragmentShader`

Shadery zoptymalizowane do rysowania tekstu. WierzchoÄąâ€ški sÄ… przesuwane o `u_Offset` (pozycja tekstu na ekranie), a kolor jest jednolity dla caÄąâ€šego tekstu (`u_Color`).
## `lineVertexShader` i `lineFragmentShader`

Proste shadery do rysowania linii. Shader fragmentĂłw po prostu ustawia jednolity kolor `u_Color`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest doÄąâ€šÄ…czany przez `shaders.h`.
-   Shadery te sÄ… kompilowane i uÄąÄ˝ywane przez `Painter` do implementacji `drawCache`, `drawText` i `drawLine`.

---
# Ä‘Ĺşâ€śâ€ž shaders.h
## Opis ogĂłlny

Plik `shaders.h` jest plikiem nagÄąâ€šĂłwkowym, ktĂłry agreguje wszystkie pliki zawierajÄ…ce kod ÄąĹźrĂłdÄąâ€šowy shaderĂłw. SÄąâ€šuÄąÄ˝y jako pojedynczy punkt doÄąâ€šÄ…czania dla wszystkich predefiniowanych shaderĂłw w systemie.
## ZawartoÄąâ€şÄ‡

DoÄąâ€šÄ…cza nastÄ™pujÄ…ce pliki:
-   `newshader.h`: Zawiera shadery dla nowego, wsadowego systemu renderowania (`DrawCache`).
-   `shadersources.h`: Zawiera kod ÄąĹźrĂłdÄąâ€šowy dla standardowych shaderĂłw uÄąÄ˝ywanych przez `Painter` (rysowanie tekstur, jednolitych kolorĂłw, strojĂłw).
-   `outfits.h`: Zawiera eksperymentalne/alternatywne shadery do strojĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest doÄąâ€šÄ…czany przez `painter.cpp` w celu uzyskania dostÄ™pu do kodu ÄąĹźrĂłdÄąâ€šowego shaderĂłw, ktĂłre sÄ… kompilowane podczas inicjalizacji `Painter`.

---
# Ä‘Ĺşâ€śâ€ž shadersources.h
## Opis ogĂłlny

Plik `shadersources.h` zawiera kod ÄąĹźrĂłdÄąâ€šowy w GLSL dla standardowych shaderĂłw uÄąÄ˝ywanych przez klasÄ™ `Painter`. SÄ… one zdefiniowane jako staÄąâ€še stringi i kompilowane w trakcie dziaÄąâ€šania programu.
## Shadery
## `glslMainVertexShader` i `glslMainWithTexCoordsVertexShader`

SÄ… to "szablony" dla shaderĂłw wierzchoÄąâ€škĂłw. DefiniujÄ… one funkcjÄ™ `main`, ktĂłra wywoÄąâ€šuje `calculatePosition()`. Wersja `WithTexCoords` dodatkowo przekazuje wspĂłÄąâ€šrzÄ™dne tekstury do shadera fragmentĂłw.
## `glslPositionOnlyVertexShader`

Jest to implementacja `calculatePosition()`. Oblicza ona finalnÄ… pozycjÄ™ wierzchoÄąâ€ška, mnoÄąÄ˝Ä…c jego pozycjÄ™ przez macierze transformacji i projekcji. UwzglÄ™dnia rĂłwnieÄąÄ˝ gÄąâ€šÄ™biÄ™ (`u_Depth`).
## `glslMainFragmentShader`

Szablon dla shaderĂłw fragmentĂłw. WywoÄąâ€šuje `calculatePixel()` i odrzuca piksele o niskiej wartoÄąâ€şci alfa, jeÄąâ€şli `u_Depth > 0`.
## `glslTextureSrcFragmentShader`

Implementacja `calculatePixel()`, ktĂłra pobiera kolor z tekstury (`u_Tex0`) i mnoÄąÄ˝y go przez jednolity kolor (`u_Color`).
## `glslSolidColorFragmentShader`

Implementacja `calculatePixel()`, ktĂłra zwraca jednolity kolor (`u_Color`).
## `glslSolidColorOnTextureFragmentShader`

Implementacja `calculatePixel()`, ktĂłra rysuje jednolity kolor (`u_Color`) tylko tam, gdzie tekstura (`u_Tex0`) nie jest w peÄąâ€šni przezroczysta.
## `glslOutfitVertexShader` i `glslOutfitFragmentShader`

Shadery do renderowania strojĂłw.
-   **Shader wierzchoÄąâ€škĂłw**: Przekazuje dwie pary wspĂłÄąâ€šrzÄ™dnych tekstury â€“ normalne (`v_TexCoord`) i przesuniÄ™te o `u_Offset` (`v_TexCoord2`).
-   **Shader fragmentĂłw**:
    1.  Pobiera kolor bazowy z `v_TexCoord`.
    2.  Pobiera kolor "maski" z `v_TexCoord2`.
    3.  Na podstawie koloru maski (sprawdzajÄ…c, ktĂłry kanaÄąâ€š R, G lub B jest dominujÄ…cy), mnoÄąÄ˝y kolor bazowy przez jeden z czterech kolorĂłw przekazanych w macierzy `u_Color`. Pozwala to na dynamiczne kolorowanie rĂłÄąÄ˝nych czÄ™Äąâ€şci stroju.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest doÄąâ€šÄ…czany przez `shaders.h`.
-   Kod jest uÄąÄ˝ywany w `painter.cpp` do tworzenia domyÄąâ€şlnych programĂłw shaderĂłw.

---
# Ä‘Ĺşâ€śâ€ž http.cpp
## Opis ogĂłlny

Plik `http.cpp` implementuje klasÄ™ `Http`, ktĂłra jest singletonem (`g_http`) odpowiedzialnym za obsÄąâ€šugÄ™ zapytaÄąâ€ž HTTP/HTTPS oraz poÄąâ€šÄ…czeÄąâ€ž WebSocket. DziaÄąâ€ša asynchronicznie, wykorzystujÄ…c bibliotekÄ™ Boost.Asio do operacji sieciowych w osobnym wÄ…tku.
## Zmienne globalne
## `g_http`

Globalna instancja `Http`.
## Klasa `Http`
## `void Http::init()`

Inicjalizuje menedÄąÄ˝era. Tworzy i uruchamia osobny wÄ…tek, w ktĂłrym bÄ™dzie dziaÄąâ€šaÄ‡ `boost::asio::io_service` (`m_ios`), obsÄąâ€šugujÄ…c wszystkie operacje sieciowe.
## `void Http::terminate()`

Zamyka menedÄąÄ˝era. Zatrzymuje `io_service`, anuluje wszystkie bieÄąÄ˝Ä…ce operacje i czeka na zakoÄąâ€žczenie wÄ…tku sieciowego.
## `int Http::get(const std::string& url, int timeout)`
## Opis semantyczny
WysyÄąâ€ša asynchroniczne zapytanie HTTP GET.
## DziaÄąâ€šanie
1.  Generuje unikalne ID operacji.
2.  Dodaje zadanie do `m_ios`, ktĂłre tworzy obiekt `HttpSession`.
3.  `HttpSession` wykonuje zapytanie w wÄ…tku sieciowym.
4.  Wyniki (postÄ™p, bÄąâ€šÄ…d, odpowiedÄąĹź) sÄ… przekazywane z powrotem do gÄąâ€šĂłwnego wÄ…tku za pomocÄ… `g_dispatcher` i wywoÄąâ€šywane sÄ… odpowiednie callbacki w Lua (`g_http.onGetProgress`, `g_http.onGet`).
## `int Http::post(...)`

DziaÄąâ€ša analogicznie do `get`, ale wysyÄąâ€ša zapytanie HTTP POST z podanymi danymi (`data`).
## `int Http::download(...)`

Specjalna wersja `get`, ktĂłra dodatkowo zapisuje pobrane dane w wewnÄ™trznej mapie `m_downloads`. Pozwala to na dostÄ™p do pobranych plikĂłw przez `ResourceManager` za pomocÄ… wirtualnej Äąâ€şcieÄąÄ˝ki `/downloads/...`.
## `int Http::ws(...)`

Inicjuje asynchroniczne poÄąâ€šÄ…czenie WebSocket. Tworzy obiekt `WebsocketSession`, ktĂłry zarzÄ…dza cyklem ÄąÄ˝ycia poÄąâ€šÄ…czenia. Callbacki Lua (`onWsOpen`, `onWsMessage`, `onWsClose`, `onWsError`) sÄ… wywoÄąâ€šywane w odpowiedzi na zdarzenia z gniazda.
## `bool Http::wsSend(int operationId, std::string message)`

WysyÄąâ€ša wiadomoÄąâ€şÄ‡ przez istniejÄ…ce poÄąâ€šÄ…czenie WebSocket o danym `operationId`.
## `bool Http::cancel(int id)`

Anuluje operacjÄ™ (HTTP lub WebSocket) o podanym ID.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/http/http.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/http/session.h`, `websocket.h`: Implementacje sesji HTTP i WebSocket (niedostÄ™pne dla Emscripten).
-   `framework/luaengine/luainterface.h`: Do wywoÄąâ€šywania callbackĂłw w Lua.
-   `framework/core/eventdispatcher.h`: Do przekazywania wynikĂłw z wÄ…tku sieciowego do wÄ…tku gÄąâ€šĂłwnego.
-   `boost/asio`, `boost/beast`: Podstawowe biblioteki do obsÄąâ€šugi sieci.

---
# Ä‘Ĺşâ€śâ€ž websocket.h
## Opis ogĂłlny

Plik `websocket.h` deklaruje klasÄ™ `WebsocketSession`, ktĂłra zarzÄ…dza pojedynczym poÄąâ€šÄ…czeniem WebSocket. Plik ten (i jego implementacja) jest wyÄąâ€šÄ…czony z kompilacji dla Emscripten.
## Typy wyliczeniowe i definicje

-   `enum WebsocketCallbackType`: Definiuje typy zdarzeÄąâ€ž dla callbacka (`WEBSOCKET_OPEN`, `WEBSOCKET_MESSAGE`, `WEBSOCKET_ERROR`, `WEBSOCKET_CLOSE`).
-   `using WebsocketSession_cb`: Alias dla typu funkcji zwrotnej.
## Klasa `WebsocketSession`
## Opis semantyczny
`WebsocketSession` enkapsuluje caÄąâ€šÄ… logikÄ™ zwiÄ…zanÄ… z nawiÄ…zywaniem, utrzymywaniem i zamykaniem poÄąâ€šÄ…czenia WebSocket, wÄąâ€šÄ…czajÄ…c w to obsÄąâ€šugÄ™ protokoÄąâ€šu (handshake) i szyfrowania (WSS). DziaÄąâ€ša w peÄąâ€šni asynchronicznie w oparciu o Boost.Asio.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `WebsocketSession(...)` | Konstruktor. |
| `void start()` | Rozpoczyna proces nawiÄ…zywania poÄąâ€šÄ…czenia (rozwiÄ…zywanie nazwy DNS, Äąâ€šÄ…czenie, handshake). |
| `void send(std::string data)` | Dodaje wiadomoÄąâ€şÄ‡ do kolejki wysyÄąâ€šania. |
| `void close()` | Zamyka poÄąâ€šÄ…czenie. |
## Zmienne prywatne

-   `m_service`: Referencja do `io_service`.
-   `m_url`, `m_agent`: URL i User-Agent.
-   `m_resolver`: Do rozwiÄ…zywania nazw DNS.
-   `m_callback`: Funkcja zwrotna do powiadamiania o zdarzeniach.
-   `m_result`: WskaÄąĹźnik na `HttpResult` do przechowywania stanu.
-   `m_timer`: Timer do obsÄąâ€šugi timeoutĂłw.
-   `m_socket`: Gniazdo WebSocket dla poÄąâ€šÄ…czeÄąâ€ž nieszyfrowanych (WS).
-   `m_ssl`: Gniazdo WebSocket dla poÄąâ€šÄ…czeÄąâ€ž szyfrowanych (WSS).
-   `m_context`: Kontekst SSL.
-   `m_streambuf`: Bufor na przychodzÄ…ce dane.
-   `m_sendQueue`: Kolejka wiadomoÄąâ€şci do wysÄąâ€šania.
## Metody prywatne (`on_...`)

-   SÄ… to handlery wywoÄąâ€šywane przez Boost.Asio po zakoÄąâ€žczeniu operacji asynchronicznych (np. `on_resolve`, `on_connect`, `on_handshake`, `on_read`, `on_send`). ImplementujÄ… one logikÄ™ maszyny stanĂłw poÄąâ€šÄ…czenia.
-   `onError`: Centralna funkcja do obsÄąâ€šugi bÄąâ€šÄ™dĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   `boost/asio`, `boost/beast`: Kluczowe biblioteki do obsÄąâ€šugi sieci.
-   Jest tworzona i zarzÄ…dzana przez klasÄ™ `Http`.

---
# Ä‘Ĺşâ€śâ€ž http.h
## Opis ogĂłlny

Plik `http.h` deklaruje klasÄ™ `Http`, ktĂłra jest singletonem (`g_http`) i stanowi gÄąâ€šĂłwny interfejs do wykonywania operacji sieciowych opartych na protokoÄąâ€šach HTTP/HTTPS i WebSocket.
## Klasa `Http`
## Opis semantyczny
`Http` zarzÄ…dza pulÄ… operacji sieciowych, ktĂłre sÄ… wykonywane asynchronicznie w dedykowanym wÄ…tku. UdostÄ™pnia proste API do wysyÄąâ€šania zapytaÄąâ€ž GET, POST, pobierania plikĂłw oraz nawiÄ…zywania poÄąâ€šÄ…czeÄąâ€ž WebSocket. Interakcja z resztÄ… aplikacji (gÄąâ€šĂłwnie ze skryptami Lua) odbywa siÄ™ poprzez system callbackĂłw.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Http()` | Konstruktor, inicjalizuje `io_context` i `work_guard`. |
| `void init()` | Uruchamia wÄ…tek sieciowy. |
| `void terminate()` | Zatrzymuje wÄ…tek sieciowy i anuluje wszystkie operacje. |
| `int get(...)` | Inicjuje asynchroniczne zapytanie GET. |
| `int post(...)` | Inicjuje asynchroniczne zapytanie POST. |
| `int download(...)` | Inicjuje asynchroniczne pobieranie pliku. |
| `int ws(...)` | Inicjuje asynchroniczne poÄąâ€šÄ…czenie WebSocket. |
| `bool wsSend(...)` | WysyÄąâ€ša dane przez istniejÄ…ce poÄąâ€šÄ…czenie WebSocket. |
| `bool wsClose(...)` | Zamyka poÄąâ€šÄ…czenie WebSocket. |
| `bool cancel(int id)` | Anuluje operacjÄ™ o podanym ID. |
| `const std::map<...>& downloads()` | Zwraca mapÄ™ pobranych plikĂłw. |
| `void clearDownloads()` | CzyÄąâ€şci mapÄ™ pobranych plikĂłw. |
| `HttpResult_ptr getFile(...)` | Pobiera dane pobranego pliku na podstawie jego Äąâ€şcieÄąÄ˝ki. |
| `void setUserAgent(...)` | Ustawia nagÄąâ€šĂłwek User-Agent dla wszystkich zapytaÄąâ€ž. |
## Zmienne prywatne

-   `m_working`: Flaga kontrolujÄ…ca dziaÄąâ€šanie wÄ…tku.
-   `m_operationId`: Licznik do generowania unikalnych ID dla operacji.
-   `m_thread`: WÄ…tek roboczy dla operacji sieciowych.
-   `m_ios`: Kontekst `io_context` z Boost.Asio.
-   `m_guard`: `work_guard` zapobiegajÄ…cy zakoÄąâ€žczeniu `m_ios.run()`, dopĂłki nie ma pracy.
-   `m_operations`: Mapa przechowujÄ…ca stan wszystkich aktywnych operacji.
-   `m_websockets`: Mapa przechowujÄ…ca aktywne sesje WebSocket.
-   `m_downloads`: Mapa przechowujÄ…ca pobrane pliki.
-   `m_userAgent`: String User-Agent.
## Zmienne globalne

-   `g_http`: Globalna instancja `Http`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   Jest uÄąÄ˝ywana w skryptach Lua (poprzez bindowania w `luafunctions.cpp`) do komunikacji z serwerami WWW, np. do pobierania aktualizacji, sprawdzania statusu serwerĂłw itp.
-   WspĂłÄąâ€špracuje z `ResourceManager` w celu udostÄ™pnienia pobranych plikĂłw przez wirtualny system plikĂłw.

---
# Ä‘Ĺşâ€śâ€ž result.h
## Opis ogĂłlny

Plik `result.h` deklaruje strukturÄ™ `HttpResult`, ktĂłra sÄąâ€šuÄąÄ˝y do przechowywania stanu i wyniku pojedynczej operacji HTTP lub WebSocket. Definiuje rĂłwnieÄąÄ˝ aliasy typĂłw dla inteligentnych wskaÄąĹźnikĂłw i funkcji zwrotnych.
## Struktura `HttpResult`
## Opis semantyczny
`HttpResult` jest kontenerem danych przekazywanym miÄ™dzy wÄ…tkiem sieciowym a wÄ…tkiem gÄąâ€šĂłwnym. Agreguje wszystkie informacje zwiÄ…zane z danym zapytaniem, takie jak URL, status, postÄ™p, dane odpowiedzi i ewentualne bÄąâ€šÄ™dy.
## Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `url` | `std::string` | Adres URL zapytania. |
| `operationId` | `int` | Unikalny identyfikator operacji. |
| `status` | `int` | Kod statusu odpowiedzi HTTP (np. 200, 404). |
| `size` | `int` | CaÄąâ€škowity rozmiar odpowiedzi (z nagÄąâ€šĂłwka Content-Length). |
| `progress` | `int` | PostÄ™p pobierania w procentach (0-100). |
| `redirects` | `int` | Licznik przekierowaÄąâ€ž. |
| `connected` | `bool` | Flaga wskazujÄ…ca, czy poÄąâ€šÄ…czenie jest aktywne. |
| `finished` | `bool` | Flaga wskazujÄ…ca, czy operacja zostaÄąâ€ša zakoÄąâ€žczona. |
| `canceled` | `bool` | Flaga wskazujÄ…ca, czy operacja zostaÄąâ€ša anulowana. |
| `postData` | `std::string` | Dane wysÄąâ€šane w zapytaniu POST. |
| `response` | `std::vector<uint8_t>`| Surowe bajty odpowiedzi. |
| `error` | `std::string` | Komunikat bÄąâ€šÄ™du, jeÄąâ€şli wystÄ…piÄąâ€š. |
| `session` | `std::weak_ptr<HttpSession>` | SÄąâ€šaby wskaÄąĹźnik do obiektu sesji, aby uniknÄ…Ä‡ cyklicznych referencji. |
## Definicje typĂłw

-   `HttpResult_ptr`: Alias dla `std::shared_ptr<HttpResult>`.
-   `HttpResult_cb`: Alias dla `std::function<void(HttpResult_ptr)>`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to podstawowa struktura danych uÄąÄ˝ywana przez `Http`, `HttpSession` i `WebsocketSession` do komunikacji i przekazywania wynikĂłw.
-   Zawiera `std::weak_ptr` do `HttpSession`, aby umoÄąÄ˝liwiÄ‡ anulowanie operacji z zewnÄ…trz bez tworzenia cyklu referencji.

---
# Ä‘Ĺşâ€śâ€ž session.cpp
## Opis ogĂłlny

Plik `session.cpp` zawiera implementacjÄ™ klasy `HttpSession`, ktĂłra zarzÄ…dza pojedynczÄ… sesjÄ… HTTP/HTTPS. Jest on wyÄąâ€šÄ…czony z kompilacji dla platformy Emscripten.
## Klasa `HttpSession`
## `void HttpSession::start()`
## Opis semantyczny
Rozpoczyna proces wysyÄąâ€šania zapytania HTTP.
## DziaÄąâ€šanie
1.  Sprawdza limit przekierowaÄąâ€ž.
2.  Parsuje URL, aby uzyskaÄ‡ protokĂłÄąâ€š, domenÄ™, port i Äąâ€şcieÄąÄ˝kÄ™.
3.  Ustawia timer (`m_timer`) na obsÄąâ€šugÄ™ timeoutu.
4.  Konfiguruje obiekt ÄąÄ˝Ä…dania `boost::beast::http::request` (metoda, nagÄąâ€šĂłwki, treÄąâ€şÄ‡).
5.  Uruchamia asynchroniczne rozwiÄ…zywanie nazwy DNS za pomocÄ… `m_resolver.async_resolve`.
## Metody `on_...()`

SÄ… to handlery (funkcje zwrotne) dla operacji asynchronicznych Boost.Asio, ktĂłre implementujÄ… maszynÄ™ stanĂłw sesji HTTP:

-   **`on_resolve`**: WywoÄąâ€šywana po rozwiÄ…zaniu nazwy DNS. Inicjuje `async_connect`.
-   **`on_connect`**: WywoÄąâ€šywana po nawiÄ…zaniu poÄąâ€šÄ…czenia TCP.
    -   JeÄąâ€şli protokĂłÄąâ€š to HTTPS, inicjalizuje kontekst SSL i wykonuje `async_handshake`.
    -   WysyÄąâ€ša ÄąÄ˝Ä…danie HTTP za pomocÄ… `boost::beast::http::async_write`.
-   **`on_request_sent`**: WywoÄąâ€šywana po wysÄąâ€šaniu ÄąÄ˝Ä…dania. Rozpoczyna odczytywanie nagÄąâ€šĂłwkĂłw odpowiedzi za pomocÄ… `async_read_header`.
-   **`on_read_header`**: WywoÄąâ€šywana po odczytaniu nagÄąâ€šĂłwkĂłw.
    -   Sprawdza kod statusu.
    -   JeÄąâ€şli jest to przekierowanie (np. 301, 302), tworzy nowÄ… `HttpSession` dla nowego URL.
    -   JeÄąâ€şli status jest niepoprawny, zgÄąâ€šasza bÄąâ€šÄ…d.
    -   Rozpoczyna odczytywanie treÄąâ€şci odpowiedzi za pomocÄ… `async_read_some`.
-   **`on_read`**: WywoÄąâ€šywana wielokrotnie podczas odczytywania treÄąâ€şci odpowiedzi.
    -   Aktualizuje postÄ™p pobierania i wywoÄąâ€šuje `callback` progresu.
    -   Gdy caÄąâ€ša treÄąâ€şÄ‡ zostanie odczytana (`end_of_stream`), finalizuje operacjÄ™, zapisuje odpowiedÄąĹź w `m_result` i wywoÄąâ€šuje `callback` koÄąâ€žcowy.
-   **`onTimeout`**: Handler dla timera, ktĂłry zgÄąâ€šasza bÄąâ€šÄ…d timeoutu.
-   **`onError`**: Centralna funkcja do obsÄąâ€šugi bÄąâ€šÄ™dĂłw. Zamyka gniazdo, anuluje timer i wywoÄąâ€šuje `callback` z informacjÄ… o bÄąâ€šÄ™dzie.
## `void HttpSession::close()`

Zamyka poÄąâ€šÄ…czenie, anuluje timer i, w przypadku HTTPS, wykonuje `async_shutdown` dla strumienia SSL.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/http/session.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/stdext/uri.h`: Do parsowania URL.
-   **Boost.Asio** i **Boost.Beast**: Kluczowe biblioteki do obsÄąâ€šugi sieci.
-   Jest tworzona i zarzÄ…dzana przez klasÄ™ `Http`.

---
# Ä‘Ĺşâ€śâ€ž session.h
## Opis ogĂłlny

Plik `session.h` deklaruje klasÄ™ `HttpSession`, ktĂłra enkapsuluje logikÄ™ pojedynczej sesji HTTP/HTTPS. Plik ten jest wyÄąâ€šÄ…czony z kompilacji dla Emscripten.
## Klasa `HttpSession`
## Opis semantyczny
`HttpSession` zarzÄ…dza caÄąâ€šym cyklem ÄąÄ˝ycia zapytania HTTP, od rozwiÄ…zania nazwy DNS, przez nawiÄ…zanie poÄąâ€šÄ…czenia (w tym SSL/TLS handshake), wysÄąâ€šanie ÄąÄ˝Ä…dania, aÄąÄ˝ po odczytanie odpowiedzi. Jest zaprojektowana do dziaÄąâ€šania asynchronicznego w ramach `boost::asio::io_service`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `HttpSession(...)` | Konstruktor. |
| `void start()` | Rozpoczyna sesjÄ™ HTTP. |
| `void cancel()` | Anuluje bieÄąÄ˝Ä…cÄ… operacjÄ™. |
## Zmienne prywatne

-   `m_service`: Referencja do `io_service`.
-   `m_url`, `m_agent`: URL i User-Agent.
-   `m_socket`: Gniazdo TCP.
-   `m_resolver`: Resolver DNS.
-   `m_callback`: Funkcja zwrotna do powiadamiania o wyniku.
-   `m_result`: WskaÄąĹźnik na obiekt `HttpResult` przechowujÄ…cy stan.
-   `m_timer`: Timer do obsÄąâ€šugi timeoutĂłw.
-   `m_timeout`: Czas timeoutu.
-   `m_isJson`: Flaga wskazujÄ…ca, czy treÄąâ€şÄ‡ POST jest w formacie JSON.
-   `m_ssl`, `m_context`: Do obsÄąâ€šugi HTTPS.
-   `m_streambuf`: Bufor na dane przychodzÄ…ce.
-   `m_request`: Obiekt ÄąÄ˝Ä…dania z Boost.Beast.
-   `m_response`: Parser odpowiedzi z Boost.Beast.
## Metody prywatne (`on_...`, `close`, `onError`)

Deklaracje handlerĂłw dla operacji asynchronicznych i funkcji pomocniczych.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   Jest tworzona i uÄąÄ˝ywana przez klasÄ™ `Http` do realizacji zapytaÄąâ€ž GET i POST.

---
# Ä‘Ĺşâ€śâ€ž websocket.cpp
## Opis ogĂłlny

Plik `websocket.cpp` zawiera implementacjÄ™ klasy `WebsocketSession`, ktĂłra zarzÄ…dza pojedynczym poÄąâ€šÄ…czeniem WebSocket. Plik ten jest wyÄąâ€šÄ…czony z kompilacji dla Emscripten.
## Klasa `WebsocketSession`
## `void WebsocketSession::start()`
## Opis semantyczny
Rozpoczyna proces nawiÄ…zywania poÄąâ€šÄ…czenia WebSocket.
## DziaÄąâ€šanie
1.  Sprawdza limit przekierowaÄąâ€ž.
2.  Parsuje URL, aby uzyskaÄ‡ protokĂłÄąâ€š, domenÄ™, port i Äąâ€şcieÄąÄ˝kÄ™.
3.  Ustawia timer na obsÄąâ€šugÄ™ timeoutu.
4.  Tworzy odpowiedni obiekt gniazda (`m_socket` dla WS lub `m_ssl` dla WSS).
5.  Uruchamia asynchroniczne rozwiÄ…zywanie nazwy DNS.
## `void WebsocketSession::send(std::string data)`

Dodaje wiadomoÄąâ€şÄ‡ do kolejki `m_sendQueue`. JeÄąâ€şli kolejka byÄąâ€ša pusta i poÄąâ€šÄ…czenie jest aktywne, natychmiast inicjuje operacjÄ™ wysyÄąâ€šania.
## Metody `on_...()`

SÄ… to handlery dla operacji asynchronicznych, ktĂłre implementujÄ… maszynÄ™ stanĂłw poÄąâ€šÄ…czenia WebSocket:

-   **`on_resolve`**: WywoÄąâ€šywana po rozwiÄ…zaniu nazwy DNS. Inicjuje `async_connect`.
-   **`on_connect`**: WywoÄąâ€šywana po nawiÄ…zaniu poÄąâ€šÄ…czenia TCP. W przypadku WSS, wykonuje handshake SSL. NastÄ™pnie inicjuje handshake protokoÄąâ€šu WebSocket za pomocÄ… `async_handshake`.
-   **`on_handshake`**: WywoÄąâ€šywana po pomyÄąâ€şlnym handshake'u WebSocket. Ustawia stan na `connected`, wywoÄąâ€šuje `callback` `WEBSOCKET_OPEN`, rozpoczyna nasÄąâ€šuchiwanie wiadomoÄąâ€şci (`async_read`) i wysyÄąâ€ša wiadomoÄąâ€şci z kolejki.
-   **`on_send`**: WywoÄąâ€šywana po wysÄąâ€šaniu wiadomoÄąâ€şci. Usuwa wysÄąâ€šanÄ… wiadomoÄąâ€şÄ‡ z kolejki i, jeÄąâ€şli kolejka nie jest pusta, inicjuje wysyÄąâ€šanie nastÄ™pnej.
-   **`on_read`**: WywoÄąâ€šywana po otrzymaniu nowej wiadomoÄąâ€şci. Resetuje timer, wywoÄąâ€šuje `callback` `WEBSOCKET_MESSAGE` i ponownie nasÄąâ€šuchuje.
-   **`onTimeout`**: ZgÄąâ€šasza bÄąâ€šÄ…d timeoutu.
-   **`onError`**: ObsÄąâ€šuguje bÄąâ€šÄ™dy i wywoÄąâ€šuje `callback` `WEBSOCKET_ERROR`.
## `void WebsocketSession::close()`

Zamyka poÄąâ€šÄ…czenie, anuluje timer i wywoÄąâ€šuje `callback` `WEBSOCKET_CLOSE`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/http/websocket.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/stdext/uri.h`: Do parsowania URL.
-   **Boost.Asio** i **Boost.Beast**: Kluczowe biblioteki do obsÄąâ€šugi sieci i protokoÄąâ€šu WebSocket.
-   Jest tworzona i zarzÄ…dzana przez klasÄ™ `Http`.

---
# Ä‘Ĺşâ€śâ€ž mouse.cpp
## Opis ogĂłlny

Plik `mouse.cpp` implementuje klasÄ™ `Mouse`, ktĂłra jest singletonem (`g_mouse`) odpowiedzialnym za zarzÄ…dzanie kursorami myszy.
## Zmienne globalne
## `g_mouse`

Globalna instancja `Mouse`.
## Klasa `Mouse`
## `void Mouse::init()` i `void Mouse::terminate()`

Metody do inicjalizacji i zwalniania zasobĂłw. `terminate()` czyÄąâ€şci listÄ™ zaÄąâ€šadowanych kursorĂłw.
## `void Mouse::loadCursors(std::string filename)`

ÄąÂaduje definicje kursorĂłw z pliku OTML. Parsuje plik i dla kaÄąÄ˝dego wpisu w sekcji `Cursors` wywoÄąâ€šuje `addCursor`.
## `void Mouse::addCursor(const std::string& name, const std::string& file, const Point& hotSpot)`
## Opis semantyczny
ÄąÂaduje obraz kursora z pliku i tworzy z niego natywny kursor systemowy. Jest bezpieczna wÄ…tkowo.
## DziaÄąâ€šanie
1.  JeÄąâ€şli jest wywoÄąâ€šana z wÄ…tku innego niÄąÄ˝ graficzny, deleguje zadanie do `g_graphicsDispatcher`.
2.  WywoÄąâ€šuje `g_window.loadMouseCursor`, ktĂłra wykonuje operacje specyficzne dla platformy.
3.  Zapisuje zwrĂłcone ID kursora w mapie `m_cursors` pod podanÄ… nazwÄ….
## `void Mouse::pushCursor(const std::string& name)`
## Opis semantyczny
Ustawia nowy kursor i dodaje go na stos aktywnych kursorĂłw.
## DziaÄąâ€šanie
1.  Deleguje do wÄ…tku graficznego, jeÄąâ€şli to konieczne.
2.  Znajduje ID kursora w `m_cursors`.
3.  WywoÄąâ€šuje `g_window.setMouseCursor` z znalezionym ID.
4.  Dodaje ID na koniec stosu `m_cursorStack`.
## `void Mouse::popCursor(const std::string& name)`
## Opis semantyczny
Usuwa kursor ze stosu i przywraca poprzedni.
## DziaÄąâ€šanie
1.  Deleguje do wÄ…tku graficznego.
2.  JeÄąâ€şli `name` jest puste, usuwa ostatni kursor ze stosu.
3.  JeÄąâ€şli `name` jest podane, wyszukuje i usuwa konkretny kursor ze stosu.
4.  JeÄąâ€şli stos nie jest pusty, ustawia kursor, ktĂłry jest teraz na jego szczycie.
5.  JeÄąâ€şli stos jest pusty, przywraca domyÄąâ€şlny kursor systemowy.
## `bool Mouse::isCursorChanged()`

Zwraca `true`, jeÄąâ€şli stos kursorĂłw nie jest pusty, co oznacza, ÄąÄ˝e aktualny kursor jest niestandardowy.
## `bool Mouse::isPressed(Fw::MouseButton mouseButton)`

Sprawdza i zwraca stan wciÄąâ€şniÄ™cia danego przycisku myszy, delegujÄ…c zapytanie do `g_window`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/input/mouse.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/ui/uiwidget.h`: Widgety mogÄ… zmieniaÄ‡ kursor.
-   `framework/platform/platformwindow.h`: UÄąÄ˝ywa `g_window` do niskopoziomowych operacji na kursorach.
-   `framework/core/eventdispatcher.h`: Do zapewnienia bezpieczeÄąâ€žstwa wÄ…tkowego.
-   `framework/core/resourcemanager.h`: Do Äąâ€šadowania plikĂłw definicji kursorĂłw.

---
# Ä‘Ĺşâ€śâ€ž mouse.h
## Opis ogĂłlny

Plik `mouse.h` deklaruje klasÄ™ `Mouse`, ktĂłra jest interfejsem wysokiego poziomu do zarzÄ…dzania kursorami myszy w aplikacji.
## Klasa `Mouse`
## Opis semantyczny
`Mouse` zarzÄ…dza kolekcjÄ… niestandardowych kursorĂłw, ktĂłre mogÄ… byÄ‡ Äąâ€šadowane z plikĂłw. Implementuje mechanizm stosu (`m_cursorStack`), ktĂłry pozwala na tymczasowÄ… zmianÄ™ kursora (np. gdy kursor znajduje siÄ™ nad widgetem) i Äąâ€šatwy powrĂłt do poprzedniego stanu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedÄąÄ˝era. |
| `void terminate()` | Zwalnia zasoby. |
| `void loadCursors(...)` | ÄąÂaduje definicje kursorĂłw z pliku OTML. |
| `void addCursor(...)` | Dodaje nowy niestandardowy kursor. |
| `void pushCursor(...)` | Ustawia nowy kursor, dodajÄ…c go na szczyt stosu. |
| `void popCursor(...)` | Usuwa kursor ze stosu i przywraca poprzedni. |
| `bool isCursorChanged()` | Sprawdza, czy aktualny kursor jest niestandardowy. |
| `bool isPressed(...)` | Sprawdza stan wciÄąâ€şniÄ™cia przycisku myszy. |
## Zmienne prywatne

-   `m_cursors`: Mapa przechowujÄ…ca nazwy kursorĂłw i ich ID specyficzne dla platformy.
-   `m_cursorStack`: Stos (`std::deque`) przechowujÄ…cy ID aktywnych kursorĂłw.
-   `m_mutex`: Mutex do ochrony dostÄ™pu do `m_cursorStack` z rĂłÄąÄ˝nych wÄ…tkĂłw.
## Zmienne globalne

-   `g_mouse`: Globalna instancja `Mouse`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   Jest uÄąÄ˝ywana przez `UIWidget` do zmiany wyglÄ…du kursora, gdy znajduje siÄ™ on nad widgetem.
-   WspĂłÄąâ€špracuje z `PlatformWindow` w celu faktycznego ustawiania kursora w systemie operacyjnym.

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## Opis ogĂłlny

Plik `declarations.h` w module `luaengine` sÄąâ€šuÄąÄ˝y do wczesnych deklaracji (forward declarations) i definicji typĂłw zwiÄ…zanych z silnikiem Lua. Jego celem jest unikanie zaleÄąÄ˝noÄąâ€şci cyklicznych i zmniejszenie liczby doÄąâ€šÄ…czanych nagÄąâ€šĂłwkĂłw.
## Wczesne deklaracje

-   `LuaInterface`: GÄąâ€šĂłwna klasa interfejsu Lua.
-   `LuaObject`: Bazowa klasa dla wszystkich obiektĂłw eksportowanych do Lua.
## Definicje typĂłw

-   **`LuaCppFunction`**: Alias dla `std::function<int(LuaInterface*)>`. Jest to typ funkcji C++, ktĂłra moÄąÄ˝e byÄ‡ wywoÄąâ€šana z Lua. Przyjmuje wskaÄąĹźnik do `LuaInterface` i zwraca liczbÄ™ wartoÄąâ€şci zwrĂłconych na stos Lua.
-   **`LuaCppFunctionPtr`**: Alias dla `std::unique_ptr<LuaCppFunction>`. UÄąÄ˝ywany wewnÄ™trznie do zarzÄ…dzania czasem ÄąÄ˝ycia funkcji bindowanych.
-   **`LuaObjectPtr`**: Alias dla `stdext::shared_object_ptr<LuaObject>`. Standardowy sposĂłb przekazywania i przechowywania obiektĂłw C++ w Lua.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Zawiera podstawowe definicje.
-   `<memory>`: Dla `std::unique_ptr`.
-   Jest to fundamentalny plik dla caÄąâ€šego silnika Lua, doÄąâ€šÄ…czany przez `luainterface.h`, `luaobject.h` i inne.

---
# Ä‘Ĺşâ€śâ€ž lbitlib.cpp
## Opis ogĂłlny

Plik `lbitlib.cpp` zawiera kod ÄąĹźrĂłdÄąâ€šowy biblioteki `bit32` z Lua 5.2.0, przeniesiony (backported) do uÄąÄ˝ytku z Lua 5.1.4 (lub LuaJIT, ktĂłry jest kompatybilny z 5.1). Biblioteka ta dostarcza operacje bitowe na 32-bitowych liczbach caÄąâ€škowitych bez znaku.
## ZawartoÄąâ€şÄ‡

Plik skÄąâ€šada siÄ™ z kilku czÄ™Äąâ€şci:

1.  **Adaptacje i definicje kompatybilnoÄąâ€şci**:
    -   Zawiera kod przeniesiony z `luaconf.h` i `llimits.h` z Lua 5.2, ktĂłry definiuje makra (`lua_number2unsigned`) do bezpiecznej konwersji miÄ™dzy `lua_Number` (zwykle `double`) a `lua_Unsigned` (32-bitowy `unsigned int`). Jest to konieczne, poniewaÄąÄ˝ Lua 5.1 nie ma wbudowanego typu caÄąâ€škowitoliczbowego.
    -   Definiuje funkcjÄ™ `lua_pushunsigned` i `luaL_checkunsigned` do obsÄąâ€šugi tego typu na stosie Lua.
    -   Definiuje makro `luaL_newlib` dla kompatybilnoÄąâ€şci z `luaL_register` z Lua 5.1.

2.  **Oryginalny kod `lbitlib.c` z Lua 5.2.0**:
    -   Zawiera implementacje wszystkich funkcji z biblioteki `bit32`.
## Funkcje biblioteki `bit32`

| Funkcja Lua | Opis |
| :--- | :--- |
| `bit32.band(...)` | Wykonuje bitowe AND na wszystkich argumentach. |
| `bit32.btest(...)` | Wykonuje bitowe AND i zwraca `true`, jeÄąâ€şli wynik jest rĂłÄąÄ˝ny od zera. |
| `bit32.bor(...)` | Wykonuje bitowe OR na wszystkich argumentach. |
| `bit32.bxor(...)` | Wykonuje bitowe XOR na wszystkich argumentach. |
| `bit32.bnot(x)` | Wykonuje bitowÄ… negacjÄ™. |
| `bit32.lshift(x, n)` | PrzesuniÄ™cie bitowe w lewo. |
| `bit32.rshift(x, n)` | PrzesuniÄ™cie bitowe w prawo (logiczne). |
| `bit32.arshift(x, n)`| PrzesuniÄ™cie bitowe w prawo (arytmetyczne). |
| `bit32.lrotate(x, n)`| Rotacja bitowa w lewo. |
| `bit32.rrotate(x, n)`| Rotacja bitowa w prawo. |
| `bit32.extract(n, field, width)`| Ekstrahuje `width` bitĂłw z liczby `n`, zaczynajÄ…c od bitu `field`. |
| `bit32.replace(n, v, field, width)`| ZastÄ™puje bity w liczbie `n` bitami z `v`. |
## `int luaopen_bit32 (lua_State *L)`

GÄąâ€šĂłwna funkcja, ktĂłra rejestruje bibliotekÄ™ `bit32` w podanym stanie Lua.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `lbitlib.h`: Plik nagÄąâ€šĂłwkowy.
-   NagÄąâ€šĂłwki Lua/LuaJIT (`lua.h`, `lualib.h`, `lauxlib.h`).
-   Jest Äąâ€šadowana w `LuaInterface::createLuaState`, aby udostÄ™pniÄ‡ operacje bitowe w skryptach.

---
# Ä‘Ĺşâ€śâ€ž lbitlib.h
## Opis ogĂłlny

Plik `lbitlib.h` jest plikiem nagÄąâ€šĂłwkowym dla biblioteki `bit32` z Lua 5.2, ktĂłra zostaÄąâ€ša przeniesiona do uÄąÄ˝ytku w tym projekcie.
## Deklaracje
## `int luaopen_bit32 (lua_State *L)`

Deklaruje funkcjÄ™, ktĂłra jest punktem wejÄąâ€şcia do zaÄąâ€šadowania biblioteki `bit32` w stanie Lua. Zgodnie z konwencjÄ… Lua, funkcje `luaopen_*` sÄ… uÄąÄ˝ywane do rejestrowania moduÄąâ€šĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Wymaga definicji `struct lua_State`.
-   Jest doÄąâ€šÄ…czany przez `luainterface.cpp`, aby umoÄąÄ˝liwiÄ‡ zaÄąâ€šadowanie biblioteki `bit32` podczas inicjalizacji `LuaInterface`.

---
# Ä‘Ĺşâ€śâ€ž luabinder.h
## Opis ogĂłlny

Plik `luabinder.h` jest sercem mechanizmu bindowania C++ do Lua. Zawiera on zestaw zaawansowanych szablonĂłw metaprogramowania, ktĂłre umoÄąÄ˝liwiajÄ… automatyczne generowanie funkcji-opakowaÄąâ€ž (wrapperĂłw) dla niemal dowolnych funkcji C++, w tym funkcji globalnych, statycznych, metod klas, funkcji `std::function` i lambd.
## Namespace `luabinder`
## Opis semantyczny
PrzestrzeÄąâ€ž nazw `luabinder` zawiera szablony, ktĂłre dziaÄąâ€šajÄ… jak "fabryka" funkcji typu `LuaCppFunction`. AnalizujÄ… one sygnaturÄ™ funkcji C++ (typ zwracany i typy argumentĂłw), a nastÄ™pnie generujÄ… lambdÄ™, ktĂłra:
1.  Pobiera argumenty z stosu Lua i konwertuje je na odpowiednie typy C++.
2.  WywoÄąâ€šuje oryginalnÄ… funkcjÄ™ C++ z tymi argumentami.
3.  Pobiera wartoÄąâ€şÄ‡ zwracanÄ… przez funkcjÄ™ C++.
4.  Konwertuje tÄ™ wartoÄąâ€şÄ‡ na typ zrozumiaÄąâ€šy dla Lua i umieszcza jÄ… na stosie.
5.  Zwraca liczbÄ™ wartoÄąâ€şci umieszczonych na stosie.
## GÄąâ€šĂłwne szablony

-   **`pack_values_into_tuple`**: Szablon rekurencyjny, ktĂłry pobiera `N` wartoÄąâ€şci ze stosu Lua i umieszcza je w `std::tuple`.
-   **`expand_fun_arguments`**: Szablon rekurencyjny, ktĂłry rozpakowuje `std::tuple` z argumentami i wywoÄąâ€šuje z nimi docelowÄ… funkcjÄ™ C++.
-   **`call_fun_and_push_result`**: Szablon, ktĂłry wywoÄąâ€šuje funkcjÄ™ i obsÄąâ€šuguje wartoÄąâ€şÄ‡ zwracanÄ… (specjalizacje dla `void` i typĂłw nie-`void`).
-   **`bind_fun_specializer`**: GÄąâ€šĂłwny szablon, ktĂłry Äąâ€šÄ…czy powyÄąÄ˝sze, generujÄ…c finalnÄ… lambdÄ™.
-   **`bind_fun(...)`**: PrzeciÄ…ÄąÄ˝one funkcje, ktĂłre sÄ… publicznym API tego namespace. PrzyjmujÄ… rĂłÄąÄ˝ne typy funkcji (wskaÄąĹźniki, `std::function`, lambdy) i przekierowujÄ… je do odpowiednich specjalizacji.
-   **`make_mem_func(...)` i `make_mem_func_singleton(...)`**: Funkcje pomocnicze, ktĂłre konwertujÄ… wskaÄąĹźniki na metody klas na obiekty `std::function` (lambdy), ktĂłre moÄąÄ˝na nastÄ™pnie zbindowaÄ‡.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to plik wewnÄ™trzny, doÄąâ€šÄ…czany tylko przez `luainterface.h`.
-   Intensywnie korzysta z zaawansowanych cech C++11/14/17, takich jak szablony wariadyczne, `std::tuple`, `std::function`, `std::enable_if`, `decltype`.
-   `framework/stdext/traits.h`: UÄąÄ˝ywa `remove_const_ref` do normalizacji typĂłw.
-   `luaexception.h`: MoÄąÄ˝e rzucaÄ‡ wyjÄ…tki w przypadku bÄąâ€šÄ™dĂłw (np. wywoÄąâ€šanie metody na obiekcie `nullptr`).
-   Jest podstawÄ… dla wszystkich metod `bind...` w `LuaInterface`, ktĂłre automatyzujÄ… proces tworzenia bindowaÄąâ€ž.

---
# Ä‘Ĺşâ€śâ€ž luaexception.h
## Opis ogĂłlny

Plik `luaexception.h` deklaruje hierarchiÄ™ klas wyjÄ…tkĂłw specyficznych dla interakcji z silnikiem Lua. Te klasy wyjÄ…tkĂłw sÄ… uÄąÄ˝ywane do sygnalizowania bÄąâ€šÄ™dĂłw, ktĂłre wystÄ™pujÄ… podczas operacji na stosie Lua, rzutowania typĂłw lub wywoÄąâ€šywania funkcji.
## Klasa `LuaException`
## Opis semantyczny
Jest to bazowa klasa dla wszystkich wyjÄ…tkĂłw zwiÄ…zanych z Lua. Dziedziczy po `stdext::exception`. Jej gÄąâ€šĂłwnym zadaniem jest sformatowanie komunikatu o bÄąâ€šÄ™dzie, opcjonalnie doÄąâ€šÄ…czajÄ…c do niego Äąâ€şlad stosu (traceback) z Lua.
## Metody

-   `LuaException(const std::string& error, int traceLevel = -1)`: Konstruktor, ktĂłry generuje komunikat bÄąâ€šÄ™du.
-   `virtual const char* what() const throw()`: Zwraca sformatowany komunikat bÄąâ€šÄ™du.
## Klasa `LuaBadNumberOfArgumentsException`
## Opis semantyczny
Specjalistyczny wyjÄ…tek rzucany, gdy funkcja C++ bindowana do Lua zostanie wywoÄąâ€šana z nieprawidÄąâ€šowÄ… liczbÄ… argumentĂłw.
## Metody

-   `LuaBadNumberOfArgumentsException(int expected = -1, int got = -1)`: Konstruktor, ktĂłry tworzy odpowiedni komunikat o bÄąâ€šÄ™dzie.
## Klasa `LuaBadValueCastException`
## Opis semantyczny
Specjalistyczny wyjÄ…tek rzucany, gdy prĂłba rzutowania wartoÄąâ€şci ze stosu Lua na okreÄąâ€şlony typ C++ (`luavalue_cast`) nie powiedzie siÄ™.
## Metody

-   `LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName)`: Konstruktor, ktĂłry tworzy komunikat bÄąâ€šÄ™du informujÄ…cy o typach, miÄ™dzy ktĂłrymi rzutowanie zawiodÄąâ€šo.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/luaengine/declarations.h`: Podstawowe deklaracje.
-   `framework/stdext/exception.h`: Klasa bazowa `stdext::exception`.
-   WyjÄ…tki te sÄ… rzucane przez `LuaInterface` i `luabinder`, a Äąâ€šapane w bezpiecznych punktach wywoÄąâ€šaÄąâ€ž (np. `luaCppFunctionCallback`), aby zapobiec awarii aplikacji i przekazaÄ‡ bÄąâ€šÄ…d do logĂłw lub z powrotem do Äąâ€şrodowiska Lua.

---
# Ä‘Ĺşâ€śâ€ž luaexception.cpp
## Opis ogĂłlny

Plik `luaexception.cpp` zawiera implementacjÄ™ klas wyjÄ…tkĂłw zdefiniowanych w `luaexception.h`.
## Klasa `LuaException`
## `LuaException::LuaException(const std::string& error, int traceLevel)`

Konstruktor. Jego gÄąâ€šĂłwnym zadaniem jest wywoÄąâ€šanie `generateLuaErrorMessage`, aby przygotowaÄ‡ peÄąâ€šny komunikat bÄąâ€šÄ™du.
## `void LuaException::generateLuaErrorMessage(const std::string& error, int traceLevel)`

Metoda ta formatuje finalny komunikat bÄąâ€šÄ™du, ktĂłry bÄ™dzie dostÄ™pny przez `what()`.
-   JeÄąâ€şli `traceLevel` jest podany (wiÄ™kszy lub rĂłwny 0), wywoÄąâ€šuje `g_lua.traceback`, aby doÄąâ€šÄ…czyÄ‡ do komunikatu Äąâ€şlad stosu wywoÄąâ€šaÄąâ€ž Lua.
-   W przeciwnym razie, po prostu prefiksuje bÄąâ€šÄ…d napisem "LUA ERROR:".
## Klasa `LuaBadNumberOfArgumentsException`
## `LuaBadNumberOfArgumentsException::LuaBadNumberOfArgumentsException(int expected, int got)`

Konstruktor. Tworzy specyficzny komunikat bÄąâ€šÄ™du informujÄ…cy o nieprawidÄąâ€šowej liczbie argumentĂłw, a nastÄ™pnie wywoÄąâ€šuje `generateLuaErrorMessage` z poziomem Äąâ€şledzenia `1`, aby pokazaÄ‡, ktĂłra funkcja w Lua zostaÄąâ€ša ÄąĹźle wywoÄąâ€šana.
## Klasa `LuaBadValueCastException`
## `LuaBadValueCastException::LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName)`

Konstruktor. Tworzy komunikat bÄąâ€šÄ™du informujÄ…cy o niemoÄąÄ˝noÄąâ€şci rzutowania miÄ™dzy danym typem Lua a typem C++, a nastÄ™pnie wywoÄąâ€šuje `generateLuaErrorMessage`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/luaengine/luaexception.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/luaengine/luainterface.h`: UÄąÄ˝ywa `g_lua` do generowania Äąâ€şladu stosu.
-   Implementuje logikÄ™ formatowania bÄąâ€šÄ™dĂłw, ktĂłra jest kluczowa dla debugowania skryptĂłw Lua.

---
# Ä‘Ĺşâ€śâ€ž luainterface.cpp
## Opis ogĂłlny

Plik `luainterface.cpp` zawiera implementacjÄ™ klasy `LuaInterface`, ktĂłra jest centralnym interfejsem do komunikacji z silnikiem Lua. Jest to jedna z najwaÄąÄ˝niejszych klas w caÄąâ€šym frameworku.
## Zmienne globalne
## `g_lua`

Globalna instancja `LuaInterface`.
## Klasa `LuaInterface`
## Inicjalizacja i zamykanie

-   **`init()`**: Inicjalizuje `LuaInterface`.
    1.  Tworzy nowy stan Lua (`createLuaState`).
    2.  Zapisuje referencjÄ™ do globalnego Äąâ€şrodowiska.
    3.  Rejestruje bazowÄ… klasÄ™ `LuaObject` i jej podstawowe metody.
-   **`terminate()`**: Zamyka stan Lua, co powoduje zwolnienie wszystkich zasobĂłw i wywoÄąâ€šanie garbage collectora.
-   **`createLuaState()`**: Tworzy stan Lua (`luaL_newstate`), Äąâ€šaduje standardowe biblioteki (`luaL_openlibs`), Äąâ€šaduje bibliotekÄ™ `bit32`, tworzy specjalnÄ… "sÄąâ€šabÄ…" tabelÄ™ do przechowywania referencji i instaluje niestandardowe loadery (`dofile`, `loadfile`).
## Rejestracja i bindowanie

-   **`registerSingletonClass(...)`**, **`registerClass(...)`**: ImplementujÄ… logikÄ™ tworzenia tabel i metatabel w Lua, ktĂłre reprezentujÄ… klasy C++. `registerClass` dodatkowo ustawia dziedziczenie, linkujÄ…c metatabelÄ™ klasy pochodnej do metatabeli klasy bazowej za pomocÄ… metametody `__index`.
-   **`register...Function(...)`**, **`register...Field(...)`**: Metody te pobierajÄ… odpowiednie tabele (klasy, metody, fieldmethods) z globalnego Äąâ€şrodowiska Lua i umieszczajÄ… w nich funkcje C++ opakowane w `LuaCppFunction`.
## Metody obsÄąâ€šugi metametod obiektĂłw

-   **`luaObjectGetEvent(__index)`**: Handler wywoÄąâ€šywany przy prĂłbie odczytu pola z obiektu C++ w Lua. Wyszukuje on kolejno: metodÄ™ "get", pole w tabeli `fields` obiektu, metodÄ™ w tabeli metod klasy.
-   **`luaObjectSetEvent(__newindex)`**: Handler wywoÄąâ€šywany przy prĂłbie zapisu pola. Wyszukuje i wywoÄąâ€šuje metodÄ™ "set" lub zapisuje wartoÄąâ€şÄ‡ w tabeli `fields`.
-   **`luaObjectEqualEvent(__eq)`**: PorĂłwnuje dwa obiekty C++.
-   **`luaObjectCollectEvent(__gc)`**: Handler wywoÄąâ€šywany przez garbage collector Lua. Zwalnia `shared_ptr` do obiektu, dekrementujÄ…c jego licznik referencji.
## Wykonywanie skryptĂłw

-   **`runScript(...)`**, **`loadScript(...)`**, **`runBuffer(...)`**: Metody do Äąâ€šadowania i wykonywania skryptĂłw Lua z plikĂłw lub buforĂłw w pamiÄ™ci. `loadScript` uÄąÄ˝ywa `g_resources` do znalezienia i odczytania pliku.
-   **`safeCall(...)`**: Kluczowa metoda do bezpiecznego wywoÄąâ€šywania funkcji Lua. Ustawia `luaErrorHandler` jako funkcjÄ™ obsÄąâ€šugi bÄąâ€šÄ™dĂłw, a nastÄ™pnie wywoÄąâ€šuje `lua_pcall`. W przypadku bÄąâ€šÄ™du, Äąâ€šapie go i zwraca jako string lub rzuca wyjÄ…tek `LuaException`.
-   **`signalCall(...)`**: Wysokopoziomowa metoda, ktĂłra opakowuje `safeCall` i dodatkowo obsÄąâ€šuguje wywoÄąâ€šywanie tabeli funkcji.
## Inne

-   **`traceback(...)`**: Generuje Äąâ€şlad stosu wywoÄąâ€šaÄąâ€ž Lua.
-   **`getCurrentSourcePath(...)`**: Zwraca Äąâ€şcieÄąÄ˝kÄ™ do pliku skryptu, w ktĂłrym aktualnie wykonywany jest kod.
-   **`newSandboxEnv()`**: Tworzy nowe, odizolowane Äąâ€şrodowisko Lua.
-   **`lua...` (funkcje statyczne)**: Implementacje funkcji C, ktĂłre sÄ… bezpoÄąâ€şrednio rejestrowane w Lua (np. `lua_dofile`).
-   **`...Callback`**: Implementacje handlerĂłw dla `lua_pcall` i `__gc`.
-   **Metody opakowujÄ…ce API Lua**: Plik zawiera dziesiÄ…tki metod (`getTop`, `pushNil`, `toString`, `isTable`, etc.), ktĂłre sÄ… cienkimi, ale bezpieczniejszymi (dziÄ™ki `VALIDATE`) opakowaniami na funkcje z biblioteki Lua C API.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to centralna klasa, ktĂłra Äąâ€šÄ…czy C++ z Lua. ZaleÄąÄ˝y od `lua.h`, `lualib.h`, `lauxlib.h`.
-   ÄąĹˇciÄąâ€şle wspĂłÄąâ€špracuje z `LuaObject`, `luabinder.h`, `luavaluecasts.h`.
-   UÄąÄ˝ywa `g_resources` do Äąâ€šadowania skryptĂłw.
-   UÄąÄ˝ywana przez `Application` do inicjalizacji, `ModuleManager` do Äąâ€šadowania moduÄąâ€šĂłw i `UIWidget` do wywoÄąâ€šywania callbackĂłw.

---
# Ä‘Ĺşâ€śâ€ž luainterface.h
## Opis ogĂłlny

Plik `luainterface.h` deklaruje klasÄ™ `LuaInterface`, ktĂłra jest gÄąâ€šĂłwnym interfejsem do interakcji z silnikiem Lua. Jest to klasa singletonowa (`g_lua`), ktĂłra enkapsuluje stan Lua (`lua_State*`) i dostarcza bogaty zestaw metod do manipulacji stosem, wywoÄąâ€šywania funkcji, bindowania kodu C++ i zarzÄ…dzania obiektami.
## Klasa `LuaInterface`
## Opis semantyczny
`LuaInterface` stanowi most miÄ™dzy kodem C++ a skryptami Lua. UdostÄ™pnia wysokopoziomowe API, ktĂłre ukrywa zÄąâ€šoÄąÄ˝onoÄąâ€şÄ‡ bezpoÄąâ€şredniej pracy z Lua C API. Wszystkie operacje, takie jak umieszczanie wartoÄąâ€şci na stosie, odczytywanie ich, wywoÄąâ€šywanie funkcji czy rejestrowanie klas, sÄ… opakowane w metody tej klasy.
## Metody publiczne (wybrane)
## Inicjalizacja i zarzÄ…dzanie
-   `init()` / `terminate()`: Uruchamia i zamyka silnik Lua.
-   `collectGarbage()`: Wymusza uruchomienie garbage collectora.
## Rejestracja i bindowanie
-   `registerSingletonClass(...)`: Rejestruje globalny obiekt (singleton) w Lua.
-   `registerClass(...)`: Rejestruje klasÄ™ C++ w Lua, umoÄąÄ˝liwiajÄ…c tworzenie jej instancji.
-   `bind...Function(...)`, `bind...Field(...)`: Szablonowe metody do bindowania funkcji i pĂłl klas.
## Wykonywanie skryptĂłw
-   `safeRunScript(...)`: Bezpiecznie wykonuje skrypt z pliku.
-   `runScript(...)`, `runBuffer(...)`: WykonujÄ… skrypt z pliku lub bufora.
-   `loadScript(...)`, `loadFunction(...)`: ÄąÂadujÄ… skrypt/funkcjÄ™ na stos bez jej wykonywania.
-   `safeCall(...)`: Bezpiecznie wywoÄąâ€šuje funkcjÄ™ na stosie, z obsÄąâ€šugÄ… bÄąâ€šÄ™dĂłw.
-   `signalCall(...)`: Wysokopoziomowa wersja `safeCall` z dodatkowymi funkcjami.
-   `callGlobalField<R, ...T>(...)`: Wygodna metoda do wywoÄąâ€šywania globalnej funkcji Lua z C++ i otrzymywania wyniku.
## Manipulacja stosem i typami
-   `push...()` / `pop...()` / `to...()` / `is...()`: Zestaw metod do pracy ze stosem Lua dla rĂłÄąÄ˝nych typĂłw danych (np. `pushInteger`, `isString`, `toObject`).
-   `getTop()`: Zwraca rozmiar stosu.
-   `ref()` / `unref()`: Do tworzenia i zwalniania trwaÄąâ€šych referencji do wartoÄąâ€şci Lua.
-   `polymorphicPush<T>(...)`: Szablonowa metoda do umieszczania na stosie dowolnego typu, dla ktĂłrego zdefiniowano `push_luavalue`.
-   `castValue<T>(...)`: Szablonowa metoda do rzutowania wartoÄąâ€şci ze stosu na typ C++, uÄąÄ˝ywajÄ…c `luavalue_cast`.
## Zmienne prywatne

-   `L`: WskaÄąĹźnik na `lua_State`.
-   `m_weakTableRef`: Referencja do tabeli ze sÄąâ€šabymi referencjami.
-   `m_cppCallbackDepth`: Licznik zagnieÄąÄ˝dÄąÄ˝enia wywoÄąâ€šaÄąâ€ž zwrotnych C++.
-   `m_totalObjRefs`, `m_totalFuncRefs`: Liczniki do Äąâ€şledzenia alokacji.
-   `m_globalEnv`: Referencja do globalnego Äąâ€şrodowiska Lua.
## DoÄąâ€šÄ…czane pliki
Plik ten na koÄąâ€žcu doÄąâ€šÄ…cza trzy kluczowe pliki, ktĂłre sÄ… od niego zaleÄąÄ˝ne i rozszerzajÄ… jego funkcjonalnoÄąâ€şÄ‡:
-   `luaexception.h`: Definicje wyjÄ…tkĂłw.
-   `luabinder.h`: Maszyneria do bindowania funkcji.
-   `luavaluecasts.h`: Implementacje `push_luavalue` i `luavalue_cast` dla rĂłÄąÄ˝nych typĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to centralny plik dla caÄąâ€šego podsystemu Lua.
-   ZaleÄąÄ˝ny od `framework/luaengine/declarations.h`.
-   UÄąÄ˝ywany przez praktycznie kaÄąÄ˝dÄ… czÄ™Äąâ€şÄ‡ aplikacji, ktĂłra wchodzi w interakcjÄ™ z Lua.

---
# Ä‘Ĺşâ€śâ€ž luaobject.cpp
## Opis ogĂłlny

Plik `luaobject.cpp` zawiera implementacjÄ™ klasy `LuaObject`, ktĂłra jest klasÄ… bazowÄ… dla wszystkich obiektĂłw C++, ktĂłre majÄ… byÄ‡ dostÄ™pne w Äąâ€şrodowisku Lua.
## Klasa `LuaObject`
## `LuaObject::LuaObject()`

Konstruktor. Inicjalizuje `m_fieldsTableRef` na -1, co oznacza, ÄąÄ˝e obiekt nie ma jeszcze przypisanej tabeli pĂłl w Lua.
## `LuaObject::~LuaObject()`

Destruktor. WywoÄąâ€šuje `releaseLuaFieldsTable()`, aby zwolniÄ‡ referencjÄ™ do tabeli pĂłl w Lua, co pozwala garbage collectorowi na jej usuniÄ™cie. Sprawdza rĂłwnieÄąÄ˝, czy nie jest wywoÄąâ€šywany podczas zamykania aplikacji.
## `bool LuaObject::hasLuaField(const std::string& field)`

Sprawdza, czy obiekt posiada pole o danej nazwie w swojej tabeli pĂłl Lua.
## `void LuaObject::releaseLuaFieldsTable()`

Zwalnia referencjÄ™ do tabeli pĂłl (`m_fieldsTableRef`), jeÄąâ€şli istnieje.
## `void LuaObject::luaSetField(const std::string& key)`
## Opis semantyczny
Ustawia pole w tabeli Lua powiÄ…zanej z tym obiektem. WartoÄąâ€şÄ‡ do ustawienia musi znajdowaÄ‡ siÄ™ na szczycie stosu Lua.
## DziaÄąâ€šanie
1.  JeÄąâ€şli obiekt nie ma jeszcze tabeli pĂłl (`m_fieldsTableRef == -1`), tworzy nowÄ… tabelÄ™ w Lua i zapisuje do niej referencjÄ™.
2.  Pobiera tabelÄ™ pĂłl na stos Lua.
3.  Przenosi wartoÄąâ€şÄ‡ ze szczytu stosu na odpowiednie miejsce.
4.  Ustawia pole w tabeli za pomocÄ… `g_lua.setField(key)`.
5.  Zdejmuje tabelÄ™ pĂłl ze stosu.
## `void LuaObject::luaGetField(const std::string& key)`

Pobiera wartoÄąâ€şÄ‡ pola z tabeli Lua obiektu i umieszcza jÄ… na szczycie stosu. JeÄąâ€şli tabela pĂłl nie istnieje, umieszcza `nil`.
## `void LuaObject::luaGetMetatable()`

Pobiera i umieszcza na stosie metatabelÄ™ dla klasy tego obiektu. UÄąÄ˝ywa statycznej mapy (`metatableMap`) do cachowania referencji do metatabel dla kaÄąÄ˝dego typu klasy, aby uniknÄ…Ä‡ wielokrotnego wyszukiwania ich w globalnym Äąâ€şrodowisku Lua.
## `void LuaObject::luaGetFieldsTable()`

Umieszcza na stosie tabelÄ™ pĂłl tego obiektu, lub `nil`, jeÄąâ€şli ona nie istnieje.
## `int LuaObject::getUseCount()`

Zwraca liczbÄ™ referencji do obiektu (`shared_object::ref_count()`).
## `std::string LuaObject::getClassName()`

Zwraca zdemanglowanÄ… nazwÄ™ klasy obiektu, ktĂłra jest uÄąÄ˝ywana do znalezienia odpowiedniej metatabeli w Lua.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/luaengine/luaobject.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/luaengine/luainterface.h`: Intensywnie korzysta z `g_lua` do wszystkich operacji na stanie Lua.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   Jest klasÄ… bazowÄ… dla setek innych klas w projekcie, ktĂłre sÄ… eksportowane do Lua.

---
# Ä‘Ĺşâ€śâ€ž luaobject.h
## Opis ogĂłlny

Plik `luaobject.h` deklaruje klasÄ™ `LuaObject`, ktĂłra jest fundamentalnÄ… klasÄ… bazowÄ… dla wszystkich obiektĂłw C++, ktĂłre majÄ… byÄ‡ widoczne i zarzÄ…dzane przez silnik Lua.
## Klasa `LuaObject`
## Opis semantyczny
`LuaObject` dziedziczy po `stdext::shared_object`, co zapewnia zarzÄ…dzanie czasem ÄąÄ˝ycia obiektu za pomocÄ… licznika referencji. Dodaje funkcjonalnoÄąâ€şÄ‡, ktĂłra pozwala na dynamiczne doÄąâ€šÄ…czanie do obiektu C++ pĂłl i metod z poziomu Lua. KaÄąÄ˝da instancja `LuaObject` moÄąÄ˝e posiadaÄ‡ wÄąâ€šasnÄ…, unikalnÄ… tabelÄ™ w Lua (`m_fieldsTableRef`), w ktĂłrej przechowywane sÄ… te dynamiczne dane.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Szablonowe metody do interakcji z Lua** | |
| `connectLuaField(...)`| ÄąÂÄ…czy funkcjÄ™ C++ (`std::function`) z polem Lua, tworzÄ…c lub rozszerzajÄ…c tabelÄ™ callbackĂłw. |
| `luaCallLuaField(...)`| WywoÄąâ€šuje funkcjÄ™ przechowywanÄ… w polu Lua tego obiektu. |
| `callLuaField(...)`| Wysokopoziomowe opakowanie na `luaCallLuaField`, ktĂłre obsÄąâ€šuguje konwersjÄ™ typĂłw zwracanych. |
| `hasLuaField(...)` | Sprawdza, czy obiekt ma pole o danej nazwie w swojej tabeli Lua. |
| `setLuaField(...)` | Ustawia wartoÄąâ€şÄ‡ pola w tabeli Lua. |
| `getLuaField(...)` | Pobiera wartoÄąâ€şÄ‡ pola z tabeli Lua. |
| **Niskopoziomowe metody do interakcji z Lua** | |
| `releaseLuaFieldsTable()`| Zwalnia referencjÄ™ do tabeli pĂłl. |
| `luaSetField(...)` | Ustawia pole, pobierajÄ…c wartoÄąâ€şÄ‡ ze szczytu stosu Lua. |
| `luaGetField(...)` | Pobiera pole i umieszcza jego wartoÄąâ€şÄ‡ na stosie Lua. |
| `luaGetMetatable()` | Pobiera i umieszcza na stosie metatabelÄ™ klasy. |
| `luaGetFieldsTable()`| Umieszcza na stosie tabelÄ™ pĂłl obiektu. |
| **Metody pomocnicze** | |
| `getUseCount()` | Zwraca liczbÄ™ referencji do obiektu. |
| `getClassName()` | Zwraca nazwÄ™ klasy. |
## Zmienne prywatne

-   `m_fieldsTableRef`: Przechowuje referencjÄ™ (indeks w rejestrze Lua) do tabeli pĂłl tego obiektu.
## Funkcje globalne (`connect`)

Szablonowe funkcje globalne, ktĂłre sÄ… wygodnym opakowaniem na `LuaObject::connectLuaField`, pozwalajÄ…c na Äąâ€šatwe Äąâ€šÄ…czenie zarĂłwno `std::function`, jak i lambd z polami obiektĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/util/stats.h`: Potencjalnie do statystyk.
-   `framework/luaengine/declarations.h`: Podstawowe deklaracje.
-   Jest klasÄ… bazowÄ… dla prawie kaÄąÄ˝dej klasy w projekcie, ktĂłra jest eksportowana do Lua (np. `UIWidget`, `Protocol`, `Module`).
-   Oznaczona jako `@bindclass`, jej podstawowe metody (`getUseCount`, `getClassName`, `getFieldsTable`) sÄ… dostÄ™pne w Lua.

---
# Ä‘Ĺşâ€śâ€ž luavaluecasts.cpp
## Opis ogĂłlny

Plik `luavaluecasts.cpp` zawiera implementacje specjalizacji szablonĂłw `push_luavalue` i `luavalue_cast` dla podstawowych typĂłw danych. Te funkcje sÄ… sercem systemu konwersji typĂłw miÄ™dzy C++ a Lua.
## Funkcje `push_luavalue`
## Opis semantyczny
KaÄąÄ˝da funkcja `push_luavalue` przyjmuje wartoÄąâ€şÄ‡ typu C++ i umieszcza jej odpowiednik na szczycie stosu Lua. Zwraca liczbÄ™ wartoÄąâ€şci umieszczonych na stosie (zwykle 1).
## Implementacje:
-   `bool`: `g_lua.pushBoolean(b)`
-   `int`: `g_lua.pushInteger(i)`
-   `double`: `g_lua.pushNumber(d)`
-   `const char*`, `std::string`: `g_lua.pushString(str)`
-   `LuaCppFunction`: `g_lua.pushCppFunction(func)`
-   **Typy zÄąâ€šoÄąÄ˝one (`Color`, `Rect`, `Point`, `Size`)**: TworzÄ… nowÄ… tabelÄ™ w Lua i wypeÄąâ€šniajÄ… jÄ… odpowiednimi polami (np. `r`, `g`, `b`, `a` dla `Color`).
-   **`OTMLNodePtr`**: Konwertuje wÄ™zeÄąâ€š OTML na tabelÄ™ Lua, rekurencyjnie przetwarzajÄ…c jego dzieci.
## Funkcje `luavalue_cast`
## Opis semantyczny
KaÄąÄ˝da funkcja `luavalue_cast` prĂłbuje odczytaÄ‡ wartoÄąâ€şÄ‡ z podanego indeksu na stosie Lua i skonwertowaÄ‡ jÄ… na odpowiedni typ C++. Zwraca `true` w przypadku sukcesu.
## Implementacje:
-   `bool`: `g_lua.toBoolean(index)`
-   `int`, `double`: `g_lua.toInteger(index)`, `g_lua.toNumber(index)`. SprawdzajÄ… dodatkowo, czy wartoÄąâ€şÄ‡ na stosie jest faktycznie liczbÄ….
-   `std::string`: `g_lua.toString(index)`
-   **Typy zÄąâ€šoÄąÄ˝one (`Color`, `Rect`, ...)**: SprawdzajÄ…, czy na stosie jest tabela z odpowiednimi polami lub string, ktĂłry moÄąÄ˝na sparsowaÄ‡. OdczytujÄ… wartoÄąâ€şci z tabeli i przypisujÄ… je do obiektu C++.
-   **`OTMLNodePtr`**: Konwertuje tabelÄ™ Lua z powrotem na strukturÄ™ wÄ™zÄąâ€šĂłw OTML.
-   **`LuaObjectPtr`**: Sprawdza, czy na stosie jest `userdata` i rzutuje je na odpowiedni typ wskaÄąĹźnika.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/luaengine/luavaluecasts.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/luaengine/luainterface.h`: UÄąÄ˝ywajÄ… metod `g_lua` do interakcji ze stosem.
-   `framework/otml/otmlnode.h`: Do konwersji wÄ™zÄąâ€šĂłw OTML.
-   SÄ… to funkcje niskiego poziomu, uÄąÄ˝ywane przez `LuaInterface::polymorphicPush` i `LuaInterface::castValue` do automatycznej konwersji typĂłw.

---
# Ä‘Ĺşâ€śâ€ž luavaluecasts.h
## Opis ogĂłlny

Plik `luavaluecasts.h` deklaruje zestaw szablonowych funkcji `push_luavalue` i `luavalue_cast`, ktĂłre definiujÄ…, w jaki sposĂłb rĂłÄąÄ˝ne typy danych C++ sÄ… konwertowane do i z wartoÄąâ€şci Lua. Jest to kluczowy element systemu bindowania, ktĂłry umoÄąÄ˝liwia automatycznÄ… konwersjÄ™ argumentĂłw funkcji i wartoÄąâ€şci zwracanych.
## Szablony i funkcje
## `push_luavalue<T>(const T& v)`
## Opis
Szablon funkcji, ktĂłry przyjmuje wartoÄąâ€şÄ‡ typu `T` i umieszcza jej reprezentacjÄ™ na stosie Lua. Dla kaÄąÄ˝dego typu, ktĂłry ma byÄ‡ przekazywany miÄ™dzy C++ a Lua, musi istnieÄ‡ specjalizacja tej funkcji.
## `luavalue_cast<T>(int index, T& v)`
## Opis
Szablon funkcji, ktĂłry prĂłbuje odczytaÄ‡ wartoÄąâ€şÄ‡ z podanego indeksu `index` na stosie Lua i skonwertowaÄ‡ jÄ… do typu `T`. Zwraca `true`, jeÄąâ€şli konwersja siÄ™ powiedzie.
## Zadeklarowane specjalizacje

Plik deklaruje (a w przypadku typĂłw prostych, rĂłwnieÄąÄ˝ definiuje `inline`) specjalizacje dla:
-   **TypĂłw prostych**: `bool`, `int`, `double`, `float`, liczby caÄąâ€škowite o staÄąâ€šym rozmiarze (`int8`, `uint16`, itp.).
-   **StringĂłw**: `const char*`, `std::string`.
-   **Funkcji C++**: `LuaCppFunction`, `std::function`.
-   **Struktur frameworka**: `Color`, `Rect`, `Point`, `Size`.
-   **WÄ™zÄąâ€šĂłw OTML**: `OTMLNodePtr`.
-   **TypĂłw wyliczeniowych (enum)**.
-   **ObiektĂłw C++**: `LuaObjectPtr` i wskaÄąĹźniki do klas pochodnych.
-   **KontenerĂłw STL**: `std::list`, `std::vector`, `std::set`, `std::deque`, `std::map`.
-   **Krotek**: `std::tuple`.
## PrzykÄąâ€šad dziaÄąâ€šania

`$fenceInfo
// C++
void myFunction(int a, const std::string& b) { /* ... */ }

// Lua
myFunction(10, "hello")
```
Gdy `myFunction` jest wywoÄąâ€šywana z Lua, `luabinder` uÄąÄ˝yje:
-   `luavalue_cast(1, int&)` do konwersji `10` z Lua na `int` w C++.
-   `luavalue_cast(2, std::string&)` do konwersji `"hello"` z Lua na `std::string` w C++.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to plik wewnÄ™trzny, doÄąâ€šÄ…czany tylko przez `luainterface.h`.
-   Wymaga definicji `LuaInterface`, `LuaObject`, `LuaException`.
-   Jest podstawÄ… caÄąâ€šego systemu automatycznej konwersji typĂłw, uÄąÄ˝ywanego przez `luabinder`.

---
# Ä‘Ĺşâ€śâ€ž connection.cpp
## Opis ogĂłlny

Plik `connection.cpp` zawiera implementacjÄ™ klasy `Connection`, ktĂłra jest niskopoziomowym opakowaniem na asynchroniczne gniazdo TCP (TCP socket) z biblioteki Boost.Asio. ZarzÄ…dza ona cyklem ÄąÄ˝ycia poÄąâ€šÄ…czenia, operacjami odczytu i zapisu oraz obsÄąâ€šugÄ… bÄąâ€šÄ™dĂłw.
## Zmienne globalne

-   `g_ioService`: Globalna instancja `boost::asio::io_service`, ktĂłra jest sercem pÄ™tli zdarzeÄąâ€ž dla wszystkich operacji sieciowych.
-   `Connection::m_outputStreams`: Statyczna lista, ktĂłra dziaÄąâ€ša jak pula buforĂłw wyjÄąâ€şciowych. ZuÄąÄ˝yte bufory sÄ… do niej zwracane, co pozwala na ich ponowne wykorzystanie i redukuje alokacjÄ™ pamiÄ™ci.
## Klasa `Connection`
## `Connection::Connection()`

Konstruktor. Inicjalizuje obiekty Boost.Asio (`timer`, `resolver`, `socket`) powiÄ…zane z `g_ioService`.
## `void Connection::poll()` i `void Connection::terminate()`

Statyczne metody, ktĂłre zarzÄ…dzajÄ… globalnym `g_ioService`. `poll()` przetwarza zdarzenia sieciowe, a `terminate()` zatrzymuje `io_service`.
## `void Connection::close()`

Zamyka poÄąâ€šÄ…czenie. Anuluje wszystkie aktywne operacje asynchroniczne, zamyka gniazdo i resetuje callbacki.
## `void Connection::connect(...)`

Rozpoczyna proces nawiÄ…zywania poÄąâ€šÄ…czenia. WywoÄąâ€šuje `m_resolver.async_resolve` w celu przetÄąâ€šumaczenia nazwy hosta na adres IP.
## `void Connection::write(uint8* buffer, size_t size)`

Dodaje dane do bufora wyjÄąâ€şciowego (`m_outputStream`). Aby uniknÄ…Ä‡ zatorĂłw (congestion), faktyczne wysÄąâ€šanie danych jest opĂłÄąĹźniane o 0 milisekund za pomocÄ… `m_delayedWriteTimer`. Oznacza to, ÄąÄ˝e wysÄąâ€šanie nastÄ…pi w nastÄ™pnej iteracji pÄ™tli `io_service`, co pozwala na zgrupowanie wielu maÄąâ€šych zapisĂłw w jeden wiÄ™kszy.
## Metody `read(...)`, `read_until(...)`, `read_some(...)`

InicjujÄ… asynchroniczne operacje odczytu danych z gniazda. UstawiajÄ… `m_recvCallback`, ktĂłry zostanie wywoÄąâ€šany po otrzymaniu danych, oraz `m_readTimer` do obsÄąâ€šugi timeoutu.
## Metody `on...()`

SÄ… to handlery (funkcje zwrotne) dla operacji asynchronicznych Boost.Asio:
-   `onResolve`: WywoÄąâ€šywana po rozwiÄ…zaniu nazwy DNS. Inicjuje poÄąâ€šÄ…czenie.
-   `onConnect`: WywoÄąâ€šywana po nawiÄ…zaniu poÄąâ€šÄ…czenia. Ustawia opcje gniazda (np. `no_delay` - wyÄąâ€šÄ…czenie algorytmu Nagle'a) i wywoÄąâ€šuje `m_connectCallback`.
-   `onCanWrite`: WywoÄąâ€šywana przez `m_delayedWriteTimer`. Inicjuje faktyczne wysÄąâ€šanie danych.
-   `onWrite`: WywoÄąâ€šywana po zakoÄąâ€žczeniu operacji zapisu. Zwraca bufor do puli.
-   `onRecv`: WywoÄąâ€šywana po otrzymaniu danych. Przekazuje dane do `m_recvCallback`.
-   `onTimeout`: WywoÄąâ€šywana, gdy upÄąâ€šynie czas oczekiwania na operacjÄ™.
## `void Connection::handleError(...)`

Centralna funkcja do obsÄąâ€šugi bÄąâ€šÄ™dĂłw sieciowych. Zapisuje bÄąâ€šÄ…d, wywoÄąâ€šuje `m_errorCallback` i zamyka poÄąâ€šÄ…czenie.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/connection.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/application.h`, `eventdispatcher.h`: Do walidacji i planowania zdarzeÄąâ€ž.
-   `boost/asio`: Kluczowa zaleÄąÄ˝noÄąâ€şÄ‡ do obsÄąâ€šugi sieci.
-   Jest uÄąÄ˝ywana przez klasÄ™ `Protocol` do implementacji protokoÄąâ€šu komunikacyjnego z serwerem gry.

---
# Ä‘Ĺşâ€śâ€ž server.h
## Opis ogĂłlny

Plik `server.h` deklaruje klasÄ™ `Server`, ktĂłra jest prostym opakowaniem na `boost::asio::ip::tcp::acceptor`. UmoÄąÄ˝liwia tworzenie serwera TCP, ktĂłry nasÄąâ€šuchuje na przychodzÄ…ce poÄąâ€šÄ…czenia na okreÄąâ€şlonym porcie.
## Klasa `Server`
## Opis semantyczny
`Server` dziedziczy po `LuaObject`, co pozwala na tworzenie i zarzÄ…dzanie serwerami z poziomu skryptĂłw Lua. Jego gÄąâ€šĂłwnym zadaniem jest akceptowanie nowych poÄąâ€šÄ…czeÄąâ€ž i przekazywanie ich do obsÄąâ€šugi (np. w formie obiektu `Connection`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Server(int port)` | Konstruktor, tworzy i bindowanie akceptor do podanego portu. |
| `static ServerPtr create(int port)` | Metoda fabryczna, ktĂłra tworzy `Server` i opakowuje go w `shared_ptr`. |
| `bool isOpen()` | Zwraca `true`, jeÄąâ€şli serwer nasÄąâ€šuchuje. |
| `void close()` | Zamyka akceptor, przestajÄ…c nasÄąâ€šuchiwaÄ‡. |
| `void acceptNext()` | Inicjuje asynchronicznÄ… operacjÄ™ oczekiwania na nastÄ™pne poÄąâ€šÄ…czenie. Po jego nadejÄąâ€şciu, wywoÄąâ€šywany jest `callback` `onAccept` w Lua. |
## Zmienne prywatne

-   `m_isOpen`: Flaga wskazujÄ…ca, czy serwer jest aktywny.
-   `m_acceptor`: Obiekt `tcp::acceptor` z Boost.Asio.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   `boost/asio`: UÄąÄ˝ywa `tcp::acceptor`.
-   Jest uÄąÄ˝ywana do implementacji serwerĂłw nasÄąâ€šuchujÄ…cych w Lua, np. do niestandardowych narzÄ™dzi lub protokoÄąâ€šĂłw.

---
# Ä‘Ĺşâ€śâ€ž connection.h
## Opis ogĂłlny

Plik `connection.h` deklaruje klasÄ™ `Connection`, ktĂłra jest interfejsem do asynchronicznego poÄąâ€šÄ…czenia TCP. Jest to kluczowy element podsystemu sieciowego.
## Klasa `Connection`
## Opis semantyczny
`Connection` enkapsuluje `boost::asio::ip::tcp::socket` i zarzÄ…dza caÄąâ€šym cyklem ÄąÄ˝ycia poÄąâ€šÄ…czenia: od nawiÄ…zywania, przez wysyÄąâ€šanie i odbieranie danych, aÄąÄ˝ po zamykanie i obsÄąâ€šugÄ™ bÄąâ€šÄ™dĂłw. DziaÄąâ€ša w peÄąâ€šni asynchronicznie, integrujÄ…c siÄ™ z globalnÄ… pÄ™tlÄ… zdarzeÄąâ€ž `g_ioService`. Dziedziczy po `LuaObject`, co umoÄąÄ˝liwia jej uÄąÄ˝ycie w Lua.
## StaÄąâ€še

-   `READ_TIMEOUT`, `WRITE_TIMEOUT`: Czas (w sekundach) na zakoÄąâ€žczenie operacji odczytu/zapisu.
-   `SEND_BUFFER_SIZE`, `RECV_BUFFER_SIZE`: Rozmiary buforĂłw.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Statyczne** | |
| `static void poll()` | Przetwarza zdarzenia w globalnym `g_ioService`. |
| `static void terminate()` | Zatrzymuje `g_ioService`. |
| **Cykl ÄąÄ˝ycia** | |
| `void connect(...)` | Rozpoczyna asynchroniczne nawiÄ…zywanie poÄąâ€šÄ…czenia. |
| `void close()` | Zamyka poÄąâ€šÄ…czenie. |
| **Operacje I/O** | |
| `void write(...)` | Dodaje dane do kolejki wysyÄąâ€šania. |
| `void read(...)` | Rozpoczyna asynchroniczny odczyt okreÄąâ€şlonej liczby bajtĂłw. |
| `void read_until(...)` | Odczytuje dane aÄąÄ˝ do napotkania okreÄąâ€şlonego separatora. |
| `void read_some(...)` | Odczytuje dowolnÄ… iloÄąâ€şÄ‡ dostÄ™pnych danych (nie wiÄ™cej niÄąÄ˝ rozmiar bufora). |
| **Callbacki i stan** | |
| `void setErrorCallback(...)`| Ustawia funkcjÄ™ zwrotnÄ… dla bÄąâ€šÄ™dĂłw. |
| `int getIp()` | Zwraca adres IP zdalnego hosta. |
| `boost::system::error_code getError()` | Zwraca ostatni bÄąâ€šÄ…d. |
| `bool isConnecting()` | Zwraca `true`, jeÄąâ€şli trwa nawiÄ…zywanie poÄąâ€šÄ…czenia. |
| `bool isConnected()` | Zwraca `true`, jeÄąâ€şli poÄąâ€šÄ…czenie jest aktywne. |
| `ticks_t getElapsedTicksSinceLastRead()` | Zwraca czas od ostatniej operacji odczytu (do wykrywania timeoutĂłw na wyÄąÄ˝szym poziomie). |
## Zmienne chronione

-   `m_connectCallback`, `m_errorCallback`, `m_recvCallback`: Funkcje zwrotne.
-   `m_readTimer`, `m_writeTimer`, ...: Obiekty Boost.Asio (timery, resolver, socket).
-   `m_outputStream`, `m_inputStream`: Bufory do zapisu i odczytu.
-   `m_connected`, `m_connecting`: Flagi stanu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/declarations.h`: Deklaracje typĂłw.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/core/timer.h`: Do Äąâ€şledzenia aktywnoÄąâ€şci.
-   Jest uÄąÄ˝ywana przez `Protocol` do komunikacji z serwerem gry.
-   Jest zwracana przez `Server` po zaakceptowaniu nowego poÄąâ€šÄ…czenia.

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## Opis ogĂłlny

Plik `declarations.h` w module `net` sÄąâ€šuÄąÄ˝y do wczesnych deklaracji (forward declarations) i definicji typĂłw wskaÄąĹźnikĂłw dla klas zwiÄ…zanych z obsÄąâ€šugÄ… sieci. Pomaga to unikaÄ‡ zaleÄąÄ˝noÄąâ€şci cyklicznych i skraca czas kompilacji.
## Deklaracje
## `namespace asio`

Deklaruje, ÄąÄ˝e `asio` jest aliasem dla `boost::asio`.
## Wczesne deklaracje klas

-   `InputMessage`
-   `OutputMessage`
-   `Connection`
-   `Protocol`
-   `Server`
-   `PacketPlayer`
-   `PacketRecorder`
## Definicje typĂłw

Definiuje aliasy dla inteligentnych wskaÄąĹźnikĂłw (`shared_object_ptr`) do klas sieciowych.

-   `InputMessagePtr`
-   `OutputMessagePtr`
-   `ConnectionPtr`
-   `ProtocolPtr`
-   `ServerPtr`
-   `PacketPlayerPtr`
-   `PacketRecorderPtr`
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doÄąâ€šÄ…czany przez wiÄ™kszoÄąâ€şÄ‡ plikĂłw nagÄąâ€šĂłwkowych w module `net`.

---
# Ä‘Ĺşâ€śâ€ž inputmessage.h
## Opis ogĂłlny

Plik `inputmessage.h` deklaruje klasÄ™ `InputMessage`, ktĂłra jest narzÄ™dziem do parsowania przychodzÄ…cych pakietĂłw sieciowych.
## Klasa `InputMessage`
## Opis semantyczny
`InputMessage` dziaÄąâ€ša jak bufor z wskaÄąĹźnikiem odczytu. Przechowuje surowe dane pakietu i udostÄ™pnia metody do sekwencyjnego odczytywania z niego rĂłÄąÄ˝nych typĂłw danych (np. `getU8`, `getU16`, `getString`). ZarzÄ…dza rĂłwnieÄąÄ˝ pozycjÄ… nagÄąâ€šĂłwka, co pozwala na oddzielenie metadanych pakietu (rozmiar, suma kontrolna) od jego wÄąâ€šaÄąâ€şciwej zawartoÄąâ€şci (ciaÄąâ€ša).
## StaÄąâ€še

-   `BUFFER_MAXSIZE`: Maksymalny rozmiar bufora.
-   `MAX_HEADER_SIZE`: Maksymalny rozmiar nagÄąâ€šĂłwka (rezerwowane miejsce na poczÄ…tku bufora).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setBuffer(...)` | Kopiuje dane z `std::string` do wewnÄ™trznego bufora. |
| `getBuffer()` | Zwraca caÄąâ€šy pakiet (nagÄąâ€šĂłwek + ciaÄąâ€šo) jako `std::string`. |
| `getBodyBuffer()`| Zwraca tylko ciaÄąâ€šo pakietu. |
| `skipBytes(uint32 bytes)` | Przesuwa wskaÄąĹźnik odczytu. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | OdczytujÄ… liczby caÄąâ€škowite bez znaku. |
| `getString()` | Odczytuje string (poprzedzony dÄąâ€šugoÄąâ€şciÄ… U16). |
| `getDouble()` | Odczytuje liczbÄ™ zmiennoprzecinkowÄ… w niestandardowym formacie. |
| `peekU8()`, ... | OdczytujÄ… wartoÄąâ€şÄ‡ bez przesuwania wskaÄąĹźnika. |
| `decryptRsa(...)` | Deszyfruje fragment bufora za pomocÄ… RSA. |
| `getHeaderSize()`, `getMessageSize()`, `getUnreadSize()` | ZwracajÄ… informacje o rozmiarach. |
| `eof()` | Zwraca `true`, jeÄąâ€şli wszystkie dane zostaÄąâ€šy odczytane. |
## Metody chronione (uÄąÄ˝ywane przez `Protocol`)

-   `reset()`: Resetuje stan wiadomoÄąâ€şci.
-   `fillBuffer(...)`: Dopisuje dane do bufora.
-   `setHeaderSize(...)`: Ustawia rozmiar nagÄąâ€šĂłwka.
-   `readChecksum()`: Odczytuje i weryfikuje sumÄ™ kontrolnÄ….
## Zmienne prywatne

-   `m_headerPos`: Pozycja startowa nagÄąâ€šĂłwka.
-   `m_readPos`: Aktualna pozycja odczytu.
-   `m_messageSize`: CaÄąâ€škowity rozmiar wiadomoÄąâ€şci (bez nagÄąâ€šĂłwka).
-   `m_buffer`: Bufor na dane.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Oznaczona jako `@bindclass`, jest dostÄ™pna w Lua.
-   Jest tworzona i zarzÄ…dzana przez `Protocol` do parsowania danych otrzymanych z `Connection`.

---
# Ä‘Ĺşâ€śâ€ž outputmessage.cpp
## Opis ogĂłlny

Plik `outputmessage.cpp` zawiera implementacjÄ™ klasy `OutputMessage`, ktĂłra sÄąâ€šuÄąÄ˝y do budowania wychodzÄ…cych pakietĂłw sieciowych.
## Klasa `OutputMessage`
## `OutputMessage::OutputMessage()`

Konstruktor, wywoÄąâ€šuje `reset()`.
## `void OutputMessage::reset()`

Resetuje stan wiadomoÄąâ€şci, ustawiajÄ…c wskaÄąĹźnik zapisu (`m_writePos`) i pozycjÄ™ nagÄąâ€šĂłwka (`m_headerPos`) na poczÄ…tek obszaru na ciaÄąâ€šo wiadomoÄąâ€şci.
## `void OutputMessage::setBuffer(const std::string& buffer)`

Kopiuje dane z `std::string` do bufora wiadomoÄąâ€şci.
## Metody `add...()`

SÄąâ€šuÄąÄ˝Ä… do dodawania rĂłÄąÄ˝nych typĂłw danych na koniec wiadomoÄąâ€şci.
-   `addU8`, `addU16`, `addU32`, `addU64`: DodajÄ… liczby caÄąâ€škowite, konwertujÄ…c je do porzÄ…dku Little Endian.
-   `addString`: Dodaje `std::string`, poprzedzajÄ…c go 2-bajtowÄ… dÄąâ€šugoÄąâ€şciÄ….
-   `addRawString`: Dodaje `std::string` bez informacji o dÄąâ€šugoÄąâ€şci.
-   `addPaddingBytes`: Dodaje okreÄąâ€şlonÄ… liczbÄ™ bajtĂłw wypeÄąâ€šniajÄ…cych.
-   KaÄąÄ˝da z tych metod wywoÄąâ€šuje `checkWrite` w celu sprawdzenia, czy jest wystarczajÄ…co miejsca w buforze.
## `void OutputMessage::encryptRsa()`

Szyfruje ostatnie `N` bajtĂłw bufora za pomocÄ… klucza publicznego RSA, gdzie `N` to rozmiar klucza.
## Metody `write...()`

Metody te operujÄ… na zarezerwowanym miejscu na nagÄąâ€šĂłwek (przed ciaÄąâ€šem wiadomoÄąâ€şci):
-   `writeChecksum()`: Oblicza sumÄ™ kontrolnÄ… Adler-32 dla ciaÄąâ€ša wiadomoÄąâ€şci i zapisuje jÄ… w nagÄąâ€šĂłwku.
-   `writeSequence()`: Zapisuje numer sekwencyjny pakietu.
-   `writeMessageSize()`: Zapisuje caÄąâ€škowity rozmiar ciaÄąâ€ša wiadomoÄąâ€şci w nagÄąâ€šĂłwku.
## `void OutputMessage::checkWrite(int bytes)`

Sprawdza, czy dodanie `bytes` bajtĂłw nie przekroczy maksymalnego rozmiaru bufora. JeÄąâ€şli tak, rzuca wyjÄ…tek.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/outputmessage.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/util/crypt.h`: UÄąÄ˝ywa `g_crypt` do szyfrowania RSA i `stdext::adler32` do sum kontrolnych.
-   Jest tworzona przez kod logiki gry, wypeÄąâ€šniana danymi, a nastÄ™pnie przekazywana do `Protocol::send()` w celu wysÄąâ€šania.

---
# Ä‘Ĺşâ€śâ€ž outputmessage.h
## Opis ogĂłlny

Plik `outputmessage.h` deklaruje klasÄ™ `OutputMessage`, ktĂłra jest narzÄ™dziem do konstruowania wychodzÄ…cych pakietĂłw sieciowych.
## Klasa `OutputMessage`
## Opis semantyczny
`OutputMessage` dziaÄąâ€ša jak bufor z wskaÄąĹźnikiem zapisu. UdostÄ™pnia metody do dodawania rĂłÄąÄ˝nych typĂłw danych (`addU8`, `addString`, itp.), ktĂłre sÄ… doÄąâ€šÄ…czane na koÄąâ€žcu bufora. Posiada rĂłwnieÄąÄ˝ zarezerwowane miejsce na poczÄ…tku bufora na nagÄąâ€šĂłwek, ktĂłry jest wypeÄąâ€šniany tuÄąÄ˝ przed wysÄąâ€šaniem (np. rozmiarem wiadomoÄąâ€şci, sumÄ… kontrolnÄ…).
## StaÄąâ€še

-   `BUFFER_MAXSIZE`: Maksymalny rozmiar bufora.
-   `MAX_STRING_LENGTH`: Maksymalna dÄąâ€šugoÄąâ€şÄ‡ stringa.
-   `MAX_HEADER_SIZE`: Rozmiar zarezerwowanego miejsca na nagÄąâ€šĂłwek.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `reset()` | Resetuje wiadomoÄąâ€şÄ‡ do stanu poczÄ…tkowego. |
| `setBuffer(...)` | Ustawia zawartoÄąâ€şÄ‡ ciaÄąâ€ša wiadomoÄąâ€şci. |
| `getBuffer()` | Zwraca gotowy pakiet (nagÄąâ€šĂłwek + ciaÄąâ€šo) jako `std::string`. |
| `addU8()`, ..., `addString()` | DodajÄ… dane do ciaÄąâ€ša wiadomoÄąâ€şci. |
| `encryptRsa()` | Szyfruje czÄ™Äąâ€şÄ‡ wiadomoÄąâ€şci za pomocÄ… RSA. |
| `getWritePos()` | Zwraca aktualnÄ… pozycjÄ™ zapisu. |
| `getMessageSize()` | Zwraca aktualny rozmiar ciaÄąâ€ša wiadomoÄąâ€şci. |
| `setWritePos(...)`, `setMessageSize(...)` | UstawiajÄ… pozycjÄ™ zapisu i rozmiar. |
## Metody chronione (uÄąÄ˝ywane przez `Protocol`)

-   `getHeaderBuffer()`: Zwraca wskaÄąĹźnik na poczÄ…tek gotowego pakietu (poczÄ…tek nagÄąâ€šĂłwka).
-   `writeChecksum()`, `writeSequence()`, `writeMessageSize()`: WypeÄąâ€šniajÄ… nagÄąâ€šĂłrek odpowiednimi metadanymi.
## Zmienne prywatne

-   `m_headerPos`: Aktualna pozycja poczÄ…tku nagÄąâ€šĂłwka.
-   `m_writePos`: Aktualna pozycja zapisu w ciele wiadomoÄąâ€şci.
-   `m_messageSize`: Rozmiar caÄąâ€šego pakietu (nagÄąâ€šĂłwek + ciaÄąâ€šo).
-   `m_buffer`: Bufor na dane.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Oznaczona jako `@bindclass`, jest dostÄ™pna w Lua do tworzenia pakietĂłw.
-   Jest uÄąÄ˝ywana przez `Protocol` do przygotowania pakietĂłw do wysÄąâ€šania przez `Connection`.

---
# Ä‘Ĺşâ€śâ€ž packet_player.cpp
## Opis ogĂłlny

Plik `packet_player.cpp` zawiera implementacjÄ™ klasy `PacketPlayer`, ktĂłra umoÄąÄ˝liwia odtwarzanie wczeÄąâ€şniej nagranych sesji sieciowych. Jest to narzÄ™dzie do debugowania i testowania.
## Klasa `PacketPlayer`
## `PacketPlayer::PacketPlayer(const std::string& file)`

Konstruktor.
-   **DziaÄąâ€šanie**:
    1.  Otwiera plik nagrania z katalogu `records/`.
    2.  Czyta plik linia po linii.
    3.  KaÄąÄ˝da linia zawiera typ pakietu (`<` dla przychodzÄ…cego, `>` dla wychodzÄ…cego), sygnaturÄ™ czasowÄ… i dane pakietu w formacie heksadecymalnym.
    4.  Dekoduje dane heksadecymalne do postaci binarnej i zapisuje pakiety w odpowiednich kolejkach (`m_input` lub `m_output`).
## `PacketPlayer::~PacketPlayer()`

Destruktor. Anuluje zaplanowane zdarzenie (`m_event`), jeÄąâ€şli istnieje.
## `void PacketPlayer::start(...)`

Rozpoczyna odtwarzanie.
-   **DziaÄąâ€šanie**:
    1.  Zapisuje czas startu (`m_start`).
    2.  Zapisuje callbacki do obsÄąâ€šugi "otrzymanych" pakietĂłw i zdarzenia rozÄąâ€šÄ…czenia.
    3.  Planuje pierwsze wywoÄąâ€šanie metody `process()` za 50ms.
## `void PacketPlayer::stop()`

Zatrzymuje odtwarzanie, anulujÄ…c zdarzenie.
## `void PacketPlayer::onOutputPacket(const OutputMessagePtr& packet)`

Metoda wywoÄąâ€šywana przez `Protocol`, gdy prĂłbuje on wysÄąâ€šaÄ‡ pakiet. W trybie odtwarzania, pakiety wychodzÄ…ce sÄ… analizowane (np. w celu wykrycia wylogowania), ale nie sÄ… nigdzie wysyÄąâ€šane.
## `void PacketPlayer::process()`
## Opis semantyczny
GÄąâ€šĂłwna metoda pÄ™tli odtwarzacza.
## DziaÄąâ€šanie
1.  Iteruje po kolejce pakietĂłw przychodzÄ…cych (`m_input`).
2.  Sprawdza sygnaturÄ™ czasowÄ… kaÄąÄ˝dego pakietu. JeÄąâ€şli czas odtworzenia pakietu (`packet.first + m_start`) juÄąÄ˝ minÄ…Äąâ€š, wywoÄąâ€šuje `m_recvCallback` z danymi pakietu i usuwa go z kolejki.
3.  JeÄąâ€şli kolejka nie jest pusta, planuje swoje nastÄ™pne wywoÄąâ€šanie z opĂłÄąĹźnieniem rĂłwnym rĂłÄąÄ˝nicy czasu do nastÄ™pnego pakietu.
4.  JeÄąâ€şli kolejka jest pusta, wywoÄąâ€šuje `m_disconnectCallback`, symulujÄ…c koniec sesji.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/packet_player.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/clock.h`, `eventdispatcher.h`: Do zarzÄ…dzania czasem i planowania zdarzeÄąâ€ž.
-   `boost/algorithm/hex.hpp`: Do dekodowania danych z formatu heksadecymalnego.
-   Jest uÄąÄ˝ywana przez `Protocol` w trybie odtwarzania.

---
# Ä‘Ĺşâ€śâ€ž packet_player.h
## Opis ogĂłlny

Plik `packet_player.h` deklaruje klasÄ™ `PacketPlayer`, ktĂłra sÄąâ€šuÄąÄ˝y do odtwarzania nagranych sesji sieciowych z plikĂłw.
## Klasa `PacketPlayer`
## Opis semantyczny
`PacketPlayer` odczytuje plik z zarejestrowanymi pakietami i ich sygnaturami czasowymi. Po uruchomieniu, symuluje przychodzÄ…ce pakiety sieciowe, wywoÄąâ€šujÄ…c `callback` w odpowiednich odstÄ™pach czasu, zgodnie z nagraniem. Pozwala to na debugowanie i testowanie logiki klienta bez potrzeby Äąâ€šÄ…czenia siÄ™ z serwerem. Dziedziczy po `LuaObject`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PacketPlayer(const std::string& file)` | Konstruktor, Äąâ€šaduje nagranie z pliku. |
| `virtual ~PacketPlayer()` | Destruktor. |
| `void start(...)` | Rozpoczyna odtwarzanie sesji. Przyjmuje callbacki na otrzymanie pakietu i na rozÄąâ€šÄ…czenie. |
| `void stop()` | Zatrzymuje odtwarzanie. |
| `void onOutputPacket(...)` | Przechwytuje pakiety, ktĂłre normalnie byÄąâ€šyby wysÄąâ€šane, w celu symulacji (np. wykrycia wylogowania). |
## Zmienne prywatne

-   `m_start`: Czas rozpoczÄ™cia odtwarzania.
-   `m_event`: WskaÄąĹźnik na zaplanowane zdarzenie do przetwarzania pakietĂłw.
-   `m_input`, `m_output`: Kolejki (`std::deque`) przechowujÄ…ce pary (czas, dane pakietu) dla pakietĂłw przychodzÄ…cych i wychodzÄ…cych.
-   `m_recvCallback`: `Callback` wywoÄąâ€šywany z danymi "otrzymanego" pakietu.
-   `m_disconnectCallback`: `Callback` wywoÄąâ€šywany na koniec sesji.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/core/eventdispatcher.h`: Do planowania zdarzeÄąâ€ž.
-   `framework/net/outputmessage.h`: Do analizy pakietĂłw wychodzÄ…cych.
-   Jest tworzona i uÄąÄ˝ywana przez `Protocol` w trybie odtwarzania.

---
# Ä‘Ĺşâ€śâ€ž protocol.h
## Opis ogĂłlny

Plik `protocol.h` deklaruje klasÄ™ `Protocol`, ktĂłra jest klasÄ… bazowÄ… do implementacji protokoÄąâ€šĂłw komunikacji sieciowej.
## Klasa `Protocol`
## Opis semantyczny
`Protocol` jest abstrakcjÄ… wysokiego poziomu, ktĂłra zarzÄ…dza poÄąâ€šÄ…czeniem (`Connection`) i implementuje logikÄ™ specyficznÄ… dla danego protokoÄąâ€šu, takÄ… jak szyfrowanie XTEA, obsÄąâ€šuga sum kontrolnych, kompresja i sekwencjonowanie pakietĂłw. Przetwarza surowe dane z `Connection` na obiekty `InputMessage` i przygotowuje `OutputMessage` do wysÄąâ€šania. Dziedziczy po `LuaObject`, co pozwala na tworzenie implementacji protokoÄąâ€šĂłw w Lua.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `connect(...)` | NawiÄ…zuje poÄąâ€šÄ…czenie z serwerem. |
| `disconnect()` | Zamyka poÄąâ€šÄ…czenie. |
| `setRecorder(...)` / `playRecord(...)` | WÄąâ€šÄ…cza tryb nagrywania lub odtwarzania sesji. |
| `bool isConnected()` / `isConnecting()` | ZwracajÄ… stan poÄąâ€šÄ…czenia. |
| `ConnectionPtr getConnection()` | Zwraca obiekt `Connection`. |
| **Konfiguracja protokoÄąâ€šu** | |
| `generateXteaKey()`, `setXteaKey(...)`, `enableXteaEncryption()` | ZarzÄ…dzajÄ… szyfrowaniem XTEA. |
| `enableChecksum()`, `enabledSequencedPackets()`, `enableBigPackets()`, `enableCompression()` | WÄąâ€šÄ…czajÄ… rĂłÄąÄ˝ne cechy protokoÄąâ€šu. |
| **Operacje I/O** | |
| `virtual void send(...)` | WysyÄąâ€ša `OutputMessage`, opcjonalnie szyfrujÄ…c i dodajÄ…c nagÄąâ€šĂłwki. |
| `virtual void recv()` | Inicjuje proces odbierania nastÄ™pnego pakietu. |
## Metody chronione

-   `onConnect()`: Wirtualna metoda wywoÄąâ€šywana po nawiÄ…zaniu poÄąâ€šÄ…czenia. DomyÄąâ€şlnie wywoÄąâ€šuje `onConnect` w Lua.
-   `onRecv(...)`: Wirtualna metoda wywoÄąâ€šywana po otrzymaniu i zdeserializowaniu peÄąâ€šnego pakietu. DomyÄąâ€şlnie wywoÄąâ€šuje `onRecv` w Lua.
-   `onError(...)`: Wirtualna metoda wywoÄąâ€šywana w przypadku bÄąâ€šÄ™du sieciowego.
## Zmienne

-   `m_xteaKey`: Klucz XTEA.
-   `m_packetNumber`: Licznik dla pakietĂłw sekwencyjnych.
-   `m_player`, `m_recorder`: WskaÄąĹźniki na obiekty do odtwarzania/nagrywania.
-   `m_checksumEnabled`, `m_xteaEncryptionEnabled`, ...: Flagi konfiguracji protokoÄąâ€šu.
-   `m_connection`: WskaÄąĹźnik na obiekt `Connection`.
-   `m_inputMessage`: Bufor na przychodzÄ…ce dane.
-   `m_zstream`: StrumieÄąâ€ž ZLIB do dekompresji.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/declarations.h`, `inputmessage.h`, `outputmessage.h`, `connection.h`: Podstawowe klasy sieciowe.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/proxy/proxy.h`: Do integracji z systemem proxy.
-   Oznaczona jako `@bindclass`, jest kluczowym elementem do implementacji logiki sieciowej w Lua.

---
# Ä‘Ĺşâ€śâ€ž packet_recorder.cpp
## Opis ogĂłlny

Plik `packet_recorder.cpp` zawiera implementacjÄ™ klasy `PacketRecorder`, ktĂłra sÄąâ€šuÄąÄ˝y do nagrywania sesji sieciowej do pliku tekstowego.
## Klasa `PacketRecorder`
## `PacketRecorder::PacketRecorder(const std::string& file)`

Konstruktor.
-   **DziaÄąâ€šanie**:
    1.  Zapisuje czas startu nagrywania (`m_start`).
    2.  Tworzy katalog `records/`, jeÄąâ€şli nie istnieje.
    3.  Otwiera plik o podanej nazwie w tym katalogu do zapisu.
## `void PacketRecorder::addInputPacket(const InputMessagePtr& packet)`

Nagrywa pakiet przychodzÄ…cy.
-   **DziaÄąâ€šanie**:
    1.  Zapisuje do pliku znacznik `<`.
    2.  Zapisuje rĂłÄąÄ˝nicÄ™ czasu od startu nagrywania.
    3.  Zapisuje zawartoÄąâ€şÄ‡ ciaÄąâ€ša pakietu w formacie heksadecymalnym.
    4.  Dodaje znak nowej linii.
## `void PacketRecorder::addOutputPacket(const OutputMessagePtr& packet)`

Nagrywa pakiet wychodzÄ…cy.
-   **DziaÄąâ€šanie**:
    1.  Ignoruje pierwszy pakiet wychodzÄ…cy (ktĂłry zazwyczaj zawiera login i hasÄąâ€šo), aby nie zapisywaÄ‡ wraÄąÄ˝liwych danych.
    2.  Zapisuje do pliku znacznik `>`.
    3.  Zapisuje rĂłÄąÄ˝nicÄ™ czasu.
    4.  Zapisuje caÄąâ€šÄ… zawartoÄąâ€şÄ‡ pakietu (wraz z nagÄąâ€šĂłwkiem) w formacie heksadecymalnym.
    5.  Dodaje znak nowej linii.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/packet_recorder.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/core/clock.h`, `resourcemanager.h`: Do zarzÄ…dzania czasem i plikami.
-   `boost/algorithm/hex.hpp`: Do konwersji danych binarnych na format heksadecymalny.
-   Jest uÄąÄ˝ywana przez `Protocol`, gdy wÄąâ€šÄ…czony jest tryb nagrywania.

---
# Ä‘Ĺşâ€śâ€ž protocol.cpp
## Opis ogĂłlny

Plik `protocol.cpp` zawiera implementacjÄ™ klasy `Protocol`, ktĂłra stanowi bazÄ™ dla protokoÄąâ€šĂłw komunikacyjnych. Implementuje ona logikÄ™ niskiego poziomu, takÄ… jak szyfrowanie, sumy kontrolne i kompresjÄ™, delegujÄ…c obsÄąâ€šugÄ™ samych pakietĂłw do skryptĂłw Lua.
## Klasa `Protocol`
## `Protocol::Protocol()`

Konstruktor. Inicjalizuje domyÄąâ€şlne flagi protokoÄąâ€šu na `false` i przygotowuje strumieÄąâ€ž ZLIB do dekompresji.
## `void Protocol::connect(const std::string& host, uint16 port)`

Rozpoczyna poÄąâ€šÄ…czenie. JeÄąâ€şli `host` to "proxy" lub inny specjalny adres, uÄąÄ˝ywa `g_proxy`. W przeciwnym razie tworzy nowy `Connection`.
## `void Protocol::disconnect()`

Zamyka poÄąâ€šÄ…czenie, zwalniajÄ…c `Connection` lub sesjÄ™ proxy.
## `void Protocol::send(const OutputMessagePtr& outputMessage, bool rawPacket)`
## Opis semantyczny
Przygotowuje i wysyÄąâ€ša pakiet.
## DziaÄąâ€šanie
1.  JeÄąâ€şli wÄąâ€šÄ…czone jest nagrywanie, zapisuje pakiet.
2.  JeÄąâ€şli `rawPacket` jest `false`:
    -   Szyfruje pakiet za pomocÄ… XTEA, jeÄąâ€şli wÄąâ€šÄ…czone.
    -   Dodaje sumÄ™ kontrolnÄ… lub numer sekwencyjny.
    -   Dodaje rozmiar pakietu na poczÄ…tku.
3.  WysyÄąâ€ša gotowy pakiet przez `Connection` lub `Proxy`.
4.  Resetuje `outputMessage`, aby mĂłgÄąâ€š byÄ‡ ponownie uÄąÄ˝yty.
## `void Protocol::recv()`

Rozpoczyna proces odbierania nowego pakietu, instruujÄ…c `Connection`, aby najpierw odczytaÄąâ€š nagÄąâ€šĂłwek o odpowiedniej dÄąâ€šugoÄąâ€şci.
## `void Protocol::internalRecvHeader(...)` i `internalRecvData(...)`

Handlery wywoÄąâ€šywane przez `Connection`. `internalRecvHeader` odczytuje rozmiar ciaÄąâ€ša pakietu, a `internalRecvData` odczytuje resztÄ™ danych. `internalRecvData` nastÄ™pnie wykonuje deszyfrowanie, weryfikacjÄ™ sumy kontrolnej i dekompresjÄ™, a na koÄąâ€žcu wywoÄąâ€šuje `onRecv` z gotowym `InputMessage`.
## `void Protocol::generateXteaKey()` i `setXteaKey(...)`

Metody do zarzÄ…dzania kluczem szyfrowania XTEA.
## `bool Protocol::xteaDecrypt(...)` i `void Protocol::xteaEncrypt(...)`

Implementacje algorytmu XTEA do szyfrowania i deszyfrowania buforĂłw wiadomoÄąâ€şci.
## `void Protocol::onConnect()`, `onRecv(...)`, `onError(...)`

Metody wirtualne, ktĂłre domyÄąâ€şlnie wywoÄąâ€šujÄ… odpowiednie funkcje w Lua (`onConnect`, `onRecv`, `onError`), przekazujÄ…c im kontrolÄ™ nad logikÄ… protokoÄąâ€šu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/protocol.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/net/connection.h`, `packet_player.h`, `packet_recorder.h`: Komponenty sieciowe.
-   `framework/proxy/proxy.h`: Do integracji z proxy.
-   **ZLIB**: Do kompresji/dekompresji.
-   Jest to kluczowa klasa, ktĂłra jest dziedziczona (w Lua) w celu zaimplementowania konkretnego protokoÄąâ€šu gry.

---
# Ä‘Ĺşâ€śâ€ž server.cpp
## Opis ogĂłlny

Plik `server.cpp` zawiera implementacjÄ™ klasy `Server`, ktĂłra umoÄąÄ˝liwia tworzenie prostych serwerĂłw TCP nasÄąâ€šuchujÄ…cych na przychodzÄ…ce poÄąâ€šÄ…czenia.
## Zmienne globalne
## `g_ioService`

Globalny `io_service` z Boost.Asio, uÄąÄ˝ywany rĂłwnieÄąÄ˝ przez `Connection`, na ktĂłrym dziaÄąâ€ša akceptor serwera.
## Klasa `Server`
## `Server::Server(int port)`

Konstruktor. Tworzy i otwiera obiekt `boost::asio::ip::tcp::acceptor`, bindowanie go do wszystkich interfejsĂłw (`tcp::v4()`) na podanym porcie.
## `ServerPtr Server::create(int port)`

Statyczna metoda fabryczna. Tworzy obiekt `Server`, opakowujÄ…c go w `shared_ptr`. ObsÄąâ€šuguje wyjÄ…tki, ktĂłre mogÄ… wystÄ…piÄ‡, jeÄąâ€şli port jest juÄąÄ˝ zajÄ™ty.
## `void Server::close()`

Zamyka serwer. Anuluje wszystkie oczekujÄ…ce operacje akceptowania i zamyka akceptor.
## `void Server::acceptNext()`
## Opis semantyczny
Rozpoczyna asynchroniczne oczekiwanie na nowe poÄąâ€šÄ…czenie.
## DziaÄąâ€šanie
1.  Tworzy nowy, pusty obiekt `Connection`.
2.  WywoÄąâ€šuje `m_acceptor.async_accept`, przekazujÄ…c jej gniazdo nowego `Connection` oraz `callback` (lambdÄ™).
3.  Gdy nowe poÄąâ€šÄ…czenie zostanie nawiÄ…zane, `callback` jest wywoÄąâ€šywany.
4.  `Callback` ustawia stan `Connection` na `connected` i wywoÄąâ€šuje funkcjÄ™ `onAccept` w skrypcie Lua, przekazujÄ…c jej nowy obiekt `Connection` oraz ewentualny kod bÄąâ€šÄ™du.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/server.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/net/connection.h`: Tworzy obiekty `Connection` dla nowych poÄąâ€šÄ…czeÄąâ€ž.
-   `boost/asio`: UÄąÄ˝ywa `tcp::acceptor`.
-   Jest przeznaczona do uÄąÄ˝ytku w Lua, co pozwala na tworzenie np. prostych serwerĂłw pomocniczych, serwerĂłw proxy lub narzÄ™dzi deweloperskich.

---
# Ä‘Ĺşâ€śâ€ž inputmessage.cpp
## Opis ogĂłlny

Plik `inputmessage.cpp` zawiera implementacjÄ™ klasy `InputMessage`, ktĂłra jest narzÄ™dziem do parsowania przychodzÄ…cych pakietĂłw sieciowych.
## Klasa `InputMessage`
## `InputMessage::InputMessage()`

Konstruktor, wywoÄąâ€šuje `reset()`.
## `void InputMessage::reset()`

Resetuje stan wiadomoÄąâ€şci do wartoÄąâ€şci poczÄ…tkowych, ustawiajÄ…c pozycjÄ™ odczytu i nagÄąâ€šĂłwka na `MAX_HEADER_SIZE`.
## `void InputMessage::setBuffer(const std::string& buffer)`

Ustawia zawartoÄąâ€şÄ‡ ciaÄąâ€ša wiadomoÄąâ€şci, kopiujÄ…c dane z `std::string` do wewnÄ™trznego bufora.
## Metody `get...()`

OdczytujÄ… dane z bufora, zaczynajÄ…c od bieÄąÄ˝Ä…cej pozycji `m_readPos`.
-   KaÄąÄ˝da metoda najpierw wywoÄąâ€šuje `checkRead`, aby upewniÄ‡ siÄ™, ÄąÄ˝e jest wystarczajÄ…co duÄąÄ˝o danych do odczytania.
-   NastÄ™pnie odczytuje dane z bufora, konwertujÄ…c je z porzÄ…dku Little Endian, jeÄąâ€şli to konieczne.
-   Na koniec przesuwa wskaÄąĹźnik `m_readPos`.
-   `getString` najpierw odczytuje 2-bajtowÄ… dÄąâ€šugoÄąâ€şÄ‡, a potem sam string.
-   `getDouble` odczytuje niestandardowy format liczby zmiennoprzecinkowej.
## `bool InputMessage::decryptRsa(int size)`

Deszyfruje `size` bajtĂłw z bieÄąÄ˝Ä…cej pozycji za pomocÄ… klucza prywatnego RSA. Zwraca `true`, jeÄąâ€şli pierwszy zdeszyfrowany bajt to 0.
## `void InputMessage::fillBuffer(...)`

Dopisuje surowe dane do bufora w bieÄąÄ˝Ä…cej pozycji odczytu (uÄąÄ˝ywane przez `Protocol` podczas odbierania danych z gniazda).
## `void InputMessage::setHeaderSize(uint32 size)`

Ustawia pozycjÄ™ poczÄ…tku nagÄąâ€šĂłwka (`m_headerPos`), co efektywnie okreÄąâ€şla jego rozmiar.
## `bool InputMessage::readChecksum()`

Odczytuje 4-bajtowÄ… sumÄ™ kontrolnÄ… z bufora, oblicza sumÄ™ kontrolnÄ… Adler-32 dla reszty danych i porĂłwnuje je.
## `void InputMessage::checkRead(int bytes)`

Prywatna metoda, ktĂłra rzuca wyjÄ…tek, jeÄąâ€şli prĂłba odczytu `bytes` bajtĂłw wykroczyÄąâ€šaby poza granice wiadomoÄąâ€şci.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/inputmessage.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/util/crypt.h`: Do deszyfracji RSA.
-   `client/map.h`: Potencjalna zaleÄąÄ˝noÄąâ€şÄ‡, byÄ‡ moÄąÄ˝e z starszej wersji.
-   Jest uÄąÄ˝ywana przez `Protocol` do reprezentowania i parsowania przychodzÄ…cych pakietĂłw.

---
# Ä‘Ĺşâ€śâ€ž packet_recorder.h
## Opis ogĂłlny

Plik `packet_recorder.h` deklaruje klasÄ™ `PacketRecorder`, ktĂłra sÄąâ€šuÄąÄ˝y do nagrywania sesji sieciowej do pliku tekstowego w celu pĂłÄąĹźniejszej analizy lub odtworzenia.
## Klasa `PacketRecorder`
## Opis semantyczny
`PacketRecorder` przechwytuje pakiety przychodzÄ…ce (`InputMessage`) i wychodzÄ…ce (`OutputMessage`) i zapisuje je w czytelnym formacie do pliku. KaÄąÄ˝dy wpis zawiera znacznik kierunku (`<` lub `>`), sygnaturÄ™ czasowÄ… i zawartoÄąâ€şÄ‡ pakietu w postaci heksadecymalnej. Dziedziczy po `LuaObject`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PacketRecorder(const std::string& file)` | Konstruktor, otwiera plik do zapisu. |
| `virtual ~PacketRecorder()` | Destruktor. |
| `void addInputPacket(...)` | Zapisuje pakiet przychodzÄ…cy do pliku. |
| `void addOutputPacket(...)` | Zapisuje pakiet wychodzÄ…cy do pliku. |
## Zmienne prywatne

-   `m_start`: Czas rozpoczÄ™cia nagrywania.
-   `m_stream`: StrumieÄąâ€ž pliku do zapisu.
-   `m_firstOutput`: Flaga uÄąÄ˝ywana do pominiÄ™cia pierwszego pakietu wychodzÄ…cego (zwykle zawierajÄ…cego hasÄąâ€šo).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/net/inputmessage.h`, `outputmessage.h`: Przyjmuje obiekty tych typĂłw do nagrania.
-   Jest tworzona i uÄąÄ˝ywana przez `Protocol`, gdy wÄąâ€šÄ…czony jest tryb nagrywania.

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## Opis ogĂłlny

Plik `declarations.h` w module `otml` sÄąâ€šuÄąÄ˝y do wczesnych deklaracji (forward declarations) i definicji typĂłw dla klas zwiÄ…zanych z parserem OTML.
## Wczesne deklaracje

-   `OTMLNode`
-   `OTMLDocument`
-   `OTMLParser`
-   `OTMLEmitter`
## Definicje typĂłw

-   `OTMLNodePtr`: `stdext::shared_object_ptr<OTMLNode>`
-   `OTMLDocumentPtr`: `stdext::shared_object_ptr<OTMLDocument>`
-   `OTMLNodeList`: `std::vector<OTMLNodePtr>`
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doÄąâ€šÄ…czany przez wszystkie pliki nagÄąâ€šĂłwkowe w module `otml`.

---
# Ä‘Ĺşâ€śâ€ž otmlparser.h
## Opis ogĂłlny

Plik `otmlparser.h` deklaruje klasÄ™ `OTMLParser`, ktĂłra jest odpowiedzialna za parsowanie dokumentĂłw w formacie OTML (OTClient Markup Language).
## Klasa `OTMLParser`
## Opis semantyczny
`OTMLParser` odczytuje dane linia po linii ze strumienia wejÄąâ€şciowego, analizuje wciÄ™cia (ktĂłre definiujÄ… hierarchiÄ™), a nastÄ™pnie parsuje tagi i wartoÄąâ€şci, budujÄ…c drzewo obiektĂłw `OTMLNode`.
## Metody publiczne

-   `OTMLParser(OTMLDocumentPtr doc, std::istream& in)`: Konstruktor.
-   `void parse()`: GÄąâ€šĂłwna metoda rozpoczynajÄ…ca proces parsowania.
## Metody prywatne

-   `std::string getNextLine()`: Odczytuje nastÄ™pnÄ… liniÄ™ ze strumienia.
-   `int getLineDepth(...)`: Oblicza poziom zagnieÄąÄ˝dÄąÄ˝enia na podstawie liczby spacji na poczÄ…tku linii.
-   `void parseLine(...)`: Przetwarza pojedynczÄ… liniÄ™ (sprawdza wciÄ™cia, komentarze, puste linie).
-   `void parseNode(...)`: Parsuje tag i wartoÄąâ€şÄ‡ z linii i tworzy nowy `OTMLNode`.
## Zmienne prywatne

-   `currentDepth`, `currentLine`: ÄąĹˇledzÄ… pozycjÄ™ w pliku.
-   `doc`: WskaÄąĹźnik na dokument, ktĂłry jest budowany.
-   `currentParent`: WskaÄąĹźnik na bieÄąÄ˝Ä…cy wÄ™zeÄąâ€š-rodzica.
-   `parentMap`: Mapa do Äąâ€şledzenia hierarchii.
-   `previousNode`: WskaÄąĹźnik na ostatnio dodany wÄ™zeÄąâ€š.
-   `in`: Referencja do strumienia wejÄąâ€şciowego.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/declarations.h`: Definicje typĂłw.
-   Jest uÄąÄ˝ywana przez `OTMLDocument::parse`.

---
# Ä‘Ĺşâ€śâ€ž otml.h
## Opis ogĂłlny

Plik `otml.h` jest gÄąâ€šĂłwnym plikiem nagÄąâ€šĂłwkowym dla moduÄąâ€šu OTML. Jego jedynym zadaniem jest doÄąâ€šÄ…czenie dwĂłch najwaÄąÄ˝niejszych plikĂłw tego moduÄąâ€šu: `otmldocument.h` i `otmlnode.h`.
## ZawartoÄąâ€şÄ‡

`$fenceInfo
# include "otmldocument.h"
# include "otmlnode.h"
```
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   UÄąâ€šatwia doÄąâ€šÄ…czanie podstawowych funkcjonalnoÄąâ€şci OTML w innych czÄ™Äąâ€şciach projektu, ktĂłre potrzebujÄ… zarĂłwno `OTMLDocument`, jak i `OTMLNode`.

---
# Ä‘Ĺşâ€śâ€ž otmldocument.cpp
## Opis ogĂłlny

Plik `otmldocument.cpp` zawiera implementacjÄ™ klasy `OTMLDocument`, ktĂłra reprezentuje caÄąâ€šy dokument OTML i jest korzeniem drzewa wÄ™zÄąâ€šĂłw.
## Klasa `OTMLDocument`
## `OTMLDocumentPtr OTMLDocument::create()`

Statyczna metoda fabryczna. Tworzy nowy, pusty dokument z domyÄąâ€şlnym tagiem "doc".
## `OTMLDocumentPtr OTMLDocument::parse(const std::string& fileName)`

Statyczna metoda, ktĂłra Äąâ€šaduje i parsuje dokument OTML z pliku. UÄąÄ˝ywa `g_resources` do odczytania pliku do strumienia, a nastÄ™pnie wywoÄąâ€šuje `parse(std::istream&, ...)`.
## `OTMLDocumentPtr OTMLDocument::parseString(const std::string& data, const std::string& source)`

Parsuje dokument z `std::string`.
## `OTMLDocumentPtr OTMLDocument::parse(std::istream& in, const std::::string& source)`

GÄąâ€šĂłwna metoda parsujÄ…ca.
1.  Tworzy nowy `OTMLDocument`.
2.  Tworzy `OTMLParser` dla tego dokumentu i strumienia.
3.  WywoÄąâ€šuje `parser.parse()` w celu zbudowania drzewa wÄ™zÄąâ€šĂłw.
4.  Zwraca gotowy dokument.
## `std::string OTMLDocument::emit()`

Konwertuje caÄąâ€še drzewo wÄ™zÄąâ€šĂłw OTML z powrotem na format tekstowy, uÄąÄ˝ywajÄ…c `OTMLEmitter`.
## `bool OTMLDocument::save(const std::string& fileName)`

Zapisuje wyemitowany dokument do pliku za pomocÄ… `g_resources`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/otmldocument.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/otml/otmlparser.h`, `otmlemitter.h`: UÄąÄ˝ywa parsera i emittera.
-   `framework/core/resourcemanager.h`: Do operacji na plikach.

---
# Ä‘Ĺşâ€śâ€ž otmldocument.h
## Opis ogĂłlny

Plik `otmldocument.h` deklaruje klasÄ™ `OTMLDocument`, ktĂłra jest specjalizacjÄ… `OTMLNode` i reprezentuje korzeÄąâ€ž dokumentu OTML.
## Klasa `OTMLDocument`
## Opis semantyczny
`OTMLDocument` dziedziczy po `OTMLNode`, wiÄ™c jest jednoczeÄąâ€şnie wÄ™zÄąâ€šem (korzeniem) i caÄąâ€šym dokumentem. Dodaje funkcjonalnoÄąâ€şÄ‡ zwiÄ…zanÄ… z plikami: parsowanie z pliku/stringu i zapisywanie do pliku. Przechowuje rĂłwnieÄąÄ˝ informacjÄ™ o ÄąĹźrĂłdle (`source`), z ktĂłrego zostaÄąâ€š zaÄąâ€šadowany.
## Metody publiczne (statyczne)

| Metoda | Opis |
| :--- | :--- |
| `static OTMLDocumentPtr create()` | Tworzy pusty dokument. |
| `static OTMLDocumentPtr parse(...)` | Parsuje dokument z pliku, stringu lub strumienia. |
## Metody publiczne (instancji)

| Metoda | Opis |
| :--- | :--- |
| `std::string emit()` | Konwertuje dokument na string w formacie OTML. |
| `bool save(const std::string& fileName)` | Zapisuje dokument do pliku. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/otmlnode.h`: Klasa bazowa.
-   Jest uÄąÄ˝ywana jako punkt wejÄąâ€şcia do tworzenia i Äąâ€šadowania struktur OTML w caÄąâ€šej aplikacji (np. w `UIManager`, `ConfigManager`).

---
# Ä‘Ĺşâ€śâ€ž otmlemitter.cpp
## Opis ogĂłlny

Plik `otmlemitter.cpp` zawiera implementacjÄ™ klasy `OTMLEmitter`, ktĂłra jest odpowiedzialna za konwersjÄ™ drzewa `OTMLNode` z powrotem do formatu tekstowego OTML.
## Klasa `OTMLEmitter`
## `std::string OTMLEmitter::emitNode(const OTMLNodePtr& node, int currentDepth)`
## Opis semantyczny
Rekurencyjna, statyczna metoda, ktĂłra generuje tekstowÄ… reprezentacjÄ™ pojedynczego wÄ™zÄąâ€ša i wszystkich jego dzieci.
## DziaÄąâ€šanie
1.  Dodaje wciÄ™cie (2 spacje na poziom) odpowiednie dla `currentDepth`.
2.  Zapisuje tag wÄ™zÄąâ€ša. JeÄąâ€şli wÄ™zeÄąâ€š ma wartoÄąâ€şÄ‡ lub jest unikalny, dodaje `:`. JeÄąâ€şli nie ma tagu, zapisuje `-`.
3.  Zapisuje wartoÄąâ€şÄ‡ wÄ™zÄąâ€ša:
    -   JeÄąâ€şli wartoÄąâ€şÄ‡ to `null` (`m_null`), zapisuje `~`.
    -   JeÄąâ€şli wartoÄąâ€şÄ‡ zawiera znaki nowej linii, formatuje jÄ… jako blok wieloliniowy, uÄąÄ˝ywajÄ…c `|`, `|-` lub `|+` w zaleÄąÄ˝noÄąâ€şci od tego, jak majÄ… byÄ‡ traktowane koÄąâ€žcowe znaki nowej linii.
    -   W przeciwnym razie, zapisuje wartoÄąâ€şÄ‡ w tej samej linii.
4.  Rekurencyjnie wywoÄąâ€šuje `emitNode` dla wszystkich dzieci, zwiÄ™kszajÄ…c `currentDepth`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/otmlemitter.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/otml/otmldocument.h`: UÄąÄ˝ywana przez `OTMLDocument::emit()`.

---
# Ä‘Ĺşâ€śâ€ž otmlexception.cpp
## Opis ogĂłlny

Plik `otmlexception.cpp` zawiera implementacjÄ™ klasy `OTMLException`, ktĂłra jest uÄąÄ˝ywana do sygnalizowania bÄąâ€šÄ™dĂłw podczas parsowania lub przetwarzania dokumentĂłw OTML.
## Klasa `OTMLException`
## Konstruktory

-   **`OTMLException(const OTMLNodePtr& node, const std::string& error)`**: Tworzy wyjÄ…tek zwiÄ…zany z konkretnym wÄ™zÄąâ€šem. Komunikat bÄąâ€šÄ™du bÄ™dzie zawieraÄąâ€š informacjÄ™ o ÄąĹźrĂłdle (`source`) tego wÄ™zÄąâ€ša.
-   **`OTMLException(const OTMLDocumentPtr& doc, const std::string& error, int line)`**: Tworzy wyjÄ…tek zwiÄ…zany z caÄąâ€šym dokumentem, opcjonalnie podajÄ…c numer linii, w ktĂłrej wystÄ…piÄąâ€š bÄąâ€šÄ…d parsowania.
## DziaÄąâ€šanie
Oba konstruktory budujÄ… szczegĂłÄąâ€šowy komunikat bÄąâ€šÄ™du w `std::stringstream`, ktĂłry jest nastÄ™pnie zapisywany w `m_what` i dostÄ™pny przez metodÄ™ `what()`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/otmlexception.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/otml/otmldocument.h`: Do dostÄ™pu do ÄąĹźrĂłdÄąâ€ša dokumentu.
-   Jest rzucana przez `OTMLParser` w przypadku bÄąâ€šÄ™dĂłw skÄąâ€šadniowych i przez `OTMLNode` w przypadku bÄąâ€šÄ™dĂłw logicznych (np. brak wymaganego dziecka).

---
# Ä‘Ĺşâ€śâ€ž otmlexception.h
## Opis ogĂłlny

Plik `otmlexception.h` deklaruje klasÄ™ `OTMLException`, ktĂłra jest typem wyjÄ…tku uÄąÄ˝ywanym do sygnalizowania bÄąâ€šÄ™dĂłw zwiÄ…zanych z OTML.
## Klasa `OTMLException`
## Opis semantyczny
Dziedziczy po `stdext::exception`. Jest tworzona z informacjÄ… o kontekÄąâ€şcie bÄąâ€šÄ™du (wÄ™zeÄąâ€š lub dokument oraz numer linii), co pozwala na generowanie precyzyjnych komunikatĂłw o bÄąâ€šÄ™dach, uÄąâ€šatwiajÄ…cych debugowanie plikĂłw OTML.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OTMLException(...)` | Konstruktory. |
| `virtual ~OTMLException()` | Destruktor. |
| `virtual const char* what() const throw()` | Zwraca sformatowany komunikat bÄąâ€šÄ™du. |
## Zmienne chronione

-   `m_what`: `std::string` przechowujÄ…ca komunikat bÄąâ€šÄ™du.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/declarations.h`: Podstawowe deklaracje.
-   `framework/stdext/exception.h`: Klasa bazowa.
-   Jest rzucana przez `OTMLParser` i `OTMLNode`.

---
# Ä‘Ĺşâ€śâ€ž otmlemitter.h
## Opis ogĂłlny

Plik `otmlemitter.h` deklaruje klasÄ™ `OTMLEmitter`, ktĂłra jest odpowiedzialna za proces "emitowania", czyli konwersji drzewa wÄ™zÄąâ€šĂłw OTML z powrotem do jego tekstowej reprezentacji.
## Klasa `OTMLEmitter`
## Opis semantyczny
`OTMLEmitter` zawiera jednÄ… statycznÄ… metodÄ™, ktĂłra rekurencyjnie przechodzi przez drzewo `OTMLNode` i buduje sformatowany `std::string` zgodny ze skÄąâ€šadniÄ… OTML, uwzglÄ™dniajÄ…c wciÄ™cia, tagi, wartoÄąâ€şci (w tym wieloliniowe) i hierarchiÄ™.
## Metody publiczne (statyczne)

| Metoda | Opis |
| :--- | :--- |
| `static std::string emitNode(...)` | Generuje tekstowÄ… reprezentacjÄ™ podanego wÄ™zÄąâ€ša i wszystkich jego dzieci. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/declarations.h`: Podstawowe deklaracje.
-   Jest uÄąÄ˝ywana przez `OTMLDocument::emit()` i `OTMLNode::emit()`.

---
# Ä‘Ĺşâ€śâ€ž otmlparser.cpp
## Opis ogĂłlny

Plik `otmlparser.cpp` zawiera implementacjÄ™ klasy `OTMLParser`, ktĂłra jest sercem mechanizmu parsowania jÄ™zyka OTML.
## Klasa `OTMLParser`
## `OTMLParser::OTMLParser(...)`

Konstruktor. Inicjalizuje stan parsera, ustawiajÄ…c bieÄąÄ˝Ä…cy wÄ™zeÄąâ€š-rodzica na korzeÄąâ€ž dokumentu.
## `void OTMLParser::parse()`

GÄąâ€šĂłwna metoda, ktĂłra w pÄ™tli odczytuje kolejne linie ze strumienia (`getNextLine()`) i przekazuje je do `parseLine()`, aÄąÄ˝ do koÄąâ€žca pliku.
## `int OTMLParser::getLineDepth(...)`

Oblicza poziom wciÄ™cia linii, liczÄ…c spacje na jej poczÄ…tku. Wymusza, aby wciÄ™cie byÄąâ€šo wielokrotnoÄąâ€şciÄ… dwĂłch spacji i zabrania uÄąÄ˝ywania tabulatorĂłw.
## `void OTMLParser::parseLine(std::string line)`

Przetwarza pojedynczÄ… liniÄ™.
1.  Oblicza jej gÄąâ€šÄ™bokoÄąâ€şÄ‡.
2.  Usuwa biaÄąâ€še znaki z poczÄ…tku i koÄąâ€žca.
3.  Ignoruje puste linie i komentarze (`//`).
4.  Na podstawie rĂłÄąÄ˝nicy miÄ™dzy bieÄąÄ˝Ä…cÄ… gÄąâ€šÄ™bokoÄąâ€şciÄ… a gÄąâ€šÄ™bokoÄąâ€şciÄ… linii, aktualizuje `currentParent`, wchodzÄ…c w gÄąâ€šÄ…b hierarchii lub wracajÄ…c na wyÄąÄ˝szy poziom.
5.  WywoÄąâ€šuje `parseNode` w celu sparsowania wÄąâ€šaÄąâ€şciwej zawartoÄąâ€şci linii.
## `void OTMLParser::parseNode(const std::string& data)`

Parsuje tag i wartoÄąâ€şÄ‡ z podanego ciÄ…gu znakĂłw.
1.  Dzieli ciÄ…g na tag i wartoÄąâ€şÄ‡ na podstawie separatora `:`.
2.  ObsÄąâ€šuguje specjalny przypadek `-` dla wÄ™zÄąâ€šĂłw bez tagu.
3.  ObsÄąâ€šuguje wartoÄąâ€şci wieloliniowe (rozpoczynajÄ…ce siÄ™ od `|`, `|-`, `|+`), odczytujÄ…c kolejne linie, dopĂłki wciÄ™cie siÄ™ zgadza.
4.  ObsÄąâ€šuguje listy w nawiasach kwadratowych (`[...]`), dzielÄ…c je na osobne wartoÄąâ€şci.
5.  Tworzy nowy obiekt `OTMLNode`, ustawia jego wÄąâ€šaÄąâ€şciwoÄąâ€şci (tag, wartoÄąâ€şÄ‡, ÄąĹźrĂłdÄąâ€šo) i dodaje go do `currentParent`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/otmlparser.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/otml/otmldocument.h`, `otmlexception.h`: Do tworzenia i obsÄąâ€šugi bÄąâ€šÄ™dĂłw.
-   `boost/tokenizer.hpp`: Do parsowania list w nawiasach kwadratowych.

---
# Ä‘Ĺşâ€śâ€ž otmlnode.h
## Opis ogĂłlny

Plik `otmlnode.h` deklaruje klasÄ™ `OTMLNode`, ktĂłra jest podstawowym budulcem drzewa dokumentu OTML. Reprezentuje pojedynczy wÄ™zeÄąâ€š, ktĂłry moÄąÄ˝e mieÄ‡ tag, wartoÄąâ€şÄ‡ i listÄ™ dzieci.
## Klasa `OTMLNode`
## Opis semantyczny
`OTMLNode` to uniwersalny kontener na dane w strukturze drzewiastej. Jest uÄąÄ˝ywany do reprezentowania zarĂłwno stylĂłw UI, jak i samych widgetĂłw w plikach `.otui`, a takÄąÄ˝e moduÄąâ€šĂłw w `.otmod` i konfiguracji w plikach `.otml`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `static OTMLNodePtr create(...)` | Metody fabryczne do tworzenia nowych wÄ™zÄąâ€šĂłw. |
| `tag()`, `size()`, `source()`, `rawValue()` | Gettery dla podstawowych wÄąâ€šaÄąâ€şciwoÄąâ€şci. |
| `isUnique()`, `isNull()`, `hasTag()`, `hasValue()`, `hasChildren()` | Metody sprawdzajÄ…ce stan wÄ™zÄąâ€ša. |
| `setTag(...)`, `setValue(...)`, ... | Settery dla wÄąâ€šaÄąâ€şciwoÄąâ€şci. |
| `get(const std::string& childTag)` | Zwraca pierwszy wÄ™zeÄąâ€š-dziecko o danym tagu. |
| `at(const std::string& childTag)` | To samo co `get`, ale rzuca wyjÄ…tek, jeÄąâ€şli dziecko nie istnieje. |
| `addChild(...)`, `removeChild(...)` | Dodaje/usuwa dziecko. `addChild` obsÄąâ€šuguje logikÄ™ Äąâ€šÄ…czenia (merge) dla unikalnych wÄ™zÄąâ€šĂłw. |
| `copy(...)`, `merge(...)`, `clear()`, `clone()` | Metody do manipulacji strukturÄ… wÄ™zÄąâ€ša. |
| `children()` | Zwraca listÄ™ wszystkich dzieci. |
| **Szablonowe metody `value...`** | |
| `value<T>()` | Zwraca wartoÄąâ€şÄ‡ wÄ™zÄąâ€ša, rzutowanÄ… na typ `T`. |
| `valueAt<T>(...)` | Zwraca wartoÄąâ€şÄ‡ dziecka o danym tagu. |
| `valueAtIndex<T>(...)` | Zwraca wartoÄąâ€şÄ‡ dziecka o danym indeksie. |
| **Szablonowe metody `write...`** | |
| `write<T>(...)` | Ustawia wartoÄąâ€şÄ‡ wÄ™zÄąâ€ša. |
| `writeAt<T>(...)` | Tworzy i dodaje unikalne dziecko z danÄ… wartoÄąâ€şciÄ…. |
| `writeIn<T>(...)` | Tworzy i dodaje nie-unikalne dziecko z danÄ… wartoÄąâ€şciÄ…. |
| `emit()` | Konwertuje wÄ™zeÄąâ€š i jego dzieci na string. |
## Zmienne chronione

-   `m_children`: Mapa przechowujÄ…ca dzieci pogrupowane wedÄąâ€šug tagĂłw.
-   `m_tag`, `m_value`, `m_source`: Podstawowe wÄąâ€šaÄąâ€şciwoÄąâ€şci.
-   `m_unique`, `m_null`: Flagi stanu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/declarations.h`: Definicje typĂłw.
-   `framework/otml/otmlexception.h`: Do rzucania wyjÄ…tkĂłw.
-   Jest to podstawowa klasa moduÄąâ€šu OTML, uÄąÄ˝ywana przez `OTMLParser`, `OTMLEmitter` i `OTMLDocument`.

---
# Ä‘Ĺşâ€śâ€ž otmlnode.cpp
## Opis ogĂłlny

Plik `otmlnode.cpp` zawiera implementacjÄ™ metod klasy `OTMLNode`.
## Klasa `OTMLNode`
## `OTMLNodePtr OTMLNode::create(...)`

Metody fabryczne, ktĂłre tworzÄ… nowy `OTMLNode` i ustawiajÄ… jego poczÄ…tkowe wÄąâ€šaÄąâ€şciwoÄąâ€şci.
## `bool OTMLNode::hasChildren()`

Sprawdza, czy wÄ™zeÄąâ€š ma jakiekolwiek dzieci, ktĂłre nie sÄ… `null`.
## `OTMLNodePtr OTMLNode::get(const std::string& childTag)`

Wyszukuje w mapie `m_children` pierwsze dziecko o podanym tagu, ktĂłre nie jest `null`, i je zwraca.
## `void OTMLNode::addChild(const OTMLNodePtr& newChild)`

Dodaje nowe dziecko. Implementuje kluczowÄ… logikÄ™:
-   JeÄąâ€şli nowe dziecko ma tag i jest unikalne (`isUnique()`), a dziecko o takim samym tagu juÄąÄ˝ istnieje, to nowe dziecko jest Äąâ€šÄ…czone (`merge`) ze starym, effectively nadpisujÄ…c/dodajÄ…c wÄąâ€šaÄąâ€şciwoÄąâ€şci.
-   W przeciwnym razie, jest po prostu dodawane do listy dzieci o danym tagu.
-   KaÄąÄ˝demu dziecku nadawany jest unikalny, rosnÄ…cy indeks, aby zachowaÄ‡ kolejnoÄąâ€şÄ‡ wstawiania.
## `bool OTMLNode::removeChild(...)`

Usuwa podane dziecko z listy.
## `void OTMLNode::copy(const OTMLNodePtr& node)`

GÄąâ€šÄ™boko kopiuje wszystkie wÄąâ€šaÄąâ€şciwoÄąâ€şci i dzieci z innego wÄ™zÄąâ€ša, zastÄ™pujÄ…c wÄąâ€šasnÄ… zawartoÄąâ€şÄ‡.
## `void OTMLNode::merge(const OTMLNodePtr& node)`

ÄąÂÄ…czy zawartoÄąâ€şÄ‡ innego wÄ™zÄąâ€ša z bieÄąÄ˝Ä…cym. W przeciwieÄąâ€žstwie do `copy`, nie czyÄąâ€şci istniejÄ…cych dzieci, lecz dodaje nowe (lub Äąâ€šÄ…czy, jeÄąâ€şli sÄ… unikalne).
## `OTMLNodeList OTMLNode::children()`

Zwraca listÄ™ wszystkich nie-nullowych dzieci, posortowanÄ… wedÄąâ€šug ich indeksu wstawienia.
## `OTMLNodePtr OTMLNode::clone()`

Tworzy i zwraca gÄąâ€šÄ™bokÄ… kopiÄ™ wÄ™zÄąâ€ša i wszystkich jego dzieci.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/otml/otmlnode.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/otml/otmlemitter.h`: UÄąÄ˝ywany w metodzie `emit()`.
-   Jest to implementacja centralnej struktury danych dla systemu OTML.

---
# Ä‘Ĺşâ€śâ€ž androidplatform.cpp
## Opis ogĂłlny

Plik `androidplatform.cpp` zawiera implementacjÄ™ metod klasy `Platform` specyficznych dla systemu Android. Jest kompilowany tylko wtedy, gdy zdefiniowano makro `ANDROID`.
## Klasa `Platform` (implementacja dla Androida)

Wiele metod jest pustymi implementacjami lub zwraca domyÄąâ€şlne wartoÄąâ€şci, poniewaÄąÄ˝ ich funkcjonalnoÄąâ€şÄ‡ nie jest dostÄ™pna lub nie ma sensu na platformie Android w taki sam sposĂłb, jak na desktopie.

| Metoda | Implementacja na Androidzie |
| :--- | :--- |
| `processArgs(...)` | Pusta (argumenty sÄ… obsÄąâ€šugiwane inaczej). |
| `spawnProcess(...)`| Zwraca `false`. |
| `getProcessId()` | Zwraca `getpid()`. |
| `isProcessRunning(...)` | Zwraca `false`. |
| `killProcess(...)` | Zwraca `false`. |
| `getTempPath()` | Zwraca `/tmp/`. |
| `getCurrentDir()` | Zwraca wynik `getcwd()`. |
| `copyFile(...)`, `fileExists(...)`, `removeFile(...)` | Puste/zwracajÄ… `true`/`false`. Operacje na plikach sÄ… obsÄąâ€šugiwane przez `ResourceManager`. |
| `getFileModificationTime(...)` | Zwraca 0. |
| `openUrl(std::string url, ...)` | Deleguje zadanie do `AndroidWindow::openUrl` poprzez `g_graphicsDispatcher`, aby zapewniÄ‡ wykonanie w odpowiednim wÄ…tku. |
| `openDir(...)` | Zwraca `true`. |
| `getCPUName()` | Zwraca pusty string. |
| `getTotalSystemMemory()` | Zwraca 0. |
| `getMemoryUsage()` | Zwraca 0. |
| `getOSName()` | Zwraca `"android"`. |
| `traceback(...)` | Zwraca pusty string (brak `backtrace` w standardzie). |
| `getMacAddresses()` | Zwraca pusty wektor. |
| `getUserName()` | Zwraca `"android"`. |
| `getDlls()`, `getProcesses()`, `getWindows()` | ZwracajÄ… puste wektory. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/platform/platform.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/platform/androidwindow.h`: Do otwierania URL.
-   `framework/core/eventdispatcher.h`: Do bezpiecznego wÄ…tkowo wywoÄąâ€šywania metod z `AndroidWindow`.

---
# Ä‘Ĺşâ€śâ€ž androidwindow.cpp
## Opis ogĂłlny

Plik `androidwindow.cpp` zawiera implementacjÄ™ klasy `AndroidWindow`, ktĂłra jest specyficznÄ… dla platformy Android implementacjÄ… `PlatformWindow`. ZarzÄ…dza ona cyklem ÄąÄ˝ycia okna, obsÄąâ€šugÄ… wejÄąâ€şcia (dotyk, klawiatura) oraz kontekstem graficznym EGL/OpenGL ES.
## Zmienne globalne
## `g_androidWindow`

Globalna instancja `AndroidWindow`.
## Klasa `AndroidWindow`
## `AndroidWindow::AndroidWindow()`

Konstruktor. Inicjalizuje mapÄ™ klawiszy (`m_keyMap`), tÄąâ€šumaczÄ…c kody klawiszy Android (`AKEYCODE_*`) na wewnÄ™trzne kody `Fw::Key`.
## `void AndroidWindow::internalInitGL()` i `internalDestroyGL()`

Metody do zarzÄ…dzania kontekstem graficznym EGL.
-   `internalInitGL`: Pobiera domyÄąâ€şlny wyÄąâ€şwietlacz EGL, wybiera konfiguracjÄ™, tworzy powierzchniÄ™ renderowania (`EGLSurface`) na podstawie natywnego okna Android i tworzy kontekst OpenGL ES 2.0.
-   `internalDestroyGL`: Zwalnia powierzchniÄ™ i kontekst EGL.
## `void AndroidWindow::init(struct android_app* app)`

GÄąâ€šĂłwna metoda inicjalizujÄ…ca. Zapisuje wskaÄąĹźnik na `android_app` i ustawia `callbacki` dla zdarzeÄąâ€ž cyklu ÄąÄ˝ycia aplikacji i zdarzeÄąâ€ž wejÄąâ€şciowych.
## `void AndroidWindow::poll()`

Przetwarza zdarzenia systemowe z kolejki Androida za pomocÄ… `ALooper_pollAll`.
## `void AndroidWindow::swapBuffers()`

Zamienia bufory ekranu za pomocÄ… `eglSwapBuffers`.
## `void AndroidWindow::handleCmd(int32_t cmd)`

Handler dla zdarzeÄąâ€ž cyklu ÄąÄ˝ycia aplikacji Android (np. `APP_CMD_INIT_WINDOW`, `APP_CMD_GAINED_FOCUS`). W odpowiedzi na te zdarzenia, tworzy lub niszczy kontekst GL i aktualizuje stan widocznoÄąâ€şci.
## `int AndroidWindow::handleInput(AInputEvent* event)`

Handler dla zdarzeÄąâ€ž wejÄąâ€şciowych.
-   **`AINPUT_EVENT_TYPE_MOTION` (dotyk)**:
    -   TÄąâ€šumaczy zdarzenia dotyku (`ACTION_DOWN`, `ACTION_UP`, `ACTION_MOVE`) na zdarzenia myszy (`MousePress`, `MouseRelease`, `MouseMove`).
    -   Implementuje logikÄ™ do symulacji klikniÄ™cia lewym i prawym przyciskiem myszy oraz przeciÄ…gania na ekranie dotykowym.
    -   ObsÄąâ€šuguje wielodotyk, mapujÄ…c drugi i trzeci palec na `Fw::MouseTouch2` i `Fw::MouseTouch3`.
-   **`AINPUT_EVENT_TYPE_KEY` (klawiatura)**:
    -   TÄąâ€šumaczy kod klawisza Android na kod `Fw::Key`.
    -   WywoÄąâ€šuje `processKeyDown` lub `processKeyUp`.
## `void AndroidWindow::showTextEditor(...)`

WywoÄąâ€šuje metodÄ™ Javy (`showTextEdit`) za pomocÄ… JNI, aby wyÄąâ€şwietliÄ‡ natywnÄ… klawiaturÄ™ i pole edycji tekstu Androida.
## `void AndroidWindow::openUrl(std::string url)`

Otwiera URL za pomocÄ… intencji Androida, wywoÄąâ€šujÄ…c metodÄ™ Javy przez JNI.
## Funkcja `JNIEXPORT ... commitText(...)`

Funkcja C wywoÄąâ€šywana z kodu Javy, ktĂłra przekazuje tekst wpisany na klawiaturze Androida z powrotem do aplikacji.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   NagÄąâ€šĂłwki NDK Androida (`android_native_app_glue.h`, `jni.h`).
-   NagÄąâ€šĂłwki EGL i GLES.
-   WspĂłÄąâ€špracuje z `GraphicalApplication` poprzez `callbacki` `m_onInputEvent`, `m_onResize`, `m_onClose`.

---
# Ä‘Ĺşâ€śâ€ž androidwindow.h
## Opis ogĂłlny

Plik `androidwindow.h` deklaruje klasÄ™ `AndroidWindow`, ktĂłra jest implementacjÄ… `PlatformWindow` dla systemu Android.
## Klasa `AndroidWindow`
## Opis semantyczny
`AndroidWindow` integruje aplikacjÄ™ z natywnym cyklem ÄąÄ˝ycia i systemem zdarzeÄąâ€ž Androida za pomocÄ… struktury `android_app` z NDK. ZarzÄ…dza kontekstem graficznym EGL/GLES i tÄąâ€šumaczy natywne zdarzenia wejÄąâ€şciowe (dotyk, klawisze sprzÄ™towe) na wewnÄ™trzny format `InputEvent`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **ZarzÄ…dzanie cyklem ÄąÄ˝ycia** | |
| `init(struct android_app* app)` | Inicjalizuje okno, Äąâ€šÄ…czÄ…c je ze strukturÄ… `android_app`. |
| `handleCmd(int32_t cmd)` | ObsÄąâ€šuguje komendy cyklu ÄąÄ˝ycia aplikacji od systemu Android. |
| `handleInput(AInputEvent* event)` | Przetwarza natywne zdarzenia wejÄąâ€şciowe. |
| **Interfejs `PlatformWindow`** | |
| `poll()` | Przetwarza zdarzenia z kolejki systemowej. |
| `swapBuffers()` | Zamienia bufory EGL. |
| `getDisplaySize()` | Zwraca rozmiar okna. |
| `showTextEditor(...)` | WyÄąâ€şwietla natywnÄ… klawiaturÄ™ Androida. |
| `openUrl(...)` | Otwiera URL. |
| ... | Implementacje innych metod `PlatformWindow`, czÄ™sto puste, poniewaÄąÄ˝ pojÄ™cia takie jak "minimalizacja" czy "zmiana tytuÄąâ€šu okna" nie majÄ… bezpoÄąâ€şredniego odpowiednika na Androidzie. |
## Zmienne prywatne

-   `m_egl...`: Uchwyty do zasobĂłw EGL (Display, Context, Surface, Config).
-   `m_multiInputEvent[3]`: Bufory na zdarzenia wielodotykowe.
## Zmienne globalne

-   `g_androidWindow`: Globalna instancja `AndroidWindow`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `platformwindow.h`: Klasa bazowa.
-   Wymaga `android_native_app_glue.h` i nagÄąâ€šĂłwkĂłw JNI/EGL/GLES, ktĂłre sÄ… czÄ™Äąâ€şciÄ… Android NDK.
-   W `platformwindow.cpp` wskaÄąĹźnik `g_window` jest przypisywany do `g_androidWindow`, gdy kompilacja odbywa siÄ™ dla Androida.

---
# Ä‘Ĺşâ€śâ€ž crashhandler.h
## Opis ogĂłlny

Plik `crashhandler.h` deklaruje funkcje do instalacji i deinstalacji globalnego mechanizmu obsÄąâ€šugi awarii (crash handler).
## Funkcje
## `void installCrashHandler()`

Rejestruje handlery dla sygnaÄąâ€šĂłw lub wyjÄ…tkĂłw systemowych (w zaleÄąÄ˝noÄąâ€şci od platformy), ktĂłre sÄ… wywoÄąâ€šywane w przypadku krytycznego bÄąâ€šÄ™du aplikacji (np. naruszenie ochrony pamiÄ™ci).
## `void uninstallCrashHandler()`

Odinstalowuje wczeÄąâ€şniej zarejestrowane handlery.
## Dyrektywa preprocesora

CaÄąâ€ša zawartoÄąâ€şÄ‡ pliku jest objÄ™ta dyrektywÄ… `#ifdef CRASH_HANDLER`, co oznacza, ÄąÄ˝e funkcje te sÄ… dostÄ™pne tylko wtedy, gdy opcja `CRASH_HANDLER` jest wÄąâ€šÄ…czona w CMake.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Funkcje te sÄ… implementowane w plikach specyficznych dla platformy: `unixcrashhandler.cpp` i `win32crashhandler.cpp`.
-   `installCrashHandler` jest zazwyczaj wywoÄąâ€šywana na samym poczÄ…tku dziaÄąâ€šania aplikacji.

---
# Ä‘Ĺşâ€śâ€ž platform.cpp
## Opis ogĂłlny

Plik `platform.cpp` ma za zadanie jedynie zdefiniowaÄ‡ globalnÄ… instancjÄ™ klasy `Platform`.
## Zmienne globalne
## `g_platform`

Globalna, jedyna instancja klasy `Platform`, ktĂłra dostarcza interfejs do funkcji specyficznych dla systemu operacyjnego.

`$fenceInfo
Platform g_platform;
```
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/platform/platform.h`: Plik nagÄąâ€šĂłwkowy, ktĂłry deklaruje klasÄ™ `Platform`.
-   WÄąâ€šaÄąâ€şciwa implementacja metod tej klasy znajduje siÄ™ w plikach `win32platform.cpp`, `unixplatform.cpp` i `androidplatform.cpp`, z ktĂłrych tylko jeden jest kompilowany w zaleÄąÄ˝noÄąâ€şci od docelowej platformy.

---
# Ä‘Ĺşâ€śâ€ž platformwindow.cpp
## Opis ogĂłlny

Plik `platformwindow.cpp` jest kluczowym plikiem, ktĂłry zarzÄ…dza implementacjÄ… okna specyficznÄ… dla danej platformy. Jego gÄąâ€šĂłwnym zadaniem jest doÄąâ€šÄ…czenie odpowiedniego pliku nagÄąâ€šĂłwkowego (np. `win32window.h` lub `x11window.h`) i zdefiniowanie globalnego wskaÄąĹźnika `g_window`, ktĂłry bÄ™dzie wskazywaÄąâ€š na wÄąâ€šaÄąâ€şciwÄ…, platformowÄ… instancjÄ™ okna.
## Zmienne globalne
## `g_window`

Globalna referencja do obiektu okna. Jest to centralny punkt dostÄ™pu do wszystkich operacji zwiÄ…zanych z oknem w caÄąâ€šym frameworku. W zaleÄąÄ˝noÄąâ€şci od platformy, wskazuje na instancjÄ™ `WIN32Window`, `X11Window`, `AndroidWindow` lub `SDLWindow`.

`$fenceInfo
# ifdef ANDROID
PlatformWindow& g_window = g_androidWindow;
# else
PlatformWindow& g_window = window; // gdzie 'window' to globalna instancja np. WIN32Window
# endif
```
## Klasa `PlatformWindow`
## `int PlatformWindow::loadMouseCursor(...)`

ÄąÂaduje obraz kursora, sprawdza jego poprawnoÄąâ€şÄ‡ (rozmiar 32x32, 4 kanaÄąâ€šy kolorĂłw) i deleguje wÄąâ€šaÄąâ€şciwe tworzenie kursora do metody wirtualnej `internalLoadMouseCursor`, ktĂłra jest zaimplementowana w klasach pochodnych.
## `void PlatformWindow::updateUnmaximizedCoords()`

Zapisuje aktualnÄ… pozycjÄ™ i rozmiar okna, ale tylko wtedy, gdy okno nie jest zmaksymalizowane ani w trybie peÄąâ€šnoekranowym. SÄąâ€šuÄąÄ˝y do przywracania poprzedniego stanu okna.
## `void PlatformWindow::processKeyDown(Fw::Key keyCode)`

ObsÄąâ€šuguje zdarzenie wciÄąâ€şniÄ™cia klawisza.
-   Aktualizuje stan modyfikatorĂłw (Ctrl, Alt, Shift).
-   Sprawdza, czy klawisz nie jest juÄąÄ˝ wciÄąâ€şniÄ™ty (obsÄąâ€šuga auto-powtarzania).
-   Ustawia stan klawisza na wciÄąâ€şniÄ™ty (`m_keysState`).
-   WysyÄąâ€ša zdarzenia `KeyDownInputEvent` i `KeyPressInputEvent` do zarejestrowanego `callbacka`.
## `void PlatformWindow::processKeyUp(Fw::Key keyCode)`

ObsÄąâ€šuguje zdarzenie zwolnienia klawisza.
-   Aktualizuje stan modyfikatorĂłw.
-   Ustawia stan klawisza na zwolniony.
-   WysyÄąâ€ša zdarzenie `KeyUpInputEvent`.
## `void PlatformWindow::releaseAllKeys()`

Resetuje stan wszystkich wciÄąâ€şniÄ™tych klawiszy i przyciskĂłw myszy. WywoÄąâ€šywana np. gdy okno traci fokus.
## `void PlatformWindow::fireKeysPress()`

Metoda wywoÄąâ€šywana cyklicznie. Sprawdza, ktĂłre klawisze sÄ… wciÄąâ€şniÄ™te i od odpowiednio dÄąâ€šugiego czasu, a nastÄ™pnie generuje zdarzenia `KeyPressInputEvent` (auto-powtarzanie).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   WÄąâ€šÄ…cza jeden z plikĂłw nagÄąâ€šĂłwkowych specyficznych dla platformy (`win32window.h`, `x11window.h`, etc.).
-   `framework/core/eventdispatcher.h`: UÄąÄ˝ywa `g_dispatcher` do bezpiecznego wÄ…tkowo przetwarzania zdarzeÄąâ€ž.
-   `framework/graphics/image.h`: Do Äąâ€šadowania obrazĂłw kursorĂłw.
-   Jest to implementacja czÄ™Äąâ€şci wspĂłlnej dla wszystkich platform, podczas gdy specyfika jest w klasach pochodnych.

---
# Ä‘Ĺşâ€śâ€ž platform.h
## Opis ogĂłlny

Plik `platform.h` deklaruje klasÄ™ `Platform`, ktĂłra jest interfejsem do funkcji specyficznych dla systemu operacyjnego. Zapewnia abstrakcjÄ™ nad rĂłÄąÄ˝nicami miÄ™dzy platformami (Windows, Linux, macOS, Android).
## Klasa `Platform`
## Opis semantyczny
`Platform` dostarcza zestaw statycznych metod do interakcji z systemem operacyjnym. Implementacja tych metod znajduje siÄ™ w plikach specyficznych dla platformy (np. `win32platform.cpp`, `unixplatform.cpp`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void processArgs(...)` | Przetwarza argumenty wiersza poleceÄąâ€ž, konwertujÄ…c je do UTF-8. |
| `bool spawnProcess(...)` | Uruchamia nowy proces. |
| `int getProcessId()` | Zwraca ID bieÄąÄ˝Ä…cego procesu. |
| `bool isProcessRunning(...)` | Sprawdza, czy proces o danej nazwie jest uruchomiony. |
| `bool killProcess(...)` | Zamyka proces o danej nazwie. |
| `std::string getTempPath()` | Zwraca Äąâ€şcieÄąÄ˝kÄ™ do katalogu tymczasowego. |
| `std::string getCurrentDir()` | Zwraca bieÄąÄ˝Ä…cy katalog roboczy. |
| `bool copyFile(...)`, `fileExists(...)`, `removeFile(...)` | Podstawowe operacje na plikach. |
| `ticks_t getFileModificationTime(...)` | Zwraca czas ostatniej modyfikacji pliku. |
| `bool openUrl(...)` | Otwiera URL w domyÄąâ€şlnej przeglÄ…darce. |
| `bool openDir(...)` | Otwiera katalog w menedÄąÄ˝erze plikĂłw. |
| `std::string getCPUName()` | Zwraca nazwÄ™ procesora. |
| `double getTotalSystemMemory()`| Zwraca caÄąâ€škowitÄ… iloÄąâ€şÄ‡ pamiÄ™ci RAM. |
| `double getMemoryUsage()` | Zwraca uÄąÄ˝ycie pamiÄ™ci przez bieÄąÄ˝Ä…cy proces. |
| `std::string getOSName()` | Zwraca nazwÄ™ systemu operacyjnego. |
| `std::string traceback(...)` | Generuje Äąâ€şlad stosu wywoÄąâ€šaÄąâ€ž C++. |
| `std::vector<std::string> getMacAddresses()` | Zwraca listÄ™ adresĂłw MAC. |
| `std::string getUserName()` | Zwraca nazwÄ™ zalogowanego uÄąÄ˝ytkownika. |
| `std::vector<std::string> getDlls()` | (Windows) Zwraca listÄ™ zaÄąâ€šadowanych bibliotek DLL. |
| `std::vector<std::string> getProcesses()` | Zwraca listÄ™ uruchomionych procesĂłw. |
| `std::vector<std::string> getWindows()` | (Windows) Zwraca listÄ™ tytuÄąâ€šĂłw otwartych okien. |
## Zmienne globalne

-   `g_platform`: Globalna instancja `Platform`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   UÄąÄ˝ywana w caÄąâ€šym projekcie do operacji, ktĂłre wymagajÄ… interakcji z systemem operacyjnym.
-   Jej implementacja jest dostarczana przez pliki `*.cpp` specyficzne dla platformy.

---
# Ä‘Ĺşâ€śâ€ž platformwindow.h
## Opis ogĂłlny

Plik `platformwindow.h` deklaruje abstrakcyjnÄ… klasÄ™ bazowÄ… `PlatformWindow`, ktĂłra definiuje wspĂłlny interfejs do zarzÄ…dzania oknem aplikacji na rĂłÄąÄ˝nych systemach operacyjnych.
## Klasa `PlatformWindow`
## Opis semantyczny
`PlatformWindow` jest klasÄ… abstrakcyjnÄ…, ktĂłra ukrywa szczegĂłÄąâ€šy implementacyjne zwiÄ…zane z tworzeniem okna, obsÄąâ€šugÄ… zdarzeÄąâ€ž i zarzÄ…dzaniem kontekstem graficznym. KaÄąÄ˝da platforma (Windows, Linux, Android) dostarcza wÄąâ€šasnÄ…, konkretnÄ… implementacjÄ™ tej klasy.
## Metody czysto wirtualne (do implementacji przez klasy pochodne)

-   `init()`, `terminate()`: Cykl ÄąÄ˝ycia okna.
-   `move()`, `resize()`, `show()`, `hide()`, `minimize()`, `maximize()`: ZarzÄ…dzanie stanem okna.
-   `poll()`: Przetwarzanie zdarzeÄąâ€ž systemowych.
-   `swapBuffers()`: Zamiana buforĂłw graficznych.
-   `set...()`: Metody do ustawiania wÄąâ€šaÄąâ€şciwoÄąâ€şci okna (tytuÄąâ€š, ikona, VSync, etc.).
-   `get...()`: Metody do pobierania informacji (rozmiar ekranu, tekst ze schowka).
## Metody z implementacjÄ…

-   `loadMouseCursor(...)`: ÄąÂaduje kursor z pliku.
-   `processKeyDown()`, `processKeyUp()`, `releaseAllKeys()`, `fireKeysPress()`: ImplementujÄ… logikÄ™ obsÄąâ€šugi stanu klawiatury, ktĂłra jest wspĂłlna dla wszystkich platform.
-   Gettery dla stanu okna (`getSize`, `getPosition`, `isVisible`, `isKeyPressed`, etc.).
## Zmienne chronione

-   `m_keyMap`: Mapa tÄąâ€šumaczÄ…ca kody klawiszy specyficzne dla platformy na wewnÄ™trzne kody `Fw::Key`.
-   `m_keysState`, `m_lastKeysPress`: Mapy do Äąâ€şledzenia stanu klawiszy.
-   `m_size`, `m_position`, `m_minimumSize`: WÄąâ€šaÄąâ€şciwoÄąâ€şci geometryczne okna.
-   `m_inputEvent`: Obiekt do przechowywania danych o bieÄąÄ˝Ä…cym zdarzeniu wejÄąâ€şciowym.
-   `m_visible`, `m_focused`, `m_fullscreen`, `m_maximized`: Flagi stanu okna.
-   `m_onClose`, `m_onResize`, `m_onInputEvent`: Callbacki do powiadamiania `GraphicalApplication` o zdarzeniach.
## Zmienne globalne

-   `g_window`: Globalna referencja do aktywnej instancji `PlatformWindow`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/core/inputevent.h`: Struktura `InputEvent`.
-   `framework/graphics/declarations.h`: Deklaracje typĂłw graficznych.
-   Jest klasÄ… bazowÄ… dla `WIN32Window`, `X11Window`, `AndroidWindow`, `SDLWindow`.
-   Jest uÄąÄ˝ywana przez `GraphicalApplication` do wszystkich operacji na oknie.

---
# Ä‘Ĺşâ€śâ€ž sdlwindow.cpp
## Opis ogĂłlny

Plik `sdlwindow.cpp` zawiera implementacjÄ™ klasy `SDLWindow`, ktĂłra jest wersjÄ… `PlatformWindow` dla platformy Emscripten (WebAssembly), opartÄ… na bibliotece SDL.

> **NOTE:** Implementacja jest w wiÄ™kszoÄąâ€şci pusta. Sugeruje to, ÄąÄ˝e obsÄąâ€šuga okna i zdarzeÄąâ€ž w Emscripten jest realizowana w inny sposĂłb, prawdopodobnie poprzez gÄąâ€šĂłwnÄ… pÄ™tlÄ™ Emscripten i bezpoÄąâ€şrednie wywoÄąâ€šania JavaScript, a ta klasa jest jedynie "zaÄąâ€şlepkÄ…" (placeholderem), aby kod siÄ™ kompilowaÄąâ€š.
## Klasa `SDLWindow`

Wszystkie metody implementujÄ…ce interfejs `PlatformWindow` sÄ… puste. Oznacza to, ÄąÄ˝e operacje takie jak `resize`, `move`, `setTitle`, `poll` czy `swapBuffers` nie majÄ… tutaj ÄąÄ˝adnego efektu i muszÄ… byÄ‡ obsÄąâ€šugiwane przez zewnÄ™trzny kod (prawdopodobnie w gÄąâ€šĂłwnej pÄ™tli `emscripten_set_main_loop`).
## `SDLWindow::SDLWindow()`

Konstruktor. Inicjalizuje domyÄąâ€şlne rozmiary i stan.
## `std::string SDLWindow::getPlatformType()`

Zwraca `"WASM"`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/platform/sdlwindow.h`: Plik nagÄąâ€šĂłwkowy.
-   W `platformwindow.cpp` (niezaÄąâ€šÄ…czony, ale moÄąÄ˝na siÄ™ domyÄąâ€şlaÄ‡), `g_window` jest ustawiane na instancjÄ™ `SDLWindow` gdy kompilacja odbywa siÄ™ dla Emscripten.

---
# Ä‘Ĺşâ€śâ€ž sdlwindow.h
## Opis ogĂłlny

Plik `sdlwindow.h` deklaruje klasÄ™ `SDLWindow`, ktĂłra jest implementacjÄ… `PlatformWindow` dla platformy Emscripten (WebAssembly), opartÄ… na bibliotece SDL.
## Klasa `SDLWindow`
## Opis semantyczny
`SDLWindow` jest klasÄ…-zaÄąâ€şlepkÄ…, ktĂłra speÄąâ€šnia kontrakt interfejsu `PlatformWindow`, ale wiÄ™kszoÄąâ€şÄ‡ jej metod jest pusta. Logika okna dla Emscripten jest zazwyczaj obsÄąâ€šugiwana przez gÄąâ€šĂłwnÄ… pÄ™tlÄ™ zdefiniowanÄ… w `emscripten.h` i interakcje z API przeglÄ…darki, a nie przez tradycyjny model okienkowy.
## Metody publiczne
Deklaruje wszystkie metody wirtualne z `PlatformWindow` z pustymi implementacjami.
## Zmienne prywatne
-   `m_egl...`: Pola zwiÄ…zane z EGL, odziedziczone po logice Androida, ale prawdopodobnie nieuÄąÄ˝ywane w kontekÄąâ€şcie Emscripten/SDL.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `platformwindow.h`: Klasa bazowa.
-   Jest to implementacja `PlatformWindow` uÄąÄ˝ywana, gdy zdefiniowano `__EMSCRIPTEN__`.

---
# Ä‘Ĺşâ€śâ€ž unixcrashhandler.cpp
## Opis ogĂłlny

Plik `unixcrashhandler.cpp` zawiera implementacjÄ™ mechanizmu obsÄąâ€šugi awarii (crash handler) dla systemĂłw uniksowych (Linux, macOS). Jest kompilowany tylko wtedy, gdy zdefiniowano `CRASH_HANDLER` i platforma nie jest Windows ani Emscripten.
## Funkcje
## `void crashHandler(int signum, siginfo_t* info, void* secret)`
## Opis semantyczny
Jest to funkcja obsÄąâ€šugi sygnaÄąâ€šu, ktĂłra jest wywoÄąâ€šywana przez system operacyjny w momencie wystÄ…pienia krytycznego bÄąâ€šÄ™du (np. bÄąâ€šÄ…d segmentacji). Jej zadaniem jest zebranie jak najwiÄ™kszej iloÄąâ€şci informacji o stanie programu w momencie awarii i zapisanie ich do logu.
## DziaÄąâ€šanie
1.  Loguje komunikat "Application crashed".
2.  Tworzy strumieÄąâ€ž `stringstream` do budowy raportu.
3.  Zapisuje podstawowe informacje o aplikacji (nazwa, wersja, data kompilacji itp.).
4.  Pobiera kontekst procesora (`ucontext_t`) i zapisuje wartoÄąâ€şci rejestrĂłw (np. `rip`, `rax` dla x64; `eip`, `eax` dla x86).
5.  Generuje Äąâ€şlad stosu wywoÄąâ€šaÄąâ€ž (backtrace) za pomocÄ… `backtrace()` i `backtrace_symbols()`.
6.  Opcjonalnie (jeÄąâ€şli zdefiniowano `DEMANGLE_BACKTRACE_SYMBOLS`), prĂłbuje zdemanglowaÄ‡ nazwy funkcji C++ w Äąâ€şladzie stosu.
7.  Zapisuje caÄąâ€šy raport do pliku `crash_report.log` i do gÄąâ€šĂłwnego logu aplikacji.
8.  Przywraca domyÄąâ€şlnÄ… obsÄąâ€šugÄ™ sygnaÄąâ€šĂłw, aby umoÄąÄ˝liwiÄ‡ systemowi operacyjnemu dokoÄąâ€žczenie procesu zamykania aplikacji.
## `void installCrashHandler()`

Rejestruje funkcjÄ™ `crashHandler` jako handler dla sygnaÄąâ€šĂłw:
-   `SIGILL`: Nielegalna instrukcja.
-   `SIGSEGV`: Naruszenie ochrony pamiÄ™ci.
-   `SIGFPE`: BÄąâ€šÄ…d operacji zmiennoprzecinkowej.
-   `SIGABRT`: SygnaÄąâ€š przerwania (np. z `assert`).
## `void uninstallCrashHandler()`

Pusta funkcja, deinstalacja nie jest zaimplementowana.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/platform/crashhandler.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/global.h`, `framework/core/application.h`: Do pobierania informacji o aplikacji.
-   NagÄąâ€šĂłwki systemowe: `execinfo.h`, `ucontext.h`, `signal.h`.

---
# Ä‘Ĺşâ€śâ€ž unixplatform.cpp
## Opis ogĂłlny

Plik `unixplatform.cpp` zawiera implementacjÄ™ metod klasy `Platform` specyficznych dla systemĂłw uniksowych (Linux, macOS). Jest kompilowany, gdy platforma nie jest ani Windows, ani Emscripten.
## Klasa `Platform` (implementacja dla Uniksa)

| Metoda | Implementacja na Uniksie |
| :--- | :--- |
| `spawnProcess(...)` | UÄąÄ˝ywa `fork()` i `execv()` do uruchomienia nowego procesu. |
| `getProcessId()` | UÄąÄ˝ywa `getpid()`. |
| `isProcessRunning(...)`, `killProcess(...)` | Puste implementacje. |
| `getTempPath()` | Zwraca `/tmp/`. |
| `getCurrentDir()` | UÄąÄ˝ywa `getcwd()`. |
| `copyFile(...)` | WywoÄąâ€šuje systemowÄ… komendÄ™ `cp`. |
| `fileExists(...)` | UÄąÄ˝ywa `stat()`. |
| `removeFile(...)` | UÄąÄ˝ywa `unlink()`. |
| `getFileModificationTime(...)`| UÄąÄ˝ywa `stat()` do odczytania `st_mtime`. |
| `openUrl(...)`, `openDir(...)` | WywoÄąâ€šuje systemowÄ… komendÄ™ `xdg-open`. MoÄąÄ˝e to zrobiÄ‡ natychmiast lub w `EventDispatcher`. |
| `getCPUName()` | Parsuje plik `/proc/cpuinfo`. |
| `getTotalSystemMemory()` | Parsuje plik `/proc/meminfo`. |
| `getMemoryUsage()` | Pusta implementacja. |
| `getOSName()` | Parsuje plik `/etc/issue`. |
| `traceback(...)` | UÄąÄ˝ywa `backtrace()` i `backtrace_symbols()` do generowania Äąâ€şladu stosu, z opcjonalnym demanglowaniem nazw funkcji. |
| `getMacAddresses()` | Pusta implementacja. |
| `getUserName()` | UÄąÄ˝ywa `getlogin_r()`. |
| `getDlls()`, `getProcesses()`, `getWindows()` | Puste implementacje (brak bezpoÄąâ€şrednich odpowiednikĂłw). |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/platform/platform.h`: Plik nagÄąâ€šĂłwkowy.
-   NagÄąâ€šĂłwki systemowe POSIX (`unistd.h`, `sys/stat.h`, `execinfo.h`).
-   `framework/core/eventdispatcher.h`: Do asynchronicznego otwierania URL/katalogĂłw.

---
# Ä‘Ĺşâ€śâ€ž win32crashhandler.cpp
## Opis ogĂłlny

Plik `win32crashhandler.cpp` zawiera implementacjÄ™ mechanizmu obsÄąâ€šugi awarii (crash handler) dla systemu Windows. Jest kompilowany, gdy zdefiniowano `WIN32` i `CRASH_HANDLER`.
## Funkcje
## `const char *getExceptionName(DWORD exceptionCode)`

Funkcja pomocnicza, ktĂłra tÄąâ€šumaczy kod wyjÄ…tku Windows (np. `EXCEPTION_ACCESS_VIOLATION`) ÄËťÄÂ° czytelnÄ… nazwÄ™.
## `void Stacktrace(LPEXCEPTION_POINTERS e, std::stringstream& ss)`

Generuje Äąâ€şlad stosu wywoÄąâ€šaÄąâ€ž. UÄąÄ˝ywa funkcji z biblioteki `DbgHelp.dll` (`StackWalk`, `SymGetModuleBase`, `SymGetSymFromAddr`), aby przejÄąâ€şÄ‡ przez stos i odczytaÄ‡ nazwy funkcji i moduÄąâ€šĂłw.
## `LONG CALLBACK ExceptionHandler(PEXCEPTION_POINTERS e)`

Starsza wersja handlera. Generuje raport tekstowy podobny do wersji uniksowej, zapisuje go do pliku i wyÄąâ€şwietla `MessageBox` z informacjÄ… o awarii.
## `LONG WINAPI UnhandledExceptionFilter2(PEXCEPTION_POINTERS exception)`

Nowsza, gÄąâ€šĂłwna funkcja obsÄąâ€šugi wyjÄ…tkĂłw.
-   **DziaÄąâ€šanie**:
    1.  Tworzy i zapisuje **minidump** awarii do plikĂłw (`exception.dmp`, `exception_full.dmp`). Minidump to plik, ktĂłry moÄąÄ˝na otworzyÄ‡ w debuggerze (np. Visual Studio, WinDbg) w celu poÄąâ€şmiertnej analizy stanu programu.
    2.  JeÄąâ€şli `quiet_crash` jest `true` (ustawiane przez `uninstallCrashHandler`), cicho zamyka aplikacjÄ™.
    3.  W przeciwnym razie, wywoÄąâ€šuje `ExceptionHandler` w celu wygenerowania raportu tekstowego i wyÄąâ€şwietlenia komunikatu.
## `void installCrashHandler()`

Rejestruje `UnhandledExceptionFilter2` jako globalny handler nieobsÄąâ€šuÄąÄ˝onych wyjÄ…tkĂłw za pomocÄ… `SetUnhandledExceptionFilter`.
## `void uninstallCrashHandler()`

Ustawia flagÄ™ `quiet_crash` na `true`. Jest to uÄąÄ˝ywane np. podczas aktualizacji, aby cicho zamknÄ…Ä‡ starÄ… wersjÄ™ klienta bez wyÄąâ€şwietlania okna bÄąâ€šÄ™du.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/platform/crashhandler.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/global.h`, `core/application.h`, `core/resourcemanager.h`.
-   NagÄąâ€šĂłwki Windows (`windows.h`, `imagehlp.h`, `DbgHelp.h`).

---
# Ä‘Ĺşâ€śâ€ž win32platform.cpp
## Opis ogĂłlny

Plik `win32platform.cpp` zawiera implementacjÄ™ metod klasy `Platform` specyficznych dla systemu Windows.
## Klasa `Platform` (implementacja dla Windows)

| Metoda | Implementacja na Windows |
| :--- | :--- |
| `processArgs(...)` | UÄąÄ˝ywa `CommandLineToArgvW` do poprawnego sparsowania argumentĂłw wiersza poleceÄąâ€ž (z obsÄąâ€šugÄ… Unicode). |
| `spawnProcess(...)`| UÄąÄ˝ywa `ShellExecuteW`. |
| `getProcessId()` | UÄąÄ˝ywa `GetCurrentProcessId()`. |
| `isProcessRunning(...)` | UÄąÄ˝ywa `FindWindowA`. |
| `killProcess(...)` | UÄąÄ˝ywa `FindWindowA`, `GetProcessId` i `TerminateProcess`. |
| `getTempPath()` | UÄąÄ˝ywa `GetTempPathW`. |
| `getCurrentDir()` | UÄąÄ˝ywa `GetCurrentDirectoryW`. |
| `copyFile(...)`, `fileExists(...)`, `removeFile(...)` | UÄąÄ˝ywajÄ… odpowiednikĂłw z WinAPI (`CopyFileW`, `GetFileAttributesW`, `DeleteFileW`). |
| `getFileModificationTime(...)`| UÄąÄ˝ywa `GetFileAttributesExW`. |
| `openUrl(...)`, `openDir(...)` | UÄąÄ˝ywajÄ… `ShellExecuteW`. |
| `getCPUName()` | Odczytuje wartoÄąâ€şÄ‡ z rejestru systemowego. |
| `getTotalSystemMemory()`| UÄąÄ˝ywa `GlobalMemoryStatusEx`. |
| `getMemoryUsage()` | UÄąÄ˝ywa `GetProcessMemoryInfo`. |
| `getOSName()` | UÄąÄ˝ywa `VerifyVersionInfo` i `GetProductInfo` do uzyskania szczegĂłÄąâ€šowej nazwy wersji Windows. |
| `traceback(...)` | Prosta implementacja, zwraca tylko informacjÄ™ o miejscu wywoÄąâ€šania. |
| `getMacAddresses()` | UÄąÄ˝ywa `GetAdaptersInfo`. |
| `getUserName()` | UÄąÄ˝ywa `GetUserNameA`. |
| `getDlls()` | UÄąÄ˝ywa `EnumProcessModules`. |
| `getProcesses()` | UÄąÄ˝ywa `CreateToolhelp32Snapshot` do iteracji po procesach. |
| `getWindows()` | UÄąÄ˝ywa `EnumWindows` do iteracji po otwartych oknach. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/platform/platform.h`: Plik nagÄąâ€šĂłwkowy.
-   NagÄąâ€šĂłwki WinAPI.
-   `boost/algorithm/string.hpp`: Do operacji na stringach.

---
# Ä‘Ĺşâ€śâ€ž win32window.cpp
## Opis ogĂłlny

Plik `win32window.cpp` zawiera implementacjÄ™ klasy `WIN32Window`, ktĂłra jest specyficznÄ… dla Windows implementacjÄ… `PlatformWindow`. ZarzÄ…dza ona natywnym oknem WinAPI, obsÄąâ€šugÄ… zdarzeÄąâ€ž i kontekstem graficznym (WGL dla OpenGL lub EGL dla OpenGL ES/DirectX).
## Klasa `WIN32Window`
## `WIN32Window::WIN32Window()`

Konstruktor. Inicjalizuje mapÄ™ klawiszy (`m_keyMap`), tÄąâ€šumaczÄ…c wirtualne kody klawiszy Windows (`VK_*`) na wewnÄ™trzne kody `Fw::Key`.
## `void WIN32Window::init()`

Inicjalizuje okno, wywoÄąâ€šujÄ…c kolejno:
1.  `internalSetupTimerAccuracy()`: ZwiÄ™ksza precyzjÄ™ systemowego timera.
2.  `internalCreateWindow()`: Rejestruje klasÄ™ okna i tworzy okno za pomocÄ… `CreateWindowExA`.
3.  `internalCreateGLContext()`: Tworzy kontekst graficzny (WGL lub EGL).
4.  `internalRestoreGLContext()`: Aktywuje kontekst.
## `void WIN32Window::internalCreateGLContext()`

Implementacja tworzenia kontekstu graficznego:
-   **Dla OpenGL ES (`OPENGL_ES`)**: UÄąÄ˝ywa EGL (ANGLE), prĂłbujÄ…c kolejno backendĂłw D3D11, D3D9 i WARP, aby zapewniÄ‡ maksymalnÄ… kompatybilnoÄąâ€şÄ‡.
-   **Dla standardowego OpenGL**: UÄąÄ˝ywa WGL. Tworzy `PIXELFORMATDESCRIPTOR`, wybiera format pikseli i tworzy kontekst za pomocÄ… `wglCreateContext`.
## `LRESULT WIN32Window::windowProc(...)`

GÄąâ€šĂłwna funkcja obsÄąâ€šugi zdarzeÄąâ€ž okna (Window Procedure). Odbiera komunikaty od systemu Windows.
-   Przekazuje zdarzenia do `dispatcherWindowProc` w celu obsÄąâ€šugi w gÄąâ€šĂłwnym wÄ…tku aplikacji.
-   BezpoÄąâ€şrednio obsÄąâ€šuguje niektĂłre komunikaty, ktĂłre muszÄ… byÄ‡ przetworzone synchronicznie (np. `WM_SETCURSOR`, `WM_GETMINMAXINFO`).
## `LRESULT WIN32Window::dispatcherWindowProc(...)`

Metoda wywoÄąâ€šywana przez `g_dispatcher` w gÄąâ€šĂłwnym wÄ…tku. TÄąâ€šumaczy komunikaty Windows (`WM_KEYDOWN`, `WM_LBUTTONDOWN`, `WM_MOUSEMOVE` itp.) na wewnÄ™trzne `InputEvent` i przekazuje je do `m_onInputEvent` (czyli do `GraphicalApplication`).
## `void WIN32Window::poll()`

Przetwarza kolejkÄ™ komunikatĂłw Windows za pomocÄ… `PeekMessage`, `TranslateMessage` i `DispatchMessage`.
## `void WIN32Window::swapBuffers()`

Zamienia bufory ekranu za pomocÄ… `SwapBuffers` (dla WGL) lub `eglSwapBuffers` (dla EGL).
## `void WIN32Window::setVerticalSync(bool enable)`

WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza synchronizacjÄ™ pionowÄ…, uÄąÄ˝ywajÄ…c rozszerzeÄąâ€ž WGL (`WGL_EXT_swap_control`).
## Inne metody

ImplementujÄ… interfejs `PlatformWindow`, opakowujÄ…c odpowiednie funkcje WinAPI (np. `SetWindowTextW` dla `setTitle`, `ShellExecuteW` dla `openUrl`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   NagÄąâ€šĂłwki WinAPI.
-   NagÄąâ€šĂłwki OpenGL/EGL/WGL.
-   WspĂłÄąâ€špracuje z `GraphicalApplication` i `Mouse`.

---
# Ä‘Ĺşâ€śâ€ž win32window.h
## Opis ogĂłlny

Plik `win32window.h` deklaruje klasÄ™ `WIN32Window`, ktĂłra jest implementacjÄ… `PlatformWindow` dla systemu Windows.
## Klasa `WIN32Window`
## Opis semantyczny
`WIN32Window` enkapsuluje uchwyty i logikÄ™ zwiÄ…zanÄ… z natywnym oknem WinAPI. ZarzÄ…dza jego cyklem ÄąÄ˝ycia, obsÄąâ€šugÄ… komunikatĂłw systemowych i tworzeniem kontekstu graficznego (WGL dla OpenGL lub EGL dla OpenGL ES przez ANGLE).
## Metody prywatne i chronione

-   `internal...()`: Grupa metod do wewnÄ™trznego zarzÄ…dzania oknem i kontekstem GL.
-   `windowProc(...)`: GÄąâ€šĂłwna funkcja obsÄąâ€šugi komunikatĂłw Windows.
-   `dispatcherWindowProc(...)`: Handler komunikatĂłw wykonywany w gÄąâ€šĂłwnym wÄ…tku.
-   `retranslateVirtualKey(...)`: TÄąâ€šumaczy kody klawiszy WinAPI.
-   `getClientRect()`, `getWindowRect()`, `adjustWindowRect()`: Metody pomocnicze do geometrii okna.
## Zmienne prywatne

-   `m_window`: Uchwyt `HWND` do okna.
-   `m_instance`: Uchwyt `HINSTANCE` do moduÄąâ€šu aplikacji.
-   `m_deviceContext`: Uchwyt `HDC` do kontekstu urzÄ…dzenia.
-   `m_cursors`: Wektor uchwytĂłw `HCURSOR`.
-   `m_cursor`, `m_defaultCursor`: Aktywny i domyÄąâ€şlny kursor.
-   `m_hidden`: Flaga ukrycia okna.
-   `m_egl...` / `m_wglContext`: Uchwyty do zasobĂłw EGL lub WGL.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `platformwindow.h`: Klasa bazowa.
-   NagÄąâ€šĂłwki WinAPI i OpenGL/EGL.

---
# Ä‘Ĺşâ€śâ€ž x11window.h
## Opis ogĂłlny

Plik `x11window.h` deklaruje klasÄ™ `X11Window`, ktĂłra jest implementacjÄ… `PlatformWindow` dla systemĂłw uniksowych uÄąÄ˝ywajÄ…cych serwera X11 (gÄąâ€šĂłwnie Linux).
## Klasa `X11Window`
## Opis semantyczny
`X11Window` zarzÄ…dza natywnym oknem X11, obsÄąâ€šugÄ… jego zdarzeÄąâ€ž oraz tworzeniem kontekstu graficznego (GLX dla OpenGL lub EGL dla OpenGL ES).
## Metody prywatne i chronione

-   `internal...()`: Grupa metod do wewnÄ™trznego zarzÄ…dzania oknem i kontekstem GL.
-   `getExtensionProcAddress(...)`, `isExtensionSupported(...)`: Do obsÄąâ€šugi rozszerzeÄąâ€ž GLX/EGL.
## Zmienne prywatne

-   `m_display`: WskaÄąĹźnik na `Display` (poÄąâ€šÄ…czenie z serwerem X11).
-   `m_visual`: Informacje o wizualu (gÄąâ€šÄ™bia kolorĂłw itp.).
-   `m_window`: ID okna.
-   `m_rootWindow`: ID okna gÄąâ€šĂłwnego.
-   `m_colormap`: Mapa kolorĂłw.
-   `m_cursors`: Wektor kursorĂłw.
-   `m_cursor`, `m_hiddenCursor`: Aktywny i ukryty kursor.
-   `m_xim`, `m_xic`: Do obsÄąâ€šugi metod wprowadzania tekstu.
-   `m_wmDelete`: Atom do obsÄąâ€šugi zdarzenia zamkniÄ™cia okna.
-   `m_glxContext` / `m_egl...`: Uchwyty do zasobĂłw GLX lub EGL.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `platformwindow.h`: Klasa bazowa.
-   NagÄąâ€šĂłwki X11, GLX, EGL.

---
# Ä‘Ĺşâ€śâ€ž x11window.cpp
## Opis ogĂłlny

Plik `x11window.cpp` zawiera implementacjÄ™ klasy `X11Window` dla systemĂłw uniksowych z X11.
## Klasa `X11Window`
## `X11Window::X11Window()`

Konstruktor. Inicjalizuje mapÄ™ klawiszy, tÄąâ€šumaczÄ…c `KeySym` z X11 na `Fw::Key`.
## `void X11Window::init()`

Inicjalizuje okno, wywoÄąâ€šujÄ…c kolejno:
1.  `internalOpenDisplay()`: Otwiera poÄąâ€šÄ…czenie z serwerem X11.
2.  `internalCheckGL()`: Sprawdza dostÄ™pnoÄąâ€şÄ‡ GLX/EGL.
3.  `internalChooseGLVisual()`: Wybiera odpowiedni format wizualny.
4.  `internalCreateGLContext()`: Tworzy kontekst graficzny.
5.  `internalCreateWindow()`: Tworzy okno X11.
## `void X11Window::internalCreateWindow()`

Tworzy okno za pomocÄ… `XCreateWindow`, ustawia atrybuty, w tym maskÄ™ zdarzeÄąâ€ž, i przygotowuje obsÄąâ€šugÄ™ zamkniÄ™cia okna przez menedÄąÄ˝era okien. Inicjalizuje rĂłwnieÄąÄ˝ XIM/XIC do obsÄąâ€šugi wprowadzania tekstu.
## `void X11Window::poll()`

Przetwarza kolejkÄ™ zdarzeÄąâ€ž X11 za pomocÄ… `XPending` i `XNextEvent`. TÄąâ€šumaczy zdarzenia X11 (`KeyPress`, `ButtonPress`, `MotionNotify`, `ConfigureNotify` itp.) na wewnÄ™trzne `InputEvent` i wywoÄąâ€šuje odpowiednie `callbacki` w `g_dispatcher`. ObsÄąâ€šuguje rĂłwnieÄąÄ˝ logikÄ™ auto-powtarzania klawiszy i wprowadzania tekstu.
## `void X11Window::swapBuffers()`

Zamienia bufory ekranu za pomocÄ… `glXSwapBuffers` (dla GLX) lub `eglSwapBuffers` (dla EGL).
## `void X11Window::setFullscreen(bool fullscreen)`

Zmienia stan okna na peÄąâ€šnoekranowy, wysyÄąâ€šajÄ…c odpowiedni komunikat `_NET_WM_STATE` do menedÄąÄ˝era okien.
## `void X11Window::setClipboardText(...)` i `getClipboardText()`

ImplementujÄ… obsÄąâ€šugÄ™ schowka za pomocÄ… mechanizmu selekcji X11.
## Inne metody

ImplementujÄ… interfejs `PlatformWindow`, opakowujÄ…c odpowiednie funkcje X11 (np. `XStoreName` dla `setTitle`, `XMoveWindow` dla `move`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   NagÄąâ€šĂłwki X11, GLX, EGL.
-   WspĂłÄąâ€špracuje z `GraphicalApplication`.

---
# Ä‘Ĺşâ€śâ€ž proxy.cpp
## Opis ogĂłlny

Plik `proxy.cpp` zawiera implementacjÄ™ klasy `ProxyManager`, ktĂłra zarzÄ…dza systemem proxy do komunikacji z serwerem gry.
## Zmienne globalne
## `g_proxy`

Globalna instancja `ProxyManager`.
## Klasa `ProxyManager`
## `void ProxyManager::init()` i `terminate()`

UruchamiajÄ… i zatrzymujÄ… dedykowany wÄ…tek sieciowy, w ktĂłrym dziaÄąâ€ša `io_context` dla operacji proxy.
## `void ProxyManager::clear()`

Zamyka wszystkie aktywne sesje i poÄąâ€šÄ…czenia z serwerami proxy.
## `bool ProxyManager::isActive()`

Zwraca `true`, jeÄąâ€şli skonfigurowano co najmniej jeden serwer proxy.
## `void ProxyManager::addProxy(...)`

Dodaje nowy serwer proxy do puli. Tworzy obiekt `Proxy` i uruchamia go.
## `void ProxyManager::removeProxy(...)`

Usuwa serwer proxy z puli.
## `uint32_t ProxyManager::addSession(...)`

Tworzy nowÄ… sesjÄ™ proxy dla poÄąâ€šÄ…czenia z serwerem gry. Tworzy obiekt `Session` i zwraca jego unikalne ID.
## `void ProxyManager::removeSession(...)`

Zamyka sesjÄ™ o danym ID.
## `void ProxyManager::send(...)`

WysyÄąâ€ša pakiet w ramach danej sesji. Znajduje odpowiedni obiekt `Session` i przekazuje mu pakiet.
## `int ProxyManager::getPing()`

Zwraca najlepszy (najniÄąÄ˝szy) ping spoÄąâ€şrĂłd wszystkich aktywnych i poÄąâ€šÄ…czonych serwerĂłw proxy.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/proxy/proxy.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/proxy/proxy_client.h`: Definicje klas `Proxy` i `Session`.
-   Jest uÄąÄ˝ywana przez `Protocol` do tunelowania poÄąâ€šÄ…czenia przez serwery proxy.

---
# Ä‘Ĺşâ€śâ€ž proxy.h
## Opis ogĂłlny

Plik `proxy.h` deklaruje klasÄ™ `ProxyManager`, ktĂłra jest singletonem (`g_proxy`) odpowiedzialnym za zarzÄ…dzanie caÄąâ€šym systemem poÄąâ€šÄ…czeÄąâ€ž proxy. Stanowi on gÄąâ€šĂłwny punkt wejÄąâ€şcia do konfiguracji i wykorzystania tunelowania ruchu sieciowego.
## Klasa `ProxyManager`
## Opis semantyczny
`ProxyManager` zarzÄ…dza pulÄ… dostÄ™pnych serwerĂłw proxy (obiekty `Proxy`) oraz pulÄ… aktywnych sesji klienta (obiekty `Session`). Jego zadaniem jest koordynacja miÄ™dzy sesjami a serwerami proxy, dynamiczne wybieranie najlepszych serwerĂłw do tunelowania ruchu oraz dostarczanie interfejsu do zarzÄ…dzania tym procesem z poziomu aplikacji i skryptĂłw Lua. DziaÄąâ€ša w dedykowanym wÄ…tku sieciowym, aby nie blokowaÄ‡ gÄąâ€šĂłwnego wÄ…tku aplikacji.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Uruchamia i zatrzymuje wÄ…tek sieciowy `ProxyManager`. |
| `clear()` | Zamyka wszystkie aktywne sesje i poÄąâ€šÄ…czenia z serwerami proxy. |
| `setMaxActiveProxies(int value)` | Ustawia, przez ile najlepszych (pod wzglÄ™dem pingu) serwerĂłw proxy ma byÄ‡ jednoczeÄąâ€şnie tunelowany ruch dla kaÄąÄ˝dej sesji. |
| `isActive()` | Zwraca `true`, jeÄąâ€şli co najmniej jeden serwer proxy jest skonfigurowany. |
| `addProxy(...)` / `removeProxy(...)` | Dodaje lub usuwa serwer proxy z puli dostÄ™pnych serwerĂłw. |
| `uint32_t addSession(...)` | Tworzy nowÄ… sesjÄ™ proxy dla poÄąâ€šÄ…czenia z serwerem gry. Zwraca unikalne ID sesji. |
| `void removeSession(uint32_t sessionId)` | Zamyka i usuwa sesjÄ™ o podanym ID. |
| `void send(uint32_t sessionId, ProxyPacketPtr packet)` | WysyÄąâ€ša pakiet w ramach okreÄąâ€şlonej sesji. `ProxyManager` przekazuje go do odpowiedniego obiektu `Session`. |
| `std::map<...> getProxies()` | Zwraca mapÄ™ dostÄ™pnych serwerĂłw proxy wraz z ich pingiem. |
| `std::map<...> getProxiesDebugInfo()` | Zwraca szczegĂłÄąâ€šowe informacje diagnostyczne o kaÄąÄ˝dym proxy. |
| `int getPing()` | Zwraca najniÄąÄ˝szy ping spoÄąâ€şrĂłd wszystkich aktywnych serwerĂłw proxy. |
## Zmienne prywatne

-   `m_io`: Kontekst `io_context` z Boost.Asio, na ktĂłrym dziaÄąâ€šajÄ… wszystkie operacje sieciowe proxy.
-   `m_guard`: Obiekt `work_guard`, ktĂłry zapobiega zakoÄąâ€žczeniu dziaÄąâ€šania `m_io`, dopĂłki `ProxyManager` jest aktywny.
-   `m_working`: Flaga kontrolujÄ…ca dziaÄąâ€šanie wÄ…tku.
-   `m_thread`: Dedykowany wÄ…tek dla operacji sieciowych proxy.
-   `m_maxActiveProxies`: Maksymalna liczba proxy uÄąÄ˝ywanych przez jednÄ… sesjÄ™.
-   `m_proxies`: Lista wskaÄąĹźnikĂłw na dostÄ™pne obiekty `Proxy`.
-   `m_sessions`: Lista wskaÄąĹźnikĂłw na aktywne obiekty `Session`.
## Zmienne globalne

-   `g_proxy`: Globalna instancja `ProxyManager`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/proxy/proxy_client.h`: Definicje klas `Proxy` i `Session`, ktĂłrymi zarzÄ…dza.
-   Jest uÄąÄ˝ywana przez `Protocol` do tworzenia tunelowanych poÄąâ€šÄ…czeÄąâ€ž.
-   Jej API jest dostÄ™pne w Lua (przez `luafunctions.cpp`), co pozwala na dynamicznÄ… konfiguracjÄ™ proxy ze skryptĂłw.

---
# Ä‘Ĺşâ€śâ€ž proxy_client.h
## Opis ogĂłlny

Plik `proxy_client.h` deklaruje dwie kluczowe klasy dla systemu proxy: `Proxy` i `Session`. Te klasy implementujÄ… logikÄ™ klienta, ktĂłry Äąâ€šÄ…czy siÄ™ z serwerami proxy i tuneluje przez nie ruch sieciowy.
## Definicje typĂłw

-   `ProxyPacket`: Alias dla `std::vector<uint8_t>`, reprezentuje pojedynczy pakiet.
-   `ProxyPacketPtr`: Alias dla `std::shared_ptr<ProxyPacket>`.
-   `Session`, `SessionPtr`: Wczesna deklaracja i alias dla wskaÄąĹźnika na `Session`.
## Klasa `Proxy`
## Opis semantyczny
`Proxy` reprezentuje pojedyncze, trwaÄąâ€še poÄąâ€šÄ…czenie z jednym serwerem proxy. Jego zadaniem jest utrzymanie poÄąâ€šÄ…czenia, monitorowanie jego jakoÄąâ€şci (ping), przesyÄąâ€šanie pakietĂłw dla wielu sesji oraz raportowanie swojego stanu do `ProxyManager`.
## StaÄąâ€še i typy wyliczeniowe

-   `CHECK_INTERVAL`: InterwaÄąâ€š (w ms) sprawdzania stanu poÄąâ€šÄ…czenia i wysyÄąâ€šania pingĂłw.
-   `BUFFER_SIZE`: Rozmiar bufora odczytu.
-   `enum ProxyState`: Definiuje stany, w jakich moÄąÄ˝e znajdowaÄ‡ siÄ™ poÄąâ€šÄ…czenie z proxy (np. `STATE_NOT_CONNECTED`, `STATE_CONNECTING`, `STATE_CONNECTED`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Proxy(...)` | Konstruktor. |
| `void start()` | Inicjuje cykl ÄąÄ˝ycia obiektu, dodajÄ…c go do globalnej puli i uruchamiajÄ…c pÄ™tlÄ™ `check`. |
| `void terminate()` | Zamyka poÄąâ€šÄ…czenie i usuwa obiekt z globalnej puli. |
| `uint32_t getPing()` | Zwraca opĂłÄąĹźnienie do serwera proxy, uwzglÄ™dniajÄ…c priorytet. |
| `uint32_t getRealPing()` | Zwraca rzeczywiste opĂłÄąĹźnienie (bez priorytetu). |
| `bool isConnected()` | Zwraca `true`, jeÄąâ€şli poÄąâ€šÄ…czenie jest w stanie `STATE_CONNECTED`. |
| `std::string getDebugInfo()`| Zwraca informacje diagnostyczne. |
| `bool isActive()` | Zwraca `true`, jeÄąâ€şli przez to proxy przechodzi ruch co najmniej jednej sesji. |
| `void addSession(...)` | WysyÄąâ€ša do serwera proxy polecenie utworzenia nowej sesji tunelowania. |
| `void removeSession(...)` | WysyÄąâ€ša polecenie zamkniÄ™cia sesji. |
| `void send(...)` | Dodaje pakiet do kolejki wysyÄąâ€šania do serwera proxy. |
## Klasa `Session`
## Opis semantyczny
`Session` reprezentuje pojedynczÄ… sesjÄ™ klienta z serwerem gry, ktĂłra jest tunelowana przez jeden lub wiÄ™cej serwerĂłw proxy. MoÄąÄ˝e dziaÄąâ€šaÄ‡ w dwĂłch trybach: jako serwer (akceptujÄ…c lokalne poÄąâ€šÄ…czenie od klienta gry) lub jako klient (gdy jest tworzona bezpoÄąâ€şrednio przez `Protocol`). Odpowiada za dynamiczne wybieranie najlepszych `Proxy` do wysyÄąâ€šania pakietĂłw oraz za re-asemblacjÄ™ pakietĂłw przychodzÄ…cych, ktĂłre mogÄ… docieraÄ‡ z rĂłÄąÄ˝nych `Proxy` i w rĂłÄąÄ˝nej kolejnoÄąâ€şci.
## StaÄąâ€še

-   `CHECK_INTERVAL`: InterwaÄąâ€š (w ms) sprawdzania stanu sesji i wyboru proxy.
-   `BUFFER_SIZE`: Rozmiar bufora.
-   `TIMEOUT`: Czas (w ms) braku aktywnoÄąâ€şci, po ktĂłrym sesja jest zamykana.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Session(...)` | Konstruktory dla trybu serwera i klienta. |
| `uint32_t getId()` | Zwraca unikalne ID sesji. |
| `void start(...)` | Uruchamia sesjÄ™, rozpoczynajÄ…c pÄ™tlÄ™ `check` i (w trybie serwera) nasÄąâ€šuchiwanie na pakiety od klienta. |
| `void terminate(...)` | Zamyka sesjÄ™, informujÄ…c powiÄ…zane `Proxy` i klienta. |
| `void onPacket(...)` | Handler dla pakietĂłw przychodzÄ…cych **od klienta gry**. Opakowuje je w protokĂłÄąâ€š proxy i wysyÄąâ€ša. |
| `void onProxyPacket(...)` | Handler dla pakietĂłw przychodzÄ…cych **od serwerĂłw proxy**. Odpakowuje je, sprawdza kolejnoÄąâ€şÄ‡ i przekazuje do klienta gry. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   **Boost.Asio**: Fundamentalna zaleÄąÄ˝noÄąâ€şÄ‡ do wszystkich operacji sieciowych.
-   Klasy `Proxy` i `Session` sÄ… ze sobÄ… Äąâ€şciÄąâ€şle powiÄ…zane. `Session` utrzymuje zbiĂłr `Proxy`, przez ktĂłre wysyÄąâ€ša dane. `Proxy` jest Äąâ€şwiadome sesji, ktĂłre obsÄąâ€šuguje.
-   Obie klasy sÄ… zarzÄ…dzane przez `ProxyManager`.
-   W projekcie istniejÄ… globalne, dostÄ™pne w wÄ…tku `io_context` kontenery `g_sessions` i `g_proxies` do wzajemnej komunikacji.

---
# Ä‘Ĺşâ€śâ€ž proxy_client.cpp
## Opis ogĂłlny

Plik `proxy_client.cpp` zawiera implementacjÄ™ logiki dla klas `Proxy` i `Session`, ktĂłre razem tworzÄ… system klienta proxy. Kod jest w peÄąâ€šni asynchroniczny i oparty na Boost.Asio.
## Zmienne globalne

-   `g_sessions`: Globalna mapa (`std::map`) przechowujÄ…ca sÄąâ€šabe wskaÄąĹźniki (`std::weak_ptr`) do aktywnych sesji, indeksowane po ich ID.
-   `g_proxies`: Globalny zbiĂłr (`std::set`) przechowujÄ…cy wskaÄąĹźniki do aktywnych obiektĂłw `Proxy`.
-   `UID`: Unikalny identyfikator tej instancji klienta, uÄąÄ˝ywany w pakietach ping.
## Klasa `Proxy` (implementacja)
## `void Proxy::check(...)`

GÄąâ€šĂłwna metoda cyklu ÄąÄ˝ycia `Proxy`. DziaÄąâ€ša jak maszyna stanĂłw, wywoÄąâ€šywana cyklicznie przez `m_timer`.
-   W stanie `STATE_NOT_CONNECTED`, inicjuje `connect()`.
-   W stanie `STATE_CONNECTING`, sprawdza timeout dla poÄąâ€šÄ…czenia.
-   W stanie `STATE_CONNECTED`, wysyÄąâ€ša pakiety ping, jeÄąâ€şli nie oczekuje na odpowiedÄąĹź.
-   W stanie `STATE_CONNECTING_WAIT_FOR_PING`, czeka na pierwszÄ… odpowiedÄąĹź ping.
## `void Proxy::connect()`

Asynchronicznie rozwiÄ…zuje nazwÄ™ hosta, a nastÄ™pnie Äąâ€šÄ…czy siÄ™ z serwerem proxy. Po pomyÄąâ€şlnym poÄąâ€šÄ…czeniu, ustawia opcje gniazda (`no_delay`, rozmiary buforĂłw), rozpoczyna odczyt nagÄąâ€šĂłwkĂłw i wysyÄąâ€ša pierwszy ping.
## `void Proxy::disconnect()`

Zamyka gniazdo i resetuje stan do `STATE_NOT_CONNECTED`.
## `void Proxy::ping()`

WysyÄąâ€ša pakiet kontrolny "ping" do serwera proxy. Pakiet zawiera unikalne ID klienta (`UID`) i ostatni zmierzony ping.
## `void Proxy::onPing(uint32_t packetId)`

Handler odpowiedzi na ping. Oblicza nowy ping na podstawie czasu wysÄąâ€šania i odebrania pakietu. JeÄąâ€şli to byÄąâ€š pierwszy ping, zmienia stan na `STATE_CONNECTED`.
## `void Proxy::readHeader()` i `onHeader(...)`

ImplementujÄ… dwuetapowy odczyt pakietu: najpierw odczytywany jest 2-bajtowy nagÄąâ€šĂłwek z rozmiarem, a nastÄ™pnie reszta pakietu.
## `void Proxy::onPacket(...)`

Przetwarza przychodzÄ…cy pakiet. Na podstawie `sessionId` decyduje, czy jest to pakiet danych dla sesji, czy pakiet kontrolny (ping, zamkniÄ™cie sesji). Znajduje odpowiedniÄ… sesjÄ™ w `g_sessions` i przekazuje jej dane.
## `void Proxy::send(...)`

Implementuje kolejkÄ™ wysyÄąâ€šania. Dodaje pakiet do `m_sendQueue` i rozpoczyna operacjÄ™ `async_write`, jeÄąâ€şli kolejka byÄąâ€ša pusta.
## Klasa `Session` (implementacja)
## `void Session::start(int maxConnections)`

Dodaje sesjÄ™ do globalnej mapy `g_sessions`, uruchamia pÄ™tlÄ™ `check` i, w trybie serwera, rozpoczyna odczyt danych od klienta gry.
## `void Session::terminate(...)`

Zamyka sesjÄ™, informuje wszystkie powiÄ…zane `Proxy` o zamkniÄ™ciu, zamyka gniazdo (jeÄąâ€şli jest) i wywoÄąâ€šuje `callback` rozÄąâ€šÄ…czenia.
## `void Session::check(...)`

Metoda cykliczna. Sprawdza timeout braku aktywnoÄąâ€şci i wywoÄąâ€šuje `selectProxies` w celu optymalizacji routingu.
## `void Session::selectProxies()`

Inteligentny algorytm wyboru proxy.
1.  Iteruje po wszystkich globalnie dostÄ™pnych, poÄąâ€šÄ…czonych `Proxy`.
2.  Znajduje najlepsze `Proxy`, ktĂłre nie jest jeszcze uÄąÄ˝ywane przez tÄ™ sesjÄ™.
3.  JeÄąâ€şli liczba aktywnych proxy dla tej sesji jest mniejsza niÄąÄ˝ `m_maxConnections`, dodaje najlepsze znalezione `Proxy`.
4.  JeÄąâ€şli liczba jest rĂłwna `m_maxConnections`, a znalezione `Proxy` jest znacznie lepsze niÄąÄ˝ najgorsze z aktualnie uÄąÄ˝ywanych, zastÄ™puje najgorsze nowym.
5.  Po dodaniu nowego `Proxy`, wysyÄąâ€ša do niego wszystkie pakiety z kolejki `m_proxySendQueue` (pakiety, ktĂłre mogÄąâ€šy zostaÄ‡ utracone przez poprzednie `Proxy`).
## `void Session::onProxyPacket(...)`

Handler dla pakietĂłw przychodzÄ…cych od proxy.
-   Sprawdza numer sekwencyjny (`packetId`). Odrzuca stare pakiety.
-   Usuwa z `m_proxySendQueue` pakiety wychodzÄ…ce, ktĂłrych otrzymanie potwierdziÄąâ€š serwer proxy (`lastRecivedPacketId`).
-   Dodaje przychodzÄ…cy pakiet do kolejki `m_sendQueue` (ktĂłra tutaj dziaÄąâ€ša jako bufor odbiorczy do re-asemblacji).
-   JeÄąâ€şli pakiet jest tym, na ktĂłry czeka (`packetId == m_inputPacketId`), przetwarza go (i wszystkie nastÄ™pne w kolejce), wywoÄąâ€šujÄ…c `m_recvCallback` lub wysyÄąâ€šajÄ…c do klienta gry.
## `void Session::onPacket(...)`

Handler dla pakietĂłw przychodzÄ…cych od klienta gry.
1.  Generuje nowy numer sekwencyjny (`m_outputPacketId`).
2.  Opakowuje pakiet w nagÄąâ€šĂłwek protokoÄąâ€šu proxy.
3.  Dodaje opakowany pakiet do `m_proxySendQueue` (bufor do retransmisji).
4.  WysyÄąâ€ša pakiet do wszystkich aktywnych `Proxy`.

---
# Ä‘Ĺşâ€śâ€ž combinedsoundsource.cpp
## Opis ogĂłlny

Plik `combinedsoundsource.cpp` zawiera implementacjÄ™ klasy `CombinedSoundSource`, ktĂłra jest specjalnym rodzajem ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku.
## Klasa `CombinedSoundSource`
## Opis semantyczny
`CombinedSoundSource` dziaÄąâ€ša jak kontener na wiele innych obiektĂłw `SoundSource`. Wszystkie operacje wykonane na `CombinedSoundSource` (np. `play()`, `stop()`, `setGain()`) sÄ… delegowane i wykonywane na kaÄąÄ˝dym z podrzÄ™dnych ÄąĹźrĂłdeÄąâ€š dÄąĹźwiÄ™ku, ktĂłre przechowuje. Jest to uÄąÄ˝yteczne do tworzenia zÄąâ€šoÄąÄ˝onych efektĂłw dÄąĹźwiÄ™kowych lub do implementacji obejÄąâ€şÄ‡ (workarounds), jak w przypadku problemu z dÄąĹźwiÄ™kiem stereo na Linuksie (gdzie dÄąĹźwiÄ™k stereo jest symulowany przez dwa ÄąĹźrĂłdÄąâ€ša mono).
## `CombinedSoundSource::CombinedSoundSource()`

Konstruktor. WywoÄąâ€šuje konstruktor klasy bazowej `SoundSource` z ID 0, poniewaÄąÄ˝ sam nie reprezentuje rzeczywistego ÄąĹźrĂłdÄąâ€ša w OpenAL.
## `void CombinedSoundSource::addSource(const SoundSourcePtr& source)`

Dodaje nowe podrzÄ™dne ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku do wewnÄ™trznego wektora `m_sources`.
## Metody operacyjne (`play`, `stop`, `setLooping`, `setGain`, etc.)

KaÄąÄ˝da z tych metod jest prostÄ… pÄ™tlÄ…, ktĂłra iteruje po wektorze `m_sources` i wywoÄąâ€šuje odpowiedniÄ… metodÄ™ na kaÄąÄ˝dym z podrzÄ™dnych obiektĂłw `SoundSource`.

`$fenceInfo
void CombinedSoundSource::play()
{
    for(const SoundSourcePtr& source : m_sources)
        source->play();
}

void CombinedSoundSource::setGain(float gain)
{
    for(const SoundSourcePtr& source : m_sources)
        source->setGain(gain);
}
// ... i tak dalej
```
## Metody sprawdzajÄ…ce stan (`isBuffering`, `isPlaying`)

ZwracajÄ… `true`, jeÄąâ€şli **ktĂłrekolwiek** z podrzÄ™dnych ÄąĹźrĂłdeÄąâ€š speÄąâ€šnia dany warunek.

`$fenceInfo
bool CombinedSoundSource::isPlaying()
{
    for(const SoundSourcePtr& source : m_sources) {
        if(source->isPlaying())
            return true;
}
    return false;
}
```
## `void CombinedSoundSource::update()`

Metoda wywoÄąâ€šywana w pÄ™tli `SoundManager::poll()`. WywoÄąâ€šuje `update()` na wszystkich podrzÄ™dnych ÄąĹźrĂłdÄąâ€šach, co jest potrzebne np. do obsÄąâ€šugi pÄąâ€šynnego wyciszania/zgÄąâ€šaÄąâ€şniania (fading).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/combinedsoundsource.h`: Plik nagÄąâ€šĂłwkowy.
-   UÄąÄ˝ywana w `SoundManager` jako obejÄąâ€şcie problemu z dÄąĹźwiÄ™kiem stereo na Linuksie.

---
# Ä‘Ĺşâ€śâ€ž combinedsoundsource.h
## Opis ogĂłlny

Plik `combinedsoundsource.h` deklaruje klasÄ™ `CombinedSoundSource`, ktĂłra jest kompozytem wielu ÄąĹźrĂłdeÄąâ€š dÄąĹźwiÄ™ku, zachowujÄ…cym siÄ™ jak jedno.
## Klasa `CombinedSoundSource`
## Opis semantyczny
`CombinedSoundSource` implementuje wzorzec projektowy "Kompozyt". Pozwala traktowaÄ‡ grupÄ™ obiektĂłw `SoundSource` w ten sam sposĂłb, co pojedynczy obiekt. Wszystkie operacje sÄ… delegowane do wewnÄ™trznej kolekcji ÄąĹźrĂłdeÄąâ€š. Dziedziczy po `SoundSource`, aby zachowaÄ‡ zgodnoÄąâ€şÄ‡ interfejsu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CombinedSoundSource()` | Konstruktor. |
| `void addSource(...)` | Dodaje podrzÄ™dne ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku. |
| `std::vector<...> getSources()` | Zwraca listÄ™ podrzÄ™dnych ÄąĹźrĂłdeÄąâ€š. |
| `play()`, `stop()`, `setLooping()`, `setGain()`, `setPosition()`, etc. | Metody delegujÄ…ce operacje do wszystkich podrzÄ™dnych ÄąĹźrĂłdeÄąâ€š. |
| `isBuffering()`, `isPlaying()` | SprawdzajÄ… stan, zwracajÄ…c `true`, jeÄąâ€şli co najmniej jedno podrzÄ™dne ÄąĹźrĂłdÄąâ€šo jest w danym stanie. |
## Metody chronione

-   `virtual void update()`: PrzesÄąâ€šania metodÄ™ z `SoundSource` i wywoÄąâ€šuje `update()` na wszystkich dzieciach.
## Zmienne prywatne

-   `m_sources`: Wektor (`std::vector`) przechowujÄ…cy wskaÄąĹźniki na podrzÄ™dne obiekty `SoundSource`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundsource.h`: Klasa bazowa i typ przechowywanych obiektĂłw.
-   Jest tworzona i uÄąÄ˝ywana przez `SoundManager`.

---
# Ä‘Ĺşâ€śâ€ž oggsoundfile.cpp
## Opis ogĂłlny

Plik `oggsoundfile.cpp` zawiera implementacjÄ™ klasy `OggSoundFile`, ktĂłra jest odpowiedzialna za odczytywanie i dekodowanie plikĂłw dÄąĹźwiÄ™kowych w formacie Ogg Vorbis.
## Klasa `OggSoundFile`
## `OggSoundFile::OggSoundFile(const FileStreamPtr& fileStream)`

Konstruktor. WywoÄąâ€šuje konstruktor klasy bazowej `SoundFile`.
## `OggSoundFile::~OggSoundFile()`

Destruktor. Zwalnia zasoby zwiÄ…zane z bibliotekÄ… Vorbis, wywoÄąâ€šujÄ…c `ov_clear()`.
## `bool OggSoundFile::prepareOgg()`
## Opis semantyczny
Inicjalizuje proces dekodowania pliku Ogg Vorbis.
## DziaÄąâ€šanie
1.  Tworzy strukturÄ™ `ov_callbacks` z wskaÄąĹźnikami na statyczne metody `cb_...`, ktĂłre bÄ™dÄ… uÄąÄ˝ywane przez bibliotekÄ™ Vorbis do odczytu danych ze strumienia `FileStream`.
2.  WywoÄąâ€šuje `ov_open_callbacks`, przekazujÄ…c `FileStream` jako ÄąĹźrĂłdÄąâ€šo danych.
3.  Pobiera informacje o pliku (liczba kanaÄąâ€šĂłw, czÄ™stotliwoÄąâ€şÄ‡ prĂłbkowania) za pomocÄ… `ov_info`.
4.  Zapisuje te informacje w polach klasy bazowej (`m_channels`, `m_rate`).
5.  Oblicza caÄąâ€škowity rozmiar zdekompresowanych danych za pomocÄ… `ov_pcm_total`.
## `int OggSoundFile::read(void *buffer, int bufferSize)`

Odczytuje i dekoduje fragment pliku dÄąĹźwiÄ™kowego do podanego bufora. WywoÄąâ€šuje `ov_read`, ktĂłra wykonuje caÄąâ€šÄ… pracÄ™ zwiÄ…zanÄ… z dekodowaniem.
## `void OggSoundFile::reset()`

Przewija strumieÄąâ€ž dÄąĹźwiÄ™kowy na poczÄ…tek za pomocÄ… `ov_pcm_seek()`.
## Statyczne metody `cb_...`

SÄ… to funkcje zwrotne (callbacks) C, ktĂłre opakowujÄ… metody obiektu `FileStream`, tÄąâ€šumaczÄ…c interfejs wymagany przez `libvorbisfile` na interfejs `FileStream`.
-   `cb_read`: opakowuje `file->read()`
-   `cb_seek`: opakowuje `file->seek()`
-   `cb_close`: opakowuje `file->close()`
-   `cb_tell`: opakowuje `file->tell()`
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/oggsoundfile.h`: Plik nagÄąâ€šĂłwkowy.
-   **libvorbisfile**: Kluczowa zaleÄąÄ˝noÄąâ€şÄ‡ do dekodowania plikĂłw Ogg Vorbis.
-   Jest tworzona przez `SoundFile::loadSoundFile`, gdy wykryty zostanie plik w formacie Ogg.

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## Opis ogĂłlny

Plik `declarations.h` w module `sound` sÄąâ€šuÄąÄ˝y do wczesnych deklaracji klas i definicji typĂłw wskaÄąĹźnikĂłw zwiÄ…zanych z systemem dÄąĹźwiÄ™ku. Jest on kompilowany tylko wtedy, gdy zdefiniowano flagÄ™ `FW_SOUND`.
## Wczesne deklaracje

-   `SoundManager`
-   `SoundSource`
-   `SoundBuffer`
-   `SoundFile`
-   `SoundChannel`
-   `StreamSoundSource`
-   `CombinedSoundSource`
-   `OggSoundFile`
## Definicje typĂłw

-   `SoundSourcePtr`
-   `SoundFilePtr`
-   `SoundBufferPtr`
-   `SoundChannelPtr`
-   `StreamSoundSourcePtr`
-   `CombinedSoundSourcePtr`
-   `OggSoundFilePtr`
## DoÄąâ€šÄ…czanie nagÄąâ€šĂłwkĂłw OpenAL

Plik doÄąâ€šÄ…cza nagÄąâ€šĂłwki biblioteki OpenAL (`al.h`, `alc.h`), ktĂłra jest podstawÄ… caÄąâ€šego systemu dÄąĹźwiÄ™ku.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doÄąâ€šÄ…czany przez wszystkie pliki nagÄąâ€šĂłwkowe w module `sound`.

---
# Ä‘Ĺşâ€śâ€ž oggsoundfile.h
## Opis ogĂłlny

Plik `oggsoundfile.h` deklaruje klasÄ™ `OggSoundFile`, ktĂłra jest konkretnÄ… implementacjÄ… `SoundFile` do obsÄąâ€šugi plikĂłw w formacie Ogg Vorbis.
## Klasa `OggSoundFile`
## Opis semantyczny
`OggSoundFile` dziedziczy po `SoundFile` i implementuje jej wirtualne metody, uÄąÄ˝ywajÄ…c biblioteki `libvorbisfile` do dekodowania danych. Enkapsuluje ona strukturÄ™ `OggVorbis_File` i dostarcza `callbacki` C, ktĂłre pozwalajÄ… bibliotece Vorbis na odczyt danych ze strumienia `FileStream`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OggSoundFile(...)` | Konstruktor. |
| `virtual ~OggSoundFile()` | Destruktor. |
| `bool prepareOgg()` | Inicjalizuje dekoder Vorbis i odczytuje metadane pliku. |
| `int read(...)` | Odczytuje i dekoduje fragment danych. |
| `void reset()` | Przewija strumieÄąâ€ž na poczÄ…tek. |
## Metody prywatne (statyczne)

-   `cb_read`, `cb_seek`, `cb_close`, `cb_tell`: Statyczne funkcje zwrotne dla `libvorbisfile`.
## Zmienne prywatne

-   `m_vorbisFile`: Uchwyt do struktur `libvorbisfile`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundfile.h`: Klasa bazowa.
-   `vorbis/vorbisfile.h`: NagÄąâ€šĂłwek biblioteki Vorbis.
-   Jest tworzona przez `SoundFile::loadSoundFile`.

---
# Ä‘Ĺşâ€śâ€ž soundbuffer.cpp
## Opis ogĂłlny

Plik `soundbuffer.cpp` zawiera implementacjÄ™ klasy `SoundBuffer`, ktĂłra jest opakowaniem na bufor audio w OpenAL.
## Klasa `SoundBuffer`
## Opis semantyczny
`SoundBuffer` reprezentuje blok danych audio (prĂłbek dÄąĹźwiÄ™kowych) zaÄąâ€šadowany do pamiÄ™ci, gotowy do odtworzenia przez OpenAL. KaÄąÄ˝dy `SoundBuffer` ma unikalne ID w OpenAL. Jest uÄąÄ˝ywany do przechowywania krĂłtkich, czÄ™sto odtwarzanych dÄąĹźwiÄ™kĂłw, ktĂłre opÄąâ€šaca siÄ™ trzymaÄ‡ w pamiÄ™ci.
## `SoundBuffer::SoundBuffer()`

Konstruktor. Generuje nowy bufor OpenAL za pomocÄ… `alGenBuffers()` i zapisuje jego ID.
## `SoundBuffer::~SoundBuffer()`

Destruktor. Zwalnia bufor OpenAL za pomocÄ… `alDeleteBuffers()`.
## `bool SoundBuffer::fillBuffer(const SoundFilePtr& soundFile)`

WypeÄąâ€šnia bufor danymi z obiektu `SoundFile`.
1.  Pobiera format, rozmiar i czÄ™stotliwoÄąâ€şÄ‡ prĂłbkowania z `soundFile`.
2.  Odczytuje caÄąâ€šÄ… zawartoÄąâ€şÄ‡ pliku dÄąĹźwiÄ™kowego do tymczasowego bufora w RAM.
3.  WywoÄąâ€šuje drugÄ… wersjÄ™ `fillBuffer` w celu przesÄąâ€šania danych do OpenAL.
## `bool SoundBuffer::fillBuffer(ALenum sampleFormat, const DataBuffer<char>& data, int size, int rate)`

PrzesyÄąâ€ša surowe dane prĂłbek dÄąĹźwiÄ™kowych do bufora OpenAL za pomocÄ… `alBufferData()`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundbuffer.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/sound/soundfile.h`: Do pobierania danych z plikĂłw.
-   Jest tworzona i zarzÄ…dzana przez `SoundManager`, ktĂłry przechowuje je w cache.
-   Jest uÄąÄ˝ywana przez `SoundSource` jako ÄąĹźrĂłdÄąâ€šo danych do odtwarzania.

---
# Ä‘Ĺşâ€śâ€ž soundbuffer.h
## Opis ogĂłlny

Plik `soundbuffer.h` deklaruje klasÄ™ `SoundBuffer`, ktĂłra jest opakowaniem na bufor audio OpenAL.
## Klasa `SoundBuffer`
## Opis semantyczny
`SoundBuffer` enkapsuluje ID bufora OpenAL i dostarcza metody do wypeÄąâ€šniania go danymi dÄąĹźwiÄ™kowymi. Jest to obiekt przechowujÄ…cy dane audio, ktĂłry moÄąÄ˝e byÄ‡ nastÄ™pnie przypisany do jednego lub wielu `SoundSource` w celu odtwarzania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundBuffer()` / `~SoundBuffer()` | Konstruktor i destruktor zarzÄ…dzajÄ…ce zasobem OpenAL. |
| `bool fillBuffer(const SoundFilePtr& soundFile)` | WypeÄąâ€šnia bufor danymi z pliku dÄąĹźwiÄ™kowego. |
| `bool fillBuffer(...)` | WypeÄąâ€šnia bufor surowymi danymi z pamiÄ™ci. |
| `uint getBufferId()` | Zwraca ID bufora w OpenAL. |
## Zmienne prywatne

-   `m_bufferId`: ID (uchwyt) bufora w OpenAL.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/declarations.h`: Definicje typĂłw.
-   `framework/util/databuffer.h`: Do pracy z buforami danych.
-   Jest tworzona i zarzÄ…dzana przez `SoundManager`.

---
# Ä‘Ĺşâ€śâ€ž soundfile.cpp
## Opis ogĂłlny

Plik `soundfile.cpp` zawiera implementacjÄ™ klasy `SoundFile`, ktĂłra jest abstrakcyjnÄ… klasÄ… bazowÄ… do odczytu rĂłÄąÄ˝nych formatĂłw plikĂłw dÄąĹźwiÄ™kowych.
## Klasa `SoundFile`
## `SoundFile::SoundFile(const FileStreamPtr& fileStream)`

Konstruktor. Zapisuje wskaÄąĹźnik do strumienia pliku.
## `SoundFilePtr SoundFile::loadSoundFile(const std::string& filename)`
## Opis semantyczny
Statyczna metoda fabryczna, ktĂłra prĂłbuje zaÄąâ€šadowaÄ‡ plik dÄąĹźwiÄ™kowy. Automatycznie wykrywa format pliku i tworzy odpowiedniÄ… podklasÄ™ `SoundFile`.
## DziaÄąâ€šanie
1.  Otwiera plik za pomocÄ… `g_resources.openFile()`.
2.  Odczytuje pierwsze 4 bajty ("magiczne bajty"), aby zidentyfikowaÄ‡ format.
3.  JeÄąâ€şli plik to Ogg Vorbis (zaczyna siÄ™ od "OggS"), tworzy instancjÄ™ `OggSoundFile` i wywoÄąâ€šuje jej metodÄ™ `prepareOgg()`.
4.  W przypadku nieznanego formatu rzuca wyjÄ…tek.
## `ALenum SoundFile::getSampleFormat()`

Konwertuje wewnÄ™trzne informacje o liczbie kanaÄąâ€šĂłw i bitach na sekundÄ™ na format zrozumiaÄąâ€šy dla OpenAL (np. `AL_FORMAT_STEREO16`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundfile.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/sound/oggsoundfile.h`: Implementacja dla formatu Ogg.
-   `framework/core/resourcemanager.h`: Do otwierania plikĂłw.
-   Jest uÄąÄ˝ywana przez `SoundBuffer` i `StreamSoundSource` jako ÄąĹźrĂłdÄąâ€šo danych audio.

---
# Ä‘Ĺşâ€śâ€ž soundchannel.cpp
## Opis ogĂłlny

Plik `soundchannel.cpp` zawiera implementacjÄ™ klasy `SoundChannel`, ktĂłra reprezentuje kanaÄąâ€š dÄąĹźwiÄ™kowy, umoÄąÄ˝liwiajÄ…cy odtwarzanie dÄąĹźwiÄ™kĂłw w sposĂłb zorganizowany i kontrolowany.
## Klasa `SoundChannel`
## `SoundSourcePtr SoundChannel::play(...)`

Odtwarza nowy dÄąĹźwiÄ™k na tym kanale. JeÄąâ€şli inny dÄąĹźwiÄ™k jest juÄąÄ˝ odtwarzany, zostaje on zatrzymany. WywoÄąâ€šuje `g_sounds.play`, aby utworzyÄ‡ i uruchomiÄ‡ nowe ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku.
## `void SoundChannel::stop(float fadetime)`

Zatrzymuje bieÄąÄ˝Ä…cy dÄąĹźwiÄ™k i czyÄąâ€şci kolejkÄ™. Opcjonalnie moÄąÄ˝e to zrobiÄ‡ z efektem wyciszania (`fadetime`).
## `void SoundChannel::enqueue(...)`

Dodaje plik dÄąĹźwiÄ™kowy do kolejki odtwarzania. Gdy bieÄąÄ˝Ä…cy dÄąĹźwiÄ™k siÄ™ skoÄąâ€žczy, `update()` automatycznie odtworzy nastÄ™pny z kolejki. Kolejka jest tasowana, aby zapewniÄ‡ losowÄ… kolejnoÄąâ€şÄ‡ odtwarzania.
## `void SoundChannel::update()`

Metoda wywoÄąâ€šywana cyklicznie przez `SoundManager`.
-   Sprawdza, czy bieÄąÄ˝Ä…ce ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku zakoÄąâ€žczyÄąâ€šo odtwarzanie. JeÄąâ€şli tak, zwalnia je.
-   JeÄąâ€şli nie ma bieÄąÄ˝Ä…cego ÄąĹźrĂłdÄąâ€ša, a kolejka nie jest pusta, pobiera nastÄ™pny utwĂłr z kolejki i go odtwarza.
## `void SoundChannel::setEnabled(bool enable)`

WÄąâ€šÄ…cza lub wyÄąâ€šÄ…cza kanaÄąâ€š. WyÄąâ€šÄ…czenie kanaÄąâ€šu natychmiast zatrzymuje odtwarzany dÄąĹźwiÄ™k i zapobiega odtwarzaniu nowych.
## `void SoundChannel::setGain(float gain)`

Ustawia ogĂłlnÄ… gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡ dla kanaÄąâ€šu. GÄąâ€šoÄąâ€şnoÄąâ€şÄ‡ ta jest mnoÄąÄ˝ona przez gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡ poszczegĂłlnych dÄąĹźwiÄ™kĂłw odtwarzanych na tym kanale.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundchannel.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/sound/streamsoundsource.h`: UÄąÄ˝ywane do efektĂłw wyciszania.
-   `framework/sound/soundmanager.h`: UÄąÄ˝ywa `g_sounds` do tworzenia ÄąĹźrĂłdeÄąâ€š dÄąĹźwiÄ™ku.
-   Jest tworzona i zarzÄ…dzana przez `SoundManager`.

---
# Ä‘Ĺşâ€śâ€ž soundchannel.h
## Opis ogĂłlny

Plik `soundchannel.h` deklaruje klasÄ™ `SoundChannel`, ktĂłra reprezentuje logiczny kanaÄąâ€š audio.
## Klasa `SoundChannel`
## Opis semantyczny
`SoundChannel` pozwala na grupowanie i zarzÄ…dzanie odtwarzaniem dÄąĹźwiÄ™kĂłw. KaÄąÄ˝dy kanaÄąâ€š moÄąÄ˝e odtwarzaÄ‡ tylko jeden dÄąĹźwiÄ™k naraz, ale posiada kolejkÄ™, ktĂłra pozwala na automatyczne odtwarzanie kolejnych utworĂłw. UmoÄąÄ˝liwia globalnÄ… kontrolÄ™ nad grupÄ… dÄąĹźwiÄ™kĂłw, np. ustawienie gÄąâ€šoÄąâ€şnoÄąâ€şci dla caÄąâ€šej muzyki w grze.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundChannel(int id)` | Konstruktor. |
| `SoundSourcePtr play(...)`| Odtwarza dÄąĹźwiÄ™k na tym kanale, przerywajÄ…c poprzedni. |
| `void stop(...)` | Zatrzymuje odtwarzanie i czyÄąâ€şci kolejkÄ™. |
| `void enqueue(...)` | Dodaje dÄąĹźwiÄ™k do kolejki odtwarzania. |
| `void enable()` / `disable()` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza kanaÄąâ€š. |
| `void setGain(float gain)` | Ustawia gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡ kanaÄąâ€šu. |
| `float getGain()` | Zwraca gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡ kanaÄąâ€šu. |
| `bool isEnabled()` | Sprawdza, czy kanaÄąâ€š jest wÄąâ€šÄ…czony. |
| `int getId()` | Zwraca ID kanaÄąâ€šu. |
## Metody chronione

-   `void update()`: Metoda cykliczna do zarzÄ…dzania kolejkÄ….
## Zmienne prywatne

-   `m_queue`: Kolejka (`std::deque`) utworĂłw do odtworzenia.
-   `m_currentSource`: WskaÄąĹźnik na aktualnie odtwarzane ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku.
-   `m_enabled`: Flaga wÄąâ€šÄ…czenia kanaÄąâ€šu.
-   `m_id`: ID kanaÄąâ€šu.
-   `m_gain`: GÄąâ€šoÄąâ€şnoÄąâ€şÄ‡ kanaÄąâ€šu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundsource.h`: UÄąÄ˝ywa `SoundSourcePtr`.
-   Jest oznaczona jako `@bindclass`, co udostÄ™pnia jej API w Lua.
-   Jest tworzona i zarzÄ…dzana przez `SoundManager`.

---
# Ä‘Ĺşâ€śâ€ž soundfile.h
## Opis ogĂłlny

Plik `soundfile.h` deklaruje abstrakcyjnÄ… klasÄ™ bazowÄ… `SoundFile`, ktĂłra definiuje wspĂłlny interfejs do odczytu danych z rĂłÄąÄ˝nych formatĂłw plikĂłw dÄąĹźwiÄ™kowych.
## Klasa `SoundFile`
## Opis semantyczny
`SoundFile` jest abstrakcjÄ… nad plikiem dÄąĹźwiÄ™kowym. Ukrywa szczegĂłÄąâ€šy konkretnego formatu (np. Ogg, WAV), dostarczajÄ…c ujednolicony sposĂłb na odczytywanie zdekompresowanych prĂłbek audio.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundFile(...)` | Konstruktor. |
| `static SoundFilePtr loadSoundFile(...)`| Statyczna metoda fabryczna, ktĂłra wykrywa format pliku i tworzy odpowiedniÄ… podklasÄ™. |
| `virtual int read(...) = 0` | Czysto wirtualna metoda do odczytu zdekompresowanych danych. |
| `virtual void reset() = 0` | Czysto wirtualna metoda do przewiniÄ™cia strumienia na poczÄ…tek. |
| `bool eof()` | Sprawdza, czy osiÄ…gniÄ™to koniec pliku. |
| `ALenum getSampleFormat()` | Konwertuje format (kanaÄąâ€šy, bity) na format OpenAL. |
| `getChannels()`, `getRate()`, `getBpp()`, `getSize()`, `getName()`| Gettery dla metadanych pliku. |
## Zmienne chronione

-   `m_file`: WskaÄąĹźnik na `FileStream`, z ktĂłrego odczytywane sÄ… dane.
-   `m_channels`, `m_rate`, `m_bps`, `m_size`: Metadane dÄąĹźwiÄ™ku.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/declarations.h`: Deklaracje.
-   `framework/core/filestream.h`: UÄąÄ˝ywa `FileStream` jako ÄąĹźrĂłdÄąâ€ša danych.
-   Jest klasÄ… bazowÄ… dla `OggSoundFile` i potencjalnie innych klas dla rĂłÄąÄ˝nych formatĂłw.

---
# Ä‘Ĺşâ€śâ€ž soundmanager.cpp
## Opis ogĂłlny

Plik `soundmanager.cpp` zawiera implementacjÄ™ klasy `SoundManager`, ktĂłra jest singletonem (`g_sounds`) i centralnym punktem zarzÄ…dzania caÄąâ€šym podsystemem dÄąĹźwiÄ™ku.
## Zmienne globalne
## `g_sounds`

Globalna instancja `SoundManager`.
## Klasa `SoundManager`
## `void SoundManager::init()`

Inicjalizuje system dÄąĹźwiÄ™ku.
1.  Otwiera domyÄąâ€şlne urzÄ…dzenie audio za pomocÄ… `alcOpenDevice`.
2.  Tworzy kontekst OpenAL za pomocÄ… `alcCreateContext`.
3.  Ustawia ten kontekst jako aktywny za pomocÄ… `alcMakeContextCurrent`.
## `void SoundManager::terminate()`

Zamyka system dÄąĹźwiÄ™ku. Zwalnia wszystkie zasoby (ÄąĹźrĂłdÄąâ€ša, bufory, kanaÄąâ€šy), niszczy kontekst i zamyka urzÄ…dzenie audio.
## `void SoundManager::poll()`

Metoda wywoÄąâ€šywana cyklicznie w gÄąâ€šĂłwnej pÄ™tli aplikacji.
-   Aktualizuje wszystkie aktywne ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku (`m_sources`).
-   Aktualizuje wszystkie kanaÄąâ€šy dÄąĹźwiÄ™kowe (`m_channels`), co pozwala na zarzÄ…dzanie kolejkami odtwarzania.
-   Przetwarza asynchronicznie Äąâ€šadowane pliki dÄąĹźwiÄ™kowe.
## `void SoundManager::setAudioEnabled(bool enable)`

Globalnie wÄąâ€šÄ…cza lub wyÄąâ€šÄ…cza dÄąĹźwiÄ™k. WyÄąâ€šÄ…czenie powoduje zatrzymanie wszystkich odtwarzanych dÄąĹźwiÄ™kĂłw.
## `void SoundManager::preload(std::string filename)`

ÄąÂaduje plik dÄąĹźwiÄ™kowy do pamiÄ™ci i tworzy z niego `SoundBuffer`. Jest to optymalizacja dla krĂłtkich, czÄ™sto uÄąÄ˝ywanych dÄąĹźwiÄ™kĂłw. Bufor jest przechowywany w cache (`m_buffers`).
## `SoundSourcePtr SoundManager::play(...)`

GÄąâ€šĂłwna metoda do odtwarzania dÄąĹźwiÄ™ku.
1.  Tworzy odpowiednie ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku (`SoundSource` dla skeszowanych plikĂłw lub `StreamSoundSource` dla strumieniowanych).
2.  Ustawia jego parametry (gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡, fadetime).
3.  Rozpoczyna odtwarzanie i dodaje ÄąĹźrĂłdÄąâ€šo do listy aktywnych ÄąĹźrĂłdeÄąâ€š.
## `SoundChannelPtr SoundManager::getChannel(int channel)`

Zwraca obiekt kanaÄąâ€šu o danym ID. JeÄąâ€şli kanaÄąâ€š nie istnieje, jest tworzony.
## `SoundSourcePtr SoundManager::createSoundSource(...)`

Metoda pomocnicza, ktĂłra decyduje, czy utworzyÄ‡ `SoundSource` (z bufora) czy `StreamSoundSource` (strumieniowanie z pliku). Dla Linuksa implementuje obejÄąâ€şcie problemu z dÄąĹźwiÄ™kiem stereo, tworzÄ…c `CombinedSoundSource` z dwoma ÄąĹźrĂłdÄąâ€šami mono.
## `void SoundManager::ensureContext()`

Upewnia siÄ™, ÄąÄ˝e kontekst OpenAL jest aktywny w bieÄąÄ˝Ä…cym wÄ…tku.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   **OpenAL**: Podstawowa biblioteka do obsÄąâ€šugi dÄąĹźwiÄ™ku.
-   WspĂłÄąâ€špracuje ze wszystkimi klasami z moduÄąâ€šu `sound`.
-   `framework/core/asyncdispatcher.h`: UÄąÄ˝ywany do asynchronicznego Äąâ€šadowania plikĂłw dÄąĹźwiÄ™kowych.

---
# Ä‘Ĺşâ€śâ€ž soundmanager.h
## Opis ogĂłlny

Plik `soundmanager.h` deklaruje klasÄ™ `SoundManager`, ktĂłra jest singletonem (`g_sounds`) zarzÄ…dzajÄ…cym caÄąâ€šym systemem dÄąĹźwiÄ™ku w aplikacji.
## Klasa `SoundManager`
## Opis semantyczny
`SoundManager` jest centralnym interfejsem do odtwarzania dÄąĹźwiÄ™kĂłw. Odpowiada za inicjalizacjÄ™ i zamykanie OpenAL, zarzÄ…dzanie ÄąĹźrĂłdÄąâ€šami dÄąĹźwiÄ™ku (`SoundSource`), buforami (`SoundBuffer`) i kanaÄąâ€šami (`SoundChannel`). Posiada mechanizm cachowania dla maÄąâ€šych plikĂłw dÄąĹźwiÄ™kowych i strumieniowania dla wiÄ™kszych.
## StaÄąâ€še

-   `MAX_CACHE_SIZE`: Maksymalny rozmiar pliku (w bajtach), ktĂłry bÄ™dzie cachowany w pamiÄ™ci.
-   `POLL_DELAY`: Minimalny interwaÄąâ€š (w ms) miÄ™dzy wywoÄąâ€šaniami `poll()`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | InicjalizujÄ… i zamykajÄ… system dÄąĹźwiÄ™ku. |
| `poll()` | Aktualizuje stan wszystkich aktywnych ÄąĹźrĂłdeÄąâ€š i kanaÄąâ€šĂłw. |
| `setAudioEnabled(...)`, `enableAudio()`, `disableAudio()` | Globalnie wÄąâ€šÄ…czajÄ…/wyÄąâ€šÄ…czajÄ… dÄąĹźwiÄ™k. |
| `stopAll()` | Zatrzymuje wszystkie odtwarzane dÄąĹźwiÄ™ki. |
| `void preload(...)` | ÄąÂaduje dÄąĹźwiÄ™k do pamiÄ™ci podrÄ™cznej. |
| `SoundSourcePtr play(...)` | Odtwarza dÄąĹźwiÄ™k z pliku. |
| `SoundChannelPtr getChannel(...)` | Pobiera lub tworzy kanaÄąâ€š dÄąĹźwiÄ™kowy. |
| `std::string resolveSoundFile(...)` | RozwiÄ…zuje Äąâ€şcieÄąÄ˝kÄ™ do pliku dÄąĹźwiÄ™kowego. |
| `void ensureContext()` | Upewnia siÄ™, ÄąÄ˝e kontekst OpenAL jest aktywny. |
## Zmienne prywatne

-   `m_device`, `m_context`: Uchwyty do urzÄ…dzenia i kontekstu OpenAL.
-   `m_streamFiles`: Mapa do zarzÄ…dzania asynchronicznym Äąâ€šadowaniem plikĂłw strumieniowanych.
-   `m_buffers`: Cache dla `SoundBuffer`.
-   `m_sources`: Lista aktywnych ÄąĹźrĂłdeÄąâ€š dÄąĹźwiÄ™ku.
-   `m_audioEnabled`: Globalna flaga wÄąâ€šÄ…czenia dÄąĹźwiÄ™ku.
-   `m_channels`: Mapa kanaÄąâ€šĂłw dÄąĹźwiÄ™kowych.
## Zmienne globalne

-   `g_sounds`: Globalna instancja `SoundManager`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/declarations.h`, `soundchannel.h`.
-   Oznaczona jako `@bindsingleton g_sounds`, udostÄ™pnia swoje API w Lua.

---
# Ä‘Ĺşâ€śâ€ž soundsource.cpp
## Opis ogĂłlny

Plik `soundsource.cpp` zawiera implementacjÄ™ klasy `SoundSource`, ktĂłra jest opakowaniem na ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku w OpenAL.
## Klasa `SoundSource`
## `SoundSource::SoundSource()`

Konstruktor. Generuje nowe ÄąĹźrĂłdÄąâ€šo w OpenAL za pomocÄ… `alGenSources()` i ustawia domyÄąâ€şlne parametry, takie jak dystans referencyjny.
## `SoundSource::~SoundSource()`

Destruktor. Zatrzymuje odtwarzanie i zwalnia zasĂłb ÄąĹźrĂłdÄąâ€ša w OpenAL za pomocÄ… `alDeleteSources()`.
## `void SoundSource::play()`

Rozpoczyna odtwarzanie dÄąĹźwiÄ™ku za pomocÄ… `alSourcePlay()`.
## `void SoundSource::stop()`

Zatrzymuje odtwarzanie (`alSourceStop()`) i odÄąâ€šÄ…cza bufor od ÄąĹźrĂłdÄąâ€ša.
## `bool SoundSource::isBuffering()`

Sprawdza, czy ÄąĹźrĂłdÄąâ€šo jest w stanie innym niÄąÄ˝ `AL_STOPPED` (czyli `AL_PLAYING` lub `AL_PAUSED`).
## Metody `set...()`

SÄ… to opakowania na funkcje `alSource...()`, ktĂłre ustawiajÄ… rĂłÄąÄ˝ne wÄąâ€šaÄąâ€şciwoÄąâ€şci ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku:
-   `setBuffer`: Przypisuje `SoundBuffer` do ÄąĹźrĂłdÄąâ€ša.
-   `setLooping`: Ustawia zapÄ™tlanie.
-   `setRelative`: Ustawia, czy pozycja ÄąĹźrĂłdÄąâ€ša jest wzglÄ™dna do sÄąâ€šuchacza.
-   `setGain`: Ustawia gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡.
-   `setPitch`: Ustawia wysokoÄąâ€şÄ‡ dÄąĹźwiÄ™ku.
-   `setPosition`, `setVelocity`: UstawiajÄ… wÄąâ€šaÄąâ€şciwoÄąâ€şci 3D dÄąĹźwiÄ™ku.
## `void SoundSource::setFading(...)`

Inicjuje proces pÄąâ€šynnego zgÄąâ€šaÄąâ€şniania (`FadingOn`) lub wyciszania (`FadingOff`) dÄąĹźwiÄ™ku w okreÄąâ€şlonym czasie. Zapisuje stan i czas rozpoczÄ™cia.
## `void SoundSource::update()`

Metoda wywoÄąâ€šywana cyklicznie przez `SoundManager`. Implementuje logikÄ™ "fadingu", aktualizujÄ…c gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡ ÄąĹźrĂłdÄąâ€ša w kaÄąÄ˝dej klatce na podstawie upÄąâ€šywajÄ…cego czasu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundsource.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/sound/soundbuffer.h`: UÄąÄ˝ywa `SoundBuffer` jako ÄąĹźrĂłdÄąâ€ša danych.
-   `framework/core/clock.h`: Do obsÄąâ€šugi czasu w mechanizmie "fading".

---
# Ä‘Ĺşâ€śâ€ž streamsoundsource.cpp
## Opis ogĂłlny

Plik `streamsoundsource.cpp` zawiera implementacjÄ™ klasy `StreamSoundSource`, ktĂłra jest specjalizacjÄ… `SoundSource` do odtwarzania dÄąĹźwiÄ™kĂłw strumieniowo z plikĂłw.
## Klasa `StreamSoundSource`
## Opis semantyczny
`StreamSoundSource` jest przeznaczona do odtwarzania dÄąâ€šugich plikĂłw dÄąĹźwiÄ™kowych (np. muzyki), ktĂłre nie sÄ… w caÄąâ€šoÄąâ€şci Äąâ€šadowane do pamiÄ™ci. Zamiast tego, uÄąÄ˝ywa mechanizmu kolejkowania maÄąâ€šych buforĂłw w OpenAL. Dane sÄ… odczytywane z pliku i dekodowane w locie, a nastÄ™pnie umieszczane w buforach, ktĂłre sÄ… dodawane do kolejki odtwarzania ÄąĹźrĂłdÄąâ€ša.
## `StreamSoundSource::StreamSoundSource()`

Konstruktor. Tworzy `STREAM_FRAGMENTS` (zwykle 4) maÄąâ€šych obiektĂłw `SoundBuffer`, ktĂłre bÄ™dÄ… uÄąÄ˝ywane do kolejkowania.
## `void StreamSoundSource::setSoundFile(...)`

Ustawia plik dÄąĹźwiÄ™kowy, z ktĂłrego bÄ™dÄ… strumieniowane dane. JeÄąâ€şli ÄąĹźrĂłdÄąâ€šo czekaÄąâ€šo na plik, rozpoczyna odtwarzanie.
## `void StreamSoundSource::play()`

Rozpoczyna odtwarzanie. JeÄąâ€şli plik dÄąĹźwiÄ™kowy nie zostaÄąâ€š jeszcze zaÄąâ€šadowany (bo Äąâ€šadowanie odbywa siÄ™ asynchronicznie), ustawia flagÄ™ `m_waitingFile`. W przeciwnym razie, wywoÄąâ€šuje `queueBuffers()` i `SoundSource::play()`.
## `void StreamSoundSource::stop()`

Zatrzymuje odtwarzanie i czyÄąâ€şci kolejkÄ™ buforĂłw za pomocÄ… `unqueueBuffers()`.
## `void StreamSoundSource::update()`

Metoda wywoÄąâ€šywana cyklicznie.
1.  Sprawdza, ile buforĂłw zostaÄąâ€šo juÄąÄ˝ przetworzonych (odtworzonych) przez OpenAL.
2.  Odkolejkowuje przetworzone bufory.
3.  WypeÄąâ€šnia je nowymi danymi z pliku i ponownie dodaje do kolejki.
4.  ObsÄąâ€šuguje zapÄ™tlanie i sprawdza, czy odtwarzanie nie zostaÄąâ€šo przerwane przez "buffer underrun" (gdy OpenAL skoÄąâ€žczy odtwarzaÄ‡, a nie ma nowych buforĂłw w kolejce).
## `bool StreamSoundSource::fillBufferAndQueue(uint buffer)`

Kluczowa metoda.
1.  Odczytuje fragment danych z `m_soundFile`.
2.  ObsÄąâ€šuguje zapÄ™tlanie, resetujÄ…c plik po dojÄąâ€şciu do koÄąâ€žca.
3.  Opcjonalnie wykonuje "down-mix" z stereo do mono, jeÄąâ€şli `m_downMix` jest ustawione.
4.  WypeÄąâ€šnia podany bufor OpenAL nowymi danymi.
5.  Dodaje bufor do kolejki odtwarzania ÄąĹźrĂłdÄąâ€ša.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/streamsoundsource.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/sound/soundbuffer.h`, `soundfile.h`: UÄąÄ˝ywa tych klas do zarzÄ…dzania buforami i odczytu plikĂłw.
-   Jest tworzona przez `SoundManager` dla plikĂłw, ktĂłre nie sÄ… cachowane.

---
# Ä‘Ĺşâ€śâ€ž streamsoundsource.h
## Opis ogĂłlny

Plik `streamsoundsource.h` deklaruje klasÄ™ `StreamSoundSource`, ktĂłra jest implementacjÄ… `SoundSource` do strumieniowego odtwarzania dÄąĹźwiÄ™ku.
## Klasa `StreamSoundSource`
## Opis semantyczny
`StreamSoundSource` pozwala na odtwarzanie dÄąâ€šugich plikĂłw dÄąĹźwiÄ™kowych bez potrzeby Äąâ€šadowania ich w caÄąâ€šoÄąâ€şci do pamiÄ™ci. DziaÄąâ€ša poprzez dzielenie dÄąĹźwiÄ™ku na maÄąâ€še fragmenty, ktĂłre sÄ… dynamicznie Äąâ€šadowane do kolejki buforĂłw OpenAL w trakcie odtwarzania.
## StaÄąâ€še

-   `STREAM_BUFFER_SIZE`: CaÄąâ€škowity rozmiar bufora cyklicznego w pamiÄ™ci.
-   `STREAM_FRAGMENTS`: Liczba fragmentĂłw (buforĂłw OpenAL), na ktĂłre jest podzielony bufor cykliczny.
-   `STREAM_FRAGMENT_SIZE`: Rozmiar pojedynczego fragmentu.
## Typ wyliczeniowy `DownMix`

OkreÄąâ€şla, czy i jak konwertowaÄ‡ dÄąĹźwiÄ™k stereo na mono (tylko lewy kanaÄąâ€š, tylko prawy, lub brak konwersji).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `StreamSoundSource()` | Konstruktor, tworzy bufory. |
| `virtual ~StreamSoundSource()` | Destruktor. |
| `void play()` | Rozpoczyna strumieniowanie i odtwarzanie. |
| `void stop()` | Zatrzymuje odtwarzanie i czyÄąâ€şci kolejkÄ™ buforĂłw. |
| `bool isPlaying()` | Zwraca, czy ÄąĹźrĂłdÄąâ€šo jest w stanie odtwarzania. |
| `void setSoundFile(...)` | Ustawia plik dÄąĹźwiÄ™kowy do strumieniowania. |
| `void downMix(...)` | Ustawia tryb konwersji na mono. |
| `void update()` | Aktualizuje kolejkÄ™ buforĂłw (metoda cykliczna). |
## Zmienne prywatne

-   `m_soundFile`: WskaÄąĹźnik na plik dÄąĹźwiÄ™kowy.
-   `m_buffers`: Tablica buforĂłw OpenAL uÄąÄ˝ywanych w kolejce.
-   `m_downMix`: Tryb konwersji na mono.
-   `m_looping`, `m_playing`, `m_eof`, `m_waitingFile`: Flagi stanu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/soundsource.h`: Klasa bazowa.
-   Jest tworzona przez `SoundManager` do odtwarzania duÄąÄ˝ych plikĂłw dÄąĹźwiÄ™kowych.

---
# Ä‘Ĺşâ€śâ€ž soundsource.h
## Opis ogĂłlny

Plik `soundsource.h` deklaruje klasÄ™ `SoundSource`, ktĂłra jest abstrakcyjnym opakowaniem na ÄąĹźrĂłdÄąâ€šo dÄąĹźwiÄ™ku w OpenAL.
## Klasa `SoundSource`
## Opis semantyczny
`SoundSource` reprezentuje punkt w przestrzeni, z ktĂłrego wydobywa siÄ™ dÄąĹźwiÄ™k. Enkapsuluje ona ID ÄąĹźrĂłdÄąâ€ša OpenAL i dostarcza interfejs do kontrolowania jego wÄąâ€šaÄąâ€şciwoÄąâ€şci, takich jak gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡, wysokoÄąâ€şÄ‡ dÄąĹźwiÄ™ku, pozycja, zapÄ™tlanie i stan odtwarzania. Dziedziczy po `LuaObject`.
## Typ wyliczeniowy `FadeState`

-   `NoFading`: Brak efektu.
-   `FadingOn`: DÄąĹźwiÄ™k jest w trakcie zgÄąâ€šaÄąâ€şniania.
-   `FadingOff`: DÄąĹźwiÄ™k jest w trakcie wyciszania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundSource()` | Konstruktor. |
| `virtual ~SoundSource()` | Destruktor. |
| `virtual void play()` | Rozpoczyna odtwarzanie. |
| `virtual void stop()` | Zatrzymuje odtwarzanie. |
| `virtual bool isBuffering()` | Sprawdza stan ÄąĹźrĂłdÄąâ€ša w OpenAL. |
| `virtual bool isPlaying()` | DomyÄąâ€şlnie to samo co `isBuffering`. |
| `void setName(...)` | Ustawia nazwÄ™ (do identyfikacji). |
| `virtual void setLooping(...)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza zapÄ™tlanie. |
| `virtual void setRelative(...)` | Ustawia, czy pozycja jest wzglÄ™dna do sÄąâ€šuchacza. |
| `virtual void setReferenceDistance(...)` | Ustawia dystans referencyjny dla tÄąâ€šumienia dÄąĹźwiÄ™ku 3D. |
| `virtual void setGain(...)` | Ustawia gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡. |
| `virtual void setPitch(...)` | Ustawia wysokoÄąâ€şÄ‡ dÄąĹźwiÄ™ku. |
| `virtual void setPosition(...)` / `setVelocity(...)` | UstawiajÄ… wÄąâ€šaÄąâ€şciwoÄąâ€şci 3D. |
| `virtual void setFading(...)` | Inicjuje efekt pÄąâ€šynnego zgÄąâ€šaÄąâ€şniania/wyciszania. |
## Metody chronione

-   `void setBuffer(...)`: Przypisuje `SoundBuffer` do ÄąĹźrĂłdÄąâ€ša.
-   `virtual void update()`: Metoda cykliczna do obsÄąâ€šugi np. "fadingu".
## Zmienne

-   `m_sourceId`: ID ÄąĹźrĂłdÄąâ€ša w OpenAL.
-   `m_name`: Nazwa.
-   `m_buffer`: WskaÄąĹźnik na `SoundBuffer` (dla ÄąĹźrĂłdeÄąâ€š nie-strumieniowych).
-   `m_fade...`: Zmienne do obsÄąâ€šugi "fadingu".
-   `m_gain`: Aktualna gÄąâ€šoÄąâ€şnoÄąâ€şÄ‡.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/sound/declarations.h`, `soundbuffer.h`.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   Jest klasÄ… bazowÄ… dla `StreamSoundSource` i `CombinedSoundSource`.
-   Jest tworzona i zarzÄ…dzana przez `SoundManager`.

---
# Ä‘Ĺşâ€śâ€ž any.h
## Opis ogĂłlny

Plik `any.h` zawiera implementacjÄ™ klasy `stdext::any`, ktĂłra jest prostÄ…, wÄąâ€šasnÄ… wersjÄ… `std::any` (dostÄ™pnego od C++17) lub `boost::any`. Pozwala na przechowywanie wartoÄąâ€şci dowolnego typu w sposĂłb bezpieczny typowo.
## Klasa `any`
## Opis semantyczny
`any` dziaÄąâ€ša jak polimorficzny kontener. WewnÄ…trz przechowuje wskaÄąĹźnik na obiekt-opakowanie (`placeholder`), ktĂłry jest tworzony na stercie. Obiekt-opakowanie jest szablonem (`holder<T>`), ktĂłry przechowuje rzeczywistÄ… wartoÄąâ€şÄ‡ i informacje o jej typie (`type_info`).
## Struktury wewnÄ™trzne

-   **`placeholder`**: Abstrakcyjna klasa bazowa dla opakowaÄąâ€ž. Definiuje wirtualny interfejs do pobierania `type_info` i klonowania.
-   **`holder<T>`**: Szablonowa klasa pochodna, ktĂłra faktycznie przechowuje wartoÄąâ€şÄ‡ typu `T`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `any()` | Konstruktor domyÄąâ€şlny (pusty). |
| `any(const any& other)` | Konstruktor kopiujÄ…cy (gÄąâ€šÄ™boka kopia). |
| `template<typename T> any(const T& value)` | Konstruktor szablonowy, tworzy `holder<T>`. |
| `~any()` | Destruktor, zwalnia `placeholder`. |
| `any& swap(any& rhs)` | Zamienia zawartoÄąâ€şÄ‡ dwĂłch obiektĂłw `any`. |
| `operator=` | Operatory przypisania. |
| `bool empty()` | Zwraca `true`, jeÄąâ€şli `any` nie przechowuje wartoÄąâ€şci. |
| `template<typename T> const T& cast() const` | Rzutuje i zwraca przechowywanÄ… wartoÄąâ€şÄ‡. Rzuca `VALIDATE` error, jeÄąâ€şli typ jest nieprawidÄąâ€šowy. |
| `const std::type_info & type() const` | Zwraca `type_info` przechowywanej wartoÄąâ€şci. |
## Funkcja `any_cast`

Funkcja pomocnicza, ktĂłra wykonuje bezpieczne rzutowanie. Sprawdza, czy typ przechowywany w `any` zgadza siÄ™ z typem docelowym.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `<algorithm>`, `<typeinfo>`: Standardowe nagÄąâ€šĂłwki C++.
-   Jest uÄąÄ˝ywana w `dynamic_storage` do przechowywania wartoÄąâ€şci rĂłÄąÄ˝nych typĂłw.

---
# Ä‘Ĺşâ€śâ€ž cast.h
## Opis ogĂłlny

Plik `cast.h` zawiera zestaw szablonowych funkcji i klas do konwersji (rzutowania) miÄ™dzy rĂłÄąÄ˝nymi typami danych, gÄąâ€šĂłwnie z i do `std::string`.
## Funkcje `cast`
## `template<typename T, typename R> bool cast(const T& in, R& out)`

GÄąâ€šĂłwna, szablonowa funkcja. UÄąÄ˝ywa `std::stringstream` do konwersji. Zwraca `true`, jeÄąâ€şli konwersja siÄ™ powiodÄąâ€ša.
## Specjalizacje

Plik zawiera specjalizacje dla typowych i problematycznych konwersji, aby byÄąâ€šy one bardziej wydajne i niezawodne:
-   `string` do `string`: Proste przypisanie.
-   `string` do `bool`: ObsÄąâ€šuguje tylko "true" i "false".
-   `string` do `char`: Tylko dla stringĂłw o dÄąâ€šugoÄąâ€şci 1.
-   `string` do `long`, `int`, `double`, `float`: UÄąÄ˝ywajÄ… `atol` i `atof`, ale z dodatkowÄ… walidacjÄ… znakĂłw, aby uniknÄ…Ä‡ nieprawidÄąâ€šowych konwersji (np. "123a" nie zostanie skonwertowane).
-   `bool` do `string`: Konwertuje na "true" lub "false".
## Klasa `cast_exception`

WyjÄ…tek rzucany przez `safe_cast`, gdy konwersja siÄ™ nie powiedzie.
## Funkcje `safe_cast` i `unsafe_cast`

-   **`safe_cast<R, T>(...)`**: Opakowanie na `cast`, ktĂłre rzuca `cast_exception` w przypadku niepowodzenia.
-   **`unsafe_cast<R, T>(...)`**: Opakowanie na `safe_cast`, ktĂłre Äąâ€šapie wyjÄ…tek, loguje bÄąâ€šÄ…d i zwraca wartoÄąâ€şÄ‡ domyÄąâ€şlnÄ….
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/exception.h`, `demangle.h`: Do obsÄąâ€šugi bÄąâ€šÄ™dĂłw i nazw typĂłw.
-   SÄ… to fundamentalne narzÄ™dzia uÄąÄ˝ywane w caÄąâ€šym projekcie, szczegĂłlnie do parsowania wartoÄąâ€şci z plikĂłw OTML i konwersji typĂłw dla Lua.

---
# Ä‘Ĺşâ€śâ€ž demangle.cpp
## Opis ogĂłlny

Plik `demangle.cpp` zawiera implementacjÄ™ funkcji `demangle_name`, ktĂłra konwertuje "znieksztaÄąâ€šcone" (mangled) nazwy typĂłw C++ na ich czytelnÄ… formÄ™.
## Funkcja `demangle_name`
## `const char* demangle_name(const char* name)`
## Opis semantyczny
Nazwy typĂłw C++ (szczegĂłlnie w przypadku szablonĂłw i przestrzeni nazw) sÄ… przez kompilator zamieniane na unikalne, ale nieczytelne identyfikatory (np. `N6stdext11cast_exceptionE`). Funkcja ta odwraca ten proces, uÄąÄ˝ywajÄ…c narzÄ™dzi specyficznych dla danego kompilatora.
## Implementacja
-   **Dla MSVC (`_MSC_VER`)**: UÄąÄ˝ywa funkcji `UnDecorateSymbolName` z biblioteki `DbgHelp.dll`.
-   **Dla GCC/Clang**: UÄąÄ˝ywa funkcji `abi::__cxa_demangle` z biblioteki `cxxabi`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/stdext/demangle.h`: Plik nagÄąâ€šĂłwkowy.
-   NagÄąâ€šĂłwki specyficzne dla platformy (`dbghelp.h` lub `cxxabi.h`).
-   Jest uÄąÄ˝ywana w systemie rzutowania (`cast_exception`) i w logowaniu, aby dostarczaÄ‡ czytelne nazwy typĂłw w komunikatach o bÄąâ€šÄ™dach.

---
# Ä‘Ĺşâ€śâ€ž compiler.h
## Opis ogĂłlny

Plik `compiler.h` zawiera makra i dyrektywy preprocesora specyficzne dla kompilatora. Jego celem jest ujednolicenie obsÄąâ€šugi rĂłÄąÄ˝nych kompilatorĂłw (GCC, Clang, MSVC) i zapewnienie kompatybilnoÄąâ€şci.
## ZawartoÄąâ€şÄ‡
## `BUILD_COMPILER`

Makro, ktĂłre jest definiowane jako string zawierajÄ…cy nazwÄ™ i wersjÄ™ uÄąÄ˝ywanego kompilatora. Jest to ustalane na podstawie predefiniowanych makr kompilatora (`__clang__`, `__GNUC__`, `_MSC_VER`).
## Sprawdzanie wersji kompilatora

Plik zawiera dyrektywy `#error`, ktĂłre zatrzymajÄ… kompilacjÄ™, jeÄąâ€şli wersja kompilatora jest zbyt stara (wymagany GCC >= 4.6, MSVC >= 2013).
## WyÄąâ€šÄ…czanie ostrzeÄąÄ˝eÄąâ€ž (MSVC)

Dla kompilatora MSVC, wyÄąâ€šÄ…cza szereg czÄ™sto wystÄ™pujÄ…cych, ale zazwyczaj nieszkodliwych ostrzeÄąÄ˝eÄąâ€ž (`#pragma warning(disable: ...)`), aby utrzymaÄ‡ czysty output kompilacji.
## `__PRETTY_FUNCTION__`

Dla MSVC, definiuje `__PRETTY_FUNCTION__` jako alias dla `__FUNCDNAME__`, aby ujednoliciÄ‡ sposĂłb uzyskiwania "ozdobnej" nazwy funkcji.
## `likely(x)` i `unlikely(x)`

Makra do optymalizacji podpowiedzi dla kompilatora (branch prediction). Dla GCC/Clang uÄąÄ˝ywajÄ… `__builtin_expect`. Dla innych kompilatorĂłw sÄ… puste.
## Sprawdzanie wsparcia C++0x

Sprawdza, czy kompilator wspiera wymagany standard C++ (C++11 lub nowszy).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to jeden z najbardziej fundamentalnych plikĂłw nagÄąâ€šĂłwkowych, doÄąâ€šÄ…czany przez `global.h`, i wpÄąâ€šywa na kompilacjÄ™ caÄąâ€šego projektu.

---
# Ä‘Ĺşâ€śâ€ž demangle.h
## Opis ogĂłlny

Plik `demangle.h` deklaruje funkcje pomocnicze do "demanglowania" (odkodowywania) nazw typĂłw C++, ktĂłre sÄ… znieksztaÄąâ€šcane przez kompilator w procesie kompilacji.
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `const char* demangle_name(const char* name)` | Przyjmuje znieksztaÄąâ€šconÄ… nazwÄ™ i zwraca jej czytelnÄ… wersjÄ™. |
| `template<typename T> std::string demangle_class()`| Szablonowa funkcja, ktĂłra zwraca czytelnÄ… nazwÄ™ klasy dla danego typu `T`. |
| `template<typename T> std::string demangle_type()` | Szablonowa funkcja, ktĂłra zwraca czytelnÄ… nazwÄ™ dowolnego typu `T`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `<typeinfo>`, `<string>`: Standardowe nagÄąâ€šĂłwki.
-   Jest uÄąÄ˝ywana do generowania czytelnych komunikatĂłw o bÄąâ€šÄ™dach, np. w `cast_exception` i `LuaBadValueCastException`.

---
# Ä‘Ĺşâ€śâ€ž boolean.h
## Opis ogĂłlny

Plik `boolean.h` deklaruje prostÄ… klasÄ™ szablonowÄ… `stdext::boolean`, ktĂłra jest opakowaniem na typ `bool` z moÄąÄ˝liwoÄąâ€şciÄ… zdefiniowania wartoÄąâ€şci domyÄąâ€şlnej.
## Klasa `boolean`
## `template<bool def>`

-   **Parametr szablonu `def`**: OkreÄąâ€şla domyÄąâ€şlnÄ… wartoÄąâ€şÄ‡ (`true` lub `false`).
## Opis semantyczny
`boolean` zachowuje siÄ™ jak standardowy `bool`, ale jego konstruktor domyÄąâ€şlny inicjalizuje go wartoÄąâ€şciÄ… `def`. Jest to przydatne do inicjalizacji pĂłl w klasach, gdzie domyÄąâ€şlna wartoÄąâ€şÄ‡ `bool` (ktĂłra jest nieokreÄąâ€şlona) mogÄąâ€šaby prowadziÄ‡ do bÄąâ€šÄ™dĂłw.
## PrzykÄąâ€šad uÄąÄ˝ycia

`$fenceInfo
class MyWidget {
    stdext::boolean<true> m_visible; // DomyÄąâ€şlnie true
    stdext::boolean<false> m_enabled; // DomyÄąâ€şlnie false
};
```
## Operatory

Klasa przeciÄ…ÄąÄ˝a operatory `operator bool&`, `operator bool const&` i `operator=`, co pozwala na uÄąÄ˝ywanie jej w taki sam sposĂłb, jak standardowego `bool`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to prosta klasa narzÄ™dziowa, uÄąÄ˝ywana w wielu miejscach w projekcie (np. w `UIWidget`) do definiowania flag stanu.

---
# Ä‘Ĺşâ€śâ€ž dumper.h
## Opis ogĂłlny

Plik `dumper.h` zawiera proste narzÄ™dzie do szybkiego debugowania, ktĂłre pozwala na wypisywanie wartoÄąâ€şci wielu zmiennych na standardowe wyjÄąâ€şcie w jednej linii.
## Zmienne globalne
## `dump`

Globalny obiekt o specjalnej strukturze, ktĂłry przeciÄ…ÄąÄ˝a operator `<<`.
## Opis semantyczny
UÄąÄ˝ycie `dump` pozwala na tworzenie Äąâ€šaÄąâ€žcuchowych wywoÄąâ€šaÄąâ€ž, ktĂłre wypisujÄ… wartoÄąâ€şci oddzielone spacjami, a na koÄąâ€žcu automatycznie dodajÄ… znak nowej linii.
## PrzykÄąâ€šad uÄąÄ˝ycia
`$fenceInfo
int x = 10;
std::string y = "hello";
dump << "WartoÄąâ€şci:" << x << y;
```
**WyjÄąâ€şcie:**
`$fenceInfo
WartoÄąâ€şci: 10 hello 
```
## Implementacja
-   Tworzy globalny obiekt, ktĂłrego `operator<<` zwraca tymczasowy obiekt `dumper_dummy`.
-   `dumper_dummy` ma przeciÄ…ÄąÄ˝ony `operator<<` do wypisywania wartoÄąâ€şci i destruktor, ktĂłry wypisuje znak nowej linii.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `<iostream>`: Do wypisywania na `std::cout`.
-   Jest to narzÄ™dzie wyÄąâ€šÄ…cznie do celĂłw debugowania.

---
# Ä‘Ĺşâ€śâ€ž dynamic_storage.h
## Opis ogĂłlny

Plik `dynamic_storage.h` deklaruje klasÄ™ szablonowÄ… `dynamic_storage`, ktĂłra implementuje dynamiczny kontener asocjacyjny, gdzie kluczem jest typ caÄąâ€škowitoliczbowy, a wartoÄąâ€şciÄ… moÄąÄ˝e byÄ‡ dowolny typ (przechowywany za pomocÄ… `stdext::any`).
## Klasa `dynamic_storage`
## Opis semantyczny
`dynamic_storage` dziaÄąâ€ša jak mapa, ale jest zaimplementowana w oparciu o `std::vector<stdext::any>`. Klucz (`Key`) jest uÄąÄ˝ywany jako indeks w wektorze. Jest to wydajne, jeÄąâ€şli klucze sÄ… maÄąâ€šymi, kolejnymi liczbami caÄąâ€škowitymi. Pozwala na przechowywanie heterogenicznych danych w jednym kontenerze.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `template<typename T> void set(...)` | Ustawia wartoÄąâ€şÄ‡ dla danego klucza. W razie potrzeby rozszerza wektor. |
| `bool remove(...)` | Usuwa wartoÄąâ€şÄ‡ dla danego klucza (zastÄ™pujÄ…c jÄ… pustym `any`). |
| `template<typename T> T get(...) const` | Pobiera wartoÄąâ€şÄ‡ dla danego klucza, rzutujÄ…c jÄ… na typ `T`. Zwraca wartoÄąâ€şÄ‡ domyÄąâ€şlnÄ…, jeÄąâ€şli klucz nie istnieje. |
| `bool has(...) const` | Sprawdza, czy klucz istnieje i ma przypisanÄ… wartoÄąâ€şÄ‡. |
| `std::size_t size() const` | Zwraca liczbÄ™ niepustych elementĂłw. |
| `void clear()` | CzyÄąâ€şci kontener. |
## Zmienne prywatne

-   `m_data`: Wektor `stdext::any`, ktĂłry przechowuje dane.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/types.h`, `stdext/any.h`: Wymagane definicje.
-   `<unordered_map>`: NagÄąâ€šĂłwek jest doÄąâ€šÄ…czony, ale nie jest uÄąÄ˝ywany.
-   MoÄąÄ˝e byÄ‡ uÄąÄ˝ywana do implementacji niestandardowych systemĂłw atrybutĂłw lub wÄąâ€šaÄąâ€şciwoÄąâ€şci dla obiektĂłw.

---
# Ä‘Ĺşâ€śâ€ž exception.h
## Opis ogĂłlny

Plik `exception.h` deklaruje klasÄ™ `stdext::exception`, ktĂłra jest bazowÄ… klasÄ… dla wszystkich niestandardowych wyjÄ…tkĂłw w projekcie.
## Klasa `exception`
## Opis semantyczny
Dziedziczy po `std::exception` i rozszerza jÄ… o konstruktor przyjmujÄ…cy `std::string` oraz o przechowywanie komunikatu bÄąâ€šÄ™du w `m_what`. Upraszcza to tworzenie i rzucanie wyjÄ…tkĂłw z niestandardowymi komunikatami.
## Metody

-   `exception(const std::string& what)`: Konstruktor.
-   `virtual const char* what() const throw()`: Zwraca komunikat bÄąâ€šÄ™du.
## Funkcja `throw_exception`

Funkcja pomocnicza, ktĂłra tworzy i rzuca `stdext::exception`.

`$fenceInfo
inline void throw_exception(const std::string& what) { throw exception(what); }
```
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest klasÄ… bazowÄ… dla `cast_exception` i `LuaException`.
-   Jest uÄąÄ˝ywana w caÄąâ€šym projekcie do sygnalizowania bÄąâ€šÄ™dĂłw, ktĂłre mogÄ… byÄ‡ przechwycone i obsÄąâ€šuÄąÄ˝one na wyÄąÄ˝szym poziomie.

---
# Ä‘Ĺşâ€śâ€ž fastrand.h
## Opis ogĂłlny

Plik `fastrand.h` zawiera implementacjÄ™ prostej i szybkiej funkcji do generowania liczb pseudolosowych.
## Funkcja `fastrand`
## `static int fastrand()`
## Opis semantyczny
Implementuje liniowy generator kongruentny (Linear Congruential Generator - LCG). Jest to bardzo prosty i szybki algorytm, ale o niskiej jakoÄąâ€şci losowoÄąâ€şci w porĂłwnaniu do nowoczeÄąâ€şniejszych generatorĂłw (jak Mersenne Twister). Jest odpowiedni do zastosowaÄąâ€ž, gdzie wydajnoÄąâ€şÄ‡ jest waÄąÄ˝niejsza niÄąÄ˝ jakoÄąâ€şÄ‡ losowoÄąâ€şci (np. proste efekty wizualne).
## DziaÄąâ€šanie
-   UÄąÄ˝ywa statycznej zmiennej `g_seed` jako stanu.
-   W kaÄąÄ˝dym wywoÄąâ€šaniu, aktualizuje `g_seed` wedÄąâ€šug wzoru: `g_seed = (a * g_seed + c)`.
-   Zwraca 15 najbardziej znaczÄ…cych bitĂłw z wyÄąÄ˝szych 16 bitĂłw wyniku.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to samodzielna funkcja narzÄ™dziowa.

---
# Ä‘Ĺşâ€śâ€ž math.cpp
## Opis ogĂłlny

Plik `math.cpp` zawiera implementacjÄ™ funkcji matematycznych i losowych zadeklarowanych w `math.h`.
## Funkcje
## `uint32_t stdext::adler32(...)`

Implementuje algorytm sumy kontrolnej Adler-32, ktĂłry jest szybszy, ale mniej niezawodny niÄąÄ˝ CRC32.
## `long stdext::random_range(long min, long max)`

Generuje losowÄ… liczbÄ™ caÄąâ€škowitÄ… z podanego zakresu (wÄąâ€šÄ…cznie). UÄąÄ˝ywa generatora Mersenne Twister (`std::mt19937`) zasilanego przez `std::random_device`, co zapewnia wysokÄ… jakoÄąâ€şÄ‡ losowoÄąâ€şci.
## `float stdext::random_range(float min, float max)`

Generuje losowÄ… liczbÄ™ zmiennoprzecinkowÄ… z podanego zakresu.
## `double stdext::round(double r)`

Implementuje zaokrÄ…glanie matematyczne (od .5 w gĂłrÄ™).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/stdext/math.h`: Plik nagÄąâ€šĂłwkowy.
-   `<random>`: Do generowania liczb losowych.

---
# Ä‘Ĺşâ€śâ€ž math.h
## Opis ogĂłlny

Plik `math.h` deklaruje zestaw funkcji pomocniczych zwiÄ…zanych z matematykÄ…, operacjami bitowymi i losowoÄąâ€şciÄ….
## Funkcje

-   **`is_power_of_two(v)`**: Sprawdza, czy liczba jest potÄ™gÄ… dwĂłjki.
-   **`to_power_of_two(v)`**: Zwraca najbliÄąÄ˝szÄ… potÄ™gÄ™ dwĂłjki, ktĂłra jest wiÄ™ksza lub rĂłwna `v`.
-   **`readULE16`, `readULE32`, `readULE64`**: OdczytujÄ… liczby caÄąâ€škowite bez znaku w porzÄ…dku Little Endian z bufora.
-   **`writeULE16`, `writeULE32`, `writeULE64`**: ZapisujÄ… liczby do bufora w porzÄ…dku Little Endian.
-   **`readSLE...`, `writeSLE...`**: Analogiczne funkcje dla liczb ze znakiem.
-   **`adler32(...)`**: Deklaracja funkcji sumy kontrolnej.
-   **`random_range(...)`**: Deklaracje funkcji do generowania liczb losowych.
-   **`round(...)`**: Deklaracja funkcji zaokrÄ…glajÄ…cej.
-   **`clamp(...)`**: Szablonowa funkcja ograniczajÄ…ca wartoÄąâ€şÄ‡ do podanego zakresu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   SÄ… to podstawowe funkcje narzÄ™dziowe, uÄąÄ˝ywane w wielu miejscach, szczegĂłlnie w obsÄąâ€šudze sieci (odczyt/zapis pakietĂłw) i grafice (operacje na potÄ™gach dwĂłjki dla tekstur).

---
# Ä‘Ĺşâ€śâ€ž net.h
## Opis ogĂłlny

Plik `net.h` deklaruje funkcje pomocnicze zwiÄ…zane z operacjami na adresach IP.
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `std::string ip_to_string(uint32 ip)` | Konwertuje 32-bitowy adres IP (w porzÄ…dku sieciowym) na jego reprezentacjÄ™ tekstowÄ… (np. "127.0.0.1"). |
| `uint32 string_to_ip(const std::string& string)` | Konwertuje adres IP w formacie tekstowym na jego 32-bitowÄ… reprezentacjÄ™ w porzÄ…dku sieciowym. |
| `std::vector<uint32> listSubnetAddresses(...)` | Generuje listÄ™ wszystkich adresĂłw IP w danej podsieci. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/types.h`.
-   Implementacja w `net.cpp` uÄąÄ˝ywa Boost.Asio do konwersji.
-   Funkcje te sÄ… uÄąÄ˝ywane w logice sieciowej, np. do logowania adresĂłw IP.

---
# Ä‘Ĺşâ€śâ€ž packed_any.h
## Opis ogĂłlny

Plik `packed_any.h` deklaruje klasÄ™ `stdext::packed_any`, ktĂłra jest zoptymalizowanÄ… pod kÄ…tem pamiÄ™ci wersjÄ… `stdext::any`.
## Klasa `packed_any`
## Opis semantyczny
`packed_any` dziaÄąâ€ša podobnie do `any`, ale wprowadza optymalizacjÄ™ dla maÄąâ€šych, trywialnych typĂłw (takich jak `int`, `bool`, `enum`, wskaÄąĹźniki). Zamiast alokowaÄ‡ pamiÄ™Ä‡ na stercie dla `holdera`, wartoÄąâ€şci takich typĂłw sÄ… przechowywane bezpoÄąâ€şrednio w wskaÄąĹźniku `content` poprzez rzutowanie. Flaga `scalar` odrĂłÄąÄ˝nia te dwa tryby przechowywania. Zmniejsza to fragmentacjÄ™ pamiÄ™ci i narzut na alokacjÄ™ dla czÄ™sto uÄąÄ˝ywanych, maÄąâ€šych typĂłw.
## Szablon `can_pack_in_any`

Szablon pomocniczy, ktĂłry w czasie kompilacji okreÄąâ€şla, czy dany typ `T` moÄąÄ˝e byÄ‡ "spakowany" bezpoÄąâ€şrednio we wskaÄąĹźniku. Warunkiem jest, aby `sizeof(T)` byÄąâ€š mniejszy lub rĂłwny `sizeof(void*)` i aby typ byÄąâ€š trywialnie kopiowalny.
## Metody i pola

SÄ… analogiczne do `stdext::any`, z dodatkowym polem `scalar` do rozrĂłÄąÄ˝niania trybu.
## Funkcja `packed_any_cast`

Posiada dwie specjalizacje: jednÄ… dla typĂłw "pakowalnych" (ktĂłra rzutuje wskaÄąĹźnik z powrotem na wartoÄąâ€şÄ‡) i drugÄ… dla typĂłw nie-pakowalnych (ktĂłra dziaÄąâ€ša jak `any_cast`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest uÄąÄ˝ywana w `packed_storage` jako mechanizm przechowywania wartoÄąâ€şci.

---
# Ä‘Ĺşâ€śâ€ž shared_object.h
## Opis ogĂłlny

Plik `shared_object.h` zawiera implementacjÄ™ wÄąâ€šasnego, intruzywnego inteligentnego wskaÄąĹźnika (`shared_object_ptr`) i powiÄ…zanej z nim klasy bazowej (`shared_object`).
## Klasa `shared_object`
## Opis semantyczny
Jest to klasa bazowa, po ktĂłrej muszÄ… dziedziczyÄ‡ wszystkie klasy, ktĂłre chcÄ… byÄ‡ zarzÄ…dzane przez `shared_object_ptr`. Zawiera ona licznik referencji (`refs`) i metody do jego inkrementacji i dekrementacji. Jest to tzw. "intruzywny" wskaÄąĹźnik, poniewaÄąÄ˝ sam obiekt przechowuje swĂłj licznik referencji.
## Metody

-   `add_ref()`: Inkrementuje licznik.
-   `dec_ref()`: Dekrementuje licznik. JeÄąâ€şli osiÄ…gnie 0, obiekt usuwa sam siebie (`delete this`).
-   `ref_count()`: Zwraca liczbÄ™ referencji.
-   `..._self_cast()`: Metody pomocnicze do bezpiecznego rzutowania `this` na `shared_object_ptr`.
## Klasa `shared_object_ptr`
## Opis semantyczny
Jest to szablonowa klasa inteligentnego wskaÄąĹźnika, ktĂłra naÄąâ€şladuje zachowanie `std::shared_ptr`, ale wspĂłÄąâ€špracuje z `shared_object`. ZarzÄ…dza czasem ÄąÄ˝ycia obiektu, na ktĂłry wskazuje, automatycznie wywoÄąâ€šujÄ…c `add_ref` i `dec_ref`.
## Metody i operatory

Implementuje wszystkie standardowe operacje dla inteligentnych wskaÄąĹźnikĂłw: konstruktory, destruktor, operatory przypisania, dereferencji (`*`, `->`), porĂłwnania, a takÄąÄ˝e konwersjÄ™ do `bool`.
## Funkcje pomocnicze

-   `get_pointer`, `static_pointer_cast`, `const_pointer_cast`, `dynamic_pointer_cast`, `make_shared_object`: Funkcje globalne naÄąâ€şladujÄ…ce te znane z `<memory>`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to fundamentalny element frameworka. Prawie wszystkie klasy, ktĂłre sÄ… dynamicznie alokowane i przekazywane miÄ™dzy rĂłÄąÄ˝nymi czÄ™Äąâ€şciami systemu (szczegĂłlnie do i z Lua), dziedziczÄ… po `shared_object` i sÄ… zarzÄ…dzane przez `shared_object_ptr`.

---
# Ä‘Ĺşâ€śâ€ž stdext.h
## Opis ogĂłlny

Plik `stdext.h` jest gÄąâ€šĂłwnym plikiem nagÄąâ€šĂłwkowym dla moduÄąâ€šu `stdext` (standard extensions). Jego jedynym zadaniem jest doÄąâ€šÄ…czenie wszystkich innych plikĂłw nagÄąâ€šĂłwkowych z tego moduÄąâ€šu w jednym miejscu.
## ZawartoÄąâ€şÄ‡

DoÄąâ€šÄ…cza wszystkie pliki z `framework/stdext/`, w tym:
-   `compiler.h`
-   `dumper.h`
-   `types.h`
-   `exception.h`
-   `demangle.h`
-   `cast.h`
-   `math.h`
-   `string.h`
-   `time.h`
-   `boolean.h`
-   `shared_object.h`
-   `any.h`
-   `packed_any.h`
-   `dynamic_storage.h`
-   `packed_storage.h`
-   `format.h`
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest doÄąâ€šÄ…czany przez `global.h`, co sprawia, ÄąÄ˝e wszystkie narzÄ™dzia z `stdext` sÄ… dostÄ™pne w caÄąâ€šym projekcie.

---
# Ä‘Ĺşâ€śâ€ž packed_storage.h
## Opis ogĂłlny

Plik `packed_storage.h` deklaruje klasÄ™ szablonowÄ… `packed_storage`, ktĂłra jest kontenerem asocjacyjnym zoptymalizowanym pod kÄ…tem minimalnego zuÄąÄ˝ycia pamiÄ™ci.
## Klasa `packed_storage`
## Opis semantyczny
`packed_storage` dziaÄąâ€ša jak mapa, ale zamiast zÄąâ€šoÄąÄ˝onych struktur drzewiastych lub tablic hashujÄ…cych, przechowuje swoje elementy w prostej, dynamicznie alokowanej tablicy par `(klucz, wartoÄąâ€şÄ‡)`. WartoÄąâ€şci sÄ… przechowywane w `packed_any`, co dodatkowo minimalizuje zuÄąÄ˝ycie pamiÄ™ci. Jest to rozwiÄ…zanie kompromisowe: zuÄąÄ˝ywa bardzo maÄąâ€šo pamiÄ™ci, ale operacje wyszukiwania, dodawania i usuwania majÄ… zÄąâ€šoÄąÄ˝onoÄąâ€şÄ‡ liniowÄ… O(n). Jest odpowiednia dla maÄąâ€šej liczby elementĂłw.
## Metody publiczne

SÄ… analogiczne do `dynamic_storage`: `set`, `remove`, `get`, `has`, `clear`, `size`.
## Zmienne prywatne

-   `m_values`: WskaÄąĹźnik na tablicÄ™ `value_pair`.
-   `m_size`: Aktualna liczba elementĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/types.h`, `stdext/packed_any.h`.
-   MoÄąÄ˝e byÄ‡ uÄąÄ˝ywana tam, gdzie liczy siÄ™ kaÄąÄ˝dy bajt pamiÄ™ci, a liczba przechowywanych elementĂłw jest niewielka.

---
# Ä‘Ĺşâ€śâ€ž thread.h
## Opis ogĂłlny

Plik `thread.h` jest prostym plikiem nagÄąâ€šĂłwkowym, ktĂłry doÄąâ€šÄ…cza standardowe nagÄąâ€šĂłwki C++ zwiÄ…zane z wielowÄ…tkowoÄąâ€şciÄ….
## ZawartoÄąâ€şÄ‡

`$fenceInfo
# include <thread>
# include <condition_variable>
# include <mutex>
```
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   SÄąâ€šuÄąÄ˝y jako centralny punkt doÄąâ€šÄ…czania nagÄąâ€šĂłwkĂłw wielowÄ…tkowoÄąâ€şci, co uÄąâ€šatwia zarzÄ…dzanie zaleÄąÄ˝noÄąâ€şciami.
-   Jest uÄąÄ˝ywany przez klasy takie jak `AsyncDispatcher`, `Logger`, `ProxyManager`.

---
# Ä‘Ĺşâ€śâ€ž time.h
## Opis ogĂłlny

Plik `time.h` deklaruje zestaw funkcji i klas do obsÄąâ€šugi czasu, stanowiÄ…c opakowanie na `std::chrono`.
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `ticks_t time()` | Zwraca czas w sekundach od epoki (Unix timestamp). |
| `ticks_t millis()` | Zwraca czas w milisekundach od uruchomienia aplikacji. |
| `ticks_t micros()` | Zwraca czas w mikrosekundach od uruchomienia aplikacji. |
| `void millisleep(size_t ms)` | Usypia bieÄąÄ˝Ä…cy wÄ…tek na `ms` milisekund. |
| `void microsleep(size_t us)` | Usypia bieÄąÄ˝Ä…cy wÄ…tek na `us` mikrosekund. |
## Struktura `timer`

Prosta klasa-stoper, podobna do `Timer` z moduÄąâ€šu `core`, ale dziaÄąâ€šajÄ…ca na "rzeczywistym" czasie z `stdext::micros()`, a nie na buforowanym czasie z `g_clock`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/types.h`.
-   Implementacja w `time.cpp` uÄąÄ˝ywa `std::chrono` i `std::this_thread`.
-   SÄ… to niskopoziomowe funkcje czasowe, na ktĂłrych bazuje `Clock`.

---
# Ä‘Ĺşâ€śâ€ž traits.h
## Opis ogĂłlny

Plik `traits.h` zawiera szablony metaprogramowania (type traits), ktĂłre sÄ… uÄąÄ˝ywane do manipulacji i analizy typĂłw w czasie kompilacji.
## Namespace `stdext`
## Szablony

-   **`replace_extent`**: Usuwa wymiar tablicy z typu i zastÄ™puje go wskaÄąĹźnikiem. Np. `int[10]` staje siÄ™ `const int*`.
-   **`remove_const_ref`**: Metafunkcja, ktĂłra z danego typu `T` usuwa kwalifikatory `const` oraz referencjÄ™, zwracajÄ…c "czysty" typ. Np. `const std::string&` staje siÄ™ `std::string`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `<type_traits>`: Standardowy nagÄąâ€šĂłwek C++.
-   SÄ… to zaawansowane narzÄ™dzia metaprogramowania, uÄąÄ˝ywane gÄąâ€šĂłwnie w `luabinder.h` do analizy sygnatur funkcji i w `format.h` do obsÄąâ€šugi argumentĂłw.

---
# Ä‘Ĺşâ€śâ€ž string.h
## Opis ogĂłlny

Plik `string.h` deklaruje zestaw funkcji pomocniczych do manipulacji i konwersji ciÄ…gĂłw znakĂłw (`std::string`).
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `to_string<T>(...)` / `from_string<T>(...)` | SkrĂłty do `unsafe_cast` dla konwersji z/do stringa. |
| `resolve_path(...)` | ÄąÂÄ…czy Äąâ€şcieÄąÄ˝kÄ™ do pliku ze Äąâ€şcieÄąÄ˝kÄ… ÄąĹźrĂłdÄąâ€šowÄ…. |
| `date_time_string()` | Zwraca sformatowanÄ… datÄ™ i czas. |
| `dec_to_hex(...)` / `hex_to_dec(...)` | Konwersje miÄ™dzy systemem dziesiÄ™tnym a szesnastkowym. |
| `tolower(...)`, `toupper(...)`, `trim(...)`, `ucwords(...)` | Standardowe operacje na stringach. |
| `ends_with(...)`, `starts_with(...)`, `replace_all(...)` | Operacje wyszukiwania i zamiany. |
| `is_valid_utf8(...)` | Sprawdza, czy string jest poprawnym ciÄ…giem UTF-8. |
| `utf8_to_latin1(...)`, `latin1_to_utf8(...)` | Konwersje kodowania znakĂłw. |
| `utf8_to_utf16(...)`, `utf16_to_utf8(...)` | (Windows) Konwersje do/z UTF-16 (`std::wstring`). |
| `split(...)` | Dzieli string na wektor stringĂłw na podstawie separatorĂłw. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/types.h`, `cast.h`.
-   Implementacja w `string.cpp` uÄąÄ˝ywa biblioteki Boost.StringAlgo do niektĂłrych operacji.
-   SÄ… to podstawowe funkcje narzÄ™dziowe uÄąÄ˝ywane w caÄąâ€šym projekcie.

---
# Ä‘Ĺşâ€śâ€ž time.cpp
## Opis ogĂłlny

Plik `time.cpp` zawiera implementacjÄ™ funkcji czasowych zadeklarowanych w `time.h`.
## Namespace `stdext`
## `startup_time`

Statyczna zmienna, ktĂłra przechowuje czas uruchomienia aplikacji. Jest uÄąÄ˝ywana jako punkt odniesienia dla `millis()` i `micros()`.

`$fenceInfo
const static auto startup_time = std::chrono::high_resolution_clock::now();
```
## Implementacje funkcji

-   **`time()`**: UÄąÄ˝ywa `std::time(NULL)`.
-   **`millis()`**, **`micros()`**: ObliczajÄ… rĂłÄąÄ˝nicÄ™ miÄ™dzy bieÄąÄ˝Ä…cym czasem a `startup_time` za pomocÄ… `std::chrono` i konwertujÄ… wynik na odpowiedniÄ… jednostkÄ™.
-   **`millisleep()`**, **`microsleep()`**: UÄąÄ˝ywajÄ… `std::this_thread::sleep_for`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/time.h`: Plik nagÄąâ€šĂłwkowy.
-   `<chrono>`, `<ctime>`, `<thread>`: Standardowe biblioteki C++.

---
# Ä‘Ĺşâ€śâ€ž uri.h
## Opis ogĂłlny

Plik `uri.h` deklaruje strukturÄ™ `ParsedURI` oraz funkcjÄ™ do parsowania adresĂłw URL.
## Struktura `ParsedURI`

Przechowuje rozbity na czÄ™Äąâ€şci adres URL.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `protocol` | `std::string` | ProtokĂłÄąâ€š (np. "http", "wss"). |
| `domain` | `std::string` | Domena (np. "example.com"). |
| `port` | `std::string` | Port. |
| `query` | `std::string` | ÄąĹˇcieÄąÄ˝ka i zapytanie (np. "/path?a=1"). |
## Funkcja `parseURI`
## `ParsedURI parseURI(const std::string& url)`

Parsuje podany URL i zwraca strukturÄ™ `ParsedURI` z jego komponentami.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest uÄąÄ˝ywana przez `HttpSession` i `WebsocketSession` do analizy podanego adresu URL.

---
# Ä‘Ĺşâ€śâ€ž net.cpp
## Opis ogĂłlny

Plik `net.cpp` zawiera implementacjÄ™ funkcji pomocniczych do operacji na adresach IP, zadeklarowanych w `net.h`.
## Namespace `stdext`
## `std::string ip_to_string(uint32 ip)`

Konwertuje 32-bitowy adres IP z porzÄ…dku sieciowego na porzÄ…dek hosta, a nastÄ™pnie na `std::string` za pomocÄ… `boost::asio::ip::address_v4`.
## `uint32 string_to_ip(const std::string& string)`

Konwertuje `std::string` na obiekt `address_v4`, a nastÄ™pnie na 32-bitowÄ… liczbÄ™ w porzÄ…dku sieciowym.
## `std::vector<uint32> listSubnetAddresses(uint32 address, uint8 mask)`

Generuje listÄ™ wszystkich adresĂłw IP w podanej podsieci. Oblicza maskÄ™ bitowÄ… i iteruje po wszystkich moÄąÄ˝liwych adresach w zakresie, dodajÄ…c je do listy.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/stdext/net.h`: Plik nagÄąâ€šĂłwkowy.
-   `boost/asio`: UÄąÄ˝ywana do konwersji adresĂłw IP.
-   SÄ… to funkcje narzÄ™dziowe uÄąÄ˝ywane w logice sieciowej.

---
# Ä‘Ĺşâ€śâ€ž uri.cpp
## Opis ogĂłlny

Plik `uri.cpp` zawiera implementacjÄ™ funkcji `parseURI` do parsowania adresĂłw URL.
## Funkcja `parseURI`
## `ParsedURI parseURI(const std::string& url)`

UÄąÄ˝ywa wyraÄąÄ˝enia regularnego (`std::regex`) do rozbicia adresu URL na jego komponenty: protokĂłÄąâ€š, domenÄ™, port i Äąâ€şcieÄąÄ˝kÄ™/zapytanie. ObsÄąâ€šuguje protokoÄąâ€šy "http", "https", "ws", "wss" i poprawnie ustawia domyÄąâ€şlne porty (80 dla http/ws, 443 dla https/wss).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/stdext/uri.h`: Plik nagÄąâ€šĂłwkowy.
-   `<regex>`: Do parsowania.
-   `boost/algorithm/string.hpp`: Do konwersji na maÄąâ€še litery.
-   Jest uÄąÄ˝ywana przez `HttpSession` i `WebsocketSession`.

---
# Ä‘Ĺşâ€śâ€ž types.h
## Opis ogĂłlny

Plik `types.h` definiuje zestaw aliasĂłw dla typĂłw caÄąâ€škowitoliczbowych o staÄąâ€šym rozmiarze oraz inne podstawowe typy uÄąÄ˝ywane w caÄąâ€šym frameworku.
## Definicje typĂłw

-   **SkrĂłty**: `uchar`, `ushort`, `uint`, `ulong`.
-   **Liczby o staÄąâ€šym rozmiarze**: `uint64`, `uint32`, `uint16`, `uint8` oraz ich wersje ze znakiem (`int...`).
-   **`ticks_t`**: Alias dla `int64`, uÄąÄ˝ywany do przechowywania czasu w milisekundach lub mikrosekundach.
-   **`refcount_t`**: Typ dla licznika referencji.
-   **`size_t`, `ptrdiff_t`**: Importuje typy ze `std`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `<cstdint>`, `<cstddef>`: Standardowe nagÄąâ€šĂłwki.
-   Jest to fundamentalny plik, doÄąâ€šÄ…czany przez `stdext.h` i `global.h`, zapewniajÄ…cy spĂłjne i przenoÄąâ€şne typy danych w caÄąâ€šym projekcie.

---
# Ä‘Ĺşâ€śâ€ž format.h
## Opis ogĂłlny

Plik `format.h` zawiera implementacjÄ™ funkcji `stdext::format`, ktĂłra jest bezpiecznÄ… typowo alternatywÄ… dla `sprintf`, podobnÄ… do `boost::format` lub `fmt::format`.
## Funkcje
## `stdext::print(...)`

Funkcja debugujÄ…ca, ktĂłra wypisuje na konsolÄ™ dowolnÄ… liczbÄ™ argumentĂłw, oddzielajÄ…c je tabulatorami, podobnie jak `print` w Lua.
## `stdext::snprintf(...)`

Opakowanie na `snprintf` / `_snprintf`, ktĂłre potrafi obsÄąâ€šugiwaÄ‡ typy niestandardowe, takie jak `std::string`, poprzez `sprintf_cast`.
## `stdext::format(...)`

GÄąâ€šĂłwna funkcja.
-   **DziaÄąâ€šanie**:
    1.  WywoÄąâ€šuje `snprintf` z `NULL` jako buforem, aby obliczyÄ‡ wymaganÄ… dÄąâ€šugoÄąâ€şÄ‡ wynikowego stringa.
    2.  Alokuje `std::string` o odpowiednim rozmiarze.
    3.  WywoÄąâ€šuje `snprintf` ponownie, tym razem zapisujÄ…c wynik do bufora stringa.
-   **Zalety**: Jest w peÄąâ€šni bezpieczna (brak przepeÄąâ€šnienia bufora) i obsÄąâ€šuguje rĂłÄąÄ˝ne typy danych.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `stdext/traits.h`: Do analizy typĂłw.
-   `<tuple>`, `<sstream>`: Do metaprogramowania i formatowania.
-   Jest to kluczowe narzÄ™dzie uÄąÄ˝ywane w caÄąâ€šym projekcie do formatowania stringĂłw, szczegĂłlnie w logach i komunikatach o bÄąâ€šÄ™dach.

---
# Ä‘Ĺşâ€śâ€ž string.cpp
## Opis ogĂłlny

Plik `string.cpp` zawiera implementacjÄ™ funkcji pomocniczych do manipulacji stringami, zadeklarowanych w `string.h`.
## Funkcje

-   **`resolve_path(...)`**: Implementuje logikÄ™ Äąâ€šÄ…czenia Äąâ€şcieÄąÄ˝ek, obsÄąâ€šugujÄ…c Äąâ€şcieÄąÄ˝ki absolutne i wzglÄ™dne.
-   **`date_time_string()`, `timestamp_to_date(...)`**: UÄąÄ˝ywajÄ… `std::localtime` i `std::strftime` do formatowania daty i czasu.
-   **`dec_to_hex(...)`, `hex_to_dec(...)`**: UÄąÄ˝ywajÄ… `std::stringstream` do konwersji.
-   **Konwersje kodowania**: `is_valid_utf8` implementuje walidacjÄ™ bajt po bajcie. `utf8_to_latin1` i `latin1_to_utf8` implementujÄ… uproszczonÄ… konwersjÄ™. Wersje dla Windows (`..._to_utf16`) uÄąÄ˝ywajÄ… funkcji WinAPI `MultiByteToWideChar` i `WideCharToMultiByte`.
-   **Inne operacje**: `tolower`, `toupper`, `trim`, `ends_with`, `starts_with`, `replace_all`, `split` sÄ… opakowaniami na odpowiednie funkcje z biblioteki Boost.StringAlgo.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/stdext/string.h`, `format.h`.
-   `boost/algorithm/string.hpp`: Kluczowa zaleÄąÄ˝noÄąâ€şÄ‡ dla wielu operacji.
-   `physfs.h`: Potencjalnie, choÄ‡ nie jest bezpoÄąâ€şrednio uÄąÄ˝ywany.
-   NagÄąâ€šĂłwki WinAPI (dla konwersji kodowania).

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## Opis ogĂłlny

Plik `declarations.h` w module `ui` jest plikiem nagÄąâ€šĂłwkowym do wczesnych deklaracji (forward declarations) i definicji typĂłw dla klas interfejsu uÄąÄ˝ytkownika.
## Wczesne deklaracje

-   `UIManager`
-   `UIWidget`
-   `UITextEdit`
-   `UILayout` i wszystkie jego podklasy (`UIBoxLayout`, `UIGridLayout`, etc.)
-   `UIAnchor`, `UIAnchorGroup`, `UIAnchorLayout`
## Definicje typĂłw

-   `UIWidgetPtr`, `UITextEditPtr`, `UILayoutPtr`, ...: Aliasy dla `shared_object_ptr` do klas UI.
-   `UIWidgetList`: Alias dla `std::deque<UIWidgetPtr>`.
-   `UIAnchorList`: Alias dla `std::vector<UIAnchorPtr>`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doÄąâ€šÄ…czany przez wszystkie pliki nagÄąâ€šĂłwkowe w module `ui`.

---
# Ä‘Ĺşâ€śâ€ž ui.h
## Opis ogĂłlny

Plik `ui.h` jest gÄąâ€šĂłwnym, zbiorczym plikiem nagÄąâ€šĂłwkowym dla moduÄąâ€šu UI. Jego zadaniem jest doÄąâ€šÄ…czenie wszystkich najwaÄąÄ˝niejszych nagÄąâ€šĂłwkĂłw zwiÄ…zanych z interfejsem uÄąÄ˝ytkownika w jednym miejscu.
## ZawartoÄąâ€şÄ‡

DoÄąâ€šÄ…cza wszystkie podstawowe komponenty UI:
-   `uimanager.h`
-   `uiwidget.h`
-   `uitextedit.h`
-   `uilayout.h` i jego pochodne (`uihorizontallayout.h`, `uiverticallayout.h`, `uigridlayout.h`, `uianchorlayout.h`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   UÄąâ€šatwia doÄąâ€šÄ…czanie caÄąâ€šego podsystemu UI w innych czÄ™Äąâ€şciach projektu, ktĂłre go potrzebujÄ… (np. w plikach moduÄąâ€šĂłw gry).

---
# Ä‘Ĺşâ€śâ€ž uiboxlayout.cpp
## Opis ogĂłlny

Plik `uiboxlayout.cpp` zawiera implementacjÄ™ klasy `UIBoxLayout`, ktĂłra jest abstrakcyjnÄ… klasÄ… bazowÄ… dla layoutĂłw ukÄąâ€šadajÄ…cych widgety w jednej linii (poziomo lub pionowo).
## Klasa `UIBoxLayout`
## `UIBoxLayout::UIBoxLayout(UIWidgetPtr parentWidget)`

Konstruktor. WywoÄąâ€šuje konstruktor `UILayout` i inicjalizuje `m_spacing` na 0.
## `void UIBoxLayout::applyStyle(const OTMLNodePtr& styleNode)`

Parsuje atrybuty specyficzne dla `UIBoxLayout` z wÄ™zÄąâ€ša OTML.
-   `spacing`: OdstÄ™p miÄ™dzy widgetami.
-   `fit-children`: Flaga okreÄąâ€şlajÄ…ca, czy layout powinien dostosowaÄ‡ rozmiar rodzica do sumarycznego rozmiaru dzieci.
## `addWidget` i `removeWidget`

Te metody po prostu wywoÄąâ€šujÄ… `update()`, poniewaÄąÄ˝ kaÄąÄ˝da zmiana w liczbie dzieci wymaga ponownego przeliczenia layoutu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiboxlayout.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   Jest klasÄ… bazowÄ… dla `UIHorizontalLayout` i `UIVerticalLayout`.

---
# Ä‘Ĺşâ€śâ€ž uiboxlayout.h
## Opis ogĂłlny

Plik `uiboxlayout.h` deklaruje klasÄ™ `UIBoxLayout`, ktĂłra jest abstrakcyjnÄ… klasÄ… bazowÄ… dla layoutĂłw liniowych.
## Klasa `UIBoxLayout`
## Opis semantyczny
`UIBoxLayout` dziedziczy po `UILayout` i dodaje wspĂłlnÄ… funkcjonalnoÄąâ€şÄ‡ dla layoutĂłw horyzontalnych i wertykalnych, a mianowicie:
-   `spacing`: OdstÄ™p miÄ™dzy kolejnymi elementami.
-   `fit-children`: MoÄąÄ˝liwoÄąâ€şÄ‡ automatycznego dostosowania rozmiaru widgetu-rodzica, aby zmieÄąâ€şciÄąâ€š wszystkie swoje dzieci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setSpacing(int spacing)` | Ustawia odstÄ™p miÄ™dzy widgetami. |
| `setFitChildren(bool fitParent)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza dopasowywanie rozmiaru rodzica. |
## Zmienne chronione

-   `m_fitChildren`: Flaga `fit-children`.
-   `m_spacing`: WartoÄąâ€şÄ‡ odstÄ™pu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Jest klasÄ… bazowÄ… dla `UIHorizontalLayout` i `UIVerticalLayout`.
-   Oznaczona jako `@bindclass`, jej metody sÄ… dostÄ™pne w Lua.

---
# Ä‘Ĺşâ€śâ€ž uigridlayout.cpp
## Opis ogĂłlny

Plik `uigridlayout.cpp` zawiera implementacjÄ™ klasy `UIGridLayout`, ktĂłra ukÄąâ€šada widgety w siatce o staÄąâ€šym rozmiarze komĂłrek.
## Klasa `UIGridLayout`
## `UIGridLayout::UIGridLayout(...)`

Konstruktor, ustawia domyÄąâ€şlne wartoÄąâ€şci (rozmiar komĂłrki 16x16, 1 kolumna).
## `void UIGridLayout::applyStyle(...)`

Parsuje atrybuty specyficzne dla siatki z wÄ™zÄąâ€ša OTML, takie jak `cell-size`, `cell-spacing`, `num-columns`, `flow`.
## `bool UIGridLayout::internalUpdate()`
## Opis semantyczny
GÄąâ€šĂłwna metoda przeliczajÄ…ca pozycje widgetĂłw w siatce.
## DziaÄąâ€šanie
1.  Pobiera listÄ™ dzieci od rodzica.
2.  **Tryb `flow`**: JeÄąâ€şli wÄąâ€šÄ…czony, dynamicznie oblicza liczbÄ™ kolumn (`numColumns`), tak aby zmieÄąâ€şciÄąâ€šy siÄ™ w szerokoÄąâ€şci rodzica. Na podstawie tego oblicza liczbÄ™ wierszy.
3.  **Tryb `auto-spacing`**: JeÄąâ€şli wÄąâ€šÄ…czony, dynamicznie oblicza odstÄ™p miÄ™dzy komĂłrkami (`cellSpacing`), aby rĂłwnomiernie rozÄąâ€šoÄąÄ˝yÄ‡ je na caÄąâ€šej szerokoÄąâ€şci rodzica.
4.  W pÄ™tli przechodzi przez wszystkie widoczne widgety:
    -   Oblicza wiersz i kolumnÄ™ dla bieÄąÄ˝Ä…cego widgetu.
    -   Na tej podstawie oblicza jego pozycjÄ™.
    -   Ustawia docelowy prostokÄ…t (`Rect`) widgetu na rozmiar komĂłrki w obliczonej pozycji.
5.  **Tryb `fit-children`**: JeÄąâ€şli wÄąâ€šÄ…czony, oblicza wymaganÄ… wysokoÄąâ€şÄ‡ rodzica, aby zmieÄąâ€şciÄ‡ wszystkie wiersze, i planuje jej ustawienie w `EventDispatcher` (aby uniknÄ…Ä‡ problemĂłw z rekurencyjnymi aktualizacjami).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uigridlayout.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania wysokoÄąâ€şci rodzica.

---
# Ä‘Ĺşâ€śâ€ž uigridlayout.h
## Opis ogĂłlny

Plik `uigridlayout.h` deklaruje klasÄ™ `UIGridLayout`, ktĂłra implementuje layout siatkowy.
## Klasa `UIGridLayout`
## Opis semantyczny
`UIGridLayout` ukÄąâ€šada swoje widgety w regularnej siatce. MoÄąÄ˝e mieÄ‡ staÄąâ€šÄ… liczbÄ™ kolumn lub dynamicznie dostosowywaÄ‡ jÄ… do dostÄ™pnej przestrzeni (`flow`). Posiada rĂłwnieÄąÄ˝ opcje automatycznego dostosowywania odstÄ™pĂłw i rozmiaru rodzica.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setCellSize(...)` | Ustawia rozmiar pojedynczej komĂłrki siatki. |
| `setCellSpacing(...)` | Ustawia odstÄ™p miÄ™dzy komĂłrkami. |
| `setNumColumns(...)` | Ustawia staÄąâ€šÄ… liczbÄ™ kolumn. |
| `setNumLines(...)` | Ustawia maksymalnÄ… liczbÄ™ wierszy. |
| `setFlow(bool enable)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza tryb "pÄąâ€šynny", w ktĂłrym liczba kolumn jest dynamiczna. |
| `setAutoSpacing(bool enable)`| WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza automatyczne obliczanie odstÄ™pĂłw. |
| `setFitChildren(bool enable)`| WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza dopasowywanie wysokoÄąâ€şci rodzica. |
## Zmienne prywatne

-   `m_cellSize`: Rozmiar komĂłrki.
-   `m_cellSpacing`: OdstÄ™p miÄ™dzy komĂłrkami.
-   `m_numColumns`, `m_numLines`: Liczba kolumn i wierszy.
-   `m_autoSpacing`, `m_fitChildren`, `m_flow`: Flagi trybĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# Ä‘Ĺşâ€śâ€ž uihorizontallayout.cpp
## Opis ogĂłlny

Plik `uihorizontallayout.cpp` zawiera implementacjÄ™ klasy `UIHorizontalLayout`, ktĂłra ukÄąâ€šada widgety w jednym rzÄ™dzie, od lewej do prawej lub od prawej do lewej.
## Klasa `UIHorizontalLayout`
## `void UIHorizontalLayout::applyStyle(...)`

Parsuje atrybut `align-right` z wÄ™zÄąâ€ša OTML.
## `bool UIHorizontalLayout::internalUpdate()`
## Opis semantyczny
GÄąâ€šĂłwna metoda przeliczajÄ…ca pozycje widgetĂłw.
## DziaÄąâ€šanie
1.  Pobiera listÄ™ dzieci. JeÄąâ€şli `m_alignRight` jest `true`, odwraca kolejnoÄąâ€şÄ‡ listy.
2.  Iteruje po widgetach:
    -   Oblicza pozycjÄ™ `x` na podstawie pozycji i szerokoÄąâ€şci poprzedniego widgetu oraz odstÄ™pĂłw (`spacing`, `margin`).
    -   Oblicza pozycjÄ™ `y` w zaleÄąÄ˝noÄąâ€şci od wyrĂłwnania pionowego widgetu (`AlignTop`, `AlignBottom`, `AlignCenter`) wewnÄ…trz wysokoÄąâ€şci rodzica.
    -   JeÄąâ€şli widget nie ma staÄąâ€šego rozmiaru, jego wysokoÄąâ€şÄ‡ jest rozciÄ…gana do wysokoÄąâ€şci rodzica.
    -   Ustawia nowy `Rect` dla widgetu.
3.  Oblicza sumarycznÄ…, preferowanÄ… szerokoÄąâ€şÄ‡ (`preferredWidth`).
4.  JeÄąâ€şli `m_fitChildren` jest `true`, planuje asynchroniczne ustawienie szerokoÄąâ€şci rodzica na `preferredWidth`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uihorizontallayout.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania szerokoÄąâ€şci rodzica.

---
# Ä‘Ĺşâ€śâ€ž uihorizontallayout.h
## Opis ogĂłlny

Plik `uihorizontallayout.h` deklaruje klasÄ™ `UIHorizontalLayout`, ktĂłra implementuje layout horyzontalny.
## Klasa `UIHorizontalLayout`
## Opis semantyczny
`UIHorizontalLayout` dziedziczy po `UIBoxLayout` i specjalizuje go do ukÄąâ€šadania widgetĂłw w pojedynczym rzÄ™dzie. MoÄąÄ˝e ukÄąâ€šadaÄ‡ elementy od lewej do prawej (domyÄąâ€şlnie) lub od prawej do lewej (`align-right`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setAlignRight(bool alignRight)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza ukÄąâ€šadanie od prawej do lewej. |
## Zmienne chronione

-   `m_alignRight`: Flaga trybu wyrĂłwnania do prawej.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiboxlayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# Ä‘Ĺşâ€śâ€ž uilayout.cpp
## Opis ogĂłlny

Plik `uilayout.cpp` zawiera implementacjÄ™ klasy `UILayout`, ktĂłra jest abstrakcyjnÄ… klasÄ… bazowÄ… dla wszystkich menedÄąÄ˝erĂłw layoutu.
## Klasa `UILayout`
## `void UILayout::update()`
## Opis semantyczny
GÄąâ€šĂłwna metoda publiczna inicjujÄ…ca aktualizacjÄ™ layoutu.
## DziaÄąâ€šanie
1.  Sprawdza, czy aktualizacje nie sÄ… wyÄąâ€šÄ…czone (`m_updateDisabled`).
2.  Sprawdza, czy aktualizacja nie jest juÄąÄ˝ w toku (`m_updating`), aby zapobiec rekurencji. JeÄąâ€şli tak, planuje aktualizacjÄ™ na pĂłÄąĹźniej (`updateLater()`).
3.  Ustawia flagÄ™ `m_updating` na `true`.
4.  WywoÄąâ€šuje wirtualnÄ… metodÄ™ `internalUpdate()`, gdzie klasy pochodne implementujÄ… swojÄ… logikÄ™.
5.  WywoÄąâ€šuje `callback` `onLayoutUpdate` na widÄąÄ˝ecie-rodzicu.
6.  Resetuje flagÄ™ `m_updating`.
## `void UILayout::updateLater()`

Planuje wykonanie `update()` w nastÄ™pnej iteracji pÄ™tli `EventDispatcher`. Jest to mechanizm zapobiegajÄ…cy wielokrotnym, zbÄ™dnym przeliczeniom layoutu w tej samej klatce.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uilayout.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/ui/uiwidget.h`: KaÄąÄ˝dy layout jest powiÄ…zany z widgetem-rodzicem.
-   `framework/core/eventdispatcher.h`: Do planowania opĂłÄąĹźnionych aktualizacji.

---
# Ä‘Ĺşâ€śâ€ž uilayout.h
## Opis ogĂłlny

Plik `uilayout.h` deklaruje abstrakcyjnÄ… klasÄ™ bazowÄ… `UILayout`, ktĂłra definiuje wspĂłlny interfejs dla wszystkich klas zarzÄ…dzajÄ…cych pozycjÄ… i rozmiarem widgetĂłw-dzieci.
## Klasa `UILayout`
## Opis semantyczny
`UILayout` jest powiÄ…zany z jednym widgetem-rodzicem (`m_parentWidget`). Jego zadaniem jest automatyczne zarzÄ…dzanie geometriÄ… dzieci tego widgetu. KaÄąÄ˝da podklasa (`UIAnchorLayout`, `UIBoxLayout` itd.) implementuje inny algorytm ukÄąâ€šadania elementĂłw. Posiada mechanizmy do wÄąâ€šÄ…czania/wyÄąâ€šÄ…czania aktualizacji oraz do unikania rekurencyjnych i zbÄ™dnych przeliczeÄąâ€ž.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `UILayout(UIWidgetPtr parentWidget)`| Konstruktor. |
| `void update()` | Natychmiast ÄąÄ˝Ä…da przeliczenia layoutu. |
| `void updateLater()` | Planuje przeliczenie layoutu w najbliÄąÄ˝szej przyszÄąâ€šoÄąâ€şci. |
| `virtual void applyStyle(...)` | Stosuje wÄąâ€šaÄąâ€şciwoÄąâ€şci layoutu z wÄ™zÄąâ€ša OTML. |
| `virtual void addWidget(...)` | Powiadamia layout o dodaniu nowego widgetu. |
| `virtual void removeWidget(...)` | Powiadamia layout o usuniÄ™ciu widgetu. |
| `void disableUpdates()` / `enableUpdates()`| Tymczasowo wstrzymuje/wznawia aktualizacje layoutu. |
| `void setParent(...)` / `getParentWidget()` | ZarzÄ…dza powiÄ…zaniem z widgetem-rodzicem. |
| `bool isUpdating()` | Zwraca `true`, jeÄąâ€şli layout jest w trakcie aktualizacji. |
| `isUI...Layout()` | Metody RTTI (Run-Time Type Information) do identyfikacji typu layoutu. |
## Zmienne chronione

-   `m_updateDisabled`: Licznik blokad aktualizacji.
-   `m_updating`, `m_updateScheduled`: Flagi zapobiegajÄ…ce rekurencji i wielokrotnym aktualizacjom.
-   `m_parentWidget`: WskaÄąĹźnik do widgetu, ktĂłrego dzieÄ‡mi zarzÄ…dza layout.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/otml/otml.h`: Do parsowania stylĂłw.
-   Jest klasÄ… bazowÄ… dla wszystkich konkretnych implementacji layoutĂłw.
-   KaÄąÄ˝dy `UIWidget` moÄąÄ˝e mieÄ‡ jeden `UILayout`.

---
# Ä‘Ĺşâ€śâ€ž uimanager.h
## Opis ogĂłlny

Plik `uimanager.h` deklaruje klasÄ™ `UIManager`, ktĂłra jest singletonem (`g_ui`) i centralnym punktem zarzÄ…dzania caÄąâ€šym interfejsem uÄąÄ˝ytkownika.
## Klasa `UIManager`
## Opis semantyczny
`UIManager` zarzÄ…dza hierarchiÄ… widgetĂłw, poczynajÄ…c od korzenia (`m_rootWidget`). Odpowiada za propagacjÄ™ zdarzeÄąâ€ž wejÄąâ€şciowych (mysz, klawiatura), renderowanie, zarzÄ…dzanie stylami OTML oraz Äąâ€şledzenie globalnych stanĂłw UI, takich jak aktualnie wciÄąâ€şniÄ™ty, najechany czy przeciÄ…gany widget.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Inicjalizuje i zwalnia menedÄąÄ˝era. |
| `void render(Fw::DrawPane)`| Rozpoczyna proces renderowania UI dla danej warstwy. |
| `void resize(const Size&)` | Aktualizuje rozmiar `m_rootWidget`. |
| `void inputEvent(...)` | GÄąâ€šĂłwny punkt wejÄąâ€şcia dla wszystkich zdarzeÄąâ€ž wejÄąâ€şciowych. |
| `void clearStyles()` | CzyÄąâ€şci zaÄąâ€šadowane style. |
| `bool importStyle(...)` | ÄąÂaduje style z pliku `.otui`. |
| `OTMLNodePtr getStyle(...)` | Zwraca definicjÄ™ stylu o podanej nazwie. |
| `UIWidgetPtr loadUI(...)` | ÄąÂaduje i tworzy hierarchiÄ™ widgetĂłw z pliku `.otui`. |
| `UIWidgetPtr createWidget(...)` | Tworzy widget na podstawie nazwy stylu. |
| `setMouseReceiver(...)` / `setKeyboardReceiver(...)` | Ustawia widget, ktĂłry "przechwytuje" zdarzenia myszy/klawiatury. |
| `get...Widget()` | ZwracajÄ… wskaÄąĹźniki na widgety w okreÄąâ€şlonych stanach (przeciÄ…gany, najechany, wciÄąâ€şniÄ™ty). |
## Metody chronione (wywoÄąâ€šywane przez `UIWidget`)

-   `onWidgetAppear(...)`, `onWidgetDisappear(...)`, `onWidgetDestroy(...)`: Callbacki informujÄ…ce menedÄąÄ˝era o zmianach w drzewie widgetĂłw, co pozwala na aktualizacjÄ™ globalnych stanĂłw (np. `m_hoveredWidget`).
## Zmienne prywatne

-   `m_rootWidget`: KorzeÄąâ€ž drzewa widgetĂłw, wypeÄąâ€šnia caÄąâ€še okno.
-   `m_mouseReceiver`, `m_keyboardReceiver`: Widgety przechwytujÄ…ce zdarzenia.
-   `m_draggingWidget`, `m_hoveredWidget`, `m_pressedWidget`: ÄąĹˇledzÄ… globalne stany myszy.
-   `m_styles`: Mapa przechowujÄ…ca wszystkie zaÄąâ€šadowane style.
-   `m_destroyedWidgets`: Lista do Äąâ€şledzenia niszczonych widgetĂłw w celach debugowania wyciekĂłw pamiÄ™ci.
## Zmienne globalne

-   `g_ui`: Globalna instancja `UIManager`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/declarations.h`, `uiwidget.h`.
-   `framework/core/inputevent.h`.
-   ÄąĹˇciÄąâ€şle wspĂłÄąâ€špracuje z `GraphicalApplication` (ktĂłra przekazuje jej zdarzenia) i `PlatformWindow`.
-   ZarzÄ…dza cyklem ÄąÄ˝ycia i interakcjami wszystkich `UIWidget`.

---
# Ä‘Ĺşâ€śâ€ž uitextedit.cpp
## Opis ogĂłlny

Plik `uitextedit.cpp` zawiera implementacjÄ™ klasy `UITextEdit`, ktĂłra jest specjalizowanym widgetem do wprowadzania i edycji tekstu.
## Klasa `UITextEdit`
## `UITextEdit::UITextEdit()`

Konstruktor. Inicjalizuje wszystkie pola zwiÄ…zane z edycjÄ… tekstu do wartoÄąâ€şci domyÄąâ€şlnych (np. kursor na pozycji 0, widoczny, tekst edytowalny).
## `void UITextEdit::drawSelf(...)`

PrzesÄąâ€šoniÄ™ta metoda rysujÄ…ca.
1.  Rysuje tÄąâ€šo, ramkÄ™, obraz i ikonÄ™ (dziedziczone z `UIWidget`).
2.  JeÄąâ€şli tekst jest pusty, rysuje `placeholder`.
3.  Rysuje tekst, uÄąÄ˝ywajÄ…c `CoordsBuffer` (`m_glyphsTextCoordsBuffer`) do zbuforowania geometrii.
4.  Rysuje zaznaczenie, najpierw rysujÄ…c tÄąâ€šo zaznaczenia, a potem tekst w innym kolorze na wierzchu.
5.  Rysuje migajÄ…cy kursor w odpowiedniej pozycji.
## `void UITextEdit::update(bool focusCursor)`

Kluczowa metoda, ktĂłra przelicza caÄąâ€šÄ… geometriÄ™ tekstu.
1.  Pobiera tekst do wyÄąâ€şwietlenia (zwykÄąâ€šy lub ukryty `*`).
2.  Zawija tekst, jeÄąâ€şli `m_textWrap` jest wÄąâ€šÄ…czone.
3.  Oblicza pozycje wszystkich glifĂłw za pomocÄ… `m_font->calculateGlyphsPositions`.
4.  JeÄąâ€şli `m_autoScroll` i `focusCursor` sÄ… `true`, automatycznie przewija widok, tak aby kursor byÄąâ€š zawsze widoczny.
5.  Przelicza, ktĂłre glify sÄ… widoczne w obszarze widgetu, i generuje dla nich wspĂłÄąâ€šrzÄ™dne w `m_glyphsCoords`.
## Metody edycji tekstu

-   `setCursorPos`, `setSelection`, `clearSelection`, `selectAll`: ZarzÄ…dzajÄ… pozycjÄ… kursora i zaznaczeniem.
-   `appendText`, `appendCharacter`, `removeCharacter`: ModyfikujÄ… tekst.
-   `del`, `paste`, `copy`, `cut`: ImplementujÄ… standardowe operacje edycyjne.
## `int UITextEdit::getTextPos(Point pos)`

Konwertuje pozycjÄ™ myszy (w pikselach) na indeks znaku w tekÄąâ€şcie.
## ObsÄąâ€šuga zdarzeÄąâ€ž (`on...`)

PrzesÄąâ€šania metody obsÄąâ€šugi zdarzeÄąâ€ž z `UIWidget`, aby zaimplementowaÄ‡ logikÄ™ edycji tekstu:
-   `onKeyPress`: ObsÄąâ€šuguje nawigacjÄ™ (strzaÄąâ€ški, Home, End), usuwanie (Delete, Backspace), zaznaczanie (Shift + strzaÄąâ€ški), kopiowanie/wklejanie (Ctrl+C/V).
-   `onKeyText`: Wstawia wprowadzony tekst.
-   `onMousePress`, `onMouseMove`, `onDoubleClick`: ObsÄąâ€šugujÄ… ustawianie kursora i zaznaczanie tekstu myszÄ….
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uitextedit.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/graphics/bitmapfont.h`: Intensywnie uÄąÄ˝ywa `Bitmapfont` do obliczeÄąâ€ž.
-   `framework/platform/platformwindow.h`: Do interakcji ze schowkiem.
-   Na Androidzie, zamiast wÄąâ€šasnego renderowania, wywoÄąâ€šuje natywne pole edycji tekstu.

---
# Ä‘Ĺşâ€śâ€ž uimanager.cpp
## Opis ogĂłlny

Plik `uimanager.cpp` zawiera implementacjÄ™ klasy `UIManager`, ktĂłra jest centralnym menedÄąÄ˝erem interfejsu uÄąÄ˝ytkownika.
## Klasa `UIManager`
## `void UIManager::init()`

Inicjalizuje menedÄąÄ˝era, tworzÄ…c gÄąâ€šĂłwny, niewidoczny widget (`m_rootWidget`), ktĂłry jest korzeniem caÄąâ€šego drzewa UI i zajmuje caÄąâ€šÄ… powierzchniÄ™ okna.
## `void UIManager::render(Fw::DrawPane drawPane)`

Rozpoczyna proces renderowania, wywoÄąâ€šujÄ…c metodÄ™ `draw()` na `m_rootWidget` dla okreÄąâ€şlonej warstwy rysowania.
## `void UIManager::resize(const Size& size)`

Aktualizuje rozmiar `m_rootWidget`, co powoduje rekurencyjne przeliczenie layoutu dla wszystkich widgetĂłw potomnych.
## `void UIManager::inputEvent(const InputEvent& event)`
## Opis semantyczny
GÄąâ€šĂłwny punkt wejÄąâ€şcia dla wszystkich zdarzeÄąâ€ž wejÄąâ€şciowych. TÄąâ€šumaczy surowe zdarzenia na akcje w UI.
## DziaÄąâ€šanie
-   Dla zdarzeÄąâ€ž klawiatury, przekazuje je do `m_keyboardReceiver`.
-   Dla wciÄąâ€şniÄ™cia przycisku myszy:
    1.  Identyfikuje widget pod kursorem.
    2.  Aktualizuje `m_pressedWidget`.
    3.  Propaguje zdarzenie `onMousePress` w dĂłÄąâ€š drzewa.
-   Dla zwolnienia przycisku myszy:
    1.  JeÄąâ€şli trwaÄąâ€šo przeciÄ…ganie, koÄąâ€žczy je i obsÄąâ€šuguje "upuszczenie".
    2.  Propaguje zdarzenie `onMouseRelease`.
    3.  JeÄąâ€şli zwolnienie nastÄ…piÄąâ€šo nad pierwotnie wciÄąâ€şniÄ™tym widgetem, generuje zdarzenie `onClick`.
-   Dla ruchu myszy:
    1.  Aktualizuje `m_hoveredWidget`.
    2.  JeÄąâ€şli jakiÄąâ€ş widget jest wciÄąâ€şniÄ™ty i przeciÄ…galny, rozpoczyna przeciÄ…ganie.
    3.  Propaguje zdarzenie `onMouseMove`.
-   Dla kĂłÄąâ€ška myszy, propaguje zdarzenie.
## `void UIManager::update...Widget(...)`

Metody te zarzÄ…dzajÄ… globalnym stanem UI:
-   `updatePressedWidget`: Zmienia, ktĂłry widget jest aktualnie wciÄąâ€şniÄ™ty.
-   `updateDraggingWidget`: Rozpoczyna lub koÄąâ€žczy przeciÄ…ganie widgetu.
-   `updateHoveredWidget`: Aktualizuje, nad ktĂłrym widgetem znajduje siÄ™ kursor.
## `bool UIManager::importStyle(...)`

ÄąÂaduje i parsuje plik `.otui` ze stylami, dodajÄ…c je do `m_styles`.
## `UIWidgetPtr UIManager::loadUI(...)` i `createWidgetFromOTML(...)`

ImplementujÄ… logikÄ™ tworzenia widgetĂłw na podstawie plikĂłw i wÄ™zÄąâ€šĂłw OTML. `createWidgetFromOTML` jest kluczowÄ… metodÄ…, ktĂłra:
1.  Znajduje styl bazowy.
2.  ÄąÂÄ…czy (merge) go ze stylem zdefiniowanym w pliku UI.
3.  Na podstawie atrybutu `__class`, wywoÄąâ€šuje w Lua funkcjÄ™ fabrycznÄ… (`create`) dla danego typu widgetu.
4.  Stosuje styl i rekurencyjnie tworzy dzieci.
## `void UIManager::onWidgetDestroy(...)`

Callback wywoÄąâ€šywany przez `UIWidget`. CzyÄąâ€şci wszystkie globalne referencje do niszczonego widgetu (np. `m_hoveredWidget`, `m_pressedWidget`). W trybie debugowania, planuje sprawdzenie, czy nie pozostaÄąâ€šy ÄąÄ˝adne wiszÄ…ce referencje do widgetu po jego zniszczeniu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to centralna klasa UI, ktĂłra Äąâ€šÄ…czy `PlatformWindow` (ÄąĹźrĂłdÄąâ€šo zdarzeÄąâ€ž) z `UIWidget` (odbiorcy zdarzeÄąâ€ž).
-   ZarzÄ…dza caÄąâ€šym drzewem widgetĂłw.
-   WspĂłÄąâ€špracuje z `OTML` do parsowania stylĂłw i layoutĂłw.

---
# Ä‘Ĺşâ€śâ€ž uitextedit.h
## Opis ogĂłlny

Plik `uitextedit.h` deklaruje klasÄ™ `UITextEdit`, ktĂłra jest widgetem sÄąâ€šuÄąÄ˝Ä…cym do wprowadzania i edycji tekstu przez uÄąÄ˝ytkownika.
## Klasa `UITextEdit`
## Opis semantyczny
`UITextEdit` dziedziczy po `UIWidget` i rozszerza jego funkcjonalnoÄąâ€şÄ‡ o logikÄ™ obsÄąâ€šugi kursora, zaznaczania tekstu, wprowadzania z klawiatury, kopiowania/wklejania i zawijania wierszy. Jest to jeden z najbardziej zÄąâ€šoÄąÄ˝onych widgetĂłw w podstawowym zestawie.
## Metody publiczne
## ZarzÄ…dzanie tekstem i kursorem
-   `setCursorPos(...)`: Ustawia pozycjÄ™ kursora.
-   `setSelection(...)`: Ustawia zaznaczenie.
-   `setTextHidden(...)`: WÄąâ€šÄ…cza tryb "hasÄąâ€ša" (wyÄąâ€şwietla `*`).
-   `setMaxLength(...)`: Ustawia maksymalnÄ… dÄąâ€šugoÄąâ€şÄ‡ tekstu.
-   `appendText(...)`: Dodaje tekst w pozycji kursora.
-   `del()`, `paste()`, `copy()`, `cut()`: Standardowe operacje edycyjne.
-   `selectAll()`, `clearSelection()`: ZarzÄ…dzanie zaznaczeniem.
## Konfiguracja
-   `setEditable(...)`: WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza moÄąÄ˝liwoÄąâ€şÄ‡ edycji.
-   `setMultiline(...)`: WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza tryb wieloliniowy.
-   `setValidCharacters(...)`: Ogranicza dozwolone znaki.
-   `setPlaceholder(...)`: Ustawia tekst wyÄąâ€şwietlany, gdy pole jest puste.
## Gettery
-   `getCursorPos()`, `getSelection()`, `getTextPos(...)`, ...: ZwracajÄ… informacje o stanie edytora.
## Zmienne prywatne

-   `m_cursorPos`: Pozycja kursora.
-   `m_selectionStart`, `m_selectionEnd`: Granice zaznaczenia.
-   `m_textHidden`, `m_multiline`, `m_editable`, ...: Flagi konfiguracyjne.
-   `m_glyphsCoords`, `m_glyphsTexCoords`: Wektory przechowujÄ…ce geometriÄ™ renderowanego tekstu.
-   `m_glyphsTextCoordsBuffer`, `m_glyphsSelectCoordsBuffer`: Bufory `CoordsBuffer` dla tekstu i zaznaczenia.
-   `m_placeholder`, `m_placeholderColor`, ...: WÄąâ€šaÄąâ€şciwoÄąâ€şci placeholdera.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiwidget.h`: Klasa bazowa.
-   Jest oznaczona jako `@bindclass`, co udostÄ™pnia jej bogate API w Lua.
-   Jest jednym z podstawowych, predefiniowanych typĂłw widgetĂłw tworzonych przez `UIManager`.

---
# Ä‘Ĺşâ€śâ€ž uitranslator.cpp
## Opis ogĂłlny

Plik `uitranslator.cpp` zawiera implementacje funkcji, ktĂłre tÄąâ€šumaczÄ… tekstowe reprezentacje rĂłÄąÄ˝nych enumĂłw uÄąÄ˝ywanych w UI na ich faktyczne wartoÄąâ€şci liczbowe.
## Namespace `Fw`
## `Fw::AlignmentFlag Fw::translateAlignment(std::string aligment)`

Konwertuje string (np. "top-left", "center") na odpowiedniÄ… flagÄ™ z `Fw::AlignmentFlag`. UÄąÄ˝ywa `boost::to_lower` i `boost::erase_all` do normalizacji wejÄąâ€şcia.
## `Fw::AnchorEdge Fw::translateAnchorEdge(std::string anchorEdge)`

Konwertuje string (np. "left", "horizontal-center") na odpowiedniÄ… wartoÄąâ€şÄ‡ z `Fw::AnchorEdge`.
## `Fw::WidgetState Fw::translateState(std::string state)`

Konwertuje string (np. "hover", "pressed") na odpowiedniÄ… flagÄ™ z `Fw::WidgetState`.
## `Fw::AutoFocusPolicy Fw::translateAutoFocusPolicy(std::string policy)`

Konwertuje string (np. "first", "last") na odpowiedniÄ… wartoÄąâ€şÄ‡ z `Fw::AutoFocusPolicy`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uitranslator.h`: Plik nagÄąâ€šĂłwkowy.
-   `boost/algorithm/string.hpp`: Do normalizacji stringĂłw.
-   Funkcje te sÄ… uÄąÄ˝ywane przez `UIWidget` i jego podklasy podczas parsowania stylĂłw z OTML, aby przekonwertowaÄ‡ wartoÄąâ€şci tekstowe na enumy.

---
# Ä‘Ĺşâ€śâ€ž uitranslator.h
## Opis ogĂłlny

Plik `uitranslator.h` deklaruje zestaw funkcji pomocniczych do konwersji stringĂłw na wartoÄąâ€şci wyliczeniowe (enum) uÄąÄ˝ywane w systemie UI.
## Namespace `Fw`
## Deklaracje funkcji

| Funkcja | Opis |
| :--- | :--- |
| `AlignmentFlag translateAlignment(...)`| Konwertuje string na `Fw::AlignmentFlag`. |
| `AnchorEdge translateAnchorEdge(...)` | Konwertuje string na `Fw::AnchorEdge`. |
| `WidgetState translateState(...)` | Konwertuje string na `Fw::WidgetState`. |
| `AutoFocusPolicy translateAutoFocusPolicy(...)`| Konwertuje string na `Fw::AutoFocusPolicy`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/const.h`: Definicje enumĂłw.
-   `<string>`: Do operacji na stringach.
-   Te funkcje sÄ… kluczowe dla parsowania plikĂłw OTML, gdzie wÄąâ€šaÄąâ€şciwoÄąâ€şci takie jak wyrĂłwnanie sÄ… zdefiniowane za pomocÄ… sÄąâ€šĂłw kluczowych.

---
# Ä‘Ĺşâ€śâ€ž uiverticallayout.cpp
## Opis ogĂłlny

Plik `uiverticallayout.cpp` zawiera implementacjÄ™ klasy `UIVerticalLayout`, ktĂłra ukÄąâ€šada widgety w jednej kolumnie, od gĂłry do doÄąâ€šu lub od doÄąâ€šu do gĂłry.
## Klasa `UIVerticalLayout`
## `void UIVerticalLayout::applyStyle(...)`

Parsuje atrybut `align-bottom` z wÄ™zÄąâ€ša OTML.
## `bool UIVerticalLayout::internalUpdate()`
## Opis semantyczny
GÄąâ€šĂłwna metoda przeliczajÄ…ca pozycje widgetĂłw. DziaÄąâ€ša analogicznie do `UIHorizontalLayout::internalUpdate`, ale operuje na osi Y.
## DziaÄąâ€šanie
1.  Pobiera listÄ™ dzieci. JeÄąâ€şli `m_alignBottom` jest `true`, odwraca kolejnoÄąâ€şÄ‡ listy.
2.  Iteruje po widgetach:
    -   Oblicza pozycjÄ™ `y` na podstawie pozycji i wysokoÄąâ€şci poprzedniego widgetu oraz odstÄ™pĂłw.
    -   Oblicza pozycjÄ™ `x` w zaleÄąÄ˝noÄąâ€şci od wyrĂłwnania poziomego widgetu (`AlignLeft`, `AlignRight`, `AlignCenter`) wewnÄ…trz szerokoÄąâ€şci rodzica.
    -   JeÄąâ€şli widget nie ma staÄąâ€šego rozmiaru, jego szerokoÄąâ€şÄ‡ jest rozciÄ…gana do szerokoÄąâ€şci rodzica.
    -   Ustawia nowy `Rect` dla widgetu.
3.  Oblicza sumarycznÄ…, preferowanÄ… wysokoÄąâ€şÄ‡ (`preferredHeight`).
4.  JeÄąâ€şli `m_fitChildren` jest `true`, planuje asynchroniczne ustawienie wysokoÄąâ€şci rodzica na `preferredHeight`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiverticallayout.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania wysokoÄąâ€şci rodzica.

---
# Ä‘Ĺşâ€śâ€ž uiverticallayout.h
## Opis ogĂłlny

Plik `uiverticallayout.h` deklaruje klasÄ™ `UIVerticalLayout`, ktĂłra implementuje layout wertykalny.
## Klasa `UIVerticalLayout`
## Opis semantyczny
`UIVerticalLayout` dziedziczy po `UIBoxLayout` i specjalizuje go do ukÄąâ€šadania widgetĂłw w pojedynczej kolumnie. MoÄąÄ˝e ukÄąâ€šadaÄ‡ elementy od gĂłry do doÄąâ€šu (domyÄąâ€şlnie) lub od doÄąâ€šu do gĂłry (`align-bottom`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setAlignBottom(bool alignBottom)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza ukÄąâ€šadanie od doÄąâ€šu do gĂłry. |
| `isAlignBottom()` | Zwraca stan flagi `align-bottom`. |
## Zmienne chronione

-   `m_alignBottom`: Flaga trybu wyrĂłwnania do doÄąâ€šu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiboxlayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# Ä‘Ĺşâ€śâ€ž uiwidget.cpp
## Opis ogĂłlny

Plik `uiwidget.cpp` jest gÄąâ€šĂłwnym plikiem implementacyjnym dla klasy `UIWidget`. Zawiera on logikÄ™ dla podstawowych operacji na widgetach, takich jak zarzÄ…dzanie dzieÄ‡mi, obsÄąâ€šuga layoutĂłw, zdarzeÄąâ€ž, stanĂłw i stylĂłw.
## Klasa `UIWidget`
## `UIWidget::UIWidget()`

Konstruktor. Inicjalizuje wszystkie pola do wartoÄąâ€şci domyÄąâ€şlnych, w tym podstawowy styl, wÄąâ€šaÄąâ€şciwoÄąâ€şci tekstu i obrazu. Co waÄąÄ˝ne, zapisuje Äąâ€şcieÄąÄ˝kÄ™ do skryptu Lua, w ktĂłrym widget zostaÄąâ€š utworzony (`m_source`), co jest niezwykle przydatne do debugowania.
## `void UIWidget::draw(...)`

GÄąâ€šĂłwna metoda renderujÄ…ca. Jest rekurencyjna.
1.  WywoÄąâ€šuje `drawSelf()` do narysowania samego widgetu.
2.  JeÄąâ€şli wÄąâ€šÄ…czone jest przycinanie (`m_clipping`), ustawia odpowiedni `DrawQueueConditionClip`.
3.  WywoÄąâ€šuje `drawChildren()` do narysowania wszystkich widocznych dzieci.
4.  Stosuje globalne efekty dla widgetu i jego dzieci, takie jak przezroczystoÄąâ€şÄ‡ (`setOpacity`) i rotacja (`setRotation`), dodajÄ…c odpowiednie warunki do `DrawQueue`.
## `void UIWidget::addChild(...)`, `insertChild(...)`, `removeChild(...)`

Metody do zarzÄ…dzania hierarchiÄ… widgetĂłw. Poza modyfikacjÄ… `m_children`, dbajÄ… o:
-   Ustawienie/zresetowanie wskaÄąĹźnika `m_parent` w dziecku.
-   Dodanie/usuniÄ™cie widgetu z layoutu rodzica.
-   AktualizacjÄ™ stanu fokusu, jeÄąâ€şli usuwane jest dziecko z fokusem.
-   AktualizacjÄ™ stanĂłw indeksowych (`FirstState`, `LastState`) u rodzeÄąâ€žstwa.
-   Powiadomienie `UIManager` o pojawieniu siÄ™/znikniÄ™ciu widgetu.
## `void UIWidget::focusChild(...)`, `focusNextChild(...)`, `focusPreviousChild(...)`

ImplementujÄ… logikÄ™ zarzÄ…dzania fokusem wewnÄ…trz widgetu. `focusChild` zmienia `m_focusedChild` i wywoÄąâ€šuje callbacki `onFocusChange`. `focusNext/PreviousChild` implementujÄ… nawigacjÄ™ (np. klawiszem Tab).
## `void UIWidget::applyStyle(const OTMLNodePtr& styleNode)`

Aplikuje wÄąâ€šaÄąâ€şciwoÄąâ€şci z wÄ™zÄąâ€ša stylu do widgetu. WywoÄąâ€šuje `onStyleApply` oraz `onStyleApply` w Lua.
## `void UIWidget::updateState(Fw::WidgetState state)`

Kluczowa metoda, ktĂłra aktualizuje pojedynczÄ… flagÄ™ stanu (np. `HoverState`). Oblicza, czy widget powinien mieÄ‡ dany stan (np. dla `HoverState` sprawdza, czy `g_ui.getHoveredWidget() == this`), a nastÄ™pnie wywoÄąâ€šuje `setState`.
## `void UIWidget::updateStates()`

WywoÄąâ€šuje `updateState` dla wszystkich moÄąÄ˝liwych stanĂłw, synchronizujÄ…c peÄąâ€šny stan widgetu.
## `void UIWidget::updateStyle()`

Gdy stan widgetu siÄ™ zmienia, ta metoda jest wywoÄąâ€šywana. Przebudowuje ona tymczasowy wÄ™zeÄąâ€š stylu (`m_stateStyle`), Äąâ€šÄ…czÄ…c style z warunkĂłw (`$!hover`, `$checked`, itp.), a nastÄ™pnie wywoÄąâ€šuje `applyStyle` z tym nowym, poÄąâ€šÄ…czonym stylem.
## Metody `on...` i `propagateOn...`

ImplementujÄ… domyÄąâ€şlnÄ… obsÄąâ€šugÄ™ i propagacjÄ™ zdarzeÄąâ€ž w drzewie widgetĂłw. Metody `propagate...` decydujÄ…, do ktĂłrych dzieci przekazaÄ‡ zdarzenie, a nastÄ™pnie wywoÄąâ€šujÄ… metodÄ™ `on...` na samym widgecie.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   Jest to centralna klasa moduÄąâ€šu UI, ktĂłra zaleÄąÄ˝y od prawie wszystkich innych jego czÄ™Äąâ€şci (`UIManager`, `UILayout`, `UITranslator`) oraz wielu moduÄąâ€šĂłw frameworka (`Graphics`, `LuaInterface`, `EventDispatcher`, `OTML`).

---
# Ä‘Ĺşâ€śâ€ž uiwidget.h
## Opis ogĂłlny

Plik `uiwidget.h` deklaruje klasÄ™ `UIWidget`, ktĂłra jest fundamentalnÄ… klasÄ… bazowÄ… dla wszystkich elementĂłw interfejsu uÄąÄ˝ytkownika.
## Struktura `EdgeGroup`

Szablonowa struktura pomocnicza do przechowywania wartoÄąâ€şci dla czterech krawÄ™dzi (gĂłra, prawo, dĂłÄąâ€š, lewo), uÄąÄ˝ywana dla `margin`, `padding`, `border-width` i `border-color`.
## Klasa `UIWidget`
## Opis semantyczny
`UIWidget` jest obiektowym odpowiednikiem elementu DOM. Reprezentuje prostokÄ…tny obszar na ekranie, ktĂłry moÄąÄ˝e byÄ‡ rysowany, reagowaÄ‡ na zdarzenia i zawieraÄ‡ inne widgety. Implementuje model drzewa (rodzic-dzieci), system zdarzeÄąâ€ž (propagacja i obsÄąâ€šuga), system stanĂłw (aktywny, najechany, etc.), zarzÄ…dzanie layoutem oraz integracjÄ™ z OTML i Lua.
## PodziaÄąâ€š interfejsu (w pliku `.h`)

Interfejs klasy jest podzielony na sekcje tematyczne:
-   **Widget Core**: Podstawowe metody do zarzÄ…dzania hierarchiÄ…, layoutem, stylami i stanami.
-   **State Management**: Metody do zarzÄ…dzania stanami (`setState`, `hasState`).
-   **Event Processing**: Wirtualne metody `on...` do obsÄąâ€šugi zdarzeÄąâ€ž.
-   **Function Shortcuts**: Wygodne metody opakowujÄ…ce (`hide`, `show`, `enable`).
-   **Base Style**: Pola i metody zwiÄ…zane z podstawowymi wÄąâ€šaÄąâ€şciwoÄąâ€şciami wizualnymi (tÄąâ€šo, ramka, ikona, przezroczystoÄąâ€şÄ‡).
-   **Image**: Pola i metody zwiÄ…zane z wyÄąâ€şwietlaniem obrazu (`m_imageTexture`, `setImageSource`).
-   **Text**: Pola i metody zwiÄ…zane z wyÄąâ€şwietlaniem tekstu (`m_text`, `m_font`, `setText`).
## Kluczowe wÄąâ€šaÄąâ€şciwoÄąâ€şci

-   **Hierarchia**: `m_parent`, `m_children`.
-   **Geometria**: `m_rect`.
-   **Styl**: `m_style` (wÄ™zeÄąâ€š OTML), `m_states`.
-   **Layout**: `m_layout`.
-   **Zdarzenia**: Zestaw wirtualnych metod `on...` (np. `onMousePress`, `onKeyPress`).
-   **WyglÄ…d**: `m_backgroundColor`, `m_borderColor`, `m_imageTexture`, `m_text`, `m_font`, etc.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/declarations.h`, `uilayout.h`.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   Jest klasÄ… bazowÄ… dla wszystkich innych widgetĂłw, np. `UITextEdit`.
-   Jest zarzÄ…dzana przez `UIManager`.

---
# Ä‘Ĺşâ€śâ€ž uiwidgetimage.cpp
## Opis ogĂłlny

Plik `uiwidgetimage.cpp` zawiera implementacjÄ™ czÄ™Äąâ€şci klasy `UIWidget` odpowiedzialnej za obsÄąâ€šugÄ™ i renderowanie obrazu tÄąâ€ša.

> **NOTE:** To nie jest osobna klasa, lecz czÄ™Äąâ€şÄ‡ implementacji `UIWidget`, wydzielona do osobnego pliku dla lepszej organizacji kodu.
## Klasa `UIWidget` (czÄ™Äąâ€şÄ‡ implementacji)
## `void UIWidget::initImage()`

Inicjalizuje pola zwiÄ…zane z obrazem do wartoÄąâ€şci domyÄąâ€şlnych.
## `void UIWidget::parseImageStyle(const OTMLNodePtr& styleNode)`

Parsuje z wÄ™zÄąâ€ša OTML wszystkie atrybuty zwiÄ…zane z obrazem (`image-source`, `image-clip`, `image-color`, `image-border`, `image-shader` itp.) i wywoÄąâ€šuje odpowiednie settery.
## `void UIWidget::drawImage(const Rect& screenCoords)`
## Opis semantyczny
GÄąâ€šĂłwna metoda rysujÄ…ca obraz.
## DziaÄąâ€šanie
1.  Sprawdza, czy tekstura obrazu istnieje.
2.  JeÄąâ€şli geometria (`screenCoords`) lub wÄąâ€šaÄąâ€şciwoÄąâ€şci obrazu ulegÄąâ€šy zmianie (`m_imageMustRecache`), przelicza i buforuje wspĂłÄąâ€šrzÄ™dne wierzchoÄąâ€škĂłw i tekstur w `m_imageCoordsBuffer`.
    -   ObsÄąâ€šuguje rĂłÄąÄ˝ne tryby: proste skalowanie, zachowanie proporcji (`m_imageFixedRatio`), powtarzanie (`m_imageRepeated`) oraz zÄąâ€šoÄąÄ˝one rysowanie z ramkÄ… (`m_imageBordered`), ktĂłre dzieli obraz na 9 czÄ™Äąâ€şci i odpowiednio je skaluje/powtarza.
3.  Dodaje zadanie rysowania do `g_drawQueue`. JeÄąâ€şli zdefiniowano `m_shader`, uÄąÄ˝ywa specjalnego `DrawQueueItemImageWithShader`.
## `void UIWidget::setQRCode(...)`

Generuje obraz kodu QR, tworzy z niego teksturÄ™ i ustawia jÄ… jako `m_imageTexture`.
## `void UIWidget::setImageSource(const std::string& source)`

ÄąÂaduje teksturÄ™ z pliku za pomocÄ… `g_textures` i ustawia jÄ… jako `m_imageTexture`. JeÄąâ€şli wÄąâ€šÄ…czone jest `m_imageAutoResize`, dostosowuje rozmiar widgetu do rozmiaru obrazu.
## `void UIWidget::setImageSourceBase64(...)`

Dekoduje obraz zakodowany w Base64, tworzy z niego teksturÄ™ i ustawia jÄ….
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiwidget.h`: Plik nagÄąâ€šĂłwkowy klasy, ktĂłrÄ… implementuje.
-   `framework/graphics/painter.h`, `image.h`, `texture.h`, `texturemanager.h`: Komponenty graficzne.
-   `framework/util/crypt.h`: Do dekodowania Base64.

---
# Ä‘Ĺşâ€śâ€ž uianchorlayout.h
## Opis ogĂłlny

Plik `uianchorlayout.h` deklaruje klasy `UIAnchor`, `UIAnchorGroup` i `UIAnchorLayout`, ktĂłre razem implementujÄ… system layoutu oparty na "kotwicach" (anchors).
## Klasa `UIAnchor`
## Opis semantyczny
Reprezentuje pojedynczÄ… reguÄąâ€šÄ™ "kotwiczenia", ktĂłra wiÄ…ÄąÄ˝e jednÄ… krawÄ™dÄąĹź widgetu z krawÄ™dziÄ… innego widgetu (lub rodzica).

-   **Pola**: `m_anchoredEdge` (krawÄ™dÄąĹź tego widgetu), `m_hookedWidgetId` (ID widgetu docelowego), `m_hookedEdge` (krawÄ™dÄąĹź widgetu docelowego).
## Klasa `UIAnchorGroup`
## Opis semantyczny
Kontener na wszystkie kotwice (`UIAnchor`) przypisane do jednego widgetu. Posiada rĂłwnieÄąÄ˝ flagÄ™ `m_updated` uÄąÄ˝ywanÄ… przez algorytm layoutu.
## Klasa `UIAnchorLayout`
## Opis semantyczny
`UIAnchorLayout` to menedÄąÄ˝er layoutu, ktĂłry pozycjonuje i skaluje swoje widgety-dzieci na podstawie zdefiniowanych dla nich reguÄąâ€š kotwiczenia. Pozwala to na tworzenie elastycznych i responsywnych interfejsĂłw, ktĂłre dostosowujÄ… siÄ™ do zmian rozmiaru okna.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `addAnchor(...)` | Dodaje nowÄ… reguÄąâ€šÄ™ kotwiczenia dla widgetu. |
| `removeAnchors(...)` | Usuwa wszystkie kotwice z widgetu. |
| `hasAnchors(...)` | Sprawdza, czy widget ma jakiekolwiek kotwice. |
| `centerIn(...)` | SkrĂłt do dodania kotwic centrujÄ…cych widget. |
| `fill(...)` | SkrĂłt do dodania kotwic rozciÄ…gajÄ…cych widget na caÄąâ€šy obszar innego widgetu. |
## Zmienne prywatne

-   `m_anchorsGroups`: Mapa przechowujÄ…ca `UIAnchorGroup` dla kaÄąÄ˝dego zarzÄ…dzanego widgetu.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.
-   Jest jednym z najczÄ™Äąâ€şciej uÄąÄ˝ywanych layoutĂłw w projekcie.

---
# Ä‘Ĺşâ€śâ€ž uiwidgettext.cpp
## Opis ogĂłlny

Plik `uiwidgettext.cpp` zawiera implementacjÄ™ czÄ™Äąâ€şci klasy `UIWidget` odpowiedzialnej za obsÄąâ€šugÄ™ i renderowanie tekstu.

> **NOTE:** To nie jest osobna klasa, lecz czÄ™Äąâ€şÄ‡ implementacji `UIWidget`, wydzielona do osobnego pliku.
## Klasa `UIWidget` (czÄ™Äąâ€şÄ‡ implementacji)
## `void UIWidget::initText()`

Inicjalizuje pola zwiÄ…zane z tekstem do wartoÄąâ€şci domyÄąâ€şlnych (np. domyÄąâ€şlny font, wyrĂłwnanie do Äąâ€şrodka).
## `void UIWidget::updateText()`

Metoda wywoÄąâ€šywana po kaÄąÄ˝dej zmianie tekstu lub jego wÄąâ€šaÄąâ€şciwoÄąâ€şci.
1.  JeÄąâ€şli zawijanie jest wÄąâ€šÄ…czone, wywoÄąâ€šuje `m_font->wrapText()`, aby przygotowaÄ‡ tekst do wyÄąâ€şwietlenia (`m_drawText`).
2.  JeÄąâ€şli wÄąâ€šÄ…czone jest `m_textAutoResize`, oblicza nowy, preferowany rozmiar widgetu na podstawie rozmiaru tekstu i go ustawia.
3.  Ustawia flagÄ™ `m_textMustRecache`, aby geometria zostaÄąâ€ša przeliczona przy nastÄ™pnym rysowaniu.
## `void UIWidget::parseTextStyle(...)`

Parsuje z wÄ™zÄąâ€ša OTML wszystkie atrybuty zwiÄ…zane z tekstem (`text`, `font`, `text-align`, `text-wrap` itp.).
## `void UIWidget::drawText(const Rect& screenCoords)`

Dodaje zadanie rysowania tekstu do `g_drawQueue`. UÄąÄ˝ywa `m_font` do wykonania wÄąâ€šaÄąâ€şciwej operacji rysowania, przekazujÄ…c mu tekst (`m_drawText`), obszar (`m_textCachedScreenCoords`), wyrĂłwnanie, kolor i ewentualne informacje o wielu kolorach.
## `void UIWidget::onTextChange(...)` i `onFontChange(...)`

Wirtualne metody, ktĂłre domyÄąâ€şlnie wywoÄąâ€šujÄ… odpowiednie `callbacki` w Lua.
## `void UIWidget::setText(std::string text, ...)`

GÄąâ€šĂłwny setter dla tekstu. JeÄąâ€şli `m_textOnlyUpperCase` jest `true`, konwertuje tekst na wielkie litery. Aktualizuje `m_text`, wywoÄąâ€šuje `updateText()` i `onTextChange`.
## `void UIWidget::setColoredText(...)`

Setter dla tekstu wielokolorowego. Parsuje wektor stringĂłw, budujÄ…c `m_text` i `m_textColors`.
## `void UIWidget::setFont(...)`

Ustawia font, pobierajÄ…c go z `g_fonts`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiwidget.h`.
-   `framework/ui/uitranslator.h`: Do parsowania `text-align`.
-   `framework/graphics/fontmanager.h`: Do pobierania fontĂłw.

---
# Ä‘Ĺşâ€śâ€ž uiwidgetbasestyle.cpp
## Opis ogĂłlny

Plik `uiwidgetbasestyle.cpp` zawiera implementacjÄ™ czÄ™Äąâ€şci klasy `UIWidget` odpowiedzialnej za podstawowy styl, czyli wÄąâ€šaÄąâ€şciwoÄąâ€şci wspĂłlne dla wszystkich widgetĂłw, takie jak tÄąâ€šo, ramka, ikona i ogĂłlne atrybuty.
## Klasa `UIWidget` (czÄ™Äąâ€şÄ‡ implementacji)
## `void UIWidget::initBaseStyle()`

Inicjalizuje podstawowe wÄąâ€šaÄąâ€şciwoÄąâ€şci stylu do wartoÄąâ€şci domyÄąâ€şlnych (np. przezroczyste tÄąâ€šo, biaÄąâ€šy kolor, brak ramki).
## `void UIWidget::parseBaseStyle(const OTMLNodePtr& styleNode)`

GÄąâ€šĂłwna metoda parsujÄ…ca styl.
1.  Najpierw parsuje pola i `callbacki` Lua (`@` i `&`), aby byÄąâ€šy dostÄ™pne podczas parsowania innych atrybutĂłw.
2.  NastÄ™pnie parsuje wszystkie podstawowe atrybuty, takie jak `color`, `x`, `y`, `width`, `height`, `background-color`, `opacity`, `rotation`, `enabled`, `visible`, `margin`, `padding`, `border`, `icon`, etc.
3.  ObsÄąâ€šuguje rĂłwnieÄąÄ˝ definicjÄ™ layoutu (`layout: ...`) oraz deklaracje kotwic (`anchors.left: ...`).
## `void UIWidget::drawBackground(const Rect& screenCoords)`

Dodaje do `g_drawQueue` zadanie narysowania prostokÄ…ta wypeÄąâ€šnionego kolorem `m_backgroundColor`.
## `void UIWidget::drawBorder(const Rect& screenCoords)`

Dodaje do `g_drawQueue` zadania narysowania czterech prostokÄ…tĂłw tworzÄ…cych ramkÄ™, kaÄąÄ˝dy z odpowiednim kolorem i gruboÄąâ€şciÄ….
## `void UIWidget::drawIcon(const Rect& screenCoords)`

JeÄąâ€şli `m_icon` jest ustawiony, dodaje do `g_drawQueue` zadanie narysowania tekstury ikony w odpowiednim miejscu, uwzglÄ™dniajÄ…c `m_iconAlign`, `m_iconOffset` i `m_iconColor`.
## `void UIWidget::setIcon(const std::string& iconFile)`

ÄąÂaduje teksturÄ™ ikony za pomocÄ… `g_textures` i ustawia jej domyÄąâ€şlny `clip-rect`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uiwidget.h`.
-   `framework/ui/uitranslator.h`: Do parsowania `icon-align`.
-   `framework/graphics/texturemanager.h`: Do Äąâ€šadowania tekstur ikon.
-   `framework/graphics/painter.h`: PoÄąâ€şrednio, poprzez `g_drawQueue`.

---
# Ä‘Ĺşâ€śâ€ž uianchorlayout.cpp
## Opis ogĂłlny

Plik `uianchorlayout.cpp` zawiera implementacjÄ™ klas `UIAnchor`, `UIAnchorGroup` i `UIAnchorLayout`, ktĂłre razem tworzÄ… system layoutu opartego na kotwicach.
## Klasa `UIAnchor`
## `UIWidgetPtr UIAnchor::getHookedWidget(...)`

Znajduje widget, do ktĂłrego dana kotwica jest "przyczepiona". ObsÄąâ€šuguje specjalne identyfikatory:
-   `parent`: widget-rodzic.
-   `next`: nastÄ™pne rodzeÄąâ€žstwo.
-   `prev`: poprzednie rodzeÄąâ€žstwo.
-   Inne: szuka dziecka o danym ID w rodzicu.
## `int UIAnchor::getHookedPoint(...)`

Oblicza wspĂłÄąâ€šrzÄ™dnÄ… (X lub Y) krawÄ™dzi widgetu, do ktĂłrego kotwica jest przyczepiona.
## Klasa `UIAnchorGroup`
## `void UIAnchorGroup::addAnchor(...)`

Dodaje nowÄ… kotwicÄ™ do grupy. JeÄąâ€şli kotwica dla tej samej krawÄ™dzi juÄąÄ˝ istnieje, jest ona zastÄ™powana.
## Klasa `UIAnchorLayout`
## `void UIAnchorLayout::addAnchor(...)`

GÄąâ€šĂłwna metoda do tworzenia i dodawania nowej reguÄąâ€šy kotwiczenia. Tworzy obiekt `UIAnchor` i dodaje go do odpowiedniej `UIAnchorGroup`.
## `bool UIAnchorLayout::updateWidget(...)`
## Opis semantyczny
Rekurencyjna metoda, ktĂłra oblicza nowy `Rect` dla pojedynczego widgetu na podstawie jego kotwic.
## DziaÄąâ€šanie
1.  JeÄąâ€şli widget, do ktĂłrego siÄ™ kotwiczymy, sam nie zostaÄąâ€š jeszcze zaktualizowany, wywoÄąâ€šuje `updateWidget` rekurencyjnie dla niego.
2.  Iteruje po wszystkich kotwicach widgetu.
3.  Dla kaÄąÄ˝dej kotwicy, oblicza docelowy punkt (`point`) na podstawie `getHookedPoint`.
4.  Modyfikuje `newRect` widgetu, ustawiajÄ…c lub przesuwajÄ…c odpowiedniÄ… krawÄ™dÄąĹź (`moveLeft`, `setRight`, `moveVerticalCenter`, itp.).
5.  Po przetworzeniu wszystkich kotwic, ustawia nowy `Rect` dla widgetu.
## `bool UIAnchorLayout::internalUpdate()`

GÄąâ€šĂłwna metoda aktualizacji layoutu.
1.  Resetuje flagi `m_updated` we wszystkich `UIAnchorGroup`.
2.  W pÄ™tli przechodzi przez wszystkie widgety zarzÄ…dzane przez ten layout i, jeÄąâ€şli nie zostaÄąâ€šy jeszcze zaktualizowane, wywoÄąâ€šuje dla nich `updateWidget`. PÄ™tla zapewnia, ÄąÄ˝e wszystkie zaleÄąÄ˝noÄąâ€şci zostanÄ… rozwiÄ…zane.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania

-   `framework/ui/uianchorlayout.h`: Plik nagÄąâ€šĂłwkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.

---
# Meta-dokumenty
## Ä‘Ĺşâ€śâ€ Spis treÄąâ€şci

-   **`const.h`**: Definicje globalnych staÄąâ€šych, makr i typĂłw wyliczeniowych.
-   **`CMakeLists.txt`**: Skrypt konfiguracyjny budowania projektu.
-   **`global.h`**: Centralny plik nagÄąâ€šĂłwkowy, agregujÄ…cy podstawowe zaleÄąÄ˝noÄąâ€şci.
-   **`pch.h`**: Prekompilowany nagÄąâ€šĂłwek ze standardowymi bibliotekami.
-   **`luafunctions.cpp`**: Implementacja bindowaÄąâ€ž C++ do Lua.
-   **`resourcemanager.h`**: Deklaracja menedÄąÄ˝era zasobĂłw.
-   **`adaptiverenderer.cpp`**: Implementacja renderera adaptacyjnego.
-   **`adaptiverenderer.h`**: Deklaracja renderera adaptacyjnego.
-   **`application.cpp`**: Implementacja bazowej klasy aplikacji.
-   **`application.h`**: Deklaracja bazowej klasy aplikacji.
-   **`asyncdispatcher.h`**: Deklaracja dyspozytora zadaÄąâ€ž asynchronicznych.
-   **`binarytree.cpp`**: Implementacja czytnika/writera formatu binarnego drzewa.
-   **`asyncdispatcher.cpp`**: Implementacja dyspozytora zadaÄąâ€ž asynchronicznych.
-   **`clock.h`**: Deklaracja klasy zegara.
-   **`binarytree.h`**: Deklaracja klas do obsÄąâ€šugi formatu binarnego drzewa.
-   **`config.cpp`**: Implementacja klasy do zarzÄ…dzania pojedynczÄ… konfiguracjÄ….
-   **`configmanager.cpp`**: Implementacja menedÄąÄ˝era konfiguracji.
-   **`configmanager.h`**: Deklaracja menedÄąÄ˝era konfiguracji.
-   **`config.h`**: Deklaracja klasy `Config`.
-   **`clock.cpp`**: Implementacja klasy zegara.
-   **`consoleapplication.h`**: Deklaracja aplikacji konsolowej.
-   **`declarations.h`**: Wczesne deklaracje dla moduÄąâ€šu `core`.
-   **`event.cpp`**: Implementacja klasy `Event`.
-   **`event.h`**: Deklaracja klasy `Event`.
-   **`eventdispatcher.cpp`**: Implementacja dyspozytora zdarzeÄąâ€ž.
-   **`eventdispatcher.h`**: Deklaracja dyspozytora zdarzeÄąâ€ž.
-   **`filestream.cpp`**: Implementacja strumienia plikowego.
-   **`filestream.h`**: Deklaracja strumienia plikowego.
-   **`graphicalapplication.cpp`**: Implementacja aplikacji graficznej.
-   **`inputevent.h`**: Deklaracja struktury `InputEvent`.
-   **`graphicalapplication.h`**: Deklaracja aplikacji graficznej.
-   **`logger.h`**: Deklaracja klasy `Logger`.
-   **`module.cpp`**: Implementacja klasy `Module`.
-   **`modulemanager.cpp`**: Implementacja menedÄąÄ˝era moduÄąâ€šĂłw.
-   **`logger.cpp`**: Implementacja klasy `Logger`.
-   **`module.h`**: Deklaracja klasy `Module`.
-   **`modulemanager.h`**: Deklaracja menedÄąÄ˝era moduÄąâ€šĂłw.
-   **`scheduledevent.cpp`**: Implementacja zdarzenia zaplanowanego.
-   **`resourcemanager.cpp`**: Implementacja menedÄąÄ˝era zasobĂłw.
-   **`scheduledevent.h`**: Deklaracja zdarzenia zaplanowanego.
-   **`timer.cpp`**: Implementacja timera.
-   **`timer.h`**: Deklaracja timera.
-   **`consoleapplication.cpp`**: Implementacja aplikacji konsolowej.
-   **`shaderprogram.h`**: Deklaracja programu shadera.
-   **`animatedtexture.cpp`**: Implementacja tekstury animowanej.
-   **`animatedtexture.h`**: Deklaracja tekstury animowanej.
-   **`apngloader.cpp`**: Implementacja Äąâ€šadowarki APNG.
-   **`apngloader.h`**: Deklaracja Äąâ€šadowarki APNG.
-   **`atlas.cpp`**: Implementacja atlasu tekstur.
-   **`bitmapfont.cpp`**: Implementacja fontu bitmapowego.
-   **`atlas.h`**: Deklaracja atlasu tekstur.
-   **`bitmapfont.h`**: Deklaracja fontu bitmapowego.
-   **`cachedtext.cpp`**: Implementacja keszowanego tekstu.
-   **`colorarray.h`**: Deklaracja tablicy kolorĂłw.
-   **`cachedtext.h`**: Deklaracja keszowanego tekstu.
-   **`coordsbuffer.h`**: Deklaracja bufora wspĂłÄąâ€šrzÄ™dnych.
-   **`deptharray.h`**: Deklaracja tablicy gÄąâ€šÄ™bokoÄąâ€şci.
-   **`declarations.h`**: Wczesne deklaracje dla moduÄąâ€šu `graphics`.
-   **`coordsbuffer.cpp`**: Implementacja bufora wspĂłÄąâ€šrzÄ™dnych.
-   **`drawcache.cpp`**: Implementacja cache'a rysowania.
-   **`drawcache.h`**: Deklaracja cache'a rysowania.
-   **`drawqueue.cpp`**: Implementacja kolejki rysowania.
-   **`fontmanager.cpp`**: Implementacja menedÄąÄ˝era fontĂłw.
-   **`fontmanager.h`**: Deklaracja menedÄąÄ˝era fontĂłw.
-   **`drawqueue.h`**: Deklaracja kolejki rysowania.
-   **`framebuffer.cpp`**: Implementacja bufora ramki.
-   **`framebuffer.h`**: Deklaracja bufora ramki.
-   **`framebuffermanager.cpp`**: Implementacja menedÄąÄ˝era buforĂłw ramki.
-   **`graph.cpp`**: Implementacja wykresu debugujÄ…cego.
-   **`graph.h`**: Deklaracja wykresu debugujÄ…cego.
-   **`glutil.h`**: NarzÄ™dzia OpenGL.
-   **`graphics.cpp`**: Implementacja menedÄąÄ˝era grafiki.
-   **`graphics.h`**: Deklaracja menedÄąÄ˝era grafiki.
-   **`image.cpp`**: Implementacja klasy `Image`.
-   **`hardwarebuffer.h`**: Deklaracja bufora sprzÄ™towego.
-   **`image.h`**: Deklaracja klasy `Image`.
-   **`framebuffermanager.h`**: Deklaracja menedÄąÄ˝era buforĂłw ramki.
-   **`painter.h`**: Deklaracja klasy `Painter`.
-   **`painter.cpp`**: Implementacja klasy `Painter`.
-   **`hardwarebuffer.cpp`**: Implementacja bufora sprzÄ™towego.
-   **`paintershaderprogram.cpp`**: Implementacja programu shadera dla `Painter`.
-   **`paintershaderprogram.h`**: Deklaracja programu shadera dla `Painter`.
-   **`shader.cpp`**: Implementacja klasy `Shader`.
-   **`shadermanager.h`**: Deklaracja menedÄąÄ˝era shaderĂłw.
-   **`shadermanager.cpp`**: Implementacja menedÄąÄ˝era shaderĂłw.
-   **`shader.h`**: Deklaracja klasy `Shader`.
-   **`textrender.cpp`**: Implementacja renderera tekstu.
-   **`shaderprogram.cpp`**: Implementacja programu shadera.
-   **`texture.cpp`**: Implementacja klasy `Texture`.
-   **`texture.h`**: Deklaracja klasy `Texture`.
-   **`texturemanager.cpp`**: Implementacja menedÄąÄ˝era tekstur.
-   **`vertexarray.h`**: Deklaracja tablicy wierzchoÄąâ€škĂłw.
-   **`texturemanager.h`**: Deklaracja menedÄąÄ˝era tekstur.
-   **`textrender.h`**: Deklaracja renderera tekstu.
-   **`outfits.h`**: Shadery dla strojĂłw.
-   **`newshader.h`**: Nowe shadery.
-   **`shaders.h`**: Agregacja shaderĂłw.
-   **`shadersources.h`**: ÄąÄ…rĂłdÄąâ€ša standardowych shaderĂłw.
-   **`http.cpp`**: Implementacja klienta HTTP/WebSocket.
-   **`websocket.h`**: Deklaracja sesji WebSocket.
-   **`http.h`**: Deklaracja klienta HTTP/WebSocket.
-   **`result.h`**: Deklaracja struktury `HttpResult`.
-   **`session.cpp`**: Implementacja sesji HTTP.
-   **`session.h`**: Deklaracja sesji HTTP.
-   **`websocket.cpp`**: Implementacja sesji WebSocket.
-   **`mouse.cpp`**: Implementacja menedÄąÄ˝era myszy.
-   **`mouse.h`**: Deklaracja menedÄąÄ˝era myszy.
-   **`declarations.h`**: Wczesne deklaracje dla moduÄąâ€šu `luaengine`.
-   **`lbitlib.cpp`**: Implementacja biblioteki `bit32` dla Lua.
-   **`lbitlib.h`**: Deklaracja biblioteki `bit32`.
-   **`luabinder.h`**: Mechanizm bindowania C++ do Lua.
-   **`luaexception.h`**: Deklaracja wyjÄ…tkĂłw Lua.
-   **`luaexception.cpp`**: Implementacja wyjÄ…tkĂłw Lua.
-   **`luainterface.cpp`**: Implementacja interfejsu Lua.
-   **`luainterface.h`**: Deklaracja interfejsu Lua.
-   **`luaobject.cpp`**: Implementacja `LuaObject`.
-   **`luaobject.h`**: Deklaracja `LuaObject`.
-   **`luavaluecasts.cpp`**: Implementacja konwersji typĂłw Lua.
-   **`luavaluecasts.h`**: Deklaracja konwersji typĂłw Lua.
-   **`connection.cpp`**: Implementacja poÄąâ€šÄ…czenia TCP.
-   **`server.h`**: Deklaracja serwera TCP.
-   **`connection.h`**: Deklaracja poÄąâ€šÄ…czenia TCP.
-   **`declarations.h`**: Wczesne deklaracje dla moduÄąâ€šu `net`.
-   **`inputmessage.h`**: Deklaracja wiadomoÄąâ€şci przychodzÄ…cej.
-   **`outputmessage.cpp`**: Implementacja wiadomoÄąâ€şci wychodzÄ…cej.
-   **`outputmessage.h`**: Deklaracja wiadomoÄąâ€şci wychodzÄ…cej.
-   **`packet_player.cpp`**: Implementacja odtwarzacza pakietĂłw.
-   **`packet_player.h`**: Deklaracja odtwarzacza pakietĂłw.
-   **`protocol.h`**: Deklaracja protokoÄąâ€šu sieciowego.
-   **`packet_recorder.cpp`**: Implementacja nagrywarki pakietĂłw.
-   **`protocol.cpp`**: Implementacja protokoÄąâ€šu sieciowego.
-   **`server.cpp`**: Implementacja serwera TCP.
-   **`inputmessage.cpp`**: Implementacja wiadomoÄąâ€şci przychodzÄ…cej.
-   **`packet_recorder.h`**: Deklaracja nagrywarki pakietĂłw.
-   **`declarations.h`**: Wczesne deklaracje dla moduÄąâ€šu `otml`.
-   **`otmlparser.h`**: Deklaracja parsera OTML.
-   **`otml.h`**: Agregacja nagÄąâ€šĂłwkĂłw OTML.
-   **`otmldocument.cpp`**: Implementacja dokumentu OTML.
-   **`otmldocument.h`**: Deklaracja dokumentu OTML.
-   **`otmlemitter.cpp`**: Implementacja emittera OTML.
-   **`otmlexception.cpp`**: Implementacja wyjÄ…tkĂłw OTML.
-   **`otmlexception.h`**: Deklaracja wyjÄ…tkĂłw OTML.
-   **`otmlemitter.h`**: Deklaracja emittera OTML.
-   **`otmlparser.cpp`**: Implementacja parsera OTML.
-   **`otmlnode.h`**: Deklaracja wÄ™zÄąâ€ša OTML.
-   **`otmlnode.cpp`**: Implementacja wÄ™zÄąâ€ša OTML.
-   **`androidplatform.cpp`**: Implementacja platformy dla Androida.
-   **`androidwindow.cpp`**: Implementacja okna dla Androida.
-   **`androidwindow.h`**: Deklaracja okna dla Androida.
-   **`crashhandler.h`**: Deklaracja obsÄąâ€šugi awarii.
-   **`platform.cpp`**: Implementacja globalnej instancji platformy.
-   **`platformwindow.cpp`**: Implementacja bazowej klasy okna.
-   **`platform.h`**: Deklaracja klasy `Platform`.
-   **`platformwindow.h`**: Deklaracja bazowej klasy okna.
-   **`sdlwindow.cpp`**: Implementacja okna SDL (WASM).
-   **`sdlwindow.h`**: Deklaracja okna SDL.
-   **`unixcrashhandler.cpp`**: Implementacja obsÄąâ€šugi awarii dla Uniksa.
-   **`unixplatform.cpp`**: Implementacja platformy dla Uniksa.
-   **`win32crashhandler.cpp`**: Implementacja obsÄąâ€šugi awarii dla Windows.
-   **`win32platform.cpp`**: Implementacja platformy dla Windows.
-   **`win32window.cpp`**: Implementacja okna dla Windows.
-   **`win32window.h`**: Deklaracja okna dla Windows.
-   **`x11window.h`**: Deklaracja okna X11.
-   **`x11window.cpp`**: Implementacja okna X11.
-   **`proxy.cpp`**: Implementacja menedÄąÄ˝era proxy.
-   **`proxy.h`**: Deklaracja menedÄąÄ˝era proxy.
-   **`proxy_client.h`**: Deklaracja klienta proxy.
-   **`proxy_client.cpp`**: Implementacja klienta proxy.
-   **`combinedsoundsource.cpp`**: Implementacja zÄąâ€šoÄąÄ˝onego ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku.
-   **`combinedsoundsource.h`**: Deklaracja zÄąâ€šoÄąÄ˝onego ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku.
-   **`oggsoundfile.cpp`**: Implementacja pliku dÄąĹźwiÄ™kowego OGG.
-   **`declarations.h`**: Wczesne deklaracje dla moduÄąâ€šu `sound`.
-   **`oggsoundfile.h`**: Deklaracja pliku dÄąĹźwiÄ™kowego OGG.
-   **`soundbuffer.cpp`**: Implementacja bufora dÄąĹźwiÄ™ku.
-   **`soundbuffer.h`**: Deklaracja bufora dÄąĹźwiÄ™ku.
-   **`soundfile.cpp`**: Implementacja pliku dÄąĹźwiÄ™kowego.
-   **`soundchannel.cpp`**: Implementacja kanaÄąâ€šu dÄąĹźwiÄ™kowego.
-   **`soundchannel.h`**: Deklaracja kanaÄąâ€šu dÄąĹźwiÄ™kowego.
-   **`soundfile.h`**: Deklaracja pliku dÄąĹźwiÄ™kowego.
-   **`soundmanager.cpp`**: Implementacja menedÄąÄ˝era dÄąĹźwiÄ™ku.
-   **`soundmanager.h`**: Deklaracja menedÄąÄ˝era dÄąĹźwiÄ™ku.
-   **`soundsource.cpp`**: Implementacja ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku.
-   **`streamsoundsource.cpp`**: Implementacja strumieniowego ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku.
-   **`streamsoundsource.h`**: Deklaracja strumieniowego ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku.
-   **`soundsource.h`**: Deklaracja ÄąĹźrĂłdÄąâ€ša dÄąĹźwiÄ™ku.
-   **`any.h`**: Implementacja `stdext::any`.
-   **`cast.h`**: Funkcje do rzutowania typĂłw.
-   **`demangle.cpp`**: Implementacja demanglowania nazw.
-   **`compiler.h`**: Makra specyficzne dla kompilatora.
-   **`demangle.h`**: Deklaracja demanglowania nazw.
-   **`boolean.h`**: Implementacja `stdext::boolean`.
-   **`dumper.h`**: NarzÄ™dzie do debugowania.
-   **`dynamic_storage.h`**: Implementacja `dynamic_storage`.
-   **`exception.h`**: Deklaracja `stdext::exception`.
-   **`fastrand.h`**: Szybki generator liczb losowych.
-   **`math.cpp`**: Implementacja funkcji matematycznych.
-   **`math.h`**: Deklaracja funkcji matematycznych.
-   **`net.h`**: Deklaracja narzÄ™dzi sieciowych.
-   **`packed_any.h`**: Implementacja `packed_any`.
-   **`shared_object.h`**: Implementacja `shared_object` i `shared_object_ptr`.
-   **`stdext.h`**: Agregacja nagÄąâ€šĂłwkĂłw `stdext`.
-   **`packed_storage.h`**: Implementacja `packed_storage`.
-   **`thread.h`**: Agregacja nagÄąâ€šĂłwkĂłw wÄ…tkĂłw.
-   **`time.h`**: Deklaracja funkcji czasowych.
-   **`traits.h`**: NarzÄ™dzia metaprogramowania.
-   **`string.h`**: Deklaracja funkcji do stringĂłw.
-   **`time.cpp`**: Implementacja funkcji czasowych.
-   **`uri.h`**: Deklaracja parsera URI.
-   **`net.cpp`**: Implementacja narzÄ™dzi sieciowych.
-   **`uri.cpp`**: Implementacja parsera URI.
-   **`types.h`**: Definicje typĂłw.
-   **`format.h`**: Implementacja `stdext::format`.
-   **`string.cpp`**: Implementacja funkcji do stringĂłw.
-   **`declarations.h`**: Wczesne deklaracje dla moduÄąâ€šu `ui`.
-   **`ui.h`**: Agregacja nagÄąâ€šĂłwkĂłw UI.
-   **`uiboxlayout.cpp`**: Implementacja `UIBoxLayout`.
-   **`uiboxlayout.h`**: Deklaracja `UIBoxLayout`.
-   **`uigridlayout.cpp`**: Implementacja `UIGridLayout`.
-   **`uigridlayout.h`**: Deklaracja `UIGridLayout`.
-   **`uihorizontallayout.cpp`**: Implementacja `UIHorizontalLayout`.
-   **`uihorizontallayout.h`**: Deklaracja `UIHorizontalLayout`.
-   **`uilayout.cpp`**: Implementacja `UILayout`.
-   **`uilayout.h`**: Deklaracja `UILayout`.
-   **`uimanager.h`**: Deklaracja `UIManager`.
-   **`uitextedit.cpp`**: Implementacja `UITextEdit`.
-   **`uimanager.cpp`**: Implementacja `UIManager`.
-   **`uitextedit.h`**: Deklaracja `UITextEdit`.
-   **`uitranslator.cpp`**: Implementacja translatorĂłw UI.
-   **`uitranslator.h`**: Deklaracja translatorĂłw UI.
-   **`uiverticallayout.cpp`**: Implementacja `UIVerticalLayout`.
-   **`uiverticallayout.h`**: Deklaracja `UIVerticalLayout`.
-   **`uiwidget.cpp`**: Implementacja `UIWidget`.
-   **`uiwidget.h`**: Deklaracja `UIWidget`.
-   **`uiwidgetimage.cpp`**: Implementacja czÄ™Äąâ€şci `UIWidget` (obraz).
-   **`uianchorlayout.h`**: Deklaracja `UIAnchorLayout`.
-   **`uiwidgettext.cpp`**: Implementacja czÄ™Äąâ€şci `UIWidget` (tekst).
-   **`uiwidgetbasestyle.cpp`**: Implementacja czÄ™Äąâ€şci `UIWidget` (styl).
-   **`uianchorlayout.cpp`**: Implementacja `UIAnchorLayout`.
-   **`color.cpp`**: Implementacja klasy `Color`.
-   **`color.h`**: Deklaracja klasy `Color`.
-   **`crypt.cpp`**: Implementacja narzÄ™dzi kryptograficznych.
-   **`databuffer.h`**: Implementacja `DataBuffer`.
-   **`crypt.h`**: Deklaracja narzÄ™dzi kryptograficznych.
-   **`extras.cpp`**: Implementacja `Extras`.
-   **`extras.h`**: Deklaracja `Extras`.
-   **`framecounter.h`**: Implementacja licznika klatek.
-   **`matrix.h`**: Implementacja macierzy.
-   **`pngunpacker.cpp`**: Implementacja unpackera PNG.
-   **`pngunpacker.h`**: Deklaracja unpackera PNG.
-   **`point.h`**: Implementacja `Point`.
-   **`qrcodegen.c`**: Implementacja generatora kodĂłw QR.
-   **`qrcodegen.h`**: Deklaracja generatora kodĂłw QR.
-   **`rect.h`**: Implementacja `Rect`.
-   **`size.h`**: Implementacja `Size`.
-   **`stats.cpp`**: Implementacja systemu statystyk.
-   **`stats.h`**: Deklaracja systemu statystyk.
-   **`tinystr.cpp`**: Implementacja `TiXmlString`.
-   **`tinyxmlparser.cpp`**: Implementacja parsera TinyXML.
-   **`tinystr.h`**: Deklaracja `TiXmlString`.
-   **`tinyxml.cpp`**: Implementacja TinyXML.
-   **`tinyxmlerror.cpp`**: BÄąâ€šÄ™dy TinyXML.
-   **`tinyxml.h`**: Deklaracja TinyXML.

---
## Ä‘Ĺşâ€ťĹ¤ Indeks funkcji/metod
*W przygotowaniu*

---
## Ä‘ĹşÂ§Â­ Mapa zaleÄąÄ˝noÄąâ€şci

`$fenceInfo
graph TD
    subgraph Aplikacja
        Application --dziedziczy--> GraphicalApplication
        Application --dziedziczy--> ConsoleApplication
        GraphicalApplication --> PlatformWindow
        GraphicalApplication --> UIManager
        GraphicalApplication --> Graphics
        GraphicalApplication --> SoundManager
    end

    subgraph Framework_Core
        Application --> EventDispatcher
        Application --> ModuleManager
        Application --> ResourceManager
        Application --> ConfigManager
        Application --> Logger
        EventDispatcher --> Event
        Event --dziedziczy--> ScheduledEvent
        Clock & Timer
    end

    subgraph Framework_UI
        UIManager --> UIWidget
        UIWidget --> UILayout
        UILayout --dziedziczy--> UIAnchorLayout
        UILayout --dziedziczy--> UIBoxLayout
        UIBoxLayout --dziedziczy--> UIHorizontalLayout
        UIBoxLayout --dziedziczy--> UIVerticalLayout
        UIWidget --> BitmapFont
        UIWidget --> Painter
    end

    subgraph Framework_Graphics
        Graphics --> Painter
        Graphics --> TextureManager
        Graphics --> FrameBufferManager
        Graphics --> ShaderManager
        Painter --> ShaderProgram
        TextureManager --> Texture
        Texture --dziedziczy--> AnimatedTexture
        Texture --> Image
    end

    subgraph Framework_Platform
        PlatformWindow --implementuje--> WIN32Window
        PlatformWindow --implementuje--> X11Window
        PlatformWindow --implementuje--> AndroidWindow
        PlatformWindow --implementuje--> SDLWindow
        Platform
    end

    subgraph Framework_Lua
        LuaInterface --> LuaObject
        LuaInterface --> luabinder
        UIWidget --dziedziczy--> LuaObject
        Protocol --dziedziczy--> LuaObject
    end

    subgraph Framework_Net
        Protocol --> Connection
        Protocol --> InputMessage & OutputMessage
        ProxyManager --> Proxy & Session
        Connection & Proxy & Session --> Boost.Asio
    end

    subgraph ZaleÄąÄ˝noÄąâ€şci_ZewnÄ™trzne
        Boost.Asio
        Boost.Beast
        Boost.Process
        OpenGL/GLES/GLEW
        OpenAL
        Lua/LuaJIT
        PhysFS
        ZLIB
        OpenSSL
        TinyXML
    end

    Application --> Framework_Core
    GraphicalApplication --> Framework_Graphics
    GraphicalApplication --> Framework_UI
    GraphicalApplication --> Framework_Platform
    Application --> Framework_Lua
    Application --> Framework_Net

    Framework_Graphics --> OpenGL/GLES/GLEW
    Framework_Net --> ZaleÄąÄ˝noÄąâ€şci_ZewnÄ™trzne
    ResourceManager --> PhysFS
```
## Ä‘ĹşÂ§Â± Architektura systemu

System `otclient` jest zbudowany w oparciu o architekturÄ™ moduÄąâ€šowÄ… i warstwowÄ…, ktĂłra oddziela rdzeÄąâ€ž frameworka od logiki specyficznej dla klienta gry.
## Warstwy

1.  **Warstwa platformy (`framework/platform`)**
    -   **Opis**: NajniÄąÄ˝sza warstwa, ktĂłra abstrakcjonuje interakcje z systemem operacyjnym. Zawiera implementacje dla Windows (WinAPI), Linux/macOS (X11) i Android (NDK/JNI).
    -   **Komponenty**: `Platform` (operacje na plikach, procesach), `PlatformWindow` (zarzÄ…dzanie oknem, wejÄąâ€şciem, kontekstem graficznym), `CrashHandler`.
    -   **Cel**: Zapewnienie przenoÄąâ€şnoÄąâ€şci kodu miÄ™dzy rĂłÄąÄ˝nymi systemami.

2.  **Warstwa rozszerzeÄąâ€ž standardowych (`framework/stdext`)**
    -   **Opis**: ZbiĂłr narzÄ™dzi i rozszerzeÄąâ€ž do standardowej biblioteki C++, ktĂłre sÄ… uÄąÄ˝ywane w caÄąâ€šym projekcie.
    -   **Komponenty**: `shared_object_ptr` (inteligentne wskaÄąĹźniki), `cast` (bezpieczne rzutowanie typĂłw), `format` (formatowanie stringĂłw), `string` (narzÄ™dzia do stringĂłw), `time` (obsÄąâ€šuga czasu).
    -   **Cel**: Dostarczenie spĂłjnego i rozbudowanego zestawu narzÄ™dzi podstawowych.

3.  **Warstwa rdzenia frameworka (`framework/core`)**
    -   **Opis**: Serce aplikacji. Implementuje gÄąâ€šĂłwne pÄ™tle, system zdarzeÄąâ€ž, zarzÄ…dzanie zasobami, moduÄąâ€šami i konfiguracjÄ….
    -   **Komponenty**: `Application` (i pochodne), `EventDispatcher`, `ResourceManager`, `ModuleManager`, `ConfigManager`, `Logger`.
    -   **Cel**: Zapewnienie solidnej podstawy i infrastruktury dla dziaÄąâ€šania aplikacji.

4.  **Warstwa silnikĂłw (Framework Engines)**
    -   **Opis**: ZbiĂłr wyspecjalizowanych podsystemĂłw (silnikĂłw), ktĂłre realizujÄ… kluczowe funkcjonalnoÄąâ€şci.
    -   **Komponenty**:
        -   **Silnik graficzny (`framework/graphics`, `framework/ui`)**: `Graphics`, `Painter`, `TextureManager`, `UIManager`, `UIWidget`. Odpowiada za caÄąâ€še renderowanie 2D i interfejs uÄąÄ˝ytkownika.
        -   **Silnik Lua (`framework/luaengine`)**: `LuaInterface`, `luabinder`. Most miÄ™dzy C++ a Lua, umoÄąÄ˝liwiajÄ…cy skryptowanie.
        -   **Silnik sieciowy (`framework/net`, `framework/proxy`)**: `Protocol`, `Connection`, `ProxyManager`. ObsÄąâ€šuguje komunikacjÄ™ z serwerem.
        -   **Silnik dÄąĹźwiÄ™ku (`framework/sound`)**: `SoundManager`. ObsÄąâ€šuguje odtwarzanie dÄąĹźwiÄ™ku.
    -   **Cel**: Enkapsulacja zÄąâ€šoÄąÄ˝onych funkcjonalnoÄąâ€şci w oddzielne, zarzÄ…dzalne moduÄąâ€šy.

5.  **Warstwa logiki klienta (`src/client`)**
    -   **Opis**: NajwyÄąÄ˝sza warstwa, ktĂłra zawiera logikÄ™ specyficznÄ… dla klienta gry Tibii. Implementuje ona mechanikÄ™ gry, renderowanie Äąâ€şwiata, postaci, przedmiotĂłw itp.
    -   **Komponenty**: (NiezaÄąâ€šÄ…czone w promptcie) `Game`, `Map`, `Creature`, `Item`, `ProtocolGame`.
    -   **Cel**: Implementacja wÄąâ€šaÄąâ€şciwej gry. Ta warstwa intensywnie korzysta z API dostarczanego przez niÄąÄ˝sze warstwy frameworka.

6.  **Warstwa skryptowa (ModuÄąâ€šy Lua)**
    -   **Opis**: ZewnÄ™trzna warstwa, ktĂłra pozwala na rozszerzanie i modyfikowanie klienta bez potrzeby rekompilacji kodu C++. Skrypty Lua majÄ… dostÄ™p do API frameworka i logiki klienta za poÄąâ€şrednictwem bindowaÄąâ€ž.
    -   **Komponenty**: Pliki `.lua` i `.otmod` w katalogach `modules/` i `mods/`.
    -   **Cel**: UmoÄąÄ˝liwienie tworzenia wtyczek, modyfikacji interfejsu i dodawania nowej funkcjonalnoÄąâ€şci.
## PrzepÄąâ€šyw danych i interakcje

-   **Start aplikacji**: `main()` tworzy instancjÄ™ `GraphicalApplication`, ktĂłra inicjalizuje warstwy od doÄąâ€šu do gĂłry (Platforma -> RdzeÄąâ€ž -> Silniki).
-   **GÄąâ€šĂłwna pÄ™tla**: `GraphicalApplication::run()` uruchamia wielowÄ…tkowÄ… pÄ™tlÄ™. WÄ…tek logiki (`worker`) aktualizuje stan gry i przygotowuje dane do rysowania. WÄ…tek renderowania (gÄąâ€šĂłwny) rysuje te dane na ekranie i odbiera zdarzenia od `PlatformWindow`.
-   **Zdarzenia wejÄąâ€şciowe**: `PlatformWindow` -> `GraphicalApplication` -> `UIManager` -> `UIWidget` -> Skrypt Lua (callback `onClick` itp.).
-   **Komunikacja sieciowa**: Skrypt Lua (np. `g_game.login(...)`) -> `ProtocolGame` (Lua) -> `Protocol` (C++) -> `Connection` (C++) -> SieÄ‡. Pakiety przychodzÄ…ce idÄ… w odwrotnÄ… stronÄ™.
-   **Renderowanie**: Logika klienta (C++ lub Lua) tworzy widgety i ustawia ich wÄąâ€šaÄąâ€şciwoÄąâ€şci -> `UIManager` i `UIWidget` przygotowujÄ… `DrawQueue` -> `GraphicalApplication` przekazuje `DrawQueue` do `Painter` -> `Painter` wykonuje wywoÄąâ€šania OpenGL.




# Workbench – Szablony i narzędzia deweloperskie

:::{admonition} Warsztat deweloperski
:class: tip
Workbench zawiera szablony skryptów, checklisty, przykłady kodu i narzędzia pomocnicze dla deweloperów OTClient v8.
:::

## Szybki dostęp

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} 📝 Szablony skryptów
:link: #szablony-skryptow
:link-type: ref
:shadow: sm

Gotowe szablony dla modułów Lua, OTUI i integracji C++
:::

:::{grid-item-card} ✅ Checklisty
:link: #checklisty
:link-type: ref
:shadow: sm

Listy kontrolne dla tworzenia modułów i dokumentacji
:::

:::{grid-item-card} 🔧 Narzędzia
:link: #narzedzia
:link-type: ref
:shadow: sm

Pomocnicze skrypty i narzędzia developerskie
:::

:::{grid-item-card} 📊 Rejestr skryptów
:link: #rejestr-skryptow
:link-type: ref
:shadow: sm

Baza dostępnych skryptów i ich statusu
:::

:::

```{toctree}
:maxdepth: 2
:hidden:

template
example_health_monitor
```

(szablony-skryptow)=
## Szablony skryptów

### Szablon modułu Lua

```lua
-- modules/my_module/init.lua
-- Podstawowy szablon modułu OTClient v8

MyModule = {}

-- Inicjalizacja modułu
function MyModule.init()
  print("[MyModule] Initializing...")
  
  -- Rejestracja eventów
  connect(g_game, { 
    onGameStart = MyModule.onGameStart,
    onGameEnd = MyModule.onGameEnd 
  })
  
  print("[MyModule] Initialized successfully")
end

-- Czyszczenie przy wyłączaniu
function MyModule.terminate()
  print("[MyModule] Terminating...")
  
  -- Odłączanie eventów
  disconnect(g_game, { 
    onGameStart = MyModule.onGameStart,
    onGameEnd = MyModule.onGameEnd 
  })
  
  MyModule = nil
end

-- Handler rozpoczęcia gry
function MyModule.onGameStart()
  print("[MyModule] Game started")
  -- Twoja logika tutaj
end

-- Handler zakończenia gry
function MyModule.onGameEnd()
  print("[MyModule] Game ended")
  -- Czyszczenie stanu
end

-- Eksport funkcji publicznych
return MyModule
```

### Szablon OTUI Widget

```{code-block} text
-- modules/my_module/my_widget.otui
-- Podstawowy szablon widgetu OTUI

MyWidget < UIWidget
  id: myWidget
  size: 200 150
  anchors.centerIn: parent
  
  Label
    id: title
    text: Mój Widget
    anchors.top: parent.top
    anchors.horizontalCenter: parent.horizontalCenter
    margin-top: 10
    font: verdana-11px-rounded
    color: #ffffff
  
  Button
    id: actionButton
    text: Wykonaj akcję
    anchors.bottom: parent.bottom
    anchors.horizontalCenter: parent.horizontalCenter
    margin-bottom: 10
    width: 120
    @onClick: MyModule.onActionClick()
```

### Szablon integracji C++/Lua

```cpp
// src/client/my_feature.cpp
// Podstawowy szablon funkcji C++ eksportowanej do Lua

#include "my_feature.h"
#include <framework/luaengine/luainterface.h>

void MyFeature::registerLuaFunctions()
{
  // Rejestracja globalnej funkcji
  g_lua.bindSingletonFunction("myFunction", &MyFeature::myFunction, &g_myFeature);
  
  // Rejestracja klasy
  g_lua.registerClass<MyClass>();
  g_lua.bindClassMemberFunction<MyClass>("doSomething", &MyClass::doSomething);
}

int MyFeature::myFunction(const std::string& param)
{
  // Implementacja funkcji
  g_logger.info(stdext::format("Called with param: %s", param));
  return 42;
}
```

(checklisty)=
## Checklisty

### Checklist: Tworzenie nowego modułu

- [ ] Utworzyć katalog `modules/module_name/`
- [ ] Dodać plik `init.lua` z funkcjami `init()` i `terminate()`
- [ ] Utworzyć manifest modułu (jeśli wymagany)
- [ ] Zaimplementować logikę modułu
- [ ] Dodać pliki OTUI (jeśli wymagane)
- [ ] Zarejestrować eventy/hooki
- [ ] Przetestować inicjalizację i terminację
- [ ] Dodać dokumentację w `docs/modules/`
- [ ] Zaktualizować rejestr modułów

### Checklist: Dokumentacja API

- [ ] Dodać frontmatter YAML z metadanymi
- [ ] Opisać cel i zakres API
- [ ] Udokumentować wszystkie funkcje z parametrami
- [ ] Dodać przykłady użycia
- [ ] Uwzględnić edge cases i błędy
- [ ] Dodać linki krzyżowe do powiązanych API
- [ ] Zaktualizować indeks API
- [ ] Zweryfikować renderowanie w Sphinx

(narzedzia)=
## Narzędzia

### Dostępne skrypty

- **`scripts/build_authoring_pages.py`** – Generator stron dokumentacji
- **`scripts/patch_diagrams_clicks.py`** – Naprawa linków w diagramach Mermaid
- **Szablony w `docs/authoring/_blueprints/`** – Szablony rozdziałów dokumentacji

### Przykładowe użycie

```bash
# Budowanie dokumentacji
cd /path/to/otcv8-dev
python scripts/build_authoring_pages.py

# Build Sphinx
sphinx-build -b html docs docs/_build/html

# Serwer lokalny
cd docs/_build/html
python -m http.server 8000
```

(rejestr-skryptow)=
## Rejestr skryptów

:::{dropdown} Lista dostępnych skryptów (CSV → tabela)
:open:

```{csv-table} Skrypty
:header-rows: 1
:file: ../_data/scripts.csv
:widths: 10 20 14 10 12 34
```

:::

## Zobacz też

- {doc}`../modules/index` – Dokumentacja modułów
- {doc}`../api/index` – API Reference
- {doc}`../authoring/index` – Przewodniki authoring
- {doc}`../ui/index` – System UI (OTUI)

---
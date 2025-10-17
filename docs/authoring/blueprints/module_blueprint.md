---
title: "OTMOD Module Blueprint"
updated: "2025-10-17T20:02:11Z"
---

# OTMOD Module Blueprint

Minimalny, re-używalny szablon do opisu modułu **OTClient v8** (w tym `modules/game_bot`).

## Meta

- **module:** `example_module`
- **path:** `modules/example_module`
- **sandboxed:** `true`
- **reloadable:** `false`
- **version:** `1.0.0`
- **license:** `MIT`
- **author:** `yourname`
- **website:** `https://example.com`

## Manifest (OTMOD)

```otmod
Module
  name: example_module
  description: Short module description
  author: yourname
  website: https://example.com
  sandboxed: true
  reloadable: false
  scripts: [ example ]
  @onLoad: init()
  @onUnload: terminate()
  dependencies:
    - game_interface
  # opcjonalne opóźnione ładowanie zasobów/plików
  # load-later:
  #   - example_styles
```

## Lifecycle i powiązania

- `@onLoad` → `init()`
- `@onUnload` → `terminate()`
- **OTUI:** `modules/example_module/example.otui` (w tym *automatyczna iniekcja instancji widgetów* na podstawie CSV)
- **vBot (opcjonalnie):** definicje makr w `vbot_macros_blueprint.csv`

## Integracja

1. Skopiuj katalog do `modules/example_module`.
2. Dodaj `example.otui` oraz potrzebne zasoby (`data/images`, `data/fonts`).
3. Zweryfikuj zależności (np. `game_interface`).
4. Jeśli moduł wystawia API, opisz je w „Public API”.

## Public API (opcjonalnie)

```lua
-- modules/example_module/example.lua
local M = {}

function M.toggleWindow() end
function M.setEnabled(v) end

return M
```

## CSV mapping (pole → opis)

| Pole                      | Typ         | Wymagane | Opis |
|---------------------------|-------------|----------|------|
| module                    | string      | tak      | Nazwa modułu (również `name` w `.otmod`) |
| path                      | string      | tak      | Katalog modułu |
| sandboxed                 | bool        | tak      | Uruchamianie w sandboxie |
| reloadable                | bool        | tak      | Czy moduł można przeładować |
| version                   | string      | nie      | Wersja semver |
| license                   | string      | nie      | Licencja |
| author                    | string      | nie      | Autor/autorzy |
| website                   | string      | nie      | URL |
| description               | string      | nie      | Opis (krótki) |
| scripts                   | list; `;`   | tak      | Lista plików lua bez rozszerzeń |
| onLoad                    | string      | tak      | Nazwa funkcji `@onLoad` |
| onUnload                  | string      | tak      | Nazwa funkcji `@onUnload` |
| dependencies              | list; `;`   | nie      | Zależności (nazwa modułu) |
| load_later                | list; `;`   | nie      | Pliki/zasoby ładowane później |
| otui_files                | list; `;`   | nie      | Powiązane pliki OTUI |
| assets_fonts              | list; `;`   | nie      | Wymagane fonty |
| assets_images             | list; `;`   | nie      | Wymagane grafiki |
| public_api                | bool        | nie      | Czy moduł publikuje API |
| api_functions             | list; `;`   | nie      | Sygnatury funkcji API |
| **bot_support**           | bool        | nie      | Czy moduł posiada integracje z vBot |
| **bot_macros_file**       | string      | nie      | Nazwa CSV z definicjami makr |
| **bot_panel_id**          | string      | nie      | Identyfikator panelu/zakładki w UI bota |
| **panel_order**           | int         | nie      | Pozycja panelu w UI bota |
| **panel_icon**            | string      | nie      | Ikona panelu (ścieżka `"/images/..."` lub alias `icon-*`) |
| **hotkeys**               | list; `;`   | nie      | Lista domyślnych hotkeyów |
| **hotkeys_context**       | string      | nie      | Kontekst hotkeyów (np. `game`, `global`) |
| **hotkeys_conflict_policy** | enum       | nie      | `prefer|skip|warn` |
| **macro_group**           | string      | nie      | Grupa domyślna dla makr modułu (fallback) |

---

**Konwencje OTUI:** porządek atrybutów: **GEOMETRIA → STYL → ZACHOWANIE**; zdarzenia jako `@onX`. Iniekcja widgetów następuje do `MiniWindowContents` o `id: <module>_contents`.
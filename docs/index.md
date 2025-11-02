---
title: OTClientV8 – Developer Documentation
---

# OTClientV8 – Developer Documentation

:::{admonition} Witamy w dokumentacji OTClient v8
:class: tip
**OTClient v8** to klient gry i jednocześnie framework skryptowy (Lua/C++).  
Udostępnia API po stronie klienta, system modułów (OTUI/OTML/Lua) oraz integrację z **modules/game_bot (vBot)**.
:::

:::{admonition} Co jest czym?
:class: info
**Klient (core)** — binarny rdzeń i framework (C++), który uruchamia UI (OTUI), wczytuje zasoby (OTML), udostępnia API do Lua i zarządza pętlą zdarzeń.

**Framework Lua** — warstwa skryptowa z dostępem do wybranych menedżerów (tzw. _globals_) oraz hooków/eventów. Skrypty działają po stronie klienta, bez wpływu na serwer poza protokołem gry.

**Moduły (data/modules/...)** — pakiety funkcjonalne zawierające deklaracje `.otmod` (manifest), layouty `.otui`, konfiguracje `.otml` oraz skrypty `.lua`. Moduł może rozszerzać UI, logikę i integracje (np. z vBot).

**vBot (modules/game_bot)** — moduł automatyzacji działający w przestrzeni klienta, wykorzystujący udostępnione przez klienta API (makra, hooki, dostęp do stanu gry/UI). To nie jest osobny runtime — współdzieli środowisko modułów.
:::

:::{admonition} API i globalne managery (Lua)
:class: note
API klienta udostępnia *globalne obiekty/menedżery* (np. UI, okno, zasoby, gra). Pełny katalog globali zależy od kompilacji/gałęzi klienta.

**Przykładowe (niespełna lista):**
- `g_ui` — tworzenie/ładowanie UI (OTUI), widgety, style,
- `g_window` — okno aplikacji, rozmiar, fullscreen,
- `g_app` — cykl życia aplikacji, shutdown/restart,
- `g_resources` — pliki, zasoby, pakiety,
- `g_game` — stan połączenia/protokołu gry, player, map events,

:::

:::{admonition} Moduły i sandbox
:class: caution
Skrypty modułów działają w **sandboxie** — środowisku z *restrykcyjnie* ograniczonym dostępem do systemu i API spoza klienta.

- **Zakres:** sandbox pozwala na to, co jawnie udostępnia klient (API + globals).  
- **IO/OS:** brak bezpośredniego dostępu do systemu operacyjnego (procesy, raw-sockets, dowolne pliki poza `g_resources`) — **intencjonalnie ograniczone**.  
- **Manifest (.otmod):** konfiguracja modułu deklaruje metadane (nazwa, zależności, pliki). W wielu dystrybucjach manifest obsługuje *flagę sandbox* (np. `sandboxed: true`) — nazwa/obecność pola może się różnić między forkami → **sprawdź w `modules_Documentation.md` swojej bazy**.

> Podsumowanie: sandbox jest **bardzo rygorystyczny** i „pozwala na niewiele” poza tym, co zdefiniowano w API klienta — taki jest cel, aby moduły były bezpieczne i odseparowane.
:::

:::{admonition} Integracja kontekstowa: „OTClient v8 + vBot”
:class: success
W tej dokumentacji „OTClient v8 + vBot” oznacza, że:
- opisujemy **ten sam** klient i jego API (Lua/C++) oraz
- **moduł vBot** jako część ekosystemu modułów (`modules/game_bot`), korzystającą z udostępnionych hooków, zdarzeń i makr po stronie klienta.

To *nie jest* alternatywny klient ani osobny interpreter — vBot działa *wewnątrz* przestrzeni modułów OTClient v8.
:::

:::{admonition} Dobre praktyki (skrót)
:class: tip
- Pisz skrypty defensywnie (`local`, sprawdzaj `nil`, używaj `table.unpack`).  
- UI: zachowaj reguły OTUI (2 spacje, **GEOMETRIA → STYL → ZACHOWANIE**, `tr()` dla stałych tekstów).  
- Unikaj globali: kapsułkuj w modułach i przestrzeniach nazw.  
- Przed wydaniem: przetestuj hooki/eventy i powiązania z vBot.
:::


## Główne sekcje

:::{grid} 1 1 2 3
:gutter: 3

:::{grid-item-card} 🚀 Szybki start
:link: overview/getting_started
:link-type: doc
:shadow: md
Wprowadzenie do projektu, instalacja i pierwsze kroki
:::

:::{grid-item-card} 📚 API Reference
:link: api/index
:link-type: doc
:shadow: md
Kompletna dokumentacja API (Lua/C++), funkcje i interfejsy
:::

:::{grid-item-card} 🧩 Moduły
:link: modules/index
:link-type: doc
:shadow: md
Dokumentacja modułów Lua, struktura i przykłady użycia
:::

:::{grid-item-card} 🎨 UI (OTUI)
:link: ui/index
:link-type: doc
:shadow: md
System interfejsu użytkownika, widżety i style
:::

:::{grid-item-card} 📝 Authoring
:link: authoring/index
:link-type: doc
:shadow: md
Przewodniki tworzenia dokumentacji i rozdziały techniczne
:::

:::{grid-item-card} 🔍 RAG / Wyszukiwanie
:link: rag/index
:link-type: doc
:shadow: md
Wyszukiwarka semantyczna i indeks RAG
:::

:::{grid-item-card} 🧪 Workbench
:link: workbench/index
:link-type: doc
:shadow: md
Szablony skryptów, checklisty i narzędzia deweloperskie
:::

:::{grid-item-card} 📊 Dashboard
:link: dashboard/index
:link-type: doc
:shadow: md
Portal deweloperski z przeglądem projektu
:::
:::

## Architektura systemu

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
flowchart TB
    Core[OTCv8 Core C++] --> Events[System zdarzeń]
    Core --> Modules[Moduły Lua]
    Core --> UI[System UI OTUI]
    Events --> Network[Warstwa sieciowa]
    Modules --> GameRuntime[Game Runtime]
    UI --> Assets[Zasoby grafika/dźwięk]
    Core --> Settings[Ustawienia/Krypto]
    Core --> Audio[System audio]
    Core --> Logging[System logowania]

    style Core fill:#2d5a8c,stroke:#4a90e2,stroke-width:3px
    style Modules fill:#2d5a3c,stroke:#4ae24a,stroke-width:2px
    style UI fill:#5a2d8c,stroke:#904ae2,stroke-width:2px
```

## Struktura dokumentacji

```{toctree}
:maxdepth: 1
:caption: Główne sekcje

overview/getting_started
dashboard/index
api/index
modules/index
ui/index
rag/index
workbench/index
```

```{toctree}
:maxdepth: 3
:caption: Authoring

authoring/index
```

```{toctree}
:maxdepth: 2
:caption: API (Auto)

autoapi/index
```

```{toctree}
:maxdepth: 3
:caption: Copilot Docs

copilot/sphinx/index
```

```{toctree}
:maxdepth: 2
:caption: Reference

reference/index
reference/api
reference/events
reference/modules
reference/ui
```

```{toctree}
:maxdepth: 1
:caption: Zasoby

guide/index
cpp/index
lua/index
data/index
tools/index
```

```{toctree}
:maxdepth: 2
:caption: examples

examples/csv
examples/diagrams
```

## Status modułów

```{csv-table} Przegląd modułów
:header-rows: 1
:file: _data/modules.csv
:widths: 20, 60, 20
```

## Dodatkowe zasoby

* 🔗 **GitHub**: [lukaszj321/otcv8-dev](https://github.com/lukaszj321/otcv8-dev)
* 📖 **Edit on GitHub**: Każda strona ma link do edycji
* 🔍 **Wyszukiwarka**: Użyj pola wyszukiwania w górnym pasku
* 🌓 **Motyw**: Przełącznik jasny/ciemny w prawym górnym rogu

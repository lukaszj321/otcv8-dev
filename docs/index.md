# OTClient v8 — Dokumentacja projektu
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream

<<<<<<< Updated upstream
(intro)=
## O projekcie

**OTClientV8** to zaawansowany klient gry online oparty na silniku C++ z obsługą Lua dla skryptów i OTUI dla interfejsu użytkownika. Ten projekt zapewnia kompletną dokumentację techniczną obejmującą architekturę, API, moduły, UI oraz narzędzia dla deweloperów.

:::note
Ta dokumentacja jest generowana automatycznie z kodu źródłowego i zawiera pełne snippety, diagramy oraz przykłady użycia.
:::

## Główne cechy

* **Architektura modułowa** - elastyczny system ładowania modułów z zależnościami
* **Lua scripting** - pełne API Lua dla logiki gry i botów
* **OTUI** - deklaratywny język opisu interfejsu użytkownika
* **System zdarzeń** - asynchroniczna komunikacja między komponentami
* **Network stack** - stabilny protokół sieciowy z auto-reconnect
* **Asset management** - zarządzanie grafiką, dźwiękiem, fontami i innymi zasobami

(navigation)=
## Nawigacja

:::tip
Użyj wyszukiwarki (Ctrl+K lub ikona lupy) aby szybko znaleźć interesujące Cię tematy.
:::

### Dla początkujących

Jeśli dopiero zaczynasz pracę z OTClientV8, polecamy przeczytać w kolejności:

1. [Core Architecture](chapters/01_core.md) - architektura rdzenia
2. [Specyfikacja Runtime](chapters/01_specyfikacja.md) - środowisko uruchomieniowe
2. [System modułów](chapters/03_modules.md) - jak działają moduły
3. [Interfejs użytkownika](chapters/04_ui.md) - podstawy OTUI
4. [Przykłady diagramów](examples/diagrams.md) - wizualizacje architektury

### Dla deweloperów

Dokumentacja techniczna i referencje API:

* [API C++](reference/api.md) - kompletne API silnika
* [Events](reference/events.md) - system zdarzeń
* [Moduły Lua](reference/modules.md) - dostępne moduły
* [UI Components](reference/ui.md) - widgety OTUI

### Zasoby

* [Dane i assety](datasets/index.md) - obrazy, fonty, dźwięki
* [Przykłady CSV](examples/csv.md) - integracja danych tabelarycznych
=======
>>>>>>> Stashed changes

=======

>>>>>>> Stashed changes
=======

>>>>>>> Stashed changes
=======

>>>>>>> Stashed changes
Ta dokumentacja łączy opis architektury, wytyczne dla deweloperów oraz referencję modułów i zdarzeń. Korzysta z **PyData Sphinx Theme**, **MyST** (Markdown w Sphinx), oraz rozszerzeń do diagramów i podświetlania kodu.

## Jak czytać tę dokumentację

- Lewy panel to **nawigacja globalna** (rozdziały, dodatki).
- Na górze każdej strony jest **lokalny spis treści** (H2–H4).
- Bloki kodu mają przycisk **copy**; znaczniki `mermaid` renderują diagramy.

---

```{{toctree}}
:maxdepth: 2
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
:caption: Wprowadzenie
:hidden:

chapters/01_core
chapters/01_specyfikacja
chapters/02_events
chapters/03_modules
chapters/04_ui
chapters/05_assets
chapters/06_network
chapters/07_settings_crypto
chapters/08_audio
chapters/09_logging
chapters/10_game_runtime
:::
=======
Ta dokumentacja łączy opis architektury, wytyczne dla deweloperów oraz referencję modułów i zdarzeń. Korzysta z **PyData Sphinx Theme**, **MyST** (Markdown w Sphinx), oraz rozszerzeń do diagramów i podświetlania kodu.

## Jak czytać tę dokumentację

- Lewy panel to **nawigacja globalna** (rozdziały, dodatki).
- Na górze każdej strony jest **lokalny spis treści** (H2–H4).
- Bloki kodu mają przycisk **copy**; znaczniki `mermaid` renderują diagramy.

---

```{{toctree}}
:maxdepth: 2
:caption: Część I — Wprowadzenie i założenia

Specyfikacja studia (React/Electron) <chapters/chapter_01_specyfikacja_implementacji_studio_react_electron_dla_skryptow_otclient_v_8_v_bot>
```
>>>>>>> Stashed changes

```{{toctree}}
:maxdepth: 2
<<<<<<< Updated upstream
:caption: Referencje (API / moduły / UI)
:hidden:
=======
:caption: Część II — Silnik, zdarzenia, moduły, UI
>>>>>>> Stashed changes
=======
:caption: Część I — Wprowadzenie i założenia

Specyfikacja studia (React/Electron) <chapters/chapter_01_specyfikacja_implementacji_studio_react_electron_dla_skryptow_otclient_v_8_v_bot>
=======
:caption: Część I — Wprowadzenie i założenia

Specyfikacja studia (React/Electron) <chapters/chapter_01_specyfikacja_implementacji_studio_react_electron_dla_skryptow_otclient_v_8_v_bot>
```

```{{toctree}}
:maxdepth: 2
:caption: Część II — Silnik, zdarzenia, moduły, UI

Zdarzenia (Events) <chapters/chapter_02_events_docs_export_kit_authoring_agent_ready>
Moduły (Modules) <chapters/chapter_03_modules_docs_export_kit_authoring_agent_ready>
Interfejs (UI) <chapters/chapter_04_ui_docs_export_kit_authoring_agent_ready>
Zasoby (Assets) <chapters/chapter_05_assets_docs_export_kit_authoring_agent_ready>
Sieć (Network) <chapters/chapter_06_network_docs_export_kit_authoring_agent_ready>
Ustawienia & Kryptografia <chapters/chapter_07_settings_crypto_docs_export_kit_authoring_agent_ready>
Audio <chapters/chapter_08_audio_docs_export_kit_authoring_agent_ready>
Logowanie/Zdarzeniowość <chapters/chapter_09_logging_docs_export_kit_authoring_agent_ready>
Runtime gry <chapters/chapter_10_game_runtime_docs_export_kit_authoring_agent_ready>
>>>>>>> Stashed changes
```

```{{toctree}}
:maxdepth: 2
<<<<<<< Updated upstream
:caption: Część II — Silnik, zdarzenia, moduły, UI
>>>>>>> Stashed changes

Zdarzenia (Events) <chapters/chapter_02_events_docs_export_kit_authoring_agent_ready>
Moduły (Modules) <chapters/chapter_03_modules_docs_export_kit_authoring_agent_ready>
Interfejs (UI) <chapters/chapter_04_ui_docs_export_kit_authoring_agent_ready>
Zasoby (Assets) <chapters/chapter_05_assets_docs_export_kit_authoring_agent_ready>
Sieć (Network) <chapters/chapter_06_network_docs_export_kit_authoring_agent_ready>
Ustawienia & Kryptografia <chapters/chapter_07_settings_crypto_docs_export_kit_authoring_agent_ready>
Audio <chapters/chapter_08_audio_docs_export_kit_authoring_agent_ready>
Logowanie/Zdarzeniowość <chapters/chapter_09_logging_docs_export_kit_authoring_agent_ready>
Runtime gry <chapters/chapter_10_game_runtime_docs_export_kit_authoring_agent_ready>
```

```{{toctree}}
:maxdepth: 2
<<<<<<< Updated upstream
<<<<<<< Updated upstream
:caption: Przykłady / Wzorce
:hidden:
=======
:caption: Część III — Datasets, przykłady i dodatki
>>>>>>> Stashed changes
=======
:caption: Część III — Datasets, przykłady i dodatki
>>>>>>> Stashed changes
=======
:caption: Część III — Datasets, przykłady i dodatki
>>>>>>> Stashed changes
=======
:caption: Część I — Wprowadzenie i założenia

Specyfikacja studia (React/Electron) <chapters/chapter_01_specyfikacja_implementacji_studio_react_electron_dla_skryptow_otclient_v_8_v_bot>
```

```{{toctree}}
:maxdepth: 2
:caption: Część II — Silnik, zdarzenia, moduły, UI

Zdarzenia (Events) <chapters/chapter_02_events_docs_export_kit_authoring_agent_ready>
Moduły (Modules) <chapters/chapter_03_modules_docs_export_kit_authoring_agent_ready>
Interfejs (UI) <chapters/chapter_04_ui_docs_export_kit_authoring_agent_ready>
Zasoby (Assets) <chapters/chapter_05_assets_docs_export_kit_authoring_agent_ready>
Sieć (Network) <chapters/chapter_06_network_docs_export_kit_authoring_agent_ready>
Ustawienia & Kryptografia <chapters/chapter_07_settings_crypto_docs_export_kit_authoring_agent_ready>
Audio <chapters/chapter_08_audio_docs_export_kit_authoring_agent_ready>
Logowanie/Zdarzeniowość <chapters/chapter_09_logging_docs_export_kit_authoring_agent_ready>
Runtime gry <chapters/chapter_10_game_runtime_docs_export_kit_authoring_agent_ready>
```

```{{toctree}}
:maxdepth: 2
:caption: Część III — Datasets, przykłady i dodatki
>>>>>>> Stashed changes

Datasets i integracja z katalogiem `data/` <datasets/index>
Diagramy (Mermaid) <examples/diagrams>
CSV / Tabele / Snippety <examples/csv>
```

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
:::{toctree}
:maxdepth: 1
:caption: Dane i zasoby
:hidden:
=======
---
>>>>>>> Stashed changes
=======
---
>>>>>>> Stashed changes
=======
---
>>>>>>> Stashed changes
=======
---
>>>>>>> Stashed changes
=======
:caption: Część I — Wprowadzenie i założenia

Specyfikacja studia (React/Electron) <chapters/chapter_01_specyfikacja_implementacji_studio_react_electron_dla_skryptow_otclient_v_8_v_bot>
```

```{{toctree}}
:maxdepth: 2
:caption: Część II — Silnik, zdarzenia, moduły, UI

Zdarzenia (Events) <chapters/chapter_02_events_docs_export_kit_authoring_agent_ready>
Moduły (Modules) <chapters/chapter_03_modules_docs_export_kit_authoring_agent_ready>
Interfejs (UI) <chapters/chapter_04_ui_docs_export_kit_authoring_agent_ready>
Zasoby (Assets) <chapters/chapter_05_assets_docs_export_kit_authoring_agent_ready>
Sieć (Network) <chapters/chapter_06_network_docs_export_kit_authoring_agent_ready>
Ustawienia & Kryptografia <chapters/chapter_07_settings_crypto_docs_export_kit_authoring_agent_ready>
Audio <chapters/chapter_08_audio_docs_export_kit_authoring_agent_ready>
Logowanie/Zdarzeniowość <chapters/chapter_09_logging_docs_export_kit_authoring_agent_ready>
Runtime gry <chapters/chapter_10_game_runtime_docs_export_kit_authoring_agent_ready>
```

```{{toctree}}
:maxdepth: 2
:caption: Część III — Datasets, przykłady i dodatki

Datasets i integracja z katalogiem `data/` <datasets/index>
Diagramy (Mermaid) <examples/diagrams>
CSV / Tabele / Snippety <examples/csv>
```

---
>>>>>>> Stashed changes

## Indeks i wyszukiwanie

- **Wyszukiwanie**: ikona lupy w górnym pasku (pełnotekstowe).
- **Indeks tagów** (jeśli włączony): patrz stopka strony.

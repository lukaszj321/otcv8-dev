# Dokumentacja OTClientV8

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

:::{toctree}
:maxdepth: 2
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

:::{toctree}
:maxdepth: 2
:caption: Referencje (API / moduły / UI)
:hidden:

reference/index
:::

:::{toctree}
:maxdepth: 2
:caption: Przykłady / Wzorce
:hidden:

examples/diagrams
examples/csv
:::

:::{toctree}
:maxdepth: 1
:caption: Dane i zasoby
:hidden:

datasets/index
:::

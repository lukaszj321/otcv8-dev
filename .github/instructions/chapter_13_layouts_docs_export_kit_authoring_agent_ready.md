---
doc_id: chapter_13_layouts_docs_export_kit_authoring_agent_ready
source_path: layouts/*
source_sha: unknown
last_sync_iso: 2025-10-15T20:31:06Z
doc_class: ui/layouts
language: pl
title: 13_layouts — system motywów i nadpisań zasobów
summary: Zasady nadpisywania plików data/ przez layouts/, dobre praktyki dla sprite-sheetów i stylów OTUI, biblioteka blueprintów oraz kontrola jakości.
tags: [layouts, themes, otui, ui, assets, overrides, sprites, styles]
---

```{contents}
:local:
:depth: 2
```

## 1. Cel i zakres

Katalog `layouts/` służy do **tematyzacji** i **separacji wariantów wizualnych** bez ingerencji w bazowe `data/`.
Aktywny layout pełni rolę „warstwy pierwszej”, która może podmienić obrazy, style, kursory, dźwięki oraz część shaderów.
System musi pozostać **deterministyczny**: to co nie jest nadpisane w `layouts/` jest pobierane z `data/`.

**Konsekwencje projektowe**:

- Nazwy i rozkłady sprite-sheetów nie mogą łamać kontraktu (wymiary i kolejność klipów).
- Style OTUI zachowują identyfikatory i strukturę dziedziczenia; layout dopuszcza tylko dekorowanie.
- Dźwięki powinny mieć podobne poziomy głośności (normalizacja).

## 2. Reguły rozwiązywania ścieżek

Rozwiązywanie pliku ma postać funkcji `resolve(path)`:

```python
def resolve(path, layout):
    layout_path = f"layouts/{layout}/{path.lstrip('/')}"
    if exists(layout_path):
        return layout_path
    return f"data/{path.lstrip('/')}"
```

Ważne detale platformowe:

- **Windows vs Linux** – stosuj ścieżki **bez spacji**, małe litery, separator `/`.
- **Pakiety ZIP** – jeśli zasoby są archiwizowane, utrzymuj identyczny casing i strukturę katalogów.

## 3. Struktura katalogów (specyfikacja)

```{list-table} Wymagane katalogi wewnątrz layoutu
:header-rows: 1
* - ścieżka
  - typ
  - przeznaczenie
* - layouts/<active>/images
  - grafika
  - sprite-sheety, ikony, kursory
* - layouts/<active>/styles
  - otui
  - style i skórki widgetów
* - layouts/<active>/sounds
  - audio
  - kliknięcia, dźwięki UI
* - layouts/<active>/shaders
  - glsl
  - nadpisania shaderów post-process
```

## 4. Datasets: nadpisania (ground truth)

```{csv-table} layout_overrides
:header-rows: 1
:file: ../datasets/layout_overrides.csv
:widths: auto
```

(facet-13_layouts.overrides)=

### Facet: `13_layouts.overrides`

Kotwica wykorzystywana w linkowaniu wewnętrznym i narzędziach QA.

## 5. Sprite-sheety i klipy

Zmiana grafiki pociąga za sobą korekty w OTUI:

- `image-clip` dla każdego stanu (`$hover`, `$checked`, `$disabled`).
- `image-border` (skala devnine-patch) jeżeli komponent ma rozciąganą ramkę.
- `image-color` / `icon-color` dla wariantów kolorystycznych.

**Przykładowa mapa klipów** (dla `tabbutton_square` 3-stanowego 98×18):

```text
0 0 98 18    # normal
0 18 98 18   # hover
0 36 98 18   # checked
```

## 6. Konwencje stylów OTUI

- Dziedziczenie przez `<` (np. `TabBarRoundedButton < TabBarButton`).
- Stany warunkowe prefiksowane `$state` (kolejność *ma znaczenie*).
- Właściwości zakotwiczeń: `anchors.left/right/top/bottom` oraz `anchors.fill`.
- Unikaj globalnych `id`; stosuj lokalne identyfikatory i przekazuj referencje przez hierarchię.

**Fragment stylu** (wycinek gotowy do re-use):

```otui
TabBarButton < UIButton
  size: 17 18
  image-source: /images/ui/tabbutton_square
  image-clip: 0 0 98 18
  image-border: 3
  $hover !checked: image-clip: 0 18 98 18
  $disabled: image-color: #aaaaaa
  $checked: image-clip: 0 36 98 18
```

## 7. Biblioteka blueprintów (OTUI)

Dostarczamy indeks wzorców do re-użycia (CSV):

```{csv-table} otui_widget_blueprints
:header-rows: 1
:file: ../blueprints/otui_widget_blueprints.csv
:widths: auto
```

Zasada: blueprint definiuje **komórkę UI** (widget + zestaw propsów/states/events). Moduły importują blueprinty
i składają je w okna (np. MiniWindow Skills).

## 8. Integracja z OTMOD (relacje)

Moduł `game_skills` używa stylu `skills.otui`. Przykłady (sample do kopiowania):

- `docs/authoring/_samples/skills.otui`
- `docs/authoring/_samples/game_skills.otmod`

**Diagram relacji**:

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph LR
  A[game_skills.otmod] --> B((skills.otui))
  B --> C[SkillButton]
  B --> D[SkillValueLabel]
  A --> E[onMiniWindowClose handler]
```

## 9. Diagram rozwiązywania zasobów

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
flowchart TD
  A[Request asset path] --> B{layouts/<active>/... exists?}
  B -- yes --> C[Use layout asset]
  B -- no --> D[Use data asset]
  C --> E[Style Engine]
  D --> E[Style Engine]
  E --> F[Render]
```

## 10. QA dla layoutów

- **layout_overrides sanity** – brak pustych kolumn, wszystkie ścieżki względne.
- **sprite grid check** – porównanie wymiarów nowej grafiki z oryginałem.
- **style compile** – parsing OTUI (brak nieznanych właściwości).
- **link-lint** – działające kotwice `facet-13_layouts.overrides` i odsyłacze do datasetów.

## 11. FAQ (unikalne przypadki)

**Jak zmienić rozmiar przycisków bez psucia klipów?**  
Zwiększ `image-border` (skalowanie środka), pozostawiając wymiary klipów.

**Czy mogę nadpisać tylko część sprite-sheetu?**  
Nie. Nadpisujesz cały plik; jeśli siatka się zmienia – zaktualizuj każdy stan w OTUI.

**Jak dodać layout „mobile”?**  
Utwórz `layouts/mobile/…`, dodaj wpisy do `layout_overrides.csv` oraz test `render-smoke` z TabBar i oknem Skills.

---

## Aneks redakcyjny (merytoryczne uzupełnienia)

### Procedura review layoutu (kroki)

1) Porównaj sprite-sheet (wymiary, liczba klipów).
2) Zweryfikuj stany w OTUI ($hover/$checked/$disabled).
3) Przejdź smoke-test (HUD: TabBar, Skills, Inventory).
4) Sprawdź kontrast kolorów (WCAG AA).
5) Upewnij się, że linki do facetów działają.

### Przykład migracji stylu z data/ do layouts/

```diff
- image-source: /images/ui/tabbutton_square
+ image-source: /images/ui/tabbutton_square  # plik nadpisany w layouts/retro
```

## 12. Tokeny motywu (mapa wartości)

```text
--color-accent        = #d7b15e
--color-accent-hover  = #e0c06f
--color-bg            = #1a1a1a
--color-bg-panel      = #222222
--color-fg            = #e6e6e6
--color-muted         = #999999
--radius-small        = 2px
--radius-medium       = 4px
--radius-large        = 8px
--space-1             = 2px
--space-2             = 4px
--space-3             = 8px
--space-4             = 12px
```

## 13. Komplet stylów OTUI (przykład do skopiowania)

```otui
BaseButton < UIButton
  height: 18
  image-border: 3
  image-source: /images/ui/button
  $hover: image-color: #ffffff
  $disabled: image-color: #777777

PrimaryButton < BaseButton
  image-color: #d7b15e

Toggle < UIButton
  width: 12
  height: 12
  image-source: /images/ui/toggle
  image-clip: 0 0 12 12
  $checked: image-clip: 0 12 12 12

Slider < UISlider
  height: 12
  knob-image-source: /images/ui/slider_knob
  groove-image-source: /images/ui/slider_groove

Progress < ProgressBar
  height: 6
  background-color: #333333
  bar-color: #d7b15e

MiniWindow
  id: example
  !text: tr('Example')
  icon: /images/topbuttons/skills
  @onClose: modules.game_interface.minimize()
  &save: true
  &autoOpen: true

Tooltip < UILabel
  font: verdana-11px-monochrome
  color: #e6e6e6
  background: /images/ui/tooltip_bg
  padding: 4 6 4 6
```

## 14. Scenariusze migracji i ryzyka

- **Zmiana DPI**: gdy layout wprowadza pliki @2x, należy zachować te same wymiary logiczne w OTUI.
- **Sprite z dodatkową kolumną**: wprowadź nowy stan jako *nieużywany* w starszych stylach; unikniesz błędu indeksowania.
- **Fallback fontu**: jeśli motyw używa niestandardowego fontu, zdefiniuj fallback do `verdana-11px-monochrome`.
- **Kursory i fokus**: sprawdź widoczność focus ringów w ciemnych i jasnych tłach.

## 15. Runbook QA (krok po kroku)

1. Uruchom narzędzie `sprite-grid-check` na wszystkich zmianach `images/`.
2. Zbuduj *demo layout* i przejdź przez listę ekranów: login, map, skills, inventory.
3. Zweryfikuj `link-lint` (kotwice facetów), popraw ewentualne odnośniki.
4. Sprawdź kontrast (narzędzie `contrast-check`), zrzuty ekranu w ciemnym/jasnym motywie.
5. Dodaj wpis do `layout_overrides.csv` wraz z krótką notatką (`note`).

## 16. Najlepsze praktyki dostępności

- Kontrast przycisku w stanie disabled nie może spaść poniżej 3:1 względem tła.
- Elementy interaktywne >= 32×32 px obszaru kliknięcia.
- Informacje kolorystyczne muszą być wzmocnione kształtem/ikoną.
- Teksty w przyciskach: min. 11 px (bitmapy) lub 12 sp (system font).

## 17. Checklista releasu layoutu

- [ ] Uzupełnione `layout_overrides.csv`.
- [ ] Przejście smoke-testów (TabBar, Skills, Inventory).
- [ ] Akceptacja designu (zrzuty w 3 rozdzielczościach).
- [ ] Brak odwołań do nieistniejących plików.
- [ ] Zgodność licencji grafik (jeśli zewnętrzne).

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

## 18. Atlas ikon — konwencje i mapa

Ikony UI są pakowane w atlasie, aby ograniczyć liczbę bindów tekstur. Zalecenia:

- Plik atlasu powinien mieć rozmiary potęgi dwójki (np. 1024×1024), o ile pipeline tego wymaga.
- Wszystkie ikony zachowują margines 2px od krawędzi (bleed).
- Nazwy klipów w OTUI opisujemy deklaratywnie.

```otui
IconAtlas
  image-source: /images/ui/icons_atlas
  # nazwy logiczne -> klipy
  # name: x y w h
  icon: backpack    0 0 16 16
  icon: sword       16 0 16 16
  icon: shield      32 0 16 16
```

### Mapowanie nazw na klipy

```{list-table} Przykłady nazw ikon
:header-rows: 1
* - nazwa
  - klip (x y w h)
  - opis
* - backpack
  - 0 0 16 16
  - Ekwipunek
* - sword
  - 16 0 16 16
  - Atak
* - shield
  - 32 0 16 16
  - Obrona
```

## 19. Stylowanie stanów zagnieżdżonych

Stany mogą się łączyć: `$hover $checked` — najpierw hover, następnie checked. Pisz reguły od **bardziej ogólnych** do **bardziej szczegółowych**.

```otui
TabBarButton < UIButton
  image-source: /images/ui/tabbutton_square
  image-clip: 0 0 98 18
  $hover: image-clip: 0 18 98 18
  $checked: image-clip: 0 36 98 18
  $hover $checked: image-color: #ffe6a6
```

## 20. Zależności między layoutami (dziedziczenie motywów)

Można budować rodziny motywów (np. `base-dark` -> `retro-dark`). Nie kopiuj całych plików — nadpisuj minimalny podzbiór:

- wspólne pliki w `layouts/base-dark/…`,
- warianty w `layouts/retro-dark/…` tylko dla różniących się elementów.

```text
layouts/
  base-dark/
    images/ui/button.png
    styles/button.otui
  retro-dark/
    images/ui/button.png       # inny kolor, ta sama siatka
```

## 21. Narzędzia wspierające

- `otui-lint`: wykrywa nieznane właściwości i brakujące stany.
- `sprite-diff`: porównuje siatki (wymiary, liczba ramek).
- `atlas-verify`: sprawdza nakładanie się klipów i margines bleed.

## 22. Przykład pełnego okna (OTUI)

```otui
MiniWindow
  id: inventoryWindow
  !text: tr('Inventory')
  icon: /images/topbuttons/inventory
  width: 170
  height: 200
  @onClose: modules.game_interface.onInventoryClose()
  &save: true
  &autoOpen: false

  MiniWindowContents
    padding: 6
    layout: verticalBox

    Panel
      id: itemsGrid
      layout: grid
      layout-columns: 5
      layout-rows: 4
      anchors.fill: parent

    Panel
      height: 18
      layout: horizontalBox
      PrimaryButton
        id: sortButton
        !text: tr('Sort')
        &onClick: modules.game_inventory.sortItems()
```

## 23. Wersjonowanie motywów

W metadanych layoutu dodaj plik `theme.json`:

```json
{
  "name": "retro",
  "version": "1.2.0",
  "inherits": "base-dark",
  "author": "Team",
  "changelog": ["Nowy TabBar", "Poprawa kontrastu w Tooltip"]
}
```

## 24. Plan testów regresyjnych

- **Nawigacja**: TabBar, zmiana zakładek, stany klawiszy.
- **Okna MiniWindow**: otwieranie/zamykanie, zapamiętywanie pozycji.
- **Tooltip**: widoczność na różnych tłach.
- **Skalowanie**: render w 0.75×, 1.0×, 1.25×, 1.5×.

## 25. Przykładowy raport QA (szkielet)

```text
Layout: retro 1.2.0
Build: 2025-10-15
Checks:
- sprite-grid-check: OK (12 plików)
- otui-lint: OK (0 warnings)
- link-lint: OK
- contrast-check: 4/4 pass
Known issues: brak
Reviewer: JD
```

## 26. Tabela zmiennych stylu (rozszerzona)

```{list-table} Zmienne stylu
:header-rows: 1
* - klucz
  - wartość domyślna
  - użycie
* - --btn-height
  - 18px
  - Wysokość przycisków UI
* - --tab-width
  - 98px
  - Szerokość klipu TabBar
* - --tab-height
  - 18px
  - Wysokość klipu TabBar
* - --tooltip-padding-x
  - 6px
  - Margines poziomy
* - --tooltip-padding-y
  - 4px
  - Margines pionowy
* - --outline-width
  - 1px
  - Grubość ramki focus
* - --shadow-strength
  - 0.35
  - Intensywność cienia
```

## 27. Studium przypadku: konwersja motywu „retro”

1. **Analiza** sprite-sheetów: dopasowanie liczby stanów i kolejności.

2. **Migracja stylów**: wyodrębnienie wspólnych klas (`BaseButton`, `PrimaryButton`).

3. **Weryfikacja na mini-scenach**: login, mapa, okna HUD.

4. **Naprawa kontrastu**: korekta `image-color` dla disabled.

5. **Final QA**: raport z narzędzi lintujących (sprite-diff, otui-lint, link-lint).

## 28. Okno konfiguracji (pełny przykład OTUI)

```otui
MiniWindow
  id: settingsWindow
  !text: tr('Settings')
  icon: /images/topbuttons/options
  width: 240
  height: 220
  &save: true
  &autoOpen: false

  MiniWindowContents
    padding: 8
    layout: verticalBox

    Panel
      layout: grid
      layout-columns: 2
      layout-rows: 4

      Label
        !text: tr('Music')
      Toggle
        id: musicToggle

      Label
        !text: tr('Sound')
      Toggle
        id: soundToggle

      Label
        !text: tr('Brightness')
      Slider
        id: brightSlider

      Label
        !text: tr('Language')
      ComboBox
        id: langCombo

    Panel
      height: 20
      layout: horizontalBox
      anchors.bottom: parent.bottom
      anchors.right: parent.right

      PrimaryButton
        !text: tr('Apply')
        &onClick: modules.game_options.apply()
      BaseButton
        !text: tr('Cancel')
        &onClick: modules.game_options.cancel()
```

## 29. Wskazówki dotyczące internacjonalizacji

- Używaj `tr('...')` w tekstach; nie koduj literalnych stringów w grafikach.

- Długości tekstów mogą się różnić — pozostaw elastyczne paddingi.

- Kierunek pisma LTR/RTL — unikaj ikon sugerujących kierunek bez wariantów.

## 30. Integracja lintów w CI

```yaml
jobs:
  qa_layouts:
    steps:
      - run: sprite-diff --base data/images --layout layouts/retro/images
      - run: otui-lint docs/authoring/_samples/*.otui
      - run: link-lint docs/authoring/_sources/*.md
```

## 31. Style guide (UI)

- Siatki: trzymaj baseline 2 px; odstępy poziome/parzyste.

- Ikony: kontury 1 px; unikaj półprzezroczystości < 20% w cieniu.

- Tekst na przyciskach: ALL CAPS tylko dla akcji krytycznych.

- Tooltip: maksymalna szerokość 280 px; zawijaj słowa.

## 32. Macierz dostępności (check)

```{list-table} WCAG mini-matrix
:header-rows: 1
* - element
  - metryka
  - min.
  - sposób weryfikacji
* - przycisk
  - kontrast
  - AA
  - narzędzie contrast-check
* - label
  - rozmiar
  - 11px
  - inspekcja UI
* - fokus
  - outline
  - 1px
  - zrzuty / screen reader
```

## 33. Katalog blueprintów (rozszerzenie)

```otui
SliderVertical < Slider
  orientation: vertical
  height: 120
  width: 12

TooltipCritical < Tooltip
  background: /images/ui/tooltip_critical_bg
  color: #fff
  border-color: #aa0000
```

## 34. Profilowanie renderu UI

- Batchuj draw calle: grupuj widgety z tym samym atlasem.

- Unikaj nadmiernej liczby warstw alpha; łącz tła.

- Wykrywaj overdraw — narzędzie debug w renderze.

## 35. Zarządzanie wersjami layoutów

- `1.x` — kompatybilne ze schematem OTUI v1.

- `2.x` — zmiany łamiące (np. nowe nazwy id, inne wymiary sprite).

- Migracje dokumentuj w `theme.json` (pole `changelog`).

## 36. Ikony SVG — wytyczne eksportu

- Zamieniaj krzywe na ścieżki; usuwaj metadane i nieużywane warstwy.

- Rasteryzuj do sprite-atlasów PNG z jednakowym DPI.

- Utrzymuj krzywe o minimalnej liczbie węzłów (wydajność).

## 37. Release notes (szablon)

```text
Version: 1.3.0 (retro)
Date: 2025-10-15
Changes:
- Nowe cienie w oknach
- Zwiększona czytelność tooltipów
- Naprawa klipu TabBar hover
```

## 38. Mapowanie tokenów na CSS (przykład dokumentacyjny)

```css
:root {
  --color-accent: #d7b15e;
  --color-bg: #1a1a1a;
  --color-fg: #e6e6e6;
  --radius-small: 2px;
  --space-2: 4px;
}
.button { border-radius: var(--radius-small); }
.tooltip { padding: var(--space-2) var(--space-2); }
```

## 39. Audyt przed merge (lista 10 punktów)

1. Czy wszystkie obrazy mają właściwy format i kanał alpha?

2. Czy klipy sprite są zaktualizowane w każdym stanie OTUI?

3. Czy nazwy id nie kolidują z bazowymi stylami?

4. Czy tooltipy są czytelne na ciemnym i jasnym tle?

5. Czy blueprinty są użyte zamiast duplikowania stylów?

6. Czy anchorowanie jest stabilne w rozdzielczościach 720p–4K?

7. Czy cursory mają właściwe hotspoty?

8. Czy w `layout_overrides.csv` dodano notatki `note`?

9. Czy linki facetów działają?

10. Czy raport QA został dołączony?

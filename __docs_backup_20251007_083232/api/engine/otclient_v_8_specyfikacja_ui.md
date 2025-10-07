# OTClient v8 - Specyfikacja UI

---
## 0. Wprowadzenie i zasady
- [0.1 Cel i zakres "1:1"](#ch-0-1)
- [0.2 Terminologia (widget, layouta'owner, area/slot, preset, blueprint, AST)](#ch-0-2)
- [0.3 Kryteria jakoLci (deterministyczny rounda'trip, zgodnoLc 1:1)](#ch-0-3)
- [0.4 Workflow: projekt a' walidacja a' serializacja a' eksport a' import](#ch-0-4)
## 1. Konwencje formatowania i STRICT OTUI
- [1.1 Indent 2 sp., LF, bez BOM, bez tabow/komentarzy](#ch-1-1)
- [1.2 KolejnoLc atrybutow: GEOMETRIA a' STYL a' ZACHOWANIE](#ch-1-2)
- [1.3 Teksty i i18n: `!text: tr('...')`, wrap/autoa'resize/align/offset](#ch-1-3)
- [1.4 Stany: `$on`, `$!on`, `$focus` (kompletnoLc blokow)](#ch-1-4)
- [1.5 Zasoby `data/`: fonty, obrazy, kolory (#AARRGGBB/alpha)](#ch-1-5)
## 2. Architektura UI
- [2.1 Pliki `.otui` i L'adowanie `g_ui.displayUI('...')`](#ch-2-1)
- [2.2 Tworzenie dynamiczne `g_ui.createWidget('<Typ>', parent)`](#ch-2-2)
- [2.3 Hierarchia i identyfikacja (`id`, `getChildById`) ](#ch-2-3)
- [2.4 Fokus i nawigacja (bindy, `@onSetup`, FocusReason)](#ch-2-4)
## 3. Layout i wL'asnoLc ukL'adu
- [3.1 Zasada "layouta'owner" (parent vs child)](#ch-3-1)
- [3.2 Anchors, size, margins, padding - reguL'y i kolizje](#ch-3-2)
- [3.3 Scroll pairing (TextList/Multiline a" ScrollBar)](#ch-3-3)
- [3.4 Autoa'fit width (okna w panelach/kontenerach)](#ch-3-4)
## 4. Taksonomia komponentow (przeglad)
- [4.1 Okna: MainWindow, StaticMainWindow, MiniWindow, ContainerWindow, DialogWindow](#ch-4-1)
- [4.2 Kontenery: Panel, GroupBox, UIWidget, Grid, StatusOverlay](#ch-4-2)
- [4.3 Organizacja: Titlebar, Toolbar, TabBar/TabWidget, Splitter, HorizontalSeparator](#ch-4-3)
- [4.4 Dane/edycja: Label, Button, CheckBox, TextEdit, PasswordTextEdit, MultilineTextEdit, ComboBox, TextList/ListRow](#ch-4-4)
- [4.5 WskaLsniki: ProgressBar, ScrollBar (Vertical/Horizontal)](#ch-4-5)

---
## 5. MainWindow
- [5.1 Struktura i sloty](#ch-5-1)
- [5.2 Dozwolone dzieci (macierz)](#ch-5-2)
- [5.3 Geometria i styl](#ch-5-3)
- [5.4 Stany i zdarzenia](#ch-5-4)
- [5.5 Blueprint OTUI (kanoniczny)](#ch-5-5)
- [5.6 Mapowanie TS a" OTUI (serializer)](#ch-5-6)
- [5.7 Walidator (bL'edy/ostrzeLLenia)](#ch-5-7)
- [5.8 PrzykL'ady i edgea'cases](#ch-5-8)
## 6. StaticMainWindow
- [6.1 Struktura i sloty](#ch-6-1)
- [6.2 Dozwolone dzieci (macierz)](#ch-6-2)
- [6.3 Geometria i styl](#ch-6-3)
- [6.4 Stany i zdarzenia](#ch-6-4)
- [6.5 Blueprint OTUI](#ch-6-5)
- [6.6 TSa"OTUI](#ch-6-6)
- [6.7 Walidator](#ch-6-7)
- [6.8 PrzykL'ady](#ch-6-8)
## 7. MiniWindow
- [7.1 Struktura (titlebar/content/footer)](#ch-7-1)
- [7.2 Titlebar: minimize/close, draga'area](#ch-7-2)
- [7.3 Autoa'fit width i docking](#ch-7-3)
- [7.4 Stany i zdarzenia](#ch-7-4)
- [7.5 Blueprint OTUI](#ch-7-5)
- [7.6 TSa"OTUI](#ch-7-6)
- [7.7 Walidator](#ch-7-7)
- [7.8 PrzykL'ady](#ch-7-8)
## 8. ContainerWindow
- [8.1 Struktura (titlebar/content)](#ch-8-1)
- [8.2 Titlebar: back/pin/min/close](#ch-8-2)
- [8.3 Content: ItemSlotGrid/slots, DnD](#ch-8-3)
- [8.4 Scroll i overflow](#ch-8-4)
- [8.5 Blueprint OTUI](#ch-8-5)
- [8.6 TSa"OTUI](#ch-8-6)
- [8.7 Walidator](#ch-8-7)
- [8.8 PrzykL'ady](#ch-8-8)
## 9. DialogWindow
- [9.1 Struktura](#ch-9-1)
- [9.2 Enter/Escape (OK/Cancel)](#ch-9-2)
- [9.3 ModalnoLc i fokus](#ch-9-3)
- [9.4 Blueprint/TS/Walidator](#ch-9-4)

---
## 10. Titlebar
- [10.1 Ikona, tytuL', przyciski](#ch-10-1)
- [10.2 Slot i dozwolone dzieci](#ch-10-2)
- [10.3 Draga'move, fokus](#ch-10-3)
- [10.4 Blueprint/TS/Walidator](#ch-10-4)
## 11. Toolbar
- [11.1 Grupy akcji i separatory](#ch-11-1)
- [11.2 Toggle/active state](#ch-11-2)
- [11.3 Blueprint/TS/Walidator](#ch-11-3)
## 12. Panel / GroupBox
- [12.1 Sloty treLci, nagL'owki, separatory](#ch-12-1)
- [12.2 Dozwolone dzieci i autoa'fit](#ch-12-2)
- [12.3 Blueprint/TS/Walidator](#ch-12-3)
## 13. TabBar / TabWidget
- [13.1 ZakL'adki i kontener treLci](#ch-13-1)
- [13.2 Zdarzenia i aktywacja](#ch-13-2)
- [13.3 Blueprint/TS/Walidator](#ch-13-3)
## 14. Splitter
- [14.1 Dwoje dzieci, mina'size, pamiec podziaL'u](#ch-14-1)
- [14.2 Blueprint/TS/Walidator](#ch-14-2)
## 15. TextList / ListRow
- [15.1 Struktura wiersza (focus/select)](#ch-15-1)
- [15.2 Scroll pairing i kotwice](#ch-15-2)
- [15.3 Blueprinty row + walidator](#ch-15-3)
## 16. Label / UILabel
- [16.1 Wrap/autoa'resize/font/kolor/offset](#ch-16-1)
- [16.2 Blueprint/TS/Walidator](#ch-16-2)
## 17. Button
- [17.1 Stany `$on/$!on`, ikonografia, mina'size](#ch-17-1)
- [17.2 Shortcuts i zdarzenia](#ch-17-2)
- [17.3 Blueprint/TS/Walidator](#ch-17-3)
## 18. CheckBox
- [18.1 Zachowania i focus](#ch-18-1)
- [18.2 Blueprint/TS/Walidator](#ch-18-2)
## 19. TextEdit / PasswordTextEdit / MultilineTextEdit
- [19.1 Placeholder, caret, multiline](#ch-19-1)
- [19.2 Scroll pairing](#ch-19-2)
- [19.3 Blueprint/TS/Walidator](#ch-19-3)
## 20. ComboBox
- [20.1 Menu height/scroll step](#ch-20-1)
- [20.2 OptionChange i integracja](#ch-20-2)
- [20.3 Blueprint/TS/Walidator](#ch-20-3)
## 21. ProgressBar
- [21.1 Zakres, style, opis stanu](#ch-21-1)
- [21.2 Blueprint/TS/Walidator](#ch-21-2)
## 22. ScrollBar (Vertical/Horizontal)
- [22.1 Docking (right/bottom), step, pixelsa'scroll](#ch-22-1)
- [22.2 Pairing rules + walidator](#ch-22-2)
## 23. HorizontalSeparator
- [23.1 ULLycie i ograniczenia](#ch-23-1)
- [23.2 Blueprint](#ch-23-2)
## 24. StatusOverlay
- [24.1 Label + Progress + Cancel](#ch-24-1)
- [24.2 Blueprint/TS/Walidator](#ch-24-2)

---
## 25. Macierze dozwolonych dzieci (global)
- [25.1 Tabele macierzowe per komponent i slot](#ch-25-1)
- [25.2 ReguL'y globalne, zakazy, autoa'naprawy](#ch-25-2)
## 26. Walidacja i autoa'naprawy (global)
- [26.1 BL'edy blokujace (STRICT, anchors, wymagane elementy)](#ch-26-1)
- [26.2 OstrzeLLenia (scroll pairing, Enter/Escape, Min/Close)](#ch-26-2)
- [26.3 Autoa'naprawy deterministyczne (kolejnoLc, sloty, scroll, snapping 2px)](#ch-26-3)
## 27. Parser/Serializer OTUI a' AST (TypeScript)
- [27.1 Specyfikacja tokenow i INDENT/DEDENT](#ch-27-1)
- [27.2 KsztaL't AST; API `parseOtui()` i `serializeAst()`](#ch-27-2)
- [27.3 Normalizacja do STRICT (`ensureStrictOtui()`)](#ch-27-3)
- [27.4 Testy "rounda'trip" (goldeny)](#ch-27-4)
## 28. Import/Export i rounda'trip (edytor a" plik a" Lua)
- [28.1 Import z `.otui` i z blokow `@OTUI_BEGIN/END`](#ch-28-1)
- [28.2 Eksport do `.otui` + odLwieLLenie bloku w Lua](#ch-28-2)
- [28.3 Generatory stubow Lua (`g_ui.displayUI('...')` + kontrolery)](#ch-28-3)
- [28.4 Runtime: brak publicznego `load UI from string` (tylko pliki)](#ch-28-4)
## 29. Biblioteka presetow (gotowe szablony)
- [29.1 Okna (MiniWindow, ContainerWindow, Dialog)](#ch-29-1)
- [29.2 Komponenty (Titlebar, Toolbar, Panel, a|)](#ch-29-2)
- [29.3 Warianty tematyczne (narzedzie, kontener, dialog)](#ch-29-3)
## 30. Testy wizualne i regresja
- [30.1 Snapshoty i porownania 1:1](#ch-30-1)
- [30.2 DPI / font metrics / skalowanie](#ch-30-2)
- [30.3 DostepnoLc (kontrasty, czytelnoLc)](#ch-30-3)
## 31. SL'ownik i indeks
- [31.1 SL'ownik atrybutow OTUI (A-Z)](#ch-31-1)
- [31.2 Indeks komponentow i wL'aLciwoLci](#ch-31-2)

---

<!-- Puste kotwice (placeholdery), aby linki dziaL'aL'y od razu -->
<div id="ch-0-1"></div>
## 0.1 Cel i zakres "1:1"
Ten dokument definiuje **kanoniczne zasady projektowania UI OTClient v8** (OTUI/OTML + Lua) oraz wymagania dla Twojego **edytora TypeScript**: jak skL'adac okna i komponenty, aby eksport/import byL' **deterministyczny i w 100% zgodny** z klientem. Zawiera: reguL'y formatowania (STRICT OTUI), taksonomie komponentow, macierze dozwolonych dzieci, blueprinty OTUI, glue Lua, walidacje, parser/serializer OTUIa'AST i rounda'trip (edytor a" plik `.otui` a" Lua).<div id="ch-0-2"></div>
## 0.2 Terminologia
- **Widget** - jednostka UI (np. Label, Button, TextList).
- **Layouta'owner** - rodzic odpowiadajacy za obszary/sloty i dokowanie dzieci.
- **Area/slot** - semantyczna przestrzeL" dla dzieci (np. `titlebar`, `content`, `footer`).
- **Preset/Blueprint** - gotowy wzorzec OTUI danego komponentu/okna.
- **AST** - abstrakcyjne drzewo skL'adniowe w edytorze (model OTUI w TS).
- **STRICT OTUI** - LcisL'y format tekstu `.otui`: LF, 2 spacje, brak tabow/komentarzy, staL'a kolejnoLc atrybutow.
- **Rounda'trip** - pewny obieg: import a' edycja a' eksport bez utraty semantyki ani formatowania reguL'owego.<div id="ch-0-3"></div>
## 0.3 Kryteria jakoLci
- **ZgodnoLc 1:1** z OTClientem (ukL'ad, stany, eventy, zasoby).
- **Deterministyczny eksport** (ta sama treLc wej./wyj. po serializacji, przy zachowaniu STRICT).
- **Stabilne identyfikatory `id`** i spojne nazewnictwo kontrolerow Lua.
- **Lokalizacja**: wszystkie staL'e teksty przechodza przez `tr()`.
- **Zasoby**: tylko z `data/` (fonty/obrazy), kolory #AARRGGBB/`alpha`.
- **Brak "magii"** w stanach: stany nadpisuja styl, nie geometrie.<div id="ch-0-4"></div>
## 0.4 Workflow
1) **Projekt** w edytorze (drag&drop presetow; macierze pilnuja dozwolonych dzieci).  
2) **Walidacja** (STRICT, anchors, wymagane elementy).  
3) **Serializacja** do `.otui` (kolejnoLc GEOMETRIAa'STYLa'ZACHOWANIE).  
4) **Eksport**: zapis `.otui` + generator stubow Lua (`g_ui.displayUI('...')`).  
5) **Import**: z plikow `.otui` lub blokow Lua oznaczonych `@OTUI_BEGIN/END`.  
6) **Rounda'trip**: zmiany w edytorze odzwierciedlone w pliku i opcjonalnym bloku Lua.
<div id="ch-1-1"></div>
## 1.1 Indent i STRICT
- **LF**, bez BOM; **spacje** (bez tabow); **brak trailing spaces**.  
- **Wciecia = 2 spacje** (mnoLLniki).  
- **Zero komentarzy** w treLci OTUI.  
- Dozwolone znaki: L'agodne ASCII + `#` (wyL'acznie w kolorach), `-_:./<>()` itp. WartoLci tekstowe w `!text` w pojedynczych cudzysL'owach.

PrzykL'ad minimalnego bloku zgodnego ze STRICT:
Label
  id: info
  anchors.left: parent.left
  anchors.right: parent.right
  text-wrap: true
  !text: tr('Information')
  font: verdana-11px-monochrome
```

<div id="ch-1-2"></div>
## 1.2 KolejnoLc atrybutow
**GEOMETRIA** (najpierw): `id`, `size`/`width`/`height`, `anchors.*` (najpierw `fill`, potem krawedzie), `margin-*`, `padding`.  
**STYL**: `background-color`, `font`, `color`, `image-*`, `text-*` (`align`, `wrap`, `auto-resize`, `offset`), `!text: tr('...')`.  
**ZACHOWANIE**: `&metaFn`, `@on...` (Enter/Escape/Click/Setup/...), stany `$on/$!on/$focus`.

> Serializator **musi** zawsze emitowac w tej kolejnoLci.<div id="ch-1-3"></div>
## 1.3 Teksty i i18n
- KaLLdy staL'y tekst: `!text: tr('...')`.  
- Escaping `'` a' `\'` wewnatrz `tr('...')`.  
- `text-wrap`/`text-auto-resize`/`text-align`/`text-offset` steruja renderem.  
- Nie umieszczaj surowych napisow poza `!text` (rownieLL w stanach).<div id="ch-1-4"></div>
## 1.4 Stany
- `$on` / `$!on` - przeL'aczane `widget:setOn(true/false)`.  
- `$focus` - aktywne przy fokusie klawiatury.  
- **Zalecenie**: stany modyfikuja **styl** (kolory, `!text`, obraz), **nie** geometrie (anchors/size).  

PrzykL'ad:
Button
  id: toggle
  width: 96
  !text: tr('Off')

  $on:
    !text: tr('On')
    color: #ffffff

  $!on:
    !text: tr('Off')
    color: #bbbbbb
```

<div id="ch-1-5"></div>
## 1.5 Zasoby `data/`
- **Fonty**: uLLywaj nazw z `data/fonts/` (np. `verdana-11px-monochrome`, `verdana-11px-rounded`, `terminus-14px-bold`).  
- **Obrazy**: LcieLLki `/images/...`, opcje `image-smooth`, `image-fixed-ratio`.  
- **Kolory**: `#AARRGGBB` lub `alpha`.  
- Walidator blokuje LcieLLki spoza `data/`.
<div id="ch-2-1"></div>
## 2.1 Pliki `.otui` i L'adowanie
- **Kanonicznie** UI L'aduje sie z pliku: `local win = g_ui.displayUI('nazwa_pliku')`.  
- Nazwa w `displayUI` odpowiada plikowi `.otui` w module.  
- Brak publicznego API "load UI from string" - w runtime uLLywaj plikow.<div id="ch-2-2"></div>
## 2.2 Tworzenie dynamiczne
local parent = rootWidget
local row = g_ui.createWidget('UIWidget', parent)
row:setId('row1')
local name = g_ui.createWidget('Label', row)
name:setText(tr('Name'))
```
- Tworzenie dzieci w Lua jest dozwolone, ale **eksport** z edytora powinien odtwarzac ukL'ad w `.otui` (statyczny szkielet), a dynamike zostawic skryptom.<div id="ch-2-3"></div>
## 2.3 Hierarchia i identyfikacja
- `id` unikalne w ramach rodzica.  
- Dostep w Lua: `parent:getChildById('...')`, wyszukiwanie gL'ebokie: `rootWidget:recursiveGetChildById('...')`.  
- WidocznoLc: `widget:isVisible()`, `widget:setVisible(true/false)`; `:show()/:hide()`.<div id="ch-2-4"></div>
## 2.4 Fokus i nawigacja
- Bindy w `@onSetup` lub Lua: `g_keyboard.bindKeyPress('Up', fn, scope)`.  
- Fokus: `widget:focus()`, powody fokusowania (FocusReason) wpL'ywaja na zachowanie.  
- Listy: `focusNextChild/PreviousChild`, zapewnij `ensureChildVisible` przy przewijaniu.
<div id="ch-3-1"></div>
## 3.1 Zasada "layouta'owner"
- **Parent** definiuje sloty i reguL'y dokowania (anchors, padding, marginesy).  
- **Child** ustawia swoje `anchors.*` wzgledem parenta/sasiadow.  
- ScrollBar naleLLy do parenta (kontenera), ale jest **sparowany** z przewijanym dzieckiem.<div id="ch-3-2"></div>
## 3.2 Anchors, size, margins, kolizje
- `anchors.fill: parent` **nie** L'acz z jednoczesnym `top/bottom/left/right`.  
- JeLli okno jest dokowane w panelu: ustaw `anchors.left/right: parent` i usuL" `width` (autoa'fit).  
- Marginesy `margin-*` i `padding` determinuja odstepy - trzymaj parzyste wartoLci (snapping 2 px).<div id="ch-3-3"></div>
## 3.3 Scroll pairing
- `TextList`/`MultilineTextEdit` a" **`VerticalScrollBar`** jako **sibling**:  
  - ScrollBar: `anchors.right/top/bottom: parent`.  
  - Lista/tekst: `anchors.right: scroll.left`.  
- `HorizontalScrollBar` dokowany na dole; treLc: `anchors.bottom: hscroll.top`.  
- Samotny ScrollBar a' bL'ad walidacji.<div id="ch-3-4"></div>
## 3.4 Autoa'fit width (dokowane okna)
- Dla `MiniWindow`/`DialogWindow` w panelach: domyLlnie **rozciagaj w poziomie** (`anchors.left/right: parent`) i zarzadzaj odstepami przez `margin-*`.  
- Edytor przy eksporcie **autoa'naprawia**: usuwa `width`, gdy ustawiono `left/right`.
<div id="ch-4-1"></div>
## 4.1 Okna (Windowa'class)
**Cel**: najwyLLsze elementy kompozycji; zapewniaja rame, titlebar, focus i skroty.

- **MainWindow**  
  *Rola*: gL'owne okno moduL'u/sceny.  
  *Sloty*: brak nazwanych slotow - treLc bezpoLrednio w root.  
  *Typowe*: peL'noekran/duLLe panele, dopuszcza wszystkie "panelowe" dzieci.  
  *Zakazy*: oknaa'dzieci (inne Main/StaticMain) jako potomkowie.

- **StaticMainWindow**  
  *Rola*: jak MainWindow, ale **bez draga'move** (statyczne tL'o/ekrany).  
  *ULLycie*: ekrany logowania, waiting list.

- **MiniWindow**  
  *Rola*: moduL'owe okno narzedziowe.  
  *Sloty*: `titlebar`, `content`, `footer`.  
  *Przyciski*: **minimize**, **close** (opcjonalnie **back/pin**).  
  *Autoa'fit*: domyLlnie rozciaga sie na szerokoLc rodzica w panelu.

- **ContainerWindow**  
  *Rola*: przegladanie zawartoLci (sloty/items).  
  *Sloty*: `titlebar`, `content`.  
  *Przyciski*: **back**, **pin/lock**, **minimize**, **close**.  
  *TreLc*: `ItemSlotGrid`/sloty; DnD; scroll przy overflow.

- **DialogWindow**  
  *Rola*: potwierdzenia/prompt.  
  *Skroty*: `@onEnter` (OK), `@onEscape` (Cancel).  
  *Sloty*: typowo tytuL' + treLc + przyciski OK/Cancel.<div id="ch-4-2"></div>
## 4.2 Kontenery (Contenta'class)
**Cel**: organizacja i grupowanie treLci.

- **Panel**  
  Lekki kontener na treLc. Dopuszcza wiekszoLc elementow panelowych; uLLywany jako sekcja lub obszar roboczy.

- **GroupBox**  
  Panel z nagL'owkiem (etykieta) i ramka/separatorem. Dla formularzy/pogrupowanych opcji.

- **UIWidget**  
  Bazowy kontener/"kafelek". MoLLe miec tL'o (`image-*`, `background-color`), sL'uLLy teLL jako wiersze list.

- **Grid (edytorowy)**  
  Artefakt **tylko w edytorze** do ukL'adania na siatce (snapping, gapy). **Nie** jest typem OTUI - przy eksporcie mapuje sie na anchors/marginesy prawdziwych widgetow.

- **StatusOverlay**  
  Lekka warstwa informacyjna (Label/Progress/Cancel) dokowana nad treLcia. Bez zL'oLLonych dzieci.<div id="ch-4-3"></div>
## 4.3 Organizacja i nawigacja
**Cel**: nawigowanie, przeL'aczanie kontekstu, dzielenie przestrzeni.

- **Titlebar**  
  Slot nagL'owka okna: `Label` (tytuL'), przyciski (**min/close/back/pin**), ewentualna ikona. MoLLe stanowic **draga'area**. Zakaz list, edytorow, scrollbarow.

- **Toolbar**  
  Pasek akcji (grupy `Button`, separatory). Stany toggle, skroty klawiszowe.

- **TabBar / TabWidget**  
  TabBar zawiera **zakL'adki** (przyciski), a **kontent zakL'adki** znajduje sie w osobnym kontenerze obok/poniLLej. Nie wkL'adamy treLci do TabBar.

- **Splitter**  
  Dzieli przestrzeL" na **dwa** panele; wymagane `min-size` dzieci; pamietanie podziaL'u mile widziane.

- **HorizontalSeparator**  
  Linie/separatory sekcji. Element wizualny - **bez dzieci**.

<div id="ch-4-4"></div>
## 4.4 Dane i edycja (Inputs/Lists)
**Cel**: prezentacja i wprowadzanie danych.

- **Label / UILabel**  
  Tekst z `!text: tr('...')`, `font`, `color`, `text-wrap`, `text-auto-resize`, `text-align`, `text-offset`.

- **Button**  
  Akcje; `@onClick`; stany `$on/$!on` (np. toggle). Minimalne wymiary zalecane aA16A-16.

- **CheckBox**  
  PrzeL'acznik bool; fokus i interakcja klawiatura. Czesto obok napisu (Label) w tym samym kontenerze.

- **TextEdit / PasswordTextEdit / MultilineTextEdit**  
  Pola tekstowe; `Multiline` wymaga pary ze **ScrollBar** (sibling, dock right/bottom).

- **ComboBox**  
  Selektor opcji; `menu-height`, `menu-scroll-step`, `@onOptionChange`. Pozycje menu wewnetrzne (bez manualnych dzieci).

- **TextList / ListRow**  
  Lista przewijana; wiersze jako `UIWidget`/custom row; fokus/zaznaczenie; para z **VerticalScrollBar** (sibling).

  <div id="ch-4-5"></div>
## 4.5 WskaLsniki i przewijanie
- **ProgressBar**  
  Pasek postepu; zakres i styl; **bez dzieci**. Opisy stanu (Label) obok.

- **ScrollBar (Vertical/Horizontal)**  
  `step`, `pixels-scroll`; **sibling** przewijanej treLci. Dock: Vertical a' **right**, Horizontal a' **bottom**.  
  **Pairing rules**: lista/tekst kotwiczy `right: scroll.left` (dla V) lub `bottom: hscroll.top` (dla H). Samotny ScrollBar a' bL'ad.

---

> **Uwaga**: SzczegoL'owe macierze dozwolonych dzieci na poziomie kaLLdego komponentu znajduja sie w rozdziale **25** i sa egzekwowane przez walidator podczas eksportu.
<div id="ch-5-1"></div>
## 5.1 Struktura i sloty
**MainWindow** jest najwyLLszym kontenerem okna roboczego moduL'u/sceny. Nie definiuje nazwanych slotow (jak `titlebar/content/footer`) - treLc umieszczasz bezpoLrednio w root lub w wydzielonych `UIWidget`/`Panel`.

**Zalecany podziaL' logiczny (nieobowiazkowy):**
- `header` (opcjonalny pasek tytuL'u/toolbar jako `UIWidget`),
- `content` (gL'owna przestrzeL" pracy),
- `footer` (status/akcje). 
To **nazwa wL'asna** dzieci, nie formalny "slot" klasy - pomaga w edytorze, w walidacji i przy presetach.<div id="ch-5-2"></div>
## 5.2 Dozwolone dzieci (macierz)
| Parent: `MainWindow` | Dopuszczone dzieci | Niedozwolone / uwagi |
|---|---|---|
| root | `UIWidget`, `Panel`, `Label`, `Button`, `TextEdit`, `PasswordTextEdit`, `MultilineTextEdit`, `TextList`, `ComboBox`, `CheckBox`, `ProgressBar`, `VerticalScrollBar`, `HorizontalSeparator`, `TabBar`, `Splitter` | Inne okna (`MainWindow/StaticMainWindow/MiniWindow/ContainerWindow/DialogWindow`) - as- |
| `header` (jeLli wydzielisz) | `Label`, `Button`, `Toolbar`, `UIWidget` (ikona) | Scroll/edytory/listy - as- |
| `content` | wszystkie elementy "panelowe" (lista powyLLej) | oknaa'dzieci - as- |
| `footer` | `Button`, `Label`, `ProgressBar` | listy/edytory - as- |

**Scroll pairing:** jeLli w `content` dodasz `TextList`/`MultilineTextEdit`, dockuj **VerticalScrollBar** po prawej i kotwicz treLc do `scroll.left`.<div id="ch-5-3"></div>
## 5.3 Geometria i styl (GEOMETRIA a' STYL a' ZACHOWANIE)
- **Rozmiar**: `size: W H` lub kotwice wzgledem rodzica (zalecane w narzedziach: `anchors.left/right: parent` + wysokoLc/marginesy).
- **Kotwice**: unikaj L'aczenia `anchors.fill: parent` z recznymi `top/bottom/left/right`. 
- **Marginesy/padding**: parzyste wartoLci (snapping 2 px) dla spojnoLci.
- **TL'o**: `background-color` lub `image-source` (np. tL'o ekranu); `image-smooth`, `image-fixed-ratio` w razie potrzeby.
- **Teksty**: wyL'acznie `!text: tr('...')` (STRICT). 
- **Fonty/obrazy**: tylko z `data/`.

> **Autoa'fit width**: osadzone w panelu `MainWindow` powinno domyLlnie rozciagac sie na szerokoLc rodzica (edytor moLLe automatycznie usuwac `width`).<div id="ch-5-4"></div>
## 5.4 Stany i zdarzenia
- **Zdarzenia okienne**: `@onEnter` (OK/Apply), `@onEscape` (Cancel/Close), `@onSetup` (bindy klawiszy). 
- **Stany**: `MainWindow` z reguL'y nie uLLywa `$on/$!on` na sobie; stosuj na przyciskach/wierszach listy.
- **Fokus i nawigacja**: w `@onSetup` zbinduj strzaL'ki/PageUp/PageDown dla list, Enter/Escape dla akcji.
- **Zamykanie**: implementuj w controllerze (Lua), a w `.otui` tylko wiaLL `@onEscape`/przyciski.<div id="ch-5-5"></div>
## 5.5 Blueprint OTUI (kanoniczny)
MainWindow
  id: main
  size: 420 320
  anchors.left: parent.left
  anchors.top: parent.top
  margin-top: 6
  margin-left: 6

  background-color: alpha

  @onEnter: MainController.onConfirm()
  @onEscape: MainController.onCancel()
  @onSetup: MainController.onSetup()
# HEADER (opcjonalny pasek tytuL'u/toolbar)
  UIWidget
    id: header
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Main Window')
      font: verdana-11px-rounded
# CONTENT (lista + scroll jako sibling)
  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: header.bottom
    anchors.bottom: footer.top
    padding: 6

    background-color: alpha

    TextList
      id: items
      anchors.fill: parent

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: header.bottom
    anchors.bottom: footer.top
    step: 16
# FOOTER (akcje)
  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28

    background-color: #00000033

    Button
      id: okButton
      anchors.right: cancelButton.left
      anchors.bottom: parent.bottom
      width: 64
      margin-right: 8
      !text: tr('Ok')
      @onClick: MainController.onConfirm()

    Button
      id: cancelButton
      anchors.right: parent.right
      anchors.bottom: parent.bottom
      width: 64
      margin-right: 8
      !text: tr('Cancel')
      @onClick: MainController.onCancel()
```

**Uwagi do blueprintu:** 
- ScrollBar to **sibling** `content`; lista kotwiczona do `scroll.left`. 
- Wciecia **2 spacje**, kolejnoLc sekcji zachowana (STRICT). 
- Teksty przez `tr()`; zasoby wyL'acznie z `data/`.<div id="ch-5-6"></div>
## 5.6 Mapowanie TS a" OTUI (serializer)
**Minimalny preset w edytorze (TS):**
export function presetMainWindow(): WidgetNode {
  return {
    base: 'MainWindow',
    geometry: { id: 'main', size: [420, 320], anchors: { left: 'parent.left', top: 'parent.top' }, marginTop: 6, marginLeft: 6 },
    style: { backgroundColor: 'alpha' },
    behavior: { events: { onEnter: 'MainController.onConfirm()', onEscape: 'MainController.onCancel()', onSetup: 'MainController.onSetup()' } },
    children: [
      { base: 'UIWidget', geometry: { id: 'header', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, style: { backgroundColor: '#00000066' }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6, }, style: { textAutoResize: true, text: 'Main Window', font: 'verdana-11px-rounded' } }
      ]},
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'scroll.left', top: 'header.bottom', bottom: 'footer.top' }, padding: 6 }, style: { backgroundColor: 'alpha' }, children: [
        { base: 'TextList', geometry: { id: 'items', anchors: { fill: 'parent' } } }
      ]},
      { base: 'VerticalScrollBar', geometry: { id: 'scroll', anchors: { right: 'parent.right', top: 'header.bottom', bottom: 'footer.top' } }, /* style */ undefined, behavior: undefined },
      { base: 'UIWidget', geometry: { id: 'footer', anchors: { left: 'parent.left', right: 'parent.right', bottom: 'parent.bottom' }, height: 28 }, style: { backgroundColor: '#00000033' }, children: [
        { base: 'Button', geometry: { id: 'okButton', anchors: { right: 'cancelButton.left', bottom: 'parent.bottom' }, width: 64, marginRight: 8 }, style: { text: 'Ok' }, behavior: { events: { onClick: 'MainController.onConfirm()' } } },
        { base: 'Button', geometry: { id: 'cancelButton', anchors: { right: 'parent.right', bottom: 'parent.bottom' }, width: 64, marginRight: 8 }, style: { text: 'Cancel' }, behavior: { events: { onClick: 'MainController.onCancel()' } } }
]}
]
};
}
```
**Serializer** musi emitowac: GEOMETRIA a' STYL a' ZACHOWANIE, `style.text` a' `!text: tr('...')`, `events` a' `@on...`, stany a' `$...`.

**Sanityzacja** przed zapisem: `ensureStrictOtui()` (LF, 2 sp., brak komentarzy/tabow/trailing spaces).<div id="ch-5-7"></div>
## 5.7 Walidator (bL'edy/ostrzeLLenia)
**Blokujace (atS):**
- Dziecko typu okno (`*Window`) wewnatrz `MainWindow`.
- Sprzeczne kotwice (`fill` + `top/bottom/left/right`).
- `TextList`/`MultilineTextEdit` bez pary **VerticalScrollBar** (gdy overflow) lub bL'edne kotwice pary.
- Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeLLenia (as dZ):**
- Brak `@onEnter/@onEscape` przy oknie z przyciskami OK/Cancel.
- Brak `header`/`footer` przy zL'oLLonych ukL'adach (zalecenie porzadkowe). 
- Nieparzyste marginesy (odstep od siatki 2 px).<div id="ch-5-8"></div>
## 5.8 PrzykL'ady i edgea'cases
- **Fullscreen tL'o**: zamiast narzucac `size`, uLLyj `anchors.fill: parent` i obraz tL'a z `image-fixed-ratio: true` (bez L'aczenia z recznymi kotwicami). 
- **Lista bez scrolla**: jeLli wiesz, LLe elementow jest maL'o - dopuszczalne, ale walidator zasugeruje dodanie scrolla przy overflow. 
- **Shortcuty**: w `@onSetup` zbinduj strzaL'ki, PageUp/Down do nawigacji po liLcie; Enter/Escape do akcji. 
- **Zamykanie okna**: mapuj `@onEscape` na `MainController.onCancel()` - sam kontroler decyduje o `:hide()`/sprzataniu. 
- **Nadpisywanie geometrii w stanach**: unikaj modyfikowania `anchors/size` wewnatrz `$on/$!on/$focus` - trzymaj stany stylistyczne (kolor/tekst).
<div id="ch-6-1"></div>
## 6.1 Struktura i sloty
**StaticMainWindow** to gL'owne okno **statyczne** (bez draga'move), stosowane m.in. dla ekranow logowania, komunikatow, list oczekiwania. Nie posiada formalnych slotow jak `titlebar/content/footer`, ale zalecamy logiczny podziaL' na: `header`, `content`, `footer` (jako `UIWidget`).

- **header** (opcjonalny): pasek tytuL'u/toolbar (Label/Buttons).  
- **content**: gL'owna przestrzeL" treLci (teksty, listy, formularze, progress).  
- **footer**: akcje (OK/Cancel) lub status.

StaticMainWindow nie powinno miec **innych okien** jako dzieci.<div id="ch-6-2"></div>
## 6.2 Dozwolone dzieci (macierz)
| Parent: `StaticMainWindow` | Dopuszczone dzieci | Niedozwolone / uwagi |
|---|---|---|
| root | `UIWidget`, `Panel`, `Label`, `Button`, `TextEdit`, `PasswordTextEdit`, `MultilineTextEdit`, `TextList`, `ComboBox`, `CheckBox`, `ProgressBar`, `VerticalScrollBar`, `HorizontalSeparator`, `TabBar`, `Splitter` | Inne okna (`*Window`) - as- |
| `header` | `Label`, `Button`, `Toolbar`, `UIWidget` (ikona) | Scroll/edytory/listy - as- |
| `content` | wszystkie elementy panelowe z wiersza root | `*Window` - as-; `ScrollBar` tylko jako para do list/tekstow |
| `footer` | `Button`, `Label`, `ProgressBar` | listy/edytory - as- |

**Scroll pairing**: przy `TextList`/`MultilineTextEdit` dodaj **VerticalScrollBar** (dok po prawej), a treLc kotwicz do `scroll.left`.<div id="ch-6-3"></div>
## 6.3 Geometria i styl
- **Rozmiar/pozycja**: `size: W H` lub anchors; w panelach a' autoa'fit szerokoLci (`anchors.left/right: parent`, bez `width`).
- **Kotwice**: nie L'acz `anchors.fill: parent` z recznymi `top/bottom/left/right`.
- **Marginesy/padding**: parzyste wartoLci (snapping 2 px).
- **TL'o**: `background-color` albo `image-source` (np. ekran powitalny) + `image-smooth/fixed-ratio` w razie potrzeby.
- **Teksty**: zawsze `!text: tr('...')` (STRICT). Zasoby tylko z `data/`.<div id="ch-6-4"></div>
## 6.4 Stany i zdarzenia
- **Zdarzenia**: `@onEnter` (OK/Continue), `@onEscape` (Cancel/Back), `@onSetup` (bindy, np. Enter/Escape/strzaL'ki).
- **Stany**: zwykle na **dzieciach** (Button/ListRow), nie na samym `StaticMainWindow`.
- **Fokus**: zapewnij fokus pierwszego sensownego dziecka; nawigacja klawiatura w `@onSetup`.<div id="ch-6-5"></div>
## 6.5 Blueprint OTUI (kanoniczny)
StaticMainWindow
  id: staticMain
  size: 420 320
  anchors.left: parent.left
  anchors.top: parent.top
  margin-top: 6
  margin-left: 6

  background-color: alpha

  @onEnter: StaticController.onConfirm()
  @onEscape: StaticController.onCancel()
  @onSetup: StaticController.onSetup()

  UIWidget
    id: header
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Static Window')
      font: verdana-11px-rounded

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: header.bottom
    anchors.bottom: footer.top
    padding: 6

    background-color: alpha

    Label
      id: info
      anchors.left: parent.left
      anchors.right: parent.right
      text-wrap: true
      !text: tr('Please wait...')
      font: verdana-11px-monochrome

    ProgressBar
      id: progress
      anchors.left: parent.left
      anchors.right: parent.right
      anchors.top: info.bottom
      margin-top: 6

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: header.bottom
    anchors.bottom: footer.top
    step: 16

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28

    background-color: #00000033

    Button
      id: cancelButton
      anchors.right: parent.right
      anchors.bottom: parent.bottom
      width: 64
      margin-right: 8
      !text: tr('Cancel')
      @onClick: StaticController.onCancel()
```

**Uwaga**: blueprint jest **STRICT** (brak komentarzy), wciecia = 2 sp., kolejnoLc sekcji zachowana.<div id="ch-6-6"></div>
## 6.6 Mapowanie TS a" OTUI (serializer)
**Preset (TS)**
export function presetStaticMainWindow(): WidgetNode {
  return {
    base: 'StaticMainWindow',
    geometry: { id: 'staticMain', size: [420, 320], anchors: { left: 'parent.left', top: 'parent.top' }, marginTop: 6, marginLeft: 6 },
    style: { backgroundColor: 'alpha' },
    behavior: { events: { onEnter: 'StaticController.onConfirm()', onEscape: 'StaticController.onCancel()', onSetup: 'StaticController.onSetup()' } },
    children: [
      { base: 'UIWidget', geometry: { id: 'header', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, style: { backgroundColor: '#00000066' }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { textAutoResize: true, text: 'Static Window', font: 'verdana-11px-rounded' } }
      ]},
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'scroll.left', top: 'header.bottom', bottom: 'footer.top' }, padding: 6 }, style: { backgroundColor: 'alpha' }, children: [
        { base: 'Label', geometry: { id: 'info', anchors: { left: 'parent.left', right: 'parent.right' } }, style: { textWrap: true, text: 'Please wait...', font: 'verdana-11px-monochrome' } },
        { base: 'ProgressBar', geometry: { id: 'progress', anchors: { left: 'parent.left', right: 'parent.right', top: 'info.bottom' }, marginTop: 6 } }
      ]},
      { base: 'VerticalScrollBar', geometry: { id: 'scroll', anchors: { right: 'parent.right', top: 'header.bottom', bottom: 'footer.top' } } },
      { base: 'UIWidget', geometry: { id: 'footer', anchors: { left: 'parent.left', right: 'parent.right', bottom: 'parent.bottom' }, height: 28 }, style: { backgroundColor: '#00000033' }, children: [
        { base: 'Button', geometry: { id: 'cancelButton', anchors: { right: 'parent.right', bottom: 'parent.bottom' }, width: 64, marginRight: 8 }, style: { text: 'Cancel' }, behavior: { events: { onClick: 'StaticController.onCancel()' } } }
]}
]
};
}
```
**Serializer**: identyczne reguL'y jak dla MainWindow - GEOMETRIAa'STYLa'ZACHOWANIE, `text`a'`!text: tr(...)`, `events`a'`@on...`, stanya'`$...`. **Sanityzacja**: `ensureStrictOtui()` przed zapisem.<div id="ch-6-7"></div>
## 6.7 Walidator (bL'edy/ostrzeLLenia)
**Blokujace (atS):**
- Dziecko typu okno (`*Window`) wewnatrz `StaticMainWindow`.
- ScrollBar w `header`/`footer`.
- Sprzeczne kotwice (`fill` + `top/bottom/left/right`).
- `TextList`/`MultilineTextEdit` bez pary ScrollBar (przy overflow) lub bL'edne kotwice pary.
- Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeLLenia (as dZ):**
- Brak `@onEnter/@onEscape` w ekranie wymagajacym akcji (OK/Cancel).
- Brak `header`/`footer` przy zL'oLLonych ukL'adach. 
- Nieparzyste marginesy (snapping 2 px).<div id="ch-6-8"></div>
## 6.8 PrzykL'ady i edgea'cases
- **Ekran oczekiwania**: `Label` (wrap) + `ProgressBar`; `Cancel` w `footer`; brak list - ScrollBar opcjonalny.  
- **MOTD / dL'ugi komunikat**: `MultilineTextEdit` + **VerticalScrollBar**; `@onEnter` = Continue, `@onEscape` = Back.  
- **TL'o peL'noekranowe**: `image-source` + `image-fixed-ratio`; zakotwicz `anchors.fill: parent` (bez mieszania z krawedziami).  
- **Fokus**: ustaw na pierwszy przycisk/edytor; zapewnij strzaL'ki/Enter/Escape w `@onSetup`.
<div id="ch-7-1"></div>
## 7.1 Struktura (titlebar/content/footer)
**MiniWindow** to lekkie, moduL'owe okno narzedziowe. SkL'ada sie z trzech logicznych obszarow:
- **`titlebar`** - nagL'owek z tytuL'em i przyciskami (wymagane: **minimize** i **close**; opcjonalne: **back**, **pin**).
- **`content`** - gL'owna przestrzeL" robocza (formulare, listy, panele).
- **`footer`** - przyciski akcji (OK/Cancel/Apply) lub status.

**Zakazy**: w `titlebar/footer` nie umieszczaj `ScrollBar`, list ani edytorow; w `content` nie osadzaj innych okien (`*Window`).<div id="ch-7-2"></div>
## 7.2 Titlebar: minimize/close, draga'area
- **Minimize** zwija/rozwija `content` i `footer` (zmiana widocznoLci/wysokoLci); stan moLLe byc odzwierciedlany na przycisku (np. `!text: tr('-')`/`!text: tr('+')`).
- **Close** wywoL'uje akcje zamkniecia (ukrycie/usuniecie okna przez kontroler Lua).
- **Back/Pin** (opcjonalnie) - stosowane w wariantach kontenerowych/narzedziowych.
- **Draga'area**: `titlebar` moLLe peL'nic obszar przeciagania (obsL'uga po stronie klienta/kontrolera).

**Dozwolone dzieci `titlebar`**: `Label` (tytuL'), `Button` (min/close/back/pin), `UIWidget` (ikona).<div id="ch-7-3"></div>
## 7.3 Autoa'fit width i docking
- Gdy `MiniWindow` jest osadzony w panelu/kontenerze, **domyLlnie** rozciaga sie na szerokoLc rodzica: ustaw `anchors.left/right: parent` i usuL" `width`.
- Odstepy od krawedzi zapewnij przez `margin-*` (parzyste wartoLci - snapping 2 px).
- Unikaj L'aczenia `anchors.fill: parent` z recznymi kotwicami (`top/bottom/left/right`).<div id="ch-7-4"></div>
## 7.4 Stany i zdarzenia
- **Zdarzenia**: `@onEnter` (OK/Apply), `@onEscape` (Cancel/Close), `@onClick` (przyciski titlebara), `@onSetup` (bindy klawiatury).
- **Minimize toggle**: kontroler Lua przeL'acza widocznoLc `content` i `footer`.
- **Stany `$on/$!on`**: stosuj gL'ownie do przyciskow (np. podLwietlenie aktywnoLci), nie do geometrii okna.
- **Fokus**: po otwarciu ustaw fokus na pierwszym sensownym dziecku (`content`).<div id="ch-7-5"></div>
## 7.5 Blueprint OTUI (kanoniczny, STRICT)
MiniWindow < MainWindow
  id: miniWindow
  size: 260 180
  anchors.left: parent.left
  anchors.top: parent.top
  margin-top: 6
  margin-left: 6

  background-color: alpha

  @onEnter: MiniWindowController.onConfirm()
  @onEscape: MiniWindowController.onCancel()

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Mini Window')
      font: verdana-11px-rounded

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')
      @onClick: MiniWindowController.onToggleMinimize()

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')
      @onClick: MiniWindowController.onClose()

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 6

    background-color: alpha

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28

    background-color: #00000033

    Button
      id: okButton
      anchors.right: cancelButton.left
      anchors.bottom: parent.bottom
      width: 64
      margin-right: 8
      !text: tr('Ok')
      @onClick: MiniWindowController.onConfirm()

    Button
      id: cancelButton
      anchors.right: parent.right
      anchors.bottom: parent.bottom
      width: 64
      margin-right: 8
      !text: tr('Cancel')
      @onClick: MiniWindowController.onCancel()
```

<div id="ch-7-6"></div>
## 7.6 Mapowanie TS a" OTUI (serializer)
**Preset (TS)**
export function presetMiniWindow(): WidgetNode {
  return {
    base: 'MiniWindow',
    extends: 'MainWindow',
    geometry: { id: 'miniWindow', size: [260, 180], anchors: { left: 'parent.left', top: 'parent.top' }, marginTop: 6, marginLeft: 6 },
    style: { backgroundColor: 'alpha' },
    behavior: { events: { onEnter: 'MiniWindowController.onConfirm()', onEscape: 'MiniWindowController.onCancel()' } },
    children: [
      { base: 'UIWidget', geometry: { id: 'titlebar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, style: { backgroundColor: '#00000066' }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { textAutoResize: true, text: 'Mini Window', font: 'verdana-11px-rounded' } },
        { base: 'Button', geometry: { id: 'minimizeBtn', anchors: { right: 'closeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: '-' }, behavior: { events: { onClick: 'MiniWindowController.onToggleMinimize()' } } },
        { base: 'Button', geometry: { id: 'closeBtn', anchors: { right: 'parent.right', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: 'x' }, behavior: { events: { onClick: 'MiniWindowController.onClose()' } } }
      ]},
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'parent.right', top: 'titlebar.bottom', bottom: 'footer.top' }, padding: 6 }, style: { backgroundColor: 'alpha' } },
      { base: 'UIWidget', geometry: { id: 'footer', anchors: { left: 'parent.left', right: 'parent.right', bottom: 'parent.bottom' }, height: 28 }, style: { backgroundColor: '#00000033' }, children: [
        { base: 'Button', geometry: { id: 'okButton', anchors: { right: 'cancelButton.left', bottom: 'parent.bottom' }, width: 64, marginRight: 8 }, style: { text: 'Ok' }, behavior: { events: { onClick: 'MiniWindowController.onConfirm()' } } },
        { base: 'Button', geometry: { id: 'cancelButton', anchors: { right: 'parent.right', bottom: 'parent.bottom' }, width: 64, marginRight: 8 }, style: { text: 'Cancel' }, behavior: { events: { onClick: 'MiniWindowController.onCancel()' } } }
]}
]
};
}
```
**Serializer**: emituj GEOMETRIAa'STYLa'ZACHOWANIE; `style.text`a'`!text: tr('...')`; `events`a'`@on...`; stanya'`$...`. **Sanityzacja**: `ensureStrictOtui()` przed zapisem.<div id="ch-7-7"></div>
## 7.7 Walidator (bL'edy/ostrzeLLenia)
**Blokujace (atS):**
- Brak przyciskow **minimize** i **close** w `titlebar`.
- Niedozwolone dzieci w `titlebar/footer` (scroll, listy, edytory).
- `content` zawiera inne okno (`*Window`).
- Sprzeczne kotwice (`fill` + krawedzie). 
- Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeLLenia (as dZ):**
- Brak `@onEnter/@onEscape` dla okna z przyciskami akcji.
- Brak autoa'fit width (okno dokowane ma `width`).
- Nieparzyste marginesy (snapping 2 px).<div id="ch-7-8"></div>
## 7.8 PrzykL'ady i edgea'cases
- **Lista w content**: wstaw `TextList` i dokoL'kuj `VerticalScrollBar` jako **sibling** po prawej; ustaw `content.anchors.right: scroll.left`.
- **Kolaps/rozwin**: `onToggleMinimize()` ukrywa/pokazuje `content` i `footer`; przycisk zmienia label `'-'`/`'+'`.
- **Dialoga'like**: `MiniWindow` moLLe peL'nic role prostego dialogu - dodaj `@onEnter/@onEscape` i ukL'ad przyciskow w `footer`.
- **Wiele MiniWindow**: kaLLde musi miec unikalne `id`; edytor powinien zapobiegac kolizjom przy imporcie.
<div id="ch-8-1"></div>
## 8.1 Struktura (titlebar/content)
**ContainerWindow** sL'uLLy do prezentacji i operacji na zawartoLci (sloty/elementy). SkL'ada sie z:
- **`titlebar`** - nagL'owek z przyciskami **back/pin/minimize/close** i tytuL'em,
- **`content`** - obszar siatki slotow (przewijalny przy overflow). 

**Zakazy**: w `titlebar` brak list/edytorow/scrollbarow; w `content` brak okiena'dzieci (`*Window`).

**Autoa'fit width**: po osadzeniu w panelu okno powinno rozciagac sie poziomo (`anchors.left/right: parent`), odstepy przez `margin-*`.<div id="ch-8-2"></div>
## 8.2 Titlebar: back/pin/min/close
- **Back** - powrot do poprzedniego kontenera (kontroler Lua zarzadza stosem/nawigacja).
- **Pin/Lock** - przypina okno (zachowanie w kontrolerze; moLLe wpL'ywac na za'order/dokowanie).
- **Minimize** - zwija `content` (i ukrywa ewentualny `footer` jeLli wystepuje), stan sygnalizowany na przycisku.
- **Close** - ukrywa/zamyka okno przez kontroler.

**Dozwolone dzieci `titlebar`**: `Label` (tytuL'), `Button` (back/pin/min/close), `UIWidget` (ikona).<div id="ch-8-3"></div>
## 8.3 Content: siatka slotow i DnD
- **Siatka**: projektowana jako `UIWidget id: grid`, z **powtarzanymi** dziecmi `SlotWidget < UIWidget` (staL'y rozmiar i odstepy). 
- **Rozmieszczenie**: edytor dba o snapping (2 px) i kolumny/wiersze; runtime moLLe dynamicznie przepinac sloty, ale eksport zachowuje deterministyczny ukL'ad.
- **DnD**: LsrodL'o/cel tylko w `content` (sloty). PodLwietlenie slotu podczas hover/mocy przeniesienia realizowane stanami na `SlotWidget` lub przez kontroler Lua.
- **Scroll**: przy overflow dodaj **VerticalScrollBar** jako sibling po prawej; `grid.anchors.right: scroll.left`.<div id="ch-8-4"></div>
## 8.4 Scroll i overflow
- **VerticalScrollBar** dokowany do prawej krawedzi `ContainerWindow`; `grid` kotwiczy `right: scroll.left`.
- **Step/pixels**: ustaw `step` zgodnie z wysokoLcia slotu (np. 32/36), aby skok przewijania pokrywaL' rzad.
- **Samotny ScrollBar** lub listy/edytory w `titlebar` - bL'ad walidacji.<div id="ch-8-5"></div>
## 8.5 Blueprint OTUI (kanoniczny, STRICT)
ContainerWindow < MainWindow
  id: containerWindow
  size: 300 220
  anchors.left: parent.left
  anchors.top: parent.top
  margin-top: 6
  margin-left: 6

  background-color: alpha

  @onEnter: ContainerController.onConfirm()
  @onEscape: ContainerController.onBack()

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Container')
      font: verdana-11px-rounded

    Button
      id: backBtn
      anchors.right: pinBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('<')
      @onClick: ContainerController.onBack()

    Button
      id: pinBtn
      anchors.right: minimizeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('*')
      @onClick: ContainerController.onTogglePin()

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')
      @onClick: ContainerController.onToggleMinimize()

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')
      @onClick: ContainerController.onClose()

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: titlebar.bottom
    anchors.bottom: parent.bottom
    padding: 6

    background-color: alpha

    UIWidget
      id: grid
      anchors.left: parent.left
      anchors.top: parent.top
      width: 1
      height: 1

      SlotWidget < UIWidget
        id: slot1
        size: 36 36
        background-color: #00000033

      SlotWidget < UIWidget
        id: slot2
        anchors.left: slot1.right
        anchors.top: slot1.top
        margin-left: 4
        size: 36 36
        background-color: #00000033

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: parent.bottom
    step: 36
```

<div id="ch-8-6"></div>
## 8.6 Mapowanie TS a" OTUI (serializer)
**Preset (TS)**
export function presetContainerWindow(): WidgetNode {
  return {
    base: 'ContainerWindow',
    extends: 'MainWindow',
    geometry: { id: 'containerWindow', size: [300, 220], anchors: { left: 'parent.left', top: 'parent.top' }, marginTop: 6, marginLeft: 6 },
    style: { backgroundColor: 'alpha' },
    behavior: { events: { onEnter: 'ContainerController.onConfirm()', onEscape: 'ContainerController.onBack()' } },
    children: [
      { base: 'UIWidget', geometry: { id: 'titlebar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, style: { backgroundColor: '#00000066' }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { textAutoResize: true, text: 'Container', font: 'verdana-11px-rounded' } },
        { base: 'Button', geometry: { id: 'backBtn', anchors: { right: 'pinBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 20 }, style: { text: '<' }, behavior: { events: { onClick: 'ContainerController.onBack()' } } },
        { base: 'Button', geometry: { id: 'pinBtn', anchors: { right: 'minimizeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 20 }, style: { text: '*' }, behavior: { events: { onClick: 'ContainerController.onTogglePin()' } } },
        { base: 'Button', geometry: { id: 'minimizeBtn', anchors: { right: 'closeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: '-' }, behavior: { events: { onClick: 'ContainerController.onToggleMinimize()' } } },
        { base: 'Button', geometry: { id: 'closeBtn', anchors: { right: 'parent.right', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: 'x' }, behavior: { events: { onClick: 'ContainerController.onClose()' } } }
      ]},
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'scroll.left', top: 'titlebar.bottom', bottom: 'parent.bottom' }, padding: 6 }, style: { backgroundColor: 'alpha' }, children: [
        { base: 'UIWidget', geometry: { id: 'grid', anchors: { left: 'parent.left', top: 'parent.top' }, size: [1,1] }, children: [
          { base: 'SlotWidget', extends: 'UIWidget', geometry: { id: 'slot1', size: [36,36] }, style: { backgroundColor: '#00000033' } },
          { base: 'SlotWidget', extends: 'UIWidget', geometry: { id: 'slot2', anchors: { left: 'slot1.right', top: 'slot1.top' }, marginLeft: 4, size: [36,36] }, style: { backgroundColor: '#00000033' } }
]}
      ]},
      { base: 'VerticalScrollBar', geometry: { id: 'scroll', anchors: { right: 'parent.right', top: 'titlebar.bottom', bottom: 'parent.bottom' } }, behavior: { } }
]
};
}
```
**Serializer**: GEOMETRIAa'STYLa'ZACHOWANIE; `style.text`a'`!text: tr('...')`; `events`a'`@on...`. **Sanityzacja**: `ensureStrictOtui()`.

**Uwaga**: `SlotWidget < UIWidget` to **lokalna klasa stylu** w pliku; w realnym projekcie moLLesz podmienic na wL'asny typ slotu.<div id="ch-8-7"></div>
## 8.7 Walidator (bL'edy/ostrzeLLenia)
**Blokujace (atS):**
- Brak przycisku **back** w `titlebar` (nawigacja kontenera).
- Niedozwolone dzieci w `titlebar` (scroll/listy/edytory).
- `content` zawiera inne okno (`*Window`).
- `VerticalScrollBar` bez sparowanej treLci (`grid`) lub odwrotnie (overflow bez scrolla).
- Sprzeczne kotwice (`fill` + krawedzie). Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeLLenia (as dZ):**
- Brak `pin`/`minimize`/`close` w `titlebar` (wymagane zaleLLnie od projektu). 
- `step` scrolla nie odpowiada wysokoLci wiersza slotow (nieprzyjemne przewijanie). 
- Nieparzyste marginesy/spacing (snapping 2 px).<div id="ch-8-8"></div>
## 8.8 PrzykL'ady i edgea'cases
- **Powrot (back)**: `ContainerController.onBack()` przywraca poprzedni kontener (stack), a `@onEscape` mapuje sie na te sama akcje.
- **Pin/Lock**: przeL'acza stan "przypiety" okna; w `$on` przycisku moLLesz zmienic kolor/ikone.
- **Overflow**: przy dodaniu N+1 rzedu slotow a' edytor proponuje VerticalScrollBar i kotwice `grid.right: scroll.left`.
- **DnD**: slot w stanie "hover" (`$focus` lub wL'asny stan logiczny) zmienia tL'o; kontroler waliduje dozwolone dropy.
- **Minimalne rozmiary slotu**: aA32A-32 (lub projektowe), spacing aA4 px - zapewnij spojnoLc siatki.

---
## 9. DialogWindow
- [9.1 Struktura](#ch-9-1)
- [9.2 Enter/Escape (OK/Cancel)](#ch-9-2)
- [9.3 ModalnoLc i fokus](#ch-9-3)
- [9.4 Blueprint OTUI (STRICT)](#ch-9-4)
- [9.5 Preset TS (serializera'ready)](#ch-9-5)
- [9.6 Walidator (bL'edy/ostrzeLLenia)](#ch-9-6)
- [9.7 PrzykL'ady i edgea'cases](#ch-9-7)

<div id="ch-9-1"></div>
## 9.1 Struktura
**DialogWindow** to lekkie okno dialogowe do potwierdzeL", komunikatow i prostych promptow.
- Obszary: `titlebar`, `content`, `footer` (analogicznie do MiniWindow).
- Wymagane skroty: **Enter = OK**, **Escape = Cancel**.
- Zakazy: brak okiena'dzieci (`*Window`) w `content`; brak list/edytorow/scrolla w `titlebar`/`footer`.

<div id="ch-9-2"></div>
## 9.2 Enter/Escape (OK/Cancel)
- `@onEnter` a' akcja domyLlna (OK/Apply).
- `@onEscape` a' anulowanie/zamkniecie.
- Edytor wymusza obecnoLc **co najmniej jednego** przycisku w `footer` i mapuje go na Enter/Escape zgodnie z rola.

<div id="ch-9-3"></div>
## 9.3 ModalnoLc i fokus
- ModalnoLc: opcjonalna (np. przez overlay moduL'u).
- Po otwarciu ustaw fokus na domyLlny przycisk OK lub pierwsze pole edycji.
- Zamkniecie: kontroler Lua decyduje o `:hide()` i sprzataniu zasobow.

<div id="ch-9-4"></div>
## 9.4 Blueprint OTUI (STRICT)
DialogWindow < MainWindow
  id: dialog
  size: 300 140
  anchors.left: parent.left
  anchors.top: parent.top
  margin-top: 8
  margin-left: 8

  background-color: alpha

  @onEnter: DialogController.onOk()
  @onEscape: DialogController.onCancel()

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Dialog')
      font: verdana-11px-rounded

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 8

    background-color: alpha

    Label
      id: message
      anchors.left: parent.left
      anchors.right: parent.right
      text-wrap: true
      !text: tr('Are you sure?')
      font: verdana-11px-monochrome

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 32

    background-color: #00000033

    Button
      id: okButton
      anchors.right: cancelButton.left
      anchors.bottom: parent.bottom
      width: 72
      margin-right: 8
      !text: tr('Ok')
      @onClick: DialogController.onOk()

    Button
      id: cancelButton
      anchors.right: parent.right
      anchors.bottom: parent.bottom
      width: 72
      margin-right: 8
      !text: tr('Cancel')
      @onClick: DialogController.onCancel()
```

<div id="ch-9-5"></div>
## 9.5 Preset TS (serializera'ready)
export function presetDialogWindow(): WidgetNode {
  return {
    base: 'DialogWindow', extends: 'MainWindow',
    geometry: { id: 'dialog', size: [300,140], anchors: { left: 'parent.left', top: 'parent.top' }, marginTop: 8, marginLeft: 8 },
    style: { backgroundColor: 'alpha' },
    behavior: { events: { onEnter: 'DialogController.onOk()', onEscape: 'DialogController.onCancel()' } },
    children: [
      { base: 'UIWidget', geometry: { id: 'titlebar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, style: { backgroundColor: '#00000066' }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { textAutoResize: true, text: 'Dialog', font: 'verdana-11px-rounded' } }
      ]},
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'parent.right', top: 'titlebar.bottom', bottom: 'footer.top' }, padding: 8 }, style: { backgroundColor: 'alpha' }, children: [
        { base: 'Label', geometry: { id: 'message', anchors: { left: 'parent.left', right: 'parent.right' } }, style: { textWrap: true, text: 'Are you sure?', font: 'verdana-11px-monochrome' } }
      ]},
      { base: 'UIWidget', geometry: { id: 'footer', anchors: { left: 'parent.left', right: 'parent.right', bottom: 'parent.bottom' }, height: 32 }, style: { backgroundColor: '#00000033' }, children: [
        { base: 'Button', geometry: { id: 'okButton', anchors: { right: 'cancelButton.left', bottom: 'parent.bottom' }, width: 72, marginRight: 8 }, style: { text: 'Ok' }, behavior: { events: { onClick: 'DialogController.onOk()' } } },
        { base: 'Button', geometry: { id: 'cancelButton', anchors: { right: 'parent.right', bottom: 'parent.bottom' }, width: 72, marginRight: 8 }, style: { text: 'Cancel' }, behavior: { events: { onClick: 'DialogController.onCancel()' } } }
]}
]
};
}
```

<div id="ch-9-6"></div>
## 9.6 Walidator (bL'edy/ostrzeLLenia)
**Blokujace (atS):** brak `@onEnter/@onEscape`; brak przyciskow w `footer` lub brak mapowania OK/Escape; dzieci niedozwolone w `titlebar/footer` (listy/edytory/scroll); `*Window` w `content`; sprzeczne kotwice; brak `tr()`; zasoby spoza `data/`.

**OstrzeLLenia (as dZ):** brak autoa'fit w poziomie po dokowaniu; nieparzyste marginesy/spacing.

<div id="ch-9-7"></div>
## 9.7 PrzykL'ady i edgea'cases
- Prompt z `TextEdit`: pole w `content` + mapowanie Enter/Escape na OK/Cancel.
- DL'ugi tekst: `MultilineTextEdit` + **VerticalScrollBar** (sibling) i wrapping label z leadem.
- Dialoga'potwierdzenie otwierany z MiniWindow: fokus od razu na OK; Escape zamyka bez skutkow ubocznych.

---
## 10. Titlebar
- [10.1 Ikona, tytuL', przyciski](#ch-10-1)
- [10.2 Slot i dozwolone dzieci](#ch-10-2)
- [10.3 Draga'move i fokus](#ch-10-3)
- [10.4 Blueprint OTUI (STRICT)](#ch-10-4)
- [10.5 Preset TS (warianty back/pin)](#ch-10-5)
- [10.6 Walidator](#ch-10-6)
- [10.7 Integracja (Lua glue)](#ch-10-7)

<div id="ch-10-1"></div>
## 10.1 Ikona, tytuL', przyciski
**Titlebar** to pasek nagL'owka okna. Typowe elementy:
- **Ikona** (`UIWidget` z obrazem) - opcjonalna z lewej.
- **TytuL'** (`Label`) - `text-auto-resize: true`, wyrownanie do lewej.
- **Przyciski** (`Button`) - po prawej: **minimize**, **close**, opcjonalnie **back**, **pin**.
- WysokoLc staL'a (np. 20 px); tL'o/kolor zgodne z motywem.

<div id="ch-10-2"></div>
## 10.2 Slot i dozwolone dzieci
- Titlebar jest **wydzielonym `UIWidget`** (slot) wewnatrz okna (`*Window`).
- Dozwolone dzieci: `Label`, `Button`, `UIWidget` (ikona).
- Zakazane: listy, edytory, ScrollBary i inne okna.
- Przyciski powinny miec jednolite szerokoLci (16-20 px) i kotwice do prawej krawedzi.

<div id="ch-10-3"></div>
## 10.3 Draga'move i fokus
- Obszar przeciagania moLLe obejmowac caL'y `titlebar` (obsL'uga po stronie klienta/kontrolera).
- Klik w tytuL'/puste pole nie powinien zabierac fokusu kluczowym elementom w `content`.
- Skroty dla przyciskow moLLna zmapowac w `@onSetup`/Lua.

<div id="ch-10-4"></div>
## 10.4 Blueprint OTUI (STRICT)
TitlebarWidget < UIWidget
  id: titlebar
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 20

  background-color: #00000066

  Label
    id: title
    anchors.left: parent.left
    anchors.verticalCenter: parent.verticalCenter
    margin-left: 6
    text-auto-resize: true
    !text: tr('Title')
    font: verdana-11px-rounded

  Button
    id: minimizeBtn
    anchors.right: closeBtn.left
    anchors.verticalCenter: parent.verticalCenter
    width: 16
    !text: tr('-')

  Button
    id: closeBtn
    anchors.right: parent.right
    anchors.verticalCenter: parent.verticalCenter
    width: 16
    !text: tr('x')
```

<div id="ch-10-5"></div>
## 10.5 Preset TS (warianty back/pin)
export function presetTitlebar(opts?: { withBack?: boolean; withPin?: boolean; }): WidgetNode {
  const children: WidgetNode[] = [
    { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { textAutoResize: true, text: 'Title', font: 'verdana-11px-rounded' } },
    { base: 'Button', geometry: { id: 'minimizeBtn', anchors: { right: 'closeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: '-' } },
    { base: 'Button', geometry: { id: 'closeBtn', anchors: { right: 'parent.right', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: 'x' } }
];
  if (opts?.withPin) {
    children.splice(2,0,{ base: 'Button', geometry: { id: 'pinBtn', anchors: { right: 'minimizeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 20 }, style: { text: '*' } });
}
  if (opts?.withBack) {
    children.unshift({ base: 'Button', geometry: { id: 'backBtn', anchors: { right: children[0]?.geometry?.id ? `${children[0].geometry!.id}.left` : 'minimizeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 20 }, style: { text: '<' } });
}
  return {
    base: 'TitlebarWidget', extends: 'UIWidget',
    geometry: { id: 'titlebar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 },
    style: { backgroundColor: '#00000066' },
    children
};
}
```

<div id="ch-10-6"></div>
## 10.6 Walidator
- atS Dzieci spoza dozwolonego zestawu (lista/edytory/scroll).
- atS Brak `minimize`/`close` tam, gdzie wymagane (MiniWindow/Container/Dialog).
- atS Niepoprawne kotwice (przyciski bez powiazaL" do prawej krawedzi).
- as dZ Brak `back`/`pin` w wariantach wymaganych projektowo.
- as dZ Nieparzyste marginesy i niespojne szerokoLci przyciskow.

<div id="ch-10-7"></div>
## 10.7 Integracja (Lua glue)
TitlebarController = {}

function TitlebarController.onMinimize()
  local content = rootWidget:recursiveGetChildById('content')
  local footer  = rootWidget:recursiveGetChildById('footer')
  if not content then return end
  local show = not content:isVisible()
  content:setVisible(show)
  if footer then footer:setVisible(show) end
end

function TitlebarController.onClose()
  local owner = rootWidget:recursiveGetChildById('miniWindow') or rootWidget:recursiveGetChildById('containerWindow') or rootWidget:recursiveGetChildById('dialog')
  if owner then owner:hide() end
end

function TitlebarController.onBack()
  if ContainerController and ContainerController.onBack then
    ContainerController.onBack()
  end
end

function TitlebarController.onTogglePin()
  -- przeL'acz stan przypiecia; szczegoL'y zaleLLne od projektu
end
```

---
## 11. Toolbar
- [11.1 Rola i struktura](#ch-11-1)
- [11.2 Dozwolone dzieci](#ch-11-2)
- [11.3 Geometria i styl](#ch-11-3)
- [11.4 Stany i zdarzenia](#ch-11-4)
- [11.5 Blueprint OTUI (STRICT)](#ch-11-5)
- [11.6 Preset TS (serializera'ready)](#ch-11-6)
- [11.7 Walidator](#ch-11-7)
- [11.8 PrzykL'ady i edgea'cases](#ch-11-8)

<div id="ch-11-1"></div>
## 11.1 Rola i struktura
**Toolbar** to pasek akcji, zwykle pod `titlebar` lub w `header`. Zawiera grupy przyciskow i separatory.

<div id="ch-11-2"></div>
## 11.2 Dozwolone dzieci
Dozwolone: `Button` (akcje/toggle), `UIWidget` jako separator lub ikona. Niedozwolone: listy, edytory, ScrollBary i okna.

<div id="ch-11-3"></div>
## 11.3 Geometria i styl
WysokoLc staL'a (np. 20-24). Anchors lewoa'prawo do rodzica. TL'o poL'przezroczyste lub obraz motywu. Jednolite odstepy miedzy grupami.

<div id="ch-11-4"></div>
## 11.4 Stany i zdarzenia
Przyciski moga miec stany `$on/$!on` (toggle). Zdarzenia `@onClick`. Klawiszowe skroty wiaLL w `@onSetup` okna.

<div id="ch-11-5"></div>
## 11.5 Blueprint OTUI (STRICT)
ToolbarWidget < UIWidget
  id: toolbar
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 20

  background-color: #00000044

  Button
    id: action1
    anchors.left: parent.left
    anchors.verticalCenter: parent.verticalCenter
    width: 60
    !text: tr('Action')

  UIWidget
    id: sep1
    anchors.left: action1.right
    anchors.verticalCenter: parent.verticalCenter
    margin-left: 6
    width: 1
    height: 12
    background-color: #ffffff33

  Button
    id: toggle1
    anchors.left: sep1.right
    anchors.verticalCenter: parent.verticalCenter
    margin-left: 6
    width: 60
    !text: tr('Toggle')

    $on:
      background-color: #ffffff22

    $!on:
      background-color: alpha
```

<div id="ch-11-6"></div>
## 11.6 Preset TS (serializera'ready)
export function presetToolbar(): WidgetNode {
  return {
    base: 'ToolbarWidget', extends: 'UIWidget',
    geometry: { id: 'toolbar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 },
    style: { backgroundColor: '#00000044' },
    children: [
      { base: 'Button', geometry: { id: 'action1', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, width: 60 }, style: { text: 'Action' } },
      { base: 'UIWidget', geometry: { id: 'sep1', anchors: { left: 'action1.right', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6, width: 1, height: 12 }, style: { backgroundColor: '#ffffff33' } },
      { base: 'Button', geometry: { id: 'toggle1', anchors: { left: 'sep1.right', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6, width: 60 }, style: { text: 'Toggle' }, behavior: { states: { on: { backgroundColor: '#ffffff22' }, off: { backgroundColor: 'alpha' } } } }
]
};
}
```

<div id="ch-11-7"></div>
## 11.7 Walidator
atS Listy/edytory/scroll w Toolbar. atS Brak wysokoLci. atS Nieparzyste marginesy lub nierowne szerokoLci w grupie. as dZ Brak skrotow dla akcji o wysokiej czestotliwoLci.

<div id="ch-11-8"></div>
## 11.8 PrzykL'ady i edgea'cases
Lewa grupa akcji + prawa grupa statusow; wariant kompaktowy 16 px wysokoLci; tryb toggle dla filtrow danych.

---
## 12. Panel / GroupBox
- [12.1 Rola i struktura](#ch-12-1)
- [12.2 Dozwolone dzieci](#ch-12-2)
- [12.3 Geometria i styl](#ch-12-3)
- [12.4 Stany i zdarzenia](#ch-12-4)
- [12.5 Blueprinty OTUI (STRICT)](#ch-12-5)
- [12.6 Presety TS](#ch-12-6)
- [12.7 Walidator](#ch-12-7)
- [12.8 PrzykL'ady i edgea'cases](#ch-12-8)

<div id="ch-12-1"></div>
## 12.1 Rola i struktura
**Panel** to podstawowy kontener sekcji. **GroupBox** to panel z nagL'owkiem i ramka/separatorem.

<div id="ch-12-2"></div>
## 12.2 Dozwolone dzieci
Dozwolone: wszystkie elementy "panelowe" (Label, Button, TextEdit, MultilineTextEdit, TextList, ComboBox, CheckBox, ProgressBar, TabBar, Splitter, VerticalScrollBar, HorizontalSeparator, UIWidget). Niedozwolone: okna (`*Window`).

<div id="ch-12-3"></div>
## 12.3 Geometria i styl
Anchors zgodne z ukL'adem rodzica. Marginesy i padding parzyste. TL'o transparentne lub obraz/kolor sekcji. GroupBox ma label nagL'owka oraz obramowanie lub separator pod tytuL'em.

<div id="ch-12-4"></div>
## 12.4 Stany i zdarzenia
Zwykle brak stanow na samym Panelu; stany stosuj na dzieciach. Zdarzenia klikalne tylko, jeLli Panel peL'ni role przyciskopodobna.

<div id="ch-12-5"></div>
## 12.5 Blueprinty OTUI (STRICT)
Panel
  id: panel
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 100

  background-color: alpha

  Label
    id: caption
    anchors.left: parent.left
    anchors.top: parent.top
    margin-left: 6
    margin-top: 6
    !text: tr('Panel')
    font: verdana-11px-rounded

  UIWidget
    id: body
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: caption.bottom
    anchors.bottom: parent.bottom
    padding: 6

    background-color: alpha
```

GroupBox < UIWidget
  id: group
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 120

  background-color: alpha

  Label
    id: header
    anchors.left: parent.left
    anchors.top: parent.top
    margin-left: 6
    margin-top: 4
    !text: tr('Group')
    font: verdana-11px-rounded

  UIWidget
    id: separator
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: header.bottom
    margin-top: 4
    height: 1
    background-color: #ffffff33

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: separator.bottom
    anchors.bottom: parent.bottom
    padding: 6

    background-color: alpha
```

<div id="ch-12-6"></div>
## 12.6 Presety TS
export function presetPanel(): WidgetNode {
  return {
    base: 'Panel',
    geometry: { id: 'panel', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 100 },
    style: { backgroundColor: 'alpha' },
    children: [
      { base: 'Label', geometry: { id: 'caption', anchors: { left: 'parent.left', top: 'parent.top' }, marginLeft: 6, marginTop: 6 }, style: { text: 'Panel', font: 'verdana-11px-rounded' } },
      { base: 'UIWidget', geometry: { id: 'body', anchors: { left: 'parent.left', right: 'parent.right', top: 'caption.bottom', bottom: 'parent.bottom' }, padding: 6 }, style: { backgroundColor: 'alpha' } }
]
};
}

export function presetGroupBox(): WidgetNode {
  return {
    base: 'GroupBox', extends: 'UIWidget',
    geometry: { id: 'group', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 120 },
    style: { backgroundColor: 'alpha' },
    children: [
      { base: 'Label', geometry: { id: 'header', anchors: { left: 'parent.left', top: 'parent.top' }, marginLeft: 6, marginTop: 4 }, style: { text: 'Group', font: 'verdana-11px-rounded' } },
      { base: 'UIWidget', geometry: { id: 'separator', anchors: { left: 'parent.left', right: 'parent.right', top: 'header.bottom' }, marginTop: 4, height: 1 }, style: { backgroundColor: '#ffffff33' } },
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'parent.right', top: 'separator.bottom', bottom: 'parent.bottom' }, padding: 6 }, style: { backgroundColor: 'alpha' } }
]
};
}
```

<div id="ch-12-7"></div>
## 12.7 Walidator
atS Okna (`*Window`) jako dzieci. atS Brak obszaru treLci w GroupBox. atS Sprzeczne kotwice. atS Brak `tr()` w nagL'owkach. as dZ Nieparzyste marginesy/padding. as dZ Brak autoa'fit przy dokowaniu.

<div id="ch-12-8"></div>
## 12.8 PrzykL'ady i edgea'cases
Panel z formularzem i przyciskami akcji w dolnym rogu; GroupBox z wieloma polami i czytelnym separatorem; warianty z tL'em obrazkowym.

---
## 13. TabBar / TabWidget
- [13.1 Rola i struktura](#ch-13-1)
- [13.2 Dozwolone dzieci](#ch-13-2)
- [13.3 Geometria i styl](#ch-13-3)
- [13.4 Stany i zdarzenia](#ch-13-4)
- [13.5 Blueprinty OTUI (STRICT)](#ch-13-5)
- [13.6 Presety TS](#ch-13-6)
- [13.7 Walidator](#ch-13-7)
- [13.8 PrzykL'ady i edgea'cases](#ch-13-8)

<div id="ch-13-1"></div>
## 13.1 Rola i struktura
**TabBar** zawiera przyciski zakL'adek. **TabWidget** lub dedykowany `UIWidget` jest kontenerem treLci zakL'adki. TabBar i treLc sa rodzeL"stwem w drzewie.

<div id="ch-13-2"></div>
## 13.2 Dozwolone dzieci
TabBar: `Button` dla kaLLdej zakL'adki, ewentualne separatory. TreLc zakL'adki: dowolne elementy panelowe. Niedozwolone: okna w treLci, ScrollBar w TabBarze.

<div id="ch-13-3"></div>
## 13.3 Geometria i styl
TabBar u gory, rozciagniety poziomo. Content poniLLej, zakotwiczony do TabBar `top: tabBar.bottom`. StaL'e wysokoLci przyciskow.

<div id="ch-13-4"></div>
## 13.4 Stany i zdarzenia
Aktywna zakL'adka moLLe miec `$on`. Zdarzenie zmiany zakL'adki mapowane do kontrolera (np. `TabsController.onTabChange(index)`), ewentualnie `@onClick` na przycisku zakL'adki.

<div id="ch-13-5"></div>
## 13.5 Blueprinty OTUI (STRICT)
TabBarWidget < UIWidget
  id: tabBar
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 20

  background-color: #00000044

  Button
    id: tab1
    anchors.left: parent.left
    anchors.verticalCenter: parent.verticalCenter
    width: 60
    !text: tr('Tab 1')

    $on:
      background-color: #ffffff22

    $!on:
      background-color: alpha

  Button
    id: tab2
    anchors.left: tab1.right
    anchors.verticalCenter: parent.verticalCenter
    margin-left: 4
    width: 60
    !text: tr('Tab 2')
```

TabContent < UIWidget
  id: tabContent
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: tabBar.bottom
  anchors.bottom: parent.bottom

  background-color: alpha
```

<div id="ch-13-6"></div>
## 13.6 Presety TS
export function presetTabs(): WidgetNode[] {
  const tabBar: WidgetNode = {
    base: 'TabBarWidget', extends: 'UIWidget',
    geometry: { id: 'tabBar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 },
    style: { backgroundColor: '#00000044' },
    children: [
      { base: 'Button', geometry: { id: 'tab1', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, width: 60 }, style: { text: 'Tab 1' }, behavior: { states: { on: { backgroundColor: '#ffffff22' }, off: { backgroundColor: 'alpha' } } } },
      { base: 'Button', geometry: { id: 'tab2', anchors: { left: 'tab1.right', verticalCenter: 'parent.verticalCenter' }, marginLeft: 4, width: 60 }, style: { text: 'Tab 2' } }
]
};
  const content: WidgetNode = {
    base: 'TabContent', extends: 'UIWidget',
    geometry: { id: 'tabContent', anchors: { left: 'parent.left', right: 'parent.right', top: 'tabBar.bottom', bottom: 'parent.bottom' } },
    style: { backgroundColor: 'alpha' }
};
  return [tabBar, content];
}
```

<div id="ch-13-7"></div>
## 13.7 Walidator
atS TreLc upakowana do TabBar zamiast do dedykowanego kontenera. atS Brak aktywnej zakL'adki. atS Sprzeczne kotwice. atS Brak `tr()` w etykietach. as dZ Brak mechanizmu zmiany zakL'adki w kontrolerze.

<div id="ch-13-8"></div>
## 13.8 PrzykL'ady i edgea'cases
Dwie zakL'adki z roLLnymi panelami treLci; adaptacja do maL'ej szerokoLci przez skrotowe etykiety; synchronizacja aktywnoLci z kontrolerem i stanem `$on` na przycisku.

---
## 14. Splitter
- [14.1 Rola i struktura](#ch-14-1)
- [14.2 Dozwolone dzieci](#ch-14-2)
- [14.3 Geometria i styl](#ch-14-3)
- [14.4 Stany i zdarzenia](#ch-14-4)
- [14.5 Blueprinty OTUI (STRICT) - poziomy/pionowy](#ch-14-5)
- [14.6 Presety TS](#ch-14-6)
- [14.7 Walidator](#ch-14-7)
- [14.8 PrzykL'ady i edgea'cases](#ch-14-8)
- [14.9 Splitter - grip i persystencja](#ch-14-9)

<div id="ch-14-1"></div>
## 14.1 Rola i struktura
**Splitter** dzieli obszar na dwie czeLci (panele) z regulowanym podziaL'em. Stosowany do ukL'adow "lista a" szczegoL'y", "nawigacja a" treLc".

<div id="ch-14-2"></div>
## 14.2 Dozwolone dzieci
Dopuszczalne sa **dokL'adnie dwa panele** (np. `UIWidget`/`Panel`). Dodatkowe elementy (np. overlay "grip") moga byc zastosowane tylko jako **lekki overlay** niebedacy panelem (walidator traktuje je osobno).

<div id="ch-14-3"></div>
## 14.3 Geometria i styl
- Wariant **poziomy**: lewy panel kotwiczony do lewej, prawy do prawej; granica pomiedzy panelami.
- Wariant **pionowy**: gorny panel do gory, dolny do doL'u.  
- **Mina'size** paneli: wymagana; zapewnij, by podziaL' nie "zgniataL'" dzieci poniLLej minimalnych rozmiarow.
- TL'o zwykle transparentne; granice moLLna sygnalizowac waskim paskiem.

<div id="ch-14-4"></div>
## 14.4 Stany i zdarzenia
- Zdarzenia resize i drag "gripa" implementuje kontroler (Lua) lub logika klienta. 
- Stany wizualne (hover/drag) moLLna realizowac `$focus`/`$on` na panelu/gripie.

<div id="ch-14-5"></div>
## 14.5 Blueprinty OTUI (STRICT) - poziomy/pionowy
**Poziomy (Left/Right)**
Splitter < UIWidget
  id: split
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  anchors.bottom: parent.bottom

  UIWidget
    id: leftPane
    anchors.left: parent.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    width: 160

  UIWidget
    id: rightPane
    anchors.left: leftPane.right
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
```

**Pionowy (Top/Bottom)**
Splitter < UIWidget
  id: splitV
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  anchors.bottom: parent.bottom

  UIWidget
    id: topPane
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 140

  UIWidget
    id: bottomPane
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: topPane.bottom
    anchors.bottom: parent.bottom
```

<div id="ch-14-6"></div>
## 14.6 Presety TS
export function presetSplitterHorizontal(): WidgetNode {
  return {
    base: 'Splitter', extends: 'UIWidget',
    geometry: { id: 'split', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' } },
    children: [
      { base: 'UIWidget', geometry: { id: 'leftPane', anchors: { left: 'parent.left', top: 'parent.top', bottom: 'parent.bottom' }, width: 160 } },
      { base: 'UIWidget', geometry: { id: 'rightPane', anchors: { left: 'leftPane.right', right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' } } }
]
};
}

export function presetSplitterVertical(): WidgetNode {
  return {
    base: 'Splitter', extends: 'UIWidget',
    geometry: { id: 'splitV', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' } },
    children: [
      { base: 'UIWidget', geometry: { id: 'topPane', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 140 } },
      { base: 'UIWidget', geometry: { id: 'bottomPane', anchors: { left: 'parent.left', right: 'parent.right', top: 'topPane.bottom', bottom: 'parent.bottom' } } }
]
};
}
```

<div id="ch-14-7"></div>
## 14.7 Walidator
atS a 2 paneli. atS Sprzeczne kotwice (np. oba panele maja sztywne szerokoLci i jednoczeLnie rozciagniecie). atS Brak mina'size przy wymaganym "grip" zachowaniu. as dZ Brak parzystych marginesow. as dZ Brak autoa'fit do rodzica.

<div id="ch-14-8"></div>
## 14.8 PrzykL'ady i edgea'cases
Lewy panel: lista; prawy: szczegoL'y. Gorny: log, dolny: konsola. Zapamietywanie podziaL'u w ustawieniach moduL'u (kontroler Lua).

<div id="ch-14-9"></div>
## 14.9 Splitter - grip i persystencja
- **Grip (hitbox)**: zapewnij obszar chwytu o gruboLci **6-8 px** na granicy paneli (wizualnie 1-2 px linia, reszta transparentny hitbox).  
- **Mina'size paneli**: egzekwuj `min-width/min-height` paneli (np. 120 px) - podziaL' nie moLLe ich naruszyc.  
- **Tryb klawiatury**: `Ctrl+a/a'` (poziomy) lub `Ctrl+a'/a"` (pionowy) do krokowej zmiany podziaL'u (np. 16 px).  
- **Persystencja**: zapisuj **ratio** (0..1) lub **px** w ustawieniach moduL'u i odtwarzaj przy inicjalizacji.  
- **Blueprint grip (overlay, STRICT)**:
UIWidget
  id: grip
  anchors.left: leftPane.right
  anchors.top: parent.top
  anchors.bottom: parent.bottom
  width: 8
  background-color: alpha
```
> `grip` jest **overlayem**, nie trzecim panelem (walidator nie liczy go jako dziecka Splittera).

---
## 15. TextList / ListRow
- [15.1 Rola i struktura](#ch-15-1)
- [15.2 Dozwolone dzieci](#ch-15-2)
- [15.3 Geometria i styl](#ch-15-3)
- [15.4 Scroll pairing](#ch-15-4)
- [15.5 Stany i zdarzenia](#ch-15-5)
- [15.6 Blueprinty OTUI (STRICT)](#ch-15-6)
- [15.7 Presety TS](#ch-15-7)
- [15.8 Walidator](#ch-15-8)
- [15.9 PrzykL'ady i edgea'cases](#ch-15-9)
- [15.10 TextList - nawigacja klawiatura i ensureVisible](#ch-15-10)

<div id="ch-15-1"></div>
## 15.1 Rola i struktura
**TextList** prezentuje liste pozycji przewijalna w pionie. Wiersze sa reprezentowane jako lekkie `UIWidget` (np. `ListRow`) osadzane w kontenerze listy.

<div id="ch-15-2"></div>
## 15.2 Dozwolone dzieci
Wewnatrz listy: tylko wiersze (`UIWidget`/custom row). Zakazane: okna, ScrollBar jako dziecko (ScrollBar jest **siblingiem** listy).

<div id="ch-15-3"></div>
## 15.3 Geometria i styl
- Liste kotwicz do dostepnego obszaru (`anchors.fill: parent` lub do `scroll.left`).
- WysokoLc wiersza min. ~14 px (zalecenie) dla czytelnoLci. 
- PodLwietlenie wiersza przez stany (`$focus`/`$on`) lub kolory tL'a.

<div id="ch-15-4"></div>
## 15.4 Scroll pairing
**VerticalScrollBar** jest **siblingiem**: dokowany po prawej; lista kotwiczy `right: scroll.left`. `step` powinien odpowiadac wysokoLci wiersza.

<div id="ch-15-5"></div>
## 15.5 Stany i zdarzenia
- Zdarzenia: `@onClick` na wiersz (zaznaczenie), opcjonalny `@onSetup` do bindow strzaL'ek/PageUp/Down. 
- Fokus: po otwarciu ustaw na liste lub pierwszy wiersz; upewnij sie, LLe wybrany wiersz jest widoczny (logika kontrolera).

<div id="ch-15-6"></div>
## 15.6 Blueprinty OTUI (STRICT)
**Lista ze scrollem**
UIWidget
  id: listContainer
  anchors.left: parent.left
  anchors.right: scroll.left
  anchors.top: parent.top
  anchors.bottom: parent.bottom

  TextList
    id: items
    anchors.fill: parent
```

**Scroll**
VerticalScrollBar
  id: scroll
  anchors.right: parent.right
  anchors.top: parent.top
  anchors.bottom: parent.bottom
  step: 16
```

**Wiersz listy (uniwersalny)**
ListRow < UIWidget
  id: row
  height: 16

  Label
    id: caption
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.verticalCenter: parent.verticalCenter
    margin-left: 4
    text-auto-resize: true
    !text: tr('Item')
    font: verdana-11px-monochrome

  $focus:
    background-color: #ffffff11

  $on:
    background-color: #ffffff22
```

<div id="ch-15-7"></div>
## 15.7 Presety TS
export function presetTextListWithScroll(): WidgetNode[] {
  const listContainer: WidgetNode = {
    base: 'UIWidget',
    geometry: { id: 'listContainer', anchors: { left: 'parent.left', right: 'scroll.left', top: 'parent.top', bottom: 'parent.bottom' } },
    children: [
      { base: 'TextList', geometry: { id: 'items', anchors: { fill: 'parent' } } }
]
};
  const scroll: WidgetNode = {
    base: 'VerticalScrollBar',
    geometry: { id: 'scroll', anchors: { right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' } },
    behavior: { props: { step: 16 } }
};
  return [listContainer, scroll];
}

export function presetListRow(): WidgetNode {
  return {
    base: 'ListRow', extends: 'UIWidget',
    geometry: { id: 'row', height: 16 },
    children: [
      { base: 'Label', geometry: { id: 'caption', anchors: { left: 'parent.left', right: 'parent.right', verticalCenter: 'parent.verticalCenter' }, marginLeft: 4 }, style: { textAutoResize: true, text: 'Item', font: 'verdana-11px-monochrome' } }
],
    behavior: { states: { focus: { backgroundColor: '#ffffff11' }, on: { backgroundColor: '#ffffff22' } } }
};
}
```

<div id="ch-15-8"></div>
## 15.8 Walidator
atS ScrollBar jako dziecko listy. atS Lista bez pary scrolla przy overflow lub bL'edne kotwice pary. atS `tr()` pominiete w etykietach. as dZ Zbyt maL'a wysokoLc wiersza (nieczytelnoLc). as dZ Brak bindow klawiatury.

<div id="ch-15-9"></div>
## 15.9 PrzykL'ady i edgea'cases
Lista postaci (row = imie + poziom), lista logow (row z ikona i timestampem). "Ensure visible" przy zmianie wyboru. Paging klawiatura (PageUp/Down).

<div id="ch-15-10"></div>
## 15.10 TextList - nawigacja klawiatura i ensureVisible
- **StrzaL'ki**: a'/a" wybor sasiedniego wiersza.  
- **PageUp/Down**: skok o `pageSize` (wysokoLc kontenera / wysokoLc wiersza).  
- **Home/End**: pierwszy/ostatni wiersz.  
- **Enter/Escape**: potwierdzenie/anulowanie zgodnie z logika okna.  
- **ensureVisible**: po zmianie wyboru kontroler przewija liste tak, by wybrany wiersz byL' w peL'ni widoczny.  
- **Multia'select (opcjonalnie)**: `Shift` = zakres, `Ctrl` = pojedyncze przeL'aczanie - tylko jeLli projekt to wymaga; w `.otui` bez zmian, logika w kontrolerze.

---
## 16. Label / UILabel
- [16.1 Rola i struktura](#ch-16-1)
- [16.2 WL'aLciwoLci tekstu](#ch-16-2)
- [16.3 Geometria i styl](#ch-16-3)
- [16.4 Stany i zdarzenia](#ch-16-4)
- [16.5 Blueprinty OTUI (STRICT)](#ch-16-5)
- [16.6 Presety TS](#ch-16-6)
- [16.7 Walidator](#ch-16-7)
- [16.8 PrzykL'ady i edgea'cases](#ch-16-8)
- [16.9 Label - pomiar tekstu, elipsyzacja, DPI/scale](#ch-16-9)

<div id="ch-16-1"></div>
## 16.1 Rola i struktura
**Label/UILabel** to nieinteraktywny element tekstowy do podpisow, tytuL'ow i statusow. `UILabel` moLLe sL'uLLyc jako wariant nazwowy z gotowym stylem; oba maja te same podstawowe wL'aLciwoLci tekstowe.

<div id="ch-16-2"></div>
## 16.2 WL'aLciwoLci tekstu
- `!text: tr('...')` - jedyne dozwolone LsrodL'o staL'ych napisow (STRICT).  
- `text-wrap: true|false` - zawijanie.  
- `text-auto-resize: true|false` - dopasowanie do treLci.  
- `text-align: left|center|right` - wyrownanie.  
- `text-offset: X Y` - przesuniecie.  
- `font: <nazwa>` - z `data/fonts/`.  
- `color: #AARRGGBB`.

<div id="ch-16-3"></div>
## 16.3 Geometria i styl
- Anchors do rodzica lub sasiadow; czesto `anchors.left/right: parent` przy statusach.  
- ULLywaj parzystych marginesow (snapping 2 px).  
- TL'o zwykle `alpha`.

<div id="ch-16-4"></div>
## 16.4 Stany i zdarzenia
- Label nie jest klikany; zdarzenia zwykle pomijamy.  
- Stany `$on/$!on/$focus` moLLesz wykorzystac do zmiany koloru lub wyeksponowania (np. bL'edy/ostrzeLLenia), nie geometrii.

<div id="ch-16-5"></div>
## 16.5 Blueprinty OTUI (STRICT)
**NagL'owek sekcji**
Label
  id: header
  anchors.left: parent.left
  anchors.right: parent.right
  text-auto-resize: true
  !text: tr('Section')
  font: verdana-11px-rounded
```

**Status wielowierszowy**
Label
  id: status
  anchors.left: parent.left
  anchors.right: parent.right
  text-wrap: true
  !text: tr('This is a long message that can wrap.')
  font: verdana-11px-monochrome
```

<div id="ch-16-6"></div>
## 16.6 Presety TS
export function presetLabelHeader(): WidgetNode {
  return {
    base: 'Label',
    geometry: { id: 'header', anchors: { left: 'parent.left', right: 'parent.right' } },
    style: { textAutoResize: true, text: 'Section', font: 'verdana-11px-rounded' }
};
}

export function presetLabelStatus(): WidgetNode {
  return {
    base: 'Label',
    geometry: { id: 'status', anchors: { left: 'parent.left', right: 'parent.right' } },
    style: { textWrap: true, text: 'This is a long message that can wrap.', font: 'verdana-11px-monochrome' }
};
}
```

<div id="ch-16-7"></div>
## 16.7 Walidator
atS Brak `tr()` w `!text`. atS Zasoby fontu spoza `data/`. as dZ Nieparzyste marginesy. as dZ NaduLLywanie `text-auto-resize` przy waskich ukL'adach (ryzyko overflow).

<div id="ch-16-8"></div>
## 16.8 PrzykL'ady i edgea'cases
NagL'owki w `titlebar` i w treLci; statusy z `text-wrap: true`; komunikaty ostrzegawcze kolorem w `$on`.

<div id="ch-16-9"></div>
## 16.9 Label - pomiar tekstu, elipsyzacja, DPI/scale
- **Pomiar**: unikaj twardych szerokoLci dla dL'ugich etykiet; preferuj `text-wrap: true` lub `text-auto-resize: true` (gdy bezpieczne).  
- **Elipsyzacja**: stosuj tylko przy staL'ych szerokoLciach; zapewnij tooltip z peL'nym tekstem (kontroler).  
- **DPI/Scale**: testuj metryki fontu (line-height, kerning) w skalach 1.0/1.25/1.5; utrzymuj snapping 2 px.

---
## 17. Button
- [17.1 Rola i struktura](#ch-17-1)
- [17.2 WL'aLciwoLci i minimalne rozmiary](#ch-17-2)
- [17.3 Geometria i styl](#ch-17-3)
- [17.4 Stany i zdarzenia](#ch-17-4)
- [17.5 Blueprinty OTUI (STRICT)](#ch-17-5)
- [17.6 Presety TS](#ch-17-6)
- [17.7 Walidator](#ch-17-7)
- [17.8 PrzykL'ady i edgea'cases](#ch-17-8)
- [17.9 Button - hover/disabled i dostepnoLc](#ch-17-9)

<div id="ch-17-1"></div>
## 17.1 Rola i struktura
**Button** wyzwala akcje (`@onClick`). MoLLe dziaL'ac jako chwilowy przycisk, przeL'acznik (toggle) lub przycisk paskowy (tytuL'/toolbar). Zwykle bez dzieci - tekst ustawiany bezpoLrednio przez `!text`.

<div id="ch-17-2"></div>
## 17.2 WL'aLciwoLci i minimalne rozmiary
- `!text: tr('...')` - etykieta.  
- Zalecane minimum rozmiaru: **aA16A-16** (kompakt) lub szersze dla etykiet tekstowych (np. 60-72 px).  
- Opcjonalnie `font`, `color`, `background-color`.

<div id="ch-17-3"></div>
## 17.3 Geometria i styl
- Kotwice do krawedzi rodzica lub sasiadow (czesto do prawej w `footer`/`titlebar`).  
- Parzyste marginesy; wysokoLci zgodne ze stylem paska (np. 20 px w titlebar/toolbar).  
- Tekst przez `!text` (STRICT), bez wewnetrznego `Label`.

<div id="ch-17-4"></div>
## 17.4 Stany i zdarzenia
- `@onClick: Controller.fn()` - podstawowe zdarzenie.  
- `$on/$!on` - dla trybu **toggle** (zmiana tL'a/koloru/napisu).  
- `$focus` - podLwietlenie przy fokusie klawiatury.  
- Skroty klawiszowe mapuj w `@onSetup` okna lub w Lua.

<div id="ch-17-5"></div>
## 17.5 Blueprinty OTUI (STRICT)
**Standardowy przycisk**
Button
  id: ok
  width: 64
  !text: tr('Ok')
```

**Toggle (On/Off)**
Button
  id: toggle
  width: 72
  !text: tr('Off')

  $on:
    !text: tr('On')
    background-color: #ffffff22

  $!on:
    !text: tr('Off')
    background-color: alpha
```

**Ikonowy (tytuL'/toolbar)**
Button
  id: closeBtn
  width: 16
  !text: tr('x')
```

<div id="ch-17-6"></div>
## 17.6 Presety TS
export function presetButton(label = 'Ok', id = 'ok', width = 64): WidgetNode {
  return {
    base: 'Button',
    geometry: { id, width },
    style: { text: label }
};
}

export function presetToggle(labelOff = 'Off', labelOn = 'On', id = 'toggle', width = 72): WidgetNode {
  return {
    base: 'Button',
    geometry: { id, width },
    style: { text: labelOff },
    behavior: { states: { on: { text: labelOn, backgroundColor: '#ffffff22' }, off: { text: labelOff, backgroundColor: 'alpha' } } }
};
}
```

<div id="ch-17-7"></div>
## 17.7 Walidator
atS Brak `tr()` w etykiecie. atS Zbyt maL'y rozmiar (mniej niLL 16A-16). atS Wewnetrzne dzieci (Label) zamiast `!text`. as dZ Niespojne szerokoLci w grupie. as dZ Brak skrotow dla akcji czesto uLLywanych.

<div id="ch-17-8"></div>
## 17.8 PrzykL'ady i edgea'cases
Przyciski OK/Cancel w `footer`; ikonowe 16 px w `titlebar`; toggle dla filtrow narzedzi. Zmiana etykiety w `$on/$!on` bez modyfikacji geometrii.

<div id="ch-17-9"></div>
## 17.9 Button - hover/disabled i dostepnoLc
- **$hover**: feedback najechania (kolor/tL'o), bez zmiany geometrii.  
- **$disabled**: peL'na nieinteraktywnoLc; zachowaj kontrast etykiety aA WCAG AA.  
- **Hitbox**: min. **16A-16**; dla tekstowych szerokoLc wg etykiety (aA60 px).  
- **Skroty**: najczestsze akcje zbinduj w `@onSetup`.

**PrzykL'ad (STRICT)**
Button
  id: action
  width: 64
  !text: tr('Run')

  $hover:
    background-color: #ffffff11

  $disabled:
    color: #ffffff66
    background-color: alpha
```

---
## 18. CheckBox
- [18.1 Rola i struktura](#ch-18-1)
- [18.2 WL'aLciwoLci](#ch-18-2)
- [18.3 Geometria i styl](#ch-18-3)
- [18.4 Stany i zdarzenia](#ch-18-4)
- [18.5 Blueprinty OTUI (STRICT)](#ch-18-5)
- [18.6 Presety TS](#ch-18-6)
- [18.7 Walidator](#ch-18-7)
- [18.8 PrzykL'ady i edgea'cases](#ch-18-8)
- [18.9 CheckBox - tria'state i offset etykiety](#ch-18-9)

<div id="ch-18-1"></div>
## 18.1 Rola i struktura
**CheckBox** to przeL'acznik boolean z wbudowana etykieta tekstowa po prawej. Nie posiada dzieci. Wariant **RoundCheckBox** to styl okragL'y.

<div id="ch-18-2"></div>
## 18.2 WL'aLciwoLci
- `!text: tr('...')` - etykieta.  
- `text-align`, `text-offset` - pozycjonowanie tekstu wzgledem pola.  
- `image-source`, `image-rect`/`image-clip`, `image-color` - grafika stanu.  
- `cursor`, `change-cursor-image` - zachowanie kursora.  
- `enabled: true|false` - stan dostepnoLci.

<div id="ch-18-3"></div>
## 18.3 Geometria i styl
- Typowy rozmiar pola: **16A-16**; etykieta po prawej poprzez `text-offset` (np. `18 1`).  
- Kotwice do ukL'adu rodzica; parzyste marginesy.  
- Kolory/obrazy zgodnie z motywem.

<div id="ch-18-4"></div>
## 18.4 Stany i zdarzenia
- Stany: `$checked`, `$!checked`, `$hover`, `$disabled` (moLLliwe kombinacje, np. `$hover !disabled`).  
- Zdarzenia: `@onClick` a' przeL'aczanie stanu; skrot klawiszowy mapuj w `@onSetup` lub Lua.

<div id="ch-18-5"></div>
## 18.5 Blueprinty OTUI (STRICT)
**Kwadratowy CheckBox**
CheckBox < UICheckBox
  id: accept
  size: 16 16
  text-align: left
  text-offset: 18 1
  !text: tr('Accept')
  color: #dfdfdf
  image-color: #dfdfdfff
  image-rect: 0 0 15 15
  image-source: /images/ui/checkbox
  change-cursor-image: true
  cursor: pointer

  $hover !disabled:
    color: #ffffff

  $checked:
    color: #ffffff

  $disabled:
    color: #dfdfdf88
    image-color: #dfdfdf88
```

**RoundCheckBox (okragL'y)**
RoundCheckBox < CheckBox
  id: rcheck
  image-source: /images/ui/checkbox_round

  $first:
    margin-top: 2

  $!first:
    margin-top: 5
```

<div id="ch-18-6"></div>
## 18.6 Presety TS
export function presetCheckBox(id = 'accept', label = 'Accept'): WidgetNode {
  return {
    base: 'CheckBox', extends: 'UICheckBox',
    geometry: { id, size: [16,16] },
    style: { textAlign: 'left', textOffset: [18,1], text: label, color: '#dfdfdf', imageColor: '#dfdfdfff', imageRect: [0,0,15,15], imageSource: '/images/ui/checkbox', cursor: 'pointer', changeCursorImage: true }
};
}

export function presetRoundCheckBox(id = 'rcheck', label = 'Option'): WidgetNode {
  return {
    base: 'RoundCheckBox', extends: 'CheckBox',
    geometry: { id, size: [16,16] },
    style: { textAlign: 'left', textOffset: [18,1], text: label, imageSource: '/images/ui/checkbox_round' }
};
}
```

<div id="ch-18-7"></div>
## 18.7 Walidator
atS Dzieci wewnatrz CheckBox. atS Brak `tr()` w etykiecie. atS Zbyt maL'y rozmiar pola (<16A-16). atS Niespojne kotwice. as dZ Brak kursora "pointer". as dZ Nieparzyste marginesy/offset.

<div id="ch-18-8"></div>
## 18.8 PrzykL'ady i edgea'cases
Listy opcji w Panel/GroupBox; pierwszy element z mniejszym marginesem gornym (`$first`). Tryb globalnego wL'aczania/wyL'aczania grupy kontrolek.

<div id="ch-18-9"></div>
## 18.9 CheckBox - tria'state i offset etykiety
- **Tria'state (opcjonalnie)**: jeLLeli projekt wymaga stanu "nieokreLlony", zdefiniuj stan logiczny (np. `$indeterminate`) i nadaj mu wL'asna ikone/tL'o; przeL'aczanie cykliczne: `unchecked a' checked a' indeterminate`.  
- **Offset etykiety**: utrzymuj `text-offset` tak, by tekst nie nachodziL' na pole (np. aA18 px przy polu 16A-16).

**PrzykL'ad (STRICT)**
CheckBox
  id: opt
  size: 16 16
  text-offset: 18 1
  !text: tr('Option')

  $indeterminate:
    image-source: /images/ui/checkbox_indet
```

---
## 19. TextEdit / PasswordTextEdit / MultilineTextEdit
- [19.1 Rola i struktura](#ch-19-1)
- [19.2 WL'aLciwoLci tekstowe](#ch-19-2)
- [19.3 Geometria i styl](#ch-19-3)
- [19.4 Scroll pairing (Multiline)](#ch-19-4)
- [19.5 Stany i zdarzenia](#ch-19-5)
- [19.6 Blueprinty OTUI (STRICT)](#ch-19-6)
- [19.7 Presety TS](#ch-19-7)
- [19.8 Walidator](#ch-19-8)
- [19.9 PrzykL'ady i edgea'cases](#ch-19-9)
- [19.10 TextEdit/Multiline - IME, paste i filtry wejLcia](#ch-19-10)
- [19.11 Multiline - zaznaczenie, linea'height i pixelsa'scroll](#ch-19-11)

<div id="ch-19-1"></div>
## 19.1 Rola i struktura
- **TextEdit** - jednoa'wierszowe pole tekstowe.  
- **PasswordTextEdit** - jak TextEdit, ale treLc maskowana.  
- **MultilineTextEdit** - wielowierszowe z obsL'uga zawijania i przewijania.

<div id="ch-19-2"></div>
## 19.2 WL'aLciwoLci tekstowe
- `placeholder: '...'` oraz `placeholder-color: #AARRGGBB` - tekst i kolor placeholdera.  
- `text-wrap: true|false` - zawijanie (dot. Multiline).  
- `font`, `color` - styl tekstu.

<div id="ch-19-3"></div>
## 19.3 Geometria i styl
- Kotwicz do dostepnego obszaru; przy Multiline: zapewnij wysokoLc i padding.  
- Parzyste marginesy; tL'o transparentne lub panelowe.

<div id="ch-19-4"></div>
## 19.4 Scroll pairing (Multiline)
- **VerticalScrollBar** jako **sibling**.  
- W Multiline ustaw: `vertical-scrollbar: <idScrolla>`.  
- Kotwice: Multiline `left/top/bottom` do parenta, `right` do `scroll.left`; Scroll `right/top/bottom` do parenta.  
- `step` scrolla dopasuj do wysokoLci wiersza (np. 16) i uLLyj `pixels-scroll: true` gdy wymagane.

<div id="ch-19-5"></div>
## 19.5 Stany i zdarzenia
- `@onEnter` (zatwierdzenie w TextEdit), `@onEscape` (anulowanie), `@onSetup` (bindy).  
- Fokus klawiatury na wejLciu; kontroler moLLe zarzadzac przeL'aczaniem fokusu.

<div id="ch-19-6"></div>
## 19.6 Blueprinty OTUI (STRICT)
**TextEdit (placeholder)**
TextEdit
  id: name
  anchors.left: parent.left
  anchors.right: parent.right
  height: 20
  placeholder: Name
  placeholder-color: #00000077
  font: verdana-11px-monochrome
```

**PasswordTextEdit**
PasswordTextEdit
  id: password
  anchors.left: parent.left
  anchors.right: parent.right
  height: 20
  placeholder: Password
  placeholder-color: #00000077
  font: verdana-11px-monochrome
```

**MultilineTextEdit + VerticalScrollBar**
MultilineTextEdit
  id: text
  anchors.top: scroll.top
  anchors.left: parent.left
  anchors.right: scroll.left
  anchors.bottom: scroll.bottom
  vertical-scrollbar: scroll
  text-wrap: true

VerticalScrollBar
  id: scroll
  anchors.top: parent.top
  anchors.bottom: parent.bottom
  anchors.right: parent.right
  step: 16
  pixels-scroll: true
```

<div id="ch-19-7"></div>
## 19.7 Presety TS
export function presetTextEdit(id = 'name', placeholder = 'Name'): WidgetNode {
  return {
    base: 'TextEdit',
    geometry: { id, anchors: { left: 'parent.left', right: 'parent.right' }, height: 20 },
    style: { placeholder, placeholderColor: '#00000077', font: 'verdana-11px-monochrome' }
};
}

export function presetPasswordEdit(id = 'password', placeholder = 'Password'): WidgetNode {
  return {
    base: 'PasswordTextEdit',
    geometry: { id, anchors: { left: 'parent.left', right: 'parent.right' }, height: 20 },
    style: { placeholder, placeholderColor: '#00000077', font: 'verdana-11px-monochrome' }
};
}

export function presetMultilineWithScroll(idText = 'text', idScroll = 'scroll'): WidgetNode[] {
  const text: WidgetNode = {
    base: 'MultilineTextEdit',
    geometry: { id: idText, anchors: { top: `${idScroll}.top`, left: 'parent.left', right: `${idScroll}.left`, bottom: `${idScroll}.bottom` } },
    style: { textWrap: true },
    behavior: { props: { verticalScrollbar: idScroll } }
};
  const scroll: WidgetNode = {
    base: 'VerticalScrollBar',
    geometry: { id: idScroll, anchors: { top: 'parent.top', bottom: 'parent.bottom', right: 'parent.right' } },
    behavior: { props: { step: 16, pixelsScroll: true } }
};
  return [text, scroll];
}
```

<div id="ch-19-8"></div>
## 19.8 Walidator
atS `vertical-scrollbar` wskazuje nieistniejacy `id`. atS ScrollBar jako dziecko MultilineTextEdit. atS Sprzeczne kotwice (fill + krawedzie). atS Brak placeholdera tam, gdzie wymagany UXa'owo. as dZ Zbyt maL'a wysokoLc w Multiline. as dZ Brak `pixels-scroll` dla precyzyjnego przewijania.

<div id="ch-19-9"></div>
## 19.9 PrzykL'ady i edgea'cases
Pole loginu z placeholderem i Password z maskowaniem; edytor logow z Multiline + scroll i `text-wrap: true`; walidacja Enter/Escape w kontrolerze.

<div id="ch-19-10"></div>
## 19.10 TextEdit/Multiline - IME, paste i filtry wejLcia
- **IME**: pola powinny poprawnie akceptowac kompozycje IME; nie nadpisuj w kontrolerze zdarzeL", ktore przerywaja kompozycje.  
- **Paste**: obsL'uLL `Ctrl+V`/`Shift+Insert`; opcjonalne czyszczenie wklejanego tekstu (np. biaL'a lista znakow).  
- **Filtry**: waliduj w kontrolerze (regex, max dL'ugoLc) - bez modyfikowania `.otui`.

<div id="ch-19-11"></div>
## 19.11 Multiline - zaznaczenie, linea'height i pixelsa'scroll
- **Selection**: zapewnij widoczny kolor zaznaczenia zgodny z motywem.  
- **Linea'height**: dopasuj przewijanie do metryk fontu; `step` scrollbar'a a wysokoLc linii (np. 16).  
- **pixelsa'scroll**: wL'acz dla precyzyjnych edytorow (logi/kod) - pL'ynne przewijanie bez "skokow".

---
## 20. ComboBox
- [20.1 Rola i struktura](#ch-20-1)
- [20.2 WL'aLciwoLci i menu](#ch-20-2)
- [20.3 Geometria i styl](#ch-20-3)
- [20.4 Zdarzenia i stany](#ch-20-4)
- [20.5 Blueprint OTUI (STRICT)](#ch-20-5)
- [20.6 Presety TS](#ch-20-6)
- [20.7 Walidator](#ch-20-7)
- [20.8 PrzykL'ady i edgea'cases](#ch-20-8)

<div id="ch-20-1"></div>
## 20.1 Rola i struktura
**ComboBox** to selektor pojedynczej opcji. Posiada **wewnetrzne menu** (lista opcji) zarzadzane przez klienta - **nie dodawaj** recznie dzieci w `.otui`.

<div id="ch-20-2"></div>
## 20.2 WL'aLciwoLci i menu
- `current-index: N` lub `current-text: '...'` - wybrana pozycja (jedno LsrodL'o prawdy w czasie eksportu).
- `menu-height: H` - maksymalna wysokoLc rozwinietego menu (px).
- `menu-scroll-step: S` - krok przewijania menu (px).
- `placeholder: '...'` - tekst gdy nic nie wybrano.
- Teksty opcji przechodza przez mechanizm tL'umaczeL" na poziomie logiki (nie dodawaj jako dzieci w OTUI).

<div id="ch-20-3"></div>
## 20.3 Geometria i styl
- SzerokoLc staL'a lub `anchors.left/right: parent`.  
- Minimalna wysokoLc ~20 px.  
- TL'o zgodne z motywem; strzaL'ka rozwijania po prawej (render klienta/skinu).

<div id="ch-20-4"></div>
## 20.4 Zdarzenia i stany
- `@onOptionChange: Controller.fn(index, text)` - zmiana wyboru.  
- `$focus` - podLwietlenie fokusowanej kontrolki.  
- `$disabled` - wyglad nieaktywny.

<div id="ch-20-5"></div>
## 20.5 Blueprint OTUI (STRICT)
ComboBox
  id: combo
  anchors.left: parent.left
  anchors.right: parent.right
  height: 20
  placeholder: Select
  menu-height: 120
  menu-scroll-step: 16

  @onOptionChange: ComboController.onChange(index, text)
```

<div id="ch-20-6"></div>
## 20.6 Presety TS
export function presetComboBox(id = 'combo', placeholder = 'Select'): WidgetNode {
  return {
    base: 'ComboBox',
    geometry: { id, anchors: { left: 'parent.left', right: 'parent.right' }, height: 20 },
    style: { placeholder, menuHeight: 120, menuScrollStep: 16 },
    behavior: { events: { onOptionChange: 'ComboController.onChange(index, text)' } }
};
}
```

<div id="ch-20-7"></div>
## 20.7 Walidator
atS Dzieci "opcji" dodane recznie do ComboBox w `.otui`. atS Sprzeczne kotwice (`fill` + krawedzie). atS Brak wysokoLci. as dZ `menu-height` zbyt maL'e dla przewijania. as dZ Brak mapowania `onOptionChange` w projekcie.

<div id="ch-20-8"></div>
## 20.8 PrzykL'ady i edgea'cases
Selektor postaci; filtr w narzedziowym MiniWindow; zmiana dostepnoLci (`$disabled`) przy braku danych; placeholder gdy brak wyboru.

---
## 21. ProgressBar
- [21.1 Rola i zakres](#ch-21-1)
- [21.2 WL'aLciwoLci i styl](#ch-21-2)
- [21.3 Geometria](#ch-21-3)
- [21.4 Blueprint OTUI (STRICT)](#ch-21-4)
- [21.5 Presety TS](#ch-21-5)
- [21.6 Walidator](#ch-21-6)
- [21.7 PrzykL'ady i edgea'cases](#ch-21-7)

<div id="ch-21-1"></div>
## 21.1 Rola i zakres
**ProgressBar** prezentuje postep w zakresie. **Nie** posiada dzieci - jeLli potrzebujesz opisu, uLLyj zewnetrznego `Label`.

<div id="ch-21-2"></div>
## 21.2 WL'aLciwoLci i styl
- `minimum: 0`, `maximum: 100`, `value: 0..100`.  
- Warianty skorek: kolor tL'a i wypeL'nienia; opcjonalne "gradienty" (jeLli motyw wspiera).  
- MoLLliwy tryb indeterminate (projektowy) - sygnalizowany animacja po stronie klienta.

<div id="ch-21-3"></div>
## 21.3 Geometria
- Kotwicz w poziomie do rodzica; wysokoLc ~14-18 px.  
- Parzyste marginesy; zachowaj mina'width dla czytelnoLci.

<div id="ch-21-4"></div>
## 21.4 Blueprint OTUI (STRICT)
ProgressBar
  id: progress
  anchors.left: parent.left
  anchors.right: parent.right
  height: 16
  minimum: 0
  maximum: 100
  value: 0
```

<div id="ch-21-5"></div>
## 21.5 Presety TS
export function presetProgressBar(id = 'progress', min = 0, max = 100, value = 0): WidgetNode {
  return {
    base: 'ProgressBar',
    geometry: { id, anchors: { left: 'parent.left', right: 'parent.right' }, height: 16 },
    behavior: { props: { minimum: min, maximum: max, value } }
};
}
```

<div id="ch-21-6"></div>
## 21.6 Walidator
atS Dzieci wewnatrz ProgressBar. atS `value` poza zakresem `minimum..maximum`. as dZ Zbyt maL'a wysokoLc. as dZ Brak kotwic w poziomie (sL'aba czytelnoLc).

<div id="ch-21-7"></div>
## 21.7 PrzykL'ady i edgea'cases
Status w `StaticMainWindow`; pasek L'adowania w panelu z etykieta obok (`Label`). Tryb "nieokreLlony" w overlay statusu.

---
## 22. ScrollBar (Vertical/Horizontal)
- [22.1 Rola i parowanie](#ch-22-1)
- [22.2 WL'aLciwoLci](#ch-22-2)
- [22.3 Geometria i dokowanie](#ch-22-3)
- [22.4 Blueprinty OTUI (STRICT)](#ch-22-4)
- [22.5 Presety TS](#ch-22-5)
- [22.6 Walidator](#ch-22-6)
- [22.7 PrzykL'ady i edgea'cases](#ch-22-7)

<div id="ch-22-1"></div>
## 22.1 Rola i parowanie
**ScrollBar** jest **rodzeL"stwem** przewijanej treLci (lista/Multiline). Parowany poprzez dokowanie i kotwice treLci do krawedzi scrolla.

<div id="ch-22-2"></div>
## 22.2 WL'aLciwoLci
- `step: N` - skok przewijania (px, dostosuj do wysokoLci wiersza/slotu).  
- `pixels-scroll: true|false` - tryb przewijania pikselowego.  
- (Opcj.) `minimum/maximum/value` - gdy scroll sterowany programowo (projektowo).

<div id="ch-22-3"></div>
## 22.3 Geometria i dokowanie
- **Vertical**: `anchors.right/top/bottom: parent`; przewijana treLc: `right: scroll.left`.  
- **Horizontal**: `anchors.left/right/bottom: parent`; przewijana treLc: `bottom: hscroll.top`.  
- SzerokoLc (V) ~12-16 px; wysokoLc (H) ~12-16 px. Parzyste marginesy.

<div id="ch-22-4"></div>
## 22.4 Blueprinty OTUI (STRICT)
**VerticalScrollBar**
VerticalScrollBar
  id: scroll
  anchors.right: parent.right
  anchors.top: parent.top
  anchors.bottom: parent.bottom
  step: 16
  pixels-scroll: true
```

**HorizontalScrollBar**
HorizontalScrollBar
  id: hscroll
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.bottom: parent.bottom
  step: 16
  pixels-scroll: true
```

<div id="ch-22-5"></div>
## 22.5 Presety TS
export function presetVScroll(id = 'scroll', step = 16, pixels = true): WidgetNode {
  return {
    base: 'VerticalScrollBar',
    geometry: { id, anchors: { right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' } },
    behavior: { props: { step, pixelsScroll: pixels } }
};
}

export function presetHScroll(id = 'hscroll', step = 16, pixels = true): WidgetNode {
  return {
    base: 'HorizontalScrollBar',
    geometry: { id, anchors: { left: 'parent.left', right: 'parent.right', bottom: 'parent.bottom' } },
    behavior: { props: { step, pixelsScroll: pixels } }
};
}
```

<div id="ch-22-6"></div>
## 22.6 Walidator
atS ScrollBar jako dziecko listy/Multiline. atS Brak parowania (treLc nie kotwiczy sie do scrolla). atS `step` niedopasowany do rozmiaru wiersza (szarpane przewijanie). as dZ Brak `pixels-scroll` przy drobnym tekLcie.

<div id="ch-22-7"></div>
## 22.7 PrzykL'ady i edgea'cases
Lista z wierszem 18 px a' `step: 18`; edytor tekstu z delikatnym przewijaniem (`pixels-scroll: true`); ukL'ad podwojny (V+H) w panelu z danymi tabelarycznymi.

---
## 23. HorizontalSeparator
- [23.1 Rola i ograniczenia](#ch-23-1)
- [23.2 Geometria i styl](#ch-23-2)
- [23.3 Blueprint OTUI (STRICT)](#ch-23-3)
- [23.4 Preset TS](#ch-23-4)
- [23.5 Walidator](#ch-23-5)
- [23.6 PrzykL'ady i edgea'cases](#ch-23-6)

<div id="ch-23-1"></div>
## 23.1 Rola i ograniczenia
**HorizontalSeparator** to cienka linia dzielaca sekcje. **Nie posiada dzieci** i nie jest interaktywny.

<div id="ch-23-2"></div>
## 23.2 Geometria i styl
- Kotwice: najczeLciej `left/right: parent`, wysokoLc `1` lub `2` px.  
- Marginesy: parzyste `margin-top/bottom` dla rytmu layoutu.  
- Styl: `background-color` (przezroczystoLc mile widziana).

<div id="ch-23-3"></div>
## 23.3 Blueprint OTUI (STRICT)
HorizontalSeparator
  id: sep
  anchors.left: parent.left
  anchors.right: parent.right
  height: 1
  background-color: #ffffff33
```

<div id="ch-23-4"></div>
## 23.4 Preset TS
export function presetHorizontalSeparator(id = 'sep', height = 1): WidgetNode {
  return {
    base: 'HorizontalSeparator',
    geometry: { id, anchors: { left: 'parent.left', right: 'parent.right' }, height },
    style: { backgroundColor: '#ffffff33' }
};
}
```

<div id="ch-23-5"></div>
## 23.5 Walidator
atS Dzieci w separatorze. as dZ WysokoLc > 2 px bez uzasadnienia stylistycznego. as dZ Nieparzyste marginesy.

<div id="ch-23-6"></div>
## 23.6 PrzykL'ady i edgea'cases
Separator pod nagL'owkiem GroupBox; cienka linia w Toolbarze miedzy grupami akcji.

---
## 24. StatusOverlay
- [24.1 Rola i struktura](#ch-24-1)
- [24.2 Geometria i styl](#ch-24-2)
- [24.3 Stany i zdarzenia](#ch-24-3)
- [24.4 Blueprint OTUI (STRICT)](#ch-24-4)
- [24.5 Preset TS](#ch-24-5)
- [24.6 Walidator](#ch-24-6)
- [24.7 PrzykL'ady i edgea'cases](#ch-24-7)

<div id="ch-24-1"></div>
## 24.1 Rola i struktura
**StatusOverlay** to lekka warstwa informacyjna nad treLcia. Typowo: `Label` (komunikat), opcj. `ProgressBar`, opcj. `Button` Cancel.

<div id="ch-24-2"></div>
## 24.2 Geometria i styl
- Overlay kotwiczy sie do caL'ego rodzica: `anchors.fill: parent`.  
- TL'o poL'przezroczyste (np. `#00000055`) lub `alpha`.  
- Kafelek Lrodka (panel) wycentrowany pion/poziom przez `anchors.centerIn: parent` lub rownowaLLne kotwice.

<div id="ch-24-3"></div>
## 24.3 Stany i zdarzenia
- `@onClick` przy Cancel.  
- WidocznoLc sterowana przez kontroler (show/hide).  
- Brak zL'oLLonych dzieci - overlay jest lekki.

<div id="ch-24-4"></div>
## 24.4 Blueprint OTUI (STRICT)
StatusOverlay < UIWidget
  id: overlay
  anchors.fill: parent
  background-color: #00000055

  UIWidget
    id: panel
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    width: 220
    padding: 8
    background-color: #00000099

    Label
      id: msg
      anchors.left: parent.left
      anchors.right: parent.right
      text-wrap: true
      !text: tr('Working...')
      font: verdana-11px-monochrome

    ProgressBar
      id: progress
      anchors.left: parent.left
      anchors.right: parent.right
      anchors.top: msg.bottom
      margin-top: 6
      height: 16

    Button
      id: cancel
      anchors.top: progress.bottom
      anchors.right: parent.right
      margin-top: 6
      width: 64
      !text: tr('Cancel')
```

<div id="ch-24-5"></div>
## 24.5 Preset TS
export function presetStatusOverlay(label = 'Working...'): WidgetNode {
  return {
    base: 'StatusOverlay', extends: 'UIWidget',
    geometry: { id: 'overlay', anchors: { fill: 'parent' } },
    style: { backgroundColor: '#00000055' },
    children: [
      { base: 'UIWidget', geometry: { id: 'panel', anchors: { horizontalCenter: 'parent.horizontalCenter', verticalCenter: 'parent.verticalCenter' }, width: 220, padding: 8 }, style: { backgroundColor: '#00000099' }, children: [
        { base: 'Label', geometry: { id: 'msg', anchors: { left: 'parent.left', right: 'parent.right' } }, style: { textWrap: true, text: label, font: 'verdana-11px-monochrome' } },
        { base: 'ProgressBar', geometry: { id: 'progress', anchors: { left: 'parent.left', right: 'parent.right', top: 'msg.bottom' }, marginTop: 6, height: 16 } },
        { base: 'Button', geometry: { id: 'cancel', anchors: { top: 'progress.bottom', right: 'parent.right' }, marginTop: 6, width: 64 }, style: { text: 'Cancel' } }
]}
]
};
}
```

<div id="ch-24-6"></div>
## 24.6 Walidator
atS Overlay z nadmiarem dzieci (zL'oLLone ukL'ady). atS Brak `tr()` w komunikacie. as dZ Brak kontrastu (czytelnoLc). as dZ Panel bez wyLrodkowania.

<div id="ch-24-7"></div>
## 24.7 PrzykL'ady i edgea'cases
Overlay L'adowania zasobow; tryb indeterminate ProgressBar; anulowanie dL'ugiej operacji.

---
## 25. Macierze dozwolonych dzieci (global)
- [25.1 Tabele macierzowe per komponent i slot](#ch-25-1)
- [25.2 ReguL'y globalne](#ch-25-2)

<div id="ch-25-1"></div>
## 25.1 Tabele macierzowe per komponent i slot
| Parent/Slot | Dopuszczone dzieci | Niedozwolone / Uwagi |
|---|---|---|
| **MainWindow/StaticMainWindow** | elementy panelowe (Label, Button, TextEdit, Multiline, TextList, ComboBox, CheckBox, ProgressBar, VerticalScrollBar, HorizontalSeparator, TabBar, Splitter, UIWidget, Panel) | `*Window` jako dzieci - as- |
| **MiniWindow.titlebar** | Label, Button, UIWidget (ikona) | Scroll, listy, edytory - as- |
| **MiniWindow.content** | elementy panelowe (w tym TextList/Multiline, Panel, Grid, ProgressBar) | `*Window` - as-; Scroll tylko w parze |
| **MiniWindow.footer** | Button, Label | Listy/edytory - as- |
| **ContainerWindow.titlebar** | Button (back/pin/min/close), Label, UIWidget (ikona) | Scroll/listy/edytory - as- |
| **ContainerWindow.content** | SlotWidget/UIWidget, Label, Button, VerticalScrollBar (dock right) | `*Window` - as- |
| **DialogWindow.titlebar** | Label | Scroll/listy/edytory - as- |
| **DialogWindow.content** | Label, TextEdit, Multiline, ComboBox, CheckBox, ProgressBar | `*Window` - as- |
| **DialogWindow.footer** | Button | - |
| **Panel/GroupBox/UIWidget** | elementy panelowe | `*Window` - as- |
| **TabBar** | Button (zakL'adki) | TreLci panelowe w TabBar - as- |
| **TabContent** | elementy panelowe | - |
| **Splitter** | dokL'adnie 2 panele (UIWidget/Panel) | a 2 dzieci - as- |
| **TextList** | wiersze (UIWidget/ListRow) | Scroll jako **sibling** |
| **MultilineTextEdit** | - | Scroll jako **sibling** |
| **ComboBox** | - (menu wewnetrzne) | Reczne "opcje" - as- |
| **ProgressBar** | - | Brak dzieci |
| **HorizontalSeparator** | - | Brak dzieci |
| **StatusOverlay** | Label, ProgressBar, Button (Cancel) | ZL'oLLone ukL'ady - as- |

<div id="ch-25-2"></div>
## 25.2 ReguL'y globalne
- ScrollBar zawsze **sibling** przewijanej treLci.  
- `*Window` nigdy **nie** jest dzieckiem innego okna w slotach treLci.  
- `titlebar/footer` to obszary **bez** list/edytorow/scrolla.  
- Parzyste marginesy i spacing; snapping 2 px.  
- Wymuszone przyciski w oknach: MiniWindow (min/close), Container (back + min/close), Dialog (OK/Cancel w footerze).  
- Wszystkie napisy przez `tr()`; zasoby tylko z `data/`.

---
## 26. Walidacja i autoa'naprawy (global)
- [26.1 BL'edy blokujace](#ch-26-1)
- [26.2 OstrzeLLenia](#ch-26-2)
- [26.3 Autoa'naprawy deterministyczne](#ch-26-3)
- [26.4 Pipeline walidatora](#ch-26-4)

<div id="ch-26-1"></div>
## 26.1 BL'edy blokujace (atS)
- STRICT: komentarze, taby, CRLF/BOM, zL'e wciecia (a 2 sp.), kolejnoLc atrybutow niekanoniczna.  
- Sprzeczne kotwice (`fill` + krawedzie).  
- Niedozwolone dzieci w slotach/parentach.  
- Samotny ScrollBar lub przewijana treLc bez pary i dokowania.  
- Brak wymaganych przyciskow okna (Mini/Container/Dialog).  
- `tr()` pominiete dla staL'ych napisow; zasoby spoza `data/`.

<div id="ch-26-2"></div>
## 26.2 OstrzeLLenia (as dZ)
- Nieparzyste marginesy/spacing.  
- Brak autoa'fit width przy dokowaniu okna.  
- `step` scrolla niepasujacy do wysokoLci wiersza/slotu.  
- Brak skrotow Enter/Escape/strzaL'ek tam, gdzie UX tego wymaga.

<div id="ch-26-3"></div>
## 26.3 Autoa'naprawy deterministyczne
1) Normalizacja koL"cow linii na LF, usuniecie BOM/tabow/trailing spaces.  
2) Wciecia a' 2 sp.  
3) Porzadkowanie atrybutow: **GEOMETRIA a' STYL a' ZACHOWANIE**.  
4) Wstawienie brakujacych slotow (np. `content/footer` w MiniWindow).  
5) Parowanie ScrollBar z lista/Multiline (dokowanie + kotwice).  
6) Usuniecie `width` gdy istnieje `anchors.left/right: parent` (autoa'fit).  
7) Snapping marginesow/spacing do wartoLci parzystych.

<div id="ch-26-4"></div>
## 26.4 Pipeline walidatora
parse a' normalize(STRICT) a' validateStructure(macierze) a' validateAnchors a' validateI18n a' validateResources a' validatePairs(scroll) a' autofix a' rea'serialize a' diff
```
Wynik: `{ errors: [...], warnings: [...], fixes: [...] }` + zaktualizowany dokument.

---
## 27. Parser/Serializer OTUI a' AST (TypeScript)
- [27.1 Tokenizacja i INDENT/DEDENT](#ch-27-1)
- [27.2 KsztaL't AST](#ch-27-2)
- [27.3 Algorytm parsowania](#ch-27-3)
- [27.4 Serializacja i `ensureStrictOtui()`](#ch-27-4)
- [27.5 BL'edy/ostrzeLLenia/pozycje](#ch-27-5)
- [27.6 Testy rounda'trip (goldeny)](#ch-27-6)

<div id="ch-27-1"></div>
## 27.1 Tokenizacja i INDENT/DEDENT
Tokeny: `IDENT`, `NUMBER`, `STRING` (pojedyncze `'...'` dla `!text`), `SYMBOL` (`:`, `<`, `>`, `$`, `@`, `&`), `NEWLINE`, `INDENT`, `DEDENT`. Wciecie = **2 spacje**.

<div id="ch-27-2"></div>
## 27.2 KsztaL't AST
export type AstNode = {
  kind: 'Widget'|'Prop'|'Event'|'State'|'MetaFn';
  name?: string;
  extends?: string;
  props?: Record<string,string>;
  event?: string;
  state?: '$on'|'$!on'|'$focus'|'$checked'|'$disabled'|'$hover'|string;
  metaName?: string;
  metaBody?: string;
  children?: AstNode[];
  loc?: { line: number; col: number };
};
```

<div id="ch-27-3"></div>
## 27.3 Algorytm parsowania
1) Liniowo skanuj, budujac stos INDENT/DEDENT.  
2) Linia `X < Y` a' wezeL' `Widget` z dziedziczeniem.  
3) Linia `key: value` a' `Prop` (wL'aLciwoLci GEOMETRIA/STYL/ZACHOWANIE).  
4) Blok `@on...:` a' `Event`; blok `$...:` a' `State`; blok `&name:` a' `MetaFn`.  
5) DoL'aczaj dzieci wg wciec; zachowuj `loc` do raportow.

<div id="ch-27-4"></div>
## 27.4 Serializacja i `ensureStrictOtui()`
- Emisja w kolejnoLci **GEOMETRIA a' STYL a' ZACHOWANIE**.  
- `style.text` a' `!text: tr('...')`; zdarzenia a' `@on...`; stany a' `$...`.  
- `ensureStrictOtui(text)` usuwa BOM/taby, normalizuje LF, wciecia (2 sp.), atrybuty i kolejnoLc blokow.

<div id="ch-27-5"></div>
## 27.5 BL'edy/ostrzeLLenia/pozycje
Struktura raportu:
export type LintIssue = { kind: 'error'|'warning'; code: string; message: string; loc?: { line: number; col: number } };
```
PrzykL'ady: `E_STRICT_TABS`, `E_SLOT_CHILD_FORBIDDEN`, `E_ANCHORS_CONFLICT`, `E_SCROLL_PAIR_MISSING`, `W_MARGIN_ODD`.

<div id="ch-27-6"></div>
## 27.6 Testy rounda'trip (goldeny)
- Dla **MiniWindow**, **ContainerWindow**, **Dialog**: `parse a' serialize a' parse` i porownanie AST (bez strat).  
- Testy porzadkowania atrybutow, stanow i zdarzeL"; testy autoa'napraw (deterministyczny diff).

---
## 28. Import/Export i rounda'trip (edytor a" plik a" Lua)
- [28.1 Import z `.otui`](#ch-28-1)
- [28.2 Import z blokow w Lua (`@OTUI_BEGIN/END`)](#ch-28-2)
- [28.3 Eksport do `.otui` + aktualizacja bloku w Lua](#ch-28-3)
- [28.4 Runtime: tylko pliki](#ch-28-4)

<div id="ch-28-1"></div>
## 28.1 Import z `.otui`
- Wczytaj plik, `ensureStrictOtui()`, `parseOtui()` a' AST.  
- Walidacja + autoa'naprawy; prezentacja ostrzeLLeL" przed edycja.

<div id="ch-28-2"></div>
## 28.2 Import z blokow w Lua (`@OTUI_BEGIN/END`)
W kodzie Lua przechowuj **czysty STRICT OTUI** w stringu wielowierszowym, a **markery** trzymaj poza stringiem:
-- @OTUI_BEGIN miniwindow
local UI = [[
MiniWindow
  id: miniWindow
  width: 200
]]
-- @OTUI_END miniwindow
```
Edytor odnajduje sekcje po nazwie, wycina **dokL'adnie** zawartoLc stringa i traktuje ja jak `.otui`.

<div id="ch-28-3"></div>
## 28.3 Eksport do `.otui` + aktualizacja bloku w Lua
- Serializuj do pliku `.otui` (kanoniczny zapis).  
- JeLli w Lua istnieje sekcja `@OTUI_BEGIN/END`, **zastap** wyL'acznie Lrodek stringa nowym STRICT OTUI (bez zmiany markerow i otaczajacego kodu).  
- Generuj stub `local win = g_ui.displayUI('file')` do uLLycia w runtime.

<div id="ch-28-4"></div>
## 28.4 Runtime: tylko pliki
W OTClient v8 UI jest L'adowane kanonicznie z plikow: `g_ui.displayUI('...')`. Import/edycja "from string" sL'uLLy **wyL'acznie** edytorowi i utrzymaniu kodu - nie do produkcyjnego L'adowania w kliencie.

---
## 29. Biblioteka presetow (gotowe szablony)
- [29.1 Presety okien](#ch-29-1)
- [29.2 Presety komponentow](#ch-29-2)
- [29.3 Warianty tematyczne](#ch-29-3)
- [29.4 Rejestr presetow i wersjonowanie](#ch-29-4)
- [29.5 Zasady rozszerzania](#ch-29-5)

<div id="ch-29-1"></div>
## 29.1 Presety okien
**Preset: MinimalMiniWindow**
MiniWindow < MainWindow
  id: mini
  anchors.left: parent.left
  anchors.right: parent.right
  height: 160

  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Tool')
      font: verdana-11px-rounded

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 6

    background-color: alpha

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28

    background-color: #00000033
```

**Preset: ContainerLootWindow**
ContainerWindow < MainWindow
  id: loot
  anchors.left: parent.left
  anchors.right: parent.right
  height: 220

  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Loot')
      font: verdana-11px-rounded

    Button
      id: backBtn
      anchors.right: pinBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('<')

    Button
      id: pinBtn
      anchors.right: minimizeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('*')

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: titlebar.bottom
    anchors.bottom: parent.bottom
    padding: 6

    background-color: alpha

    UIWidget
      id: grid
      anchors.left: parent.left
      anchors.top: parent.top
      width: 1
      height: 1

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: parent.bottom
    step: 36
```

**Preset: ConfirmDialog**
DialogWindow < MainWindow
  id: confirm
  width: 300
  height: 140

  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    background-color: #00000066

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Confirm')
      font: verdana-11px-rounded

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 8

    background-color: alpha

    Label
      id: message
      anchors.left: parent.left
      anchors.right: parent.right
      text-wrap: true
      !text: tr('Are you sure?')
      font: verdana-11px-monochrome

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 32

    background-color: #00000033

    Button
      id: okButton
      anchors.right: cancelButton.left
      anchors.bottom: parent.bottom
      width: 72
      margin-right: 8
      !text: tr('Ok')

    Button
      id: cancelButton
      anchors.right: parent.right
      anchors.bottom: parent.bottom
      width: 72
      margin-right: 8
      !text: tr('Cancel')
```

<div id="ch-29-2"></div>
## 29.2 Presety komponentow
**TitlebarTool**
TitlebarWidget < UIWidget
  id: titlebar
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 20

  background-color: #00000066

  Label
    id: title
    anchors.left: parent.left
    anchors.verticalCenter: parent.verticalCenter
    margin-left: 6
    text-auto-resize: true
    !text: tr('Title')
    font: verdana-11px-rounded

  Button
    id: minimizeBtn
    anchors.right: closeBtn.left
    anchors.verticalCenter: parent.verticalCenter
    width: 16
    !text: tr('-')

  Button
    id: closeBtn
    anchors.right: parent.right
    anchors.verticalCenter: parent.verticalCenter
    width: 16
    !text: tr('x')
```

**ToolbarBasic**
ToolbarWidget < UIWidget
  id: toolbar
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 20

  background-color: #00000044

  Button
    id: action1
    anchors.left: parent.left
    anchors.verticalCenter: parent.verticalCenter
    width: 60
    !text: tr('Action')
```

**PanelForm**
Panel
  id: form
  anchors.left: parent.left
  anchors.right: parent.right
  anchors.top: parent.top
  height: 120

  background-color: alpha

  UIWidget
    id: body
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    padding: 6

    background-color: alpha
```

<div id="ch-29-3"></div>
## 29.3 Warianty tematyczne
- **Narzedzie**: tL'a poL'przezroczyste, kompaktowe wysokoLci (20 px titlebar/toolbar), marginesy 6 px.  
- **Kontener**: widoczne przyciski `back/pin`, spacing slotow 4 px, slot 36A-36.  
- **Dialog**: padding 8 px, przyciski 72 px, wysokoLc 32 px w footer.

<div id="ch-29-4"></div>
## 29.4 Rejestr presetow i wersjonowanie
- **Registry (TS)** trzyma wpisy: `id`, `title`, `base`, `version`, `factory()`.  
- Stabilne **sluga'i** presetow (np. `mini/minimal`, `container/loot`, `dialog/confirm`).  
- Zmiany L'amiace a' nowy `version`, poprzedni nadal dostepny.

export type PresetEntry = { id: string; version: string; title: string; factory: () => WidgetNode|WidgetNode[] };
export const PRESETS: PresetEntry[] = [
  { id: 'mini/minimal', version: '1.0.0', title: 'Minimal MiniWindow', factory: presetMiniMinimal },
  { id: 'container/loot', version: '1.0.0', title: 'Container Loot', factory: presetContainerLoot },
  { id: 'dialog/confirm', version: '1.0.0', title: 'Confirm Dialog', factory: presetDialogConfirm }
];
```

<div id="ch-29-5"></div>
## 29.5 Zasady rozszerzania
- Rozszerzaj przez **dziedziczenie** (`X < Y`) lub przez preset TS, nigdy przez ada'hoc dzieci naruszajace macierze.  
- Zachowuj STRICT OTUI przy eksporcie; nie duplikuj semantyki okna w stanach.

---
## 30. Testy wizualne i regresja
- [30.1 Snapshoty 1:1](#ch-30-1)
- [30.2 DPI / font metrics / skalowanie](#ch-30-2)
- [30.3 DostepnoLc (kontrast, czytelnoLc)](#ch-30-3)
- [30.4 Golden diff i tolerancje](#ch-30-4)
- [30.5 Pipeline testow](#ch-30-5)

<div id="ch-30-1"></div>
## 30.1 Snapshoty 1:1
- Generuj obraz referencyjny dla kaLLdego preset/blueprintu po eksporcie `.otui`.  
- Porownuj piksela'poa'pikselu z goldenem; rozbijaj roLLnice na heatmape.

<div id="ch-30-2"></div>
## 30.2 DPI / font metrics / skalowanie
- Testuj na staL'ych DPI (np. 96) oraz wariantach skali (1.0, 1.25, 1.5).  
- Weryfikuj metryki fontu: wysokoLc linii, kerning; nie dopuszczaj driftu miedzy wersjami.

<div id="ch-30-3"></div>
## 30.3 DostepnoLc (kontrast, czytelnoLc)
- Sprawdzaj minimalne kontrasty tekst/tL'o.  
- Minimalne rozmiary hitboxow (aA16A-16).  
- Zawijanie i elipsyzacja dL'ugich tekstow.

<div id="ch-30-4"></div>
## 30.4 Golden diff i tolerancje
- Tolerancja szumu renderera a0.5% pikseli.  
- KaLLda roLLnica > tolerancji wymaga akceptacji lub rollbacku presetow/stylow.

<div id="ch-30-5"></div>
## 30.5 Pipeline testow
for each preset a' serialize(STRICT) a' export .otui a' render snapshot a' compare with golden a' report
```
Raport: lista roLLnic, heatmapy, log walidatora (STRUCT/anchors/macierze).

---
## 31. SL'ownik i indeks
- [31.1 SL'ownik (A-Z)](#ch-31-1)
- [31.2 Indeks rozdziaL'ow](#ch-31-2)

<div id="ch-31-1"></div>
## 31.1 SL'ownik (A-Z)
- **Anchors** - kotwice poL'oLLenia i rozmiaru wzgledem krawedzi/obiektow.  
- **AST** - abstrakcyjne drzewo skL'adniowe reprezentujace OTUI w edytorze.  
- **Blueprint** - kanoniczny szablon OTUI komponentu/okna.  
- **Grid (edytorowy)** - siatka pomocnicza w edytorze, nie istnieje w OTUI.  
- **Layouta'owner** - rodzic definiujacy sloty/obszary i reguL'y dokowania.  
- **Macierz dzieci** - tabela dozwolonych dzieci per parent/slot.  
- **Preset** - gotowy zestaw wezL'ow przygotowanych do uLLycia jako wzorzec.  
- **Rounda'trip** - import a' edycja a' eksport bez utraty semantyki.  
- **Scroll pairing** - reguL'y L'aczenia treLci przewijanej ze ScrollBarem jako rodzeL"stwem.  
- **STRICT OTUI** - format: LF, 2 spacje, brak komentarzy/tabow, kolejnoLc atrybutow.

<div id="ch-31-2"></div>
## 31.2 Indeks rozdziaL'ow
- **Okna**: 5-9  
- **Organizacja**: 10-14  
- **Dane/edycja**: 15-20  
- **WskaLsniki/scroll**: 21-22  
- **Warstwy i separatory**: 23-24  
- **ReguL'y i walidacja**: 25-26  
- **AST/IO**: 27-28  
- **Presety**: 29  
- **Testy**: 30  
- **SL'ownik**: 31

---

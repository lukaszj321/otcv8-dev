# OTClient v8 â€” Specyfikacja UI

---
## 0. Wprowadzenie i zasady
- [0.1 Cel i zakres â€ž1:1â€ť](#ch-0-1)
- [0.2 Terminologia (widget, layoutĂ˘â‚¬â€owner, area/slot, preset, blueprint, AST)](#ch-0-2)
- [0.3 Kryteria jakoÄąâ€şci (deterministyczny roundĂ˘â‚¬â€trip, zgodnoÄąâ€şÄ‡ 1:1)](#ch-0-3)
- [0.4 Workflow: projekt Ă˘â€ â€™ walidacja Ă˘â€ â€™ serializacja Ă˘â€ â€™ eksport Ă˘â€ â€™ import](#ch-0-4)
## 1. Konwencje formatowania i STRICT OTUI
- [1.1 Indent 2 sp., LF, bez BOM, bez tabĂłw/komentarzy](#ch-1-1)
- [1.2 KolejnoÄąâ€şÄ‡ atrybutĂłw: GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE](#ch-1-2)
- [1.3 Teksty i i18n: `!text: tr('...')`, wrap/autoĂ˘â‚¬â€resize/align/offset](#ch-1-3)
- [1.4 Stany: `$on`, `$!on`, `$focus` (kompletnoÄąâ€şÄ‡ blokĂłw)](#ch-1-4)
- [1.5 Zasoby `data/`: fonty, obrazy, kolory (#AARRGGBB/alpha)](#ch-1-5)
## 2. Architektura UI
- [2.1 Pliki `.otui` i Äąâ€šadowanie `g_ui.displayUI('...')`](#ch-2-1)
- [2.2 Tworzenie dynamiczne `g_ui.createWidget('<Typ>', parent)`](#ch-2-2)
- [2.3 Hierarchia i identyfikacja (`id`, `getChildById`) ](#ch-2-3)
- [2.4 Fokus i nawigacja (bindy, `@onSetup`, FocusReason)](#ch-2-4)
## 3. Layout i wÄąâ€šasnoÄąâ€şÄ‡ ukÄąâ€šadu
- [3.1 Zasada â€žlayoutĂ˘â‚¬â€ownerâ€ť (parent vs child)](#ch-3-1)
- [3.2 Anchors, size, margins, padding â€” reguÄąâ€šy i kolizje](#ch-3-2)
- [3.3 Scroll pairing (TextList/Multiline Ă˘â€ â€ť ScrollBar)](#ch-3-3)
- [3.4 AutoĂ˘â‚¬â€fit width (okna w panelach/kontenerach)](#ch-3-4)
## 4. Taksonomia komponentĂłw (przeglÄ…d)
- [4.1 Okna: MainWindow, StaticMainWindow, MiniWindow, ContainerWindow, DialogWindow](#ch-4-1)
- [4.2 Kontenery: Panel, GroupBox, UIWidget, Grid, StatusOverlay](#ch-4-2)
- [4.3 Organizacja: Titlebar, Toolbar, TabBar/TabWidget, Splitter, HorizontalSeparator](#ch-4-3)
- [4.4 Dane/edycja: Label, Button, CheckBox, TextEdit, PasswordTextEdit, MultilineTextEdit, ComboBox, TextList/ListRow](#ch-4-4)
- [4.5 WskaÄąĹźniki: ProgressBar, ScrollBar (Vertical/Horizontal)](#ch-4-5)

---
## 5. MainWindow
- [5.1 Struktura i sloty](#ch-5-1)
- [5.2 Dozwolone dzieci (macierz)](#ch-5-2)
- [5.3 Geometria i styl](#ch-5-3)
- [5.4 Stany i zdarzenia](#ch-5-4)
- [5.5 Blueprint OTUI (kanoniczny)](#ch-5-5)
- [5.6 Mapowanie TS Ă˘â€ â€ť OTUI (serializer)](#ch-5-6)
- [5.7 Walidator (bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia)](#ch-5-7)
- [5.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-5-8)
## 6. StaticMainWindow
- [6.1 Struktura i sloty](#ch-6-1)
- [6.2 Dozwolone dzieci (macierz)](#ch-6-2)
- [6.3 Geometria i styl](#ch-6-3)
- [6.4 Stany i zdarzenia](#ch-6-4)
- [6.5 Blueprint OTUI](#ch-6-5)
- [6.6 TSĂ˘â€ â€ťOTUI](#ch-6-6)
- [6.7 Walidator](#ch-6-7)
- [6.8 PrzykÄąâ€šady](#ch-6-8)
## 7. MiniWindow
- [7.1 Struktura (titlebar/content/footer)](#ch-7-1)
- [7.2 Titlebar: minimize/close, dragĂ˘â‚¬â€area](#ch-7-2)
- [7.3 AutoĂ˘â‚¬â€fit width i docking](#ch-7-3)
- [7.4 Stany i zdarzenia](#ch-7-4)
- [7.5 Blueprint OTUI](#ch-7-5)
- [7.6 TSĂ˘â€ â€ťOTUI](#ch-7-6)
- [7.7 Walidator](#ch-7-7)
- [7.8 PrzykÄąâ€šady](#ch-7-8)
## 8. ContainerWindow
- [8.1 Struktura (titlebar/content)](#ch-8-1)
- [8.2 Titlebar: back/pin/min/close](#ch-8-2)
- [8.3 Content: ItemSlotGrid/slots, DnD](#ch-8-3)
- [8.4 Scroll i overflow](#ch-8-4)
- [8.5 Blueprint OTUI](#ch-8-5)
- [8.6 TSĂ˘â€ â€ťOTUI](#ch-8-6)
- [8.7 Walidator](#ch-8-7)
- [8.8 PrzykÄąâ€šady](#ch-8-8)
## 9. DialogWindow
- [9.1 Struktura](#ch-9-1)
- [9.2 Enter/Escape (OK/Cancel)](#ch-9-2)
- [9.3 ModalnoÄąâ€şÄ‡ i fokus](#ch-9-3)
- [9.4 Blueprint/TS/Walidator](#ch-9-4)

---
## 10. Titlebar
- [10.1 Ikona, tytuÄąâ€š, przyciski](#ch-10-1)
- [10.2 Slot i dozwolone dzieci](#ch-10-2)
- [10.3 DragĂ˘â‚¬â€move, fokus](#ch-10-3)
- [10.4 Blueprint/TS/Walidator](#ch-10-4)
## 11. Toolbar
- [11.1 Grupy akcji i separatory](#ch-11-1)
- [11.2 Toggle/active state](#ch-11-2)
- [11.3 Blueprint/TS/Walidator](#ch-11-3)
## 12. Panel / GroupBox
- [12.1 Sloty treÄąâ€şci, nagÄąâ€šĂłwki, separatory](#ch-12-1)
- [12.2 Dozwolone dzieci i autoĂ˘â‚¬â€fit](#ch-12-2)
- [12.3 Blueprint/TS/Walidator](#ch-12-3)
## 13. TabBar / TabWidget
- [13.1 ZakÄąâ€šadki i kontener treÄąâ€şci](#ch-13-1)
- [13.2 Zdarzenia i aktywacja](#ch-13-2)
- [13.3 Blueprint/TS/Walidator](#ch-13-3)
## 14. Splitter
- [14.1 Dwoje dzieci, minĂ˘â‚¬â€size, pamiÄ™Ä‡ podziaÄąâ€šu](#ch-14-1)
- [14.2 Blueprint/TS/Walidator](#ch-14-2)
## 15. TextList / ListRow
- [15.1 Struktura wiersza (focus/select)](#ch-15-1)
- [15.2 Scroll pairing i kotwice](#ch-15-2)
- [15.3 Blueprinty row + walidator](#ch-15-3)
## 16. Label / UILabel
- [16.1 Wrap/autoĂ˘â‚¬â€resize/font/kolor/offset](#ch-16-1)
- [16.2 Blueprint/TS/Walidator](#ch-16-2)
## 17. Button
- [17.1 Stany `$on/$!on`, ikonografia, minĂ˘â‚¬â€size](#ch-17-1)
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
- [22.1 Docking (right/bottom), step, pixelsĂ˘â‚¬â€scroll](#ch-22-1)
- [22.2 Pairing rules + walidator](#ch-22-2)
## 23. HorizontalSeparator
- [23.1 UÄąÄ˝ycie i ograniczenia](#ch-23-1)
- [23.2 Blueprint](#ch-23-2)
## 24. StatusOverlay
- [24.1 Label + Progress + Cancel](#ch-24-1)
- [24.2 Blueprint/TS/Walidator](#ch-24-2)

---
## 25. Macierze dozwolonych dzieci (global)
- [25.1 Tabele macierzowe per komponent i slot](#ch-25-1)
- [25.2 ReguÄąâ€šy globalne, zakazy, autoĂ˘â‚¬â€naprawy](#ch-25-2)
## 26. Walidacja i autoĂ˘â‚¬â€naprawy (global)
- [26.1 BÄąâ€šÄ™dy blokujÄ…ce (STRICT, anchors, wymagane elementy)](#ch-26-1)
- [26.2 OstrzeÄąÄ˝enia (scroll pairing, Enter/Escape, Min/Close)](#ch-26-2)
- [26.3 AutoĂ˘â‚¬â€naprawy deterministyczne (kolejnoÄąâ€şÄ‡, sloty, scroll, snapping 2px)](#ch-26-3)
## 27. Parser/Serializer OTUI Ă˘â€ â€™ AST (TypeScript)
- [27.1 Specyfikacja tokenĂłw i INDENT/DEDENT](#ch-27-1)
- [27.2 KsztaÄąâ€št AST; API `parseOtui()` i `serializeAst()`](#ch-27-2)
- [27.3 Normalizacja do STRICT (`ensureStrictOtui()`)](#ch-27-3)
- [27.4 Testy â€žroundĂ˘â‚¬â€tripâ€ť (goldeny)](#ch-27-4)
## 28. Import/Export i roundĂ˘â‚¬â€trip (edytor Ă˘â€ â€ť plik Ă˘â€ â€ť Lua)
- [28.1 Import z `.otui` i z blokĂłw `@OTUI_BEGIN/END`](#ch-28-1)
- [28.2 Eksport do `.otui` + odÄąâ€şwieÄąÄ˝enie bloku w Lua](#ch-28-2)
- [28.3 Generatory stubĂłw Lua (`g_ui.displayUI('...')` + kontrolery)](#ch-28-3)
- [28.4 Runtime: brak publicznego `load UI from string` (tylko pliki)](#ch-28-4)
## 29. Biblioteka presetĂłw (gotowe szablony)
- [29.1 Okna (MiniWindow, ContainerWindow, Dialog)](#ch-29-1)
- [29.2 Komponenty (Titlebar, Toolbar, Panel, Ă˘â‚¬Â¦)](#ch-29-2)
- [29.3 Warianty tematyczne (narzÄ™dzie, kontener, dialog)](#ch-29-3)
## 30. Testy wizualne i regresja
- [30.1 Snapshoty i porĂłwnania 1:1](#ch-30-1)
- [30.2 DPI / font metrics / skalowanie](#ch-30-2)
- [30.3 DostÄ™pnoÄąâ€şÄ‡ (kontrasty, czytelnoÄąâ€şÄ‡)](#ch-30-3)
## 31. SÄąâ€šownik i indeks
- [31.1 SÄąâ€šownik atrybutĂłw OTUI (Aâ€“Z)](#ch-31-1)
- [31.2 Indeks komponentĂłw i wÄąâ€šaÄąâ€şciwoÄąâ€şci](#ch-31-2)

---

<!-- Puste kotwice (placeholdery), aby linki dziaÄąâ€šaÄąâ€šy od razu -->
<div id="ch-0-1"></div>
## 0.1 Cel i zakres â€ž1:1â€ť
Ten dokument definiuje **kanoniczne zasady projektowania UI OTClient v8** (OTUI/OTML + Lua) oraz wymagania dla Twojego **edytora TypeScript**: jak skÄąâ€šadaÄ‡ okna i komponenty, aby eksport/import byÄąâ€š **deterministyczny i w 100% zgodny** z klientem. Zawiera: reguÄąâ€šy formatowania (STRICT OTUI), taksonomiÄ™ komponentĂłw, macierze dozwolonych dzieci, blueprinty OTUI, glue Lua, walidacjÄ™, parser/serializer OTUIĂ˘â€ â€™AST i roundĂ˘â‚¬â€trip (edytor Ă˘â€ â€ť plik `.otui` Ă˘â€ â€ť Lua).<div id="ch-0-2"></div>
## 0.2 Terminologia
- **Widget** â€” jednostka UI (np. Label, Button, TextList).
- **LayoutĂ˘â‚¬â€owner** â€” rodzic odpowiadajÄ…cy za obszary/sloty i dokowanie dzieci.
- **Area/slot** â€” semantyczna przestrzeÄąâ€ž dla dzieci (np. `titlebar`, `content`, `footer`).
- **Preset/Blueprint** â€” gotowy wzorzec OTUI danego komponentu/okna.
- **AST** â€” abstrakcyjne drzewo skÄąâ€šadniowe w edytorze (model OTUI w TS).
- **STRICT OTUI** â€” Äąâ€şcisÄąâ€šy format tekstu `.otui`: LF, 2 spacje, brak tabĂłw/komentarzy, staÄąâ€ša kolejnoÄąâ€şÄ‡ atrybutĂłw.
- **RoundĂ˘â‚¬â€trip** â€” pewny obieg: import Ă˘â€ â€™ edycja Ă˘â€ â€™ eksport bez utraty semantyki ani formatowania reguÄąâ€šowego.<div id="ch-0-3"></div>
## 0.3 Kryteria jakoÄąâ€şci
- **ZgodnoÄąâ€şÄ‡ 1:1** z OTClientem (ukÄąâ€šad, stany, eventy, zasoby).
- **Deterministyczny eksport** (ta sama treÄąâ€şÄ‡ wej./wyj. po serializacji, przy zachowaniu STRICT).
- **Stabilne identyfikatory `id`** i spĂłjne nazewnictwo kontrolerĂłw Lua.
- **Lokalizacja**: wszystkie staÄąâ€še teksty przechodzÄ… przez `tr()`.
- **Zasoby**: tylko z `data/` (fonty/obrazy), kolory #AARRGGBB/`alpha`.
- **Brak â€žmagiiâ€ť** w stanach: stany nadpisujÄ… styl, nie geometriÄ™.<div id="ch-0-4"></div>
## 0.4 Workflow
1) **Projekt** w edytorze (drag&drop presetĂłw; macierze pilnujÄ… dozwolonych dzieci).  
2) **Walidacja** (STRICT, anchors, wymagane elementy).  
3) **Serializacja** do `.otui` (kolejnoÄąâ€şÄ‡ GEOMETRIAĂ˘â€ â€™STYLĂ˘â€ â€™ZACHOWANIE).  
4) **Eksport**: zapis `.otui` + generator stubĂłw Lua (`g_ui.displayUI('...')`).  
5) **Import**: z plikĂłw `.otui` lub blokĂłw Lua oznaczonych `@OTUI_BEGIN/END`.  
6) **RoundĂ˘â‚¬â€trip**: zmiany w edytorze odzwierciedlone w pliku i opcjonalnym bloku Lua.
<div id="ch-1-1"></div>
## 1.1 Indent i STRICT
- **LF**, bez BOM; **spacje** (bez tabĂłw); **brak trailing spaces**.  
- **WciÄ™cia = 2 spacje** (mnoÄąÄ˝niki).  
- **Zero komentarzy** w treÄąâ€şci OTUI.  
- Dozwolone znaki: Äąâ€šagodne ASCII + `#` (wyÄąâ€šÄ…cznie w kolorach), `-_:./<>()` itp. WartoÄąâ€şci tekstowe w `!text` w pojedynczych cudzysÄąâ€šowach.

PrzykÄąâ€šad minimalnego bloku zgodnego ze STRICT:
`$fenceInfo
Label
  id: info
  anchors.left: parent.left
  anchors.right: parent.right
  text-wrap: true
  !text: tr('Information')
  font: verdana-11px-monochrome
```

<div id="ch-1-2"></div>
## 1.2 KolejnoÄąâ€şÄ‡ atrybutĂłw
**GEOMETRIA** (najpierw): `id`, `size`/`width`/`height`, `anchors.*` (najpierw `fill`, potem krawÄ™dzie), `margin-*`, `padding`.  
**STYL**: `background-color`, `font`, `color`, `image-*`, `text-*` (`align`, `wrap`, `auto-resize`, `offset`), `!text: tr('...')`.  
**ZACHOWANIE**: `&metaFn`, `@on...` (Enter/Escape/Click/Setup/...), stany `$on/$!on/$focus`.

> Serializator **musi** zawsze emitowaÄ‡ w tej kolejnoÄąâ€şci.<div id="ch-1-3"></div>
## 1.3 Teksty i i18n
- KaÄąÄ˝dy staÄąâ€šy tekst: `!text: tr('...')`.  
- Escaping `'` Ă˘â€ â€™ `\'` wewnÄ…trz `tr('...')`.  
- `text-wrap`/`text-auto-resize`/`text-align`/`text-offset` sterujÄ… renderem.  
- Nie umieszczaj surowych napisĂłw poza `!text` (rĂłwnieÄąÄ˝ w stanach).<div id="ch-1-4"></div>
## 1.4 Stany
- `$on` / `$!on` â€” przeÄąâ€šÄ…czane `widget:setOn(true/false)`.  
- `$focus` â€” aktywne przy fokusie klawiatury.  
- **Zalecenie**: stany modyfikujÄ… **styl** (kolory, `!text`, obraz), **nie** geometriÄ™ (anchors/size).  

PrzykÄąâ€šad:
`$fenceInfo
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
- **Fonty**: uÄąÄ˝ywaj nazw z `data/fonts/` (np. `verdana-11px-monochrome`, `verdana-11px-rounded`, `terminus-14px-bold`).  
- **Obrazy**: Äąâ€şcieÄąÄ˝ki `/images/...`, opcje `image-smooth`, `image-fixed-ratio`.  
- **Kolory**: `#AARRGGBB` lub `alpha`.  
- Walidator blokuje Äąâ€şcieÄąÄ˝ki spoza `data/`.
<div id="ch-2-1"></div>
## 2.1 Pliki `.otui` i Äąâ€šadowanie
- **Kanonicznie** UI Äąâ€šaduje siÄ™ z pliku: `local win = g_ui.displayUI('nazwa_pliku')`.  
- Nazwa w `displayUI` odpowiada plikowi `.otui` w module.  
- Brak publicznego API â€žload UI from stringâ€ť â€” w runtime uÄąÄ˝ywaj plikĂłw.<div id="ch-2-2"></div>
## 2.2 Tworzenie dynamiczne
`$fenceInfo
local parent = rootWidget
local row = g_ui.createWidget('UIWidget', parent)
row:setId('row1')
local name = g_ui.createWidget('Label', row)
name:setText(tr('Name'))
```
- Tworzenie dzieci w Lua jest dozwolone, ale **eksport** z edytora powinien odtwarzaÄ‡ ukÄąâ€šad w `.otui` (statyczny szkielet), a dynamikÄ™ zostawiÄ‡ skryptom.<div id="ch-2-3"></div>
## 2.3 Hierarchia i identyfikacja
- `id` unikalne w ramach rodzica.  
- DostÄ™p w Lua: `parent:getChildById('...')`, wyszukiwanie gÄąâ€šÄ™bokie: `rootWidget:recursiveGetChildById('...')`.  
- WidocznoÄąâ€şÄ‡: `widget:isVisible()`, `widget:setVisible(true/false)`; `:show()/:hide()`.<div id="ch-2-4"></div>
## 2.4 Fokus i nawigacja
- Bindy w `@onSetup` lub Lua: `g_keyboard.bindKeyPress('Up', fn, scope)`.  
- Fokus: `widget:focus()`, powody fokusowania (FocusReason) wpÄąâ€šywajÄ… na zachowanie.  
- Listy: `focusNextChild/PreviousChild`, zapewnij `ensureChildVisible` przy przewijaniu.
<div id="ch-3-1"></div>
## 3.1 Zasada â€žlayoutĂ˘â‚¬â€ownerâ€ť
- **Parent** definiuje sloty i reguÄąâ€šy dokowania (anchors, padding, marginesy).  
- **Child** ustawia swoje `anchors.*` wzglÄ™dem parenta/sÄ…siadĂłw.  
- ScrollBar naleÄąÄ˝y do parenta (kontenera), ale jest **sparowany** z przewijanym dzieckiem.<div id="ch-3-2"></div>
## 3.2 Anchors, size, margins, kolizje
- `anchors.fill: parent` **nie** Äąâ€šÄ…cz z jednoczesnym `top/bottom/left/right`.  
- JeÄąâ€şli okno jest dokowane w panelu: ustaw `anchors.left/right: parent` i usuÄąâ€ž `width` (autoĂ˘â‚¬â€fit).  
- Marginesy `margin-*` i `padding` determinujÄ… odstÄ™py â€” trzymaj parzyste wartoÄąâ€şci (snapping 2 px).<div id="ch-3-3"></div>
## 3.3 Scroll pairing
- `TextList`/`MultilineTextEdit` Ă˘â€ˇâ€ž **`VerticalScrollBar`** jako **sibling**:  
  - ScrollBar: `anchors.right/top/bottom: parent`.  
  - Lista/tekst: `anchors.right: scroll.left`.  
- `HorizontalScrollBar` dokowany na dole; treÄąâ€şÄ‡: `anchors.bottom: hscroll.top`.  
- Samotny ScrollBar Ă˘â€ â€™ bÄąâ€šÄ…d walidacji.<div id="ch-3-4"></div>
## 3.4 AutoĂ˘â‚¬â€fit width (dokowane okna)
- Dla `MiniWindow`/`DialogWindow` w panelach: domyÄąâ€şlnie **rozciÄ…gaj w poziomie** (`anchors.left/right: parent`) i zarzÄ…dzaj odstÄ™pami przez `margin-*`.  
- Edytor przy eksporcie **autoĂ˘â‚¬â€naprawia**: usuwa `width`, gdy ustawiono `left/right`.
<div id="ch-4-1"></div>
## 4.1 Okna (WindowĂ˘â‚¬â€class)
**Cel**: najwyÄąÄ˝sze elementy kompozycji; zapewniajÄ… ramÄ™, titlebar, focus i skrĂłty.

- **MainWindow**  
  *Rola*: gÄąâ€šĂłwne okno moduÄąâ€šu/sceny.  
  *Sloty*: brak nazwanych slotĂłw â€” treÄąâ€şÄ‡ bezpoÄąâ€şrednio w root.  
  *Typowe*: peÄąâ€šnoekran/duÄąÄ˝e panele, dopuszcza wszystkie â€žpaneloweâ€ť dzieci.  
  *Zakazy*: oknaĂ˘â‚¬â€dzieci (inne Main/StaticMain) jako potomkowie.

- **StaticMainWindow**  
  *Rola*: jak MainWindow, ale **bez dragĂ˘â‚¬â€move** (statyczne tÄąâ€šo/ekrany).  
  *UÄąÄ˝ycie*: ekrany logowania, waiting list.

- **MiniWindow**  
  *Rola*: moduÄąâ€šowe okno narzÄ™dziowe.  
  *Sloty*: `titlebar`, `content`, `footer`.  
  *Przyciski*: **minimize**, **close** (opcjonalnie **back/pin**).  
  *AutoĂ˘â‚¬â€fit*: domyÄąâ€şlnie rozciÄ…ga siÄ™ na szerokoÄąâ€şÄ‡ rodzica w panelu.

- **ContainerWindow**  
  *Rola*: przeglÄ…danie zawartoÄąâ€şci (sloty/items).  
  *Sloty*: `titlebar`, `content`.  
  *Przyciski*: **back**, **pin/lock**, **minimize**, **close**.  
  *TreÄąâ€şÄ‡*: `ItemSlotGrid`/sloty; DnD; scroll przy overflow.

- **DialogWindow**  
  *Rola*: potwierdzenia/prompt.  
  *SkrĂłty*: `@onEnter` (OK), `@onEscape` (Cancel).  
  *Sloty*: typowo tytuÄąâ€š + treÄąâ€şÄ‡ + przyciski OK/Cancel.<div id="ch-4-2"></div>
## 4.2 Kontenery (ContentĂ˘â‚¬â€class)
**Cel**: organizacja i grupowanie treÄąâ€şci.

- **Panel**  
  Lekki kontener na treÄąâ€şÄ‡. Dopuszcza wiÄ™kszoÄąâ€şÄ‡ elementĂłw panelowych; uÄąÄ˝ywany jako sekcja lub obszar roboczy.

- **GroupBox**  
  Panel z nagÄąâ€šĂłwkiem (etykietÄ…) i ramkÄ…/separatorem. Dla formularzy/pogrupowanych opcji.

- **UIWidget**  
  Bazowy kontener/â€žkafelekâ€ť. MoÄąÄ˝e mieÄ‡ tÄąâ€šo (`image-*`, `background-color`), sÄąâ€šuÄąÄ˝y teÄąÄ˝ jako wiersze list.

- **Grid (edytorowy)**  
  Artefakt **tylko w edytorze** do ukÄąâ€šadania na siatce (snapping, gapy). **Nie** jest typem OTUI â€” przy eksporcie mapuje siÄ™ na anchors/marginesy prawdziwych widgetĂłw.

- **StatusOverlay**  
  Lekka warstwa informacyjna (Label/Progress/Cancel) dokowana nad treÄąâ€şciÄ…. Bez zÄąâ€šoÄąÄ˝onych dzieci.<div id="ch-4-3"></div>
## 4.3 Organizacja i nawigacja
**Cel**: nawigowanie, przeÄąâ€šÄ…czanie kontekstu, dzielenie przestrzeni.

- **Titlebar**  
  Slot nagÄąâ€šĂłwka okna: `Label` (tytuÄąâ€š), przyciski (**min/close/back/pin**), ewentualna ikona. MoÄąÄ˝e stanowiÄ‡ **dragĂ˘â‚¬â€area**. Zakaz list, edytorĂłw, scrollbarĂłw.

- **Toolbar**  
  Pasek akcji (grupy `Button`, separatory). Stany toggle, skrĂłty klawiszowe.

- **TabBar / TabWidget**  
  TabBar zawiera **zakÄąâ€šadki** (przyciski), a **kontent zakÄąâ€šadki** znajduje siÄ™ w osobnym kontenerze obok/poniÄąÄ˝ej. Nie wkÄąâ€šadamy treÄąâ€şci do TabBar.

- **Splitter**  
  Dzieli przestrzeÄąâ€ž na **dwa** panele; wymagane `min-size` dzieci; pamiÄ™tanie podziaÄąâ€šu mile widziane.

- **HorizontalSeparator**  
  Linie/separatory sekcji. Element wizualny â€” **bez dzieci**.

<div id="ch-4-4"></div>
## 4.4 Dane i edycja (Inputs/Lists)
**Cel**: prezentacja i wprowadzanie danych.

- **Label / UILabel**  
  Tekst z `!text: tr('...')`, `font`, `color`, `text-wrap`, `text-auto-resize`, `text-align`, `text-offset`.

- **Button**  
  Akcje; `@onClick`; stany `$on/$!on` (np. toggle). Minimalne wymiary zalecane Ă˘â€°Ä„16Ä‚â€”16.

- **CheckBox**  
  PrzeÄąâ€šÄ…cznik bool; fokus i interakcja klawiaturÄ…. CzÄ™sto obok napisu (Label) w tym samym kontenerze.

- **TextEdit / PasswordTextEdit / MultilineTextEdit**  
  Pola tekstowe; `Multiline` wymaga pary ze **ScrollBar** (sibling, dock right/bottom).

- **ComboBox**  
  Selektor opcji; `menu-height`, `menu-scroll-step`, `@onOptionChange`. Pozycje menu wewnÄ™trzne (bez manualnych dzieci).

- **TextList / ListRow**  
  Lista przewijana; wiersze jako `UIWidget`/custom row; fokus/zaznaczenie; para z **VerticalScrollBar** (sibling).

  <div id="ch-4-5"></div>
## 4.5 WskaÄąĹźniki i przewijanie
- **ProgressBar**  
  Pasek postÄ™pu; zakres i styl; **bez dzieci**. Opisy stanu (Label) obok.

- **ScrollBar (Vertical/Horizontal)**  
  `step`, `pixels-scroll`; **sibling** przewijanej treÄąâ€şci. Dock: Vertical Ă˘â€ â€™ **right**, Horizontal Ă˘â€ â€™ **bottom**.  
  **Pairing rules**: lista/tekst kotwiczy `right: scroll.left` (dla V) lub `bottom: hscroll.top` (dla H). Samotny ScrollBar Ă˘â€ â€™ bÄąâ€šÄ…d.

---

> **Uwaga**: SzczegĂłÄąâ€šowe macierze dozwolonych dzieci na poziomie kaÄąÄ˝dego komponentu znajdujÄ… siÄ™ w rozdziale **25** i sÄ… egzekwowane przez walidator podczas eksportu.
<div id="ch-5-1"></div>
## 5.1 Struktura i sloty
**MainWindow** jest najwyÄąÄ˝szym kontenerem okna roboczego moduÄąâ€šu/sceny. Nie definiuje nazwanych slotĂłw (jak `titlebar/content/footer`) â€” treÄąâ€şÄ‡ umieszczasz bezpoÄąâ€şrednio w root lub w wydzielonych `UIWidget`/`Panel`.

**Zalecany podziaÄąâ€š logiczny (nieobowiÄ…zkowy):**
- `header` (opcjonalny pasek tytuÄąâ€šu/toolbar jako `UIWidget`),
- `content` (gÄąâ€šĂłwna przestrzeÄąâ€ž pracy),
- `footer` (status/akcje). 
To **nazwa wÄąâ€šasna** dzieci, nie formalny â€žslotâ€ť klasy â€” pomaga w edytorze, w walidacji i przy presetach.<div id="ch-5-2"></div>
## 5.2 Dozwolone dzieci (macierz)
| Parent: `MainWindow` | Dopuszczone dzieci | Niedozwolone / uwagi |
|---|---|---|
| root | `UIWidget`, `Panel`, `Label`, `Button`, `TextEdit`, `PasswordTextEdit`, `MultilineTextEdit`, `TextList`, `ComboBox`, `CheckBox`, `ProgressBar`, `VerticalScrollBar`, `HorizontalSeparator`, `TabBar`, `Splitter` | Inne okna (`MainWindow/StaticMainWindow/MiniWindow/ContainerWindow/DialogWindow`) â€” Ă˘Ĺ›â€“ |
| `header` (jeÄąâ€şli wydzielisz) | `Label`, `Button`, `Toolbar`, `UIWidget` (ikona) | Scroll/edytory/listy â€” Ă˘Ĺ›â€“ |
| `content` | wszystkie elementy â€žpaneloweâ€ť (lista powyÄąÄ˝ej) | oknaĂ˘â‚¬â€dzieci â€” Ă˘Ĺ›â€“ |
| `footer` | `Button`, `Label`, `ProgressBar` | listy/edytory â€” Ă˘Ĺ›â€“ |

**Scroll pairing:** jeÄąâ€şli w `content` dodasz `TextList`/`MultilineTextEdit`, dockuj **VerticalScrollBar** po prawej i kotwicz treÄąâ€şÄ‡ do `scroll.left`.<div id="ch-5-3"></div>
## 5.3 Geometria i styl (GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE)
- **Rozmiar**: `size: W H` lub kotwice wzglÄ™dem rodzica (zalecane w narzÄ™dziach: `anchors.left/right: parent` + wysokoÄąâ€şÄ‡/marginesy).
- **Kotwice**: unikaj Äąâ€šÄ…czenia `anchors.fill: parent` z rÄ™cznymi `top/bottom/left/right`. 
- **Marginesy/padding**: parzyste wartoÄąâ€şci (snapping 2 px) dla spĂłjnoÄąâ€şci.
- **TÄąâ€šo**: `background-color` lub `image-source` (np. tÄąâ€šo ekranu); `image-smooth`, `image-fixed-ratio` w razie potrzeby.
- **Teksty**: wyÄąâ€šÄ…cznie `!text: tr('...')` (STRICT). 
- **Fonty/obrazy**: tylko z `data/`.

> **AutoĂ˘â‚¬â€fit width**: osadzone w panelu `MainWindow` powinno domyÄąâ€şlnie rozciÄ…gaÄ‡ siÄ™ na szerokoÄąâ€şÄ‡ rodzica (edytor moÄąÄ˝e automatycznie usuwaÄ‡ `width`).<div id="ch-5-4"></div>
## 5.4 Stany i zdarzenia
- **Zdarzenia okienne**: `@onEnter` (OK/Apply), `@onEscape` (Cancel/Close), `@onSetup` (bindy klawiszy). 
- **Stany**: `MainWindow` z reguÄąâ€šy nie uÄąÄ˝ywa `$on/$!on` na sobie; stosuj na przyciskach/wierszach listy.
- **Fokus i nawigacja**: w `@onSetup` zbinduj strzaÄąâ€ški/PageUp/PageDown dla list, Enter/Escape dla akcji.
- **Zamykanie**: implementuj w controllerze (Lua), a w `.otui` tylko wiÄ…ÄąÄ˝ `@onEscape`/przyciski.<div id="ch-5-5"></div>
## 5.5 Blueprint OTUI (kanoniczny)
`$fenceInfo
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
# HEADER (opcjonalny pasek tytuÄąâ€šu/toolbar)
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
- WciÄ™cia **2 spacje**, kolejnoÄąâ€şÄ‡ sekcji zachowana (STRICT). 
- Teksty przez `tr()`; zasoby wyÄąâ€šÄ…cznie z `data/`.<div id="ch-5-6"></div>
## 5.6 Mapowanie TS Ă˘â€ â€ť OTUI (serializer)
**Minimalny preset w edytorze (TS):**
`$fenceInfo
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
**Serializer** musi emitowaÄ‡: GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE, `style.text` Ă˘â€ â€™ `!text: tr('...')`, `events` Ă˘â€ â€™ `@on...`, stany Ă˘â€ â€™ `$...`.

**Sanityzacja** przed zapisem: `ensureStrictOtui()` (LF, 2 sp., brak komentarzy/tabĂłw/trailing spaces).<div id="ch-5-7"></div>
## 5.7 Walidator (bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia)
**BlokujÄ…ce (Ă˘ĹĄĹš):**
- Dziecko typu okno (`*Window`) wewnÄ…trz `MainWindow`.
- Sprzeczne kotwice (`fill` + `top/bottom/left/right`).
- `TextList`/`MultilineTextEdit` bez pary **VerticalScrollBar** (gdy overflow) lub bÄąâ€šÄ™dne kotwice pary.
- Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeÄąÄ˝enia (Ă˘ĹˇÂ ÄŹÂ¸Ĺą):**
- Brak `@onEnter/@onEscape` przy oknie z przyciskami OK/Cancel.
- Brak `header`/`footer` przy zÄąâ€šoÄąÄ˝onych ukÄąâ€šadach (zalecenie porzÄ…dkowe). 
- Nieparzyste marginesy (odstÄ™p od siatki 2 px).<div id="ch-5-8"></div>
## 5.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
- **Fullscreen tÄąâ€šo**: zamiast narzucaÄ‡ `size`, uÄąÄ˝yj `anchors.fill: parent` i obraz tÄąâ€ša z `image-fixed-ratio: true` (bez Äąâ€šÄ…czenia z rÄ™cznymi kotwicami). 
- **Lista bez scrolla**: jeÄąâ€şli wiesz, ÄąÄ˝e elementĂłw jest maÄąâ€šo â€” dopuszczalne, ale walidator zasugeruje dodanie scrolla przy overflow. 
- **Shortcuty**: w `@onSetup` zbinduj strzaÄąâ€ški, PageUp/Down do nawigacji po liÄąâ€şcie; Enter/Escape do akcji. 
- **Zamykanie okna**: mapuj `@onEscape` na `MainController.onCancel()` â€” sam kontroler decyduje o `:hide()`/sprzÄ…taniu. 
- **Nadpisywanie geometrii w stanach**: unikaj modyfikowania `anchors/size` wewnÄ…trz `$on/$!on/$focus` â€” trzymaj stany stylistyczne (kolor/tekst).
<div id="ch-6-1"></div>
## 6.1 Struktura i sloty
**StaticMainWindow** to gÄąâ€šĂłwne okno **statyczne** (bez dragĂ˘â‚¬â€move), stosowane m.in. dla ekranĂłw logowania, komunikatĂłw, list oczekiwania. Nie posiada formalnych slotĂłw jak `titlebar/content/footer`, ale zalecamy logiczny podziaÄąâ€š na: `header`, `content`, `footer` (jako `UIWidget`).

- **header** (opcjonalny): pasek tytuÄąâ€šu/toolbar (Label/Buttons).  
- **content**: gÄąâ€šĂłwna przestrzeÄąâ€ž treÄąâ€şci (teksty, listy, formularze, progress).  
- **footer**: akcje (OK/Cancel) lub status.

StaticMainWindow nie powinno mieÄ‡ **innych okien** jako dzieci.<div id="ch-6-2"></div>
## 6.2 Dozwolone dzieci (macierz)
| Parent: `StaticMainWindow` | Dopuszczone dzieci | Niedozwolone / uwagi |
|---|---|---|
| root | `UIWidget`, `Panel`, `Label`, `Button`, `TextEdit`, `PasswordTextEdit`, `MultilineTextEdit`, `TextList`, `ComboBox`, `CheckBox`, `ProgressBar`, `VerticalScrollBar`, `HorizontalSeparator`, `TabBar`, `Splitter` | Inne okna (`*Window`) â€” Ă˘Ĺ›â€“ |
| `header` | `Label`, `Button`, `Toolbar`, `UIWidget` (ikona) | Scroll/edytory/listy â€” Ă˘Ĺ›â€“ |
| `content` | wszystkie elementy panelowe z wiersza root | `*Window` â€” Ă˘Ĺ›â€“; `ScrollBar` tylko jako para do list/tekstĂłw |
| `footer` | `Button`, `Label`, `ProgressBar` | listy/edytory â€” Ă˘Ĺ›â€“ |

**Scroll pairing**: przy `TextList`/`MultilineTextEdit` dodaj **VerticalScrollBar** (dok po prawej), a treÄąâ€şÄ‡ kotwicz do `scroll.left`.<div id="ch-6-3"></div>
## 6.3 Geometria i styl
- **Rozmiar/pozycja**: `size: W H` lub anchors; w panelach Ă˘â€ â€™ autoĂ˘â‚¬â€fit szerokoÄąâ€şci (`anchors.left/right: parent`, bez `width`).
- **Kotwice**: nie Äąâ€šÄ…cz `anchors.fill: parent` z rÄ™cznymi `top/bottom/left/right`.
- **Marginesy/padding**: parzyste wartoÄąâ€şci (snapping 2 px).
- **TÄąâ€šo**: `background-color` albo `image-source` (np. ekran powitalny) + `image-smooth/fixed-ratio` w razie potrzeby.
- **Teksty**: zawsze `!text: tr('...')` (STRICT). Zasoby tylko z `data/`.<div id="ch-6-4"></div>
## 6.4 Stany i zdarzenia
- **Zdarzenia**: `@onEnter` (OK/Continue), `@onEscape` (Cancel/Back), `@onSetup` (bindy, np. Enter/Escape/strzaÄąâ€ški).
- **Stany**: zwykle na **dzieciach** (Button/ListRow), nie na samym `StaticMainWindow`.
- **Fokus**: zapewnij fokus pierwszego sensownego dziecka; nawigacja klawiaturÄ… w `@onSetup`.<div id="ch-6-5"></div>
## 6.5 Blueprint OTUI (kanoniczny)
`$fenceInfo
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

**Uwaga**: blueprint jest **STRICT** (brak komentarzy), wciÄ™cia = 2 sp., kolejnoÄąâ€şÄ‡ sekcji zachowana.<div id="ch-6-6"></div>
## 6.6 Mapowanie TS Ă˘â€ â€ť OTUI (serializer)
**Preset (TS)**
`$fenceInfo
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
**Serializer**: identyczne reguÄąâ€šy jak dla MainWindow â€” GEOMETRIAĂ˘â€ â€™STYLĂ˘â€ â€™ZACHOWANIE, `text`Ă˘â€ â€™`!text: tr(...)`, `events`Ă˘â€ â€™`@on...`, stanyĂ˘â€ â€™`$...`. **Sanityzacja**: `ensureStrictOtui()` przed zapisem.<div id="ch-6-7"></div>
## 6.7 Walidator (bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia)
**BlokujÄ…ce (Ă˘ĹĄĹš):**
- Dziecko typu okno (`*Window`) wewnÄ…trz `StaticMainWindow`.
- ScrollBar w `header`/`footer`.
- Sprzeczne kotwice (`fill` + `top/bottom/left/right`).
- `TextList`/`MultilineTextEdit` bez pary ScrollBar (przy overflow) lub bÄąâ€šÄ™dne kotwice pary.
- Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeÄąÄ˝enia (Ă˘ĹˇÂ ÄŹÂ¸Ĺą):**
- Brak `@onEnter/@onEscape` w ekranie wymagajÄ…cym akcji (OK/Cancel).
- Brak `header`/`footer` przy zÄąâ€šoÄąÄ˝onych ukÄąâ€šadach. 
- Nieparzyste marginesy (snapping 2 px).<div id="ch-6-8"></div>
## 6.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
- **Ekran oczekiwania**: `Label` (wrap) + `ProgressBar`; `Cancel` w `footer`; brak list â€” ScrollBar opcjonalny.  
- **MOTD / dÄąâ€šugi komunikat**: `MultilineTextEdit` + **VerticalScrollBar**; `@onEnter` = Continue, `@onEscape` = Back.  
- **TÄąâ€šo peÄąâ€šnoekranowe**: `image-source` + `image-fixed-ratio`; zakotwicz `anchors.fill: parent` (bez mieszania z krawÄ™dziami).  
- **Fokus**: ustaw na pierwszy przycisk/edytor; zapewnij strzaÄąâ€ški/Enter/Escape w `@onSetup`.
<div id="ch-7-1"></div>
## 7.1 Struktura (titlebar/content/footer)
**MiniWindow** to lekkie, moduÄąâ€šowe okno narzÄ™dziowe. SkÄąâ€šada siÄ™ z trzech logicznych obszarĂłw:
- **`titlebar`** â€” nagÄąâ€šĂłwek z tytuÄąâ€šem i przyciskami (wymagane: **minimize** i **close**; opcjonalne: **back**, **pin**).
- **`content`** â€” gÄąâ€šĂłwna przestrzeÄąâ€ž robocza (formulare, listy, panele).
- **`footer`** â€” przyciski akcji (OK/Cancel/Apply) lub status.

**Zakazy**: w `titlebar/footer` nie umieszczaj `ScrollBar`, list ani edytorĂłw; w `content` nie osadzaj innych okien (`*Window`).<div id="ch-7-2"></div>
## 7.2 Titlebar: minimize/close, dragĂ˘â‚¬â€area
- **Minimize** zwija/rozwija `content` i `footer` (zmiana widocznoÄąâ€şci/wysokoÄąâ€şci); stan moÄąÄ˝e byÄ‡ odzwierciedlany na przycisku (np. `!text: tr('-')`/`!text: tr('+')`).
- **Close** wywoÄąâ€šuje akcjÄ™ zamkniÄ™cia (ukrycie/usuniÄ™cie okna przez kontroler Lua).
- **Back/Pin** (opcjonalnie) â€” stosowane w wariantach kontenerowych/narzÄ™dziowych.
- **DragĂ˘â‚¬â€area**: `titlebar` moÄąÄ˝e peÄąâ€šniÄ‡ obszar przeciÄ…gania (obsÄąâ€šuga po stronie klienta/kontrolera).

**Dozwolone dzieci `titlebar`**: `Label` (tytuÄąâ€š), `Button` (min/close/back/pin), `UIWidget` (ikona).<div id="ch-7-3"></div>
## 7.3 AutoĂ˘â‚¬â€fit width i docking
- Gdy `MiniWindow` jest osadzony w panelu/kontenerze, **domyÄąâ€şlnie** rozciÄ…ga siÄ™ na szerokoÄąâ€şÄ‡ rodzica: ustaw `anchors.left/right: parent` i usuÄąâ€ž `width`.
- OdstÄ™py od krawÄ™dzi zapewnij przez `margin-*` (parzyste wartoÄąâ€şci â€” snapping 2 px).
- Unikaj Äąâ€šÄ…czenia `anchors.fill: parent` z rÄ™cznymi kotwicami (`top/bottom/left/right`).<div id="ch-7-4"></div>
## 7.4 Stany i zdarzenia
- **Zdarzenia**: `@onEnter` (OK/Apply), `@onEscape` (Cancel/Close), `@onClick` (przyciski titlebara), `@onSetup` (bindy klawiatury).
- **Minimize toggle**: kontroler Lua przeÄąâ€šÄ…cza widocznoÄąâ€şÄ‡ `content` i `footer`.
- **Stany `$on/$!on`**: stosuj gÄąâ€šĂłwnie do przyciskĂłw (np. podÄąâ€şwietlenie aktywnoÄąâ€şci), nie do geometrii okna.
- **Fokus**: po otwarciu ustaw fokus na pierwszym sensownym dziecku (`content`).<div id="ch-7-5"></div>
## 7.5 Blueprint OTUI (kanoniczny, STRICT)
`$fenceInfo
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
## 7.6 Mapowanie TS Ă˘â€ â€ť OTUI (serializer)
**Preset (TS)**
`$fenceInfo
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
**Serializer**: emituj GEOMETRIAĂ˘â€ â€™STYLĂ˘â€ â€™ZACHOWANIE; `style.text`Ă˘â€ â€™`!text: tr('...')`; `events`Ă˘â€ â€™`@on...`; stanyĂ˘â€ â€™`$...`. **Sanityzacja**: `ensureStrictOtui()` przed zapisem.<div id="ch-7-7"></div>
## 7.7 Walidator (bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia)
**BlokujÄ…ce (Ă˘ĹĄĹš):**
- Brak przyciskĂłw **minimize** i **close** w `titlebar`.
- Niedozwolone dzieci w `titlebar/footer` (scroll, listy, edytory).
- `content` zawiera inne okno (`*Window`).
- Sprzeczne kotwice (`fill` + krawÄ™dzie). 
- Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeÄąÄ˝enia (Ă˘ĹˇÂ ÄŹÂ¸Ĺą):**
- Brak `@onEnter/@onEscape` dla okna z przyciskami akcji.
- Brak autoĂ˘â‚¬â€fit width (okno dokowane ma `width`).
- Nieparzyste marginesy (snapping 2 px).<div id="ch-7-8"></div>
## 7.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
- **Lista w content**: wstaw `TextList` i dokoÄąâ€škuj `VerticalScrollBar` jako **sibling** po prawej; ustaw `content.anchors.right: scroll.left`.
- **Kolaps/rozwin**: `onToggleMinimize()` ukrywa/pokazuje `content` i `footer`; przycisk zmienia label `'-'`/`'+'`.
- **DialogĂ˘â‚¬â€like**: `MiniWindow` moÄąÄ˝e peÄąâ€šniÄ‡ rolÄ™ prostego dialogu â€” dodaj `@onEnter/@onEscape` i ukÄąâ€šad przyciskĂłw w `footer`.
- **Wiele MiniWindow**: kaÄąÄ˝de musi mieÄ‡ unikalne `id`; edytor powinien zapobiegaÄ‡ kolizjom przy imporcie.
<div id="ch-8-1"></div>
## 8.1 Struktura (titlebar/content)
**ContainerWindow** sÄąâ€šuÄąÄ˝y do prezentacji i operacji na zawartoÄąâ€şci (sloty/elementy). SkÄąâ€šada siÄ™ z:
- **`titlebar`** â€” nagÄąâ€šĂłwek z przyciskami **back/pin/minimize/close** i tytuÄąâ€šem,
- **`content`** â€” obszar siatki slotĂłw (przewijalny przy overflow). 

**Zakazy**: w `titlebar` brak list/edytorĂłw/scrollbarĂłw; w `content` brak okienĂ˘â‚¬â€dzieci (`*Window`).

**AutoĂ˘â‚¬â€fit width**: po osadzeniu w panelu okno powinno rozciÄ…gaÄ‡ siÄ™ poziomo (`anchors.left/right: parent`), odstÄ™py przez `margin-*`.<div id="ch-8-2"></div>
## 8.2 Titlebar: back/pin/min/close
- **Back** â€” powrĂłt do poprzedniego kontenera (kontroler Lua zarzÄ…dza stosem/nawigacjÄ…).
- **Pin/Lock** â€” przypina okno (zachowanie w kontrolerze; moÄąÄ˝e wpÄąâ€šywaÄ‡ na zĂ˘â‚¬â€order/dokowanie).
- **Minimize** â€” zwija `content` (i ukrywa ewentualny `footer` jeÄąâ€şli wystÄ™puje), stan sygnalizowany na przycisku.
- **Close** â€” ukrywa/zamyka okno przez kontroler.

**Dozwolone dzieci `titlebar`**: `Label` (tytuÄąâ€š), `Button` (back/pin/min/close), `UIWidget` (ikona).<div id="ch-8-3"></div>
## 8.3 Content: siatka slotĂłw i DnD
- **Siatka**: projektowana jako `UIWidget id: grid`, z **powtarzanymi** dzieÄ‡mi `SlotWidget < UIWidget` (staÄąâ€šy rozmiar i odstÄ™py). 
- **Rozmieszczenie**: edytor dba o snapping (2 px) i kolumny/wiersze; runtime moÄąÄ˝e dynamicznie przepinaÄ‡ sloty, ale eksport zachowuje deterministyczny ukÄąâ€šad.
- **DnD**: ÄąĹźrĂłdÄąâ€šo/cel tylko w `content` (sloty). PodÄąâ€şwietlenie slotu podczas hover/mocy przeniesienia realizowane stanami na `SlotWidget` lub przez kontroler Lua.
- **Scroll**: przy overflow dodaj **VerticalScrollBar** jako sibling po prawej; `grid.anchors.right: scroll.left`.<div id="ch-8-4"></div>
## 8.4 Scroll i overflow
- **VerticalScrollBar** dokowany do prawej krawÄ™dzi `ContainerWindow`; `grid` kotwiczy `right: scroll.left`.
- **Step/pixels**: ustaw `step` zgodnie z wysokoÄąâ€şciÄ… slotu (np. 32/36), aby skok przewijania pokrywaÄąâ€š rzÄ…d.
- **Samotny ScrollBar** lub listy/edytory w `titlebar` â€” bÄąâ€šÄ…d walidacji.<div id="ch-8-5"></div>
## 8.5 Blueprint OTUI (kanoniczny, STRICT)
`$fenceInfo
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
## 8.6 Mapowanie TS Ă˘â€ â€ť OTUI (serializer)
**Preset (TS)**
`$fenceInfo
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
**Serializer**: GEOMETRIAĂ˘â€ â€™STYLĂ˘â€ â€™ZACHOWANIE; `style.text`Ă˘â€ â€™`!text: tr('...')`; `events`Ă˘â€ â€™`@on...`. **Sanityzacja**: `ensureStrictOtui()`.

**Uwaga**: `SlotWidget < UIWidget` to **lokalna klasa stylu** w pliku; w realnym projekcie moÄąÄ˝esz podmieniÄ‡ na wÄąâ€šasny typ slotu.<div id="ch-8-7"></div>
## 8.7 Walidator (bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia)
**BlokujÄ…ce (Ă˘ĹĄĹš):**
- Brak przycisku **back** w `titlebar` (nawigacja kontenera).
- Niedozwolone dzieci w `titlebar` (scroll/listy/edytory).
- `content` zawiera inne okno (`*Window`).
- `VerticalScrollBar` bez sparowanej treÄąâ€şci (`grid`) lub odwrotnie (overflow bez scrolla).
- Sprzeczne kotwice (`fill` + krawÄ™dzie). Teksty bez `tr()`; zasoby spoza `data/`.

**OstrzeÄąÄ˝enia (Ă˘ĹˇÂ ÄŹÂ¸Ĺą):**
- Brak `pin`/`minimize`/`close` w `titlebar` (wymagane zaleÄąÄ˝nie od projektu). 
- `step` scrolla nie odpowiada wysokoÄąâ€şci wiersza slotĂłw (nieprzyjemne przewijanie). 
- Nieparzyste marginesy/spacing (snapping 2 px).<div id="ch-8-8"></div>
## 8.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
- **PowrĂłt (back)**: `ContainerController.onBack()` przywraca poprzedni kontener (stack), a `@onEscape` mapuje siÄ™ na tÄ™ samÄ… akcjÄ™.
- **Pin/Lock**: przeÄąâ€šÄ…cza stan â€žprzypiÄ™tyâ€ť okna; w `$on` przycisku moÄąÄ˝esz zmieniÄ‡ kolor/ikonÄ™.
- **Overflow**: przy dodaniu N+1 rzÄ™du slotĂłw Ă˘â€ â€™ edytor proponuje VerticalScrollBar i kotwice `grid.right: scroll.left`.
- **DnD**: slot w stanie â€žhoverâ€ť (`$focus` lub wÄąâ€šasny stan logiczny) zmienia tÄąâ€šo; kontroler waliduje dozwolone dropy.
- **Minimalne rozmiary slotu**: Ă˘â€°Ä„32Ä‚â€”32 (lub projektowe), spacing Ă˘â€°Ä„4 px â€” zapewnij spĂłjnoÄąâ€şÄ‡ siatki.

---
## 9. DialogWindow
- [9.1 Struktura](#ch-9-1)
- [9.2 Enter/Escape (OK/Cancel)](#ch-9-2)
- [9.3 ModalnoÄąâ€şÄ‡ i fokus](#ch-9-3)
- [9.4 Blueprint OTUI (STRICT)](#ch-9-4)
- [9.5 Preset TS (serializerĂ˘â‚¬â€ready)](#ch-9-5)
- [9.6 Walidator (bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia)](#ch-9-6)
- [9.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-9-7)

<div id="ch-9-1"></div>
## 9.1 Struktura
**DialogWindow** to lekkie okno dialogowe do potwierdzeÄąâ€ž, komunikatĂłw i prostych promptĂłw.
- Obszary: `titlebar`, `content`, `footer` (analogicznie do MiniWindow).
- Wymagane skrĂłty: **Enter = OK**, **Escape = Cancel**.
- Zakazy: brak okienĂ˘â‚¬â€dzieci (`*Window`) w `content`; brak list/edytorĂłw/scrolla w `titlebar`/`footer`.

<div id="ch-9-2"></div>
## 9.2 Enter/Escape (OK/Cancel)
- `@onEnter` Ă˘â€ â€™ akcja domyÄąâ€şlna (OK/Apply).
- `@onEscape` Ă˘â€ â€™ anulowanie/zamkniÄ™cie.
- Edytor wymusza obecnoÄąâ€şÄ‡ **co najmniej jednego** przycisku w `footer` i mapuje go na Enter/Escape zgodnie z rolÄ….

<div id="ch-9-3"></div>
## 9.3 ModalnoÄąâ€şÄ‡ i fokus
- ModalnoÄąâ€şÄ‡: opcjonalna (np. przez overlay moduÄąâ€šu).
- Po otwarciu ustaw fokus na domyÄąâ€şlny przycisk OK lub pierwsze pole edycji.
- ZamkniÄ™cie: kontroler Lua decyduje o `:hide()` i sprzÄ…taniu zasobĂłw.

<div id="ch-9-4"></div>
## 9.4 Blueprint OTUI (STRICT)
`$fenceInfo
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
## 9.5 Preset TS (serializerĂ˘â‚¬â€ready)
`$fenceInfo
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
## 9.6 Walidator (bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia)
**BlokujÄ…ce (Ă˘ĹĄĹš):** brak `@onEnter/@onEscape`; brak przyciskĂłw w `footer` lub brak mapowania OK/Escape; dzieci niedozwolone w `titlebar/footer` (listy/edytory/scroll); `*Window` w `content`; sprzeczne kotwice; brak `tr()`; zasoby spoza `data/`.

**OstrzeÄąÄ˝enia (Ă˘ĹˇÂ ÄŹÂ¸Ĺą):** brak autoĂ˘â‚¬â€fit w poziomie po dokowaniu; nieparzyste marginesy/spacing.

<div id="ch-9-7"></div>
## 9.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
- Prompt z `TextEdit`: pole w `content` + mapowanie Enter/Escape na OK/Cancel.
- DÄąâ€šugi tekst: `MultilineTextEdit` + **VerticalScrollBar** (sibling) i wrapping label z leadem.
- DialogĂ˘â‚¬â€potwierdzenie otwierany z MiniWindow: fokus od razu na OK; Escape zamyka bez skutkĂłw ubocznych.

---
## 10. Titlebar
- [10.1 Ikona, tytuÄąâ€š, przyciski](#ch-10-1)
- [10.2 Slot i dozwolone dzieci](#ch-10-2)
- [10.3 DragĂ˘â‚¬â€move i fokus](#ch-10-3)
- [10.4 Blueprint OTUI (STRICT)](#ch-10-4)
- [10.5 Preset TS (warianty back/pin)](#ch-10-5)
- [10.6 Walidator](#ch-10-6)
- [10.7 Integracja (Lua glue)](#ch-10-7)

<div id="ch-10-1"></div>
## 10.1 Ikona, tytuÄąâ€š, przyciski
**Titlebar** to pasek nagÄąâ€šĂłwka okna. Typowe elementy:
- **Ikona** (`UIWidget` z obrazem) â€” opcjonalna z lewej.
- **TytuÄąâ€š** (`Label`) â€” `text-auto-resize: true`, wyrĂłwnanie do lewej.
- **Przyciski** (`Button`) â€” po prawej: **minimize**, **close**, opcjonalnie **back**, **pin**.
- WysokoÄąâ€şÄ‡ staÄąâ€ša (np. 20 px); tÄąâ€šo/kolor zgodne z motywem.

<div id="ch-10-2"></div>
## 10.2 Slot i dozwolone dzieci
- Titlebar jest **wydzielonym `UIWidget`** (slot) wewnÄ…trz okna (`*Window`).
- Dozwolone dzieci: `Label`, `Button`, `UIWidget` (ikona).
- Zakazane: listy, edytory, ScrollBary i inne okna.
- Przyciski powinny mieÄ‡ jednolite szerokoÄąâ€şci (16â€“20 px) i kotwice do prawej krawÄ™dzi.

<div id="ch-10-3"></div>
## 10.3 DragĂ˘â‚¬â€move i fokus
- Obszar przeciÄ…gania moÄąÄ˝e obejmowaÄ‡ caÄąâ€šy `titlebar` (obsÄąâ€šuga po stronie klienta/kontrolera).
- Klik w tytuÄąâ€š/puste pole nie powinien zabieraÄ‡ fokusu kluczowym elementom w `content`.
- SkrĂłty dla przyciskĂłw moÄąÄ˝na zmapowaÄ‡ w `@onSetup`/Lua.

<div id="ch-10-4"></div>
## 10.4 Blueprint OTUI (STRICT)
`$fenceInfo
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
`$fenceInfo
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
- Ă˘ĹĄĹš Dzieci spoza dozwolonego zestawu (lista/edytory/scroll).
- Ă˘ĹĄĹš Brak `minimize`/`close` tam, gdzie wymagane (MiniWindow/Container/Dialog).
- Ă˘ĹĄĹš Niepoprawne kotwice (przyciski bez powiÄ…zaÄąâ€ž do prawej krawÄ™dzi).
- Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak `back`/`pin` w wariantach wymaganych projektowo.
- Ă˘ĹˇÂ ÄŹÂ¸Ĺą Nieparzyste marginesy i niespĂłjne szerokoÄąâ€şci przyciskĂłw.

<div id="ch-10-7"></div>
## 10.7 Integracja (Lua glue)
`$fenceInfo
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
  -- przeÄąâ€šÄ…cz stan przypiÄ™cia; szczegĂłÄąâ€šy zaleÄąÄ˝ne od projektu
end
```

---
## 11. Toolbar
- [11.1 Rola i struktura](#ch-11-1)
- [11.2 Dozwolone dzieci](#ch-11-2)
- [11.3 Geometria i styl](#ch-11-3)
- [11.4 Stany i zdarzenia](#ch-11-4)
- [11.5 Blueprint OTUI (STRICT)](#ch-11-5)
- [11.6 Preset TS (serializerĂ˘â‚¬â€ready)](#ch-11-6)
- [11.7 Walidator](#ch-11-7)
- [11.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-11-8)

<div id="ch-11-1"></div>
## 11.1 Rola i struktura
**Toolbar** to pasek akcji, zwykle pod `titlebar` lub w `header`. Zawiera grupy przyciskĂłw i separatory.

<div id="ch-11-2"></div>
## 11.2 Dozwolone dzieci
Dozwolone: `Button` (akcje/toggle), `UIWidget` jako separator lub ikona. Niedozwolone: listy, edytory, ScrollBary i okna.

<div id="ch-11-3"></div>
## 11.3 Geometria i styl
WysokoÄąâ€şÄ‡ staÄąâ€ša (np. 20â€“24). Anchors lewoĂ˘â‚¬â€prawo do rodzica. TÄąâ€šo pĂłÄąâ€šprzezroczyste lub obraz motywu. Jednolite odstÄ™py miÄ™dzy grupami.

<div id="ch-11-4"></div>
## 11.4 Stany i zdarzenia
Przyciski mogÄ… mieÄ‡ stany `$on/$!on` (toggle). Zdarzenia `@onClick`. Klawiszowe skrĂłty wiÄ…ÄąÄ˝ w `@onSetup` okna.

<div id="ch-11-5"></div>
## 11.5 Blueprint OTUI (STRICT)
`$fenceInfo
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
## 11.6 Preset TS (serializerĂ˘â‚¬â€ready)
`$fenceInfo
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
Ă˘ĹĄĹš Listy/edytory/scroll w Toolbar. Ă˘ĹĄĹš Brak wysokoÄąâ€şci. Ă˘ĹĄĹš Nieparzyste marginesy lub nierĂłwne szerokoÄąâ€şci w grupie. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak skrĂłtĂłw dla akcji o wysokiej czÄ™stotliwoÄąâ€şci.

<div id="ch-11-8"></div>
## 11.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Lewa grupa akcji + prawa grupa statusĂłw; wariant kompaktowy 16 px wysokoÄąâ€şci; tryb toggle dla filtrĂłw danych.

---
## 12. Panel / GroupBox
- [12.1 Rola i struktura](#ch-12-1)
- [12.2 Dozwolone dzieci](#ch-12-2)
- [12.3 Geometria i styl](#ch-12-3)
- [12.4 Stany i zdarzenia](#ch-12-4)
- [12.5 Blueprinty OTUI (STRICT)](#ch-12-5)
- [12.6 Presety TS](#ch-12-6)
- [12.7 Walidator](#ch-12-7)
- [12.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-12-8)

<div id="ch-12-1"></div>
## 12.1 Rola i struktura
**Panel** to podstawowy kontener sekcji. **GroupBox** to panel z nagÄąâ€šĂłwkiem i ramkÄ…/separatorem.

<div id="ch-12-2"></div>
## 12.2 Dozwolone dzieci
Dozwolone: wszystkie elementy â€žpaneloweâ€ť (Label, Button, TextEdit, MultilineTextEdit, TextList, ComboBox, CheckBox, ProgressBar, TabBar, Splitter, VerticalScrollBar, HorizontalSeparator, UIWidget). Niedozwolone: okna (`*Window`).

<div id="ch-12-3"></div>
## 12.3 Geometria i styl
Anchors zgodne z ukÄąâ€šadem rodzica. Marginesy i padding parzyste. TÄąâ€šo transparentne lub obraz/kolor sekcji. GroupBox ma label nagÄąâ€šĂłwka oraz obramowanie lub separator pod tytuÄąâ€šem.

<div id="ch-12-4"></div>
## 12.4 Stany i zdarzenia
Zwykle brak stanĂłw na samym Panelu; stany stosuj na dzieciach. Zdarzenia klikalne tylko, jeÄąâ€şli Panel peÄąâ€šni rolÄ™ przyciskopodobnÄ….

<div id="ch-12-5"></div>
## 12.5 Blueprinty OTUI (STRICT)
`$fenceInfo
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

`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš Okna (`*Window`) jako dzieci. Ă˘ĹĄĹš Brak obszaru treÄąâ€şci w GroupBox. Ă˘ĹĄĹš Sprzeczne kotwice. Ă˘ĹĄĹš Brak `tr()` w nagÄąâ€šĂłwkach. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Nieparzyste marginesy/padding. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak autoĂ˘â‚¬â€fit przy dokowaniu.

<div id="ch-12-8"></div>
## 12.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Panel z formularzem i przyciskami akcji w dolnym rogu; GroupBox z wieloma polami i czytelnym separatorem; warianty z tÄąâ€šem obrazkowym.

---
## 13. TabBar / TabWidget
- [13.1 Rola i struktura](#ch-13-1)
- [13.2 Dozwolone dzieci](#ch-13-2)
- [13.3 Geometria i styl](#ch-13-3)
- [13.4 Stany i zdarzenia](#ch-13-4)
- [13.5 Blueprinty OTUI (STRICT)](#ch-13-5)
- [13.6 Presety TS](#ch-13-6)
- [13.7 Walidator](#ch-13-7)
- [13.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-13-8)

<div id="ch-13-1"></div>
## 13.1 Rola i struktura
**TabBar** zawiera przyciski zakÄąâ€šadek. **TabWidget** lub dedykowany `UIWidget` jest kontenerem treÄąâ€şci zakÄąâ€šadki. TabBar i treÄąâ€şÄ‡ sÄ… rodzeÄąâ€žstwem w drzewie.

<div id="ch-13-2"></div>
## 13.2 Dozwolone dzieci
TabBar: `Button` dla kaÄąÄ˝dej zakÄąâ€šadki, ewentualne separatory. TreÄąâ€şÄ‡ zakÄąâ€šadki: dowolne elementy panelowe. Niedozwolone: okna w treÄąâ€şci, ScrollBar w TabBarze.

<div id="ch-13-3"></div>
## 13.3 Geometria i styl
TabBar u gĂłry, rozciÄ…gniÄ™ty poziomo. Content poniÄąÄ˝ej, zakotwiczony do TabBar `top: tabBar.bottom`. StaÄąâ€še wysokoÄąâ€şci przyciskĂłw.

<div id="ch-13-4"></div>
## 13.4 Stany i zdarzenia
Aktywna zakÄąâ€šadka moÄąÄ˝e mieÄ‡ `$on`. Zdarzenie zmiany zakÄąâ€šadki mapowane do kontrolera (np. `TabsController.onTabChange(index)`), ewentualnie `@onClick` na przycisku zakÄąâ€šadki.

<div id="ch-13-5"></div>
## 13.5 Blueprinty OTUI (STRICT)
`$fenceInfo
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

`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš TreÄąâ€şÄ‡ upakowana do TabBar zamiast do dedykowanego kontenera. Ă˘ĹĄĹš Brak aktywnej zakÄąâ€šadki. Ă˘ĹĄĹš Sprzeczne kotwice. Ă˘ĹĄĹš Brak `tr()` w etykietach. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak mechanizmu zmiany zakÄąâ€šadki w kontrolerze.

<div id="ch-13-8"></div>
## 13.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Dwie zakÄąâ€šadki z rĂłÄąÄ˝nymi panelami treÄąâ€şci; adaptacja do maÄąâ€šej szerokoÄąâ€şci przez skrĂłtowe etykiety; synchronizacja aktywnoÄąâ€şci z kontrolerem i stanem `$on` na przycisku.

---
## 14. Splitter
- [14.1 Rola i struktura](#ch-14-1)
- [14.2 Dozwolone dzieci](#ch-14-2)
- [14.3 Geometria i styl](#ch-14-3)
- [14.4 Stany i zdarzenia](#ch-14-4)
- [14.5 Blueprinty OTUI (STRICT) â€“ poziomy/pionowy](#ch-14-5)
- [14.6 Presety TS](#ch-14-6)
- [14.7 Walidator](#ch-14-7)
- [14.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-14-8)
- [14.9 Splitter â€” grip i persystencja](#ch-14-9)

<div id="ch-14-1"></div>
## 14.1 Rola i struktura
**Splitter** dzieli obszar na dwie czÄ™Äąâ€şci (panele) z regulowanym podziaÄąâ€šem. Stosowany do ukÄąâ€šadĂłw â€žlista Ă˘â€ â€ť szczegĂłÄąâ€šyâ€ť, â€žnawigacja Ă˘â€ â€ť treÄąâ€şÄ‡â€ť.

<div id="ch-14-2"></div>
## 14.2 Dozwolone dzieci
Dopuszczalne sÄ… **dokÄąâ€šadnie dwa panele** (np. `UIWidget`/`Panel`). Dodatkowe elementy (np. overlay â€žgripâ€ť) mogÄ… byÄ‡ zastosowane tylko jako **lekki overlay** niebÄ™dÄ…cy panelem (walidator traktuje je osobno).

<div id="ch-14-3"></div>
## 14.3 Geometria i styl
- Wariant **poziomy**: lewy panel kotwiczony do lewej, prawy do prawej; granica pomiÄ™dzy panelami.
- Wariant **pionowy**: gĂłrny panel do gĂłry, dolny do doÄąâ€šu.  
- **MinĂ˘â‚¬â€size** paneli: wymagana; zapewnij, by podziaÄąâ€š nie â€žzgniataÄąâ€šâ€ť dzieci poniÄąÄ˝ej minimalnych rozmiarĂłw.
- TÄąâ€šo zwykle transparentne; granicÄ™ moÄąÄ˝na sygnalizowaÄ‡ wÄ…skim paskiem.

<div id="ch-14-4"></div>
## 14.4 Stany i zdarzenia
- Zdarzenia resize i drag â€žgripaâ€ť implementuje kontroler (Lua) lub logika klienta. 
- Stany wizualne (hover/drag) moÄąÄ˝na realizowaÄ‡ `$focus`/`$on` na panelu/gripie.

<div id="ch-14-5"></div>
## 14.5 Blueprinty OTUI (STRICT) â€“ poziomy/pionowy
**Poziomy (Left/Right)**
`$fenceInfo
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
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš Ă˘â€°Â 2 paneli. Ă˘ĹĄĹš Sprzeczne kotwice (np. oba panele majÄ… sztywne szerokoÄąâ€şci i jednoczeÄąâ€şnie rozciÄ…gniÄ™cie). Ă˘ĹĄĹš Brak minĂ˘â‚¬â€size przy wymaganym â€žgripâ€ť zachowaniu. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak parzystych marginesĂłw. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak autoĂ˘â‚¬â€fit do rodzica.

<div id="ch-14-8"></div>
## 14.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Lewy panel: lista; prawy: szczegĂłÄąâ€šy. GĂłrny: log, dolny: konsola. ZapamiÄ™tywanie podziaÄąâ€šu w ustawieniach moduÄąâ€šu (kontroler Lua).

<div id="ch-14-9"></div>
## 14.9 Splitter â€” grip i persystencja
- **Grip (hitbox)**: zapewnij obszar chwytu o gruboÄąâ€şci **6â€“8 px** na granicy paneli (wizualnie 1â€“2 px linia, reszta transparentny hitbox).  
- **MinĂ˘â‚¬â€size paneli**: egzekwuj `min-width/min-height` paneli (np. 120 px) â€” podziaÄąâ€š nie moÄąÄ˝e ich naruszyÄ‡.  
- **Tryb klawiatury**: `Ctrl+Ă˘â€ Â/Ă˘â€ â€™` (poziomy) lub `Ctrl+Ă˘â€ â€/Ă˘â€ â€ś` (pionowy) do krokowej zmiany podziaÄąâ€šu (np. 16 px).  
- **Persystencja**: zapisuj **ratio** (0..1) lub **px** w ustawieniach moduÄąâ€šu i odtwarzaj przy inicjalizacji.  
- **Blueprint grip (overlay, STRICT)**:
`$fenceInfo
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
- [15.9 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-15-9)
- [15.10 TextList â€” nawigacja klawiaturÄ… i ensureVisible](#ch-15-10)

<div id="ch-15-1"></div>
## 15.1 Rola i struktura
**TextList** prezentuje listÄ™ pozycji przewijalnÄ… w pionie. Wiersze sÄ… reprezentowane jako lekkie `UIWidget` (np. `ListRow`) osadzane w kontenerze listy.

<div id="ch-15-2"></div>
## 15.2 Dozwolone dzieci
WewnÄ…trz listy: tylko wiersze (`UIWidget`/custom row). Zakazane: okna, ScrollBar jako dziecko (ScrollBar jest **siblingiem** listy).

<div id="ch-15-3"></div>
## 15.3 Geometria i styl
- ListÄ™ kotwicz do dostÄ™pnego obszaru (`anchors.fill: parent` lub do `scroll.left`).
- WysokoÄąâ€şÄ‡ wiersza min. ~14 px (zalecenie) dla czytelnoÄąâ€şci. 
- PodÄąâ€şwietlenie wiersza przez stany (`$focus`/`$on`) lub kolory tÄąâ€ša.

<div id="ch-15-4"></div>
## 15.4 Scroll pairing
**VerticalScrollBar** jest **siblingiem**: dokowany po prawej; lista kotwiczy `right: scroll.left`. `step` powinien odpowiadaÄ‡ wysokoÄąâ€şci wiersza.

<div id="ch-15-5"></div>
## 15.5 Stany i zdarzenia
- Zdarzenia: `@onClick` na wiersz (zaznaczenie), opcjonalny `@onSetup` do bindĂłw strzaÄąâ€šek/PageUp/Down. 
- Fokus: po otwarciu ustaw na listÄ™ lub pierwszy wiersz; upewnij siÄ™, ÄąÄ˝e wybrany wiersz jest widoczny (logika kontrolera).

<div id="ch-15-6"></div>
## 15.6 Blueprinty OTUI (STRICT)
**Lista ze scrollem**
`$fenceInfo
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
`$fenceInfo
VerticalScrollBar
  id: scroll
  anchors.right: parent.right
  anchors.top: parent.top
  anchors.bottom: parent.bottom
  step: 16
```

**Wiersz listy (uniwersalny)**
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš ScrollBar jako dziecko listy. Ă˘ĹĄĹš Lista bez pary scrolla przy overflow lub bÄąâ€šÄ™dne kotwice pary. Ă˘ĹĄĹš `tr()` pominiÄ™te w etykietach. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Zbyt maÄąâ€ša wysokoÄąâ€şÄ‡ wiersza (nieczytelnoÄąâ€şÄ‡). Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak bindĂłw klawiatury.

<div id="ch-15-9"></div>
## 15.9 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Lista postaci (row = imiÄ™ + poziom), lista logĂłw (row z ikonÄ… i timestampem). â€žEnsure visibleâ€ť przy zmianie wyboru. Paging klawiaturÄ… (PageUp/Down).

<div id="ch-15-10"></div>
## 15.10 TextList â€” nawigacja klawiaturÄ… i ensureVisible
- **StrzaÄąâ€ški**: Ă˘â€ â€/Ă˘â€ â€ś wybĂłr sÄ…siedniego wiersza.  
- **PageUp/Down**: skok o `pageSize` (wysokoÄąâ€şÄ‡ kontenera / wysokoÄąâ€şÄ‡ wiersza).  
- **Home/End**: pierwszy/ostatni wiersz.  
- **Enter/Escape**: potwierdzenie/anulowanie zgodnie z logikÄ… okna.  
- **ensureVisible**: po zmianie wyboru kontroler przewija listÄ™ tak, by wybrany wiersz byÄąâ€š w peÄąâ€šni widoczny.  
- **MultiĂ˘â‚¬â€select (opcjonalnie)**: `Shift` = zakres, `Ctrl` = pojedyncze przeÄąâ€šÄ…czanie â€” tylko jeÄąâ€şli projekt to wymaga; w `.otui` bez zmian, logika w kontrolerze.

---
## 16. Label / UILabel
- [16.1 Rola i struktura](#ch-16-1)
- [16.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci tekstu](#ch-16-2)
- [16.3 Geometria i styl](#ch-16-3)
- [16.4 Stany i zdarzenia](#ch-16-4)
- [16.5 Blueprinty OTUI (STRICT)](#ch-16-5)
- [16.6 Presety TS](#ch-16-6)
- [16.7 Walidator](#ch-16-7)
- [16.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-16-8)
- [16.9 Label â€” pomiar tekstu, elipsyzacja, DPI/scale](#ch-16-9)

<div id="ch-16-1"></div>
## 16.1 Rola i struktura
**Label/UILabel** to nieinteraktywny element tekstowy do podpisĂłw, tytuÄąâ€šĂłw i statusĂłw. `UILabel` moÄąÄ˝e sÄąâ€šuÄąÄ˝yÄ‡ jako wariant nazwowy z gotowym stylem; oba majÄ… te same podstawowe wÄąâ€šaÄąâ€şciwoÄąâ€şci tekstowe.

<div id="ch-16-2"></div>
## 16.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci tekstu
- `!text: tr('...')` â€” jedyne dozwolone ÄąĹźrĂłdÄąâ€šo staÄąâ€šych napisĂłw (STRICT).  
- `text-wrap: true|false` â€” zawijanie.  
- `text-auto-resize: true|false` â€” dopasowanie do treÄąâ€şci.  
- `text-align: left|center|right` â€” wyrĂłwnanie.  
- `text-offset: X Y` â€” przesuniÄ™cie.  
- `font: <nazwa>` â€” z `data/fonts/`.  
- `color: #AARRGGBB`.

<div id="ch-16-3"></div>
## 16.3 Geometria i styl
- Anchors do rodzica lub sÄ…siadĂłw; czÄ™sto `anchors.left/right: parent` przy statusach.  
- UÄąÄ˝ywaj parzystych marginesĂłw (snapping 2 px).  
- TÄąâ€šo zwykle `alpha`.

<div id="ch-16-4"></div>
## 16.4 Stany i zdarzenia
- Label nie jest klikany; zdarzenia zwykle pomijamy.  
- Stany `$on/$!on/$focus` moÄąÄ˝esz wykorzystaÄ‡ do zmiany koloru lub wyeksponowania (np. bÄąâ€šÄ™dy/ostrzeÄąÄ˝enia), nie geometrii.

<div id="ch-16-5"></div>
## 16.5 Blueprinty OTUI (STRICT)
**NagÄąâ€šĂłwek sekcji**
`$fenceInfo
Label
  id: header
  anchors.left: parent.left
  anchors.right: parent.right
  text-auto-resize: true
  !text: tr('Section')
  font: verdana-11px-rounded
```

**Status wielowierszowy**
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš Brak `tr()` w `!text`. Ă˘ĹĄĹš Zasoby fontu spoza `data/`. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Nieparzyste marginesy. Ă˘ĹˇÂ ÄŹÂ¸Ĺą NaduÄąÄ˝ywanie `text-auto-resize` przy wÄ…skich ukÄąâ€šadach (ryzyko overflow).

<div id="ch-16-8"></div>
## 16.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
NagÄąâ€šĂłwki w `titlebar` i w treÄąâ€şci; statusy z `text-wrap: true`; komunikaty ostrzegawcze kolorem w `$on`.

<div id="ch-16-9"></div>
## 16.9 Label â€” pomiar tekstu, elipsyzacja, DPI/scale
- **Pomiar**: unikaj twardych szerokoÄąâ€şci dla dÄąâ€šugich etykiet; preferuj `text-wrap: true` lub `text-auto-resize: true` (gdy bezpieczne).  
- **Elipsyzacja**: stosuj tylko przy staÄąâ€šych szerokoÄąâ€şciach; zapewnij tooltip z peÄąâ€šnym tekstem (kontroler).  
- **DPI/Scale**: testuj metryki fontu (line-height, kerning) w skalach 1.0/1.25/1.5; utrzymuj snapping 2 px.

---
## 17. Button
- [17.1 Rola i struktura](#ch-17-1)
- [17.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci i minimalne rozmiary](#ch-17-2)
- [17.3 Geometria i styl](#ch-17-3)
- [17.4 Stany i zdarzenia](#ch-17-4)
- [17.5 Blueprinty OTUI (STRICT)](#ch-17-5)
- [17.6 Presety TS](#ch-17-6)
- [17.7 Walidator](#ch-17-7)
- [17.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-17-8)
- [17.9 Button â€” hover/disabled i dostÄ™pnoÄąâ€şÄ‡](#ch-17-9)

<div id="ch-17-1"></div>
## 17.1 Rola i struktura
**Button** wyzwala akcje (`@onClick`). MoÄąÄ˝e dziaÄąâ€šaÄ‡ jako chwilowy przycisk, przeÄąâ€šÄ…cznik (toggle) lub przycisk paskowy (tytuÄąâ€š/toolbar). Zwykle bez dzieci â€” tekst ustawiany bezpoÄąâ€şrednio przez `!text`.

<div id="ch-17-2"></div>
## 17.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci i minimalne rozmiary
- `!text: tr('...')` â€” etykieta.  
- Zalecane minimum rozmiaru: **Ă˘â€°Ä„16Ä‚â€”16** (kompakt) lub szersze dla etykiet tekstowych (np. 60â€“72 px).  
- Opcjonalnie `font`, `color`, `background-color`.

<div id="ch-17-3"></div>
## 17.3 Geometria i styl
- Kotwice do krawÄ™dzi rodzica lub sÄ…siadĂłw (czÄ™sto do prawej w `footer`/`titlebar`).  
- Parzyste marginesy; wysokoÄąâ€şci zgodne ze stylem paska (np. 20 px w titlebar/toolbar).  
- Tekst przez `!text` (STRICT), bez wewnÄ™trznego `Label`.

<div id="ch-17-4"></div>
## 17.4 Stany i zdarzenia
- `@onClick: Controller.fn()` â€” podstawowe zdarzenie.  
- `$on/$!on` â€” dla trybu **toggle** (zmiana tÄąâ€ša/koloru/napisu).  
- `$focus` â€” podÄąâ€şwietlenie przy fokusie klawiatury.  
- SkrĂłty klawiszowe mapuj w `@onSetup` okna lub w Lua.

<div id="ch-17-5"></div>
## 17.5 Blueprinty OTUI (STRICT)
**Standardowy przycisk**
`$fenceInfo
Button
  id: ok
  width: 64
  !text: tr('Ok')
```

**Toggle (On/Off)**
`$fenceInfo
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

**Ikonowy (tytuÄąâ€š/toolbar)**
`$fenceInfo
Button
  id: closeBtn
  width: 16
  !text: tr('x')
```

<div id="ch-17-6"></div>
## 17.6 Presety TS
`$fenceInfo
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
Ă˘ĹĄĹš Brak `tr()` w etykiecie. Ă˘ĹĄĹš Zbyt maÄąâ€šy rozmiar (mniej niÄąÄ˝ 16Ä‚â€”16). Ă˘ĹĄĹš WewnÄ™trzne dzieci (Label) zamiast `!text`. Ă˘ĹˇÂ ÄŹÂ¸Ĺą NiespĂłjne szerokoÄąâ€şci w grupie. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak skrĂłtĂłw dla akcji czÄ™sto uÄąÄ˝ywanych.

<div id="ch-17-8"></div>
## 17.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Przyciski OK/Cancel w `footer`; ikonowe 16 px w `titlebar`; toggle dla filtrĂłw narzÄ™dzi. Zmiana etykiety w `$on/$!on` bez modyfikacji geometrii.

<div id="ch-17-9"></div>
## 17.9 Button â€” hover/disabled i dostÄ™pnoÄąâ€şÄ‡
- **$hover**: feedback najechania (kolor/tÄąâ€šo), bez zmiany geometrii.  
- **$disabled**: peÄąâ€šna nieinteraktywnoÄąâ€şÄ‡; zachowaj kontrast etykiety Ă˘â€°Ä„ WCAG AA.  
- **Hitbox**: min. **16Ä‚â€”16**; dla tekstowych szerokoÄąâ€şÄ‡ wg etykiety (Ă˘â€°Ä„60 px).  
- **SkrĂłty**: najczÄ™stsze akcje zbinduj w `@onSetup`.

**PrzykÄąâ€šad (STRICT)**
`$fenceInfo
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
- [18.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci](#ch-18-2)
- [18.3 Geometria i styl](#ch-18-3)
- [18.4 Stany i zdarzenia](#ch-18-4)
- [18.5 Blueprinty OTUI (STRICT)](#ch-18-5)
- [18.6 Presety TS](#ch-18-6)
- [18.7 Walidator](#ch-18-7)
- [18.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-18-8)
- [18.9 CheckBox â€” triĂ˘â‚¬â€state i offset etykiety](#ch-18-9)

<div id="ch-18-1"></div>
## 18.1 Rola i struktura
**CheckBox** to przeÄąâ€šÄ…cznik boolean z wbudowanÄ… etykietÄ… tekstowÄ… po prawej. Nie posiada dzieci. Wariant **RoundCheckBox** to styl okrÄ…gÄąâ€šy.

<div id="ch-18-2"></div>
## 18.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci
- `!text: tr('...')` â€” etykieta.  
- `text-align`, `text-offset` â€” pozycjonowanie tekstu wzglÄ™dem pola.  
- `image-source`, `image-rect`/`image-clip`, `image-color` â€” grafika stanu.  
- `cursor`, `change-cursor-image` â€” zachowanie kursora.  
- `enabled: true|false` â€” stan dostÄ™pnoÄąâ€şci.

<div id="ch-18-3"></div>
## 18.3 Geometria i styl
- Typowy rozmiar pola: **16Ä‚â€”16**; etykieta po prawej poprzez `text-offset` (np. `18 1`).  
- Kotwice do ukÄąâ€šadu rodzica; parzyste marginesy.  
- Kolory/obrazy zgodnie z motywem.

<div id="ch-18-4"></div>
## 18.4 Stany i zdarzenia
- Stany: `$checked`, `$!checked`, `$hover`, `$disabled` (moÄąÄ˝liwe kombinacje, np. `$hover !disabled`).  
- Zdarzenia: `@onClick` Ă˘â€ â€™ przeÄąâ€šÄ…czanie stanu; skrĂłt klawiszowy mapuj w `@onSetup` lub Lua.

<div id="ch-18-5"></div>
## 18.5 Blueprinty OTUI (STRICT)
**Kwadratowy CheckBox**
`$fenceInfo
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

**RoundCheckBox (okrÄ…gÄąâ€šy)**
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš Dzieci wewnÄ…trz CheckBox. Ă˘ĹĄĹš Brak `tr()` w etykiecie. Ă˘ĹĄĹš Zbyt maÄąâ€šy rozmiar pola (<16Ä‚â€”16). Ă˘ĹĄĹš NiespĂłjne kotwice. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak kursora â€žpointerâ€ť. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Nieparzyste marginesy/offset.

<div id="ch-18-8"></div>
## 18.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Listy opcji w Panel/GroupBox; pierwszy element z mniejszym marginesem gĂłrnym (`$first`). Tryb globalnego wÄąâ€šÄ…czania/wyÄąâ€šÄ…czania grupy kontrolek.

<div id="ch-18-9"></div>
## 18.9 CheckBox â€” triĂ˘â‚¬â€state i offset etykiety
- **TriĂ˘â‚¬â€state (opcjonalnie)**: jeÄąÄ˝eli projekt wymaga stanu â€žnieokreÄąâ€şlonyâ€ť, zdefiniuj stan logiczny (np. `$indeterminate`) i nadaj mu wÄąâ€šasnÄ… ikonÄ™/tÄąâ€šo; przeÄąâ€šÄ…czanie cykliczne: `unchecked Ă˘â€ â€™ checked Ă˘â€ â€™ indeterminate`.  
- **Offset etykiety**: utrzymuj `text-offset` tak, by tekst nie nachodziÄąâ€š na pole (np. Ă˘â€°Ä„18 px przy polu 16Ä‚â€”16).

**PrzykÄąâ€šad (STRICT)**
`$fenceInfo
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
- [19.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci tekstowe](#ch-19-2)
- [19.3 Geometria i styl](#ch-19-3)
- [19.4 Scroll pairing (Multiline)](#ch-19-4)
- [19.5 Stany i zdarzenia](#ch-19-5)
- [19.6 Blueprinty OTUI (STRICT)](#ch-19-6)
- [19.7 Presety TS](#ch-19-7)
- [19.8 Walidator](#ch-19-8)
- [19.9 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-19-9)
- [19.10 TextEdit/Multiline â€” IME, paste i filtry wejÄąâ€şcia](#ch-19-10)
- [19.11 Multiline â€” zaznaczenie, lineĂ˘â‚¬â€height i pixelsĂ˘â‚¬â€scroll](#ch-19-11)

<div id="ch-19-1"></div>
## 19.1 Rola i struktura
- **TextEdit** â€” jednoĂ˘â‚¬â€wierszowe pole tekstowe.  
- **PasswordTextEdit** â€” jak TextEdit, ale treÄąâ€şÄ‡ maskowana.  
- **MultilineTextEdit** â€” wielowierszowe z obsÄąâ€šugÄ… zawijania i przewijania.

<div id="ch-19-2"></div>
## 19.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci tekstowe
- `placeholder: '...'` oraz `placeholder-color: #AARRGGBB` â€” tekst i kolor placeholdera.  
- `text-wrap: true|false` â€” zawijanie (dot. Multiline).  
- `font`, `color` â€” styl tekstu.

<div id="ch-19-3"></div>
## 19.3 Geometria i styl
- Kotwicz do dostÄ™pnego obszaru; przy Multiline: zapewnij wysokoÄąâ€şÄ‡ i padding.  
- Parzyste marginesy; tÄąâ€šo transparentne lub panelowe.

<div id="ch-19-4"></div>
## 19.4 Scroll pairing (Multiline)
- **VerticalScrollBar** jako **sibling**.  
- W Multiline ustaw: `vertical-scrollbar: <idScrolla>`.  
- Kotwice: Multiline `left/top/bottom` do parenta, `right` do `scroll.left`; Scroll `right/top/bottom` do parenta.  
- `step` scrolla dopasuj do wysokoÄąâ€şci wiersza (np. 16) i uÄąÄ˝yj `pixels-scroll: true` gdy wymagane.

<div id="ch-19-5"></div>
## 19.5 Stany i zdarzenia
- `@onEnter` (zatwierdzenie w TextEdit), `@onEscape` (anulowanie), `@onSetup` (bindy).  
- Fokus klawiatury na wejÄąâ€şciu; kontroler moÄąÄ˝e zarzÄ…dzaÄ‡ przeÄąâ€šÄ…czaniem fokusu.

<div id="ch-19-6"></div>
## 19.6 Blueprinty OTUI (STRICT)
**TextEdit (placeholder)**
`$fenceInfo
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
`$fenceInfo
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
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš `vertical-scrollbar` wskazuje nieistniejÄ…cy `id`. Ă˘ĹĄĹš ScrollBar jako dziecko MultilineTextEdit. Ă˘ĹĄĹš Sprzeczne kotwice (fill + krawÄ™dzie). Ă˘ĹĄĹš Brak placeholdera tam, gdzie wymagany UXĂ˘â‚¬â€owo. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Zbyt maÄąâ€ša wysokoÄąâ€şÄ‡ w Multiline. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak `pixels-scroll` dla precyzyjnego przewijania.

<div id="ch-19-9"></div>
## 19.9 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Pole loginu z placeholderem i Password z maskowaniem; edytor logĂłw z Multiline + scroll i `text-wrap: true`; walidacja Enter/Escape w kontrolerze.

<div id="ch-19-10"></div>
## 19.10 TextEdit/Multiline â€” IME, paste i filtry wejÄąâ€şcia
- **IME**: pola powinny poprawnie akceptowaÄ‡ kompozycjÄ™ IME; nie nadpisuj w kontrolerze zdarzeÄąâ€ž, ktĂłre przerywajÄ… kompozycjÄ™.  
- **Paste**: obsÄąâ€šuÄąÄ˝ `Ctrl+V`/`Shift+Insert`; opcjonalne czyszczenie wklejanego tekstu (np. biaÄąâ€ša lista znakĂłw).  
- **Filtry**: waliduj w kontrolerze (regex, max dÄąâ€šugoÄąâ€şÄ‡) â€” bez modyfikowania `.otui`.

<div id="ch-19-11"></div>
## 19.11 Multiline â€” zaznaczenie, lineĂ˘â‚¬â€height i pixelsĂ˘â‚¬â€scroll
- **Selection**: zapewnij widoczny kolor zaznaczenia zgodny z motywem.  
- **LineĂ˘â‚¬â€height**: dopasuj przewijanie do metryk fontu; `step` scrollbar'a Ă˘â€°Â wysokoÄąâ€şÄ‡ linii (np. 16).  
- **pixelsĂ˘â‚¬â€scroll**: wÄąâ€šÄ…cz dla precyzyjnych edytorĂłw (logi/kod) â€” pÄąâ€šynne przewijanie bez â€žskokĂłwâ€ť.

---
## 20. ComboBox
- [20.1 Rola i struktura](#ch-20-1)
- [20.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci i menu](#ch-20-2)
- [20.3 Geometria i styl](#ch-20-3)
- [20.4 Zdarzenia i stany](#ch-20-4)
- [20.5 Blueprint OTUI (STRICT)](#ch-20-5)
- [20.6 Presety TS](#ch-20-6)
- [20.7 Walidator](#ch-20-7)
- [20.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-20-8)

<div id="ch-20-1"></div>
## 20.1 Rola i struktura
**ComboBox** to selektor pojedynczej opcji. Posiada **wewnÄ™trzne menu** (lista opcji) zarzÄ…dzane przez klienta â€” **nie dodawaj** rÄ™cznie dzieci w `.otui`.

<div id="ch-20-2"></div>
## 20.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci i menu
- `current-index: N` lub `current-text: '...'` â€” wybrana pozycja (jedno ÄąĹźrĂłdÄąâ€šo prawdy w czasie eksportu).
- `menu-height: H` â€” maksymalna wysokoÄąâ€şÄ‡ rozwiniÄ™tego menu (px).
- `menu-scroll-step: S` â€” krok przewijania menu (px).
- `placeholder: '...'` â€” tekst gdy nic nie wybrano.
- Teksty opcji przechodzÄ… przez mechanizm tÄąâ€šumaczeÄąâ€ž na poziomie logiki (nie dodawaj jako dzieci w OTUI).

<div id="ch-20-3"></div>
## 20.3 Geometria i styl
- SzerokoÄąâ€şÄ‡ staÄąâ€ša lub `anchors.left/right: parent`.  
- Minimalna wysokoÄąâ€şÄ‡ ~20 px.  
- TÄąâ€šo zgodne z motywem; strzaÄąâ€ška rozwijania po prawej (render klienta/skinu).

<div id="ch-20-4"></div>
## 20.4 Zdarzenia i stany
- `@onOptionChange: Controller.fn(index, text)` â€” zmiana wyboru.  
- `$focus` â€” podÄąâ€şwietlenie fokusowanej kontrolki.  
- `$disabled` â€” wyglÄ…d nieaktywny.

<div id="ch-20-5"></div>
## 20.5 Blueprint OTUI (STRICT)
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš Dzieci â€žopcjiâ€ť dodane rÄ™cznie do ComboBox w `.otui`. Ă˘ĹĄĹš Sprzeczne kotwice (`fill` + krawÄ™dzie). Ă˘ĹĄĹš Brak wysokoÄąâ€şci. Ă˘ĹˇÂ ÄŹÂ¸Ĺą `menu-height` zbyt maÄąâ€še dla przewijania. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak mapowania `onOptionChange` w projekcie.

<div id="ch-20-8"></div>
## 20.8 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Selektor postaci; filtr w narzÄ™dziowym MiniWindow; zmiana dostÄ™pnoÄąâ€şci (`$disabled`) przy braku danych; placeholder gdy brak wyboru.

---
## 21. ProgressBar
- [21.1 Rola i zakres](#ch-21-1)
- [21.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci i styl](#ch-21-2)
- [21.3 Geometria](#ch-21-3)
- [21.4 Blueprint OTUI (STRICT)](#ch-21-4)
- [21.5 Presety TS](#ch-21-5)
- [21.6 Walidator](#ch-21-6)
- [21.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-21-7)

<div id="ch-21-1"></div>
## 21.1 Rola i zakres
**ProgressBar** prezentuje postÄ™p w zakresie. **Nie** posiada dzieci â€” jeÄąâ€şli potrzebujesz opisu, uÄąÄ˝yj zewnÄ™trznego `Label`.

<div id="ch-21-2"></div>
## 21.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci i styl
- `minimum: 0`, `maximum: 100`, `value: 0..100`.  
- Warianty skĂłrek: kolor tÄąâ€ša i wypeÄąâ€šnienia; opcjonalne â€žgradientyâ€ť (jeÄąâ€şli motyw wspiera).  
- MoÄąÄ˝liwy tryb indeterminate (projektowy) â€” sygnalizowany animacjÄ… po stronie klienta.

<div id="ch-21-3"></div>
## 21.3 Geometria
- Kotwicz w poziomie do rodzica; wysokoÄąâ€şÄ‡ ~14â€“18 px.  
- Parzyste marginesy; zachowaj minĂ˘â‚¬â€width dla czytelnoÄąâ€şci.

<div id="ch-21-4"></div>
## 21.4 Blueprint OTUI (STRICT)
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš Dzieci wewnÄ…trz ProgressBar. Ă˘ĹĄĹš `value` poza zakresem `minimum..maximum`. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Zbyt maÄąâ€ša wysokoÄąâ€şÄ‡. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak kotwic w poziomie (sÄąâ€šaba czytelnoÄąâ€şÄ‡).

<div id="ch-21-7"></div>
## 21.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Status w `StaticMainWindow`; pasek Äąâ€šadowania w panelu z etykietÄ… obok (`Label`). Tryb â€žnieokreÄąâ€şlonyâ€ť w overlay statusu.

---
## 22. ScrollBar (Vertical/Horizontal)
- [22.1 Rola i parowanie](#ch-22-1)
- [22.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci](#ch-22-2)
- [22.3 Geometria i dokowanie](#ch-22-3)
- [22.4 Blueprinty OTUI (STRICT)](#ch-22-4)
- [22.5 Presety TS](#ch-22-5)
- [22.6 Walidator](#ch-22-6)
- [22.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-22-7)

<div id="ch-22-1"></div>
## 22.1 Rola i parowanie
**ScrollBar** jest **rodzeÄąâ€žstwem** przewijanej treÄąâ€şci (lista/Multiline). Parowany poprzez dokowanie i kotwice treÄąâ€şci do krawÄ™dzi scrolla.

<div id="ch-22-2"></div>
## 22.2 WÄąâ€šaÄąâ€şciwoÄąâ€şci
- `step: N` â€” skok przewijania (px, dostosuj do wysokoÄąâ€şci wiersza/slotu).  
- `pixels-scroll: true|false` â€” tryb przewijania pikselowego.  
- (Opcj.) `minimum/maximum/value` â€” gdy scroll sterowany programowo (projektowo).

<div id="ch-22-3"></div>
## 22.3 Geometria i dokowanie
- **Vertical**: `anchors.right/top/bottom: parent`; przewijana treÄąâ€şÄ‡: `right: scroll.left`.  
- **Horizontal**: `anchors.left/right/bottom: parent`; przewijana treÄąâ€şÄ‡: `bottom: hscroll.top`.  
- SzerokoÄąâ€şÄ‡ (V) ~12â€“16 px; wysokoÄąâ€şÄ‡ (H) ~12â€“16 px. Parzyste marginesy.

<div id="ch-22-4"></div>
## 22.4 Blueprinty OTUI (STRICT)
**VerticalScrollBar**
`$fenceInfo
VerticalScrollBar
  id: scroll
  anchors.right: parent.right
  anchors.top: parent.top
  anchors.bottom: parent.bottom
  step: 16
  pixels-scroll: true
```

**HorizontalScrollBar**
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš ScrollBar jako dziecko listy/Multiline. Ă˘ĹĄĹš Brak parowania (treÄąâ€şÄ‡ nie kotwiczy siÄ™ do scrolla). Ă˘ĹĄĹš `step` niedopasowany do rozmiaru wiersza (szarpane przewijanie). Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak `pixels-scroll` przy drobnym tekÄąâ€şcie.

<div id="ch-22-7"></div>
## 22.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Lista z wierszem 18 px Ă˘â€ â€™ `step: 18`; edytor tekstu z delikatnym przewijaniem (`pixels-scroll: true`); ukÄąâ€šad podwĂłjny (V+H) w panelu z danymi tabelarycznymi.

---
## 23. HorizontalSeparator
- [23.1 Rola i ograniczenia](#ch-23-1)
- [23.2 Geometria i styl](#ch-23-2)
- [23.3 Blueprint OTUI (STRICT)](#ch-23-3)
- [23.4 Preset TS](#ch-23-4)
- [23.5 Walidator](#ch-23-5)
- [23.6 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-23-6)

<div id="ch-23-1"></div>
## 23.1 Rola i ograniczenia
**HorizontalSeparator** to cienka linia dzielÄ…ca sekcje. **Nie posiada dzieci** i nie jest interaktywny.

<div id="ch-23-2"></div>
## 23.2 Geometria i styl
- Kotwice: najczÄ™Äąâ€şciej `left/right: parent`, wysokoÄąâ€şÄ‡ `1` lub `2` px.  
- Marginesy: parzyste `margin-top/bottom` dla rytmu layoutu.  
- Styl: `background-color` (przezroczystoÄąâ€şÄ‡ mile widziana).

<div id="ch-23-3"></div>
## 23.3 Blueprint OTUI (STRICT)
`$fenceInfo
HorizontalSeparator
  id: sep
  anchors.left: parent.left
  anchors.right: parent.right
  height: 1
  background-color: #ffffff33
```

<div id="ch-23-4"></div>
## 23.4 Preset TS
`$fenceInfo
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
Ă˘ĹĄĹš Dzieci w separatorze. Ă˘ĹˇÂ ÄŹÂ¸Ĺą WysokoÄąâ€şÄ‡ > 2 px bez uzasadnienia stylistycznego. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Nieparzyste marginesy.

<div id="ch-23-6"></div>
## 23.6 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Separator pod nagÄąâ€šĂłwkiem GroupBox; cienka linia w Toolbarze miÄ™dzy grupami akcji.

---
## 24. StatusOverlay
- [24.1 Rola i struktura](#ch-24-1)
- [24.2 Geometria i styl](#ch-24-2)
- [24.3 Stany i zdarzenia](#ch-24-3)
- [24.4 Blueprint OTUI (STRICT)](#ch-24-4)
- [24.5 Preset TS](#ch-24-5)
- [24.6 Walidator](#ch-24-6)
- [24.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-24-7)

<div id="ch-24-1"></div>
## 24.1 Rola i struktura
**StatusOverlay** to lekka warstwa informacyjna nad treÄąâ€şciÄ…. Typowo: `Label` (komunikat), opcj. `ProgressBar`, opcj. `Button` Cancel.

<div id="ch-24-2"></div>
## 24.2 Geometria i styl
- Overlay kotwiczy siÄ™ do caÄąâ€šego rodzica: `anchors.fill: parent`.  
- TÄąâ€šo pĂłÄąâ€šprzezroczyste (np. `#00000055`) lub `alpha`.  
- Kafelek Äąâ€şrodka (panel) wycentrowany pion/poziom przez `anchors.centerIn: parent` lub rĂłwnowaÄąÄ˝ne kotwice.

<div id="ch-24-3"></div>
## 24.3 Stany i zdarzenia
- `@onClick` przy Cancel.  
- WidocznoÄąâ€şÄ‡ sterowana przez kontroler (show/hide).  
- Brak zÄąâ€šoÄąÄ˝onych dzieci â€” overlay jest lekki.

<div id="ch-24-4"></div>
## 24.4 Blueprint OTUI (STRICT)
`$fenceInfo
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
`$fenceInfo
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
Ă˘ĹĄĹš Overlay z nadmiarem dzieci (zÄąâ€šoÄąÄ˝one ukÄąâ€šady). Ă˘ĹĄĹš Brak `tr()` w komunikacie. Ă˘ĹˇÂ ÄŹÂ¸Ĺą Brak kontrastu (czytelnoÄąâ€şÄ‡). Ă˘ĹˇÂ ÄŹÂ¸Ĺą Panel bez wyÄąâ€şrodkowania.

<div id="ch-24-7"></div>
## 24.7 PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
Overlay Äąâ€šadowania zasobĂłw; tryb indeterminate ProgressBar; anulowanie dÄąâ€šugiej operacji.

---
## 25. Macierze dozwolonych dzieci (global)
- [25.1 Tabele macierzowe per komponent i slot](#ch-25-1)
- [25.2 ReguÄąâ€šy globalne](#ch-25-2)

<div id="ch-25-1"></div>
## 25.1 Tabele macierzowe per komponent i slot
| Parent/Slot | Dopuszczone dzieci | Niedozwolone / Uwagi |
|---|---|---|
| **MainWindow/StaticMainWindow** | elementy panelowe (Label, Button, TextEdit, Multiline, TextList, ComboBox, CheckBox, ProgressBar, VerticalScrollBar, HorizontalSeparator, TabBar, Splitter, UIWidget, Panel) | `*Window` jako dzieci â€” Ă˘Ĺ›â€“ |
| **MiniWindow.titlebar** | Label, Button, UIWidget (ikona) | Scroll, listy, edytory â€” Ă˘Ĺ›â€“ |
| **MiniWindow.content** | elementy panelowe (w tym TextList/Multiline, Panel, Grid, ProgressBar) | `*Window` â€” Ă˘Ĺ›â€“; Scroll tylko w parze |
| **MiniWindow.footer** | Button, Label | Listy/edytory â€” Ă˘Ĺ›â€“ |
| **ContainerWindow.titlebar** | Button (back/pin/min/close), Label, UIWidget (ikona) | Scroll/listy/edytory â€” Ă˘Ĺ›â€“ |
| **ContainerWindow.content** | SlotWidget/UIWidget, Label, Button, VerticalScrollBar (dock right) | `*Window` â€” Ă˘Ĺ›â€“ |
| **DialogWindow.titlebar** | Label | Scroll/listy/edytory â€” Ă˘Ĺ›â€“ |
| **DialogWindow.content** | Label, TextEdit, Multiline, ComboBox, CheckBox, ProgressBar | `*Window` â€” Ă˘Ĺ›â€“ |
| **DialogWindow.footer** | Button | â€” |
| **Panel/GroupBox/UIWidget** | elementy panelowe | `*Window` â€” Ă˘Ĺ›â€“ |
| **TabBar** | Button (zakÄąâ€šadki) | TreÄąâ€şci panelowe w TabBar â€” Ă˘Ĺ›â€“ |
| **TabContent** | elementy panelowe | â€” |
| **Splitter** | dokÄąâ€šadnie 2 panele (UIWidget/Panel) | Ă˘â€°Â 2 dzieci â€” Ă˘Ĺ›â€“ |
| **TextList** | wiersze (UIWidget/ListRow) | Scroll jako **sibling** |
| **MultilineTextEdit** | â€” | Scroll jako **sibling** |
| **ComboBox** | â€” (menu wewnÄ™trzne) | RÄ™czne â€žopcjeâ€ť â€” Ă˘Ĺ›â€“ |
| **ProgressBar** | â€” | Brak dzieci |
| **HorizontalSeparator** | â€” | Brak dzieci |
| **StatusOverlay** | Label, ProgressBar, Button (Cancel) | ZÄąâ€šoÄąÄ˝one ukÄąâ€šady â€” Ă˘Ĺ›â€“ |

<div id="ch-25-2"></div>
## 25.2 ReguÄąâ€šy globalne
- ScrollBar zawsze **sibling** przewijanej treÄąâ€şci.  
- `*Window` nigdy **nie** jest dzieckiem innego okna w slotach treÄąâ€şci.  
- `titlebar/footer` to obszary **bez** list/edytorĂłw/scrolla.  
- Parzyste marginesy i spacing; snapping 2 px.  
- Wymuszone przyciski w oknach: MiniWindow (min/close), Container (back + min/close), Dialog (OK/Cancel w footerze).  
- Wszystkie napisy przez `tr()`; zasoby tylko z `data/`.

---
## 26. Walidacja i autoĂ˘â‚¬â€naprawy (global)
- [26.1 BÄąâ€šÄ™dy blokujÄ…ce](#ch-26-1)
- [26.2 OstrzeÄąÄ˝enia](#ch-26-2)
- [26.3 AutoĂ˘â‚¬â€naprawy deterministyczne](#ch-26-3)
- [26.4 Pipeline walidatora](#ch-26-4)

<div id="ch-26-1"></div>
## 26.1 BÄąâ€šÄ™dy blokujÄ…ce (Ă˘ĹĄĹš)
- STRICT: komentarze, taby, CRLF/BOM, zÄąâ€še wciÄ™cia (Ă˘â€°Â 2 sp.), kolejnoÄąâ€şÄ‡ atrybutĂłw niekanoniczna.  
- Sprzeczne kotwice (`fill` + krawÄ™dzie).  
- Niedozwolone dzieci w slotach/parentach.  
- Samotny ScrollBar lub przewijana treÄąâ€şÄ‡ bez pary i dokowania.  
- Brak wymaganych przyciskĂłw okna (Mini/Container/Dialog).  
- `tr()` pominiÄ™te dla staÄąâ€šych napisĂłw; zasoby spoza `data/`.

<div id="ch-26-2"></div>
## 26.2 OstrzeÄąÄ˝enia (Ă˘ĹˇÂ ÄŹÂ¸Ĺą)
- Nieparzyste marginesy/spacing.  
- Brak autoĂ˘â‚¬â€fit width przy dokowaniu okna.  
- `step` scrolla niepasujÄ…cy do wysokoÄąâ€şci wiersza/slotu.  
- Brak skrĂłtĂłw Enter/Escape/strzaÄąâ€šek tam, gdzie UX tego wymaga.

<div id="ch-26-3"></div>
## 26.3 AutoĂ˘â‚¬â€naprawy deterministyczne
1) Normalizacja koÄąâ€žcĂłw linii na LF, usuniÄ™cie BOM/tabĂłw/trailing spaces.  
2) WciÄ™cia Ă˘â€ â€™ 2 sp.  
3) PorzÄ…dkowanie atrybutĂłw: **GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE**.  
4) Wstawienie brakujÄ…cych slotĂłw (np. `content/footer` w MiniWindow).  
5) Parowanie ScrollBar z listÄ…/Multiline (dokowanie + kotwice).  
6) UsuniÄ™cie `width` gdy istnieje `anchors.left/right: parent` (autoĂ˘â‚¬â€fit).  
7) Snapping marginesĂłw/spacing do wartoÄąâ€şci parzystych.

<div id="ch-26-4"></div>
## 26.4 Pipeline walidatora
`$fenceInfo
parse Ă˘â€ â€™ normalize(STRICT) Ă˘â€ â€™ validateStructure(macierze) Ă˘â€ â€™ validateAnchors Ă˘â€ â€™ validateI18n Ă˘â€ â€™ validateResources Ă˘â€ â€™ validatePairs(scroll) Ă˘â€ â€™ autofix Ă˘â€ â€™ reĂ˘â‚¬â€serialize Ă˘â€ â€™ diff
```
Wynik: `{ errors: [...], warnings: [...], fixes: [...] }` + zaktualizowany dokument.

---
## 27. Parser/Serializer OTUI Ă˘â€ â€™ AST (TypeScript)
- [27.1 Tokenizacja i INDENT/DEDENT](#ch-27-1)
- [27.2 KsztaÄąâ€št AST](#ch-27-2)
- [27.3 Algorytm parsowania](#ch-27-3)
- [27.4 Serializacja i `ensureStrictOtui()`](#ch-27-4)
- [27.5 BÄąâ€šÄ™dy/ostrzeÄąÄ˝enia/pozycje](#ch-27-5)
- [27.6 Testy roundĂ˘â‚¬â€trip (goldeny)](#ch-27-6)

<div id="ch-27-1"></div>
## 27.1 Tokenizacja i INDENT/DEDENT
Tokeny: `IDENT`, `NUMBER`, `STRING` (pojedyncze `'...'` dla `!text`), `SYMBOL` (`:`, `<`, `>`, `$`, `@`, `&`), `NEWLINE`, `INDENT`, `DEDENT`. WciÄ™cie = **2 spacje**.

<div id="ch-27-2"></div>
## 27.2 KsztaÄąâ€št AST
`$fenceInfo
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
1) Liniowo skanuj, budujÄ…c stos INDENT/DEDENT.  
2) Linia `X < Y` Ă˘â€ â€™ wÄ™zeÄąâ€š `Widget` z dziedziczeniem.  
3) Linia `key: value` Ă˘â€ â€™ `Prop` (wÄąâ€šaÄąâ€şciwoÄąâ€şci GEOMETRIA/STYL/ZACHOWANIE).  
4) Blok `@on...:` Ă˘â€ â€™ `Event`; blok `$...:` Ă˘â€ â€™ `State`; blok `&name:` Ă˘â€ â€™ `MetaFn`.  
5) DoÄąâ€šÄ…czaj dzieci wg wciÄ™Ä‡; zachowuj `loc` do raportĂłw.

<div id="ch-27-4"></div>
## 27.4 Serializacja i `ensureStrictOtui()`
- Emisja w kolejnoÄąâ€şci **GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE**.  
- `style.text` Ă˘â€ â€™ `!text: tr('...')`; zdarzenia Ă˘â€ â€™ `@on...`; stany Ă˘â€ â€™ `$...`.  
- `ensureStrictOtui(text)` usuwa BOM/taby, normalizuje LF, wciÄ™cia (2 sp.), atrybuty i kolejnoÄąâ€şÄ‡ blokĂłw.

<div id="ch-27-5"></div>
## 27.5 BÄąâ€šÄ™dy/ostrzeÄąÄ˝enia/pozycje
Struktura raportu:
`$fenceInfo
export type LintIssue = { kind: 'error'|'warning'; code: string; message: string; loc?: { line: number; col: number } };
```
PrzykÄąâ€šady: `E_STRICT_TABS`, `E_SLOT_CHILD_FORBIDDEN`, `E_ANCHORS_CONFLICT`, `E_SCROLL_PAIR_MISSING`, `W_MARGIN_ODD`.

<div id="ch-27-6"></div>
## 27.6 Testy roundĂ˘â‚¬â€trip (goldeny)
- Dla **MiniWindow**, **ContainerWindow**, **Dialog**: `parse Ă˘â€ â€™ serialize Ă˘â€ â€™ parse` i porĂłwnanie AST (bez strat).  
- Testy porzÄ…dkowania atrybutĂłw, stanĂłw i zdarzeÄąâ€ž; testy autoĂ˘â‚¬â€napraw (deterministyczny diff).

---
## 28. Import/Export i roundĂ˘â‚¬â€trip (edytor Ă˘â€ â€ť plik Ă˘â€ â€ť Lua)
- [28.1 Import z `.otui`](#ch-28-1)
- [28.2 Import z blokĂłw w Lua (`@OTUI_BEGIN/END`)](#ch-28-2)
- [28.3 Eksport do `.otui` + aktualizacja bloku w Lua](#ch-28-3)
- [28.4 Runtime: tylko pliki](#ch-28-4)

<div id="ch-28-1"></div>
## 28.1 Import z `.otui`
- Wczytaj plik, `ensureStrictOtui()`, `parseOtui()` Ă˘â€ â€™ AST.  
- Walidacja + autoĂ˘â‚¬â€naprawy; prezentacja ostrzeÄąÄ˝eÄąâ€ž przed edycjÄ….

<div id="ch-28-2"></div>
## 28.2 Import z blokĂłw w Lua (`@OTUI_BEGIN/END`)
W kodzie Lua przechowuj **czysty STRICT OTUI** w stringu wielowierszowym, a **markery** trzymaj poza stringiem:
`$fenceInfo
-- @OTUI_BEGIN miniwindow
local UI = [[
MiniWindow
  id: miniWindow
  width: 200
]]
-- @OTUI_END miniwindow
```
Edytor odnajduje sekcjÄ™ po nazwie, wycina **dokÄąâ€šadnie** zawartoÄąâ€şÄ‡ stringa i traktuje jÄ… jak `.otui`.

<div id="ch-28-3"></div>
## 28.3 Eksport do `.otui` + aktualizacja bloku w Lua
- Serializuj do pliku `.otui` (kanoniczny zapis).  
- JeÄąâ€şli w Lua istnieje sekcja `@OTUI_BEGIN/END`, **zastÄ…p** wyÄąâ€šÄ…cznie Äąâ€şrodek stringa nowym STRICT OTUI (bez zmiany markerĂłw i otaczajÄ…cego kodu).  
- Generuj stub `local win = g_ui.displayUI('file')` do uÄąÄ˝ycia w runtime.

<div id="ch-28-4"></div>
## 28.4 Runtime: tylko pliki
W OTClient v8 UI jest Äąâ€šadowane kanonicznie z plikĂłw: `g_ui.displayUI('...')`. Import/edycja â€žfrom stringâ€ť sÄąâ€šuÄąÄ˝y **wyÄąâ€šÄ…cznie** edytorowi i utrzymaniu kodu â€” nie do produkcyjnego Äąâ€šadowania w kliencie.

---
## 29. Biblioteka presetĂłw (gotowe szablony)
- [29.1 Presety okien](#ch-29-1)
- [29.2 Presety komponentĂłw](#ch-29-2)
- [29.3 Warianty tematyczne](#ch-29-3)
- [29.4 Rejestr presetĂłw i wersjonowanie](#ch-29-4)
- [29.5 Zasady rozszerzania](#ch-29-5)

<div id="ch-29-1"></div>
## 29.1 Presety okien
**Preset: MinimalMiniWindow**
`$fenceInfo
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
`$fenceInfo
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
`$fenceInfo
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
## 29.2 Presety komponentĂłw
**TitlebarTool**
`$fenceInfo
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
`$fenceInfo
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
`$fenceInfo
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
- **NarzÄ™dzie**: tÄąâ€ša pĂłÄąâ€šprzezroczyste, kompaktowe wysokoÄąâ€şci (20 px titlebar/toolbar), marginesy 6 px.  
- **Kontener**: widoczne przyciski `back/pin`, spacing slotĂłw 4 px, slot 36Ä‚â€”36.  
- **Dialog**: padding 8 px, przyciski 72 px, wysokoÄąâ€şÄ‡ 32 px w footer.

<div id="ch-29-4"></div>
## 29.4 Rejestr presetĂłw i wersjonowanie
- **Registry (TS)** trzyma wpisy: `id`, `title`, `base`, `version`, `factory()`.  
- Stabilne **slugĂ˘â‚¬â€i** presetĂłw (np. `mini/minimal`, `container/loot`, `dialog/confirm`).  
- Zmiany Äąâ€šamiÄ…ce Ă˘â€ â€™ nowy `version`, poprzedni nadal dostÄ™pny.

`$fenceInfo
export type PresetEntry = { id: string; version: string; title: string; factory: () => WidgetNode|WidgetNode[] };
export const PRESETS: PresetEntry[] = [
  { id: 'mini/minimal', version: '1.0.0', title: 'Minimal MiniWindow', factory: presetMiniMinimal },
  { id: 'container/loot', version: '1.0.0', title: 'Container Loot', factory: presetContainerLoot },
  { id: 'dialog/confirm', version: '1.0.0', title: 'Confirm Dialog', factory: presetDialogConfirm }
];
```

<div id="ch-29-5"></div>
## 29.5 Zasady rozszerzania
- Rozszerzaj przez **dziedziczenie** (`X < Y`) lub przez preset TS, nigdy przez adĂ˘â‚¬â€hoc dzieci naruszajÄ…ce macierze.  
- Zachowuj STRICT OTUI przy eksporcie; nie duplikuj semantyki okna w stanach.

---
## 30. Testy wizualne i regresja
- [30.1 Snapshoty 1:1](#ch-30-1)
- [30.2 DPI / font metrics / skalowanie](#ch-30-2)
- [30.3 DostÄ™pnoÄąâ€şÄ‡ (kontrast, czytelnoÄąâ€şÄ‡)](#ch-30-3)
- [30.4 Golden diff i tolerancje](#ch-30-4)
- [30.5 Pipeline testĂłw](#ch-30-5)

<div id="ch-30-1"></div>
## 30.1 Snapshoty 1:1
- Generuj obraz referencyjny dla kaÄąÄ˝dego preset/blueprintu po eksporcie `.otui`.  
- PorĂłwnuj pikselĂ˘â‚¬â€poĂ˘â‚¬â€pikselu z goldenem; rozbijaj rĂłÄąÄ˝nice na heatmapÄ™.

<div id="ch-30-2"></div>
## 30.2 DPI / font metrics / skalowanie
- Testuj na staÄąâ€šych DPI (np. 96) oraz wariantach skali (1.0, 1.25, 1.5).  
- Weryfikuj metryki fontu: wysokoÄąâ€şÄ‡ linii, kerning; nie dopuszczaj driftu miÄ™dzy wersjami.

<div id="ch-30-3"></div>
## 30.3 DostÄ™pnoÄąâ€şÄ‡ (kontrast, czytelnoÄąâ€şÄ‡)
- Sprawdzaj minimalne kontrasty tekst/tÄąâ€šo.  
- Minimalne rozmiary hitboxĂłw (Ă˘â€°Ä„16Ä‚â€”16).  
- Zawijanie i elipsyzacja dÄąâ€šugich tekstĂłw.

<div id="ch-30-4"></div>
## 30.4 Golden diff i tolerancje
- Tolerancja szumu renderera Ă˘â€°Â¤0.5% pikseli.  
- KaÄąÄ˝da rĂłÄąÄ˝nica > tolerancji wymaga akceptacji lub rollbacku presetĂłw/stylĂłw.

<div id="ch-30-5"></div>
## 30.5 Pipeline testĂłw
`$fenceInfo
for each preset Ă˘â€ â€™ serialize(STRICT) Ă˘â€ â€™ export .otui Ă˘â€ â€™ render snapshot Ă˘â€ â€™ compare with golden Ă˘â€ â€™ report
```
Raport: lista rĂłÄąÄ˝nic, heatmapy, log walidatora (STRUCT/anchors/macierze).

---
## 31. SÄąâ€šownik i indeks
- [31.1 SÄąâ€šownik (Aâ€“Z)](#ch-31-1)
- [31.2 Indeks rozdziaÄąâ€šĂłw](#ch-31-2)

<div id="ch-31-1"></div>
## 31.1 SÄąâ€šownik (Aâ€“Z)
- **Anchors** â€” kotwice poÄąâ€šoÄąÄ˝enia i rozmiaru wzglÄ™dem krawÄ™dzi/obiektĂłw.  
- **AST** â€” abstrakcyjne drzewo skÄąâ€šadniowe reprezentujÄ…ce OTUI w edytorze.  
- **Blueprint** â€” kanoniczny szablon OTUI komponentu/okna.  
- **Grid (edytorowy)** â€” siatka pomocnicza w edytorze, nie istnieje w OTUI.  
- **LayoutĂ˘â‚¬â€owner** â€” rodzic definiujÄ…cy sloty/obszary i reguÄąâ€šy dokowania.  
- **Macierz dzieci** â€” tabela dozwolonych dzieci per parent/slot.  
- **Preset** â€” gotowy zestaw wÄ™zÄąâ€šĂłw przygotowanych do uÄąÄ˝ycia jako wzorzec.  
- **RoundĂ˘â‚¬â€trip** â€” import Ă˘â€ â€™ edycja Ă˘â€ â€™ eksport bez utraty semantyki.  
- **Scroll pairing** â€” reguÄąâ€šy Äąâ€šÄ…czenia treÄąâ€şci przewijanej ze ScrollBarem jako rodzeÄąâ€žstwem.  
- **STRICT OTUI** â€” format: LF, 2 spacje, brak komentarzy/tabĂłw, kolejnoÄąâ€şÄ‡ atrybutĂłw.

<div id="ch-31-2"></div>
## 31.2 Indeks rozdziaÄąâ€šĂłw
- **Okna**: 5â€“9  
- **Organizacja**: 10â€“14  
- **Dane/edycja**: 15â€“20  
- **WskaÄąĹźniki/scroll**: 21â€“22  
- **Warstwy i separatory**: 23â€“24  
- **ReguÄąâ€šy i walidacja**: 25â€“26  
- **AST/IO**: 27â€“28  
- **Presety**: 29  
- **Testy**: 30  
- **SÄąâ€šownik**: 31

---



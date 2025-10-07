# **Pakiet:** `otc_core_v1/engine` Ă‚Â· **Wersja:** 1.0   
**Cel:** Jednolita, operacyjna specyfikacja **parsera/serializera OTUI (STRICT)**, **walidatora** i **macierzy dozwolonych dzieci**. Dokument jest fundamentem dla edytora TS (Sparky) oraz testÄ‚Ĺ‚w roundĂ˘â‚¬â€trip.

---
## Spis treÄąâ€şci
- [0. Zakres, definicje, zaÄąâ€šoÄąÄ˝enia](#ch-0)
- [1. STRICT OTUI Ă˘â‚¬â€ť gramatyka i tokenizacja](#ch-1)
- [2. Parser Ă˘â€ â€™ AST (TypeScript)](#ch-2)
- [3. Serializer (AST Ă˘â€ â€™ OTUI STRICT)](#ch-3)
- [4. Macierze dozwolonych dzieci (global)](#ch-4)
  - [4.1 Okna (WindowĂ˘â‚¬â€class)](#ch-4-1)
  - [4.2 Kontenery (ContentĂ˘â‚¬â€class)](#ch-4-2)
  - [4.3 Organizacja/Nawigacja](#ch-4-3)
  - [4.4 Dane/Edycja](#ch-4-4)
  - [4.5 WskaÄąĹźniki/Scroll](#ch-4-5)
- [5. Walidator Ă˘â‚¬â€ť reguÄąâ€šy, kody bÄąâ€šĂ„â„˘dÄ‚Ĺ‚w/ostrzeÄąÄ˝eÄąâ€ž](#ch-5)
- [6. AutoĂ˘â‚¬â€naprawy deterministyczne](#ch-6)
- [7. Import/Export i roundĂ˘â‚¬â€trip (edytor Ă˘â€ â€ť plik Ă˘â€ â€ť Lua)](#ch-7)
- [8. API edytora (TS): parse/serialize/validate/autofix](#ch-8)
- [9. Testy: goldeny i snapshoty](#ch-9)
- [10. PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases](#ch-10)
- [11. Indeks haseÄąâ€š](#ch-11)

---

<div id="ch-0"></div>
## 0. Zakres, definicje, zaÄąâ€šoÄąÄ˝enia
**Interaktywny spis:** [0.1 Zakres](#ch-0-1) Ă‚Â· [0.2 Definicje](#ch-0-2) Ă‚Â· [0.3 ZaÄąâ€šoÄąÄ˝enia projektowe](#ch-0-3)
## 0.1 Zakres {: #ch-0-1 }
- Pokrycie: *caÄąâ€šy pipeline* od tekstu OTUI (STRICT) Ă˘â€ â€ť AST (TS) Ă˘â€ â€ť walidacja Ă˘â€ â€ť autoĂ˘â‚¬â€naprawy Ă˘â€ â€ť eksport/import.  
- Zakres UI: komplet taksonomii z czĂ„â„˘Äąâ€şci Ă˘â‚¬ĹľSpecyfikacja UIĂ˘â‚¬ĹĄ (rozdz. 4) + presety kanoniczne.
## 0.2 Definicje {: #ch-0-2 }
- **STRICT OTUI** Ă˘â‚¬â€ť format bezkomentarzowy, LF, wciĂ„â„˘cia 2 sp., kolejnoÄąâ€şĂ„â€ˇ GEOMETRIAĂ˘â€ â€™STYLĂ˘â€ â€™ZACHOWANIE.
- **AST** Ă˘â‚¬â€ť drzewo `WidgetNode`, deterministyczne klucze i kolejnoÄąâ€şĂ„â€ˇ dzieci.
- **Macierz** Ă˘â‚¬â€ť tablica dozwolonych dzieci dla par (parent, slot).
## 0.3 ZaÄąâ€šoÄąÄ˝enia projektowe {: #ch-0-3 }
- **DeterministycznoÄąâ€şĂ„â€ˇ**: ten sam AST Ă˘â€ â€™ ten sam OTUI (bitĂ˘â‚¬â€identyczny, przy tej samej wersji serializera).  
- **Idempotencja**: `parse(serialize(ast))` Ă˘â€°Ë‡ `normalize(ast)`.
- **Brak magii**: walidator zgÄąâ€šasza i *tylko* przewidywalnie naprawia.

---

<div id="ch-1"></div>
## 1. STRICT OTUI Ă˘â‚¬â€ť gramatyka i tokenizacja
**Interaktywny spis:** [1.1 Zasady formatowania](#ch-1-1) Ă‚Â· [1.2 Tokeny](#ch-1-2) Ă‚Â· [1.3 Szkic EBNF](#ch-1-3)
## 1.1 Zasady formatowania {: #ch-1-1 }
- **WciĂ„â„˘cia**: 2 spacje na poziom. **Zakaz tabÄ‚Ĺ‚w**.  
- **KoÄąâ€žce linii**: LF. **Bez BOM**.  
- **Brak komentarzy** w blokach `.otui`.  
- **KolejnoÄąâ€şĂ„â€ˇ atrybutÄ‚Ĺ‚w** w kaÄąÄ˝dym wĂ„â„˘ÄąĹźle: GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE.
## 1.2 Tokeny {: #ch-1-2 }
- SÄąâ€šowa kluczowe typÄ‚Ĺ‚w: `MainWindow`, `StaticMainWindow`, `MiniWindow`, `ContainerWindow`, `DialogWindow`, `UIWidget`, `Panel`, `GroupBox`, `Titlebar`, `Toolbar`, `TabBar`, `TabWidget`, `Splitter`, `HorizontalSeparator`, `StatusOverlay`, `Label`, `Button`, `CheckBox`, `TextEdit`, `PasswordTextEdit`, `MultilineTextEdit`, `ComboBox`, `TextList`, `ProgressBar`, `VerticalScrollBar`, `HorizontalScrollBar`.
- Operator dziedziczenia: `<` (np. `MiniWindow < MainWindow`).
- Identyfikatory: `id: <slug>`; Äąâ€šaÄąâ€žcuchy w `!text: tr('...')`; liczby caÄąâ€škowite; kolory `#AARRGGBB` lub `alpha`.
## 1.3 Szkic EBNF (pogglĂ„â€¦dowy) {: #ch-1-3 }
```
document     := node*
node         := header NEWLINE indent block?
header       := type (WS '<' WS type)? NEWLINE? attributes?
type         := IDENT
attributes   := (INDENT attr+ DEDENT)?
attr         := key ':' value NEWLINE | stateBlock | event | meta
stateBlock   := '$' IDENT ':' NEWLINE INDENT attr+ DEDENT
event        := '@' IDENT ':' VALUE NEWLINE
meta         := '&' IDENT NEWLINE
block        := INDENT (node | attr)+ DEDENT
key          := IDENT ('.' IDENT)*
value        := NUMBER | STRING | COLOR | IDENT | PATH
```

---

<div id="ch-2"></div>
## 2. Parser Ă˘â€ â€™ AST (TypeScript)
**Interaktywny spis:** [2.1 KsztaÄąâ€št AST](#ch-2-1) Ă‚Â· [2.2 Normalizacja](#ch-2-2) Ă‚Â· [2.3 Stabilizacja kolejnoÄąâ€şci](#ch-2-3)
## 2.1 KsztaÄąâ€št AST {: #ch-2-1 }
```ts
export type AnchorRef = string; // np. 'parent.left', 'header.bottom'
export interface Geometry {
  id: string;
  size?: [number, number];
  width?: number; height?: number;
  anchors?: Partial<Record<'fill'|'left'|'right'|'top'|'bottom'|'verticalCenter'|'horizontalCenter', AnchorRef>>;
  padding?: number; marginLeft?: number; marginRight?: number; marginTop?: number; marginBottom?: number;
}
export interface Style {
  backgroundColor?: string; imageSource?: string; imageSmooth?: boolean; imageFixedRatio?: boolean;
  font?: string; color?: string; text?: string; textWrap?: boolean; textAutoResize?: boolean; textAlign?: string; textOffset?: [number,number];
}
export interface Behavior { events?: Partial<Record<'onEnter'|'onEscape'|'onClick'|'onSetup'|'onOptionChange', string>>; states?: Record<string, Style>; }
export interface WidgetNode {
  base: string; // typ OTUI
  extends?: string; // dla np. MiniWindow < MainWindow
  geometry: Geometry;
  style?: Style;
  behavior?: Behavior;
  children?: WidgetNode[];
  variant?: string; // np. RoundCheckBox
}
```
## 2.2 Normalizacja {: #ch-2-2 }
- UzupeÄąâ€šnij brakujĂ„â€¦ce struktury: `children = []`, `style = {}` gdy potrzebne.  
- ZamieÄąâ€ž `style.text` Ă˘â€ â€™ w serializacji na `!text: tr('...')`.  
- ZastĂ„â€¦p `size` parĂ„â€¦ `width/height` podczas walidacji kotwic (na potrzeby reguÄąâ€š), ale w serializacji zachowuj wejÄąâ€şciowĂ„â€¦ postaĂ„â€ˇ.
## 2.3 Stabilizacja kolejnoÄąâ€şci {: #ch-2-3 }
- Atrybuty: najpierw **GEOMETRIA**, potem **STYL**, na koÄąâ€žcu **ZACHOWANIE** (events/states).  
- Dzieci: sortuj stabilnie po `(slotPriority, y, x, id)` jeÄąâ€şli edytor posiada grid/snapping; inaczej po kolejnoÄąâ€şci wczytania.

---

<div id="ch-3"></div>
## 3. Serializer (AST Ă˘â€ â€™ OTUI STRICT)
**Interaktywny spis:** [3.1 ReguÄąâ€šy wypisywania](#ch-3-1) Ă‚Â· [3.2 Escaping i i18n](#ch-3-2) Ă‚Â· [3.3 Sanityzacja koÄąâ€žcowa](#ch-3-3)
## 3.1 ReguÄąâ€šy wypisywania {: #ch-3-1 }
- WciĂ„â„˘cie: **2 spacje**.  
- Puste wartoÄąâ€şci pomijaj.  
- Sekcja kolejnoÄąâ€şci: GEOMETRIA (`id`, `size`/`width`/`height`, `anchors.*`, `margin-*`, `padding`) Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE (`@on*`, `$state:` bloki).
## 3.2 Escaping i i18n {: #ch-3-2 }
- `style.text` Ă˘â€ â€™ `!text: tr('...')`, `'` Ă˘â€ â€™ `\'`.  
- Kolory tylko `#AARRGGBB` lub `alpha`.
## 3.3 Sanityzacja koÄąâ€žcowa {: #ch-3-3 }
- UsuÄąâ€ž taby, trailing spaces, wymuÄąâ€ş LF.  
- Brak komentarzy w wynikowym `.otui`.

---

<div id="ch-4"></div>
## 4. Macierze dozwolonych dzieci (global)
**Interaktywny spis:** [4.1 Okna](#ch-4-1) Ă‚Â· [4.2 Kontenery](#ch-4-2) Ă‚Â· [4.3 Organizacja](#ch-4-3) Ă‚Â· [4.4 Dane/Edycja](#ch-4-4) Ă‚Â· [4.5 WskaÄąĹźniki/Scroll](#ch-4-5)

> **Legenda:** Ă˘Ĺ›â€ś dozwolone Ă‚Â· Ă˘Ĺ›â€“ zabronione Ă‚Â· Ă˘Ĺˇ  warunkowe (patrz uwagi).
## 4.1 Okna (WindowĂ˘â‚¬â€class) {: #ch-4-1 }
**MainWindow / StaticMainWindow (root)**
| Dziecko | Status | Uwagi |
|---|:---:|---|
| UIWidget, Panel, GroupBox | Ă˘Ĺ›â€ś | Elementy panelowe.
| Label, Button, CheckBox, TextEdit, PasswordTextEdit, MultilineTextEdit, ComboBox | Ă˘Ĺ›â€ś | Formularze i akcje.
| TextList | Ă˘Ĺ›â€ś | Wymaga pary z VerticalScrollBar przy overflow (Ă˘Ĺˇ ).
| ProgressBar, HorizontalSeparator | Ă˘Ĺ›â€ś | Ă˘â‚¬â€ť
| TabBar, TabWidget, Splitter | Ă˘Ĺ›â€ś | Splitter: dokÄąâ€šadnie 2 dzieci (Ă˘Ĺˇ ).
| StatusOverlay | Ă˘Ĺ›â€ś | Warstwa wierzchnia, bez zÄąâ€šoÄąÄ˝onych dzieci (Ă˘Ĺˇ ).
| *Window (Main/Static/Mini/Container/Dialog) | Ă˘Ĺ›â€“ | Zakaz okienĂ˘â‚¬â€dzieci.
| ScrollBar (samotny) | Ă˘Ĺ›â€“ | Zawsze para z treÄąâ€şciĂ„â€¦.

**MiniWindow / ContainerWindow / DialogWindow**
- Slot `titlebar`: Label, Button, UIWidget(ikona) Ă˘Ĺ›â€ś; listy/edytory/scroll Ă˘Ĺ›â€“.  
- Slot `content`: elementy panelowe Ă˘Ĺ›â€ś; oknaĂ˘â‚¬â€dzieci Ă˘Ĺ›â€“.  
- Slot `footer` (Mini/Dialog): Button/Label/ProgressBar Ă˘Ĺ›â€ś; listy/edytory/scroll Ă˘Ĺ›â€“.
## 4.2 Kontenery (ContentĂ˘â‚¬â€class) {: #ch-4-2 }
| Parent | Dozwolone dzieci | Niedozwolone/uwagi |
|---|---|---|
| UIWidget | Wszystkie panelowe (Label/Button/Inputs/List/Progress/Scroll/Separator/StatusOverlay) | *Window Ă˘Ĺ›â€“ |
| Panel | j.w. | *Window Ă˘Ĺ›â€“ |
| GroupBox | `header: Label` Ă˘Ĺ›â€ś, `content: panelowe` Ă˘Ĺ›â€ś | Scroll w header Ă˘Ĺ›â€“ |
| TabWidget | TreÄąâ€şĂ„â€ˇ aktywnej zakÄąâ€šadki: panelowe Ă˘Ĺ›â€ś | *Window Ă˘Ĺ›â€“; sam TabBar nie tu |
| StatusOverlay | Label, ProgressBar, Button(cancel) Ă˘Ĺ›â€ś | Listy/edytory/okna Ă˘Ĺ›â€“ |
## 4.3 Organizacja/Nawigacja {: #ch-4-3 }
| Komponent | Dozwolone dzieci | Niedozwolone/uwagi |
|---|---|---|
| Titlebar | Label, Button, UIWidget(ikona) | Scroll/listy/edytory Ă˘Ĺ›â€“ |
| Toolbar | Button, HorizontalSeparator | Inne Ă˘Ĺ›â€“ |
| TabBar | Button (zakÄąâ€šadki) | TreÄąâ€şĂ„â€ˇ zakÄąâ€šadek Ă˘Ĺ›â€“ Ă˘â‚¬â€ť trafia do TabWidget |
| Splitter | **DokÄąâ€šadnie 2** dzieci: Panel/UIWidget/GroupBox | Okna/Scroll Ă˘Ĺ›â€“ |
| HorizontalSeparator | Ă˘â‚¬â€ť | **Bez dzieci** |
## 4.4 Dane/Edycja {: #ch-4-4 }
| Komponent | Dzieci |
|---|---|
| Label, Button, CheckBox, TextEdit, PasswordTextEdit, ComboBox, ProgressBar, ScrollBar | **Brak** |
| MultilineTextEdit | **Brak**; przewijanie przez sĂ„â€¦siedni Vertical/HorizontalScrollBar |
| TextList | **Brak** rĂ„â„˘cznych dzieci; wiersze generowane jako `UIWidget` (ListRow) runtime/templatem |
## 4.5 WskaÄąĹźniki/Scroll {: #ch-4-5 }
| Komponent | Zasady |
|---|---|
| VerticalScrollBar | Sibling przewijanej treÄąâ€şci; dock **right**; treÄąâ€şĂ„â€ˇ kotwiczy `right: scroll.left` |
| HorizontalScrollBar | Sibling przewijanej treÄąâ€şci; dock **bottom**; treÄąâ€şĂ„â€ˇ kotwiczy `bottom: hscroll.top` |

---

<div id="ch-5"></div>
## 5. Walidator Ă˘â‚¬â€ť reguÄąâ€šy, kody bÄąâ€šĂ„â„˘dÄ‚Ĺ‚w/ostrzeÄąÄ˝eÄąâ€ž
**Interaktywny spis:** [5.1 BÄąâ€šĂ„â„˘dy (E)](#ch-5-1) Ă‚Â· [5.2 OstrzeÄąÄ˝enia (W)](#ch-5-2) Ă‚Â· [5.3 Raport](#ch-5-3)
## 5.1 BÄąâ€šĂ„â„˘dy (E) {: #ch-5-1 }
- **E001 STRICT/Format** Ă˘â‚¬â€ť taby/BOM/komentarze/trailing spaces.  
- **E010 Anchors/Conflict** Ă˘â‚¬â€ť `anchors.fill` + inne kotwice.  
- **E020 Window/Nesting** Ă˘â‚¬â€ť okno (`*Window`) jako dziecko okna.  
- **E030 Scroll/Orphan** Ă˘â‚¬â€ť ScrollBar bez sparowanej treÄąâ€şci.  
- **E031 Scroll/Pairing** Ă˘â‚¬â€ť brak kotwicy treÄąâ€şci do ScrollBar (`right: scroll.left` lub `bottom: hscroll.top`).  
- **E040 Text/i18n** Ă˘â‚¬â€ť staÄąâ€šy tekst bez `tr()` (w OTUI).  
- **E050 Splitter/Arity** Ă˘â‚¬â€ť != 2 dzieci.  
- **E060 Titlebar/Children** Ă˘â‚¬â€ť niedozwolone dziecko w `titlebar`.
## 5.2 OstrzeÄąÄ˝enia (W) {: #ch-5-2 }
- **W101 Width/AutoFit** Ă˘â‚¬â€ť okno dokowane z `width` (sugeruj usuniĂ„â„˘cie).  
- **W110 Margins/Odd** Ă˘â‚¬â€ť nieparzyste marginesy (snapping 2 px).  
- **W120 Scroll/StepMismatch** Ă˘â‚¬â€ť `step` niezgodny z wielkoÄąâ€şciĂ„â€¦ wiersza/slotu.  
- **W130 Keyboard/Hints** Ă˘â‚¬â€ť brak `@onEnter/@onEscape` w oknie dialogowym.
## 5.3 Raport {: #ch-5-3 }
- Struktura: `{code, severity, path, message, fix?}`.  
- `path` = Äąâ€şcieÄąÄ˝ka wĂ„â„˘zÄąâ€šÄ‚Ĺ‚w (`main/content/items`).

---

<div id="ch-6"></div>
## 6. AutoĂ˘â‚¬â€naprawy deterministyczne
**Interaktywny spis:** [6.1 STRICT fixups](#ch-6-1) Ă‚Â· [6.2 Anchors/Layout](#ch-6-2) Ă‚Â· [6.3 Scroll pairing](#ch-6-3)
## 6.1 STRICT fixups {: #ch-6-1 }
- UsuÄąâ€ž taby/BOM/komentarze; przytnij trailing spaces; wymuÄąâ€ş LF.
- UporzĂ„â€¦dkuj kolejnoÄąâ€şĂ„â€ˇ atrybutÄ‚Ĺ‚w (GEOMETRIAĂ˘â€ â€™STYLĂ˘â€ â€™ZACHOWANIE).
## 6.2 Anchors/Layout {: #ch-6-2 }
- JeÄąâ€şli sĂ„â€¦ `anchors.left` + `anchors.right` **i** `width` Ă˘â€ â€™ usuÄąâ€ž `width` (AutoĂ˘â‚¬â€fit).  
- Rozdziel `size` na `width/height` tylko na potrzeby walidacji, nie w serializacji (zachowaj wejÄąâ€şciowy idiom).
## 6.3 Scroll pairing {: #ch-6-3 }
- Dla `TextList`/`MultilineTextEdit` dodaj brakujĂ„â€¦cy `VerticalScrollBar` jako sibling (po prawej) i dodaj kotwicĂ„â„˘ treÄąâ€şci `right: scroll.left`.

---

<div id="ch-7"></div>
## 7. Import/Export i roundĂ˘â‚¬â€trip (edytor Ă˘â€ â€ť plik Ă˘â€ â€ť Lua)
**Interaktywny spis:** [7.1 Import z plikÄ‚Ĺ‚w `.otui`](#ch-7-1) Ă‚Â· [7.2 Import z Lua (blok string)](#ch-7-2) Ă‚Â· [7.3 Eksport](#ch-7-3)
## 7.1 Import z plikÄ‚Ĺ‚w `.otui` {: #ch-7-1 }
- Wczytaj, znormalizuj (STRICT), sparsuj do AST. Zachowaj *oryginalny ukÄąâ€šad* do porÄ‚Ĺ‚wnaÄąâ€ž.
## 7.2 Import z Lua (blok string) {: #ch-7-2 }
- Wykryj staÄąâ€še `local <Name>_OTUI = [[...]]`; wytnij treÄąâ€şĂ„â€ˇ; sprawdÄąĹź STRICT; sparsuj.  
- OstrzeÄąÄ˝enie, gdy blok zawiera komentarze Ă˘â‚¬â€ť niedozwolone w OTUI (mimo bycia w Lua).
## 7.3 Eksport {: #ch-7-3 }
- Do pliku `.otui` (kanoniczny cel runtime).  
- Opcjonalnie: *roundĂ˘â‚¬â€trip do Lua* Ă˘â‚¬â€ť odÄąâ€şwieÄąÄ˝ istniejĂ„â€¦cy blok `[[...]]` bitĂ˘â‚¬â€identycznie po `ensureStrictOtui()`.

---

<div id="ch-8"></div>
## 8. API edytora (TS): parse/serialize/validate/autofix
**Interaktywny spis:** [8.1 Interfejsy](#ch-8-1) Ă‚Â· [8.2 PrzepÄąâ€šywy](#ch-8-2)
## 8.1 Interfejsy {: #ch-8-1 }
```ts
export function parseOtui(text: string): WidgetNode[];
export function serializeAst(nodes: WidgetNode[]): string; // STRICT OTUI
export function ensureStrictOtui(text: string): string;     // tylko format
export interface ValidationIssue { code: string; severity: 'error'|'warning'; path: string; message: string; fix?: string; }
export function validateAst(nodes: WidgetNode[]): ValidationIssue[];
export function autofixAst(nodes: WidgetNode[]): { nodes: WidgetNode[]; changes: ValidationIssue[] };
```
## 8.2 PrzepÄąâ€šywy {: #ch-8-2 }
- **Projekt Ă˘â€ â€™ Walidacja Ă˘â€ â€™ Serializacja**.  
- **Import (plik/Lua) Ă˘â€ â€™ Parser Ă˘â€ â€™ Normalizacja Ă˘â€ â€™ Walidacja Ă˘â€ â€™ Edycja Ă˘â€ â€™ Serializacja Ă˘â€ â€™ Eksport (plik/Lua)**.

---

<div id="ch-9"></div>
## 9. Testy: goldeny i snapshoty
**Interaktywny spis:** [9.1 Goldeny roundĂ˘â‚¬â€trip](#ch-9-1) Ă‚Â· [9.2 Snapshoty wizualne](#ch-9-2)
## 9.1 Goldeny roundĂ˘â‚¬â€trip {: #ch-9-1 }
- Zestaw `X.otui` Ă˘â€ â€™ `parse` Ă˘â€ â€™ `serialize` Ă˘â€ â€™ porÄ‚Ĺ‚wnanie bitĂ˘â‚¬â€poĂ˘â‚¬â€bicie.  
- DokÄąâ€šadaj przypadki: okna, scroll pairing, Splitter, TabBar/TabWidget.
## 9.2 Snapshoty wizualne {: #ch-9-2 }
- Render testowy po stronie klienta (lub symulacja) i porÄ‚Ĺ‚wnania pikselowe dla kluczowych presetÄ‚Ĺ‚w.

---

<div id="ch-10"></div>
## 10. PrzykÄąâ€šady i edgeĂ˘â‚¬â€cases
**Interaktywny spis:** [10.1 Migracja do STRICT](#ch-10-1) Ă‚Â· [10.2 Anchors/Fill vs krawĂ„â„˘dzie](#ch-10-2) Ă‚Â· [10.3 Splitter/Arity](#ch-10-3)
## 10.1 Migracja do STRICT {: #ch-10-1 }
- WejÄąâ€şcie dowolne Ă˘â€ â€™ `ensureStrictOtui()` Ă˘â€ â€™ `parse` Ă˘â€ â€™ `autofixAst()` Ă˘â€ â€™ `serializeAst()`.
## 10.2 Anchors/Fill vs krawĂ„â„˘dzie {: #ch-10-2 }
**BÄąÂĂ„ÂDNY OTUI**
```otui
UIWidget
  id: box
  anchors.fill: parent
  anchors.left: parent.left
```
**PO NAPRAWIE (autofix)**
```otui
UIWidget
  id: box
  anchors.fill: parent
```
## 10.3 Splitter/Arity {: #ch-10-3 }
**BÄąÂĂ„ÂDNY OTUI**
```otui
Splitter
  id: split
  size: 300 160

  Panel
    id: left

```
**PO NAPRAWIE (manualnej)**
```otui
Splitter
  id: split
  size: 300 160

  Panel
    id: left

  Panel
    id: right
```

---

<div id="ch-11"></div>
## 11. Indeks haseÄąâ€š
- STRICT Ă˘â‚¬Ë AST Ă˘â‚¬Ë Macierz Ă˘â‚¬Ë Walidator Ă˘â‚¬Ë AutoĂ˘â‚¬â€naprawy Ă˘â‚¬Ë RoundĂ˘â‚¬â€trip Ă˘â‚¬Ë Splitter Ă˘â‚¬Ë TabBar/TabWidget Ă˘â‚¬Ë StatusOverlay Ă˘â‚¬Ë Scroll pairing




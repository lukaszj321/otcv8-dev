# **Pakiet:** `otc_core_v1/engine` A'as **Wersja:** 1.0   
**Cel:** Jednolita, operacyjna specyfikacja **parsera/serializera OTUI (STRICT)**, **walidatora** i **macierzy dozwolonych dzieci**. Dokument jest fundamentem dla edytora TS (Sparky) oraz testA"asAaasw roundA'EAasAAa'Atrip.

---
## Spis treA"aAa'Lzci
- [0. Zakres, definicje, zaA"aAa'LoA"aA"Etenia](#ch-0)
- [1. STRICT OTUI A'EAasA" gramatyka i tokenizacja](#ch-1)
- [2. Parser A'EAa'A ' AST (TypeScript)](#ch-2)
- [3. Serializer (AST A'EAa'A ' OTUI STRICT)](#ch-3)
- [4. Macierze dozwolonych dzieci (global)](#ch-4)
  - [4.1 Okna (WindowA'EAasAAa'Aclass)](#ch-4-1)
  - [4.2 Kontenery (ContentA'EAasAAa'Aclass)](#ch-4-2)
  - [4.3 Organizacja/Nawigacja](#ch-4-3)
  - [4.4 Dane/Edycja](#ch-4-4)
  - [4.5 WskaA"aAaLsniki/Scroll](#ch-4-5)
- [5. Walidator A'EAasA" reguA"aAa'Ly, kody bA"aAa'LA'"A"EdA"asAaasw/ostrzeA"aA"EteA"a"](#ch-5)
- [6. AutoA'EAasAAa'Anaprawy deterministyczne](#ch-6)
- [7. Import/Export i roundA'EAasAAa'Atrip (edytor A'EAa'A " plik A'EAa'A " Lua)](#ch-7)
- [8. API edytora (TS): parse/serialize/validate/autofix](#ch-8)
- [9. Testy: goldeny i snapshoty](#ch-9)
- [10. PrzykA"aAa'Lady i edgeA'EAasAAa'Acases](#ch-10)
- [11. Indeks haseA"aAa'L](#ch-11)

---

<div id="ch-0"></div>
## 0. Zakres, definicje, zaA"aAa'LoA"aA"Etenia
**Interaktywny spis:** [0.1 Zakres](#ch-0-1) A'as [0.2 Definicje](#ch-0-2) A'as [0.3 ZaA"aAa'LoA"aA"Etenia projektowe](#ch-0-3)
## 0.1 Zakres {: #ch-0-1 }
- Pokrycie: *caA"aAa'Ly pipeline* od tekstu OTUI (STRICT) A'EAa'A " AST (TS) A'EAa'A " walidacja A'EAa'A " autoA'EAasAAa'Anaprawy A'EAa'A " eksport/import.  
- Zakres UI: komplet taksonomii z czA'"A"EA"aAa'Lzci A'EAasAAaAlSpecyfikacja UIA'EAasAAaA (rozdz. 4) + presety kanoniczne.
## 0.2 Definicje {: #ch-0-2 }
- **STRICT OTUI** A'EAasA" format bezkomentarzowy, LF, wciA'"A"Ecia 2 sp., kolejnoA"aAa'LzA'"Aa'E GEOMETRIAA'EAa'A 'STYLA'EAa'A 'ZACHOWANIE.
- **AST** A'EAasA" drzewo `WidgetNode`, deterministyczne klucze i kolejnoA"aAa'LzA'"Aa'E dzieci.
- **Macierz** A'EAasA" tablica dozwolonych dzieci dla par (parent, slot).
## 0.3 ZaA"aAa'LoA"aA"Etenia projektowe {: #ch-0-3 }
- **DeterministycznoA"aAa'LzA'"Aa'E**: ten sam AST A'EAa'A ' ten sam OTUI (bitA'EAasAAa'Aidentyczny, przy tej samej wersji serializera).  
- **Idempotencja**: `parse(serialize(ast))` A'EAa'AAa `normalize(ast)`.
- **Brak magii**: walidator zgA"aAa'Lasza i *tylko* przewidywalnie naprawia.

---

<div id="ch-1"></div>
## 1. STRICT OTUI A'EAasA" gramatyka i tokenizacja
**Interaktywny spis:** [1.1 Zasady formatowania](#ch-1-1) A'as [1.2 Tokeny](#ch-1-2) A'as [1.3 Szkic EBNF](#ch-1-3)
## 1.1 Zasady formatowania {: #ch-1-1 }
- **WciA'"A"Ecia**: 2 spacje na poziom. **Zakaz tabA"asAaasw**.  
- **KoA"a"ce linii**: LF. **Bez BOM**.  
- **Brak komentarzy** w blokach `.otui`.  
- **KolejnoA"aAa'LzA'"Aa'E atrybutA"asAaasw** w kaA"aA"Etdym wA'"A"EA"aAaLsle: GEOMETRIA A'EAa'A ' STYL A'EAa'A ' ZACHOWANIE.
## 1.2 Tokeny {: #ch-1-2 }
- SA"aAa'Lowa kluczowe typA"asAaasw: `MainWindow`, `StaticMainWindow`, `MiniWindow`, `ContainerWindow`, `DialogWindow`, `UIWidget`, `Panel`, `GroupBox`, `Titlebar`, `Toolbar`, `TabBar`, `TabWidget`, `Splitter`, `HorizontalSeparator`, `StatusOverlay`, `Label`, `Button`, `CheckBox`, `TextEdit`, `PasswordTextEdit`, `MultilineTextEdit`, `ComboBox`, `TextList`, `ProgressBar`, `VerticalScrollBar`, `HorizontalScrollBar`.
- Operator dziedziczenia: `<` (np. `MiniWindow < MainWindow`).
- Identyfikatory: `id: <slug>`; A"aAa'LaA"a"cuchy w `!text: tr('...')`; liczby caA"aAa'Lkowite; kolory `#AARRGGBB` lub `alpha`.
## 1.3 Szkic EBNF (pogglA'"Aa'A|dowy) {: #ch-1-3 }
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
## 2. Parser A'EAa'A ' AST (TypeScript)
**Interaktywny spis:** [2.1 KsztaA"aAa'Lt AST](#ch-2-1) A'as [2.2 Normalizacja](#ch-2-2) A'as [2.3 Stabilizacja kolejnoA"aAa'Lzci](#ch-2-3)
## 2.1 KsztaA"aAa'Lt AST {: #ch-2-1 }
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
- UzupeA"aAa'Lnij brakujA'"Aa'A|ce struktury: `children = []`, `style = {}` gdy potrzebne.  
- ZamieA"a" `style.text` A'EAa'A ' w serializacji na `!text: tr('...')`.  
- ZastA'"Aa'A|p `size` parA'"Aa'A| `width/height` podczas walidacji kotwic (na potrzeby reguA"aAa'L), ale w serializacji zachowuj wejA"aAa'LzciowA'"Aa'A| postaA'"Aa'E.
## 2.3 Stabilizacja kolejnoA"aAa'Lzci {: #ch-2-3 }
- Atrybuty: najpierw **GEOMETRIA**, potem **STYL**, na koA"a"cu **ZACHOWANIE** (events/states).  
- Dzieci: sortuj stabilnie po `(slotPriority, y, x, id)` jeA"aAa'Lzli edytor posiada grid/snapping; inaczej po kolejnoA"aAa'Lzci wczytania.

---

<div id="ch-3"></div>
## 3. Serializer (AST A'EAa'A ' OTUI STRICT)
**Interaktywny spis:** [3.1 ReguA"aAa'Ly wypisywania](#ch-3-1) A'as [3.2 Escaping i i18n](#ch-3-2) A'as [3.3 Sanityzacja koA"a"cowa](#ch-3-3)
## 3.1 ReguA"aAa'Ly wypisywania {: #ch-3-1 }
- WciA'"A"Ecie: **2 spacje**.  
- Puste wartoA"aAa'Lzci pomijaj.  
- Sekcja kolejnoA"aAa'Lzci: GEOMETRIA (`id`, `size`/`width`/`height`, `anchors.*`, `margin-*`, `padding`) A'EAa'A ' STYL A'EAa'A ' ZACHOWANIE (`@on*`, `$state:` bloki).
## 3.2 Escaping i i18n {: #ch-3-2 }
- `style.text` A'EAa'A ' `!text: tr('...')`, `'` A'EAa'A ' `\'`.  
- Kolory tylko `#AARRGGBB` lub `alpha`.
## 3.3 Sanityzacja koA"a"cowa {: #ch-3-3 }
- UsuA"a" taby, trailing spaces, wymuA"aAa'Lz LF.  
- Brak komentarzy w wynikowym `.otui`.

---

<div id="ch-4"></div>
## 4. Macierze dozwolonych dzieci (global)
**Interaktywny spis:** [4.1 Okna](#ch-4-1) A'as [4.2 Kontenery](#ch-4-2) A'as [4.3 Organizacja](#ch-4-3) A'as [4.4 Dane/Edycja](#ch-4-4) A'as [4.5 WskaA"aAaLsniki/Scroll](#ch-4-5)

> **Legenda:** A'EAaas" dozwolone A'as A'EAaas- zabronione A'as A'EAaE  warunkowe (patrz uwagi).
## 4.1 Okna (WindowA'EAasAAa'Aclass) {: #ch-4-1 }
**MainWindow / StaticMainWindow (root)**
| Dziecko | Status | Uwagi |
|---|:---:|---|
| UIWidget, Panel, GroupBox | A'EAaas" | Elementy panelowe.
| Label, Button, CheckBox, TextEdit, PasswordTextEdit, MultilineTextEdit, ComboBox | A'EAaas" | Formularze i akcje.
| TextList | A'EAaas" | Wymaga pary z VerticalScrollBar przy overflow (A'EAaE ).
| ProgressBar, HorizontalSeparator | A'EAaas" | A'EAasA"
| TabBar, TabWidget, Splitter | A'EAaas" | Splitter: dokA"aAa'Ladnie 2 dzieci (A'EAaE ).
| StatusOverlay | A'EAaas" | Warstwa wierzchnia, bez zA"aAa'LoA"aA"Etonych dzieci (A'EAaE ).
| *Window (Main/Static/Mini/Container/Dialog) | A'EAaas- | Zakaz okienA'EAasAAa'Adzieci.
| ScrollBar (samotny) | A'EAaas- | Zawsze para z treA"aAa'LzciA'"Aa'A|.

**MiniWindow / ContainerWindow / DialogWindow**
- Slot `titlebar`: Label, Button, UIWidget(ikona) A'EAaas"; listy/edytory/scroll A'EAaas-.  
- Slot `content`: elementy panelowe A'EAaas"; oknaA'EAasAAa'Adzieci A'EAaas-.  
- Slot `footer` (Mini/Dialog): Button/Label/ProgressBar A'EAaas"; listy/edytory/scroll A'EAaas-.
## 4.2 Kontenery (ContentA'EAasAAa'Aclass) {: #ch-4-2 }
| Parent | Dozwolone dzieci | Niedozwolone/uwagi |
|---|---|---|
| UIWidget | Wszystkie panelowe (Label/Button/Inputs/List/Progress/Scroll/Separator/StatusOverlay) | *Window A'EAaas- |
| Panel | j.w. | *Window A'EAaas- |
| GroupBox | `header: Label` A'EAaas", `content: panelowe` A'EAaas" | Scroll w header A'EAaas- |
| TabWidget | TreA"aAa'LzA'"Aa'E aktywnej zakA"aAa'Ladki: panelowe A'EAaas" | *Window A'EAaas-; sam TabBar nie tu |
| StatusOverlay | Label, ProgressBar, Button(cancel) A'EAaas" | Listy/edytory/okna A'EAaas- |
## 4.3 Organizacja/Nawigacja {: #ch-4-3 }
| Komponent | Dozwolone dzieci | Niedozwolone/uwagi |
|---|---|---|
| Titlebar | Label, Button, UIWidget(ikona) | Scroll/listy/edytory A'EAaas- |
| Toolbar | Button, HorizontalSeparator | Inne A'EAaas- |
| TabBar | Button (zakA"aAa'Ladki) | TreA"aAa'LzA'"Aa'E zakA"aAa'Ladek A'EAaas- A'EAasA" trafia do TabWidget |
| Splitter | **DokA"aAa'Ladnie 2** dzieci: Panel/UIWidget/GroupBox | Okna/Scroll A'EAaas- |
| HorizontalSeparator | A'EAasA" | **Bez dzieci** |
## 4.4 Dane/Edycja {: #ch-4-4 }
| Komponent | Dzieci |
|---|---|
| Label, Button, CheckBox, TextEdit, PasswordTextEdit, ComboBox, ProgressBar, ScrollBar | **Brak** |
| MultilineTextEdit | **Brak**; przewijanie przez sA'"Aa'A|siedni Vertical/HorizontalScrollBar |
| TextList | **Brak** rA'"A"Ecznych dzieci; wiersze generowane jako `UIWidget` (ListRow) runtime/templatem |
## 4.5 WskaA"aAaLsniki/Scroll {: #ch-4-5 }
| Komponent | Zasady |
|---|---|
| VerticalScrollBar | Sibling przewijanej treA"aAa'Lzci; dock **right**; treA"aAa'LzA'"Aa'E kotwiczy `right: scroll.left` |
| HorizontalScrollBar | Sibling przewijanej treA"aAa'Lzci; dock **bottom**; treA"aAa'LzA'"Aa'E kotwiczy `bottom: hscroll.top` |

---

<div id="ch-5"></div>
## 5. Walidator A'EAasA" reguA"aAa'Ly, kody bA"aAa'LA'"A"EdA"asAaasw/ostrzeA"aA"EteA"a"
**Interaktywny spis:** [5.1 BA"aAa'LA'"A"Edy (E)](#ch-5-1) A'as [5.2 OstrzeA"aA"Etenia (W)](#ch-5-2) A'as [5.3 Raport](#ch-5-3)
## 5.1 BA"aAa'LA'"A"Edy (E) {: #ch-5-1 }
- **E001 STRICT/Format** A'EAasA" taby/BOM/komentarze/trailing spaces.  
- **E010 Anchors/Conflict** A'EAasA" `anchors.fill` + inne kotwice.  
- **E020 Window/Nesting** A'EAasA" okno (`*Window`) jako dziecko okna.  
- **E030 Scroll/Orphan** A'EAasA" ScrollBar bez sparowanej treA"aAa'Lzci.  
- **E031 Scroll/Pairing** A'EAasA" brak kotwicy treA"aAa'Lzci do ScrollBar (`right: scroll.left` lub `bottom: hscroll.top`).  
- **E040 Text/i18n** A'EAasA" staA"aAa'Ly tekst bez `tr()` (w OTUI).  
- **E050 Splitter/Arity** A'EAasA" != 2 dzieci.  
- **E060 Titlebar/Children** A'EAasA" niedozwolone dziecko w `titlebar`.
## 5.2 OstrzeA"aA"Etenia (W) {: #ch-5-2 }
- **W101 Width/AutoFit** A'EAasA" okno dokowane z `width` (sugeruj usuniA'"A"Ecie).  
- **W110 Margins/Odd** A'EAasA" nieparzyste marginesy (snapping 2 px).  
- **W120 Scroll/StepMismatch** A'EAasA" `step` niezgodny z wielkoA"aAa'LzciA'"Aa'A| wiersza/slotu.  
- **W130 Keyboard/Hints** A'EAasA" brak `@onEnter/@onEscape` w oknie dialogowym.
## 5.3 Raport {: #ch-5-3 }
- Struktura: `{code, severity, path, message, fix?}`.  
- `path` = A"aAa'LzcieA"aA"Etka wA'"A"EzA"aAa'LA"asAaasw (`main/content/items`).

---

<div id="ch-6"></div>
## 6. AutoA'EAasAAa'Anaprawy deterministyczne
**Interaktywny spis:** [6.1 STRICT fixups](#ch-6-1) A'as [6.2 Anchors/Layout](#ch-6-2) A'as [6.3 Scroll pairing](#ch-6-3)
## 6.1 STRICT fixups {: #ch-6-1 }
- UsuA"a" taby/BOM/komentarze; przytnij trailing spaces; wymuA"aAa'Lz LF.
- UporzA'"Aa'A|dkuj kolejnoA"aAa'LzA'"Aa'E atrybutA"asAaasw (GEOMETRIAA'EAa'A 'STYLA'EAa'A 'ZACHOWANIE).
## 6.2 Anchors/Layout {: #ch-6-2 }
- JeA"aAa'Lzli sA'"Aa'A| `anchors.left` + `anchors.right` **i** `width` A'EAa'A ' usuA"a" `width` (AutoA'EAasAAa'Afit).  
- Rozdziel `size` na `width/height` tylko na potrzeby walidacji, nie w serializacji (zachowaj wejA"aAa'Lzciowy idiom).
## 6.3 Scroll pairing {: #ch-6-3 }
- Dla `TextList`/`MultilineTextEdit` dodaj brakujA'"Aa'A|cy `VerticalScrollBar` jako sibling (po prawej) i dodaj kotwicA'"A"E treA"aAa'Lzci `right: scroll.left`.

---

<div id="ch-7"></div>
## 7. Import/Export i roundA'EAasAAa'Atrip (edytor A'EAa'A " plik A'EAa'A " Lua)
**Interaktywny spis:** [7.1 Import z plikA"asAaasw `.otui`](#ch-7-1) A'as [7.2 Import z Lua (blok string)](#ch-7-2) A'as [7.3 Eksport](#ch-7-3)
## 7.1 Import z plikA"asAaasw `.otui` {: #ch-7-1 }
- Wczytaj, znormalizuj (STRICT), sparsuj do AST. Zachowaj *oryginalny ukA"aAa'Lad* do porA"asAaaswnaA"a".
## 7.2 Import z Lua (blok string) {: #ch-7-2 }
- Wykryj staA"aAa'Le `local <Name>_OTUI = [[...]]`; wytnij treA"aAa'LzA'"Aa'E; sprawdA"aAaLs STRICT; sparsuj.  
- OstrzeA"aA"Etenie, gdy blok zawiera komentarze A'EAasA" niedozwolone w OTUI (mimo bycia w Lua).
## 7.3 Eksport {: #ch-7-3 }
- Do pliku `.otui` (kanoniczny cel runtime).  
- Opcjonalnie: *roundA'EAasAAa'Atrip do Lua* A'EAasA" odA"aAa'LzwieA"aA"Et istniejA'"Aa'A|cy blok `[[...]]` bitA'EAasAAa'Aidentycznie po `ensureStrictOtui()`.

---

<div id="ch-8"></div>
## 8. API edytora (TS): parse/serialize/validate/autofix
**Interaktywny spis:** [8.1 Interfejsy](#ch-8-1) A'as [8.2 PrzepA"aAa'Lywy](#ch-8-2)
## 8.1 Interfejsy {: #ch-8-1 }
export function parseOtui(text: string): WidgetNode[];
export function serializeAst(nodes: WidgetNode[]): string; // STRICT OTUI
export function ensureStrictOtui(text: string): string;     // tylko format
export interface ValidationIssue { code: string; severity: 'error'|'warning'; path: string; message: string; fix?: string; }
export function validateAst(nodes: WidgetNode[]): ValidationIssue[];
export function autofixAst(nodes: WidgetNode[]): { nodes: WidgetNode[]; changes: ValidationIssue[] };
```
## 8.2 PrzepA"aAa'Lywy {: #ch-8-2 }
- **Projekt A'EAa'A ' Walidacja A'EAa'A ' Serializacja**.  
- **Import (plik/Lua) A'EAa'A ' Parser A'EAa'A ' Normalizacja A'EAa'A ' Walidacja A'EAa'A ' Edycja A'EAa'A ' Serializacja A'EAa'A ' Eksport (plik/Lua)**.

---

<div id="ch-9"></div>
## 9. Testy: goldeny i snapshoty
**Interaktywny spis:** [9.1 Goldeny roundA'EAasAAa'Atrip](#ch-9-1) A'as [9.2 Snapshoty wizualne](#ch-9-2)
## 9.1 Goldeny roundA'EAasAAa'Atrip {: #ch-9-1 }
- Zestaw `X.otui` A'EAa'A ' `parse` A'EAa'A ' `serialize` A'EAa'A ' porA"asAaaswnanie bitA'EAasAAa'ApoA'EAasAAa'Abicie.  
- DokA"aAa'Ladaj przypadki: okna, scroll pairing, Splitter, TabBar/TabWidget.
## 9.2 Snapshoty wizualne {: #ch-9-2 }
- Render testowy po stronie klienta (lub symulacja) i porA"asAaaswnania pikselowe dla kluczowych presetA"asAaasw.

---

<div id="ch-10"></div>
## 10. PrzykA"aAa'Lady i edgeA'EAasAAa'Acases
**Interaktywny spis:** [10.1 Migracja do STRICT](#ch-10-1) A'as [10.2 Anchors/Fill vs krawA'"A"Edzie](#ch-10-2) A'as [10.3 Splitter/Arity](#ch-10-3)
## 10.1 Migracja do STRICT {: #ch-10-1 }
- WejA"aAa'Lzcie dowolne A'EAa'A ' `ensureStrictOtui()` A'EAa'A ' `parse` A'EAa'A ' `autofixAst()` A'EAa'A ' `serializeAst()`.
## 10.2 Anchors/Fill vs krawA'"A"Edzie {: #ch-10-2 }
**BA"aA'AA'"A'ADNY OTUI**
UIWidget
  id: box
  anchors.fill: parent
  anchors.left: parent.left
```
**PO NAPRAWIE (autofix)**
UIWidget
  id: box
  anchors.fill: parent
```
## 10.3 Splitter/Arity {: #ch-10-3 }
**BA"aA'AA'"A'ADNY OTUI**
Splitter
  id: split
  size: 300 160

  Panel
    id: left

```
**PO NAPRAWIE (manualnej)**
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
## 11. Indeks haseA"aAa'L
- STRICT A'EAasAAA AST A'EAasAAA Macierz A'EAasAAA Walidator A'EAasAAA AutoA'EAasAAa'Anaprawy A'EAasAAA RoundA'EAasAAa'Atrip A'EAasAAA Splitter A'EAasAAA TabBar/TabWidget A'EAasAAA StatusOverlay A'EAasAAA Scroll pairing

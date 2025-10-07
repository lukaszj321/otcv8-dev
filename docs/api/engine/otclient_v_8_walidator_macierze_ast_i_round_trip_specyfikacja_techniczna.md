# **Pakiet:** `otc_core_v1/engine` Ă„â€šĂ˘â‚¬ĹˇÂ· **Wersja:** 1.0   
**Cel:** Jednolita, operacyjna specyfikacja **parsera/serializera OTUI (STRICT)**, **walidatora** i **macierzy dozwolonych dzieci**. Dokument jest fundamentem dla edytora TS (Sparky) oraz testÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw roundĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âtrip.

---
## Spis treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci
- [0. Zakres, definicje, zaÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡oÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄenia](#ch-0)
- [1. STRICT OTUI Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť gramatyka i tokenizacja](#ch-1)
- [2. Parser Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ AST (TypeScript)](#ch-2)
- [3. Serializer (AST Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ OTUI STRICT)](#ch-3)
- [4. Macierze dozwolonych dzieci (global)](#ch-4)
  - [4.1 Okna (WindowĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âclass)](#ch-4-1)
  - [4.2 Kontenery (ContentĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âclass)](#ch-4-2)
  - [4.3 Organizacja/Nawigacja](#ch-4-3)
  - [4.4 Dane/Edycja](#ch-4-4)
  - [4.5 WskaÄ‚â€žÄ…Ă„Ä…ÄąĹźniki/Scroll](#ch-4-5)
- [5. Walidator Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť reguÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡y, kody bÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡Ă„â€šâ€žÄ‚Ëâ€žĂ‹ÂdÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw/ostrzeÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄeÄ‚â€žÄ…â€ž](#ch-5)
- [6. AutoĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Ânaprawy deterministyczne](#ch-6)
- [7. Import/Export i roundĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âtrip (edytor Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť plik Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť Lua)](#ch-7)
- [8. API edytora (TS): parse/serialize/validate/autofix](#ch-8)
- [9. Testy: goldeny i snapshoty](#ch-9)
- [10. PrzykÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡ady i edgeĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âcases](#ch-10)
- [11. Indeks haseÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡](#ch-11)

---

<div id="ch-0"></div>
## 0. Zakres, definicje, zaÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡oÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄenia
**Interaktywny spis:** [0.1 Zakres](#ch-0-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [0.2 Definicje](#ch-0-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [0.3 ZaÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡oÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄenia projektowe](#ch-0-3)
## 0.1 Zakres {: #ch-0-1 }
- Pokrycie: *caÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡y pipeline* od tekstu OTUI (STRICT) Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť AST (TS) Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť walidacja Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť autoĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Ânaprawy Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť eksport/import.  
- Zakres UI: komplet taksonomii z czĂ„â€šâ€žÄ‚Ëâ€žĂ‹ÂÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ă„Ä…Ă„ÄľSpecyfikacja UIĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ă„Ä…Ä„ (rozdz. 4) + presety kanoniczne.
## 0.2 Definicje {: #ch-0-2 }
- **STRICT OTUI** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť format bezkomentarzowy, LF, wciĂ„â€šâ€žÄ‚Ëâ€žĂ‹Âcia 2 sp., kolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ GEOMETRIAĂ„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™STYLĂ„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ZACHOWANIE.
- **AST** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť drzewo `WidgetNode`, deterministyczne klucze i kolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ dzieci.
- **Macierz** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť tablica dozwolonych dzieci dla par (parent, slot).
## 0.3 ZaÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡oÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄenia projektowe {: #ch-0-3 }
- **DeterministycznoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ**: ten sam AST Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ ten sam OTUI (bitĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âidentyczny, przy tej samej wersji serializera).  
- **Idempotencja**: `parse(serialize(ast))` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â°Ä‚â€ąĂ˘â‚¬Ë‡ `normalize(ast)`.
- **Brak magii**: walidator zgÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡asza i *tylko* przewidywalnie naprawia.

---

<div id="ch-1"></div>
## 1. STRICT OTUI Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť gramatyka i tokenizacja
**Interaktywny spis:** [1.1 Zasady formatowania](#ch-1-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [1.2 Tokeny](#ch-1-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [1.3 Szkic EBNF](#ch-1-3)
## 1.1 Zasady formatowania {: #ch-1-1 }
- **WciĂ„â€šâ€žÄ‚Ëâ€žĂ‹Âcia**: 2 spacje na poziom. **Zakaz tabÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw**.  
- **KoÄ‚â€žÄ…â€žce linii**: LF. **Bez BOM**.  
- **Brak komentarzy** w blokach `.otui`.  
- **KolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ atrybutÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw** w kaÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄdym wĂ„â€šâ€žÄ‚Ëâ€žĂ‹ÂÄ‚â€žÄ…Ă„Ä…ÄąĹźle: GEOMETRIA Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ STYL Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ ZACHOWANIE.
## 1.2 Tokeny {: #ch-1-2 }
- SÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡owa kluczowe typÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw: `MainWindow`, `StaticMainWindow`, `MiniWindow`, `ContainerWindow`, `DialogWindow`, `UIWidget`, `Panel`, `GroupBox`, `Titlebar`, `Toolbar`, `TabBar`, `TabWidget`, `Splitter`, `HorizontalSeparator`, `StatusOverlay`, `Label`, `Button`, `CheckBox`, `TextEdit`, `PasswordTextEdit`, `MultilineTextEdit`, `ComboBox`, `TextList`, `ProgressBar`, `VerticalScrollBar`, `HorizontalScrollBar`.
- Operator dziedziczenia: `<` (np. `MiniWindow < MainWindow`).
- Identyfikatory: `id: <slug>`; Ä‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡aÄ‚â€žÄ…â€žcuchy w `!text: tr('...')`; liczby caÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡kowite; kolory `#AARRGGBB` lub `alpha`.
## 1.3 Szkic EBNF (pogglĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦dowy) {: #ch-1-3 }
`$fenceInfo
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
## 2. Parser Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ AST (TypeScript)
**Interaktywny spis:** [2.1 KsztaÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡t AST](#ch-2-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [2.2 Normalizacja](#ch-2-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [2.3 Stabilizacja kolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci](#ch-2-3)
## 2.1 KsztaÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡t AST {: #ch-2-1 }
`$fenceInfo
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
- UzupeÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡nij brakujĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦ce struktury: `children = []`, `style = {}` gdy potrzebne.  
- ZamieÄ‚â€žÄ…â€ž `style.text` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ w serializacji na `!text: tr('...')`.  
- ZastĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦p `size` parĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦ `width/height` podczas walidacji kotwic (na potrzeby reguÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡), ale w serializacji zachowuj wejÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşciowĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦ postaĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ.
## 2.3 Stabilizacja kolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci {: #ch-2-3 }
- Atrybuty: najpierw **GEOMETRIA**, potem **STYL**, na koÄ‚â€žÄ…â€žcu **ZACHOWANIE** (events/states).  
- Dzieci: sortuj stabilnie po `(slotPriority, y, x, id)` jeÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşli edytor posiada grid/snapping; inaczej po kolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci wczytania.

---

<div id="ch-3"></div>
## 3. Serializer (AST Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ OTUI STRICT)
**Interaktywny spis:** [3.1 ReguÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡y wypisywania](#ch-3-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [3.2 Escaping i i18n](#ch-3-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [3.3 Sanityzacja koÄ‚â€žÄ…â€žcowa](#ch-3-3)
## 3.1 ReguÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡y wypisywania {: #ch-3-1 }
- WciĂ„â€šâ€žÄ‚Ëâ€žĂ‹Âcie: **2 spacje**.  
- Puste wartoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci pomijaj.  
- Sekcja kolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci: GEOMETRIA (`id`, `size`/`width`/`height`, `anchors.*`, `margin-*`, `padding`) Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ STYL Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ ZACHOWANIE (`@on*`, `$state:` bloki).
## 3.2 Escaping i i18n {: #ch-3-2 }
- `style.text` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `!text: tr('...')`, `'` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `\'`.  
- Kolory tylko `#AARRGGBB` lub `alpha`.
## 3.3 Sanityzacja koÄ‚â€žÄ…â€žcowa {: #ch-3-3 }
- UsuÄ‚â€žÄ…â€ž taby, trailing spaces, wymuÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹş LF.  
- Brak komentarzy w wynikowym `.otui`.

---

<div id="ch-4"></div>
## 4. Macierze dozwolonych dzieci (global)
**Interaktywny spis:** [4.1 Okna](#ch-4-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [4.2 Kontenery](#ch-4-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [4.3 Organizacja](#ch-4-3) Ă„â€šĂ˘â‚¬ĹˇÂ· [4.4 Dane/Edycja](#ch-4-4) Ă„â€šĂ˘â‚¬ĹˇÂ· [4.5 WskaÄ‚â€žÄ…Ă„Ä…ÄąĹźniki/Scroll](#ch-4-5)

> **Legenda:** Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś dozwolone Ă„â€šĂ˘â‚¬ĹˇÂ· Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ zabronione Ă„â€šĂ˘â‚¬ĹˇÂ· Ă„â€šĂ‹ÂĂ„Ä…Ă‹â€ˇ  warunkowe (patrz uwagi).
## 4.1 Okna (WindowĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âclass) {: #ch-4-1 }
**MainWindow / StaticMainWindow (root)**
| Dziecko | Status | Uwagi |
|---|:---:|---|
| UIWidget, Panel, GroupBox | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Elementy panelowe.
| Label, Button, CheckBox, TextEdit, PasswordTextEdit, MultilineTextEdit, ComboBox | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Formularze i akcje.
| TextList | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Wymaga pary z VerticalScrollBar przy overflow (Ă„â€šĂ‹ÂĂ„Ä…Ă‹â€ˇ ).
| ProgressBar, HorizontalSeparator | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť
| TabBar, TabWidget, Splitter | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Splitter: dokÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡adnie 2 dzieci (Ă„â€šĂ‹ÂĂ„Ä…Ă‹â€ˇ ).
| StatusOverlay | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Warstwa wierzchnia, bez zÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡oÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄonych dzieci (Ă„â€šĂ‹ÂĂ„Ä…Ă‹â€ˇ ).
| *Window (Main/Static/Mini/Container/Dialog) | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ | Zakaz okienĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âdzieci.
| ScrollBar (samotny) | Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ | Zawsze para z treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşciĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦.

**MiniWindow / ContainerWindow / DialogWindow**
- Slot `titlebar`: Label, Button, UIWidget(ikona) Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś; listy/edytory/scroll Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“.  
- Slot `content`: elementy panelowe Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś; oknaĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âdzieci Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“.  
- Slot `footer` (Mini/Dialog): Button/Label/ProgressBar Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś; listy/edytory/scroll Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“.
## 4.2 Kontenery (ContentĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âclass) {: #ch-4-2 }
| Parent | Dozwolone dzieci | Niedozwolone/uwagi |
|---|---|---|
| UIWidget | Wszystkie panelowe (Label/Button/Inputs/List/Progress/Scroll/Separator/StatusOverlay) | *Window Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ |
| Panel | j.w. | *Window Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ |
| GroupBox | `header: Label` Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś, `content: panelowe` Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Scroll w header Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ |
| TabWidget | TreÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ aktywnej zakÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡adki: panelowe Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | *Window Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“; sam TabBar nie tu |
| StatusOverlay | Label, ProgressBar, Button(cancel) Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€ś | Listy/edytory/okna Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ |
## 4.3 Organizacja/Nawigacja {: #ch-4-3 }
| Komponent | Dozwolone dzieci | Niedozwolone/uwagi |
|---|---|---|
| Titlebar | Label, Button, UIWidget(ikona) | Scroll/listy/edytory Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ |
| Toolbar | Button, HorizontalSeparator | Inne Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ |
| TabBar | Button (zakÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡adki) | TreÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ zakÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡adek Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť trafia do TabWidget |
| Splitter | **DokÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡adnie 2** dzieci: Panel/UIWidget/GroupBox | Okna/Scroll Ă„â€šĂ‹ÂĂ„Ä…Ă˘â‚¬Ĺźâ€“ |
| HorizontalSeparator | Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť | **Bez dzieci** |
## 4.4 Dane/Edycja {: #ch-4-4 }
| Komponent | Dzieci |
|---|---|
| Label, Button, CheckBox, TextEdit, PasswordTextEdit, ComboBox, ProgressBar, ScrollBar | **Brak** |
| MultilineTextEdit | **Brak**; przewijanie przez sĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦siedni Vertical/HorizontalScrollBar |
| TextList | **Brak** rĂ„â€šâ€žÄ‚Ëâ€žĂ‹Âcznych dzieci; wiersze generowane jako `UIWidget` (ListRow) runtime/templatem |
## 4.5 WskaÄ‚â€žÄ…Ă„Ä…ÄąĹźniki/Scroll {: #ch-4-5 }
| Komponent | Zasady |
|---|---|
| VerticalScrollBar | Sibling przewijanej treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci; dock **right**; treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ kotwiczy `right: scroll.left` |
| HorizontalScrollBar | Sibling przewijanej treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci; dock **bottom**; treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ kotwiczy `bottom: hscroll.top` |

---

<div id="ch-5"></div>
## 5. Walidator Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť reguÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡y, kody bÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡Ă„â€šâ€žÄ‚Ëâ€žĂ‹ÂdÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw/ostrzeÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄeÄ‚â€žÄ…â€ž
**Interaktywny spis:** [5.1 BÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡Ă„â€šâ€žÄ‚Ëâ€žĂ‹Âdy (E)](#ch-5-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [5.2 OstrzeÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄenia (W)](#ch-5-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [5.3 Raport](#ch-5-3)
## 5.1 BÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡Ă„â€šâ€žÄ‚Ëâ€žĂ‹Âdy (E) {: #ch-5-1 }
- **E001 STRICT/Format** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť taby/BOM/komentarze/trailing spaces.  
- **E010 Anchors/Conflict** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť `anchors.fill` + inne kotwice.  
- **E020 Window/Nesting** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť okno (`*Window`) jako dziecko okna.  
- **E030 Scroll/Orphan** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť ScrollBar bez sparowanej treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci.  
- **E031 Scroll/Pairing** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť brak kotwicy treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci do ScrollBar (`right: scroll.left` lub `bottom: hscroll.top`).  
- **E040 Text/i18n** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť staÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡y tekst bez `tr()` (w OTUI).  
- **E050 Splitter/Arity** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť != 2 dzieci.  
- **E060 Titlebar/Children** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť niedozwolone dziecko w `titlebar`.
## 5.2 OstrzeÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄenia (W) {: #ch-5-2 }
- **W101 Width/AutoFit** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť okno dokowane z `width` (sugeruj usuniĂ„â€šâ€žÄ‚Ëâ€žĂ‹Âcie).  
- **W110 Margins/Odd** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť nieparzyste marginesy (snapping 2 px).  
- **W120 Scroll/StepMismatch** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť `step` niezgodny z wielkoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşciĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦ wiersza/slotu.  
- **W130 Keyboard/Hints** Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť brak `@onEnter/@onEscape` w oknie dialogowym.
## 5.3 Raport {: #ch-5-3 }
- Struktura: `{code, severity, path, message, fix?}`.  
- `path` = Ä‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşcieÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄka wĂ„â€šâ€žÄ‚Ëâ€žĂ‹ÂzÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡Ä‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw (`main/content/items`).

---

<div id="ch-6"></div>
## 6. AutoĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Ânaprawy deterministyczne
**Interaktywny spis:** [6.1 STRICT fixups](#ch-6-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [6.2 Anchors/Layout](#ch-6-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [6.3 Scroll pairing](#ch-6-3)
## 6.1 STRICT fixups {: #ch-6-1 }
- UsuÄ‚â€žÄ…â€ž taby/BOM/komentarze; przytnij trailing spaces; wymuÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹş LF.
- UporzĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦dkuj kolejnoÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ atrybutÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw (GEOMETRIAĂ„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™STYLĂ„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ZACHOWANIE).
## 6.2 Anchors/Layout {: #ch-6-2 }
- JeÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşli sĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦ `anchors.left` + `anchors.right` **i** `width` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ usuÄ‚â€žÄ…â€ž `width` (AutoĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âfit).  
- Rozdziel `size` na `width/height` tylko na potrzeby walidacji, nie w serializacji (zachowaj wejÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşciowy idiom).
## 6.3 Scroll pairing {: #ch-6-3 }
- Dla `TextList`/`MultilineTextEdit` dodaj brakujĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦cy `VerticalScrollBar` jako sibling (po prawej) i dodaj kotwicĂ„â€šâ€žÄ‚Ëâ€žĂ‹Â treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşci `right: scroll.left`.

---

<div id="ch-7"></div>
## 7. Import/Export i roundĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âtrip (edytor Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť plik Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€ť Lua)
**Interaktywny spis:** [7.1 Import z plikÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw `.otui`](#ch-7-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [7.2 Import z Lua (blok string)](#ch-7-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [7.3 Eksport](#ch-7-3)
## 7.1 Import z plikÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw `.otui` {: #ch-7-1 }
- Wczytaj, znormalizuj (STRICT), sparsuj do AST. Zachowaj *oryginalny ukÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡ad* do porÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬ĹˇwnaÄ‚â€žÄ…â€ž.
## 7.2 Import z Lua (blok string) {: #ch-7-2 }
- Wykryj staÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡e `local <Name>_OTUI = [[...]]`; wytnij treÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‹â€ˇ; sprawdÄ‚â€žÄ…Ă„Ä…ÄąĹź STRICT; sparsuj.  
- OstrzeÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄenie, gdy blok zawiera komentarze Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť niedozwolone w OTUI (mimo bycia w Lua).
## 7.3 Eksport {: #ch-7-3 }
- Do pliku `.otui` (kanoniczny cel runtime).  
- Opcjonalnie: *roundĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âtrip do Lua* Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬â€ť odÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşwieÄ‚â€žÄ…Ä‚â€žĂ‹ĹĄ istniejĂ„â€šâ€žÄ‚ËĂ˘â€šÂ¬Ă‚Â¦cy blok `[[...]]` bitĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âidentycznie po `ensureStrictOtui()`.

---

<div id="ch-8"></div>
## 8. API edytora (TS): parse/serialize/validate/autofix
**Interaktywny spis:** [8.1 Interfejsy](#ch-8-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [8.2 PrzepÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡ywy](#ch-8-2)
## 8.1 Interfejsy {: #ch-8-1 }
`$fenceInfo
export function parseOtui(text: string): WidgetNode[];
export function serializeAst(nodes: WidgetNode[]): string; // STRICT OTUI
export function ensureStrictOtui(text: string): string;     // tylko format
export interface ValidationIssue { code: string; severity: 'error'|'warning'; path: string; message: string; fix?: string; }
export function validateAst(nodes: WidgetNode[]): ValidationIssue[];
export function autofixAst(nodes: WidgetNode[]): { nodes: WidgetNode[]; changes: ValidationIssue[] };
```
## 8.2 PrzepÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡ywy {: #ch-8-2 }
- **Projekt Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Walidacja Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Serializacja**.  
- **Import (plik/Lua) Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Parser Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Normalizacja Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Walidacja Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Edycja Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Serializacja Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ Eksport (plik/Lua)**.

---

<div id="ch-9"></div>
## 9. Testy: goldeny i snapshoty
**Interaktywny spis:** [9.1 Goldeny roundĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âtrip](#ch-9-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [9.2 Snapshoty wizualne](#ch-9-2)
## 9.1 Goldeny roundĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âtrip {: #ch-9-1 }
- Zestaw `X.otui` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `parse` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `serialize` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ porÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇwnanie bitĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚ÂpoĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âbicie.  
- DokÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡adaj przypadki: okna, scroll pairing, Splitter, TabBar/TabWidget.
## 9.2 Snapshoty wizualne {: #ch-9-2 }
- Render testowy po stronie klienta (lub symulacja) i porÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇwnania pikselowe dla kluczowych presetÄ‚â€žĂ˘â‚¬ĹˇĂ„Ä…Ă˘â‚¬Ĺˇw.

---

<div id="ch-10"></div>
## 10. PrzykÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡ady i edgeĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âcases
**Interaktywny spis:** [10.1 Migracja do STRICT](#ch-10-1) Ă„â€šĂ˘â‚¬ĹˇÂ· [10.2 Anchors/Fill vs krawĂ„â€šâ€žÄ‚Ëâ€žĂ‹Âdzie](#ch-10-2) Ă„â€šĂ˘â‚¬ĹˇÂ· [10.3 Splitter/Arity](#ch-10-3)
## 10.1 Migracja do STRICT {: #ch-10-1 }
- WejÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąĹşcie dowolne Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `ensureStrictOtui()` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `parse` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `autofixAst()` Ă„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬Ă‚Â â€™ `serializeAst()`.
## 10.2 Anchors/Fill vs krawĂ„â€šâ€žÄ‚Ëâ€žĂ‹Âdzie {: #ch-10-2 }
**BÄ‚â€žÄ…Ä‚â€šĂ‚ÂĂ„â€šâ€žÄ‚â€šĂ‚ÂDNY OTUI**
`$fenceInfo
UIWidget
  id: box
  anchors.fill: parent
  anchors.left: parent.left
```
**PO NAPRAWIE (autofix)**
`$fenceInfo
UIWidget
  id: box
  anchors.fill: parent
```
## 10.3 Splitter/Arity {: #ch-10-3 }
**BÄ‚â€žÄ…Ä‚â€šĂ‚ÂĂ„â€šâ€žÄ‚â€šĂ‚ÂDNY OTUI**
`$fenceInfo
Splitter
  id: split
  size: 300 160

  Panel
    id: left

```
**PO NAPRAWIE (manualnej)**
`$fenceInfo
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
## 11. Indeks haseÄ‚â€žÄ…Ä‚ËĂ˘â€šÂ¬ÄąË‡
- STRICT Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â AST Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â Macierz Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â Walidator Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â AutoĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Ânaprawy Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â RoundĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚ËĂ˘â€šÂ¬Ă‚Âtrip Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â Splitter Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â TabBar/TabWidget Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â StatusOverlay Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ‚Â Scroll pairing




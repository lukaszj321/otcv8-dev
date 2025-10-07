# OTUI Lint Rules (MASTER) - Specyfikacja dla **OTClient Studio**

> Cel: kompletny katalog reguL' lint/autoa'fix dla **OTUI/OTML** uLLywany przez Studio. Dokument definiuje: zachowania reguL', algorytmy autoa'fix, format diagnostyk, konfiguracje, testa'wektory, integracje z edytorem i wymagania jakoLciowe. **Transfer 1:1** - gotowe do bezpoLredniej implementacji.

---
## 0) ZaL'oLLenia wspolne
- **Parser/AST**: zgodnie z dokumentem "Parser & Schemas: AST + JSON Schema (OTClient Studio)" ( OTUI AST). KaLLdy wezeL' posiada `loc` (`file`, `start`, `end`).
- **Kategoryzacja atrybutow**: `GEOMETRY`, `STYLE`, `BEHAVIOR` (lista bazowa w 1.3 tego dokumentu; rozszerzalna).
- **DeterministycznoLc**: wyniki lint i autoa'fix sa deterministyczne (stabilny sort atrybutow, niezmiennoLc biaL'ych znakow poza miejscem naprawy).
- **Backup i diff**: przy autoa'fix zapisywany jest plik `.bak` oraz generowany jest diff (Unified) do podgladu w UI.
- **Format diagnostyk** (kanaL' do edytora):
{
  "code": "OTUI-001",
  "severity": "ERROR|WARN|INFO|HINT",
  "message": "opis problemu",
  "fix": {"title": "opis auto-fix", "edits": [{"file":"...","range":{"start":{...},"end":{...}},"text":"..."}]},
  "loc": {"file":"...","start":{"offset":...},"end":{"offset":...}},
  "meta": {"category":"GEOMETRY|STYLE|BEHAVIOR", "widget":"MainWindow", "key":"width"}
}
```

---
## 1) Katalog reguL' (z autoa'fix tam, gdzie bezpieczny)

> **Legenda pol:** `Opis`, `Wykrywanie`, `Autoa'fix`, `PrzykL'ad (before/after)`, `Severity`, `BezpieczeL"stwo`, `Konfiguracja`.
## OTUIa'001 - KolejnoLc pol: GEOMETRIA a' STYL a' ZACHOWANIE (**autoa'fix**)
- **Opis**: w obrebie kaLLdego bloku deklaracji widLLetu atrybuty musza byc uporzadkowane wg kategorii.
- **Wykrywanie**: przeanalizuj liste `KV` w `Decl.body`; jeLli sekwencja kategorii zawiera inwersje (np. `STYLE` przed `GEOMETRY`), zgL'oL problem.
- **Autoa'fix**: stabilne sortowanie kluczy: najpierw wszystkie `GEOMETRY`, potem `STYLE`, potem `BEHAVIOR`. Zachowaj wzgledna kolejnoLc wewnatrz kategorii i przenieL komentarze razem z para `KV`.
- **PrzykL'ad**
# BEFORE
Window < UIWidget {
  text: "Hello"
  width: 300
  id: main
}
# AFTER
Window < UIWidget {
  width: 300        # GEOMETRY
  text: "Hello"    # STYLE
  id: main          # BEHAVIOR
}
```
- **Severity**: WARN (podniesienie do ERROR konfigurowalne).
- **BezpieczeL"stwo**: bezpieczny autoa'fix.
- **Konfiguracja**:
{"OTUI-001":{"enabled":true,"severity":"WARN"}}
```
## OTUIa'002 - Statyczne teksty musza uLLywac `tr()` (**autoa'fix**)
- **Opis**: literaL'y string w atrybutach kategorii STYLE (np. `text`) musza byc opakowane `tr("...")`.
- **Wykrywanie**: `KV.key` a STYLE a `value.type == StringLiteral` a `value.value` nie zaczyna sie od `tr(`.
- **Autoa'fix**: zamieL" `"Tekst"` a' `tr("Tekst")`. Wyklucz klucze `id`, nazwy klas/stylow.
- **PrzykL'ad**
# BEFORE
Label < UIWidget { text: "Start" }
# AFTER
Label < UIWidget { text: tr("Start") }
```
- **Severity**: WARN.
- **BezpieczeL"stwo**: bezpieczny autoa'fix.
- **Konfiguracja**: `{ "OTUI-002": {"enabled": true, "severity": "WARN", "allowList": ["tooltip"] } }`
## OTUIa'003 - Sprzeczne `anchors` / `margins` (detekcja)
- **Opis**: wykrywa sprzecznoLci (np. jednoczesne kotwice wykluczajace sie lub ujemne marginesy tam, gdzie to niedozwolone w projekcie).
- **Wykrywanie**: analizuj wartoLci `anchors` (obiekt/array) i `margin/a|`; reguL'y domenowe: brak `left`+`right` bez `width` (jeLli projekt tak definiuje), brak ujemnych `margin`.
- **Autoa'fix**: brak (tylko sugestie: usuL" `right` lub dodaj `width`).
- **Severity**: ERROR (domyLlnie).
- **BezpieczeL"stwo**: brak autoa'fixu.
## OTUIa'004 - Zasob nie istnieje (STYLE a' `image`, `font`, `style`)
- **Opis**: odwoL'anie do pliku zasobu, ktorego nie ma w projekcie.
- **Wykrywanie**: sprawdLs LcieLLki wzgledem `project-root/data/a|` lub mapy zasobow (`assets-map.json`).
- **Autoa'fix**: brak; podaj propozycje (fuzzy match) najbliLLszych nazw.
- **Severity**: ERROR.
## OTUIa'005 - Zduplikowane `id` w obrebie pliku
- **Opis**: `KV.key == id` nie moLLe wystapic wielokrotnie z ta sama wartoLcia w pliku.
- **Wykrywanie**: deduplikacja w `OTUIFile.body` (poziom pliku).
- **Autoa'fix**: brak; zaproponuj nowe `id` (`<id>_1`).
- **Severity**: ERROR.
## OTUIa'006 - Konwencja nazewnictwa `id`
- **Opis**: `id` dopuszcza `[a-z0-9_]+` (konfigurowalne).
- **Wykrywanie**: regex na `Identifier|StringLiteral`.
- **Autoa'fix**: opcjonalna transformacja do lower_snake_case (jeLli wL'aczona).
- **Severity**: WARN.
## OTUIa'007 - Nieznany atrybut widLLetu
- **Opis**: klucz `KV.key` nie znajduje sie w dozwolonych dla danego widLLetu (lista referencyjna + allowa'list projektu).
- **Wykrywanie**: porownanie do bazy atrybutow; jeLli brak dopasowania a' problem.
- **Autoa'fix**: brak; podpowiedLs najbliLLszych kluczy (Levenshtein).
- **Severity**: WARN.
## OTUIa'008 - Atrybut przestarzaL'y (deprecated)
- **Opis**: uLLycie atrybutu oznaczonego jako przestarzaL'y w profilu projektu.
- **Wykrywanie**: dopasowanie do listy `deprecatedAttributes` (konfiguracja).
- **Autoa'fix**: propozycja zamiennika (jeLli podany w konfiguracji).
- **Severity**: WARN.
## OTUIa'009 - Normalizacja booleanow
- **Opis**: wartoLci bool powinny byc `true|false` (nie `0|1|"true"`).
- **Wykrywanie**: `value` typu `Identifier/StringLiteral/NumberLiteral` odwzorowuje bool.
- **Autoa'fix**: zamieL" na `true/false`.
- **Severity**: HINT.
## OTUIa'010 - Format kolorow
- **Opis**: akceptowane formaty kolorow wg projektu (np. `#RRGGBB`, `rgba(...)`).
- **Wykrywanie**: regex na `StringLiteral`.
- **Autoa'fix**: konwersja do kanonicznego formatu (jeLli moLLliwa).
- **Severity**: WARN.
## OTUIa'011 - Jednostki wymiarow/liczb
- **Opis**: liczby powinny byc bez jednostek (lub z konkretna notacja - zaleLLnie od projektu).
- **Wykrywanie**: `NumberLiteral` OK; `StringLiteral` z sufiksem jednostki a' problem (opcjonalnie).
- **Autoa'fix**: usuniecie sufiksu, jeLli wL'aczone.
- **Severity**: HINT/WARN.
## OTUIa'012 - Cykl dziedziczenia widLLetow
- **Opis**: `Decl.base` tworzy cykl (A < B, B < C, C < A).
- **Wykrywanie**: graf dziedziczenia per plik (lub caL'y projekt); detekcja cykli.
- **Autoa'fix**: brak; raport LcieLLki cyklu.
- **Severity**: ERROR.
## OTUIa'013 - Puste deklaracje
- **Opis**: `Decl` bez atrybutow i potomkow.
- **Wykrywanie**: `Decl.body.length == 0`.
- **Autoa'fix**: usuL" pusty blok (opcjonalnie, jeLli nie referencjonowany).
- **Severity**: INFO.
## OTUIa'014 - Niezreferencjonowany widLLet (analiza projektowa)
- **Opis**: `Decl` nigdy nie L'adowany przez `g_ui.loadUI` ani dziedziczony.
- **Wykrywanie**: korelacja z `project-index.json.relations.lua_to_otui` i baza typow.
- **Autoa'fix**: brak; informacja do porzadkow.
- **Severity**: INFO.
## OTUIa'015 - OdnoLnik do stylu nie istnieje
- **Opis**: `style: "a|"` nie znajduje sie w katalogu stylow projektu.
- **Wykrywanie**: porownanie do listy stylow (assetsa'map lub dedykowana baza stylow).
- **Autoa'fix**: brak; fuzzy proposals.
- **Severity**: WARN.
## OTUIa'016 - Event handler w kluczu `on...` ma niekanoniczna wartoLc
- **Opis**: wartoLci eventow powinny byc identyfikatorami (nie stringami) - zaleLLnie od konwencji projektu.
- **Wykrywanie**: `key` zaczyna sie od `on` + wielka litera; `value.type != Identifier`.
- **Autoa'fix**: usuL" cudzysL'owy (opcjonalnie).
- **Severity**: HINT/WARN.
## OTUIa'017 - Atrybuty powielone w obrebie tego samego `Decl`
- **Opis**: ten sam `key` wystepuje wielokrotnie - ostatni wygrywa (nieczytelne).
- **Wykrywanie**: duplikaty `KV.key` w `Decl.body`.
- **Autoa'fix**: scal albo usuL" duplikaty (zachowaj ostatni) - **opcjonalne**.
- **Severity**: WARN.
## OTUIa'018 - BiaL'e znaki i wciecia (2 spacje)
- **Opis**: standaryzacja wciec i trailing spaces.
- **Wykrywanie**: tokenizer whitespace; linie z tabami/koL"cowkami spacji.
- **Autoa'fix**: konwersja TABa'2 spacje, trim koL"cowek.
- **Severity**: HINT.
## OTUIa'019 - Komentarze (#) format
- **Opis**: komentarz powinien poprzedzac deklaracje lub stac po wartoLci (a nie w Lrodku tokena).
- **Wykrywanie**: pozycje `Comment` vs `KV`/`Decl`.
- **Autoa'fix**: przenieL komentarz do poprawnej pozycji (jeLli moLLliwe).
- **Severity**: HINT.
## OTUIa'020 - Klucze nieobsL'ugiwane przez dany typ bazowy
- **Opis**: atrybut zarezerwowany dla innego typu (np. `icon` na widLLecie, ktory go nie wspiera - wg bazy projektu).
- **Wykrywanie**: mapowanie `Type`a'dozwolone atrybuty.
- **Autoa'fix**: brak.
- **Severity**: WARN.

---
## 2) Mapowanie kategorii atrybutow (bazowa lista rozszerzalna)
- **GEOMETRY**: `x,y,width,height,anchors,margin,padding,min-width,max-width,min-height,max-height`
- **STYLE**: `font,color,image,style,opacity,icon,background,spacing,text`
- **BEHAVIOR**: `id,focusable,draggable,enabled,visible,onClick,onText,tooltip`
> Lista jest punktem startowym; moLLe zostac poszerzona w `otui-rules.json`.

---
## 3) Integracja z edytorem (Monaco) - diagnostyka i Quick Fix
- **Publish diagnostyk**: na kaLLdy zapis i/lub po krotkim debounce (150 ms) po zmianie.
- **Format**: jak w 0; severity mapowane na kolor/ikone.
- **Quick Fix**: prezentuj `fix.title`; po akceptacji wykonaj `edits[]` (wspieraj multia'file).
- **Podglad diff**: dla autoa'fixow wymagajacych wiekszej zmiany (OTUIa'001) pokaLL unified diff.

---
## 4) Konfiguracja reguL' (JSON)
{
  "$schemaVersion": 1,
  "rules": {
    "OTUI-001": {"enabled": true,  "severity": "WARN"},
    "OTUI-002": {"enabled": true,  "severity": "WARN", "allowList": ["tooltip"]},
    "OTUI-003": {"enabled": true,  "severity": "ERROR"},
    "OTUI-004": {"enabled": true,  "severity": "ERROR", "assetsRoot": "data/"},
    "OTUI-005": {"enabled": true,  "severity": "ERROR"},
    "OTUI-006": {"enabled": false, "severity": "WARN", "pattern": "^[a-z0-9_]+$", "autoTransform": false},
    "OTUI-007": {"enabled": true,  "severity": "WARN", "allow": ["customAttribute"]},
    "OTUI-008": {"enabled": true,  "severity": "WARN", "map": {"oldAttr":"newAttr"}},
    "OTUI-009": {"enabled": true,  "severity": "HINT"},
    "OTUI-010": {"enabled": true,  "severity": "WARN", "format": "#RRGGBB"},
    "OTUI-011": {"enabled": false, "severity": "HINT"},
    "OTUI-012": {"enabled": true,  "severity": "ERROR"},
    "OTUI-013": {"enabled": true,  "severity": "INFO", "removeEmpty": false},
    "OTUI-014": {"enabled": true,  "severity": "INFO"},
    "OTUI-015": {"enabled": true,  "severity": "WARN"},
    "OTUI-016": {"enabled": false, "severity": "HINT"},
    "OTUI-017": {"enabled": true,  "severity": "WARN", "removeDuplicates": false},
    "OTUI-018": {"enabled": true,  "severity": "HINT"},
    "OTUI-019": {"enabled": true,  "severity": "HINT"},
    "OTUI-020": {"enabled": true,  "severity": "WARN"}
}
}
```

---
## 5) Algorytmy autoa'fix (pseudokod TS)
## 5.1 OTUIa'001 (sort kategorii)
function fixOrder(decl: Decl): Edit[] {
  const groups = {G: [] as KV[], S: [] as KV[], B: [] as KV[]};
  for (const kv of decl.body.filter(isKV)) {
    const cat = categorize(kv.key); // GEOMETRY|STYLE|BEHAVIOR
    if (cat === 'GEOMETRY') groups.G.push(kv);
    else if (cat === 'STYLE') groups.S.push(kv);
    else groups.B.push(kv);
}
  const sorted = [...groups.G, ...groups.S, ...groups.B];
  if (sameOrder(decl.body, sorted)) return [];
  const text = renderKVWithComments(sorted);
  return [{ file: decl.loc.file, range: rangeOfKVBlock(decl), text }];
}
```
## 5.2 OTUIa'002 (wrap `tr()`)
function wrapTr(kv: KV): Edit[] {
  if (kv.value.type !== 'StringLiteral') return [];
  if (kv.key === 'id') return [];
  return [{
    file: kv.loc.file,
    range: kv.value.loc,
    text: `tr(${JSON.stringify(kv.value.value)})`
  }];
}
```
## 5.3 OTUIa'009 (booleany)
function normalizeBool(kv: KV): Edit[] {
  const val = kv.value;
  const toBool = (s: string) => /^(?:true|1)$/i.test(s);
  if (val.type === 'StringLiteral')
    return [{file: kv.loc.file, range: val.loc, text: toBool(val.value) ? 'true' : 'false'}];
  if (val.type === 'NumberLiteral')
    return [{file: kv.loc.file, range: val.loc, text: val.value === 0 ? 'false' : 'true'}];
  if (val.type === 'Identifier' && /^(true|false)$/i.test(val.name) === false)
    return [{file: kv.loc.file, range: val.loc, text: toBool(val.name) ? 'true' : 'false'}];
  return [];
}
```

---
## 6) Testa'wektory (minimalny zestaw regresji)
## 6.1 KolejnoLc pol
**WejLcie**
W < UIWidget { text: "x" width: 1 id: a }
```
**Oczekiwane**: pojedyncza diagnostyka `OTUI-001` + autoa'fix sortujacy.
## 6.2 `tr()` wrap
**WejLcie**
L < UIWidget { text: "Start" id: start }
```
**Oczekiwane**: `OTUI-002` z autoa'fix a' `text: tr("Start")`.
## 6.3 Zasob nie istnieje
**WejLcie**
B < UIWidget { image: "images/missing.png" }
```
**Oczekiwane**: `OTUI-004` (ERROR), propozycje fuzzy jeLli `images/button.png` istnieje.
## 6.4 Duplikat `id`
**WejLcie**
A < UIWidget { id: x }
B < UIWidget { id: x }
```
**Oczekiwane**: `OTUI-005` na drugim wystapieniu.

---
## 7) Kody bL'edow parsera/enginu (dla OTUI)
- `OTUI_PARSE_001` - niezamkniety blok `{` (ParseError)
- `OTUI_PARSE_002` - nieznany token/literaL' a' potraktowano jako `Identifier`
- `OTUI_ENGINE_001` - nieprawidL'owa kategoria atrybutu (brak w mapie)
- `OTUI_ENGINE_100` - bL'ad I/O przy sprawdzaniu zasobow

---
## 8) WydajnoLc i limity
- ReguL'y jednoprzebiegowe; jedna analiza AST/plik.
- Sprawdzenie zasobow buforowane (cache LcieLLek a' hash katalogow assets).
- CaL'y lint dla pliku < 50 ms (target), batch 100 plikow < 2 s.

---
## 9) Checklisty wdroLLeniowe (dla warstwy Lint)
- [ ] Implementacja wszystkich reguL' OTUIa'001a|020.
- [ ] WL'aczone autoa'fix dla 001/002/009/018; pozostaL'e bezpieczne - opcjonalnie.
- [ ] Konfiguracja reguL' w `otui-rules.json`; integracja w UI (enable/disable, severity).
- [ ] Testy z 6 - zielone; snapshoty zmian po autoa'fix.
- [ ] Cache zasobow i fuzzy propozycje dziaL'aja.

---
## 10) Noty koL"cowe
- ReguL'y sa projektowalne - dopuszcza sie dodawanie wL'asnych rozszerzeL", o ile nie zmieniaja publicznych kontraktow (format diagnostyk i edycji).
- Wszelkie zmiany w zestawie reguL' wymagaja podniesienia `$schemaVersion` w konfiguracji i aktualizacji testa'wektorow.

# OTUI Lint Rules (MASTER) - Specyfikacja dla **OTClient Studio**

> Cel: kompletny katalog regul lint/auto-fix dla **OTUI/OTML** uzywany przez Studio. Dokument definiuje: zachowania regul, algorytmy auto-fix, format diagnostyk, konfiguracje, test-wektory, integracje z edytorem i wymagania jakosciowe. **Transfer 1:1** - gotowe do bezposredniej implementacji.

---
# # 0) Zalozenia wsp�lne
- **Parser/AST**: zgodnie z dokumentem "Parser & Schemas: AST + JSON Schema (OTClient Studio)" (� OTUI AST). Kazdy wezel posiada `loc` (`file`, `start`, `end`).
- **Kategoryzacja atrybut�w**: `GEOMETRY`, `STYLE`, `BEHAVIOR` (lista bazowa w �1.3 tego dokumentu; rozszerzalna).
- **Deterministycznosc**: wyniki lint i auto-fix sa deterministyczne (stabilny sort atrybut�w, niezmiennosc bialych znak�w poza miejscem naprawy).
- **Backup i diff**: przy auto-fix zapisywany jest plik `.bak` oraz generowany jest diff (Unified) do podgladu w UI.
- **Format diagnostyk** (kanal do edytora):
```json
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
# # 1) Katalog regul (z auto-fix tam, gdzie bezpieczny)

> **Legenda p�l:** `Opis`, `Wykrywanie`, `Auto-fix`, `Przyklad (before/after)`, `Severity`, `Bezpieczenstwo`, `Konfiguracja`.
# # # OTUI-001 - Kolejnosc p�l: GEOMETRIA ? STYL ? ZACHOWANIE (**auto-fix**)
- **Opis**: w obrebie kazdego bloku deklaracji widzetu atrybuty musza byc uporzadkowane wg kategorii.
- **Wykrywanie**: przeanalizuj liste `KV` w `Decl.body`; jesli sekwencja kategorii zawiera inwersje (np. `STYLE` przed `GEOMETRY`), zglos problem.
- **Auto-fix**: stabilne sortowanie kluczy: najpierw wszystkie `GEOMETRY`, potem `STYLE`, potem `BEHAVIOR`. Zachowaj wzgledna kolejnosc wewnatrz kategorii i przenies komentarze razem z para `KV`.
- **Przyklad**
```otui
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
- **Bezpieczenstwo**: bezpieczny auto-fix.
- **Konfiguracja**:
```json
{"OTUI-001":{"enabled":true,"severity":"WARN"}}
```
# # # OTUI-002 - Statyczne teksty musza uzywac `tr()` (**auto-fix**)
- **Opis**: literaly string w atrybutach kategorii STYLE (np. `text`) musza byc opakowane `tr("...")`.
- **Wykrywanie**: `KV.key` ? STYLE ? `value.type == StringLiteral` ? `value.value` nie zaczyna sie od `tr(`.
- **Auto-fix**: zamien `"Tekst"` ? `tr("Tekst")`. Wyklucz klucze `id`, nazwy klas/styl�w.
- **Przyklad**
```otui
# BEFORE
Label < UIWidget { text: "Start" }
# AFTER
Label < UIWidget { text: tr("Start") }
```
- **Severity**: WARN.
- **Bezpieczenstwo**: bezpieczny auto-fix.
- **Konfiguracja**: `{ "OTUI-002": {"enabled": true, "severity": "WARN", "allowList": ["tooltip"] } }`
# # # OTUI-003 - Sprzeczne `anchors` / `margins` (detekcja)
- **Opis**: wykrywa sprzecznosci (np. jednoczesne kotwice wykluczajace sie lub ujemne marginesy tam, gdzie to niedozwolone w projekcie).
- **Wykrywanie**: analizuj wartosci `anchors` (obiekt/array) i `margin/.`; reguly domenowe: brak `left`+`right` bez `width` (jesli projekt tak definiuje), brak ujemnych `margin`.
- **Auto-fix**: brak (tylko sugestie: usun `right` lub dodaj `width`).
- **Severity**: ERROR (domyslnie).
- **Bezpieczenstwo**: brak auto-fixu.
# # # OTUI-004 - Zas�b nie istnieje (STYLE ? `image`, `font`, `style`)
- **Opis**: odwolanie do pliku zasobu, kt�rego nie ma w projekcie.
- **Wykrywanie**: sprawdz sciezki wzgledem `project-root/data/.` lub mapy zasob�w (`assets-map.json`).
- **Auto-fix**: brak; podaj propozycje (fuzzy match) najblizszych nazw.
- **Severity**: ERROR.
# # # OTUI-005 - Zduplikowane `id` w obrebie pliku
- **Opis**: `KV.key == id` nie moze wystapic wielokrotnie z ta sama wartoscia w pliku.
- **Wykrywanie**: deduplikacja w `OTUIFile.body` (poziom pliku).
- **Auto-fix**: brak; zaproponuj nowe `id` (`<id>_1`).
- **Severity**: ERROR.
# # # OTUI-006 - Konwencja nazewnictwa `id`
- **Opis**: `id` dopuszcza `[a-z0-9_]+` (konfigurowalne).
- **Wykrywanie**: regex na `Identifier|StringLiteral`.
- **Auto-fix**: opcjonalna transformacja do lower_snake_case (jesli wlaczona).
- **Severity**: WARN.
# # # OTUI-007 - Nieznany atrybut widzetu
- **Opis**: klucz `KV.key` nie znajduje sie w dozwolonych dla danego widzetu (lista referencyjna + allow-list projektu).
- **Wykrywanie**: por�wnanie do bazy atrybut�w; jesli brak dopasowania ? problem.
- **Auto-fix**: brak; podpowiedz najblizszych kluczy (Levenshtein).
- **Severity**: WARN.
# # # OTUI-008 - Atrybut przestarzaly (deprecated)
- **Opis**: uzycie atrybutu oznaczonego jako przestarzaly w profilu projektu.
- **Wykrywanie**: dopasowanie do listy `deprecatedAttributes` (konfiguracja).
- **Auto-fix**: propozycja zamiennika (jesli podany w konfiguracji).
- **Severity**: WARN.
# # # OTUI-009 - Normalizacja boolean�w
- **Opis**: wartosci bool powinny byc `true|false` (nie `0|1|"true"`).
- **Wykrywanie**: `value` typu `Identifier/StringLiteral/NumberLiteral` odwzorowuje bool.
- **Auto-fix**: zamien na `true/false`.
- **Severity**: HINT.
# # # OTUI-010 - Format kolor�w
- **Opis**: akceptowane formaty kolor�w wg projektu (np. `#RRGGBB`, `rgba(...)`).
- **Wykrywanie**: regex na `StringLiteral`.
- **Auto-fix**: konwersja do kanonicznego formatu (jesli mozliwa).
- **Severity**: WARN.
# # # OTUI-011 - Jednostki wymiar�w/liczb
- **Opis**: liczby powinny byc bez jednostek (lub z konkretna notacja - zaleznie od projektu).
- **Wykrywanie**: `NumberLiteral` OK; `StringLiteral` z sufiksem jednostki ? problem (opcjonalnie).
- **Auto-fix**: usuniecie sufiksu, jesli wlaczone.
- **Severity**: HINT/WARN.
# # # OTUI-012 - Cykl dziedziczenia widzet�w
- **Opis**: `Decl.base` tworzy cykl (A < B, B < C, C < A).
- **Wykrywanie**: graf dziedziczenia per plik (lub caly projekt); detekcja cykli.
- **Auto-fix**: brak; raport sciezki cyklu.
- **Severity**: ERROR.
# # # OTUI-013 - Puste deklaracje
- **Opis**: `Decl` bez atrybut�w i potomk�w.
- **Wykrywanie**: `Decl.body.length == 0`.
- **Auto-fix**: usun pusty blok (opcjonalnie, jesli nie referencjonowany).
- **Severity**: INFO.
# # # OTUI-014 - Niezreferencjonowany widzet (analiza projektowa)
- **Opis**: `Decl` nigdy nie ladowany przez `g_ui.loadUI` ani dziedziczony.
- **Wykrywanie**: korelacja z `project-index.json.relations.lua_to_otui` i baza typ�w.
- **Auto-fix**: brak; informacja do porzadk�w.
- **Severity**: INFO.
# # # OTUI-015 - Odnosnik do stylu nie istnieje
- **Opis**: `style: "."` nie znajduje sie w katalogu styl�w projektu.
- **Wykrywanie**: por�wnanie do listy styl�w (assets-map lub dedykowana baza styl�w).
- **Auto-fix**: brak; fuzzy proposals.
- **Severity**: WARN.
# # # OTUI-016 - Event handler w kluczu `on...` ma niekanoniczna wartosc
- **Opis**: wartosci event�w powinny byc identyfikatorami (nie stringami) - zaleznie od konwencji projektu.
- **Wykrywanie**: `key` zaczyna sie od `on` + wielka litera; `value.type != Identifier`.
- **Auto-fix**: usun cudzyslowy (opcjonalnie).
- **Severity**: HINT/WARN.
# # # OTUI-017 - Atrybuty powielone w obrebie tego samego `Decl`
- **Opis**: ten sam `key` wystepuje wielokrotnie - ostatni wygrywa (nieczytelne).
- **Wykrywanie**: duplikaty `KV.key` w `Decl.body`.
- **Auto-fix**: scal albo usun duplikaty (zachowaj ostatni) - **opcjonalne**.
- **Severity**: WARN.
# # # OTUI-018 - Biale znaki i wciecia (2 spacje)
- **Opis**: standaryzacja wciec i trailing spaces.
- **Wykrywanie**: tokenizer whitespace; linie z tabami/konc�wkami spacji.
- **Auto-fix**: konwersja TAB?2 spacje, trim konc�wek.
- **Severity**: HINT.
# # # OTUI-019 - Komentarze (#) format
- **Opis**: komentarz powinien poprzedzac deklaracje lub stac po wartosci (a nie w srodku tokena).
- **Wykrywanie**: pozycje `Comment` vs `KV`/`Decl`.
- **Auto-fix**: przenies komentarz do poprawnej pozycji (jesli mozliwe).
- **Severity**: HINT.
# # # OTUI-020 - Klucze nieobslugiwane przez dany typ bazowy
- **Opis**: atrybut zarezerwowany dla innego typu (np. `icon` na widzecie, kt�ry go nie wspiera - wg bazy projektu).
- **Wykrywanie**: mapowanie `Type`?dozwolone atrybuty.
- **Auto-fix**: brak.
- **Severity**: WARN.

---
# # 2) Mapowanie kategorii atrybut�w (bazowa lista rozszerzalna)
- **GEOMETRY**: `x,y,width,height,anchors,margin,padding,min-width,max-width,min-height,max-height`
- **STYLE**: `font,color,image,style,opacity,icon,background,spacing,text`
- **BEHAVIOR**: `id,focusable,draggable,enabled,visible,onClick,onText,tooltip`
> Lista jest punktem startowym; moze zostac poszerzona w `otui-rules.json`.

---
# # 3) Integracja z edytorem (Monaco) - diagnostyka i Quick Fix
- **Publish diagnostyk**: na kazdy zapis i/lub po kr�tkim debounce (150 ms) po zmianie.
- **Format**: jak w �0; severity mapowane na kolor/ikone.
- **Quick Fix**: prezentuj `fix.title`; po akceptacji wykonaj `edits[]` (wspieraj multi-file).
- **Podglad diff**: dla auto-fix�w wymagajacych wiekszej zmiany (OTUI-001) pokaz unified diff.

---
# # 4) Konfiguracja regul (JSON)
```json
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
# # 5) Algorytmy auto-fix (pseudokod TS)
# # # 5.1 OTUI-001 (sort kategorii)
```ts
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
# # # 5.2 OTUI-002 (wrap `tr()`)
```ts
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
# # # 5.3 OTUI-009 (booleany)
```ts
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
# # 6) Test-wektory (minimalny zestaw regresji)
# # # 6.1 Kolejnosc p�l
**Wejscie**
```otui
W < UIWidget { text: "x" width: 1 id: a }
```
**Oczekiwane**: pojedyncza diagnostyka `OTUI-001` + auto-fix sortujacy.
# # # 6.2 `tr()` wrap
**Wejscie**
```otui
L < UIWidget { text: "Start" id: start }
```
**Oczekiwane**: `OTUI-002` z auto-fix ? `text: tr("Start")`.
# # # 6.3 Zas�b nie istnieje
**Wejscie**
```otui
B < UIWidget { image: "images/missing.png" }
```
**Oczekiwane**: `OTUI-004` (ERROR), propozycje fuzzy jesli `images/button.png` istnieje.
# # # 6.4 Duplikat `id`
**Wejscie**
```otui
A < UIWidget { id: x }
B < UIWidget { id: x }
```
**Oczekiwane**: `OTUI-005` na drugim wystapieniu.

---
# # 7) Kody bled�w parsera/enginu (dla OTUI)
- `OTUI_PARSE_001` - niezamkniety blok `{` (ParseError)
- `OTUI_PARSE_002` - nieznany token/literal ? potraktowano jako `Identifier`
- `OTUI_ENGINE_001` - nieprawidlowa kategoria atrybutu (brak w mapie)
- `OTUI_ENGINE_100` - blad I/O przy sprawdzaniu zasob�w

---
# # 8) Wydajnosc i limity
- Reguly jednoprzebiegowe; jedna analiza AST/plik.
- Sprawdzenie zasob�w buforowane (cache sciezek ? hash katalog�w assets).
- Caly lint dla pliku < 50 ms (target), batch 100 plik�w < 2 s.

---
# # 9) Checklisty wdrozeniowe (dla warstwy Lint)
- [ ] Implementacja wszystkich regul OTUI-001.020.
- [ ] Wlaczone auto-fix dla 001/002/009/018; pozostale bezpieczne - opcjonalnie.
- [ ] Konfiguracja regul w `otui-rules.json`; integracja w UI (enable/disable, severity).
- [ ] Testy z �6 - zielone; snapshoty zmian po auto-fix.
- [ ] Cache zasob�w i fuzzy propozycje dzialaja.

---
# # 10) Noty koncowe
- Reguly sa projektowalne - dopuszcza sie dodawanie wlasnych rozszerzen, o ile nie zmieniaja publicznych kontrakt�w (format diagnostyk i edycji).
- Wszelkie zmiany w zestawie regul wymagaja podniesienia `$schemaVersion` w konfiguracji i aktualizacji test-wektor�w.

# OTUI Lint Rules (MASTER) â€“ Specyfikacja dla **OTClient Studio**

> Cel: kompletny katalog reguÄąâ€š lint/autoĂ˘â‚¬â€fix dla **OTUI/OTML** uÄąÄ˝ywany przez Studio. Dokument definiuje: zachowania reguÄąâ€š, algorytmy autoĂ˘â‚¬â€fix, format diagnostyk, konfiguracjÄ™, testĂ˘â‚¬â€wektory, integracjÄ™ z edytorem i wymagania jakoÄąâ€şciowe. **Transfer 1:1** â€“ gotowe do bezpoÄąâ€şredniej implementacji.

---
## 0) ZaÄąâ€šoÄąÄ˝enia wspĂłlne
- **Parser/AST**: zgodnie z dokumentem â€žParser & Schemas: AST + JSON Schema (OTClient Studio)â€ť (Â§ OTUI AST). KaÄąÄ˝dy wÄ™zeÄąâ€š posiada `loc` (`file`, `start`, `end`).
- **Kategoryzacja atrybutĂłw**: `GEOMETRY`, `STYLE`, `BEHAVIOR` (lista bazowa w Â§1.3 tego dokumentu; rozszerzalna).
- **DeterministycznoÄąâ€şÄ‡**: wyniki lint i autoĂ˘â‚¬â€fix sÄ… deterministyczne (stabilny sort atrybutĂłw, niezmiennoÄąâ€şÄ‡ biaÄąâ€šych znakĂłw poza miejscem naprawy).
- **Backup i diff**: przy autoĂ˘â‚¬â€fix zapisywany jest plik `.bak` oraz generowany jest diff (Unified) do podglÄ…du w UI.
- **Format diagnostyk** (kanaÄąâ€š do edytora):
`$fenceInfo
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
## 1) Katalog reguÄąâ€š (z autoĂ˘â‚¬â€fix tam, gdzie bezpieczny)

> **Legenda pĂłl:** `Opis`, `Wykrywanie`, `AutoĂ˘â‚¬â€fix`, `PrzykÄąâ€šad (before/after)`, `Severity`, `BezpieczeÄąâ€žstwo`, `Konfiguracja`.
## OTUIĂ˘â‚¬â€001 â€” KolejnoÄąâ€şÄ‡ pĂłl: GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE (**autoĂ˘â‚¬â€fix**)
- **Opis**: w obrÄ™bie kaÄąÄ˝dego bloku deklaracji widÄąÄ˝etu atrybuty muszÄ… byÄ‡ uporzÄ…dkowane wg kategorii.
- **Wykrywanie**: przeanalizuj listÄ™ `KV` w `Decl.body`; jeÄąâ€şli sekwencja kategorii zawiera inwersje (np. `STYLE` przed `GEOMETRY`), zgÄąâ€šoÄąâ€ş problem.
- **AutoĂ˘â‚¬â€fix**: stabilne sortowanie kluczy: najpierw wszystkie `GEOMETRY`, potem `STYLE`, potem `BEHAVIOR`. Zachowaj wzglÄ™dnÄ… kolejnoÄąâ€şÄ‡ wewnÄ…trz kategorii i przenieÄąâ€ş komentarze razem z parÄ… `KV`.
- **PrzykÄąâ€šad**
`$fenceInfo
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
- **BezpieczeÄąâ€žstwo**: bezpieczny autoĂ˘â‚¬â€fix.
- **Konfiguracja**:
`$fenceInfo
{"OTUI-001":{"enabled":true,"severity":"WARN"}}
```
## OTUIĂ˘â‚¬â€002 â€” Statyczne teksty muszÄ… uÄąÄ˝ywaÄ‡ `tr()` (**autoĂ˘â‚¬â€fix**)
- **Opis**: literaÄąâ€šy string w atrybutach kategorii STYLE (np. `text`) muszÄ… byÄ‡ opakowane `tr("...")`.
- **Wykrywanie**: `KV.key` Ă˘ÂÂ STYLE Ă˘ÂÂ§ `value.type == StringLiteral` Ă˘ÂÂ§ `value.value` nie zaczyna siÄ™ od `tr(`.
- **AutoĂ˘â‚¬â€fix**: zamieÄąâ€ž `"Tekst"` Ă˘â€ â€™ `tr("Tekst")`. Wyklucz klucze `id`, nazwy klas/stylĂłw.
- **PrzykÄąâ€šad**
`$fenceInfo
# BEFORE
Label < UIWidget { text: "Start" }
# AFTER
Label < UIWidget { text: tr("Start") }
```
- **Severity**: WARN.
- **BezpieczeÄąâ€žstwo**: bezpieczny autoĂ˘â‚¬â€fix.
- **Konfiguracja**: `{ "OTUI-002": {"enabled": true, "severity": "WARN", "allowList": ["tooltip"] } }`
## OTUIĂ˘â‚¬â€003 â€” Sprzeczne `anchors` / `margins` (detekcja)
- **Opis**: wykrywa sprzecznoÄąâ€şci (np. jednoczesne kotwice wykluczajÄ…ce siÄ™ lub ujemne marginesy tam, gdzie to niedozwolone w projekcie).
- **Wykrywanie**: analizuj wartoÄąâ€şci `anchors` (obiekt/array) i `margin/Ă˘â‚¬Â¦`; reguÄąâ€šy domenowe: brak `left`+`right` bez `width` (jeÄąâ€şli projekt tak definiuje), brak ujemnych `margin`.
- **AutoĂ˘â‚¬â€fix**: brak (tylko sugestie: usuÄąâ€ž `right` lub dodaj `width`).
- **Severity**: ERROR (domyÄąâ€şlnie).
- **BezpieczeÄąâ€žstwo**: brak autoĂ˘â‚¬â€fixu.
## OTUIĂ˘â‚¬â€004 â€” ZasĂłb nie istnieje (STYLE Ă˘â€ â€™ `image`, `font`, `style`)
- **Opis**: odwoÄąâ€šanie do pliku zasobu, ktĂłrego nie ma w projekcie.
- **Wykrywanie**: sprawdÄąĹź Äąâ€şcieÄąÄ˝ki wzglÄ™dem `project-root/data/Ă˘â‚¬Â¦` lub mapy zasobĂłw (`assets-map.json`).
- **AutoĂ˘â‚¬â€fix**: brak; podaj propozycje (fuzzy match) najbliÄąÄ˝szych nazw.
- **Severity**: ERROR.
## OTUIĂ˘â‚¬â€005 â€” Zduplikowane `id` w obrÄ™bie pliku
- **Opis**: `KV.key == id` nie moÄąÄ˝e wystÄ…piÄ‡ wielokrotnie z tÄ… samÄ… wartoÄąâ€şciÄ… w pliku.
- **Wykrywanie**: deduplikacja w `OTUIFile.body` (poziom pliku).
- **AutoĂ˘â‚¬â€fix**: brak; zaproponuj nowe `id` (`<id>_1`).
- **Severity**: ERROR.
## OTUIĂ˘â‚¬â€006 â€” Konwencja nazewnictwa `id`
- **Opis**: `id` dopuszcza `[a-z0-9_]+` (konfigurowalne).
- **Wykrywanie**: regex na `Identifier|StringLiteral`.
- **AutoĂ˘â‚¬â€fix**: opcjonalna transformacja do lower_snake_case (jeÄąâ€şli wÄąâ€šÄ…czona).
- **Severity**: WARN.
## OTUIĂ˘â‚¬â€007 â€” Nieznany atrybut widÄąÄ˝etu
- **Opis**: klucz `KV.key` nie znajduje siÄ™ w dozwolonych dla danego widÄąÄ˝etu (lista referencyjna + allowĂ˘â‚¬â€list projektu).
- **Wykrywanie**: porĂłwnanie do bazy atrybutĂłw; jeÄąâ€şli brak dopasowania Ă˘â€ â€™ problem.
- **AutoĂ˘â‚¬â€fix**: brak; podpowiedÄąĹź najbliÄąÄ˝szych kluczy (Levenshtein).
- **Severity**: WARN.
## OTUIĂ˘â‚¬â€008 â€” Atrybut przestarzaÄąâ€šy (deprecated)
- **Opis**: uÄąÄ˝ycie atrybutu oznaczonego jako przestarzaÄąâ€šy w profilu projektu.
- **Wykrywanie**: dopasowanie do listy `deprecatedAttributes` (konfiguracja).
- **AutoĂ˘â‚¬â€fix**: propozycja zamiennika (jeÄąâ€şli podany w konfiguracji).
- **Severity**: WARN.
## OTUIĂ˘â‚¬â€009 â€” Normalizacja booleanĂłw
- **Opis**: wartoÄąâ€şci bool powinny byÄ‡ `true|false` (nie `0|1|"true"`).
- **Wykrywanie**: `value` typu `Identifier/StringLiteral/NumberLiteral` odwzorowuje bool.
- **AutoĂ˘â‚¬â€fix**: zamieÄąâ€ž na `true/false`.
- **Severity**: HINT.
## OTUIĂ˘â‚¬â€010 â€” Format kolorĂłw
- **Opis**: akceptowane formaty kolorĂłw wg projektu (np. `#RRGGBB`, `rgba(...)`).
- **Wykrywanie**: regex na `StringLiteral`.
- **AutoĂ˘â‚¬â€fix**: konwersja do kanonicznego formatu (jeÄąâ€şli moÄąÄ˝liwa).
- **Severity**: WARN.
## OTUIĂ˘â‚¬â€011 â€” Jednostki wymiarĂłw/liczb
- **Opis**: liczby powinny byÄ‡ bez jednostek (lub z konkretnÄ… notacjÄ… â€“ zaleÄąÄ˝nie od projektu).
- **Wykrywanie**: `NumberLiteral` OK; `StringLiteral` z sufiksem jednostki Ă˘â€ â€™ problem (opcjonalnie).
- **AutoĂ˘â‚¬â€fix**: usuniÄ™cie sufiksu, jeÄąâ€şli wÄąâ€šÄ…czone.
- **Severity**: HINT/WARN.
## OTUIĂ˘â‚¬â€012 â€” Cykl dziedziczenia widÄąÄ˝etĂłw
- **Opis**: `Decl.base` tworzy cykl (A < B, B < C, C < A).
- **Wykrywanie**: graf dziedziczenia per plik (lub caÄąâ€šy projekt); detekcja cykli.
- **AutoĂ˘â‚¬â€fix**: brak; raport Äąâ€şcieÄąÄ˝ki cyklu.
- **Severity**: ERROR.
## OTUIĂ˘â‚¬â€013 â€” Puste deklaracje
- **Opis**: `Decl` bez atrybutĂłw i potomkĂłw.
- **Wykrywanie**: `Decl.body.length == 0`.
- **AutoĂ˘â‚¬â€fix**: usuÄąâ€ž pusty blok (opcjonalnie, jeÄąâ€şli nie referencjonowany).
- **Severity**: INFO.
## OTUIĂ˘â‚¬â€014 â€” Niezreferencjonowany widÄąÄ˝et (analiza projektowa)
- **Opis**: `Decl` nigdy nie Äąâ€šadowany przez `g_ui.loadUI` ani dziedziczony.
- **Wykrywanie**: korelacja z `project-index.json.relations.lua_to_otui` i bazÄ… typĂłw.
- **AutoĂ˘â‚¬â€fix**: brak; informacja do porzÄ…dkĂłw.
- **Severity**: INFO.
## OTUIĂ˘â‚¬â€015 â€” OdnoÄąâ€şnik do stylu nie istnieje
- **Opis**: `style: "Ă˘â‚¬Â¦"` nie znajduje siÄ™ w katalogu stylĂłw projektu.
- **Wykrywanie**: porĂłwnanie do listy stylĂłw (assetsĂ˘â‚¬â€map lub dedykowana baza stylĂłw).
- **AutoĂ˘â‚¬â€fix**: brak; fuzzy proposals.
- **Severity**: WARN.
## OTUIĂ˘â‚¬â€016 â€” Event handler w kluczu `on...` ma niekanonicznÄ… wartoÄąâ€şÄ‡
- **Opis**: wartoÄąâ€şci eventĂłw powinny byÄ‡ identyfikatorami (nie stringami) â€” zaleÄąÄ˝nie od konwencji projektu.
- **Wykrywanie**: `key` zaczyna siÄ™ od `on` + wielka litera; `value.type != Identifier`.
- **AutoĂ˘â‚¬â€fix**: usuÄąâ€ž cudzysÄąâ€šowy (opcjonalnie).
- **Severity**: HINT/WARN.
## OTUIĂ˘â‚¬â€017 â€” Atrybuty powielone w obrÄ™bie tego samego `Decl`
- **Opis**: ten sam `key` wystÄ™puje wielokrotnie â€“ ostatni wygrywa (nieczytelne).
- **Wykrywanie**: duplikaty `KV.key` w `Decl.body`.
- **AutoĂ˘â‚¬â€fix**: scal albo usuÄąâ€ž duplikaty (zachowaj ostatni) â€” **opcjonalne**.
- **Severity**: WARN.
## OTUIĂ˘â‚¬â€018 â€” BiaÄąâ€še znaki i wciÄ™cia (2 spacje)
- **Opis**: standaryzacja wciÄ™Ä‡ i trailing spaces.
- **Wykrywanie**: tokenizer whitespace; linie z tabami/koÄąâ€žcĂłwkami spacji.
- **AutoĂ˘â‚¬â€fix**: konwersja TABĂ˘â€ â€™2 spacje, trim koÄąâ€žcĂłwek.
- **Severity**: HINT.
## OTUIĂ˘â‚¬â€019 â€” Komentarze (#) format
- **Opis**: komentarz powinien poprzedzaÄ‡ deklaracjÄ™ lub staÄ‡ po wartoÄąâ€şci (a nie w Äąâ€şrodku tokena).
- **Wykrywanie**: pozycje `Comment` vs `KV`/`Decl`.
- **AutoĂ˘â‚¬â€fix**: przenieÄąâ€ş komentarz do poprawnej pozycji (jeÄąâ€şli moÄąÄ˝liwe).
- **Severity**: HINT.
## OTUIĂ˘â‚¬â€020 â€” Klucze nieobsÄąâ€šugiwane przez dany typ bazowy
- **Opis**: atrybut zarezerwowany dla innego typu (np. `icon` na widÄąÄ˝ecie, ktĂłry go nie wspiera â€” wg bazy projektu).
- **Wykrywanie**: mapowanie `Type`Ă˘â€ â€™dozwolone atrybuty.
- **AutoĂ˘â‚¬â€fix**: brak.
- **Severity**: WARN.

---
## 2) Mapowanie kategorii atrybutĂłw (bazowa lista rozszerzalna)
- **GEOMETRY**: `x,y,width,height,anchors,margin,padding,min-width,max-width,min-height,max-height`
- **STYLE**: `font,color,image,style,opacity,icon,background,spacing,text`
- **BEHAVIOR**: `id,focusable,draggable,enabled,visible,onClick,onText,tooltip`
> Lista jest punktem startowym; moÄąÄ˝e zostaÄ‡ poszerzona w `otui-rules.json`.

---
## 3) Integracja z edytorem (Monaco) â€“ diagnostyka i Quick Fix
- **Publish diagnostyk**: na kaÄąÄ˝dy zapis i/lub po krĂłtkim debounce (150 ms) po zmianie.
- **Format**: jak w Â§0; severity mapowane na kolor/ikonÄ™.
- **Quick Fix**: prezentuj `fix.title`; po akceptacji wykonaj `edits[]` (wspieraj multiĂ˘â‚¬â€file).
- **PodglÄ…d diff**: dla autoĂ˘â‚¬â€fixĂłw wymagajÄ…cych wiÄ™kszej zmiany (OTUIĂ˘â‚¬â€001) pokaÄąÄ˝ unified diff.

---
## 4) Konfiguracja reguÄąâ€š (JSON)
`$fenceInfo
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
## 5) Algorytmy autoĂ˘â‚¬â€fix (pseudokod TS)
## 5.1 OTUIĂ˘â‚¬â€001 (sort kategorii)
`$fenceInfo
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
## 5.2 OTUIĂ˘â‚¬â€002 (wrap `tr()`)
`$fenceInfo
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
## 5.3 OTUIĂ˘â‚¬â€009 (booleany)
`$fenceInfo
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
## 6) TestĂ˘â‚¬â€wektory (minimalny zestaw regresji)
## 6.1 KolejnoÄąâ€şÄ‡ pĂłl
**WejÄąâ€şcie**
`$fenceInfo
W < UIWidget { text: "x" width: 1 id: a }
```
**Oczekiwane**: pojedyncza diagnostyka `OTUI-001` + autoĂ˘â‚¬â€fix sortujÄ…cy.
## 6.2 `tr()` wrap
**WejÄąâ€şcie**
`$fenceInfo
L < UIWidget { text: "Start" id: start }
```
**Oczekiwane**: `OTUI-002` z autoĂ˘â‚¬â€fix Ă˘â€ â€™ `text: tr("Start")`.
## 6.3 ZasĂłb nie istnieje
**WejÄąâ€şcie**
`$fenceInfo
B < UIWidget { image: "images/missing.png" }
```
**Oczekiwane**: `OTUI-004` (ERROR), propozycje fuzzy jeÄąâ€şli `images/button.png` istnieje.
## 6.4 Duplikat `id`
**WejÄąâ€şcie**
`$fenceInfo
A < UIWidget { id: x }
B < UIWidget { id: x }
```
**Oczekiwane**: `OTUI-005` na drugim wystÄ…pieniu.

---
## 7) Kody bÄąâ€šÄ™dĂłw parsera/enginu (dla OTUI)
- `OTUI_PARSE_001` â€“ niezamkniÄ™ty blok `{` (ParseError)
- `OTUI_PARSE_002` â€“ nieznany token/literaÄąâ€š Ă˘â€ â€™ potraktowano jako `Identifier`
- `OTUI_ENGINE_001` â€“ nieprawidÄąâ€šowa kategoria atrybutu (brak w mapie)
- `OTUI_ENGINE_100` â€“ bÄąâ€šÄ…d I/O przy sprawdzaniu zasobĂłw

---
## 8) WydajnoÄąâ€şÄ‡ i limity
- ReguÄąâ€šy jednoprzebiegowe; jedna analiza AST/plik.
- Sprawdzenie zasobĂłw buforowane (cache Äąâ€şcieÄąÄ˝ek Ă˘â€ â€™ hash katalogĂłw assets).
- CaÄąâ€šy lint dla pliku < 50 ms (target), batch 100 plikĂłw < 2 s.

---
## 9) Checklisty wdroÄąÄ˝eniowe (dla warstwy Lint)
- [ ] Implementacja wszystkich reguÄąâ€š OTUIĂ˘â‚¬â€001Ă˘â‚¬Â¦020.
- [ ] WÄąâ€šÄ…czone autoĂ˘â‚¬â€fix dla 001/002/009/018; pozostaÄąâ€še bezpieczne â€“ opcjonalnie.
- [ ] Konfiguracja reguÄąâ€š w `otui-rules.json`; integracja w UI (enable/disable, severity).
- [ ] Testy z Â§6 â€“ zielone; snapshoty zmian po autoĂ˘â‚¬â€fix.
- [ ] Cache zasobĂłw i fuzzy propozycje dziaÄąâ€šajÄ….

---
## 10) Noty koÄąâ€žcowe
- ReguÄąâ€šy sÄ… projektowalne â€“ dopuszcza siÄ™ dodawanie wÄąâ€šasnych rozszerzeÄąâ€ž, o ile nie zmieniajÄ… publicznych kontraktĂłw (format diagnostyk i edycji).
- Wszelkie zmiany w zestawie reguÄąâ€š wymagajÄ… podniesienia `$schemaVersion` w konfiguracji i aktualizacji testĂ˘â‚¬â€wektorĂłw.



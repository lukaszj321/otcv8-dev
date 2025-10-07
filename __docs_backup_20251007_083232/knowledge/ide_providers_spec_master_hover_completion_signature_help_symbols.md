# IDE Providers Spec (MASTER) - **Hover**, **Completion**, **Signature Help**, **Symbols**

> Cel: peL'na specyfikacja warstwy IDE dla **OTClient Studio** (Monaco + Electron). Dokument definiuje kontrakty, algorytmy, scoring, triggera'y, schematy JSON, IPC, testa'wektory i wymagania wydajnoLci. **Transfer 1:1** - gotowe do bezpoLredniej implementacji.

---
## 0) ZaL'oLLenia i kontekst
- **Jezyki:** `lua` (Luaa'Lite) i `otui` (OTUI/OTML).
- **LarodL'a wiedzy:** `resources/api.json` (kuratorowane), `project-index.json` (skan), `docstrings.json` (adnotacje), `otui-rules.json` (lint).
- **Silnik:** Monaco Editor (providers + Diagnostics).
- **Cele:** wysoka trafnoLc podpowiedzi, determinizm wynikow, niskie opoLsnienia (UX 60 FPS).

---
## 1) Rejestracja jezykow i providerow (Monaco)
## 1.1 Identyfikatory
- `languageId.luastudio = "lua"` (dialekt Luaa'Lite)
- `languageId.otuistudio = "otui"`
## 1.2 Rejestracja
- `monaco.languages.register({ id: languageId.luastudio })`
- `monaco.languages.register({ id: languageId.otuistudio })`
## 1.3 Providerzy (interfejsy Monaco)
- **Completion**: `registerCompletionItemProvider(id, provider)`
- **Hover**: `registerHoverProvider(id, provider)`
- **Signature Help**: `registerSignatureHelpProvider(id, provider)`
- **Document Symbols**: `registerDocumentSymbolProvider(id, provider)`
- **Definition/References**: (opcjonalnie MVP+) `registerDefinitionProvider`, `registerReferenceProvider`

> Dostawcy komunikuja sie z warstwa analiz przez **IPC** (sekcja 7) i uLLywaja lokalnych cacheay (sekcja 6).

---
## 2) Completion (autoa'uzupeL'nianie)
## 2.1 Triggery
- **Lua**: `.` `:` `(` `,` spacja po `function`/`local` oraz po `on` (eventy).
- **OTUI**: poczatek linii/po `\n`, po `:` (wartoLc), w nagL'owku deklaracji po `"<"` (typ bazowy), w kluczu (sugestie atrybutow wg kategorii), po `style:` (style zasobow).
## 2.2 LarodL'a sugestii
1) **API globalne** (`api.json`): `g_*` managery, funkcje, eventy.
2) **Symbole projektu** (`project-index.json`): funkcje zdefiniowane lokalnie, widLLety OTUI, pliki/LcieLLki.
3) **Docstrings** (`docstrings.json`): parametry i typy - doprecyzowanie sygnatur.
4) **Heurystyki vBot**: `macro(`, `onTextMessage`, `say(` itp. - boost rank.
## 2.3 Scoring i ranking
KaLLdy kandydat ma **score** a [0..1]. KoL"cowa kolejnoLc = malejaco po `score`, tiea'break: dL'ugoLc nazwy a', alfabetycznie.

**SkL'adniki score:**
- `s_prefix` - dopasowanie prefiksu (FZF/substring): 0.6-1.0
- `s_source` - priorytet LsrodL'a: API=1.0, projekt=0.9, docstring=0.85, heurystyka=0.8
- `s_context` - trafnoLc kontekstu (np. po `.` proponuj czL'onkow obiektu; po `:` metody; w OTUI klucze): 0.0-0.3
- `s_recent` - pamiec ostatnio uLLytych: +0.05 (TTL)

`score = 0.7*s_prefix + 0.2*s_source + 0.1*s_context + s_recent`
## 2.4 Typy pozycji (Monaco CompletionItemKind)
- `Function`, `Method`, `Property`, `Variable`, `Class` (OTUI typy), `Keyword`, `Snippet`, `File`, `Folder`.
## 2.5 Snippety i InsertText
- **Lua - funkcja lokalna:** `local ${1:name} = function(${2:args})\n  ${0}\nend`
- **Lua - moduL' skeleton:** `local M = {}\nfunction M.${1:fn}(${2})\n  ${0}\nend\nreturn M`
- **OTUI - widLLet:** `${1:Widget} < ${2:UIWidget} {\n  id: ${3:id}\n  width: ${4:100}\n  text: tr("${5:Text}")\n}`
## 2.6 Kontekstowe listy
- **Lua `.`/`:`** a' czL'onkowie obiektu (`api.json.objects[].members`) + symbole znalezione w projekcie.
- **OTUI klucz** a' lista atrybutow dozwolonych przez typ (kategoria + reguL'y `otui-rules.json`).
- **OTUI wartoLc `style:`** a' style z `assets-map.json.styles`.
## 2.7 PrzykL'ad odpowiedzi (IPC a' FE)
{
  "items": [
    {"label":"g_modules.reloadModules","kind":"Function","detail":"OTClient v8","insertText":"g_modules.reloadModules()","range": {"start":123,"end":123},"score":0.98},
    {"label":"g_resources.readFile","kind":"Method","detail":"string readFile(path)","insertText":"g_resources.readFile(${1:path})","insertTextRules":"snippet","score":0.93}
],
  "isIncomplete": false,
  "ttlMs": 3000
}
```

---
## 3) Hover (podglad dokumentacji)
## 3.1 Zasady agregacji
- Preferuj opis z **`api.json`**; jeLLeli brak a' **`docstrings.json`**; nastepnie heurystyki (np. typ identyfikatora z kontekstu).
- Dodaj **sygnature**, **opis**, **odsyL'acze** (plik:linia) i przykL'ad.
## 3.2 Format treLci (Markdown)
- NagL'owek: **Nazwa** i sygnatura, typ zwracany.
- Sekcje: `Opis`, `Parametry`, `Zwraca`, `PrzykL'ad`, `LarodL'o`.
## 3.3 PrzykL'ad odpowiedzi
{
  "contents": [
    {"value": "**g_modules.reloadModules()**a' *void*\n\nPrzeL'adowuje moduL'y i skrypty w OTClient.\n\n**LarodL'o:** api.json (v8)", "isTrusted": true}
],
  "range": {"start": 100, "end": 124},
  "ttlMs": 10000
}
```

---
## 4) Signature Help (podpowiedLs parametrow)
## 4.1 Triggery
- **Lua:** po wpisaniu `(` oraz po `,` w kontekLcie wywoL'ania.
- **OTUI:** (opcjonalnie) dla funkcji/event handlerow w wartoLciach `on...` (jeLLeli projekt dopuszcza).
## 4.2 Agregacja sygnatur
- **Priorytet:** `docstrings.json` (najbardziej szczegoL'owe typy) a' `api.json` a' heurystyka (typ `any`).
## 4.3 Model danych
{
  "signatures": [
{
      "label": "g_resources.readFile(path: string): string",
      "parameters": [
        {"label": "path: string", "documentation": "LscieLLka do pliku"}
]
}
],
  "activeSignature": 0,
  "activeParameter": 0,
  "ttlMs": 5000
}
```

---
## 5) Document Symbols / Definition / References (MVP+)
## 5.1 Document Symbols (w pliku)
- **Lua:** `FunctionDecl`, `LocalStatement (function)`, `TableConstructor (klucze funkcji)`.
- **OTUI:** `Decl` (nazwa widLLetu + `id`), klucze `KV` jako *children*.

**Output (przykL'ad):**
{"symbols":[{"name":"M.reload","kind":"Function","range":{...},"selectionRange":{...}}]}
```
## 5.2 Definition
- **Lua:** nazwa funkcji/identyfikatora a' lokalizacja deklaracji w bieLLacym pliku lub w `project-index.json.symbols`.
- **OTUI:** `WidgetName`/`id` a' definicja `Decl` w pliku.
## 5.3 References
- Przeszukanie `project-index.json` i lekkie skanowanie tokenow (prefiltrowanie po hashach plikow).

---
## 6) Cache, debounce i wydajnoLc
- **Cache L1 (process):** rezultaty zapytaL" na 3-10 s (`ttlMs` w odpowiedzi). Inwalidacja na zapis/zmiane pliku.
- **Cache L2 (disk):** indeksy `project-index.json` i `docstrings.json` w `.studio-cache/`.
- **Debounce:** 120-180 ms na zapytania providerow (per dokument).
- **BudLLet czasu:** cel < 6 ms na runde completions (po cache), < 25 ms cold.
- **Big file mode:** > 2 MB: ogranicz liczbe kandydatow (np. top 50).

---
## 7) IPC i kontrakty usL'ug (backend parsers/service)
## 7.1 KanaL'y
- `ide:completion` a' req: `CompletionQuery` a' res: `CompletionResult`
- `ide:hover` a' req: `HoverQuery` a' res: `HoverResult`
- `ide:signature` a' req: `SignatureQuery` a' res: `SignatureResult`
- `ide:symbols` a' req: `{uri}` a' res: `DocumentSymbols`
- (MVP+) `ide:definition`, `ide:references`
## 7.2 Modele zapytaL"/odpowiedzi
{
  "$schemaVersion": 1,
  "CompletionQuery": {"uri":"file:///...","language":"lua|otui","position":123,"prefix":"g_res","context":{"trigger":".","scope":"expr|key|value"}},
  "CompletionResult": {"items":[],"isIncomplete":false,"ttlMs":3000},

  "HoverQuery": {"uri":"file:///...","language":"lua|otui","range":{"start":100,"end":124}},
  "HoverResult": {"contents":[{"value":"...md...","isTrusted":true}],"range":{"start":100,"end":124},"ttlMs":10000},

  "SignatureQuery": {"uri":"file:///...","language":"lua|otui","callPos":130},
  "SignatureResult": {"signatures":[],"activeSignature":0,"activeParameter":0,"ttlMs":5000},

  "DocumentSymbols": {"symbols":[{"name":"...","kind":"Function","range":{}}]}
}
```
## 7.3 BL'edy
- Formaty: `{code,msg,details?}`; kody: `IDE_Q_BAD_REQ`, `IDE_S_TIMEOUT`, `IDE_D_SCHEMA`.

---
## 8) Algorytmy agregacji (pseudokod TS)
## 8.1 Completion (Lua)
function completeLua(q: CompletionQuery): CompletionResult {
  const ctx = analyzeContextLua(q);
  const api = apiCatalog.lookup(ctx.object, ctx.memberPrefix); // api.json
  const proj = projectIndex.members(ctx.object, ctx.memberPrefix); // project-index
  const docs = docstrings.find(ctx.memberPrefix); // docstrings
  const heur = heuristicsVBot(ctx);
  const cand = mergeDedup([api, proj, docs, heur]);
  const scored = cand.map(c => ({...c, score: score(c, q)}));
  return finalize(scored, q);
}
```
## 8.2 Completion (OTUI)
function completeOTUI(q: CompletionQuery): CompletionResult {
  if (q.context.scope === 'key') return keysForWidget(q); // kategorie + rules
  if (q.context.scope === 'value' && q.context.key === 'style') return stylesFromAssets();
  if (q.context.scope === 'typeBase') return widgetBaseTypes();
  return genericOtuiSnippets();
}
```
## 8.3 Hover
function hover(q: HoverQuery): HoverResult {
  const sym = resolveSymbolAt(q.uri, q.range);
  const a = api.jsonSym(sym);
  const d = docstrings.for(sym);
  const m = mergeDocs(a, d);
  return renderMarkdown(m);
}
```
## 8.4 Signature Help
function signature(q: SignatureQuery): SignatureResult {
  const call = findCallAt(q.callPos);
  const fromDocs = docstrings.signature(call.callee) || api.signature(call.callee) || anySignature(call.args);
  return toSignatureResult(fromDocs, call.argIndex);
}
```

---
## 9) Integracja z lintem i nawigacja
- **Diagnostics**: provider lintu OTUI/Lua publikuje problemy zgodnie z reguL'ami; IDE moLLe proponowac **Quick Fix** (np. OTUIa'001/002).
- **Goa'to Definition**: uLLyj `project-index.symbols` + lokalnego AST.
- **Peek References**: wyszukiwanie symboli w indeksie; prefiltrowanie po nazwach.

---
## 10) Konfiguracja (Ustawienia uLLytkownika)
{
  "$schemaVersion": 1,
  "completion": {"enable": true, "maxItems": 50, "fuzzy": true, "boostVBot": true},
  "hover": {"enable": true, "markdown": true},
  "signature": {"enable": true},
  "symbols": {"enable": true},
  "ranking": {"wPrefix": 0.7, "wSource": 0.2, "wContext": 0.1},
  "performance": {"debounceMs": 150, "bigFileLimit": 2000000}
}
```

---
## 11) Testa'wektory i QA
- **COMPa'01 (Lua):** `g_res` + `.` a' zawiera `g_resources.readFile` (score > 0.9).
- **COMPa'02 (OTUI):** w kluczu a' lista `GEOMETRY`/`STYLE`/`BEHAVIOR` wedL'ug reguL'; `style:` zwraca style z assets.
- **HOVa'01:** na `g_modules.reloadModules` a' opis z `api.json`.
- **SIGa'01:** `g_resources.readFile(` a' `path: string` w `activeParameter=0`.
- **SYMa'01:** `Document Symbols` zwraca funkcje i widLLety z poprawnymi zakresami.
- **PERFa'01:** czas odpowiedzi completions (cache warm) < 6 ms, (cold) < 25 ms.

---
## 12) WydajnoLc i telemetria
- Zbieraj metryki: Lredni czas odpowiedzi providerow, hit ratio cache, liczba kandydatow po deduplikacji.
- OstrzeLLenia w logu aplikacji, gdy colda'path > 50 ms lub liczba kandydatow > 500.

---
## 13) Checklisty wdroLLeniowe
- [ ] Rejestracja providerow dla `lua` i `otui`.
- [ ] Implementacja kanaL'ow IPC (7) + schematow zapytaL"/odpowiedzi.
- [ ] Agregacja `api.json` + `project-index.json` + `docstrings.json` (rankowanie 2.3).
- [ ] Snippety i triggera'y (2.1, 2.5).
- [ ] Hover/Signature z fallbackami (3, 4).
- [ ] Document Symbols (MVP), Definition/References (MVP+).
- [ ] Cache i debounce (6); budLLety czasu i biga'file mode.
- [ ] Testa'wektory (11) zielone; telemetria (12) aktywna.

---
## 14) Noty koL"cowe
- Wyniki providerow musza byc **stabilne** miedzy uruchomieniami (deterministyczne sortowanie); roLLnice jedynie przy zmianie kontekstu lub danych.
- Wszelkie rozszerzenia musza zachowac kontrakty IPC i schematy JSON (wersjonowanie `$schemaVersion`).

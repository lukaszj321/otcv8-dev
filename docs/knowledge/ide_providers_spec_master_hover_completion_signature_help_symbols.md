# IDE Providers Spec (MASTER) â€“ **Hover**, **Completion**, **Signature Help**, **Symbols**

> Cel: peÄąâ€šna specyfikacja warstwy IDE dla **OTClient Studio** (Monaco + Electron). Dokument definiuje kontrakty, algorytmy, scoring, triggerĂ˘â‚¬â€y, schematy JSON, IPC, testĂ˘â‚¬â€wektory i wymagania wydajnoÄąâ€şci. **Transfer 1:1** â€“ gotowe do bezpoÄąâ€şredniej implementacji.

---
## 0) ZaÄąâ€šoÄąÄ˝enia i kontekst
- **JÄ™zyki:** `lua` (LuaĂ˘â‚¬â€Lite) i `otui` (OTUI/OTML).
- **ÄąÄ…rĂłdÄąâ€ša wiedzy:** `resources/api.json` (kuratorowane), `project-index.json` (skan), `docstrings.json` (adnotacje), `otui-rules.json` (lint).
- **Silnik:** Monaco Editor (providers + Diagnostics).
- **Cele:** wysoka trafnoÄąâ€şÄ‡ podpowiedzi, determinizm wynikĂłw, niskie opĂłÄąĹźnienia (UX 60 FPS).

---
## 1) Rejestracja jÄ™zykĂłw i providerĂłw (Monaco)
## 1.1 Identyfikatory
- `languageId.luastudio = "lua"` (dialekt LuaĂ˘â‚¬â€Lite)
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

> Dostawcy komunikujÄ… siÄ™ z warstwÄ… analiz przez **IPC** (sekcja Â§7) i uÄąÄ˝ywajÄ… lokalnych cacheĂ˘â‚¬â„˘y (sekcja Â§6).

---
## 2) Completion (autoĂ˘â‚¬â€uzupeÄąâ€šnianie)
## 2.1 Triggery
- **Lua**: `.` `:` `(` `,` spacja po `function`/`local` oraz po `on` (eventy).
- **OTUI**: poczÄ…tek linii/po `\n`, po `:` (wartoÄąâ€şÄ‡), w nagÄąâ€šĂłwku deklaracji po `"<"` (typ bazowy), w kluczu (sugestie atrybutĂłw wg kategorii), po `style:` (style zasobĂłw).
## 2.2 ÄąÄ…rĂłdÄąâ€ša sugestii
1) **API globalne** (`api.json`): `g_*` managery, funkcje, eventy.
2) **Symbole projektu** (`project-index.json`): funkcje zdefiniowane lokalnie, widÄąÄ˝ety OTUI, pliki/Äąâ€şcieÄąÄ˝ki.
3) **Docstrings** (`docstrings.json`): parametry i typy â€“ doprecyzowanie sygnatur.
4) **Heurystyki vBot**: `macro(`, `onTextMessage`, `say(` itp. â€“ boost rank.
## 2.3 Scoring i ranking
KaÄąÄ˝dy kandydat ma **score** Ă˘ÂÂ [0..1]. KoÄąâ€žcowa kolejnoÄąâ€şÄ‡ = malejÄ…co po `score`, tieĂ˘â‚¬â€break: dÄąâ€šugoÄąâ€şÄ‡ nazwy Ă˘â€ â€, alfabetycznie.

**SkÄąâ€šadniki score:**
- `s_prefix` â€“ dopasowanie prefiksu (FZF/substring): 0.6â€“1.0
- `s_source` â€“ priorytet ÄąĹźrĂłdÄąâ€ša: API=1.0, projekt=0.9, docstring=0.85, heurystyka=0.8
- `s_context` â€“ trafnoÄąâ€şÄ‡ kontekstu (np. po `.` proponuj czÄąâ€šonkĂłw obiektu; po `:` metody; w OTUI klucze): 0.0â€“0.3
- `s_recent` â€“ pamiÄ™Ä‡ ostatnio uÄąÄ˝ytych: +0.05 (TTL)

`score = 0.7*s_prefix + 0.2*s_source + 0.1*s_context + s_recent`
## 2.4 Typy pozycji (Monaco CompletionItemKind)
- `Function`, `Method`, `Property`, `Variable`, `Class` (OTUI typy), `Keyword`, `Snippet`, `File`, `Folder`.
## 2.5 Snippety i InsertText
- **Lua â€“ funkcja lokalna:** `local ${1:name} = function(${2:args})\n  ${0}\nend`
- **Lua â€“ moduÄąâ€š skeleton:** `local M = {}\nfunction M.${1:fn}(${2})\n  ${0}\nend\nreturn M`
- **OTUI â€“ widÄąÄ˝et:** `${1:Widget} < ${2:UIWidget} {\n  id: ${3:id}\n  width: ${4:100}\n  text: tr("${5:Text}")\n}`
## 2.6 Kontekstowe listy
- **Lua `.`/`:`** Ă˘â€ â€™ czÄąâ€šonkowie obiektu (`api.json.objects[].members`) + symbole znalezione w projekcie.
- **OTUI klucz** Ă˘â€ â€™ lista atrybutĂłw dozwolonych przez typ (kategoria + reguÄąâ€šy `otui-rules.json`).
- **OTUI wartoÄąâ€şÄ‡ `style:`** Ă˘â€ â€™ style z `assets-map.json.styles`.
## 2.7 PrzykÄąâ€šad odpowiedzi (IPC Ă˘â€ â€™ FE)
`$fenceInfo
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
## 3) Hover (podglÄ…d dokumentacji)
## 3.1 Zasady agregacji
- Preferuj opis z **`api.json`**; jeÄąÄ˝eli brak Ă˘â€ â€™ **`docstrings.json`**; nastÄ™pnie heurystyki (np. typ identyfikatora z kontekstu).
- Dodaj **sygnaturÄ™**, **opis**, **odsyÄąâ€šacze** (plik:linia) i przykÄąâ€šad.
## 3.2 Format treÄąâ€şci (Markdown)
- NagÄąâ€šĂłwek: **Nazwa** i sygnatura, typ zwracany.
- Sekcje: `Opis`, `Parametry`, `Zwraca`, `PrzykÄąâ€šad`, `ÄąÄ…rĂłdÄąâ€šo`.
## 3.3 PrzykÄąâ€šad odpowiedzi
`$fenceInfo
{
  "contents": [
    {"value": "**g_modules.reloadModules()**Ă˘â€ â€™ *void*\n\nPrzeÄąâ€šadowuje moduÄąâ€šy i skrypty w OTClient.\n\n**ÄąÄ…rĂłdÄąâ€šo:** api.json (v8)", "isTrusted": true}
],
  "range": {"start": 100, "end": 124},
  "ttlMs": 10000
}
```

---
## 4) Signature Help (podpowiedÄąĹź parametrĂłw)
## 4.1 Triggery
- **Lua:** po wpisaniu `(` oraz po `,` w kontekÄąâ€şcie wywoÄąâ€šania.
- **OTUI:** (opcjonalnie) dla funkcji/event handlerĂłw w wartoÄąâ€şciach `on...` (jeÄąÄ˝eli projekt dopuszcza).
## 4.2 Agregacja sygnatur
- **Priorytet:** `docstrings.json` (najbardziej szczegĂłÄąâ€šowe typy) Ă˘â€ â€™ `api.json` Ă˘â€ â€™ heurystyka (typ `any`).
## 4.3 Model danych
`$fenceInfo
{
  "signatures": [
{
      "label": "g_resources.readFile(path: string): string",
      "parameters": [
        {"label": "path: string", "documentation": "ÄąĹˇcieÄąÄ˝ka do pliku"}
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
- **OTUI:** `Decl` (nazwa widÄąÄ˝etu + `id`), klucze `KV` jako *children*.

**Output (przykÄąâ€šad):**
`$fenceInfo
{"symbols":[{"name":"M.reload","kind":"Function","range":{...},"selectionRange":{...}}]}
```
## 5.2 Definition
- **Lua:** nazwa funkcji/identyfikatora Ă˘â€ â€™ lokalizacja deklaracji w bieÄąÄ˝Ä…cym pliku lub w `project-index.json.symbols`.
- **OTUI:** `WidgetName`/`id` Ă˘â€ â€™ definicja `Decl` w pliku.
## 5.3 References
- Przeszukanie `project-index.json` i lekkie skanowanie tokenĂłw (prefiltrowanie po hashach plikĂłw).

---
## 6) Cache, debounce i wydajnoÄąâ€şÄ‡
- **Cache L1 (process):** rezultaty zapytaÄąâ€ž na 3â€“10 s (`ttlMs` w odpowiedzi). Inwalidacja na zapis/zmianÄ™ pliku.
- **Cache L2 (disk):** indeksy `project-index.json` i `docstrings.json` w `.studio-cache/`.
- **Debounce:** 120â€“180 ms na zapytania providerĂłw (per dokument).
- **BudÄąÄ˝et czasu:** cel < 6 ms na rundÄ™ completions (po cache), < 25 ms cold.
- **Big file mode:** > 2 MB: ogranicz liczbÄ™ kandydatĂłw (np. top 50).

---
## 7) IPC i kontrakty usÄąâ€šug (backend parsers/service)
## 7.1 KanaÄąâ€šy
- `ide:completion` Ă˘â€ â€™ req: `CompletionQuery` Ă˘â€ â€™ res: `CompletionResult`
- `ide:hover` Ă˘â€ â€™ req: `HoverQuery` Ă˘â€ â€™ res: `HoverResult`
- `ide:signature` Ă˘â€ â€™ req: `SignatureQuery` Ă˘â€ â€™ res: `SignatureResult`
- `ide:symbols` Ă˘â€ â€™ req: `{uri}` Ă˘â€ â€™ res: `DocumentSymbols`
- (MVP+) `ide:definition`, `ide:references`
## 7.2 Modele zapytaÄąâ€ž/odpowiedzi
`$fenceInfo
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
## 7.3 BÄąâ€šÄ™dy
- Formaty: `{code,msg,details?}`; kody: `IDE_Q_BAD_REQ`, `IDE_S_TIMEOUT`, `IDE_D_SCHEMA`.

---
## 8) Algorytmy agregacji (pseudokod TS)
## 8.1 Completion (Lua)
`$fenceInfo
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
`$fenceInfo
function completeOTUI(q: CompletionQuery): CompletionResult {
  if (q.context.scope === 'key') return keysForWidget(q); // kategorie + rules
  if (q.context.scope === 'value' && q.context.key === 'style') return stylesFromAssets();
  if (q.context.scope === 'typeBase') return widgetBaseTypes();
  return genericOtuiSnippets();
}
```
## 8.3 Hover
`$fenceInfo
function hover(q: HoverQuery): HoverResult {
  const sym = resolveSymbolAt(q.uri, q.range);
  const a = api.jsonSym(sym);
  const d = docstrings.for(sym);
  const m = mergeDocs(a, d);
  return renderMarkdown(m);
}
```
## 8.4 Signature Help
`$fenceInfo
function signature(q: SignatureQuery): SignatureResult {
  const call = findCallAt(q.callPos);
  const fromDocs = docstrings.signature(call.callee) || api.signature(call.callee) || anySignature(call.args);
  return toSignatureResult(fromDocs, call.argIndex);
}
```

---
## 9) Integracja z lintem i nawigacjÄ…
- **Diagnostics**: provider lintu OTUI/Lua publikuje problemy zgodnie z reguÄąâ€šami; IDE moÄąÄ˝e proponowaÄ‡ **Quick Fix** (np. OTUIĂ˘â‚¬â€001/002).
- **GoĂ˘â‚¬â€to Definition**: uÄąÄ˝yj `project-index.symbols` + lokalnego AST.
- **Peek References**: wyszukiwanie symboli w indeksie; prefiltrowanie po nazwach.

---
## 10) Konfiguracja (Ustawienia uÄąÄ˝ytkownika)
`$fenceInfo
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
## 11) TestĂ˘â‚¬â€wektory i QA
- **COMPĂ˘â‚¬â€01 (Lua):** `g_res` + `.` Ă˘â€ â€™ zawiera `g_resources.readFile` (score > 0.9).
- **COMPĂ˘â‚¬â€02 (OTUI):** w kluczu Ă˘â€ â€™ lista `GEOMETRY`/`STYLE`/`BEHAVIOR` wedÄąâ€šug reguÄąâ€š; `style:` zwraca style z assets.
- **HOVĂ˘â‚¬â€01:** na `g_modules.reloadModules` Ă˘â€ â€™ opis z `api.json`.
- **SIGĂ˘â‚¬â€01:** `g_resources.readFile(` Ă˘â€ â€™ `path: string` w `activeParameter=0`.
- **SYMĂ˘â‚¬â€01:** `Document Symbols` zwraca funkcje i widÄąÄ˝ety z poprawnymi zakresami.
- **PERFĂ˘â‚¬â€01:** czas odpowiedzi completions (cache warm) < 6 ms, (cold) < 25 ms.

---
## 12) WydajnoÄąâ€şÄ‡ i telemetria
- Zbieraj metryki: Äąâ€şredni czas odpowiedzi providerĂłw, hit ratio cache, liczba kandydatĂłw po deduplikacji.
- OstrzeÄąÄ˝enia w logu aplikacji, gdy coldĂ˘â‚¬â€path > 50 ms lub liczba kandydatĂłw > 500.

---
## 13) Checklisty wdroÄąÄ˝eniowe
- [ ] Rejestracja providerĂłw dla `lua` i `otui`.
- [ ] Implementacja kanaÄąâ€šĂłw IPC (Â§7) + schematĂłw zapytaÄąâ€ž/odpowiedzi.
- [ ] Agregacja `api.json` + `project-index.json` + `docstrings.json` (rankowanie Â§2.3).
- [ ] Snippety i triggerĂ˘â‚¬â€y (Â§2.1, Â§2.5).
- [ ] Hover/Signature z fallbackami (Â§3, Â§4).
- [ ] Document Symbols (MVP), Definition/References (MVP+).
- [ ] Cache i debounce (Â§6); budÄąÄ˝ety czasu i bigĂ˘â‚¬â€file mode.
- [ ] TestĂ˘â‚¬â€wektory (Â§11) zielone; telemetria (Â§12) aktywna.

---
## 14) Noty koÄąâ€žcowe
- Wyniki providerĂłw muszÄ… byÄ‡ **stabilne** miÄ™dzy uruchomieniami (deterministyczne sortowanie); rĂłÄąÄ˝nice jedynie przy zmianie kontekstu lub danych.
- Wszelkie rozszerzenia muszÄ… zachowaÄ‡ kontrakty IPC i schematy JSON (wersjonowanie `$schemaVersion`).



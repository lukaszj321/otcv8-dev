---
id: "chapter:otmod"
chapter: "12_otmod"
slug: "12_otmod"
title: "OTMOD — moduły, hooki i lifecycle (export kit)"
status: "agent_ready"
owners:
  - "docs-export"
  - "github:lukaszj321"
tags: ["otmod","modules","lua","ui","lifecycle","authoring","rag"]
version: "1.0"
updated: "2025-10-15"
language: "pl"
encoding: "UTF-8 (no BOM)"

related:
  - "../04_ui/README.md"
  - "../11_data/README.md"
  - "../13_layouts/README.md"

artifacts:
  datasets:
    - id: "modules_index"
      file: "./datasets/modules_index.csv"
      headers: ["module","description","author","sandboxed","scripts","load_later","dependencies","website","path"]
      facet: "12_otmod.modules_index"
    - id: "module_scripts"
      file: "./datasets/module_scripts.csv"
      headers: ["module","script","order","source_file","lines","exports","requires"]
      facet: "12_otmod.module_scripts"
    - id: "module_deps"
      file: "./datasets/module_deps.csv"
      headers: ["module","depends_on","type","note"]
      facet: "12_otmod.module_deps"
    - id: "module_hooks"
      file: "./datasets/module_hooks.csv"
      headers: ["module","hook","function","priority","source_file","line"]
      facet: "12_otmod.module_hooks"
    - id: "module_ui_links"
      file: "./datasets/module_ui_links.csv"
      headers: ["module","otui_file","widget_root","widgets_count","images_count","fonts_used","styles_used"]
      facet: "12_otmod.module_ui_links"
  ndjson:
    - id: "modules_index_nd"
      file: "./datasets/ndjson/modules_index.jsonl"
    - id: "module_scripts_nd"
      file: "./datasets/ndjson/module_scripts.jsonl"
    - id: "module_deps_nd"
      file: "./datasets/ndjson/module_deps.jsonl"
    - id: "module_hooks_nd"
      file: "./datasets/ndjson/module_hooks.jsonl"
    - id: "module_ui_links_nd"
      file: "./datasets/ndjson/module_ui_links.jsonl"
  diagrams:
    - id: "lifecycle"
      file: "./diagrams/lifecycle.mmd"
      facet: "12_otmod.lifecycle"
    - id: "deps"
      file: "./diagrams/deps.mmd"
      facet: "12_otmod.deps"

outputs:
  - "./datasets/modules_index.csv"
  - "./datasets/module_scripts.csv"
  - "./datasets/module_deps.csv"
  - "./datasets/module_hooks.csv"
  - "./datasets/module_ui_links.csv"
  - "./datasets/ndjson/modules_index.jsonl"
  - "./datasets/ndjson/module_scripts.jsonl"
  - "./datasets/ndjson/module_deps.jsonl"
  - "./datasets/ndjson/module_hooks.jsonl"
  - "./datasets/ndjson/module_ui_links.jsonl"
  - "./stats/stats.json"
  - "./stats/stats.md"
---

# OTMOD — Moduły, hooki, zależności, UI i lifecycle (specyfikacja + praktyka)

**Cel:** Standaryzowany **export kit** do inwentaryzacji modułów `.otmod`, ich skryptów Lua, hooków cyklu życia, zależności (`hard/soft`) i powiązań z OTUI. Publikuje kontraktowe **CSV**, opcjonalny **NDJSON**, **statystyki**, **diagramy** i **sanity/QA**. Styl i IPC spójne z `11_data`, `13_layouts`, `14_android`, `15_vc16`.

---

## 0) Executive summary

- **Co:** indeks manifestów `.otmod`, skryptów (kolejność, linie, exports/requires), deps (`hard/soft`), hooki, linki do `.otui`.  
- **Dla kogo:** dev/QA/BI/RAG/Studio.  
- **Output:** CSV + NDJSON + `stats.{json,md}` + Mermaid.  
- **Agent-ready:** stałe nagłówki, IPC, sanity/QA, idempotentne extractory.

---

## 1) Struktura folderu (jak 11_data)

```bash
docs/12_otmod/
  README.md
  meta.json
  schemas/
    modules_index.schema.json
    module_scripts.schema.json
    module_deps.schema.json
    module_hooks.schema.json
    module_ui_links.schema.json
  sections/
    00_otmod_basics.md
    01_manifest_and_rules.md
    02_models.md
    03_collection_methods.md
    04_quality_and_limits.md
    05_how_to_read_stats.md
  datasets/
    modules_index.csv
    module_scripts.csv
    module_deps.csv
    module_hooks.csv
    module_ui_links.csv
    ndjson/*.jsonl
  stats/
    stats.json
    stats.md
  analysis/
    findings.md
    compliance.md
    figures/
  extractors/
    otmod_indexer.lua
    otmod_stats.lua
  diagrams/
    lifecycle.mmd
    deps.mmd
````

> **IO setup:** `dofile('../../_shared/lua/docio.lua')` w extractorach. Outputy zgodnie z `artifacts/outputs`.

---

## 2) README — skrót operacyjny (Agent-friendly)

**CSV headers (stałe):**

```
modules_index.csv
module,description,author,sandboxed,scripts,load_later,dependencies,website,path

module_scripts.csv
module,script,order,source_file,lines,exports,requires

module_deps.csv
module,depends_on,type,note

module_hooks.csv
module,hook,function,priority,source_file,line

module_ui_links.csv
module,otui_file,widget_root,widgets_count,images_count,fonts_used,styles_used
```

**IPC (Electron Studio):**

* `studio:otmod.index` → `extractors/otmod_indexer.lua`
* `studio:aggregate.otmod` → `extractors/otmod_stats.lua`
* `studio:open.otmod` `{file:'modules_index'|'module_scripts'|'module_deps'|'module_hooks'|'module_ui_links'}`
* Sandbox: `contextIsolation:true`, `nodeIntegration:false` (jak w 11/13).

**Crosslinks:** UI (`../04_ui`), Data (`../11_data`), Layouts (`../13_layouts`).

---

## 3) Modele danych (słowniki + przykłady)

### modules_index.csv

| Pole         | Typ     | Opis                                                   |
| ------------ | ------- | ------------------------------------------------------ |
| module       | string  | Unikalna nazwa (kebab_case).                           |
| description  | string  | Opis z manifestu.                                      |
| author       | string  | Autor/autorzy.                                         |
| sandboxed    | boolean | `true/false`.                                          |
| scripts      | string  | Lista `;` w kolejności (bootstrap→widgets→integracje). |
| load_later   | string  | Miękkie zależności (`;`).                              |
| dependencies | string  | Twarde zależności (`;`).                               |
| website      | string  | URL.                                                   |
| path         | string  | Ścieżka do `.otmod`.                                   |

**Przykład (record):**

```
game_interface,Create the game interface,OTClient team,true,widgets/uigamemap;gameinterface,game_skills;game_inventory,,https://github.com/edubart/otclient,modules/game_interface/game_interface.otmod
```

### module_scripts.csv

Zliczamy linie, heurystycznie wykrywamy `exports` (`modules.<name>.*`) i `requires` (`require('...')`).

### module_deps.csv

`type = hard|soft` (odpowiednio `dependencies` / `load-later`).

### module_hooks.csv

Hooki z manifestu (`@onLoad/@onUnload`), opcjonalnie z Lua (jeśli wykryte).

### module_ui_links.csv

Powiązania `.otui` wykryte w katalogu modułu (policz widgety/obrazy/fonty/style).

---

## 4) Przykłady manifestów i powiązań (AGENT examples)

```otmod
Module
  name: game_interface
  description: Create the game interface, where the ingame stuff starts
  author: OTClient team
  website: https://github.com/edubart/otclient
  sandboxed: true
  scripts: [ widgets/uigamemap, gameinterface ]
  load-later: [ game_skills, game_inventory, game_console ]
  @onLoad: init()
  @onUnload: terminate()
```

```otmod
Module
  name: game_skills
  description: Manage skills window
  author: baxnie, edubart
  sandboxed: true
  scripts: [ skills ]
  dependencies: [ game_interface ]
  @onLoad: init()
  @onUnload: terminate()
```

**Fragment OTUI (link):**

```otui
MiniWindow
  id: skillWindow
  !text: tr('Skills')
  icon: /images/topbuttons/skills
  @onClose: modules.game_skills.onMiniWindowClose()
```

---

## 5) Extractors (Lua) — gotowe pliki

**extractors/otmod_indexer.lua**

```lua
-- docs/12_otmod/extractors/otmod_indexer.lua
-- Indeksuje *.otmod + Lua + OTUI → CSV oraz opcjonalnie NDJSON
-- ASCII-only; UTF-8 without BOM; LF
local docio = dofile('../../_shared/lua/docio.lua')
local json = require('json')

local HDR_MI = {'module','description','author','sandboxed','scripts','load_later','dependencies','website','path'}
local HDR_MS = {'module','script','order','source_file','lines','exports','requires'}
local HDR_MD = {'module','depends_on','type','note'}
local HDR_MH = {'module','hook','function','priority','source_file','line'}
local HDR_MU = {'module','otui_file','widget_root','widgets_count','images_count','fonts_used','styles_used'}
local MAX_BYTES = 50*1024*1024

local function wcsv(file, hdr, row) docio.writeCsvHeader(file, hdr); docio.appendCsvRow(file, hdr, row, MAX_BYTES) end
local function wjsonl(file, obj) docio.appendJsonl(file, obj, MAX_BYTES) end
local function trim(s) return (tostring(s or ''):gsub('^%s+',''):gsub('%s+$','')) end
local function split(s) local t={}; for x in tostring(s or ''):gmatch('[^,;%s]+') do t[#t+1]=x end; return t end

local function rd(path)
  if g_resources and g_resources.fileExists and g_resources:fileExists(path) then return g_resources:readFileContents(path) end
  return docio.readAll(path)
end

local function parse_otmod(t)
  local M = {}
  M.name = trim((t:match('%f[%w]name:%s*([%w_%-]+)') or ''))
  M.description = trim((t:match('%f[%w]description:%s*(.-)\n') or ''):gsub('\r',''))
  M.author = trim((t:match('%f[%w]author:%s*(.-)\n') or ''))
  M.website = trim((t:match('%f[%w]website:%s*(.-)\n') or ''))
  M.sandboxed = ((t:match('%f[%w]sandboxed:%s*(%a+)') or ''):lower()=='true')
  local scripts = t:match('scripts:%s*%[(.-)%]') or t:match('%f[%w]scripts:%s*(.-)\n') or ''
  local ll = t:match('load%-later:%s*%[(.-)%]') or t:match('%f[%w]load%-later:%s*(.-)\n') or ''
  local deps = t:match('dependencies:%s*%[(.-)%]') or t:match('%f[%w]dependencies:%s*(.-)\n') or ''
  M.scripts = table.concat(split(scripts), ';'); M.load_later = table.concat(split(ll), ';'); M.dependencies = table.concat(split(deps), ';')
  M.hooks = {}
  local onLoad = t:match('@onLoad:%s*([%w_%.]+)'); if onLoad then table.insert(M.hooks, {hook='@onLoad', fn=onLoad}) end
  local onUnload = t:match('@onUnload:%s*([%w_%.]+)'); if onUnload then table.insert(M.hooks, {hook='@onUnload', fn=onUnload}) end
  return M
end

local function analyze_lua(mod, path)
  local txt = rd(path) or ''
  local lines = select(2, txt:gsub('\n','\n'))
  local exps, reqs = {}, {}
  local ns = mod:gsub('%-','_')
  for s in txt:gmatch('modules%.'..ns..'%.[%w_]+') do exps[#exps+1]=s end
  for r in txt:gmatch("require%(['\"]([%w_%./%-]+)['\"]%)") do reqs[#reqs+1]=r end
  return lines, table.concat(exps,'|'), table.concat(reqs,'|')
end

local function analyze_otui(path)
  local txt = rd(path) or ''
  local w=0; for _ in txt:gmatch('\n[%w_]+%s*<%s*[%w_]') do w=w+1 end
  local i=0; for _ in txt:gmatch('image%-source%s*:') do i=i+1 end
  local f=0; for _ in txt:gmatch('\n%s*font%s*:') do f=f+1 end
  local st=0; for _ in txt:gmatch('image%-clip%s*:') do st=st+1 end
  return w,i,f,st
end

local function index_one(otmodPath)
  local t = rd(otmodPath) or ''
  local M = parse_otmod(t)
  if not M.name or M.name=='' then return end
  -- modules_index
  wcsv('docs/12_otmod/datasets/modules_index.csv', HDR_MI, {
    module=M.name, description=M.description, author=M.author, sandboxed=tostring(M.sandboxed),
    scripts=M.scripts, load_later=M.load_later, dependencies=M.dependencies, website=M.website, path=otmodPath
  })
  wjsonl('docs/12_otmod/datasets/ndjson/modules_index.jsonl', {
    module=M.name, description=M.description, author=M.author, sandboxed=M.sandboxed,
    scripts=split(M.scripts), load_later=split(M.load_later), dependencies=split(M.dependencies),
    website=M.website, path=otmodPath
  })
  -- hooks
  for _,h in ipairs(M.hooks) do
    wcsv('docs/12_otmod/datasets/module_hooks.csv', HDR_MH, {module=M.name, hook=h.hook, ['function']=h.fn, priority='', source_file=otmodPath, line='' })
    wjsonl('docs/12_otmod/datasets/ndjson/module_hooks.jsonl', {module=M.name, hook=h.hook, func=h.fn, source=otmodPath})
  end
  -- deps
  for _,d in ipairs(split(M.dependencies)) do if d~='' then wcsv('docs/12_otmod/datasets/module_deps.csv', HDR_MD, {module=M.name, depends_on=d, type='hard', note=''}) end end
  for _,d in ipairs(split(M.load_later)) do if d~='' then wcsv('docs/12_otmod/datasets/module_deps.csv', HDR_MD, {module=M.name, depends_on=d, type='soft', note=''}) end end
  -- scripts
  local idx=0
  for _,s in ipairs(split(M.scripts)) do
    if s~='' then
      idx = idx + 1
      local luaPath = ('modules/%s/%s.lua'):format(M.name, s)
      local lines, ex, rq = analyze_lua(M.name, luaPath)
      wcsv('docs/12_otmod/datasets/module_scripts.csv', HDR_MS, {module=M.name, script=s, order=idx, source_file=luaPath, lines=lines, exports=ex, requires=rq})
      wjsonl('docs/12_otmod/datasets/ndjson/module_scripts.jsonl', {module=M.name, script=s, order=idx, source_file=luaPath, lines=lines, exports=ex, requires=rq})
    end
  end
  -- otui
  for _,p in ipairs(docio.glob(('modules/%s/*.otui'):format(M.name)) or {}) do
    local w,i,f,st = analyze_otui(p)
    wcsv('docs/12_otmod/datasets/module_ui_links.csv', HDR_MU, {module=M.name, otui_file=p, widget_root=M.name, widgets_count=w, images_count=i, fonts_used=f, styles_used=st})
    wjsonl('docs/12_otmod/datasets/ndjson/module_ui_links.jsonl', {module=M.name, otui_file=p, widget_root=M.name, widgets_count=w, images_count=i, fonts_used=f, styles_used=st})
  end
end

local function run()
  for _,p in ipairs(docio.glob('modules/**/**.otmod') or {}) do index_one(p) end
end

run()
```

**extractors/otmod_stats.lua**

```lua
-- docs/12_otmod/extractors/otmod_stats.lua
-- Agregacja → stats.json + stats.md (deterministycznie)
-- ASCII-only; UTF-8 without BOM; LF
local docio = dofile('../../_shared/lua/docio.lua')
local json = require('json')

local function read_csv(path)
  local t = docio.readAll(path); if not t or #t==0 then return {},{} end
  local rows, header = {}, nil
  for line in t:gmatch('[^\r\n]+') do
    if not header then header=docio.parseCsvHeader(line)
    else rows[#rows+1]=docio.parseCsvRow(header,line) end
  end
  return rows, header
end

local function build_stats()
  local s = { modules=0, sandboxed={true=0,false=0}, deps={hard=0,soft=0}, hooks={}, scripts={count=0,lines=0} }
  local mi = read_csv('docs/12_otmod/datasets/modules_index.csv')
  for _,r in ipairs(mi) do
    s.modules = s.modules + 1
    local sb = tostring(r.sandboxed or ''):lower()=='true'
    s.sandboxed[sb] = (s.sandboxed[sb] or 0) + 1
  end
  local md = read_csv('docs/12_otmod/datasets/module_deps.csv')
  for _,r in ipairs(md) do s.deps[(r.type=='hard') and 'hard' or 'soft'] = s.deps[(r.type=='hard') and 'hard' or 'soft'] + 1 end
  local mh = read_csv('docs/12_otmod/datasets/module_hooks.csv')
  for _,r in ipairs(mh) do s.hooks[r.hook or ''] = (s.hooks[r.hook or ''] or 0) + 1 end
  local ms = read_csv('docs/12_otmod/datasets/module_scripts.csv')
  for _,r in ipairs(ms) do s.scripts.count = s.scripts.count + 1; s.scripts.lines = s.scripts.lines + (tonumber(r.lines or '0') or 0) end
  return s
end

local function write_md(s)
  local out = {}
  out[#out+1] = '# OTMOD — Statystyki\n\n'
  out[#out+1] = ('- Moduły: %d\n'):format(s.modules)
  out[#out+1] = ('- Sandboxed: true=%d, false=%d\n'):format(s.sandboxed.true or 0, s.sandboxed.false or 0)
  out[#out+1] = ('- Zależności: hard=%d, soft=%d\n'):format(s.deps.hard or 0, s.deps.soft or 0)
  out[#out+1] = ('- Skrypty: %d plików, %d linii\n\n'):format(s.scripts.count, s.scripts.lines)
  out[#out+1] = '## Hooki\n'
  for k,v in pairs(s.hooks) do out[#out+1] = ('- %s: %d\n'):format(k, v) end
  out[#out+1] = '\nWnioski: zweryfikuj moduły niesandboxowane i długie łańcuchy deps.\n'
  return table.concat(out)
end

local function run()
  local s = build_stats()
  docio.writeAll('docs/12_otmod/stats/stats.json', json.encode(s))
  docio.writeAll('docs/12_otmod/stats/stats.md', write_md(s))
end

run()
```

---

## 6) Schematy (JSON Schema) — walidacja

*(pliki pełne w `schemas/` — poniżej skrót pól wymaganych):*

* `modules_index.schema.json` — required: `["module","path"]`
* `module_scripts.schema.json` — required: `["module","script","order"]`
* `module_deps.schema.json` — required: `["module","depends_on","type"]` (`hard|soft`)
* `module_hooks.schema.json` — required: `["module","hook","function"]`
* `module_ui_links.schema.json` — required: `["module","otui_file","widget_root"]`

---

## 7) Sanity + IPC + QA

* **headers-invariant:** nagłówki CSV *dokładnie* jak w sekcji #2.
* **list-format:** listy w `;` (bez spacji), np. `a;b;c`.
* **hook-clean:** `@onLoad/@onUnload` → istnieją funkcje Lua `init/terminate` (jeśli brak — wpis w `analysis/findings.md`).
* **deps-acyclic:** raportuj cykle w `module_deps.csv` (skrypt QA poza zakresem indeksu).
* **ui-links:** `widgets_count/images_count/fonts_used/styles_used` są liczbami ≥ 0.
* **idempotency:** drugi bieg nie zmienia istniejących wierszy.
* **encoding:** UTF-8 (no BOM), **LF**.
* **IPC:** odbiór komunikatów tylko z zaufanego procesu (Electron preload); ścieżki zapisu whitelisted pod `docs/12_otmod`.

---

## 8) Diagramy (Mermaid)

**diagrams/lifecycle.mmd** *(facet: 12_otmod.lifecycle)*

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
  participant Loader
  participant Module as OTMOD
  participant Lua as Scripts
  participant UI as OTUI
  Loader->>Module: parse manifest
  Module->>Lua: scripts[] (ordered)
  Module->>Lua: @onLoad → init()
  Lua->>UI: load *.otui / bind signals
  Lua-->>Module: ready()
  Loader->>Module: unload
  Module->>Lua: @onUnload → terminate()
```

**diagrams/deps.mmd** *(facet: 12_otmod.deps)*

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
  A[game_interface] -->|soft| B[game_skills]
  A -->|soft| C[game_inventory]
  B -->|hard| D[game_stats]
```

---

## 9) Appendix — Regexy parsera (skrót)

```text
# lists: [a, b] lub "a, b" / "a; b"
(?m)^\s*(scripts|load-later|dependencies)\s*:\s*(?:\[(.*?)\]|(.*)$)

# hooki
(?m)@onLoad:\s*([\w_.]+)
(?m)@onUnload:\s*([\w_.]+)
```

---

## 10) DoD Checklist

* [ ] Wygenerowane CSV: `modules_index`, `module_scripts`, `module_deps`, `module_hooks`, `module_ui_links`.
* [ ] NDJSON (opcjonalne) wszystkich pięciu tabel.
* [ ] `stats.json` i `stats.md` (deterministyczne).
* [ ] Sekcje `00..05` istnieją; `02_models.md` ma przykłady (AGENT INSERT).
* [ ] Diagramy `lifecycle.mmd` i `deps.mmd` renderują się.
* [ ] Sanity (headers/list-format/hook-clean/deps-acyclic/idempotency) — PASS.
* [ ] `meta.json` zawiera linki do `../04_ui` i `../11_data`.

---

## 11) meta.json — wzorzec

```json
{
  "$schemaVersion": 1,
  "chapterId": "chapter:otmod",
  "title": "OTMOD — Modules, Hooks, Lifecycle",
  "owners": ["docs-export", "github:lukaszj321"],
  "tags": ["otmod","modules","lua","ui","lifecycle","authoring","rag"],
  "fileMap": {
    "readme": "./README.md",
    "schemas": {
      "modules_index": "./schemas/modules_index.schema.json",
      "module_scripts": "./schemas/module_scripts.schema.json",
      "module_deps": "./schemas/module_deps.schema.json",
      "module_hooks": "./schemas/module_hooks.schema.json",
      "module_ui_links": "./schemas/module_ui_links.schema.json"
    },
    "sections": [
      "./sections/00_otmod_basics.md",
      "./sections/01_manifest_and_rules.md",
      "./sections/02_models.md",
      "./sections/03_collection_methods.md",
      "./sections/04_quality_and_limits.md",
      "./sections/05_how_to_read_stats.md"
    ],
    "datasets": {
      "csv": {
        "modules_index": "./datasets/modules_index.csv",
        "module_scripts": "./datasets/module_scripts.csv",
        "module_deps": "./datasets/module_deps.csv",
        "module_hooks": "./datasets/module_hooks.csv",
        "module_ui_links": "./datasets/module_ui_links.csv"
      },
      "ndjson": {
        "modules_index": "./datasets/ndjson/modules_index.jsonl",
        "module_scripts": "./datasets/ndjson/module_scripts.jsonl",
        "module_deps": "./datasets/ndjson/module_deps.jsonl",
        "module_hooks": "./datasets/ndjson/module_hooks.jsonl",
        "module_ui_links": "./datasets/ndjson/module_ui_links.jsonl"
      }
    },
    "stats": {
      "json": "./stats/stats.json",
      "md": "./stats/stats.md"
    },
    "analysis": {
      "findings": "./analysis/findings.md",
      "compliance": "./analysis/compliance.md",
      "figuresDir": "./analysis/figures"
    },
    "extractors": [
      "./extractors/otmod_indexer.lua",
      "./extractors/otmod_stats.lua"
    ],
    "diagrams": [
      "./diagrams/lifecycle.mmd",
      "./diagrams/deps.mmd"
    ]
  },
  "linking": {
    "crossChapter": {
      "ui": "../04_ui/README.md",
      "data": "../11_data/README.md",
      "layouts": "../13_layouts/README.md"
    }
  },
  "agent": {
    "tasks": [
      {"id":"index","desc":"Indeksacja .otmod + Lua + OTUI do CSV/NDJSON","outputs":["datasets.csv","datasets.ndjson"]},
      {"id":"aggregate","desc":"Agregacja do stats.json/stats.md","outputs":["stats.json","stats.md"]},
      {"id":"author","desc":"Uzupełnienie sekcji + przykłady + compliance","targets":["sections/*","analysis/*"]}
    ],
    "insertPoints": {
      "sections/02_models.md": ["AGENT:INSERT:OTMOD-EXAMPLES"],
      "analysis/findings.md": ["AGENT:INSERT:FINDINGS"],
      "analysis/compliance.md": ["AGENT:INSERT:COMPLIANCE"]
    }
  }
}
```

---

## 12) Sekcje (szablony do wypełnienia)

**sections/00_otmod_basics.md**

```markdown
# OTMOD — podstawy
`.otmod` definiuje moduł (manifest, skrypty, hooki, deps). Dbaj o deterministyczne ładowanie i `sandboxed: true`.
```

**sections/01_manifest_and_rules.md**

```markdown
# Manifest i zasady ładowania
- `scripts` (kolejność → determinizm)
- `load-later` (miękkie deps)
- `dependencies` (twarde deps)
- Hooki: `@onLoad: init()`, `@onUnload: terminate()`
```

**sections/02_models.md**

```markdown
# Modele danych — przykłady
<!-- AGENT:INSERT:OTMOD-EXAMPLES -->
```

**sections/03_collection_methods.md**

```markdown
# Zbieranie
- `otmod_indexer.lua` → CSV/NDJSON
- Heurystyki `exports/requires`, skan `.otui`
- IPC: `studio:otmod.index`, `studio:aggregate.otmod`
```

**sections/04_quality_and_limits.md**

```markdown
# Jakość i ograniczenia
- Parser defensywny list/whitespace
- Eksporty heurystyczne — potwierdzaj ręcznie
- UI ładowane dynamicznie może nie trafić do `module_ui_links`
```

**sections/05_how_to_read_stats.md**

```markdown
# Jak czytać statystyki
- Sandboxed vs non-sandboxed → ryzyka
- Deps: centralność/hotspoty
- Hooki: kolejność inicjalizacji
```

---

## 13) Facets

* (facet-12_otmod.modules_index)=**Facet: `12_otmod.modules_index`** — dataset
* (facet-12_otmod.module_scripts)=**Facet: `12_otmod.module_scripts`** — dataset
* (facet-12_otmod.module_deps)=**Facet: `12_otmod.module_deps`** — dataset
* (facet-12_otmod.module_hooks)=**Facet: `12_otmod.module_hooks`** — dataset
* (facet-12_otmod.module_ui_links)=**Facet: `12_otmod.module_ui_links`** — dataset
* (facet-12_otmod.lifecycle)=**Facet: `12_otmod.lifecycle`** — diagram
* (facet-12_otmod.deps)=**Facet: `12_otmod.deps`** — diagram

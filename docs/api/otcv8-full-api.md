# OTCv8 – Pełne AP

I

Wersja specyfikacji: 1.0 Status: **draft** (uzupełnij pola `TODO:` realnymi nazwami/argumentami z
kodu).

---

## 0. Konwencj

e

- **Typy**: `string`, `number`, `boolean`, `table`, `nil`.
- **Czas**: UNIX ms (`number`).
- **Błędy**: kody `E_*` + opis; w WS pole `error`.
- **Nazewnictwo**:
  - Lua: `snake_case`
  - Eventy: `dot.case` (`metrics.update`, `cmd.result`)
  - OTUI: `id` unikalne, `class` do stylów.

---

## 1. Runtime Lua / Moduły vBo

t

### 1.1. Cykl życia moduł

u

```lua
-- modules/<name>/init.lua
local M = {}

-- Wywoływane przy starcie modułu
function M.start(ctx) end

-- Wywoływane przy zatrzymaniu modułu
function M.stop(ctx) end

-- (opcjonalnie) okresowe ticki
function M.tick(ctx, dt_ms) end

return M

```

**`ctx` (context)** – most do UI/WS/IO:

| Metoda                      | Opis                            | Przykład                                 |        |            |                           |
| --------------------------- | ------------------------------- | ---------------------------------------- | ------ | ---------- | ------------------------- |
| `ctx.emit(target, payload)` | Publikuj zdarzenie do UI/mostu. | `ctx.emit("status", {text="OK"})`        |        |            |                           |
| `ctx.on(event, fn)`         | Subskrypcja lokalnego eventu.   | `ctx.on("config.changed", fn)`           |        |            |                           |
| `ctx.log(msg, level?)`      | Log (`"debug"                   | "info"                                   | "warn" | "error"`). | `ctx.log("start","info")` |
| `ctx.set_timeout(ms, fn)`   | Jednorazowy timer; zwraca `id`. |                                          |        |            |                           |
| `ctx.clear_timeout(id)`     | Anuluj timer.                   |                                          |        |            |                           |
| `ctx.storage.get(key)`      | Odczyt z pamięci modułu.        |                                          |        |            |                           |
| `ctx.storage.set(key,val)`  | Zapis do pamięci modułu.        |                                          |        |            |                           |
| `ctx.ws.send(type, data)`   | Wyślij wiadomość WS (patrz §3). | `ctx.ws.send("telemetry.push",{hp=100})` |        |            |                           |

> TODO: dopisz rzeczywiste metody `ctx` z projektu (HTTP? FS? IPC?).

### 1.2. Zdarzenia globalne Lua (emiter silnika

)

Rejestrujesz globalnie (przed startem lub w `M.start`). **Silnik emituje** m.in.:

```lua
-- Chat/komunikacja
onTalk(function(name, level, mode, text) end)  -- TODO: potwierdź argumenty

-- Obiekty
onCreatureAppear(function(creature) end)
onCreatureDisappear(function(creature) end)
onCreatureHealthChange(function(creature, hp, hpmax) end)

-- Wejście/użytkownik
onKeyDown(function(key) end)
onKeyUp(function(key) end)
onMouseEvent(function(x, y, btn, state) end)

-- Czas
every(ms, function() end)        -- helper okresowy
schedule(ms, function() end)     -- jednorazowy
cancel(timer_id)

```

> TODO: uzupełnij pełną listę eventów i ich parametry.

### 1.3. Błędy (Lua

)

- `E_ARG` – zły typ/zakres argumentu
- `E_STATE` – nieprawidłowy stan (np. brak UI id)
- `E_TIMEOUT` – operacja przekroczyła czas
- `E_INTERNAL` – błąd wewnętrzny

---

## 2. OTUI (UI Bridge

)

### 2.1. Identyfikacja i wiązani

a

- Każdy element ma `id` (unikalny w layoucie).
- Zmiana właściwości przez emit:

```lua
-- Tekst w Label#status
ctx.emit("status", { text = "Running" })

```

**Mapowanie domyślne (bridge po id):**

| Emisja `target` | Element OTUI (przykład) | Pola                         |
| --------------- | ----------------------- | ---------------------------- |
| `"status"`      | `Label#status`          | `text`, `color?`, `visible?` |
| `"hp_bar"`      | `ProgressBar#hp_bar`    | `value`, `max?`, `color?`    |
| `"list"`        | `ListView#list`         | `items: string[]`            |

> TODO: dopisz Twoje id → obsługiwane pola.

### 2.2. Layout – przykła

d

```otui
Panel
  id: main
  size: 400 240
  anchor: top left

Label
  id: status
  text: "init"
  anchors.centerIn: parent

```

### 2.3. Zdarzenia z UI do Lu

a

UI może wywołać event do Lua:

```lua
ctx.on("ui.click.status", function(args) end)

```

> TODO: lista eventów z UI (klik, input, select) i payloady.

---

## 3. WebSocket (protokół

)

### 3.1. Kanał i try

b

- Transport: `wss://<host>/ws` (JSON UTF-8).
- Autoryzacja: JWT w `Authorization: Bearer <token>` lub cookie sesji.
- `Origin` allowlist; `pingTimeout`; rate-limit i maks. payload (np. 32KB).

### 3.2. Typy wiadomośc

i

#### Serwer → Klient (dashboard

)

```ts
type ServerEvent =
  | { type: "metrics.update"; ts: number; payload: { hp: number; mp: number; [k: string]: number } }
  | { type: "log.line"; ts: number; level: "debug" | "info" | "warn" | "error"; msg: string }
  | { type: "char.info"; ts: number; payload: { name: string; level: number; voc: string } }
  | { type: "cmd.result"; ts: number; id: string; ok: boolean; error?: string; data?: any };
```

#### Klient → Serwe

r

```ts
type ClientEvent =
  | { type: "cmd"; id: string; name: "START" | "STOP" | "RELOAD"; args?: any }
  | { type: "subscribe"; topics: string[] } // np. ["metrics.*","log.*"]
  | { type: "settings.update"; patch: Record<string, any> };
```

**Przykład**:

```json
{ "type": "cmd", "id": "abc123", "name": "START", "args": { "profile": "pvp" } }
```

### 3.3. JSON Schema (walidacja na serwerze

)

`schemas/ws/cmd.schema.json`

```json
{
  "$id": "ws/cmd.schema.json",
  "type": "object",
  "required": ["type", "id", "name"],
  "properties": {
    "type": { "const": "cmd" },
    "id": { "type": "string", "minLength": 1 },
    "name": { "type": "string", "enum": ["START", "STOP", "RELOAD"] },
    "args": { "type": "object", "additionalProperties": true }
  },
  "additionalProperties": false
}
```

> TODO: dodaj schematy `metrics.update`, `log.line`, `settings.update`, …

### 3.4. Błędy W

S

- `401` – brak/niepoprawny token
- `403` – brak uprawnień (RBAC)
- `429` – limit
- `4401` (app) – walidacja payloadu (`error: "E_SCHEMA"`)

---

## 4. C++ / rozszerzeni

a

**Szkic struktur (dopasuj do projektu):**

```cpp
// include/otcv8/api.h
struct OTEvent {
  const char* type;      // "metrics.update"
  uint64_t    ts_ms;
  const char* json;      // payload JSON
};

using OttoEmitFn = void(*)(const OTEvent* ev); // emit from C++ -> Lua/UI

```

**Punkty integracji:**

- Rejestracja hooków (zdarzenia gry → Lua)
- Export funkcji do Lua (np. `say`, `use_item`, …)
- Konwencja ładowania modułów C++: `dll/so` w `modules/<name>/bin/`.

> TODO: wstaw prawdziwe nagłówki i entrypointy.

---

## 5. Błędy i kod

y

| Kod        | Warstwa | Opis                           |
| ---------- | ------- | ------------------------------ |
| `E_ARG`    | Lua     | nieprawidłowy argument         |
| `E_STATE`  | Lua     | zły stan (np. brak UI id)      |
| `E_WS`     | WS      | połączenie zerwane             |
| `E_SCHEMA` | WS      | payload niezgodny ze schematem |
| `E_IO`     | C++/FS  | błąd I/O                       |
| `E_INT`    | All     | błąd wewnętrzny                |

Format odpowiedzi błędu (WS):

```json
{
  "type": "cmd.result",
  "ts": 1712345678,
  "id": "abc",
  "ok": false,
  "error": "E_SCHEMA",
  "data": { "path": "/args/profile" }
}
```

---

## 6. Bezpieczeństwo (skrót

)

- HTTPS/WSS, HSTS, twardy **CSP**.
- Token JWT krótki + refresh, **RBAC**.
- Check **Origin**, **rate-limit**, **message size**.
- Sekrety poza repo (env/CI), brak kluczy w repo.
- Logowanie dostępu i audyt komend WS.

---

## 7. Versionin

g

- SemVer API: `major.minor.patch`.
- Nagłówek `X-OTCv8-API: 1.x` (WS handshake).
- Zmiany łamiące → podbij **major** i utrzymuj `deprecated` min. 1 wersję.

---

## 8. Przykłady end‑to‑en

d

### 8.1. Status do U

I

```lua
-- modules/status/init.lua
local M = {}
function M.start(ctx)
  ctx.emit("status", { text = "Ready" })
end
return M

```

### 8.2. Telemetria do dashboard

u

```lua
local M = {}
function M.tick(ctx, dt)
  ctx.ws.send("metrics.update", { hp = getHp(), mp = getMp() })
end
return M

```

### 8.3. Komenda z dashboard

u

**UI → WS**

```json
{ "type": "cmd", "id": "run1", "name": "START", "args": { "profile": "pvp" } }
```

**WS → UI**

```json
{ "type": "cmd.result", "id": "run1", "ok": true, "ts": 1712345678 }
```

---

## 9. Generowanie referencji z kodu (automaty

)

### 9.1. Lua – LDo

c

Komentuj funkcje:

```lua
--- Wysyła wiadomość do czatu.
-- @tparam string msg
-- @treturn boolean ok
function say(msg) ... end

```

**Workflow**: `ldoc -d docs/lua/ref/ .` → włącz w `mkdocs.yml` (`nav`).

### 9.2. C++ – Doxyge

n

`Doxyfile` → HTML do `docs/cpp/ref/` → dodaj do `nav`.

### 9.3. WS – JSON Schema → markdow

n

Trzymaj schematy w `schemas/ws/*.schema.json` i buduj referencję:

```bash
# przykład narzędzia

npx @apitable/json-schema-to-markdown schemas/ws -o docs/ws/ref.md

```

---

## 10. Lista TODO do uzupełnieni

a

- [ ] Pełna lista eventów Lua (nazwy + parametry)
- [ ] Mapowania `ctx.emit(target)` → UI (id + pola)
- [ ] Zamknięta lista `ClientEvent`/`ServerEvent` + schematy
- [ ] Nagłówki/entrypointy C++ i rejestracja hooków
- [ ] Wygeneruj LDoc/Doxygen i dodaj do `nav`

?# Dev Module for Hot-Reload (MASTER) - **OTClient v8**

> Cel: dostarczyc **produkcyjny modul Lua** wspierajacy hot-reload skrypt�w OTClient oraz **NDJSON logowanie** do integracji ze Studio. Dokument zawiera: pelna strukture plik�w, kompletny kod, konfiguracje, protokoly, scenariusze testowe, checklisty i wskaz�wki operacyjne. **Transfer 1:1** - gotowe do wklejenia.

---
# # 0) Zalozenia i zakres
- **Hot-reload:** wyzwalane skr�tem klawiszowym w kliencie **lub** przez "flag file" (`modules/.dev/reload.flag`).
- **Logi NDJSON:** zapisywane do `modules/.dev/log.jsonl` (rotacja rozmiaru).
- **Bezpieczenstwo:** brak step-debuggera; debug przez logi i komunikaty.
- **Zaleznosci:** standardowe API OTClient v8 (m.in. `g_modules.reloadModules`, `g_resources.readFile/writeFile`, `addEvent/scheduleEvent`).

---
# # 1) Struktura plik�w modulu
```
modules/
?? dev/
   ?? dev.otmod
   ?? dev.lua
   ?? ui/
      ?? dev.otui   # (opcjonalne mini-UI)
# Katalog roboczy dla flag/log�w (musi istniec):
modules/.dev/
   ?? reload.flag   # plik-flaga (pusty lub z trescia)
   ?? log.jsonl     # NDJSON (tworzony automatycznie)
```
> Uwaga: Utw�rz katalog `modules/.dev/` recznie, jesli nie istnieje.

---
# # 2) `dev.otmod` (pelny plik)
```otml
name: dev
description: Development tools (hot-reload + NDJSON log)
# Modul laduje dev.lua przy starcie klienta
# (dodatkowe pola otmod wedlug konwencji projektu)
```

---
# # 3) `ui/dev.otui` (opcjonalny szkielet UI)
```otui
DevWindow < UIWidget {
  id: devWindow
  width: 260
  height: 120
  text: tr("Dev Tools")
}
```
> OTUI: wciecia 2 spacje; kolejnosc p�l: GEOMETRIA ? STYL ? ZACHOWANIE.

---
# # 4) `dev.lua` (pelny, produkcyjny kod modulu)
```lua
-- modules/dev/dev.lua
-- Dev tools: hot-reload via flag file + NDJSON logging
-- Wymaga katalogu: modules/.dev/

local M = {}

-- === Konfiguracja ===
local CFG = {
  flagPath = 'modules/.dev/reload.flag',
  logPath  = 'modules/.dev/log.jsonl',
  pollMs   = 400,      -- interwal sprawdzania flagi
  minReloadIntervalMs = 800, -- anty-drd
  maxLogBytes = 512 * 1024,  -- 512 KB rotacji
  echoToConsole = true,
}

-- === Stan modulu ===
local state = {
  lastReloadAt = 0,
  reloading = false,
  loopStarted = false,
}

-- === Utils ===
local function nowMs()
  if g_clock and g_clock.millis then
    return g_clock.millis()
  end
  -- fallback (sekundy ? ms)
  return (os.time() or 0) * 1000
end

local function jsonEscape(str)
  local s = tostring(str)
  s = s:gsub('\\', '\\\\')
       :gsub('\"', '\\"')
       :gsub('\n', '\\n')
       :gsub('\r', '\\r')
       :gsub('\t', '\\t')
  return s
end

local function isArrayTable(t)
  local i = 1
  for _ in pairs(t) do
    if t[i] == nil then return false end
    i = i + 1
  end
  return true
end

local function encodeJSON(v)
  local tv = type(v)
  if tv == 'nil' then return 'null' end
  if tv == 'boolean' then return v and 'true' or 'false' end
  if tv == 'number' then return tostring(v)
  elseif tv == 'string' then return '"' .. jsonEscape(v) .. '"' end
  if tv == 'table' then
    if isArrayTable(v) then
      local out = {}
      for i = 1, #v do out[#out+1] = encodeJSON(v[i]) end
      return '[' .. table.concat(out, ',') .. ']'
    else
      local out = {}
      for k, val in pairs(v) do
        out[#out+1] = '"' .. jsonEscape(k) .. '":' .. encodeJSON(val)
      end
      table.sort(out) -- stabilna kolejnosc kluczy
      return '{' .. table.concat(out, ',') .. '}'
    end
  end
  return 'null'
end

local function readFile(path)
  local ok, data = pcall(function() return g_resources.readFile(path) end)
  if not ok then return nil end
  return data
end

local function writeFile(path, data)
  local ok = pcall(function() return g_resources.writeFile(path, data or '') end)
  return ok == true
end

local function ensureLogSize(s)
  if #s <= CFG.maxLogBytes then return s end
  -- rotacja: obetnij do ostatnich maxLogBytes (od granicy \n jesli mozliwe)
  local cut = string.sub(s, -CFG.maxLogBytes)
  local p = cut:find('\n')
  if p then
    return cut:sub(p+1)
  end
  return cut
end

local function appendLine(path, line)
  local prev = readFile(path)
  local newContent
  if prev and #prev > 0 then
    if prev:sub(-1) ~= '\n' then prev = prev .. '\n' end
    newContent = prev .. line .. '\n'
  else
    newContent = line .. '\n'
  end
  newContent = ensureLogSize(newContent)
  writeFile(path, newContent)
end

local function isoTs()
  -- ISO8601 (sekundy + opcjonalne ms)
  local t = os.date('!*t')
  local base = string.format('%04d-%02d-%02dT%02d:%02d:%02d', t.year, t.month, t.day, t.hour, t.min, t.sec)
  local ms = 0
  if g_clock and g_clock.millis then ms = nowMs() % 1000 end
  return string.format('%s.%03dZ', base, ms)
end

local function log(level, tag, msg, meta)
  if CFG.echoToConsole then
    print(string.format('[dev][%s][%s] %s', level, tag or '-', msg or ''))
  end
  local obj = {
    ts = isoTs(),
    level = level or 'INFO',
    tag = tag or 'dev',
    file = 'modules/dev/dev.lua',
    line = 0,
    msg = tostring(msg or ''),
    meta = meta or {}
}
  appendLine(CFG.logPath, encodeJSON(obj))
end

-- === Log helpers ===
local function info(tag, msg, meta)  log('INFO', tag, msg, meta)  end
local function warn(tag, msg, meta)  log('WARN', tag, msg, meta)  end
local function errorLog(tag, msg, meta) log('ERROR', tag, msg, meta) end

-- === Hot-reload core ===
local function flagExists()
  local data = readFile(CFG.flagPath)
  return data ~= nil  -- istnienie pliku (nawet pustego)
end

local function clearFlag()
  writeFile(CFG.flagPath, '')
end

local function canReload()
  local t = nowMs()
  if state.reloading then return false end
  if (t - state.lastReloadAt) < CFG.minReloadIntervalMs then return false end
  return true
end

local function doReload(reason)
  if not canReload() then return false end
  state.reloading = true
  info('reload', 'requested', { reason = reason or 'flag' })
  local ok, err = pcall(function()
    g_modules.reloadModules()
  end)
  if ok then
    state.lastReloadAt = nowMs()
    info('reload', 'done', { ts = state.lastReloadAt })
  else
    errorLog('reload', 'failed', { error = tostring(err) })
  end
  state.reloading = false
  return ok
end

-- public API do recznego wywolania z konsoli
function M.requestReload(reason)
  return doReload(reason or 'manual')
end

local function loop()
  if flagExists() then
    clearFlag()
    doReload('flag')
  end
  scheduleEvent(loop, CFG.pollMs)
end

local function start()
  if state.loopStarted then return end
  state.loopStarted = true
  addEvent(function()
    info('startup', 'dev module ready', { pollMs = CFG.pollMs })
    loop()
  end)
end

-- start modulu
start()

return M
```

---
# # 5) Protok�l integracji ze **Studio**
- **Wyzwalanie reloadu:** Studio zapisuje/"dotyka" `modules/.dev/reload.flag` ? modul wykrywa i wola `g_modules.reloadModules()`.
- **Logi NDJSON:** Studio tail-uje `modules/.dev/log.jsonl` i filtruje po `level/tag/file:line`.
- **Akcje reczne:** z konsoli: `modules.dev.dev.requestReload('manual')` (jezeli srodowisko wspiera wywolania).

---
# # 6) Konfiguracja i warianty
- `CFG.pollMs` - interwal sprawdzania flagi (zalecane 300-600 ms).
- `CFG.minReloadIntervalMs` - anty-drganie przy seryjnych zapisach.
- `CFG.maxLogBytes` - rotacja logu (zapobiega rozrostowi pliku).
- `CFG.echoToConsole` - mirror log�w do konsoli klienta.

> Zmiany konfiguracji wprowadzaj w `dev.lua` i przeladuj moduly.

---
# # 7) Scenariusze testowe (QA)
1. **Start modulu:** uruchom klienta ? w `log.jsonl` linia `startup/dev module ready`.
2. **Reload przez flage:** utw�rz pusty `modules/.dev/reload.flag` ? w logu `reload/requested` i `reload/done`.
3. **Anty-drganie:** utw�rz 3� flage w < 800 ms ? 1 realny reload.
4. **Blad podczas reloadu (symulacja):** tymczasowo zasymuluj blad w `g_modules.reloadModules` (jesli mozliwe) ? `reload/failed` (ERROR) w logu.
5. **Rotacja logu:** wygeneruj > `maxLogBytes` ? plik przyciety do dozwolonego rozmiaru, bez rozbicia JSON.

---
# # 8) Checklisty wdrozeniowe
- [ ] Utw�rz `modules/.dev/` (zapisywalny katalog).
- [ ] Skopiuj `dev.otmod`, `dev.lua`, opcjonalnie `ui/dev.otui` do `modules/dev/`.
- [ ] Uruchom klienta; sprawdz, czy `log.jsonl` powstal.
- [ ] Zapisz/"dotknij" `modules/.dev/reload.flag`; obserwuj `log.jsonl`.
- [ ] Skonfiguruj Studio, by tail-owalo `log.jsonl` i zapisywalo flage.

---
# # 9) Noty operacyjne
- Jesli `modules/.dev/` nie istnieje lub brak uprawnien zapisu, **logi trafia tylko na konsole** (zaleznie od `echoToConsole`).
- `writeFile` nadpisuje - dlatego **append** realizujemy przez odczyt?doklejenie?zapis + rotacje.
- Wydziel logowanie ciezkie (duze `meta`) - moze spowolnic zapis; zalecane kr�tkie pola.

---
# # 10) Rozszerzenia (opcjonalne)
- **Keybind reloadu:** dodac skr�t klawiszowy wiazacy `M.requestReload()` (jesli srodowisko udostepnia mapowanie klawiszy).
- **UI DevWindow:** przyciski *Request Reload*, *Open Log*, licznik reload�w.
- **Heartbeat:** wpis NDJSON co X sekund potwierdzajacy zywotnosc modulu.

---
# # 11) Definition of Done (DoD)
- [ ] Modul laduje sie, loguje `startup` (NDJSON + konsola).
- [ ] Flaga wyzwala `reload` deterministycznie (z anty-drganiem).
- [ ] Rotacja logu dziala; plik nie rosnie nieograniczenie.
- [ ] Studio wykrywa logi i poprawnie je filtruje.
- [ ] Brak globali; `local` wszedzie; brak uzycia `unpack` (tylko `table.unpack`).

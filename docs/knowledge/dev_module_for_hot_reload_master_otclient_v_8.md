# Dev Module for HotĂ˘â‚¬â€Reload (MASTER) â€“ **OTClient v8**

> Cel: dostarczyÄ‡ **produkcyjny moduÄąâ€š Lua** wspierajÄ…cy hotĂ˘â‚¬â€reload skryptĂłw OTClient oraz **NDJSON logowanie** do integracji ze Studio. Dokument zawiera: peÄąâ€šnÄ… strukturÄ™ plikĂłw, kompletny kod, konfiguracjÄ™, protokoÄąâ€šy, scenariusze testowe, checklisty i wskazĂłwki operacyjne. **Transfer 1:1** â€“ gotowe do wklejenia.

---
## 0) ZaÄąâ€šoÄąÄ˝enia i zakres
- **HotĂ˘â‚¬â€reload:** wyzwalane skrĂłtem klawiszowym w kliencie **lub** przez â€žflag fileâ€ť (`modules/.dev/reload.flag`).
- **Logi NDJSON:** zapisywane do `modules/.dev/log.jsonl` (rotacja rozmiaru).
- **BezpieczeÄąâ€žstwo:** brak stepĂ˘â‚¬â€debuggera; debug przez logi i komunikaty.
- **ZaleÄąÄ˝noÄąâ€şci:** standardowe API OTClient v8 (m.in. `g_modules.reloadModules`, `g_resources.readFile/writeFile`, `addEvent/scheduleEvent`).

---
## 1) Struktura plikĂłw moduÄąâ€šu
`$fenceInfo
modules/
Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ dev/
   Ă˘â€ťĹ›Ă˘â€ťâ‚¬ dev.otmod
   Ă˘â€ťĹ›Ă˘â€ťâ‚¬ dev.lua
   Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ ui/
      Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ dev.otui   # (opcjonalne miniĂ˘â‚¬â€UI)
# Katalog roboczy dla flag/logĂłw (musi istnieÄ‡):
modules/.dev/
   Ă˘â€ťĹ›Ă˘â€ťâ‚¬ reload.flag   # plikĂ˘â‚¬â€flaga (pusty lub z treÄąâ€şciÄ…)
   Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ log.jsonl     # NDJSON (tworzony automatycznie)
```
> Uwaga: UtwĂłrz katalog `modules/.dev/` rÄ™cznie, jeÄąâ€şli nie istnieje.

---
## 2) `dev.otmod` (peÄąâ€šny plik)
`$fenceInfo
name: dev
description: Development tools (hot-reload + NDJSON log)
# ModuÄąâ€š Äąâ€šaduje dev.lua przy starcie klienta
# (dodatkowe pola otmod wedÄąâ€šug konwencji projektu)
```

---
## 3) `ui/dev.otui` (opcjonalny szkielet UI)
`$fenceInfo
DevWindow < UIWidget {
  id: devWindow
  width: 260
  height: 120
  text: tr("Dev Tools")
}
```
> OTUI: wciÄ™cia 2 spacje; kolejnoÄąâ€şÄ‡ pĂłl: GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE.

---
## 4) `dev.lua` (peÄąâ€šny, produkcyjny kod moduÄąâ€šu)
`$fenceInfo
-- modules/dev/dev.lua
-- Dev tools: hot-reload via flag file + NDJSON logging
-- Wymaga katalogu: modules/.dev/

local M = {}

-- === Konfiguracja ===
local CFG = {
  flagPath = 'modules/.dev/reload.flag',
  logPath  = 'modules/.dev/log.jsonl',
  pollMs   = 400,      -- interwaÄąâ€š sprawdzania flagi
  minReloadIntervalMs = 800, -- anty-drd
  maxLogBytes = 512 * 1024,  -- 512 KB rotacji
  echoToConsole = true,
}

-- === Stan moduÄąâ€šu ===
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
  -- fallback (sekundy Ă˘â€ â€™ ms)
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
      table.sort(out) -- stabilna kolejnoÄąâ€şÄ‡ kluczy
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
  -- rotacja: obetnij do ostatnich maxLogBytes (od granicy \n jeÄąâ€şli moÄąÄ˝liwe)
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

-- public API do rÄ™cznego wywoÄąâ€šania z konsoli
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

-- start moduÄąâ€šu
start()

return M
```

---
## 5) ProtokĂłÄąâ€š integracji ze **Studio**
- **Wyzwalanie reloadu:** Studio zapisuje/"dotyka" `modules/.dev/reload.flag` Ă˘â€ â€™ moduÄąâ€š wykrywa i woÄąâ€ša `g_modules.reloadModules()`.
- **Logi NDJSON:** Studio tailĂ˘â‚¬â€uje `modules/.dev/log.jsonl` i filtruje po `level/tag/file:line`.
- **Akcje rÄ™czne:** z konsoli: `modules.dev.dev.requestReload('manual')` (jeÄąÄ˝eli Äąâ€şrodowisko wspiera wywoÄąâ€šania).

---
## 6) Konfiguracja i warianty
- `CFG.pollMs` â€“ interwaÄąâ€š sprawdzania flagi (zalecane 300â€“600 ms).
- `CFG.minReloadIntervalMs` â€“ antyĂ˘â‚¬â€drganie przy seryjnych zapisach.
- `CFG.maxLogBytes` â€“ rotacja logu (zapobiega rozrostowi pliku).
- `CFG.echoToConsole` â€“ mirror logĂłw do konsoli klienta.

> Zmiany konfiguracji wprowadzaj w `dev.lua` i przeÄąâ€šaduj moduÄąâ€šy.

---
## 7) Scenariusze testowe (QA)
1. **Start moduÄąâ€šu:** uruchom klienta Ă˘â€ â€™ w `log.jsonl` linia `startup/dev module ready`.
2. **Reload przez flagÄ™:** utwĂłrz pusty `modules/.dev/reload.flag` Ă˘â€ â€™ w logu `reload/requested` i `reload/done`.
3. **AntyĂ˘â‚¬â€drganie:** utwĂłrz 3Ä‚â€” flagÄ™ w < 800 ms Ă˘â€ â€™ 1 realny reload.
4. **BÄąâ€šÄ…d podczas reloadu (symulacja):** tymczasowo zasymuluj bÄąâ€šÄ…d w `g_modules.reloadModules` (jeÄąâ€şli moÄąÄ˝liwe) Ă˘â€ â€™ `reload/failed` (ERROR) w logu.
5. **Rotacja logu:** wygeneruj > `maxLogBytes` Ă˘â€ â€™ plik przyciÄ™ty do dozwolonego rozmiaru, bez rozbicia JSON.

---
## 8) Checklisty wdroÄąÄ˝eniowe
- [ ] UtwĂłrz `modules/.dev/` (zapisywalny katalog).
- [ ] Skopiuj `dev.otmod`, `dev.lua`, opcjonalnie `ui/dev.otui` do `modules/dev/`.
- [ ] Uruchom klienta; sprawdÄąĹź, czy `log.jsonl` powstaÄąâ€š.
- [ ] Zapisz/"dotknij" `modules/.dev/reload.flag`; obserwuj `log.jsonl`.
- [ ] Skonfiguruj Studio, by tailĂ˘â‚¬â€owaÄąâ€šo `log.jsonl` i zapisywaÄąâ€šo flagÄ™.

---
## 9) Noty operacyjne
- JeÄąâ€şli `modules/.dev/` nie istnieje lub brak uprawnieÄąâ€ž zapisu, **logi trafiÄ… tylko na konsolÄ™** (zaleÄąÄ˝nie od `echoToConsole`).
- `writeFile` nadpisuje â€“ dlatego **append** realizujemy przez odczytĂ˘â€ â€™doklejenieĂ˘â€ â€™zapis + rotacjÄ™.
- Wydziel logowanie ciÄ™ÄąÄ˝kie (duÄąÄ˝e `meta`) â€“ moÄąÄ˝e spowolniÄ‡ zapis; zalecane krĂłtkie pola.

---
## 10) Rozszerzenia (opcjonalne)
- **Keybind reloadu:** dodaÄ‡ skrĂłt klawiszowy wiÄ…ÄąÄ˝Ä…cy `M.requestReload()` (jeÄąâ€şli Äąâ€şrodowisko udostÄ™pnia mapowanie klawiszy).
- **UI DevWindow:** przyciski *Request Reload*, *Open Log*, licznik reloadĂłw.
- **Heartbeat:** wpis NDJSON co X sekund potwierdzajÄ…cy ÄąÄ˝ywotnoÄąâ€şÄ‡ moduÄąâ€šu.

---
## 11) Definition of Done (DoD)
- [ ] ModuÄąâ€š Äąâ€šaduje siÄ™, loguje `startup` (NDJSON + konsola).
- [ ] Flaga wyzwala `reload` deterministycznie (z antyĂ˘â‚¬â€drganiem).
- [ ] Rotacja logu dziaÄąâ€ša; plik nie roÄąâ€şnie nieograniczenie.
- [ ] Studio wykrywa logi i poprawnie je filtruje.
- [ ] Brak globali; `local` wszÄ™dzie; brak uÄąÄ˝ycia `unpack` (tylko `table.unpack`).


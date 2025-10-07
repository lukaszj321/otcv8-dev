# vBot Playbook â€“ **modules/game_bot (MASTER)**

> Cel: peÄąâ€šny, operacyjny przewodnik dla implementacji i utrzymania skryptĂłw **vBot** (moduÄąâ€š `modules/game_bot`) w ramach **OTClient Studio**. Dokument zawiera: standardy kodowania, wzorce (makra/triggerĂ˘â‚¬â„˘y), snippety, heurystyki skanera, wymagania jakoÄąâ€şciowe, checklisty, testĂ˘â‚¬â€wektory i integracjÄ™ z narzÄ™dziem. **Transfer 1:1** â€“ gotowe do wdroÄąÄ˝enia.

---
## 0) Executive Summary
- **Co obejmuje:** makra okresowe, triggerĂ˘â‚¬â„˘y eventowe, interakcje z UI/Äąâ€şwiatem gry, wzorce bezpieczeÄąâ€žstwa, logowanie, diagnostykÄ™ i performance.
- **Jak uÄąÄ˝ywaÄ‡:** jako *ÄąĹźrĂłdÄąâ€šo prawdy* dla generatorĂłw w Studio (szablony vBot), lint vBot (reguÄąâ€šy domenowe) oraz heurystyk skanera (detekcja symboli vBot w kodzie).

---
## 1) SÄąâ€šownik i konwencje
- **Makro** â€“ blok wykonywany cyklicznie (interwaÄąâ€š ms) lub sterowany warunkiem.
- **Trigger** â€“ blok reagujÄ…cy na zdarzenie (np. wiadomoÄąâ€şÄ‡, zmiana HP, wejÄąâ€şcie na tile).
- **Guard** â€“ warunek bezpieczeÄąâ€žstwa (np. `isConnected()`, `not isBusy()`), ktĂłry musi byÄ‡ speÄąâ€šniony przed akcjÄ….
- **Cooldown** â€“ minimalny czas miÄ™dzy kolejnymi akcjami (zapobiega spamowi).
- **State** â€“ lokalny stan makra (zapamiÄ™tanie poprzedniej decyzji/targetu).

Konwencje nazewnictwa (zalecane):
- Pliki: `vb_<obszar>_<cel>.lua` np. `vb_combat_uh.lua`.
- Funkcje lokalne: `vb_<obszar>_<akcja>()` np. `vb_heal_cast()`.
- Zmienne stanu: `state_<nazwa>`.
- Logi: prefiks `"[vBot]"` i tagi (`[heal]`, `[loot]`).

---
## 2) Architektura vBot (w ujÄ™ciu skryptowym)
- **Warstwa zdarzeÄąâ€ž gry** Ă˘â€ â€™ callbacki (np. text message, damage, map change).
- **Warstwa makr** Ă˘â€ â€™ pÄ™tle interwaÄąâ€šowe i warunki.
- **Warstwa akcji** Ă˘â€ â€™ uÄąÄ˝ycia czarĂłw/przedmiotĂłw, ruch, interakcja z UI.
- **Warstwa narzÄ™dzi** Ă˘â€ â€™ helpers (cooldown, debouncing, retry), logowanie NDJSON (opcjonalnie).

KaÄąÄ˝dy komponent powinien byÄ‡ **izolowany** (funkcje `local`, brak globali), testowalny oraz posiadaÄ‡ jasne **guards**.

---
## 3) Wzorce (makra i triggerĂ˘â‚¬â„˘y)
> PoniÄąÄ˝sze wzorce to gotowe schematy do generatora w Studio. KaÄąÄ˝dy zawiera: cel, preĂ˘â‚¬â€warunki, interfejs konfiguracyjny, guards, cooldown, logowanie oraz sekcjÄ™ bezpieczeÄąâ€žstwa.
## 3.1 Makro: AutoĂ˘â‚¬â€Heal na progu HP
**Cel:** rzucenie czaru/ uÄąÄ˝ycie pota, gdy HP < progu.

**Konfiguracja (OTML/JSON dla Studio):**
`$fenceInfo
{"name":"vb_auto_heal","threshold":60,"spell":"exura","cooldownMs":1200}
```

**Szkielet (Lua):**
`$fenceInfo
-- vb_auto_heal.lua
local THRESHOLD = 60      -- procent
local SPELL = 'exura'
local COOLDOWN = 1200     -- ms

local last = 0
local function can()
  return g_game.isOnline() and not g_game.isAttacking() and not g_game.isWalking()
end

local function now() return g_clock.millis() end

local function tick()
  if not can() then return end
  local hp = g_game.getLocalPlayer() and g_game.getLocalPlayer():getHealthPercent() or 100
  if hp < THRESHOLD and (now() - last) > COOLDOWN then
    say(SPELL)
    last = now()
    print('[vBot][heal] cast', SPELL, 'hp', hp)
  end
end

-- rejestracja makra w schedulerze (implementacja zaleÄąÄ˝na od Äąâ€şrodowiska vBot)
-- macro(200, tick) -- jeÄąâ€şli Äąâ€şrodowisko udostÄ™pnia
-- w OTC Studio: dodaj do pÄ™tli narzÄ™dzia lub harmonogramu moduÄąâ€šu
```

**BezpieczeÄąâ€žstwo:** sprawdÄąĹź `g_game.isOnline()`, wstrzymaj w czasie `isWalking()`; cooldown Ă˘â€°Ä„ GCD klienta, sprawdÄąĹź manÄ™ przed `say()`.
## 3.2 Trigger: Reakcja na wiadomoÄąâ€şÄ‡ tekstowÄ…
**Cel:** wykrycie frazy i akcja (np. odpowiedÄąĹź, log, zapis zdarzenia).

**Konfiguracja:**
`$fenceInfo
{"name":"vb_msg_react","match":"^hi$","reply":"hello"}
```

**Szkielet (Lua):**
`$fenceInfo
-- vb_msg_react.lua
local PATTERN = '^hi$'
local REPLY = 'hello'

local function onTextMessage(mode, text)
  if not g_game.isOnline() then return end
  if text:lower():match(PATTERN) then
    print('[vBot][msg] match:', text)
    say(REPLY)
  end
end

-- rejestracja: attach do zdarzenia tekstowego w Äąâ€şrodowisku vBot/OTClient
-- modules.game_textmessage.onTextMessage:connect(onTextMessage) -- przykÄąâ€šad; dostosuj do dostÄ™pnych hookĂłw
```

**BezpieczeÄąâ€žstwo:** sanitacja regex (escape), limit odpowiedzi (cooldown per nadawca), nie odpowiadaj na wÄąâ€šasne linie.
## 3.3 Makro: AutoĂ˘â‚¬â€Haste (buff w ruchu)
**Cel:** utrzymywanie buffa szybkoÄąâ€şci przy poruszaniu siÄ™.

**Konfiguracja:**
`$fenceInfo
{"name":"vb_auto_haste","spell":"utani hur","cooldownMs":6000}
```

**Szkielet:**
`$fenceInfo
local SPELL = 'utani hur'
local COOLDOWN = 6000
local last = 0

local function hasHaste()
  -- sprawdÄąĹź ikony buffĂłw na UI lub stan gracza (jeÄąâ€şli dostÄ™pny)
  return false
end

local function tick()
  if not g_game.isOnline() then return end
  if g_game.isWalking() and not hasHaste() and (g_clock.millis() - last) > COOLDOWN then
    say(SPELL)
    last = g_clock.millis()
    print('[vBot][buff] haste cast')
  end
end

-- macro(300, tick)
```

**BezpieczeÄąâ€žstwo:** nie spamuj â€“ sprawdÄąĹź buff i cooldown; upewnij siÄ™, ÄąÄ˝e gracz ma manÄ™.
## 3.4 Trigger: Loot po ubiciu potwora
**Cel:** podniesienie Äąâ€šupu po wykryciu ciaÄąâ€ša.

**Szkielet (zarys):**
`$fenceInfo
local function onTileAddThing(tile, thing)
  if not g_game.isOnline() then return end
  if thing:isContainer() and thing:isCorpse() then
    -- logika lootu; otwarcie kontenera, iteracja zawartoÄąâ€şci, use()
  end
end

-- rejestracja na event mapy/tili (zaleÄąÄ˝na od dostÄ™pnych hookĂłw Äąâ€şrodowiska)
```

**BezpieczeÄąâ€žstwo:** limit rĂłwnolegÄąâ€šych otwarÄ‡; przerwij, gdy inventory peÄąâ€šne; nie blokuj gÄąâ€šĂłwnej pÄ™tli.
## 3.5 Makro: AntiĂ˘â‚¬â€Idle
**Cel:** zapobiec disconnectowi przez delikatnÄ… interakcjÄ™.

**Szkielet:**
`$fenceInfo
local last = 0
local function tick()
  if not g_game.isOnline() then return end
  if g_clock.millis() - last > 60*1000 then
    turn(math.random(0,3))
    last = g_clock.millis()
    print('[vBot][antiidle] turn')
  end
end
-- macro(1000, tick)
```

**BezpieczeÄąâ€žstwo:** nie wykonuj w trakcie walki; nie przeszkadzaj w rÄ™cznych akcjach.

---
## 4) Heurystyki skanera (detekcja vBot)
> Celem jest wiarygodne wykrycie â€žkodu vBotâ€ť i jego relacji, bez uruchamiania Lua.

- **SygnaÄąâ€šy makr:** obecnoÄąâ€şÄ‡ wywoÄąâ€šaÄąâ€ž `macro(`, wzorce â€žscheduler/macro loopâ€ť (identyfikatory `macro`, `scheduleEvent`, `addEvent` z typowÄ… semantykÄ… okresowÄ…).
- **SygnaÄąâ€šy triggerĂ˘â‚¬â„˘Ăłw:** funkcje o nazwach `onX...` (np. `onTextMessage`) podpinane do znanych sygnaÄąâ€šĂłw moduÄąâ€šĂłw (np. *text message module*, *map events*).
- **SÄąâ€šowa kluczowe domeny:** `say(`, `use(`, `useWith(`, `walkTo(`, `turn(`, `attack(`, identyfikatory zasobĂłw (`ui/Ă˘â‚¬Â¦otui`).
- **Relacje:** `g_ui.loadUI('Ă˘â‚¬Â¦')` Ă˘â€ â€ť `lua_to_otui` (do mapowania UI z logikÄ… vBot).
- **Klasyfikacja plikĂłw:** prefiks `vb_`, lokalizacja w `modules/game_bot/Ă˘â‚¬Â¦` podnosi wagÄ™ dopasowania.

**Emisja do `project-index.json`:** wÄ™zeÄąâ€š `symbols.botSymbols`:
`$fenceInfo
{"heal":["modules/game_bot/vb_combat_uh.lua:12"],"antiidle":["modules/game_bot/vb_anti_idle.lua:5"]}
```

---
## 5) ReguÄąâ€šy jakoÄąâ€şci (lint vBot)
> Rozszerzenie lintu Lua/OTUI o reguÄąâ€šy domenowe vBot (bez autoĂ˘â‚¬â€fixu, chyba ÄąÄ˝e bezpieczny).

- **VBOTĂ˘â‚¬â€001** â€“ Brak `guard` przed akcjÄ… (wymagane `g_game.isOnline()` i brak kolizji z ruchem/walkÄ…, jeÄąâ€şli ma znaczenie).
- **VBOTĂ˘â‚¬â€002** â€“ Cooldown < zalecanego minimum dla danej akcji (np. < 1000 ms dla czaru) Ă˘â€ â€™ WARN.
- **VBOTĂ˘â‚¬â€003** â€“ BlokujÄ…ce pÄ™tle/sleep w makrze (zamiast tego `scheduleEvent`).
- **VBOTĂ˘â‚¬â€004** â€“ Spam `say()`/`use()` bez limitu â€“ brak licznika/okna czasowego.
- **VBOTĂ˘â‚¬â€005** â€“ Globalne symbole w pliku vBot (wymagane `local`).
- **VBOTĂ˘â‚¬â€006** â€“ Brak logowania kontekstowego przy krytycznych akcjach.
- **VBOTĂ˘â‚¬â€007** â€“ Brak anulowania makra po `isDisconnected()`.
- **VBOTĂ˘â‚¬â€008** â€“ ZaleÄąÄ˝noÄąâ€şÄ‡ od UI bez sprawdzenia istnienia `widget`.

**Konfiguracja (JSON):**
`$fenceInfo
{"VBOT-001":{"enabled":true,"severity":"ERROR"},"VBOT-002":{"enabled":true,"severity":"WARN","minCooldownMs":1000}}
```

---
## 6) Logowanie i telemetria (opcjonalnie NDJSON)
- Format linii (zalecany): `{ts, level, tag, file, line, msg, meta}`.
- Tagi: `[heal]`, `[msg]`, `[buff]`, `[loot]`, `[antiidle]`.
- Logi krytyczne: akcje `say/use` z parametrami i wynikiem.
- Integracja ze Studio: panel Log Viewer filtruje po `tag/level/file:line`.

**PrzykÄąâ€šad:**
`$fenceInfo
{"ts":"2025-10-02T12:00:00.000Z","level":"INFO","tag":"heal","file":"modules/game_bot/vb_auto_heal.lua","line":18,"msg":"cast","meta":{"spell":"exura","hp":43}}
```

---
## 7) BezpieczeÄąâ€žstwo i zgodnoÄąâ€şÄ‡
- **Idempotencja:** makra nie powinny powodowaÄ‡ skutkĂłw ubocznych przy powtarzaniu (guard+cooldown).
- **OstroÄąÄ˝noÄąâ€şÄ‡ UI:** sprawdzaj istnienie widgetĂłw przed modyfikacjÄ… (`if widget then ...`).
- **Zasoby:** nie uÄąÄ˝ywaj nieistniejÄ…cych Äąâ€şcieÄąÄ˝ek; weryfikuj z `assets-map.json`.
- **Granice:** makra nie powinny ingerowaÄ‡ w pliki poza katalogiem projektu.

---
## 8) WydajnoÄąâ€şÄ‡
- InterwaÄąâ€šy: nie schodÄąĹź poniÄąÄ˝ej 150â€“250 ms dla ogĂłlnych makr; kosztowne operacje (skany mapy/UI) Ă˘â€°Ä„ 1000 ms.
- Unikaj peÄąâ€šnych skanĂłw co tick â€“ cache wynikĂłw, porĂłwnuj zmiany.
- UÄąÄ˝ywaj `scheduleEvent` zamiast pÄ™tli blokujÄ…cych; debounce wejÄąâ€şcia.

---
## 9) Generator vBot (szablony do Studio)
**WejÄąâ€şcie:** parametry (JSON/OTML) â€“ np. `threshold`, `spell`, `cooldownMs`.
**WyjÄąâ€şcie:** plik `vb_<nazwa>.lua` + wpis w module (opcjonalny UI konfiguracyjny).
**Checklista generacji:**
- [ ] Plik w `modules/game_bot/Ă˘â‚¬Â¦`.
- [ ] Nazwy `local`, brak globali.
- [ ] Guards i cooldown zaimplementowane.
- [ ] Logi z prefiksem `[vBot]` i tagiem.
- [ ] Komentarz nagÄąâ€šĂłwkowy (opis, parametry, interwaÄąâ€š).

---
## 10) TestĂ˘â‚¬â€wektory (QA vBot)
- **HEALĂ˘â‚¬â€01:** HP 55% Ă˘â€ â€™ oczekiwany 1Ä‚â€” `say('exura')`, brak spam w 1200 ms.
- **MSGĂ˘â‚¬â€01:** Tekst `hi` Ă˘â€ â€™ odpowiedÄąĹź `hello` tylko 1Ä‚â€” / 3 s na nadawcÄ™.
- **HASTEĂ˘â‚¬â€01:** Ruch z brakiem buffa Ă˘â€ â€™ `say('utani hur')` nie czÄ™Äąâ€şciej niÄąÄ˝ co 6 s.
- **LOOTĂ˘â‚¬â€01:** Pojawia siÄ™ `corpse` na tile Ă˘â€ â€™ wywoÄąâ€šanie `use()` na kontenerze (jeÄąâ€şli dostÄ™pne API); brak bÄąâ€šÄ™dĂłw przy braku miejsca.
- **IDLEĂ˘â‚¬â€01:** Brak aktywnoÄąâ€şci 60 s Ă˘â€ â€™ `turn()`; brak gdy `isAttacking()`.

---
## 11) Integracja ze Studio
- **Skaner:** heurystyki z Â§4 zasilajÄ… `symbols.botSymbols`.
- **Lint:** reguÄąâ€šy z Â§5 uzupeÄąâ€šniajÄ… lint Lua (domena vBot).
- **Generator:** szablony z Â§9 dostÄ™pne w panelu â€žNowy Ă˘â€ â€™ vBotâ€ť.
- **Dokumentacja:** panel â€žvBot Playbookâ€ť linkuje do wzorcĂłw i przykÄąâ€šadĂłw.

---
## 12) Checklisty wdroÄąÄ˝eniowe
- [ ] KaÄąÄ˝de makro/trigger ma guards i cooldown.
- [ ] Brak globali; `local` wszÄ™dzie.
- [ ] Logi akcji krytycznych.
- [ ] Parametry wyniesione do konfiguracji.
- [ ] TestĂ˘â‚¬â€wektory przechodzÄ…; brak regresji.

---
## 13) Noty koÄąâ€žcowe
- Wzorce sÄ… rozszerzalne; dodajÄ…c nowe, zachowaj nazewnictwo i sekcje: *cel Ă˘â€ â€™ konfiguracja Ă˘â€ â€™ guards Ă˘â€ â€™ cooldown Ă˘â€ â€™ logi Ă˘â€ â€™ testy*.
- Wszelkie modyfikacje wymagajÄ… aktualizacji generatora i reguÄąâ€š QA.



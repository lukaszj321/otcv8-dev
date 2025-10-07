# vBot Playbook - **modules/game_bot (MASTER)**

> Cel: peL'ny, operacyjny przewodnik dla implementacji i utrzymania skryptow **vBot** (moduL' `modules/game_bot`) w ramach **OTClient Studio**. Dokument zawiera: standardy kodowania, wzorce (makra/triggeray), snippety, heurystyki skanera, wymagania jakoLciowe, checklisty, testa'wektory i integracje z narzedziem. **Transfer 1:1** - gotowe do wdroLLenia.

---
## 0) Executive Summary
- **Co obejmuje:** makra okresowe, triggeray eventowe, interakcje z UI/Lwiatem gry, wzorce bezpieczeL"stwa, logowanie, diagnostyke i performance.
- **Jak uLLywac:** jako *LsrodL'o prawdy* dla generatorow w Studio (szablony vBot), lint vBot (reguL'y domenowe) oraz heurystyk skanera (detekcja symboli vBot w kodzie).

---
## 1) SL'ownik i konwencje
- **Makro** - blok wykonywany cyklicznie (interwaL' ms) lub sterowany warunkiem.
- **Trigger** - blok reagujacy na zdarzenie (np. wiadomoLc, zmiana HP, wejLcie na tile).
- **Guard** - warunek bezpieczeL"stwa (np. `isConnected()`, `not isBusy()`), ktory musi byc speL'niony przed akcja.
- **Cooldown** - minimalny czas miedzy kolejnymi akcjami (zapobiega spamowi).
- **State** - lokalny stan makra (zapamietanie poprzedniej decyzji/targetu).

Konwencje nazewnictwa (zalecane):
- Pliki: `vb_<obszar>_<cel>.lua` np. `vb_combat_uh.lua`.
- Funkcje lokalne: `vb_<obszar>_<akcja>()` np. `vb_heal_cast()`.
- Zmienne stanu: `state_<nazwa>`.
- Logi: prefiks `"[vBot]"` i tagi (`[heal]`, `[loot]`).

---
## 2) Architektura vBot (w ujeciu skryptowym)
- **Warstwa zdarzeL" gry** a' callbacki (np. text message, damage, map change).
- **Warstwa makr** a' petle interwaL'owe i warunki.
- **Warstwa akcji** a' uLLycia czarow/przedmiotow, ruch, interakcja z UI.
- **Warstwa narzedzi** a' helpers (cooldown, debouncing, retry), logowanie NDJSON (opcjonalnie).

KaLLdy komponent powinien byc **izolowany** (funkcje `local`, brak globali), testowalny oraz posiadac jasne **guards**.

---
## 3) Wzorce (makra i triggeray)
> PoniLLsze wzorce to gotowe schematy do generatora w Studio. KaLLdy zawiera: cel, prea'warunki, interfejs konfiguracyjny, guards, cooldown, logowanie oraz sekcje bezpieczeL"stwa.
## 3.1 Makro: Autoa'Heal na progu HP
**Cel:** rzucenie czaru/ uLLycie pota, gdy HP < progu.

**Konfiguracja (OTML/JSON dla Studio):**
{"name":"vb_auto_heal","threshold":60,"spell":"exura","cooldownMs":1200}
```

**Szkielet (Lua):**
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

-- rejestracja makra w schedulerze (implementacja zaleLLna od Lrodowiska vBot)
-- macro(200, tick) -- jeLli Lrodowisko udostepnia
-- w OTC Studio: dodaj do petli narzedzia lub harmonogramu moduL'u
```

**BezpieczeL"stwo:** sprawdLs `g_game.isOnline()`, wstrzymaj w czasie `isWalking()`; cooldown aA GCD klienta, sprawdLs mane przed `say()`.
## 3.2 Trigger: Reakcja na wiadomoLc tekstowa
**Cel:** wykrycie frazy i akcja (np. odpowiedLs, log, zapis zdarzenia).

**Konfiguracja:**
{"name":"vb_msg_react","match":"^hi$","reply":"hello"}
```

**Szkielet (Lua):**
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

-- rejestracja: attach do zdarzenia tekstowego w Lrodowisku vBot/OTClient
-- modules.game_textmessage.onTextMessage:connect(onTextMessage) -- przykL'ad; dostosuj do dostepnych hookow
```

**BezpieczeL"stwo:** sanitacja regex (escape), limit odpowiedzi (cooldown per nadawca), nie odpowiadaj na wL'asne linie.
## 3.3 Makro: Autoa'Haste (buff w ruchu)
**Cel:** utrzymywanie buffa szybkoLci przy poruszaniu sie.

**Konfiguracja:**
{"name":"vb_auto_haste","spell":"utani hur","cooldownMs":6000}
```

**Szkielet:**
local SPELL = 'utani hur'
local COOLDOWN = 6000
local last = 0

local function hasHaste()
  -- sprawdLs ikony buffow na UI lub stan gracza (jeLli dostepny)
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

**BezpieczeL"stwo:** nie spamuj - sprawdLs buff i cooldown; upewnij sie, LLe gracz ma mane.
## 3.4 Trigger: Loot po ubiciu potwora
**Cel:** podniesienie L'upu po wykryciu ciaL'a.

**Szkielet (zarys):**
local function onTileAddThing(tile, thing)
  if not g_game.isOnline() then return end
  if thing:isContainer() and thing:isCorpse() then
    -- logika lootu; otwarcie kontenera, iteracja zawartoLci, use()
  end
end

-- rejestracja na event mapy/tili (zaleLLna od dostepnych hookow Lrodowiska)
```

**BezpieczeL"stwo:** limit rownolegL'ych otwarc; przerwij, gdy inventory peL'ne; nie blokuj gL'ownej petli.
## 3.5 Makro: Antia'Idle
**Cel:** zapobiec disconnectowi przez delikatna interakcje.

**Szkielet:**
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

**BezpieczeL"stwo:** nie wykonuj w trakcie walki; nie przeszkadzaj w recznych akcjach.

---
## 4) Heurystyki skanera (detekcja vBot)
> Celem jest wiarygodne wykrycie "kodu vBot" i jego relacji, bez uruchamiania Lua.

- **SygnaL'y makr:** obecnoLc wywoL'aL" `macro(`, wzorce "scheduler/macro loop" (identyfikatory `macro`, `scheduleEvent`, `addEvent` z typowa semantyka okresowa).
- **SygnaL'y triggeraow:** funkcje o nazwach `onX...` (np. `onTextMessage`) podpinane do znanych sygnaL'ow moduL'ow (np. *text message module*, *map events*).
- **SL'owa kluczowe domeny:** `say(`, `use(`, `useWith(`, `walkTo(`, `turn(`, `attack(`, identyfikatory zasobow (`ui/a|otui`).
- **Relacje:** `g_ui.loadUI('a|')` a" `lua_to_otui` (do mapowania UI z logika vBot).
- **Klasyfikacja plikow:** prefiks `vb_`, lokalizacja w `modules/game_bot/a|` podnosi wage dopasowania.

**Emisja do `project-index.json`:** wezeL' `symbols.botSymbols`:
{"heal":["modules/game_bot/vb_combat_uh.lua:12"],"antiidle":["modules/game_bot/vb_anti_idle.lua:5"]}
```

---
## 5) ReguL'y jakoLci (lint vBot)
> Rozszerzenie lintu Lua/OTUI o reguL'y domenowe vBot (bez autoa'fixu, chyba LLe bezpieczny).

- **VBOTa'001** - Brak `guard` przed akcja (wymagane `g_game.isOnline()` i brak kolizji z ruchem/walka, jeLli ma znaczenie).
- **VBOTa'002** - Cooldown < zalecanego minimum dla danej akcji (np. < 1000 ms dla czaru) a' WARN.
- **VBOTa'003** - Blokujace petle/sleep w makrze (zamiast tego `scheduleEvent`).
- **VBOTa'004** - Spam `say()`/`use()` bez limitu - brak licznika/okna czasowego.
- **VBOTa'005** - Globalne symbole w pliku vBot (wymagane `local`).
- **VBOTa'006** - Brak logowania kontekstowego przy krytycznych akcjach.
- **VBOTa'007** - Brak anulowania makra po `isDisconnected()`.
- **VBOTa'008** - ZaleLLnoLc od UI bez sprawdzenia istnienia `widget`.

**Konfiguracja (JSON):**
{"VBOT-001":{"enabled":true,"severity":"ERROR"},"VBOT-002":{"enabled":true,"severity":"WARN","minCooldownMs":1000}}
```

---
## 6) Logowanie i telemetria (opcjonalnie NDJSON)
- Format linii (zalecany): `{ts, level, tag, file, line, msg, meta}`.
- Tagi: `[heal]`, `[msg]`, `[buff]`, `[loot]`, `[antiidle]`.
- Logi krytyczne: akcje `say/use` z parametrami i wynikiem.
- Integracja ze Studio: panel Log Viewer filtruje po `tag/level/file:line`.

**PrzykL'ad:**
{"ts":"2025-10-02T12:00:00.000Z","level":"INFO","tag":"heal","file":"modules/game_bot/vb_auto_heal.lua","line":18,"msg":"cast","meta":{"spell":"exura","hp":43}}
```

---
## 7) BezpieczeL"stwo i zgodnoLc
- **Idempotencja:** makra nie powinny powodowac skutkow ubocznych przy powtarzaniu (guard+cooldown).
- **OstroLLnoLc UI:** sprawdzaj istnienie widgetow przed modyfikacja (`if widget then ...`).
- **Zasoby:** nie uLLywaj nieistniejacych LcieLLek; weryfikuj z `assets-map.json`.
- **Granice:** makra nie powinny ingerowac w pliki poza katalogiem projektu.

---
## 8) WydajnoLc
- InterwaL'y: nie schodLs poniLLej 150-250 ms dla ogolnych makr; kosztowne operacje (skany mapy/UI) aA 1000 ms.
- Unikaj peL'nych skanow co tick - cache wynikow, porownuj zmiany.
- ULLywaj `scheduleEvent` zamiast petli blokujacych; debounce wejLcia.

---
## 9) Generator vBot (szablony do Studio)
**WejLcie:** parametry (JSON/OTML) - np. `threshold`, `spell`, `cooldownMs`.
**WyjLcie:** plik `vb_<nazwa>.lua` + wpis w module (opcjonalny UI konfiguracyjny).
**Checklista generacji:**
- [ ] Plik w `modules/game_bot/a|`.
- [ ] Nazwy `local`, brak globali.
- [ ] Guards i cooldown zaimplementowane.
- [ ] Logi z prefiksem `[vBot]` i tagiem.
- [ ] Komentarz nagL'owkowy (opis, parametry, interwaL').

---
## 10) Testa'wektory (QA vBot)
- **HEALa'01:** HP 55% a' oczekiwany 1A- `say('exura')`, brak spam w 1200 ms.
- **MSGa'01:** Tekst `hi` a' odpowiedLs `hello` tylko 1A- / 3 s na nadawce.
- **HASTEa'01:** Ruch z brakiem buffa a' `say('utani hur')` nie czeLciej niLL co 6 s.
- **LOOTa'01:** Pojawia sie `corpse` na tile a' wywoL'anie `use()` na kontenerze (jeLli dostepne API); brak bL'edow przy braku miejsca.
- **IDLEa'01:** Brak aktywnoLci 60 s a' `turn()`; brak gdy `isAttacking()`.

---
## 11) Integracja ze Studio
- **Skaner:** heurystyki z 4 zasilaja `symbols.botSymbols`.
- **Lint:** reguL'y z 5 uzupeL'niaja lint Lua (domena vBot).
- **Generator:** szablony z 9 dostepne w panelu "Nowy a' vBot".
- **Dokumentacja:** panel "vBot Playbook" linkuje do wzorcow i przykL'adow.

---
## 12) Checklisty wdroLLeniowe
- [ ] KaLLde makro/trigger ma guards i cooldown.
- [ ] Brak globali; `local` wszedzie.
- [ ] Logi akcji krytycznych.
- [ ] Parametry wyniesione do konfiguracji.
- [ ] Testa'wektory przechodza; brak regresji.

---
## 13) Noty koL"cowe
- Wzorce sa rozszerzalne; dodajac nowe, zachowaj nazewnictwo i sekcje: *cel a' konfiguracja a' guards a' cooldown a' logi a' testy*.
- Wszelkie modyfikacje wymagaja aktualizacji generatora i reguL' QA.

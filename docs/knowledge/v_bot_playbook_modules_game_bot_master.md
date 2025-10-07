?# vBot Playbook - **modules/game_bot (MASTER)**

> Cel: pelny, operacyjny przewodnik dla implementacji i utrzymania skrypt�w **vBot** (modul `modules/game_bot`) w ramach **OTClient Studio**. Dokument zawiera: standardy kodowania, wzorce (makra/trigger'y), snippety, heurystyki skanera, wymagania jakosciowe, checklisty, test-wektory i integracje z narzedziem. **Transfer 1:1** - gotowe do wdrozenia.

---
# # 0) Executive Summary
- **Co obejmuje:** makra okresowe, trigger'y eventowe, interakcje z UI/swiatem gry, wzorce bezpieczenstwa, logowanie, diagnostyke i performance.
- **Jak uzywac:** jako *zr�dlo prawdy* dla generator�w w Studio (szablony vBot), lint vBot (reguly domenowe) oraz heurystyk skanera (detekcja symboli vBot w kodzie).

---
# # 1) Slownik i konwencje
- **Makro** - blok wykonywany cyklicznie (interwal ms) lub sterowany warunkiem.
- **Trigger** - blok reagujacy na zdarzenie (np. wiadomosc, zmiana HP, wejscie na tile).
- **Guard** - warunek bezpieczenstwa (np. `isConnected()`, `not isBusy()`), kt�ry musi byc spelniony przed akcja.
- **Cooldown** - minimalny czas miedzy kolejnymi akcjami (zapobiega spamowi).
- **State** - lokalny stan makra (zapamietanie poprzedniej decyzji/targetu).

Konwencje nazewnictwa (zalecane):
- Pliki: `vb_<obszar>_<cel>.lua` np. `vb_combat_uh.lua`.
- Funkcje lokalne: `vb_<obszar>_<akcja>()` np. `vb_heal_cast()`.
- Zmienne stanu: `state_<nazwa>`.
- Logi: prefiks `"[vBot]"` i tagi (`[heal]`, `[loot]`).

---
# # 2) Architektura vBot (w ujeciu skryptowym)
- **Warstwa zdarzen gry** ? callbacki (np. text message, damage, map change).
- **Warstwa makr** ? petle interwalowe i warunki.
- **Warstwa akcji** ? uzycia czar�w/przedmiot�w, ruch, interakcja z UI.
- **Warstwa narzedzi** ? helpers (cooldown, debouncing, retry), logowanie NDJSON (opcjonalnie).

Kazdy komponent powinien byc **izolowany** (funkcje `local`, brak globali), testowalny oraz posiadac jasne **guards**.

---
# # 3) Wzorce (makra i trigger'y)
> Ponizsze wzorce to gotowe schematy do generatora w Studio. Kazdy zawiera: cel, pre-warunki, interfejs konfiguracyjny, guards, cooldown, logowanie oraz sekcje bezpieczenstwa.
# # # 3.1 Makro: Auto-Heal na progu HP
**Cel:** rzucenie czaru/ uzycie pota, gdy HP < progu.

**Konfiguracja (OTML/JSON dla Studio):**
```json
{"name":"vb_auto_heal","threshold":60,"spell":"exura","cooldownMs":1200}
```

**Szkielet (Lua):**
```lua
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

-- rejestracja makra w schedulerze (implementacja zalezna od srodowiska vBot)
-- macro(200, tick) -- jesli srodowisko udostepnia
-- w OTC Studio: dodaj do petli narzedzia lub harmonogramu modulu
```

**Bezpieczenstwo:** sprawdz `g_game.isOnline()`, wstrzymaj w czasie `isWalking()`; cooldown ? GCD klienta, sprawdz mane przed `say()`.
# # # 3.2 Trigger: Reakcja na wiadomosc tekstowa
**Cel:** wykrycie frazy i akcja (np. odpowiedz, log, zapis zdarzenia).

**Konfiguracja:**
```json
{"name":"vb_msg_react","match":"^hi$","reply":"hello"}
```

**Szkielet (Lua):**
```lua
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

-- rejestracja: attach do zdarzenia tekstowego w srodowisku vBot/OTClient
-- modules.game_textmessage.onTextMessage:connect(onTextMessage) -- przyklad; dostosuj do dostepnych hook�w
```

**Bezpieczenstwo:** sanitacja regex (escape), limit odpowiedzi (cooldown per nadawca), nie odpowiadaj na wlasne linie.
# # # 3.3 Makro: Auto-Haste (buff w ruchu)
**Cel:** utrzymywanie buffa szybkosci przy poruszaniu sie.

**Konfiguracja:**
```json
{"name":"vb_auto_haste","spell":"utani hur","cooldownMs":6000}
```

**Szkielet:**
```lua
local SPELL = 'utani hur'
local COOLDOWN = 6000
local last = 0

local function hasHaste()
  -- sprawdz ikony buff�w na UI lub stan gracza (jesli dostepny)
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

**Bezpieczenstwo:** nie spamuj - sprawdz buff i cooldown; upewnij sie, ze gracz ma mane.
# # # 3.4 Trigger: Loot po ubiciu potwora
**Cel:** podniesienie lupu po wykryciu ciala.

**Szkielet (zarys):**
```lua
local function onTileAddThing(tile, thing)
  if not g_game.isOnline() then return end
  if thing:isContainer() and thing:isCorpse() then
    -- logika lootu; otwarcie kontenera, iteracja zawartosci, use()
  end
end

-- rejestracja na event mapy/tili (zalezna od dostepnych hook�w srodowiska)
```

**Bezpieczenstwo:** limit r�wnoleglych otwarc; przerwij, gdy inventory pelne; nie blokuj gl�wnej petli.
# # # 3.5 Makro: Anti-Idle
**Cel:** zapobiec disconnectowi przez delikatna interakcje.

**Szkielet:**
```lua
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

**Bezpieczenstwo:** nie wykonuj w trakcie walki; nie przeszkadzaj w recznych akcjach.

---
# # 4) Heurystyki skanera (detekcja vBot)
> Celem jest wiarygodne wykrycie "kodu vBot" i jego relacji, bez uruchamiania Lua.

- **Sygnaly makr:** obecnosc wywolan `macro(`, wzorce "scheduler/macro loop" (identyfikatory `macro`, `scheduleEvent`, `addEvent` z typowa semantyka okresowa).
- **Sygnaly trigger'�w:** funkcje o nazwach `onX...` (np. `onTextMessage`) podpinane do znanych sygnal�w modul�w (np. *text message module*, *map events*).
- **Slowa kluczowe domeny:** `say(`, `use(`, `useWith(`, `walkTo(`, `turn(`, `attack(`, identyfikatory zasob�w (`ui/.otui`).
- **Relacje:** `g_ui.loadUI('.')` ? `lua_to_otui` (do mapowania UI z logika vBot).
- **Klasyfikacja plik�w:** prefiks `vb_`, lokalizacja w `modules/game_bot/.` podnosi wage dopasowania.

**Emisja do `project-index.json`:** wezel `symbols.botSymbols`:
```json
{"heal":["modules/game_bot/vb_combat_uh.lua:12"],"antiidle":["modules/game_bot/vb_anti_idle.lua:5"]}
```

---
# # 5) Reguly jakosci (lint vBot)
> Rozszerzenie lintu Lua/OTUI o reguly domenowe vBot (bez auto-fixu, chyba ze bezpieczny).

- **VBOT-001** - Brak `guard` przed akcja (wymagane `g_game.isOnline()` i brak kolizji z ruchem/walka, jesli ma znaczenie).
- **VBOT-002** - Cooldown < zalecanego minimum dla danej akcji (np. < 1000 ms dla czaru) ? WARN.
- **VBOT-003** - Blokujace petle/sleep w makrze (zamiast tego `scheduleEvent`).
- **VBOT-004** - Spam `say()`/`use()` bez limitu - brak licznika/okna czasowego.
- **VBOT-005** - Globalne symbole w pliku vBot (wymagane `local`).
- **VBOT-006** - Brak logowania kontekstowego przy krytycznych akcjach.
- **VBOT-007** - Brak anulowania makra po `isDisconnected()`.
- **VBOT-008** - Zaleznosc od UI bez sprawdzenia istnienia `widget`.

**Konfiguracja (JSON):**
```json
{"VBOT-001":{"enabled":true,"severity":"ERROR"},"VBOT-002":{"enabled":true,"severity":"WARN","minCooldownMs":1000}}
```

---
# # 6) Logowanie i telemetria (opcjonalnie NDJSON)
- Format linii (zalecany): `{ts, level, tag, file, line, msg, meta}`.
- Tagi: `[heal]`, `[msg]`, `[buff]`, `[loot]`, `[antiidle]`.
- Logi krytyczne: akcje `say/use` z parametrami i wynikiem.
- Integracja ze Studio: panel Log Viewer filtruje po `tag/level/file:line`.

**Przyklad:**
```json
{"ts":"2025-10-02T12:00:00.000Z","level":"INFO","tag":"heal","file":"modules/game_bot/vb_auto_heal.lua","line":18,"msg":"cast","meta":{"spell":"exura","hp":43}}
```

---
# # 7) Bezpieczenstwo i zgodnosc
- **Idempotencja:** makra nie powinny powodowac skutk�w ubocznych przy powtarzaniu (guard+cooldown).
- **Ostroznosc UI:** sprawdzaj istnienie widget�w przed modyfikacja (`if widget then ...`).
- **Zasoby:** nie uzywaj nieistniejacych sciezek; weryfikuj z `assets-map.json`.
- **Granice:** makra nie powinny ingerowac w pliki poza katalogiem projektu.

---
# # 8) Wydajnosc
- Interwaly: nie schodz ponizej 150-250 ms dla og�lnych makr; kosztowne operacje (skany mapy/UI) ? 1000 ms.
- Unikaj pelnych skan�w co tick - cache wynik�w, por�wnuj zmiany.
- Uzywaj `scheduleEvent` zamiast petli blokujacych; debounce wejscia.

---
# # 9) Generator vBot (szablony do Studio)
**Wejscie:** parametry (JSON/OTML) - np. `threshold`, `spell`, `cooldownMs`.
**Wyjscie:** plik `vb_<nazwa>.lua` + wpis w module (opcjonalny UI konfiguracyjny).
**Checklista generacji:**
- [ ] Plik w `modules/game_bot/.`.
- [ ] Nazwy `local`, brak globali.
- [ ] Guards i cooldown zaimplementowane.
- [ ] Logi z prefiksem `[vBot]` i tagiem.
- [ ] Komentarz nagl�wkowy (opis, parametry, interwal).

---
# # 10) Test-wektory (QA vBot)
- **HEAL-01:** HP 55% ? oczekiwany 1� `say('exura')`, brak spam w 1200 ms.
- **MSG-01:** Tekst `hi` ? odpowiedz `hello` tylko 1� / 3 s na nadawce.
- **HASTE-01:** Ruch z brakiem buffa ? `say('utani hur')` nie czesciej niz co 6 s.
- **LOOT-01:** Pojawia sie `corpse` na tile ? wywolanie `use()` na kontenerze (jesli dostepne API); brak bled�w przy braku miejsca.
- **IDLE-01:** Brak aktywnosci 60 s ? `turn()`; brak gdy `isAttacking()`.

---
# # 11) Integracja ze Studio
- **Skaner:** heurystyki z �4 zasilaja `symbols.botSymbols`.
- **Lint:** reguly z �5 uzupelniaja lint Lua (domena vBot).
- **Generator:** szablony z �9 dostepne w panelu "Nowy ? vBot".
- **Dokumentacja:** panel "vBot Playbook" linkuje do wzorc�w i przyklad�w.

---
# # 12) Checklisty wdrozeniowe
- [ ] Kazde makro/trigger ma guards i cooldown.
- [ ] Brak globali; `local` wszedzie.
- [ ] Logi akcji krytycznych.
- [ ] Parametry wyniesione do konfiguracji.
- [ ] Test-wektory przechodza; brak regresji.

---
# # 13) Noty koncowe
- Wzorce sa rozszerzalne; dodajac nowe, zachowaj nazewnictwo i sekcje: *cel ? konfiguracja ? guards ? cooldown ? logi ? testy*.
- Wszelkie modyfikacje wymagaja aktualizacji generatora i regul QA.

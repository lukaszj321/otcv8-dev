# ModuL'y (vBot) - przewodnik

!!! info "Cel"

    Jak tworzyc i L'adowac moduL'y Lua dla klienta OTCv8.
## Struktura moduL'u

modules/
my-module/
init.lua
config.lua
README.md

```
## Minimalny moduL'(LUA)

-- modules/my-module/init.lua
local M = {}

function M.start()
  print("my-module start")
end

function M.stop()
  print("my-module stop")
end

return M

```
## Rejestrowanie zdarzeL" (przykL'ad)

onTalk(function(name, level, mode, text)
  if text:find("hello") then print("Hi " .. name) end
end)

```
## Konfiguracja

- `config.lua` - wartoLci domyLlne (np. hotkeye, progi).
- Pliki konfiguracyjne uLLytkownika trzymaj oddzielnie.
## Ddebug / logi

- Pisz do konsoli lub pliku `logs/my-module.log`.
- Dodaj flage `DEBUG=true` i warunkowe logowanie.
## Dobre praktyki

- Nazwy przestrzeni moduL'u (`my_module.*`).
- Brak efektow ubocznych przy `require`.
- Komendy eksportuj jawnie (np. `M.start`, `M.stop`).

# ModuÄąâ€šy (vBot) â€” przewodnik

!!! info "Cel"

    Jak tworzyÄ‡ i Äąâ€šadowaÄ‡ moduÄąâ€šy Lua dla klienta OTCv8.
## Struktura moduÄąâ€šu

`$fenceInfo
modules/
my-module/
init.lua
config.lua
README.md

```
## Minimalny moduÄąâ€š(LUA)

`$fenceInfo
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
## Rejestrowanie zdarzeÄąâ€ž (przykÄąâ€šad)

`$fenceInfo
onTalk(function(name, level, mode, text)
  if text:find("hello") then print("Hi " .. name) end
end)

```
## Konfiguracja

- `config.lua` â€“ wartoÄąâ€şci domyÄąâ€şlne (np. hotkeye, progi).
- Pliki konfiguracyjne uÄąÄ˝ytkownika trzymaj oddzielnie.
## Ddebug / logi

- Pisz do konsoli lub pliku `logs/my-module.log`.
- Dodaj flagÄ™ `DEBUG=true` i warunkowe logowanie.
## Dobre praktyki

- Nazwy przestrzeni moduÄąâ€šu (`my_module.*`).
- Brak efektĂłw ubocznych przy `require`.
- Komendy eksportuj jawnie (np. `M.start`, `M.stop`).


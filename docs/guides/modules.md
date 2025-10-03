# Moduły (vBot) — przewod

n

i

k

!!! info "Cel"

    Jak tworzyć i ładować moduły Lua dla klienta OTCv8.

## Struktura modu

ł

u

```bash
modules/
my-module/
init.lua
config.lua
README.md

```

## Minimalny moduł (Lu

a

)

```lua
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

## Rejestrowanie zdarzeń (przykła

d

)

```lua
onTalk(function(name, level, mode, text)
  if text:find("hello") then print("Hi " .. name) end
end)

```

## Konfigurac

j

a

- `config.lua` – wartości domyślne (np. hotkeye, progi).
- Pliki konfiguracyjne użytkownika trzymaj oddzielnie.

## Debug / lo

g

i

- Pisz do konsoli lub pliku `logs/my-module.log`.
- Dodaj flagę `DEBUG=true` i warunkowe logowanie.

## Dobre prakty

k

i

- Nazwy przestrzeni modułu (`my_module.*`).
- Brak efektów ubocznych przy `require`.
- Komendy eksportuj jawnie (np. `M.start`, `M.stop`).

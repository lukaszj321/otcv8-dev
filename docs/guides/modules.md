?# Moduly (vBot) -

p

r

z

e

w

o

d

n

i

k

!!! info "Cel"

    Jak tworzyc i ladowac moduly Lua dla klienta OTCv8.
# # Strukt

u

r

a

m

o

d

u

l

u

```bash
modules/
my-module/
init.lua
config.lua
README.md

```
# # Minimalny m

o

d

u

l

(

L

u

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
# # Rejestrowanie zdarzen (

p

r

z

y

k

l

a

d

)

```lua
onTalk(function(name, level, mode, text)
  if text:find("hello") then print("Hi " .. name) end
end)

```
# # Kon

f

i

g

u

r

a

c

j

a

- `config.lua` - wartosci domyslne (np. hotkeye, progi).
- Pliki konfiguracyjne uzytkownika trzymaj oddzielnie.
# # D

e

b

u

g

/

l

o

g

i

- Pisz do konsoli lub pliku `logs/my-module.log`.
- Dodaj flage `DEBUG=true` i warunkowe logowanie.
# # Dobr

e

p

r

a

k

t

y

k

i

- Nazwy przestrzeni modulu (`my_module.*`).
- Brak efekt�w ubocznych przy `require`.
- Komendy eksportuj jawnie (np. `M.start`, `M.stop`).

# OTUI — pod

s

t

a

w

y

!!! info

    OTUI to deklaratywne layouty interfejsu użytkownika.

## Przykład lay

o

u

t

u

```otui
Panel
  id: main
  anchor: top left
  size: 400 300

Label
  text: "Status: OK"
  anchors.centerIn: parent

```

## Zdarzenia / wiąz

a

n

i

a

- Właściwości elementów można powiązać z danymi (np. przez Lua).
- Aktualizacje push przez eventy modułów.

## Wskaz

ó

w

k

i

- Trzymaj layouty w `layouts/*`.
- Styluj wspólnymi klasami, nie inline.

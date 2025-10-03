# OTUI — po

d

s

t

a

w

y

!!! info

    OTUI to deklaratywne layouty interfejsu użytkownika.

## Przykład la

y

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

## Zdarzenia / wią

z

a

n

i

a

- Właściwości elementów można powiązać z danymi (np. przez Lua).
- Aktualizacje push przez eventy modułów.

## Wska

z

ó

w

k

i

- Trzymaj layouty w `layouts/*`.
- Styluj wspólnymi klasami, nie inline.

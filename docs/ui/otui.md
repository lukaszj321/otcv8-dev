# OTUI — pods

t

a

w

y

!!! info

    OTUI to deklaratywne layouty interfejsu użytkownika.

## Przykład layo

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

## Zdarzenia / wiąza

n

i

a

- Właściwości elementów można powiązać z danymi (np. przez Lua).
- Aktualizacje push przez eventy modułów.

## Wskazó

w

k

i

- Trzymaj layouty w `layouts/*`.
- Styluj wspólnymi klasami, nie inline.

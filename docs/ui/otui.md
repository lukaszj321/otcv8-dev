# OTUI — podsta

w

y

!!! info

    OTUI to deklaratywne layouty interfejsu użytkownika.

## Przykład layout

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

## Zdarzenia / wiązani

a

- Właściwości elementów można powiązać z danymi (np. przez Lua).
- Aktualizacje push przez eventy modułów.

## Wskazówk

i

- Trzymaj layouty w `layouts/*`.
- Styluj wspólnymi klasami, nie inline.

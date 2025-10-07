# OTUI - podstawy

!!! info

    OTUI to deklaratywne layouty interfejsu uLLytkownika.
## PrzykL'ad layoutu

Panel
  id: main
  anchor: top left
  size: 400 300

Label
  text: "Status: OK"
  anchors.centerIn: parent

```
## Zdarzenia / wiazania

- WL'aLciwoLci elementow moLLna powiazac z danymi (np. przez Lua).
- Aktualizacje push przez eventy moduL'ow.
## Wskazowki

- Trzymaj layouty w `layouts/*`.
- Styluj wspolnymi klasami, nie inline.

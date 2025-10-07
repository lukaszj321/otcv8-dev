# OTUI - podstawy

!!! info

    OTUI to deklaratywne layouty interfejsu uÄąÄ˝ytkownika.
## PrzykÄąâ€šad layoutu

`$fenceInfo
Panel
  id: main
  anchor: top left
  size: 400 300

Label
  text: "Status: OK"
  anchors.centerIn: parent

```
## Zdarzenia / wiÄ…zania

- WÄąâ€šaÄąâ€şciwoÄąâ€şci elementĂłw moÄąÄ˝na powiÄ…zaÄ‡ z danymi (np. przez Lua).
- Aktualizacje push przez eventy moduÄąâ€šĂłw.
## WskazĂłwki

- Trzymaj layouty w `layouts/*`.
- Styluj wspĂłlnymi klasami, nie inline.


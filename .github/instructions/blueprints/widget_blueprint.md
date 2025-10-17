---
title: "OTUI Widget Blueprint"
updated: "2025-10-17T19:53:00Z"
---

# OTUI Widget Blueprint

Szablon do opisu **pojedynczego widgetu** (definicja i instancja).

## Meta

- **widget_id:** `Example/SkillButton`
- **class:** `UIButton`
- **parent:** `MiniWindowContents`
- **source_file:** `modules/example_module/example.otui`

## Definicja klasy

```otui
SkillButton < UIButton
  # GEOMETRIA
  height: 21
  anchors.left: parent.left
  anchors.right: parent.right
  margin-bottom: 2

  # STYL
  font: verdana-11px-monochrome
  text-align: center

  # ZACHOWANIE
  @onClick: onSkillButtonClick
```

## Instancja w layoucie

```otui
SkillButton
  id: skillsToggle
  text: tr('Skills')
```

## CSV mapping (pole → opis)

| Pole              | Typ         | Wymagane | Opis |
|-------------------|-------------|----------|------|
| widget_id         | string      | tak      | Nazwa logiczna komponentu |
| class             | string      | tak      | Klasa bazowa OTUI |
| parent            | string      | nie      | Domyślny rodzic (np. `MiniWindowContents`) |
| source_file       | string      | tak      | Ścieżka OTUI |
| width             | int/string  | nie      | Szerokość |
| height            | int/string  | nie      | Wysokość |
| anchors           | dict/tuple  | nie      | `left:parent.left;right:parent.right` |
| margins           | dict/tuple  | nie      | `bottom:2` |
| paddings          | dict/tuple  | nie      | `left:2;right:2` |
| font              | string      | nie      | Nazwa fontu |
| text_align        | string      | nie      | `left|center|right` |
| image_source      | string      | nie      | Ścieżka grafiki |
| onClick           | string      | nie      | Nazwa funkcji obsługi kliknięcia |
| onSetup           | string      | nie      | Handler inicjalizacji (`@onSetup`) |
| onDestroy         | string      | nie      | Handler zwolnienia (`@onDestroy`) |
| i18n_required     | bool        | nie      | Czy wymaga `tr()` dla tekstów stałych |
| notes             | string      | nie      | Dodatkowe informacje

---

**Konwencje:** zdarzenia jako `@onX`. Porządek atrybutów: **GEOMETRIA → STYL → ZACHOWANIE**.
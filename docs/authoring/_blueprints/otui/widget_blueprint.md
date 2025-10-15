---
title: "OTUI Widget Blueprint"
updated: "2025-10-14T00:00:00Z"
---

# OTUI Widget Blueprint

Użyj tego szablonu, aby opisać **pojedynczy widget** i jego użycia.

## Meta

- **widget_id:** `GameSkills/SkillButton`
- **class:** `UIButton`
- **parent:** `MiniWindowContents`
- **source_file:** `modules/game_skills/skills.otui`

## Definicja (fragment)

```otui
SkillButton < UIButton
  height: 21
  margin-bottom: 2
  &onClick: onSkillButtonClick
```

## Tabela właściwości / zdarzeń

| pole           | wartość                         | opis |
| -------------- | ------------------------------- | ---- |
| `class`        | `UIButton`                      | Klasa bazowa widgetu |
| `height`       | `21`                            | Wysokość |
| `margin-bottom`| `2`                             | Odstęp |
| `&onClick`     | `onSkillButtonClick`            | Handler kliknięcia |

## Powiązania assetów

- `image-source`: `/images/ui/tabbutton_square`
- `font`: `verdana-11px-monochrome`

## Linki

- Facet assets: [`11_data.ui_asset_usage`](../../11_data/index.md#facet-11_data.ui_asset_usage)

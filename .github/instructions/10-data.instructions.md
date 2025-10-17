---
name: "data"
applyTo:
  - "data/**/*"
read:
  - "data/**"
  - "modules/**"
  - "layouts/**"
  - "src/**"
write:
  - "docs/authoring/11_data/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
outputs:
  - "docs/authoring/11_data/index.md"
  - "docs/authoring/11_data/datasets/data_assets.csv"
  - "docs/authoring/11_data/datasets/data_assets.ndjson"
---

# Data — Instructions

## Goal
Zbuduj inwentarz zasobów z `data/**` (obrazy, fonty, dźwięki, style, configi) oraz ich powiązania z OTUI/layoutami.

## Output
- `docs/authoring/11_data/index.md` (intro + TOC)
- `docs/authoring/11_data/datasets/data_assets.csv` **lub** `data_assets.ndjson`
  - kolumny CSV:
    - `path` (string)
    - `type` (image|font|audio|style|config|other)
    - `used_by_layouts` (JSON array, np. `["layouts/main.layout"]`)
    - `used_by_otui` (JSON array)
    - `used_by_modules` (JSON array)
    - `tags` (JSON array)
    - `notes` (string)

## Diagrams (opcjonalnie)
- `docs/authoring/11_data/diagrams/assets_links.mmd` — graf powiązań zasób ↔ UI/Layouts  
  (pierwsza linia: `%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%`)

## Notes
- Rozpoznawaj typ po rozszerzeniu/folderze; przy braku metadanych użyj heurystyk:
  - grep po nazwach w `.otui`, `layouts/**`, `*.lua`.
- Serializuj listy w CSV jako **poprawny JSON** (`[]`), bez spacji na końcu.
- Ścieżki zapisuj względnie względem repo (bez prefiksu `./`).

## Acceptance
- [ ] Wygenerowano `index.md`.
- [ ] Istnieje `data_assets.csv` **lub** `data_assets.ndjson`.
- [ ] Kolumny/klucze zgodne ze specyfikacją; listy jako JSON arrays.
- [ ] (Jeśli diagram) Mermaid renderuje się poprawnie.

## IPC

**Kanały IPC (Studio/Electron)**

- `studio:data.inventory.run` — skanuje `data/**` + `layouts/**` i generuje CSV: images/fonts/styles/locales/sounds/shaders/ui_asset_usage.
- `studio:data.aggregate` — tworzy `stats.json` + `stats.md` na podstawie CSV.
- `studio:data.open` `{ which }` — otwiera wybrany dataset (`images|fonts|styles|locales|sounds|shaders|ui`).

## Sanity

Sanity / acceptance:

- [ ] CSV mają stałe nagłówki (`images.csv`, `fonts.csv`, `styles.csv`, `locales.csv`, `sounds.csv`, `shaders.csv`, `ui_asset_usage.csv`).
- [ ] Puste wartości zapisywane jako `""`; brak kolumn nieudokumentowanych.
- [ ] `ui_asset_usage.csv.resolved_path` wskazuje istniejący plik (po uwzględnieniu `layouts/<active>`).
- [ ] `stats.json` i `stats.md` deterministyczne przy powtórnym uruchomieniu.

## Przykłady

**Przykład `ui_asset_usage.csv` (wycinek)**

```csv
ui_id,ui_file,widget_path,prop,value,asset_path,resolved_path,notes
inventoryWindow,modules/game_inventory/inventory.otui,MiniWindow/icon,icon,/images/topbuttons/inventory,data/images/topbuttons/inventory.png,data/images/topbuttons/inventory.png,""
```

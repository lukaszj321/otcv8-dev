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

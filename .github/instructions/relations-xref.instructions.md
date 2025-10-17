---
name: relations-xref
applyTo: "docs/authoring/**/*"
read:
  - "docs/authoring/**"
write:
  - "docs/authoring/relations/**"
  - "docs/authoring/_data/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# Relations/XRef — Instructions

## Cel
Zbudować **graf powiązań** między rozdziałami i artefaktami: moduły ↔ OTUI ↔ assets ↔ layouty ↔ platformy (Android/VC16). Dane wyjściowe mają zasilać raporty Analytics i podglądy w Studio.

## Wyjścia
- `relations/relations.csv`
  - headers: `["from_id","to_id","rel_type","src_path","line","notes"]`
- `relations/matrix.md` — macierz element×target
- `relations/overview.mmd` — graf Mermaid (opcjonalnie)
- `relations/errors.md` — kolizje/duplikaty

**Rel types (dozwolone):**
- `calls` (funkcja/metoda)
- `handles` (hook/event)
- `emits` (event)
- `owns` (posiada/definiuje)
- `renders` (renderuje używając)
- `uses` (zależność ogólna)
- `overrides` (layout → data)
- `links` (odsyłacz/anchor)
- `loads` (ładowanie modułu/skryptu)
- `depends` (twarda zależność)

---

## Źródła (parsery)
1. **OTMOD** (`12_otmod/datasets/*.csv`)
   - `modules_index.csv` → `module` → `scripts`, `dependencies`
     - `depends` krawędzie: `module -> module`
   - `module_scripts.csv` → `exports`, `requires`
     - `calls/uses` krawędzie: `module/script -> module.symbol | require('…')`
   - `module_ui_links.csv`
     - `renders` krawędzie: `module -> otui_file`

2. **DATA/UI** (`11_data/datasets/*.csv`)
   - `ui_asset_usage.csv` → `ui_file, widget_path, prop, asset_path`
     - `uses` krawędzie: `otui_file -> asset_path`
   - `styles.csv` → `selector, property, resolved_asset`
     - `uses` krawędzie: `style(selector) -> asset`
   - `images/fonts/sounds/shaders.csv`
     - `owns` krawędzie: `chapter:data -> asset`

3. **LAYOUTS** (`13_layouts/datasets/*.csv`)
   - `layout_overrides.csv` → `original_path` vs `path`
     - `overrides` krawędzie: `layouts/<name>/… -> data/…`
   - `sprite_grid_report.csv` (informacyjne, może trafić do `notes`)

4. **ANDROID** (`14_android/datasets/*.csv`)
   - `jni_signatures.csv` → `java_class.method ↔ cpp_symbol`
     - `links/calls` krawędzie: `java -> cpp` oraz `cpp -> java` (jeśli reverse callbacks)
   - `abi_matrix.csv` → `so presence/load_ok` (informacyjne)
   - `android_assets.csv` → (kontekst; `uses` jeśli wskazuje na `assets/`)

5. **VC16** (`15_vc16`) (jeśli obecne CSV)
   - `angle_libs.csv`/`angle_headers.csv` → `uses` krawędzie (aplikacja → ANGLE)

---

## Normalizacja ID
- `module:<name>` — moduły (np. `module:game_skills`)
- `otui:<path>` — pliki OTUI (np. `otui:modules/game_skills/skills.otui`)
- `asset:<path>` — zasoby (np. `asset:data/images/ui/button.png`)
- `layout:<name>:<path>` — override (np. `layout:retro:images/ui/button.png`)
- `java:<class>.<method>` — JNI Java (np. `java:com.otclientv8.Bridge.nativeInit`)
- `cpp:<symbol>` — JNI C++ (np. `cpp:Java_com_otclientv8_Bridge_nativeInit`)

**Zasada:** ID bez spacji, z prefixem typu.

---

## Reguły budowy grafu
1. **Dedup**: scal identyczne krawędzie (zsumuj/połącz `notes`).
2. **Kierunek**:
   - `module -> otui` (`renders`)
   - `otui -> asset` (`uses`)
   - `layout:<name>:… -> asset:data/…` (`overrides`)
   - `java -> cpp` (`calls`), odwrotnie dla callbacków
3. **Walidacja**:
   - `from_id` i `to_id` niepuste
   - `rel_type ∈ {dozwolone}`
   - `src_path` istnieje w repo (lub jest ścieżką datasetu)
4. **Idempotencja**: kolejne przebiegi generują identyczny output dla tych samych wejść.

---

## IPC (Studio)
- `studio:xref.build` → generuje `relations/*.csv|md|mmd`
- `studio:xref.open` `{ file }` → podgląd relacji
- `studio:xref.find` `{ id }` → filtruje/eksportuje ego-network elementu
- `studio:xref.validate` → walidacja rel_types i ID

---

## Przykłady krawędzi (CSV)

```csv
from_id,to_id,rel_type,src_path,line,notes
module:game_skills,otui:modules/game_skills/skills.otui,renders,docs/authoring/12_otmod/datasets/module_ui_links.csv,,widgets=12
otui:modules/game_skills/skills.otui,asset:data/images/ui/skill_button.png,uses,docs/authoring/11_data/datasets/ui_asset_usage.csv,,image-source
layout:retro:images/ui/tabbutton_square.png,asset:data/images/ui/tabbutton_square.png,overrides,docs/authoring/13_layouts/datasets/layout_overrides.csv,,clips_changed=false
java:com.otclientv8.Bridge.nativeInit,cpp:Java_com_otclientv8_Bridge_nativeInit,calls,docs/authoring/14_android/datasets/jni_signatures.csv,,sig_ok
module:game_skills,module:game_interface,depends,docs/authoring/12_otmod/datasets/module_deps.csv,,type=hard
```

---

## Macierz (matrix.md) — format

* Wiersze: `from_id`
* Kolumny: `to_id`
* Komórka: skrót relacji (`u`=uses, `r`=renders, `o`=overrides, `c`=calls, `d`=depends, `h`=handles, `e`=emits, `l`=links)

---

## DoD

* [ ] `relations.csv` istnieje i przechodzi walidację (schema, rel_types)
* [ ] `matrix.md` wygenerowana dla ≥ 1 rozdziału z relacjami
* [ ] Brak duplikatów (dedup OK), stabilne ID
* [ ] (Opcja) `overview.mmd` renderuje się poprawnie

---

---
name: qa-analytics
applyTo: "docs/authoring/**/*"
read:
  - "docs/authoring/**"
write:
  - "docs/authoring/qa/**"
  - "docs/authoring/analytics/**"
  - "docs/authoring/_data/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"

purpose: Validate structure, schemas, anchors, Sphinx render, and chapter-specific sanity.

checks:
  structure:
    - docs/authoring/<chapter>/datasets/*.csv exist
    - docs/authoring/<chapter>/diagrams/*.mmd exist (>=1 recommended)
    - docs/authoring/<chapter>/index.md exists
  csv_headers:
    - summary.csv: ["metric","value","note"]
    - entities.csv (if present): ["id","name","type","notes"]
  mermaid:
    - First line has %%{init: ...}%%
    - If CSV with same stem exists → ensure click anchor
  facets:
    - Anchor exists: (facet-<chapter>.<stem>) in index.md
    - Mermaid click points to ./index.html#facet-<chapter>.<stem>
  sphinx:
    - Build succeeds with PyData theme (no blocking warnings)
    - At least one {csv-table} and one {mermaid} per chapter
---

# Rozszerzenia per rozdział (krit.)
chapter_specific:
  11_data:
    - Must exist datasets: images.csv, fonts.csv, styles.csv, locales.csv, sounds.csv, shaders.csv, ui_asset_usage.csv
    - stats.json & stats.md present, deterministic
  12_otmod:
    - Must exist datasets: modules_index.csv, module_scripts.csv, module_deps.csv, module_hooks.csv, module_ui_links.csv
    - lifecycle.mmd & deps.mmd present with facets
  13_layouts:
    - Must exist datasets: layout_overrides.csv, sprite_grid_report.csv, style_states_map.csv
    - resolve_flow.mmd present; grid report statuses only in {OK,WARN,FAIL}
  14_android:
    - Must exist datasets: android_libs.csv, android_assets.csv, abi_matrix.csv, jni_signatures.csv, fps_report.csv
    - pipeline.mmd & jni_flow.mmd present with facets
  15_vc16:
    - angle headers/libs csv present if declared; egl smoke sample present in index

severity:
  - FAIL: łamie kontrakt (brak datasetu, błędny nagłówek, brak facetów)
  - WARN: rekomendacja (brak click-link, brak preview, brak optional)
  - INFO: kontekst (długi render, ostrzeżenia Sphinx nieblokujące)

report:
  - Save QA report to docs/authoring/_data/qa_report.csv
  - headers: ["chapter","check","status","details"]
  - Summaries:
    - docs/authoring/qa/qa_summary.md
    - docs/authoring/analytics/overview.mmd

acceptance:
  - [ ] qa_report.csv exists; any FAILs clearly listed
  - [ ] qa_summary.md has section per chapter with totals
  - [ ] All required datasets present and valid

# QA + Analytics — Instructions

## QA outputs
- `qa/frontmatter_issues.csv`
- `qa/link_lint.csv`
- `qa/chunking_report.csv`
- `qa/dataset_sanity.csv`
- `qa/diagram_lint.csv`
- `qa/idempotency.md`
- `qa/qa_summary.md`

## Analytics outputs
- `analytics/coverage.csv`
- `analytics/gaps.csv`
- `analytics/xref_stats.csv`
- `analytics/coverage_matrix.md`
- `analytics/overview.mmd`
- `analytics/run_summary.json`
- `analytics/errors.md`

---

## Sanity reguły CSV (dodatkowe)
- **Brak pustych kolumn** (poza `note/notes`).
- **Stałe nagłówki** — zgodne z rozdziałami.
- **Ścieżki względne** wobec katalogu rozdziału; separator `/`, bez spacji.
- **Idempotencja** — drugi przebieg generatorów nie zmienia plików (poza dopisaniem nowych, jeżeli tak zaprojektowano).

## IPC (Studio)
- `studio:qa.run` → uruchamia pełny zestaw QA (structure/csv/mermaid/facets/sphinx/chapter_specific)
- `studio:qa.lint.links` → link-lint + facet check
- `studio:qa.lint.csv` → nagłówki i sanity datasetów
- `studio:analytics.run` → pokrycie, xref, matrix, gaps
- `studio:open.qa` `{ file }` → otwiera raport w Studio

**Wyniki IPC** trafiają do:
- `_data/qa_report.csv`, `qa/*.md`, `analytics/*.md|json|mmd`

---

## Przykład matrycy per rozdział (fragment)
| chapter     | check                        | status | details                             |
|-------------|-------------------------------|--------|-------------------------------------|
| 13_layouts  | sprite_grid_report statuses   | OK     | {OK,WARN,FAIL} only                 |
| 14_android  | jni_signatures schema         | FAIL   | missing col `java_sig`              |
| 12_otmod    | lifecycle.mmd facet           | WARN   | missing click to module_deps facet  |

---

## DoD (klikana)
- [ ] `_data/qa_report.csv` powstał i nie ma **FAIL** na krytycznych checkach
- [ ] `qa_summary.md` zawiera sekcje dla 11/12/13/14/15
- [ ] Diagramy mają `{init}` i facet anchors
- [ ] Wszystkie wymagane datasety obecne i zgodne ze schematami

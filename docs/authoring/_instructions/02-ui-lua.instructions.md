---
title: "02 — UI (OTUI) & Lua API (Authoring Plan)"
purpose: "Extract UI widget hierarchy, signals, and Lua-facing APIs. Generate datasets + diagrams + Sphinx chapter."
scope:
  - "docs/authoring/04_ui/**"
  - "docs/authoring/03_modules/**"
owner: "authoring-agent"

constraints:
  - "GH Actions only, no new workflows"
  - "Output strictly under docs/authoring/**"

paths:
  ui_chapter: "docs/authoring/04_ui"
  ui_datasets: "docs/authoring/04_ui/datasets"
  ui_diagrams: "docs/authoring/04_ui/diagrams"
  ui_index: "docs/authoring/04_ui/index.md"
  lua_chapter: "docs/authoring/03_modules"
  lua_datasets: "docs/authoring/03_modules/datasets"
  lua_diagrams: "docs/authoring/03_modules/diagrams"
  lua_index: "docs/authoring/03_modules/index.md"

outputs:
  - "docs/authoring/04_ui/datasets/ui_widgets.csv"
  - "docs/authoring/04_ui/datasets/ui_signals.csv"
  - "docs/authoring/03_modules/datasets/lua_exports.csv"
  - "docs/authoring/04_ui/diagrams/widgets_hierarchy.mmd"
  - "docs/authoring/04_ui/diagrams/signals_matrix.mmd"
  - "docs/authoring/04_ui/index.md"
  - "docs/authoring/03_modules/index.md"

facets:
  - "04_ui.widgets_hierarchy"
  - "04_ui.signals_matrix"
  - "03_modules.lua_exports"

datasets:
  - file: "ui_widgets.csv"
    path: "docs/authoring/04_ui/datasets/ui_widgets.csv"
    header: ["id","widget","parent","inherits","otui_file","properties_count","signals_count","notes"]
  - file: "ui_signals.csv"
    path: "docs/authoring/04_ui/datasets/ui_signals.csv"
    header: ["widget","signal","args","emitted_by","handled_by","notes"]
  - file: "lua_exports.csv"
    path: "docs/authoring/03_modules/datasets/lua_exports.csv"
    header: ["module","function","params","returns","raises","availability","notes"]

diagrams:
  style:
    mermaid_init: "%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%"
    first_line_required: true
    click_rule:
      - 'click WidgetsHierarchy "./index.html#facet-04_ui.widgets_hierarchy" "Open widgets"'
      - 'click SignalsMatrix "./index.html#facet-04_ui.signals_matrix" "Open signals"'
  files:
    - file: "widgets_hierarchy.mmd"
      desc: "Tree of UI widgets (types & inheritance)"
      node_id: "WidgetsHierarchy"
    - file: "signals_matrix.mmd"
      desc: "Key signals and their emitters/handlers"
      node_id: "SignalsMatrix"

index_requirements:
  - "Embed both CSVs and both diagrams"
  - "Crosslink to Modules chapter (Lua exports) and Events"
  - "Add anchors in index.md: facet-04_ui.widgets_hierarchy, facet-04_ui.signals_matrix"
  - 'CSV arrays serialized as JSON (["a","b"])'

acceptance:
  - "[ ] Headers exactly as specified"
  - "[ ] Click anchors present in Mermaid"
  - "[ ] index.md contains toctree/contents + csv-table + mermaid + facets"
---

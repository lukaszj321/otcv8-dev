---
title: 01 — Core C++ API (Authoring Plan)
purpose: Generate high-quality developer docs for core C++ (OTClient v8) with datasets + diagrams + Sphinx pages.
scope: docs/authoring/01_core/**
owner: authoring-agent

constraints:
  - Run only in GitHub Actions (no local/manual runs required)
  - Do NOT create new workflows; use existing ones
  - All outputs must live under docs/authoring/** (not reposzablony)

outputs:
  - datasets/*.csv
  - diagrams/*.mmd
  - index.md

facets:
  - Facet ID = "<chapter>.<stem>", e.g., "01_core.headers_map"
  - Each CSV/diagram/section with the same stem MUST refer to the same facet

paths:
  chapter_root: docs/authoring/01_core
  datasets: docs/authoring/01_core/datasets
  diagrams: docs/authoring/01_core/diagrams
  index: docs/authoring/01_core/index.md

references:
  - Use headers and src files from this repo (no external net)
  - Prefer existing extractors/scripts if available (e.g. scripts/gen_api_cpp.sh, scripts/extract-api.mjs)

# 1) Datasets to produce
datasets:
  - file: summary.csv
    desc: Aggregate counters and coverage for Core C++ API
    header: ["metric","value","note"]
    rows:
      - ["headers_total","<int>","count of .h/.hpp in src/core"]
      - ["classes_total","<int>","unique public classes found"]
      - ["functions_total","<int>","unique exported functions"]
      - ["namespaces_total","<int>","unique namespaces"]
  - file: headers.csv
    desc: List of header files and basic stats
    header: ["id","path","include_guard","lines","exports_count"]
  - file: classes.csv
    desc: Public classes (primary types)
    header: ["id","name","namespace","header","methods_public","signals","notes"]
  - file: functions.csv
    desc: Free/exported functions
    header: ["id","name","namespace","return","params","header","deprecated","notes"]
  - file: macros.csv
    desc: Common macros detected
    header: ["name","header","value","notes"]
  - file: compile_flags.csv
    desc: Build flags detected/used for docs (optional)
    header: ["flag","value","source","notes"]

# 2) Diagrams to produce
# NOTE: `click` works in flowchart/graph only (NOT in sequenceDiagram)
diagrams:
  style:
    # Wstrzykuj jako 1. linia w każdym bloku Mermaid (bez cytowania w samym bloku)
    mermaid_init: "%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%"
    node_ids: "CamelCase(stem)"   # must match node IDs in .mmd
    click_rule: "click <NodeId> \"./index.html#facet-01_core.<stem>\" \"Open <stem>\""
    first_line_required: true
  files:
    - file: architecture.mmd
      desc: High-level core component map
      must_click_anchor: "01_core.architecture"
    - file: include_graph.mmd
      desc: Simplified include graph for top-level headers
      must_click_anchor: "01_core.include_graph"

# 3) Chapter index.md
index:
  must_have:
    - "Contents block (MyST: ```{contents} :local:```)"
    - "Hidden toctree (optional children)"
    - "\"Datasets\" section with at least one {csv-table}"
    - "\"Diagrams\" section with at least one ```{mermaid}```"
    - "\"Appendix / Facets\" anchors (for all stems)"
  snippet:
    markdown: |
      ---
      title: 01 — Core
      ---
  # 01 — Core

      ```{toctree}
      :hidden:
      :maxdepth: 2
      ```

      :depth: 2
      :local:

  ## Datasets
      :file: ./datasets/summary.csv
      :header-rows: 1
      :widths: auto

  ## Diagrams
      %%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
      graph TD
        Core[Core] --> Subsystems[Subsystems]
      click Core "./index.html#facet-01_core.architecture" "Open architecture"

  ## Appendix / Facets
      <span id="facet-01_core.architecture"></span>
      <span id="facet-01_core.include_graph"></span>

# 4) Acceptance checklist (DoD)
acceptance:
  - [ ] All CSV exist with the exact headers above
  - [ ] All .mmd start with mermaid_init line as line 1 (in-block, unquoted)
  - [ ] At least 1 Mermaid flowchart with valid `click` anchors
  - [ ] index.md renders CSV + Mermaid + Facets
  - [ ] Sphinx build passes under `-W` (no blocking warnings)
  - [ ] Linkcheck/nitpicky passes for internal anchors

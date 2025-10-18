# Authoring Artifacts

This directory contains generated artifacts from documentation authoring tasks.

## Batch 2 Artifact

**File:** `authoring_batch2.zip` (118 KB)
**Generated:** 2025-10-18T05:04:00Z
**Tasks:** 6-10 (01_runtime, 02_events, 06_assets, 07_settings_crypto, 10_game_runtime)

### Contents

- 5 enhanced index.md files
- 15 dataset CSV files (14 new + 1 enhanced)
- 10 Mermaid diagram files
- 4 QA report files
- 4 analytics report files

### Regeneration

To regenerate this artifact:

```bash
cd docs/authoring
zip -r artifacts/authoring_batch2.zip \
  01_runtime/datasets/*.csv \
  01_runtime/diagrams/*.mmd \
  01_runtime/index.md \
  02_events/datasets/*.csv \
  02_events/diagrams/*.mmd \
  02_events/index.md \
  06_assets/datasets/*.csv \
  06_assets/diagrams/*.mmd \
  06_assets/index.md \
  07_settings_crypto/datasets/*.csv \
  07_settings_crypto/diagrams/*.mmd \
  07_settings_crypto/index.md \
  10_game_runtime/datasets/*.csv \
  10_game_runtime/diagrams/*.mmd \
  10_game_runtime/index.md \
  qa/diagram_lint.csv \
  qa/link_lint.csv \
  qa/dataset_sanity.csv \
  qa/mermaid_sanity.csv \
  analytics/execution_report.md \
  analytics/coverage.csv \
  analytics/gaps.md \
  analytics/xref_stats.csv
```

## Note

ZIP files are excluded from git by `.gitignore`. The artifact can be regenerated on-demand using the command above or downloaded from CI artifacts if available.

# QA Summary Report

Generated: 2025-10-18T01:39:30.122373Z

## Overall Status

- ✅ PASS: 59 checks
- ⚠️ WARN: 21 checks
- ❌ FAIL: 0 checks
- ℹ️ INFO: 0 checks

## Checks by Type


### Datasets


**WARN (16):**
- 01_core: cpp_symbols.csv: no data rows; lua_bindings.csv: no data rows
- 01_runtime: runtime_stats.csv: no data rows
- 02_events: handlers.csv: no data rows; events_matrix.csv: no data rows
- 03_modules: hot_reload.csv: no data rows; lua_exports.csv: no data rows
- 04_ui: signals.csv: no data rows; needed_translations.csv: no data rows

### Diagrams


### Facets


### Frontmatter


### Links


**WARN (5):**
- 07_settings_crypto: Only 2 crosslinks (min: 3)
- 08_audio: Only 2 crosslinks (min: 3)
- 09_logging: Only 2 crosslinks (min: 3)
- 13_layouts: Only 2 crosslinks (min: 3)
- 15_vc16: Only 2 crosslinks (min: 3)


## Recommendations

1. Address all FAIL status checks immediately
2. Review WARN status checks and improve where possible
3. Ensure all chapters have:
   - Proper frontmatter with required fields
   - At least 3 datasets with valid schemas
   - Mermaid diagrams with init headers
   - At least 3 crosslinks to related chapters
   - Facet anchors for key sections

## Next Steps

- Run link-lint to verify all relative links
- Validate CSV schemas for compliance
- Check diagram rendering
- Verify facet anchor targets exist

# Authoring Documentation

This directory contains auto-generated documentation artifacts for all major components of OTClientV8.

## What's Inside

### Structure

```
authoring/
├── index.md                    # Main authoring index with grid navigation
├── 01_core/                    # Core API documentation
├── 01_runtime/                 # Runtime monitoring
├── 02_events/                  # Event system
├── 03_modules/                 # Lua modules
├── 04_ui/                      # UI components
├── 05_events/                  # Event details
├── 05_network/                 # Network protocol
├── 06_assets/                  # Asset management
├── 07_settings_crypto/         # Settings & cryptography
├── 08_audio/                   # Audio system
├── 09_logging/                 # Logging system
└── 10_game_runtime/            # Game runtime state
```

### Each Chapter Contains

1. **Summary Table** - Basic statistics and metrics
2. **Entities Table** - Key entities and their counts
3. **Architecture Diagram** - Component relationships (Mermaid)
4. **Data Flow Diagram** - Processing pipeline (Mermaid)
5. **Source Links** - Links to raw data files in repository

## Source Data

All data is generated from:
- `docs/reposzablony/<chapter>/datasets/` - Raw CSV files
- `docs/reposzablony/<chapter>/diagrams/` - Mermaid diagram definitions
- `docs/_data/<chapter>/` - Sphinx-optimized CSV files

## How to Update

To regenerate the authoring documentation:

1. Ensure you have Python 3.10+ installed
2. Install dependencies: `pip install -r requirements-docs.txt`
3. Run the generator scripts (if available) or manually update CSV files
4. Rebuild Sphinx: `sphinx-build -b html docs docs/_build/html`

## Features

- **Grid Navigation**: Easy-to-navigate card-based interface
- **CSV Tables**: Embedded tables using MyST csv-table directive
- **Mermaid Diagrams**: Interactive diagrams rendered in browser
- **GitHub Links**: Direct links to source files in repository
- **Responsive Design**: Works on desktop and mobile devices

## Integration

The authoring section is integrated into the main documentation:
- Listed in main navigation menu
- Accessible from homepage
- Part of the toctree structure
- Included in sitemap and search index

## Generation Date

This content was last generated on: 2025-10-13 04:50:32 UTC

## Notes

- All content is auto-generated - manual edits will be overwritten
- To modify content, update the source data files and regenerate
- Diagrams are rendered client-side using Mermaid.js
- CSV files are loaded at build time using Sphinx csv-table directive

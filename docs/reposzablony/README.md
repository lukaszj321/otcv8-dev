# Reposzablony - Source Data Repository

This directory contains the source data and artifacts for OTClientV8 documentation generation.

## Structure

Each chapter folder (01_core, 01_runtime, etc.) contains:

```
<chapter>/
├── index.md                 # Chapter overview and navigation
├── datasets/                # Raw CSV/JSON data files
│   ├── summary.csv         # Basic statistics
│   └── entities.csv        # Entity information
└── diagrams/                # Mermaid diagram definitions
    ├── architecture.mmd    # Architecture diagram
    └── flow.mmd           # Data flow diagram
```

## Chapters

- **01_core** - Core C++ API documentation
- **01_runtime** - Runtime statistics and monitoring
- **02_events** - Event system and signals
- **03_modules** - Lua module exports
- **04_ui** - OTUI widget hierarchy
- **05_events** - Detailed event documentation
- **05_network** - Network protocol
- **06_assets** - Asset management
- **07_settings_crypto** - Settings and cryptography
- **08_audio** - Audio system
- **09_logging** - Logging system
- **10_game_runtime** - Game runtime state

## Usage

These files serve as the source for:

1. **Sphinx Documentation** - Rendered pages in `docs/authoring/`
2. **RAG Systems** - Training data for AI/ML systems
3. **Analysis Tools** - Data for automated analysis
4. **API Documentation** - Reference material for developers

## Generation

The artifacts in this directory were generated using:
- Python scripts in `docs/reposzablony/_tools/`
- Data extraction from source code
- Template-based generation

Last generated: 2025-10-13 04:50:32 UTC

## File Formats

- **CSV**: UTF-8 encoded, comma-separated values with headers
- **Mermaid**: Graph definitions in Mermaid syntax
- **Markdown**: MyST-flavored Markdown with frontmatter

## Guidelines

When adding or modifying content:

1. Use UTF-8 encoding without BOM
2. Use LF line endings (Unix style)
3. Follow existing naming conventions
4. Keep CSV headers consistent
5. Test Mermaid diagrams before committing
6. Update index.md files when adding new files

## Integration

Data from this directory is:
- Copied to `docs/_data/<chapter>/` for Sphinx
- Referenced by `docs/authoring/<chapter>/index.md`
- Used by RAG dataset generators
- Included in CI/CD builds

## Notes

- Some content is auto-generated, some is manually curated
- Check chapter specification files for detailed requirements
- Refer to `.github/instructions/` for generation guidelines

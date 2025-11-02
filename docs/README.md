# Jak używać

1. Skopiuj folder `docs/` i `.github/workflows/docs.yml` do **roota repo**.
2. Zmień ścieżki `literalinclude` w `docs/reference/*.md` na realne pliki w repo.
3. (Opcjonalnie) dodaj zasoby do `data/` — workflow skopiuje je do `docs/_static/data/`.
4. Budowa lokalnie:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r docs/requirements.txt
python docs/scripts/generate_placeholders.py  # Generate placeholders for missing includes
sphinx-build -b html docs docs/_build/html
sphinx-build -b json docs docs/_build/json
```

## Images

Place documentation images in the `docs/images/` directory. This directory is tracked by git (contains `.gitkeep`).

Supported formats:
- PNG (preferred for screenshots)
- SVG (preferred for diagrams)
- JPEG (for photos)
- GIF (for animations)

Example usage in documentation:
```markdown
![Alt text](images/my-diagram.png)
```

## Build System

The documentation build system includes:
- **Tab-item sanitizer**: Automatically fixes malformed tab constructs
- **Lexer fallbacks**: Maps unknown code languages (mermaid, otml, csv, gradle) to safe fallbacks
- **Placeholder generation**: Creates stub files for missing literalinclude references
- **Git history**: Full git history is fetched for git-based extensions

Run `python docs/scripts/generate_placeholders.py` before building to ensure all referenced files exist.

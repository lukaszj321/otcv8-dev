#!/usr/bin/env python3
"""
Pre-build script for Sphinx documentation.
Recursively processes docs/reposzablony/** to:
1. Create index.md files where missing
2. Add {toctree} directives with children
3. Render CSV files inline with {csv-table}
4. Render Mermaid diagrams inline with {literalinclude}
5. Replace stub text with actual MyST blocks
"""

import os
import re
from pathlib import Path
from typing import List, Tuple


def natural_sort_key(s: str) -> List:
    """Natural sorting to handle prefixes like 01_, 02_, etc."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def get_children(directory: Path) -> Tuple[List[Path], List[Path]]:
    """
    Get immediate children of a directory.
    Returns (subdirectories, markdown_files) excluding index.md
    """
    if not directory.is_dir():
        return [], []
    
    subdirs = []
    md_files = []
    
    try:
        for item in directory.iterdir():
            if item.name.startswith('.') or item.name.startswith('_'):
                continue
            if item.is_dir():
                subdirs.append(item)
            elif item.is_file() and item.suffix == '.md' and item.name != 'index.md':
                md_files.append(item)
    except PermissionError:
        pass
    
    # Natural sort both lists
    subdirs.sort(key=lambda p: natural_sort_key(p.name))
    md_files.sort(key=lambda p: natural_sort_key(p.name))
    
    return subdirs, md_files


def find_datasets_and_diagrams(directory: Path) -> Tuple[List[Path], List[Path]]:
    """Find CSV files and .mmd files in the directory or its subdirectories."""
    csv_files = []
    mmd_files = []
    
    # Check if this directory is named 'datasets' or has a 'datasets' subdirectory
    if directory.name == "datasets":
        # We're in a datasets directory, look for CSV files here
        csv_files = sorted([f for f in directory.glob("*.csv")],
                          key=lambda p: natural_sort_key(p.name))
    else:
        # Look for datasets subdirectory
        datasets_dir = directory / "datasets"
        if datasets_dir.is_dir():
            csv_files = sorted([f for f in datasets_dir.glob("*.csv")],
                              key=lambda p: natural_sort_key(p.name))
    
    # Check if this directory is named 'diagrams' or has a 'diagrams' subdirectory
    if directory.name == "diagrams":
        # We're in a diagrams directory, look for .mmd files here
        mmd_files = sorted([f for f in directory.glob("*.mmd")],
                          key=lambda p: natural_sort_key(p.name))
    else:
        # Look for diagrams subdirectory
        diagrams_dir = directory / "diagrams"
        if diagrams_dir.is_dir():
            mmd_files = sorted([f for f in diagrams_dir.glob("*.mmd")],
                              key=lambda p: natural_sort_key(p.name))
    
    return csv_files, mmd_files


def generate_csv_block(csv_file: Path, relative_to: Path) -> str:
    """Generate MyST {csv-table} block for a CSV file."""
    rel_path = os.path.relpath(csv_file, relative_to)
    # Convert to forward slashes for consistency
    rel_path = rel_path.replace('\\', '/')
    
    # Use filename (without .csv) as title
    title = csv_file.stem.replace('_', ' ').title()
    
    return f"""
```{{csv-table}} {title}
:file: {rel_path}
:header-rows: 1
:widths: auto
```
"""


def generate_mermaid_block(mmd_file: Path, relative_to: Path) -> str:
    """Generate Mermaid code block by reading the .mmd file content."""
    # Use filename (without .mmd) as caption
    caption = mmd_file.stem.replace('_', ' ').title()
    
    # Read the mermaid file content
    try:
        with open(mmd_file, 'r', encoding='utf-8') as f:
            mermaid_content = f.read().strip()
    except Exception:
        mermaid_content = "graph TD\n    A[Error loading diagram]"
    
    return f"""
```{{mermaid}}
:caption: {caption}

{mermaid_content}
```
"""


def generate_toctree(subdirs: List[Path], md_files: List[Path]) -> str:
    """Generate {toctree} directive with children."""
    if not subdirs and not md_files:
        return ""
    
    lines = ["\n```{toctree}", ":maxdepth: 2", ":titlesonly:", ""]
    
    # Add subdirectories (reference their index.md)
    for subdir in subdirs:
        lines.append(f"{subdir.name}/index")
    
    # Add sibling markdown files (without .md extension)
    for md_file in md_files:
        lines.append(md_file.stem)
    
    lines.append("```\n")
    return "\n".join(lines)


def should_replace_stub(content: str) -> bool:
    """Check if content has stub text that should be replaced."""
    stub_patterns = [
        r'Location:\s*datasets/',
        r'Location:\s*diagrams/',
        r'Location:\s*`datasets/',
        r'Location:\s*`diagrams/',
    ]
    return any(re.search(pattern, content) for pattern in stub_patterns)


def replace_stubs_with_inline(content: str, directory: Path) -> str:
    """Replace stub references with inline MyST blocks."""
    csv_files, mmd_files = find_datasets_and_diagrams(directory)
    
    # Pattern to match stub sections like "### Summary\nLocation: datasets/summary.csv"
    # We'll be conservative and only replace if the pattern is clear
    
    # Replace dataset stubs
    for csv_file in csv_files:
        stub_pattern = rf'(?:###?\s+.*?\n)?Location:\s*`?datasets/{re.escape(csv_file.name)}`?.*?\n'
        csv_block = generate_csv_block(csv_file, directory)
        content = re.sub(stub_pattern, csv_block, content, flags=re.MULTILINE)
    
    # Replace diagram stubs
    for mmd_file in mmd_files:
        stub_pattern = rf'(?:###?\s+.*?\n)?Location:\s*`?diagrams/{re.escape(mmd_file.name)}`?.*?\n'
        mmd_block = generate_mermaid_block(mmd_file, directory)
        content = re.sub(stub_pattern, mmd_block, content, flags=re.MULTILINE)
    
    return content


def process_index_md(directory: Path, index_path: Path):
    """Process or create index.md for a directory."""
    # Read existing content or create minimal one
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if we should replace stubs
        if should_replace_stub(content):
            content = replace_stubs_with_inline(content, directory)
    else:
        # Create minimal index.md
        title = directory.name.replace('_', ' ').title()
        content = f"# {title}\n\n"
    
    # Get children for toctree
    subdirs, md_files = get_children(directory)
    
    # Check if toctree already exists
    has_toctree = '```{toctree}' in content or '```toctree' in content
    
    if not has_toctree and (subdirs or md_files):
        # Append toctree at the end
        toctree = generate_toctree(subdirs, md_files)
        content = content.rstrip() + "\n\n" + toctree
    
    # Check for datasets and diagrams to add inline if not already present
    csv_files, mmd_files = find_datasets_and_diagrams(directory)
    
    # Add datasets section if CSV files exist and not already included
    if csv_files and not any(csv_file.name in content for csv_file in csv_files):
        datasets_section = "\n## Datasets\n"
        for csv_file in csv_files:
            datasets_section += generate_csv_block(csv_file, directory)
        content = content.rstrip() + "\n\n" + datasets_section
    
    # Add diagrams section if Mermaid files exist and not already included
    if mmd_files and not any(mmd_file.name in content for mmd_file in mmd_files):
        diagrams_section = "\n## Diagrams\n"
        for mmd_file in mmd_files:
            diagrams_section += generate_mermaid_block(mmd_file, directory)
        content = content.rstrip() + "\n\n" + diagrams_section
    
    # Write back only if content changed
    if not index_path.exists() or index_path.read_text(encoding='utf-8') != content:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {index_path.relative_to(Path.cwd())}")


def process_directory_recursive(directory: Path):
    """Recursively process a directory and its subdirectories."""
    if not directory.is_dir():
        return
    
    # Skip special directories
    if directory.name.startswith('.') or directory.name.startswith('_'):
        return
    
    # Process index.md for this directory
    index_path = directory / "index.md"
    process_index_md(directory, index_path)
    
    # Recursively process subdirectories
    subdirs, _ = get_children(directory)
    for subdir in subdirs:
        process_directory_recursive(subdir)


def update_authoring_index(docs_path: Path):
    """Update docs/authoring/index.md to link internally to reposzablony."""
    authoring_index = docs_path / "authoring" / "index.md"
    
    # New content that links to reposzablony
    content = """---
title: Authoring — Chapter Workspace
---

# Authoring (Chapters)

```{admonition} Co to jest?
:class: tip
To „robocza" sekcja dokumentacji budowana z **docs/reposzablony/**. 
Cała zawartość jest renderowana inline — CSV, diagramy Mermaid i nawigacja.
Żadnych linków do GitHuba.
```

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Repository Templates
:link: ../reposzablony/index
:link-type: doc
Główny indeks dokumentacji z docs/reposzablony/
:::

:::{grid-item-card} 01 — Core
:link: ../reposzablony/01_core/index
:link-type: doc
Podstawy klienta, framework, C++ i API.
:::

:::{grid-item-card} 01 — Runtime
:link: ../reposzablony/01_runtime/index
:link-type: doc
Dane i pipeline runtime.
:::

:::{grid-item-card} 02 — Events
:link: ../reposzablony/02_events/index
:link-type: doc
System zdarzeń, strumienie, emitery.
:::

:::{grid-item-card} 03 — Modules
:link: ../reposzablony/03_modules/index
:link-type: doc
Moduły i integracje.
:::

:::{grid-item-card} 04 — UI
:link: ../reposzablony/04_ui/index
:link-type: doc
Interfejs OTUI, widżety, layouty.
:::

:::{grid-item-card} 05 — Events (doc)
:link: ../reposzablony/05_events/index
:link-type: doc
Dokumenty uzupełniające.
:::

:::{grid-item-card} 05 — Network
:link: ../reposzablony/05_network/index
:link-type: doc
Warstwa sieciowa i protokoły.
:::

:::{grid-item-card} 06 — Assets
:link: ../reposzablony/06_assets/index
:link-type: doc
Zasoby, formaty, pipeline.
:::

:::{grid-item-card} 07 — Settings & Crypto
:link: ../reposzablony/07_settings_crypto/index
:link-type: doc
Konfiguracja, bezpieczeństwo, kryptografia.
:::

:::{grid-item-card} 08 — Audio
:link: ../reposzablony/08_audio/index
:link-type: doc
Silnik audio i integracje.
:::

:::{grid-item-card} 09 — Logging
:link: ../reposzablony/09_logging/index
:link-type: doc
Logowanie, metryki, obserwowalność.
:::

:::{grid-item-card} 10 — Game Runtime
:link: ../reposzablony/10_game_runtime/index
:link-type: doc
Pętla gry, stany, tick i zasoby.
:::
:::

## Spis rozdziałów

```{toctree}
:caption: Rozdziały (Repository Templates)
:maxdepth: 2
:titlesonly:

../reposzablony/index
../reposzablony/01_core/index
../reposzablony/01_runtime/index
../reposzablony/02_events/index
../reposzablony/03_modules/index
../reposzablony/04_ui/index
../reposzablony/05_events/index
../reposzablony/05_network/index
../reposzablony/06_assets/index
../reposzablony/07_settings_crypto/index
../reposzablony/08_audio/index
../reposzablony/09_logging/index
../reposzablony/10_game_runtime/index
```
"""
    
    with open(authoring_index, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {authoring_index.relative_to(Path.cwd())}")


def main():
    """Main entry point."""
    # Get the docs directory (script is in scripts/, docs is sibling)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    docs_path = repo_root / "docs"
    reposzablony_path = docs_path / "reposzablony"
    
    if not reposzablony_path.is_dir():
        print(f"Error: {reposzablony_path} does not exist")
        return 1
    
    print(f"Processing {reposzablony_path}...")
    process_directory_recursive(reposzablony_path)
    
    print("\nUpdating authoring/index.md...")
    update_authoring_index(docs_path)
    
    print("\n✓ Build authoring completed successfully")
    return 0


if __name__ == "__main__":
    exit(main())

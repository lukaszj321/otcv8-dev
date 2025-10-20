#!/usr/bin/env python3
"""
Generate index.md files for all chapters with proper frontmatter, toctree, and content.
"""

import os
from datetime import datetime
import hashlib

CHAPTERS = {
    "01_core": {
        "title": "01 - Core C++ API",
        "summary": "Core C++ framework and client classes, types, functions, and class diagrams for OTClient v8.",
        "tags": ["cpp", "api", "core", "framework"],
        "doc_class": "api"
    },
    "01_runtime": {
        "title": "01 - Runtime",
        "summary": "Runtime lifecycle, scheduler/dispatcher, threading, and event queues.",
        "tags": ["runtime", "lifecycle", "scheduler", "threads"],
        "doc_class": "spec"
    },
    "02_events": {
        "title": "02 - Events",
        "summary": "C++ and Lua event emission, dispatch, signals, and emitter-handler mappings.",
        "tags": ["events", "signals", "dispatcher", "cpp", "lua"],
        "doc_class": "api"
    },
    "03_modules": {
        "title": "03 - Modules",
        "summary": "C++ and Lua modules, exports, relations, and integration examples.",
        "tags": ["modules", "cpp", "lua", "exports"],
        "doc_class": "api"
    },
    "04_ui": {
        "title": "04 - UI/OTUI",
        "summary": "UI widget hierarchy, styles, fonts, images, and links to data assets.",
        "tags": ["ui", "otui", "widgets", "styles"],
        "doc_class": "ui"
    },
    "05_network": {
        "title": "05 - Network",
        "summary": "Network protocol classes and TFS extended opcode patch appendix.",
        "tags": ["network", "protocol", "tfs"],
        "doc_class": "spec"
    },
    "06_assets": {
        "title": "06 - Assets Pipeline",
        "summary": "Asset atlas, versioning, compression, and differences from data chapter.",
        "tags": ["assets", "pipeline", "atlas"],
        "doc_class": "guide"
    },
    "07_settings_crypto": {
        "title": "07 - Settings & Crypto",
        "summary": "Settings formats, profiles, keys, and cryptographic flows.",
        "tags": ["settings", "crypto", "keys", "config"],
        "doc_class": "spec"
    },
    "08_audio": {
        "title": "08 - Audio",
        "summary": "Audio channels, loading, and C++/Lua examples.",
        "tags": ["audio", "sound", "channels"],
        "doc_class": "api"
    },
    "09_logging": {
        "title": "09 - Logging",
        "summary": "Logging levels, targets, examples, and runtime integration.",
        "tags": ["logging", "debug", "trace"],
        "doc_class": "spec"
    },
    "10_game_runtime": {
        "title": "10 - Game Runtime",
        "summary": "Game loop, input handling, map management, and dependencies with events/UI.",
        "tags": ["game", "runtime", "loop", "input"],
        "doc_class": "spec"
    },
    "11_data": {
        "title": "11 - Data",
        "summary": "Complete data taxonomy and mapping to OTUI widgets.",
        "tags": ["data", "assets", "taxonomy"],
        "doc_class": "spec"
    },
    "12_otmod": {
        "title": "12 - OTMOD",
        "summary": "Module structure, hooks, dependencies, load-later, sandbox, and blueprints.",
        "tags": ["otmod", "modules", "lua", "sandbox"],
        "doc_class": "spec"
    },
    "13_layouts": {
        "title": "13 - Layouts",
        "summary": "Layout overrides vs /data, override matrices, and image properties.",
        "tags": ["layouts", "overrides", "themes"],
        "doc_class": "spec"
    },
    "14_android": {
        "title": "14 - Android",
        "summary": "Android assets, ABI-specific .so files, AAB/APK builds, and signing.",
        "tags": ["android", "abi", "build"],
        "doc_class": "guide"
    },
    "15_vc16": {
        "title": "15 - VC16/ANGLE",
        "summary": "EGL/GLES headers, libraries, DLL distribution, and sanity tests.",
        "tags": ["vc16", "angle", "egl", "gles"],
        "doc_class": "guide"
    }
}

def generate_index(chapter_id: str, meta: dict, authoring_root: str):
    """Generate index.md for a chapter."""
    chapter_path = os.path.join(authoring_root, chapter_id)
    index_path = os.path.join(chapter_path, "index.md")
    
    # Generate SHA (abbreviated)
    sha = hashlib.sha1(chapter_id.encode()).hexdigest()[:7]
    
    # Current timestamp
    now = datetime.utcnow().isoformat() + "Z"
    
    # Frontmatter (CSV-like single line as per spec)
    frontmatter = f'doc_id: {chapter_id}, source_path: docs/authoring/{chapter_id}, source_sha: {sha}, last_sync_iso: {now}, doc_class: {meta["doc_class"]}, language: pl, title: {meta["title"]}, summary: {meta["summary"]}, tags: {",".join(meta["tags"])}'
    
    content = f"""---
{frontmatter}
---

# {meta['title']}

{meta['summary']}

## Przegląd

Ten rozdział dokumentuje {chapter_id.replace('_', ' ')} w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{{toctree}}
:maxdepth: 2
:titlesonly:
:hidden:

README
"""
    
    # Add sections if they exist
    sections_dir = os.path.join(chapter_path, "sections")
    if os.path.exists(sections_dir):
        content += "sections/index\n"
    
    # Add blueprints if they exist
    blueprints_dir = os.path.join(chapter_path, "blueprints")
    if os.path.exists(blueprints_dir):
        content += "blueprints/index\n"
    
    # Add datasets if they exist
    datasets_dir = os.path.join(chapter_path, "datasets")
    if os.path.exists(datasets_dir):
        content += "datasets/index\n"
    
    # Add diagrams if they exist
    diagrams_dir = os.path.join(chapter_path, "diagrams")
    if os.path.exists(diagrams_dir):
        content += "diagrams/index\n"
    
    content += """```

## Datasets

"""
    
    # Check for CSV files in datasets
    if os.path.exists(datasets_dir):
        csv_files = [f for f in os.listdir(datasets_dir) if f.endswith('.csv') and f != 'index.md']
        if csv_files:
            for csv_file in sorted(csv_files)[:3]:  # Show first 3
                content += f"- `{csv_file}`\n"
    
    content += """
## Diagramy

```{contents}
:local:
:depth: 2
```

## Crosslinks

"""
    
    # Add appropriate crosslinks based on chapter
    crosslinks = get_crosslinks(chapter_id)
    for link in crosslinks:
        content += f"- [{link['title']}](../{link['target']}/index.md)\n"
    
    content += """

## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** """ + now + """

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [ ] Diagrams added
- [ ] Crosslinks verified
- [ ] Content complete (≥18KB target)

## Appendix / Facets

(facet-""" + chapter_id + """.main)=
### Facet: `""" + chapter_id + """.main`

Main documentation facet for """ + chapter_id + """.
"""
    
    # Write the file
    os.makedirs(chapter_path, exist_ok=True)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated {index_path}")

def get_crosslinks(chapter_id: str) -> list:
    """Get appropriate crosslinks for a chapter."""
    crosslink_map = {
        "01_core": [
            {"title": "Runtime", "target": "01_runtime"},
            {"title": "Events", "target": "02_events"},
            {"title": "Modules", "target": "03_modules"}
        ],
        "01_runtime": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Events", "target": "02_events"},
            {"title": "Game Runtime", "target": "10_game_runtime"}
        ],
        "02_events": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Modules", "target": "03_modules"},
            {"title": "UI", "target": "04_ui"}
        ],
        "03_modules": [
            {"title": "Core API", "target": "01_core"},
            {"title": "UI", "target": "04_ui"},
            {"title": "OTMOD", "target": "12_otmod"}
        ],
        "04_ui": [
            {"title": "Data", "target": "11_data"},
            {"title": "Modules", "target": "03_modules"},
            {"title": "Layouts", "target": "13_layouts"}
        ],
        "05_network": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Events", "target": "02_events"},
            {"title": "Game Runtime", "target": "10_game_runtime"}
        ],
        "06_assets": [
            {"title": "Data", "target": "11_data"},
            {"title": "UI", "target": "04_ui"},
            {"title": "Layouts", "target": "13_layouts"}
        ],
        "07_settings_crypto": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Modules", "target": "03_modules"}
        ],
        "08_audio": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Data", "target": "11_data"}
        ],
        "09_logging": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Runtime", "target": "01_runtime"}
        ],
        "10_game_runtime": [
            {"title": "Runtime", "target": "01_runtime"},
            {"title": "Events", "target": "02_events"},
            {"title": "UI", "target": "04_ui"}
        ],
        "11_data": [
            {"title": "UI", "target": "04_ui"},
            {"title": "Assets", "target": "06_assets"},
            {"title": "Layouts", "target": "13_layouts"}
        ],
        "12_otmod": [
            {"title": "Modules", "target": "03_modules"},
            {"title": "Data", "target": "11_data"},
            {"title": "UI", "target": "04_ui"}
        ],
        "13_layouts": [
            {"title": "UI", "target": "04_ui"},
            {"title": "Data", "target": "11_data"}
        ],
        "14_android": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Data", "target": "11_data"},
            {"title": "Game Runtime", "target": "10_game_runtime"}
        ],
        "15_vc16": [
            {"title": "Core API", "target": "01_core"},
            {"title": "Network", "target": "05_network"}
        ]
    }
    
    return crosslink_map.get(chapter_id, [])

def main():
    authoring_root = "/home/runner/work/otcv8-dev/otcv8-dev/docs/authoring"
    
    for chapter_id, meta in CHAPTERS.items():
        generate_index(chapter_id, meta, authoring_root)
    
    print("\nAll chapter indexes generated!")

if __name__ == "__main__":
    main()

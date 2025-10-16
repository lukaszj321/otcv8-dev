#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Relations Matrix
Creates cross-chapter relationships and mappings.
"""

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_AUTHORING = REPO_ROOT / "docs" / "authoring"


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def generate_relations():
    """Generate relations.csv with cross-chapter relationships."""
    relations_dir = DOCS_AUTHORING / "relations"
    ensure_dir(relations_dir)
    
    # Define relations between chapters
    relations = [
        # Core → Other chapters
        ["01_core", "cpp_api", "03_modules", "lua_exports", "uses", "docs/authoring/03_modules/datasets/lua_exports.csv", "C++ bindings to Lua"],
        ["01_core", "cpp_api", "04_ui", "widgets", "renders", "docs/authoring/04_ui/datasets/ui_widgets.csv", "Core renders UI widgets"],
        ["01_core", "cpp_api", "02_events", "events_matrix", "emits", "docs/authoring/02_events/datasets/events_matrix.csv", "Core emits system events"],
        ["01_core", "cpp_api", "09_logging", "logging_categories", "logs", "docs/authoring/09_logging/datasets/logging_categories.csv", "Core uses logging"],
        
        # Runtime → Other chapters
        ["01_runtime", "scheduler", "02_events", "events_matrix", "handles", "docs/authoring/02_events/datasets/events_matrix.csv", "Runtime handles events"],
        ["01_runtime", "dispatcher", "01_core", "cpp_api", "uses", "docs/authoring/01_core/datasets/cpp_symbols.csv", "Runtime uses core API"],
        
        # Events → Other chapters
        ["02_events", "events_matrix", "03_modules", "lua_exports", "emits", "docs/authoring/03_modules/datasets/lua_exports.csv", "Events emitted from Lua"],
        ["02_events", "events_matrix", "04_ui", "widgets", "handles", "docs/authoring/04_ui/datasets/ui_widgets.csv", "UI handles events"],
        
        # Modules → Other chapters
        ["03_modules", "lua_exports", "01_core", "cpp_api", "calls", "docs/authoring/01_core/datasets/cpp_symbols.csv", "Lua calls C++ functions"],
        ["03_modules", "lua_exports", "04_ui", "widgets", "uses", "docs/authoring/04_ui/datasets/ui_widgets.csv", "Modules manipulate UI"],
        ["03_modules", "lua_exports", "02_events", "events_matrix", "emits", "docs/authoring/02_events/datasets/events_matrix.csv", "Modules emit events"],
        
        # UI → Other chapters
        ["04_ui", "widgets", "11_data", "assets_catalog", "uses", "docs/authoring/11_data/datasets/assets_catalog.csv", "UI uses data assets"],
        ["04_ui", "widgets", "13_layouts", "layouts", "uses", "docs/authoring/13_layouts/datasets/layouts.csv", "UI uses layout overrides"],
        ["04_ui", "widgets", "02_events", "events_matrix", "emits", "docs/authoring/02_events/datasets/events_matrix.csv", "UI emits user events"],
        
        # Network → Other chapters
        ["05_network", "protocol", "01_core", "cpp_api", "uses", "docs/authoring/01_core/datasets/cpp_symbols.csv", "Network uses core classes"],
        ["05_network", "protocol", "02_events", "events_matrix", "emits", "docs/authoring/02_events/datasets/events_matrix.csv", "Network emits connection events"],
        ["05_network", "protocol", "09_logging", "logging_categories", "logs", "docs/authoring/09_logging/datasets/logging_categories.csv", "Network logs traffic"],
        
        # Assets → Other chapters
        ["06_assets", "pipeline", "11_data", "assets_catalog", "processes", "docs/authoring/11_data/datasets/assets_catalog.csv", "Pipeline processes assets"],
        ["06_assets", "pipeline", "04_ui", "widgets", "renders", "docs/authoring/04_ui/datasets/ui_widgets.csv", "Assets rendered by UI"],
        
        # Settings → Other chapters
        ["07_settings_crypto", "config", "01_core", "cpp_api", "uses", "docs/authoring/01_core/datasets/cpp_symbols.csv", "Settings use core storage"],
        ["07_settings_crypto", "crypto", "05_network", "protocol", "uses", "docs/authoring/05_network/datasets/protocol.csv", "Crypto used for network"],
        
        # Audio → Other chapters
        ["08_audio", "sound_system", "11_data", "assets_catalog", "uses", "docs/authoring/11_data/datasets/assets_catalog.csv", "Audio uses sound files"],
        ["08_audio", "sound_system", "02_events", "events_matrix", "handles", "docs/authoring/02_events/datasets/events_matrix.csv", "Audio responds to events"],
        
        # Logging → Other chapters
        ["09_logging", "logging_categories", "01_core", "cpp_api", "uses", "docs/authoring/01_core/datasets/cpp_symbols.csv", "Logging uses core classes"],
        
        # Game Runtime → Other chapters
        ["10_game_runtime", "game_loop", "01_runtime", "scheduler", "uses", "docs/authoring/01_runtime/datasets/summary.csv", "Game loop uses scheduler"],
        ["10_game_runtime", "game_loop", "02_events", "events_matrix", "emits", "docs/authoring/02_events/datasets/events_matrix.csv", "Game emits gameplay events"],
        ["10_game_runtime", "game_loop", "04_ui", "widgets", "updates", "docs/authoring/04_ui/datasets/ui_widgets.csv", "Game updates UI"],
        
        # Data → Other chapters
        ["11_data", "assets_catalog", "04_ui", "widgets", "owns", "docs/authoring/04_ui/datasets/ui_widgets.csv", "Data owns UI assets"],
        ["11_data", "assets_catalog", "13_layouts", "layouts", "owns", "docs/authoring/13_layouts/datasets/layouts.csv", "Data owns layout assets"],
        
        # OTMOD → Other chapters
        ["12_otmod", "modules", "03_modules", "lua_exports", "loads", "docs/authoring/03_modules/datasets/modules_index.csv", "OTMOD loads Lua modules"],
        ["12_otmod", "modules", "04_ui", "widgets", "uses", "docs/authoring/04_ui/datasets/ui_widgets.csv", "OTMOD uses UI"],
        ["12_otmod", "modules", "11_data", "assets_catalog", "uses", "docs/authoring/11_data/datasets/assets_catalog.csv", "OTMOD uses assets"],
        
        # Layouts → Other chapters
        ["13_layouts", "layouts", "11_data", "assets_catalog", "overrides", "docs/authoring/11_data/datasets/assets_catalog.csv", "Layouts override data assets"],
        ["13_layouts", "layouts", "04_ui", "widgets", "uses", "docs/authoring/04_ui/datasets/ui_widgets.csv", "Layouts used by UI"],
        
        # Android → Other chapters
        ["14_android", "platform", "11_data", "assets_catalog", "packages", "docs/authoring/11_data/datasets/assets_catalog.csv", "Android packages assets"],
        ["14_android", "platform", "12_otmod", "modules", "packages", "docs/authoring/12_otmod/datasets/modules.csv", "Android packages modules"],
        
        # VC16 → Other chapters
        ["15_vc16", "build_system", "01_core", "cpp_api", "compiles", "docs/authoring/01_core/datasets/cpp_headers.csv", "VC16 compiles core"],
    ]
    
    # Write relations.csv
    relations_file = relations_dir / "relations.csv"
    with open(relations_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["from_chapter", "from_facet", "to_chapter", "to_facet", "rel_type", "evidence_path", "note"])
        writer.writerows(relations)
    
    print(f"✓ Created {relations_file.relative_to(REPO_ROOT)}")
    print(f"  Total relations: {len(relations)}")
    
    # Generate matrix.md
    generate_matrix(relations)


def generate_matrix(relations):
    """Generate visual matrix of relations."""
    relations_dir = DOCS_AUTHORING / "relations"
    
    # Collect all chapters
    chapters = set()
    for rel in relations:
        chapters.add(rel[0])
        chapters.add(rel[2])
    chapters = sorted(chapters)
    
    # Build relation type map
    rel_map = {}
    for rel in relations:
        from_ch, to_ch, rel_type = rel[0], rel[2], rel[4]
        key = (from_ch, to_ch)
        if key not in rel_map:
            rel_map[key] = []
        rel_map[key].append(rel_type)
    
    # Generate markdown matrix
    matrix_content = """# Relations Matrix

This matrix shows relationships between chapters.

**Legend:**
- **uses** - Uses functionality from
- **calls** - Calls functions from
- **emits** - Emits events to
- **handles** - Handles events from
- **renders** - Renders components of
- **owns** - Owns data/assets of
- **logs** - Logs to
- **processes** - Processes data from
- **packages** - Packages content from
- **compiles** - Compiles code from
- **overrides** - Overrides assets from
- **loads** - Loads modules from
- **updates** - Updates state of

## Matrix

"""
    
    # Header row
    matrix_content += "| From \\ To |"
    for to_ch in chapters:
        matrix_content += f" {to_ch} |"
    matrix_content += "\n"
    
    # Separator
    matrix_content += "|-----------|"
    for _ in chapters:
        matrix_content += "------|"
    matrix_content += "\n"
    
    # Data rows
    for from_ch in chapters:
        matrix_content += f"| **{from_ch}** |"
        for to_ch in chapters:
            if from_ch == to_ch:
                cell = "-"
            else:
                key = (from_ch, to_ch)
                if key in rel_map:
                    cell = ", ".join(rel_map[key])
                else:
                    cell = ""
            matrix_content += f" {cell} |"
        matrix_content += "\n"
    
    matrix_content += f"""

## Statistics

- Total chapters: {len(chapters)}
- Total relations: {len(relations)}
- Relation types: {len(set(rel[4] for rel in relations))}

## Relation Types Distribution

"""
    
    # Count relation types
    rel_type_counts = {}
    for rel in relations:
        rel_type = rel[4]
        rel_type_counts[rel_type] = rel_type_counts.get(rel_type, 0) + 1
    
    for rel_type, count in sorted(rel_type_counts.items(), key=lambda x: x[1], reverse=True):
        matrix_content += f"- **{rel_type}**: {count}\n"
    
    matrix_file = relations_dir / "matrix.md"
    matrix_file.write_text(matrix_content, encoding='utf-8')
    
    print(f"✓ Created {matrix_file.relative_to(REPO_ROOT)}")


def main():
    print("=" * 70)
    print("Generating Relations Matrix")
    print("=" * 70)
    
    generate_relations()
    
    print("\n✓ Relations generation complete!")


if __name__ == "__main__":
    main()

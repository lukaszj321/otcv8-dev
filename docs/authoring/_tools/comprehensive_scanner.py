#!/usr/bin/env python3
"""
Comprehensive scanner for OTClient v8 documentation and RAG rebuild.
Scans data/**, modules/**, layouts/**, android/**, vc16/** and generates datasets.
"""

import os
import csv
import json
import re
import hashlib
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

def scan_data_assets(repo_root: str) -> List[Dict]:
    """Scan data/** directory for all assets."""
    assets = []
    data_path = Path(repo_root) / "data"
    
    if not data_path.exists():
        return assets
    
    # Asset type mapping by folder
    type_map = {
        "images": "image",
        "fonts": "font",
        "sounds": "audio",
        "styles": "style",
        "locales": "config",
        "shaders": "shader",
        "cursors": "image"
    }
    
    for file_path in data_path.rglob("*"):
        if file_path.is_file():
            rel_path = str(file_path.relative_to(repo_root))
            parent = file_path.parent.name
            
            asset_type = type_map.get(parent, "other")
            
            # Try to determine format from extension
            ext = file_path.suffix.lower()
            
            assets.append({
                "path": rel_path,
                "type": asset_type,
                "format": ext,
                "used_by_layouts": json.dumps([]),
                "used_by_otui": json.dumps([]),
                "used_by_modules": json.dumps([]),
                "tags": json.dumps([parent]),
                "notes": ""
            })
    
    return assets

def scan_modules(repo_root: str) -> List[Dict]:
    """Scan modules/** for OTMOD packages."""
    modules = []
    modules_path = Path(repo_root) / "modules"
    
    if not modules_path.exists():
        return modules
    
    for mod_dir in modules_path.iterdir():
        if mod_dir.is_dir():
            # Find .otmod file
            otmod_files = list(mod_dir.glob("*.otmod"))
            manifest = otmod_files[0].name if otmod_files else None
            
            # Find lua files
            lua_files = list(mod_dir.rglob("*.lua"))
            entry_lua = None
            if lua_files:
                # Look for main/init file
                for lf in lua_files:
                    if lf.stem in [mod_dir.name, "init", "main"]:
                        entry_lua = str(lf.relative_to(repo_root))
                        break
                if not entry_lua:
                    entry_lua = str(lua_files[0].relative_to(repo_root))
            
            # Find OTUI files
            otui_files = [str(f.relative_to(repo_root)) for f in mod_dir.rglob("*.otui")]
            
            modules.append({
                "module": mod_dir.name,
                "path": str(mod_dir.relative_to(repo_root)),
                "manifest": manifest or "",
                "dependencies": json.dumps([]),  # Would need to parse .otmod
                "exports": json.dumps([]),  # Would need to parse Lua
                "assets": json.dumps([]),
                "ui_roots": json.dumps(otui_files[:5]),  # Limit to first 5
                "entry_lua": entry_lua or "",
                "notes": ""
            })
    
    return modules

def scan_layouts(repo_root: str) -> List[Dict]:
    """Scan layouts/** directory."""
    layouts = []
    layouts_path = Path(repo_root) / "layouts"
    
    if not layouts_path.exists():
        return layouts
    
    for layout_dir in layouts_path.iterdir():
        if layout_dir.is_dir():
            # Scan for OTUI and images
            otui_files = list(layout_dir.rglob("*.otui"))
            image_files = [str(f.relative_to(repo_root)) 
                          for f in layout_dir.rglob("*") 
                          if f.suffix.lower() in ['.png', '.jpg', '.bmp']]
            
            layouts.append({
                "layout_id": layout_dir.name,
                "path": str(layout_dir.relative_to(repo_root)),
                "type": "screen",  # Default
                "section": "",
                "uses_images": json.dumps(image_files[:10]),
                "uses_fonts": json.dumps([]),
                "uses_otui": json.dumps([str(f.relative_to(repo_root)) for f in otui_files[:10]]),
                "notes": ""
            })
    
    return layouts

def scan_android(repo_root: str) -> Dict[str, List[Dict]]:
    """Scan android/** directory."""
    android_path = Path(repo_root) / "android"
    
    if not android_path.exists():
        return {"assets": [], "libs": []}
    
    assets = []
    libs = []
    
    # Scan for assets
    assets_dir = android_path / "assets"
    if assets_dir.exists():
        for f in assets_dir.rglob("*"):
            if f.is_file():
                assets.append({
                    "path": str(f.relative_to(repo_root)),
                    "type": "asset",
                    "notes": ""
                })
    
    # Scan for libs
    libs_dir = android_path / "jniLibs"
    if not libs_dir.exists():
        libs_dir = android_path / "libs"
    
    if libs_dir.exists():
        for f in libs_dir.rglob("*.so"):
            libs.append({
                "path": str(f.relative_to(repo_root)),
                "abi": f.parent.name if f.parent != libs_dir else "unknown",
                "notes": ""
            })
    
    return {"assets": assets, "libs": libs}

def scan_vc16(repo_root: str) -> Dict[str, List[Dict]]:
    """Scan vc16/** directory."""
    vc16_path = Path(repo_root) / "vc16"
    
    if not vc16_path.exists():
        return {"headers": [], "libs": []}
    
    headers = []
    libs = []
    
    # Scan for headers
    for f in vc16_path.rglob("*.h"):
        headers.append({
            "path": str(f.relative_to(repo_root)),
            "type": "header",
            "notes": ""
        })
    
    # Scan for libs and DLLs
    for ext in [".lib", ".dll"]:
        for f in vc16_path.rglob(f"*{ext}"):
            libs.append({
                "path": str(f.relative_to(repo_root)),
                "type": ext[1:],  # Remove dot
                "notes": ""
            })
    
    return {"headers": headers, "libs": libs}

def write_csv(path: str, rows: List[Dict], fieldnames: List[str]):
    """Write CSV file with given fieldnames."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    repo_root = "/home/runner/work/otcv8-dev/otcv8-dev"
    authoring_root = os.path.join(repo_root, "docs", "authoring")
    
    print("Scanning data assets...")
    data_assets = scan_data_assets(repo_root)
    if data_assets:
        write_csv(
            os.path.join(authoring_root, "11_data", "datasets", "data_assets.csv"),
            data_assets,
            ["path", "type", "format", "used_by_layouts", "used_by_otui", 
             "used_by_modules", "tags", "notes"]
        )
        print(f"  - Wrote {len(data_assets)} data assets")
    
    print("Scanning modules...")
    modules = scan_modules(repo_root)
    if modules:
        write_csv(
            os.path.join(authoring_root, "12_otmod", "datasets", "otmod_packages.csv"),
            modules,
            ["module", "path", "manifest", "dependencies", "exports", 
             "assets", "ui_roots", "entry_lua", "notes"]
        )
        print(f"  - Wrote {len(modules)} modules")
    
    print("Scanning layouts...")
    layouts = scan_layouts(repo_root)
    if layouts:
        write_csv(
            os.path.join(authoring_root, "13_layouts", "datasets", "layouts.csv"),
            layouts,
            ["layout_id", "path", "type", "section", "uses_images", 
             "uses_fonts", "uses_otui", "notes"]
        )
        print(f"  - Wrote {len(layouts)} layouts")
    
    print("Scanning android...")
    android_data = scan_android(repo_root)
    if android_data["assets"]:
        write_csv(
            os.path.join(authoring_root, "14_android", "datasets", "android_assets.csv"),
            android_data["assets"],
            ["path", "type", "notes"]
        )
        print(f"  - Wrote {len(android_data['assets'])} android assets")
    if android_data["libs"]:
        write_csv(
            os.path.join(authoring_root, "14_android", "datasets", "android_libs.csv"),
            android_data["libs"],
            ["path", "abi", "notes"]
        )
        print(f"  - Wrote {len(android_data['libs'])} android libs")
    
    print("Scanning vc16...")
    vc16_data = scan_vc16(repo_root)
    if vc16_data["headers"]:
        write_csv(
            os.path.join(authoring_root, "15_vc16", "datasets", "angle_headers.csv"),
            vc16_data["headers"],
            ["path", "type", "notes"]
        )
        print(f"  - Wrote {len(vc16_data['headers'])} vc16 headers")
    if vc16_data["libs"]:
        write_csv(
            os.path.join(authoring_root, "15_vc16", "datasets", "angle_libs.csv"),
            vc16_data["libs"],
            ["path", "type", "notes"]
        )
        print(f"  - Wrote {len(vc16_data['libs'])} vc16 libs")
    
    print("\nAll datasets generated successfully!")

if __name__ == "__main__":
    main()

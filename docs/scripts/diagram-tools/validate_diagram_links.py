#!/usr/bin/env python3
"""
Validate 'click' targets found inside Mermaid blocks in Markdown files.

Usage:
  python3 scripts/diagram-tools/validate_diagram_links.py [--root docs] [--report out.json]

Checks:
- extracts click "path" from lines like: click NodeID "path" "tooltip"
- for relative paths checks file existence (relative to repo root)
- for fragment targets (file#anchor) tries to match anchor to headings in the target .md
- exits with code 0 if all found, 2 if missing files, 3 if missing anchors (or mixed)
Outputs a JSON report when --report is given.
"""
import re
import os
import sys
import json
from pathlib import Path

ROOT = Path(os.getcwd())
DEFAULT_DOCS = Path("docs")
CLICK_RE = re.compile(r'click\s+\S+\s+"([^"]+)"(?:\s+"[^"]*")?')

def slugify_heading(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s

def find_markdown_files(root: Path):
    return list(root.rglob("*.md"))

def extract_clicks_from_text(text: str):
    clicks = []
    for m in CLICK_RE.finditer(text):
        clicks.append(m.group(1))
    return clicks

def headings_in_file(path: Path):
    headings = []
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            h = re.match(r'^(#{1,6})\s+(.*)', line)
            if h:
                headings.append(slugify_heading(h.group(2)))
    except Exception:
        pass
    return headings

def main():
    root_arg = Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else DEFAULT_DOCS
    report_path = None
    if "--report" in sys.argv:
        i = sys.argv.index("--report")
        if i+1 < len(sys.argv):
            report_path = Path(sys.argv[i+1])
    md_files = find_markdown_files(Path(root_arg))
    report = {"checked_files": 0, "clicks_found": 0, "missing_files": [], "missing_anchors": []}
    for md in md_files:
        try:
            txt = md.read_text(encoding="utf-8")
        except Exception:
            continue
        clicks = extract_clicks_from_text(txt)
        if not clicks:
            continue
        report["checked_files"] += 1
        for tgt in clicks:
            report["clicks_found"] += 1
            # handle fragment
            if tgt.startswith("http://") or tgt.startswith("https://"):
                # external link - skip file existence (could optionally check HEAD)
                continue
            # normalize windows/backslashes
            tgt_norm = tgt.replace("\\", "/")
            if "#" in tgt_norm:
                filepart, anchor = tgt_norm.split("#", 1)
            else:
                filepart, anchor = tgt_norm, None
            # handle index.html -> index.md heuristic
            file_candidate = Path(filepart)
            if file_candidate.suffix == ".html":
                # try corresponding .md next to index.html
                md_candidate = None
                if file_candidate.name == "index.html":
                    # try parent/index.md
                    md_candidate = file_candidate.with_suffix(".md")
                else:
                    md_candidate = file_candidate.with_suffix(".md")
            else:
                md_candidate = file_candidate
            # Resolve relative paths relative to current md file
            resolved = (md.parent / md_candidate).resolve()
            if not resolved.exists():
                # also try resolving from repo root
                alt = (ROOT / file_candidate).resolve()
                if not alt.exists():
                    report["missing_files"].append({"source": str(md), "target": tgt, "resolved": str(resolved)})
                    continue
                else:
                    resolved = alt
            # if anchor present, check headings
            if anchor:
                headings = headings_in_file(resolved)
                # try anchors like facet-... or plain slug; remove starting '#' if any
                anchor_slug = anchor.split("#")[-1]
                anchor_slug = anchor_slug.strip().lower()
                anchor_slug = re.sub(r'[^a-z0-9_\-]', '-', anchor_slug)
                if anchor_slug not in headings:
                    report["missing_anchors"].append({"source": str(md), "target": tgt, "file": str(resolved), "anchor": anchor})
    # decide exit code
    exit_code = 0
    if report["missing_files"]:
        exit_code = 2
    if report["missing_anchors"]:
        exit_code = 3 if exit_code == 0 else exit_code
    if report_path:
        try:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        except Exception:
            pass
    # print summary
    print(json.dumps(report, indent=2))
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

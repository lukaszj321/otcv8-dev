
"""
Builds a lightweight relations CSV by scanning authoring MD for facet anchors and inline links.
This is a documented scaffold - extend with repo-specific rules as needed.
"""
import re, os, csv, pathlib

FACET = re.compile(r'^\(facet-([^)]+)\)=')
LINK  = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def collect_relations(authoring_root: str):
    rels = []
    root = pathlib.Path(authoring_root)
    for p in root.rglob("*.md"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        cur_facet = None
        for ln in text.splitlines():
            m = FACET.match(ln.strip())
            if m:
                cur_facet = m.group(1)
            for _label, href in LINK.findall(ln):
                if href.startswith("#facet-"):
                    to = href.lstrip("#").replace("facet-","")
                    if cur_facet:
                        rels.append((cur_facet, to, str(p.relative_to(root))))
    return rels

def write_csv(path: str, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["from_facet","to_facet","source_file"])
        for r in rows:
            w.writerow(r)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: xref_builder.py <authoring_root> <out_csv>")
        raise SystemExit(2)
    rels = collect_relations(sys.argv[1])
    write_csv(sys.argv[2], rels)

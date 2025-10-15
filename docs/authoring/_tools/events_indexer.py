
"""
Heuristic events indexer: scans C++ & Lua for common emitter/handler patterns.
Produces CSV with minimal fields. Extend patterns for full coverage.
"""
import re, os, csv, pathlib

CPP_EMIT = re.compile(r'\b(em(?:it|place)|dispatch|signal|sigc::signal|addEvent|g_dispatcher)\b')
LUA_EVT  = re.compile(r'\b(connect|on[A-Z][A-Za-z]+|addEvent|schedule|signal|g_ui\.)')

def scan(root: str):
    for p in pathlib.Path(root).rglob("*"):
        if p.suffix in {".cpp",".hpp",".h",".lua"}:
            text = p.read_text(encoding="utf-8", errors="ignore")
            for i, ln in enumerate(text.splitlines(), 1):
                if p.suffix in {".cpp",".hpp",".h"} and CPP_EMIT.search(ln):
                    yield {"lang":"cpp","file":str(p), "line":i, "symbol":CPP_EMIT.search(ln).group(0)}
                if p.suffix==".lua" and LUA_EVT.search(ln):
                    yield {"lang":"lua","file":str(p), "line":i, "symbol":LUA_EVT.search(ln).group(0)}

def write_csv(path: str, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["lang","file","line","symbol"])
        w.writeheader()
        w.writerows(rows)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: events_indexer.py <repo_root> <out_csv>")
        raise SystemExit(2)
    rows = list(scan(sys.argv[1]))
    os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)
    write_csv(sys.argv[2], rows)

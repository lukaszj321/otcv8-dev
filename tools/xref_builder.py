
#!/usr/bin/env python3
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[2]
AUTHORING = ROOT / "authoring"
DATA = AUTHORING / "_data"
DATA.mkdir(parents=True, exist_ok=True)

def read_csv(p: Path):
    try:
        with p.open(encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []

def main():
    edges = []
    ev = read_csv(AUTHORING / "02_events" / "datasets" / "events_matrix.csv")
    ui = read_csv(AUTHORING / "04_ui" / "datasets" / "ui_signals.csv")
    lua = read_csv(AUTHORING / "03_modules" / "datasets" / "lua_exports.csv")

    event_names = {e.get("event","").strip() for e in ev if e.get("event")}
    ui_event_names = {e.get("event","").strip() for e in ui if e.get("event")}

    for name in sorted(event_names & ui_event_names):
        edges.append({
            "from": {"c":"04_ui","f":"04_ui.ui_signals"},
            "to": {"c":"02_events","f":"02_events.events_matrix"},
            "type": "relates",
            "evidence": "04_ui/datasets/ui_signals.csv"
        })

    lua_funcs = { (row.get("module",""), row.get("function","")) for row in lua if row.get("function") }
    for row in ui:
        hb = (row.get("handled_by") or "") + " " + (row.get("emitted_by") or "")
        for mod, func in lua_funcs:
            key = f"{mod}.{func}" if mod else func
            if key and key in hb:
                edges.append({
                    "from": {"c":"04_ui","f":"04_ui.ui_signals"},
                    "to": {"c":"03_modules","f":"03_modules.lua_exports"},
                    "type": "uses",
                    "evidence": "04_ui/datasets/ui_signals.csv"
                })
                break

    csv_path = DATA / "xref.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["from_chapter","from_facet","to_chapter","to_facet","type","evidence_path","note"])
        for e in edges:
            w.writerow([e["from"]["c"], e["from"]["f"], e["to"]["c"], e["to"]["f"], e["type"], e["evidence"], "auto"])

    json_path = DATA / "xref.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(edges, f, ensure_ascii=False, indent=2)

    print(f"[XREF] wrote {csv_path} and {json_path} (edges={len(edges)})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

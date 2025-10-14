
#!/usr/bin/env python3
# Validate CSV headers against simple JSON Schemas in docs/authoring/_data/schemas/*.schema.json

from pathlib import Path
import json, csv

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"
SCHEMAS = AUTHORING / "_data" / "schemas"
REPORT = AUTHORING / "_data" / "csv_schema_report.csv"

MAP = {
    "summary.csv": "summary.schema.json",
    "events_matrix.csv": "events_matrix.schema.json",
    "lua_exports.csv": "lua_exports.schema.json",
    "ui_widgets.csv": "ui_widgets.schema.json",
    "network_messages.csv": "network_messages.schema.json",
}

def load_schema(name: str):
    p = SCHEMAS / name
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None

def check_headers(csv_path: Path, schema: dict):
    try:
        with csv_path.open(encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
        required = [c["name"] for c in schema.get("columns", []) if c.get("required", True)]
        missing = [h for h in required if h not in header]
        if missing:
            return False, "missing=" + "|".join(missing) + " found=" + "|".join(header)
        return True, "OK"
    except Exception as e:
        return False, "error reading csv: %s" % e

def main():
    rows = [ ["chapter","file","schema","status","details"] ]
    for ch in sorted([p for p in AUTHORING.iterdir() if p.is_dir() and p.name[:2].isdigit()], key=lambda p: p.name):
        ds_dir = ch / "datasets"
        if not ds_dir.exists():
            continue
        for csv_file in ds_dir.glob("*.csv"):
            schema_name = MAP.get(csv_file.name) or (csv_file.stem + ".schema.json")
            schema = load_schema(schema_name)
            if not schema:
                rows.append([ch.name, csv_file.name, schema_name, "SKIP", "no schema"])
                continue
            ok, details = check_headers(csv_file, schema)
            rows.append([ch.name, csv_file.name, schema_name, "OK" if ok else "FAIL", details])

    REPORT.write_text("\n".join([",".join(r) for r in rows]), encoding="utf-8")
    print(f"[SCHEMA] report at {REPORT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

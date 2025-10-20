
#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT.parent
AUTHORING = ROOT / "authoring"
DATA = AUTHORING / "_data"
DATA.mkdir(parents=True, exist_ok=True)

REQ_SUMMARY_HDR = ["metric","value","note"]

def write_report(rows):
    out = DATA / "qa_report.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["chapter","check","status","details"])
        for r in rows:
            w.writerow(r)
    print(f"[QA] report written: {out}")

def has_mermaid_init(text: str) -> bool:
    return text.lstrip().startswith("%%{init:")

def check_chapter(ch_dir: Path):
    rows = []
    ch = ch_dir.name
    idx = ch_dir / "index.md"
    if not idx.exists():
        rows.append([ch, "index.md exists", "FAIL", "missing index.md"])
    else:
        rows.append([ch, "index.md exists", "OK", ""])

    datasets = list((ch_dir / "datasets").glob("*.csv")) if (ch_dir / "datasets").exists() else []
    diags = list((ch_dir / "diagrams").glob("*.mmd")) if (ch_dir / "diagrams").exists() else []
    rows.append([ch, "datasets presence", "OK" if datasets else "WARN", f"{len(datasets)} csv"])
    rows.append([ch, "diagrams presence", "OK" if diags else "WARN", f"{len(diags)} mmd"])

    summ = ch_dir / "datasets" / "summary.csv"
    if summ.exists():
        with summ.open(encoding="utf-8") as f:
            import csv as _csv
            hdr = next(_csv.reader(f))
        rows.append([ch, "summary.csv header", "OK" if [h.strip() for h in hdr] == REQ_SUMMARY_HDR else "FAIL", f"found={hdr} expected={REQ_SUMMARY_HDR}"])
    else:
        rows.append([ch, "summary.csv present", "WARN", "missing"])

    if idx.exists():
        txt_idx = idx.read_text(encoding="utf-8")
        rows.append([ch, "index has csv-table", "OK" if "```{csv-table}" in txt_idx else "WARN", ""])
        rows.append([ch, "index has mermaid", "OK" if "```{mermaid}" in txt_idx else "WARN", ""])

    for m in diags:
        txt = m.read_text(encoding="utf-8")
        rows.append([ch, f"{m.name} mermaid init", "OK" if has_mermaid_init(txt) else "FAIL", "missing %%{init:...}%%"])
        stem = m.stem
        facet = f"(facet-{ch}.{stem})="
        i_txt = idx.read_text(encoding="utf-8") if idx.exists() else ""
        rows.append([ch, f"facet anchor for {stem}", "OK" if facet in i_txt else "WARN", "anchor not found in index.md"])

    return rows

def main():
    if not AUTHORING.exists():
        print("[QA] No docs/authoring")
        return 0
    rows = []
    for ch_dir in sorted([p for p in AUTHORING.iterdir() if p.is_dir() and p.name[:2].isdigit()], key=lambda x: x.name):
        rows.extend(check_chapter(ch_dir))
    write_report(rows)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

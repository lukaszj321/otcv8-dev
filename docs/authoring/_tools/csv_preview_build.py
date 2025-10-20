
#!/usr/bin/env python3
# Build lightweight CSV previews for all datasets (first N rows).

from pathlib import Path
import csv, os

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"
PREV = AUTHORING / "_data" / "previews"
PREV.mkdir(parents=True, exist_ok=True)

CSV_PREVIEW_ROWS = int(os.environ.get("CSV_PREVIEW_ROWS", "100"))

def head_copy(p_csv: Path, out_csv: Path, n: int):
    with p_csv.open(encoding="utf-8", newline="") as f_in:
        r = csv.reader(f_in)
        rows = []
        for i, row in enumerate(r):
            rows.append(row)
            if i >= n:
                break
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f_out:
        w = csv.writer(f_out)
        w.writerows(rows)

def main():
    total = 0
    for ch in sorted([p for p in AUTHORING.iterdir() if p.is_dir() and p.name[:2].isdigit()], key=lambda p: p.name):
        ds_dir = ch / "datasets"
        if not ds_dir.exists():
            continue
        for csv_file in ds_dir.glob("*.csv"):
            out = PREV / ch.name / (csv_file.stem + ".head.csv")
            if not out.exists():
                try:
                    head_copy(csv_file, out, CSV_PREVIEW_ROWS)
                    total += 1
                except Exception as e:
                    print(f"[WARN] {csv_file}: {e}")
    print(f"[PREVIEW] generated {total} preview files")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
import os, re, csv, pathlib
LAYOUTS=pathlib.Path('layouts'); OUT=pathlib.Path('docs/authoring/13_layouts/datasets/layouts.csv'); OUT.parent.mkdir(parents=True, exist_ok=True)
rows=[]
if LAYOUTS.exists():
    for p in LAYOUTS.rglob('*.otui'):
        text=p.read_text(encoding='utf-8', errors='ignore')
        inc=set(m.group(1).strip() for m in re.finditer(r'(?i)include\s*:\s*"?([^"\n]+)"?', text))
        rows.append({'layout_id':p.stem,'path':p.as_posix(),'type':'screen','section':'','uses_images[]':'','uses_fonts[]':'','uses_otui[]':'|'.join(sorted(inc)),'notes':''})
hdr=['layout_id','path','type','section','uses_images[]','uses_fonts[]','uses_otui[]','notes']
with OUT.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=hdr); w.writeheader(); [w.writerow(r) for r in rows]
print(f'[layouts_scanner] wrote {len(rows)} rows -> {OUT}')

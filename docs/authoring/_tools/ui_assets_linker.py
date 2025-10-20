#!/usr/bin/env python3
import os, re, csv, pathlib
OTUI_DIRS = [pathlib.Path('modules'), pathlib.Path('layouts')]
ASSET_DIRS = [pathlib.Path('data')]
OUT = pathlib.Path('docs/authoring/11_data/datasets/ui_assets_links.csv'); OUT.parent.mkdir(parents=True, exist_ok=True)
PROP_RE = re.compile(r'^\s*(image|icon|source|texture|sprite|background|atlas)\s*:\s*("?)([^"\n]+)\2', re.M)
rows=[]
for base in OTUI_DIRS:
    if not base.exists(): continue
    for p in base.rglob('*.otui'):
        try: txt=p.read_text(encoding='utf-8', errors='ignore')
        except Exception: continue
        for m in PROP_RE.finditer(txt):
            asset=m.group(3).strip()
            if not asset: continue
            resolved=''
            for ad in ASSET_DIRS:
                cand=ad/asset
                if cand.exists():
                    resolved=cand.as_posix(); break
            rows.append({'widget_id':'','otui_path':p.as_posix(),'asset_type':m.group(1),'asset_path':asset,'resolved_path':resolved,'exists':'yes' if resolved else 'no','notes':''})
hdr=['widget_id','otui_path','asset_type','asset_path','resolved_path','exists','notes']
with OUT.open('w', encoding='utf-8', newline='') as f:
    w=csv.DictWriter(f, fieldnames=hdr); w.writeheader(); [w.writerow(r) for r in rows]
print(f'[ui_assets_linker] wrote {len(rows)} rows -> {OUT}')

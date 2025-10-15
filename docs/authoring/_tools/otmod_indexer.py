#!/usr/bin/env python3
import os, re, csv, pathlib
MODULES=pathlib.Path('modules'); OUT=pathlib.Path('docs/authoring/12_otmod/datasets'); OUT.mkdir(parents=True, exist_ok=True)
mods=[]; exports=[]
for p in MODULES.rglob('*.otmod'):
    t=p.read_text(encoding='utf-8', errors='ignore')
    deps=[]
    for m in re.finditer(r'(?i)depends\s*=\s*\[([^\]]*)\]', t):
        deps=[d.strip().strip('"\'') for d in m.group(1).split(',') if d.strip()]
    has_otui=any((p.parent).rglob('*.otui'))
    has_lua=any((p.parent).rglob('*.lua'))
    has_cpp=any((p.parent).rglob('*.h')) or any((p.parent).rglob('*.hpp')) or any((p.parent).rglob('*.cpp'))
    mods.append({'module':p.stem,'path':p.as_posix(),'has_otui':'yes' if has_otui else 'no','has_lua':'yes' if has_lua else 'no','has_cpp':'yes' if has_cpp else 'no','depends_on':'|'.join(deps)})
for lp in MODULES.rglob('*.lua'):
    text=lp.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'(?m)^\s*(function\s+([A-Za-z_][\w]*)\s*\(|([A-Za-z_][\w]*)\s*=\s*function\s*\(|([A-Za-z_][\w]*)\s*=\s*)', text):
        sym=m.group(2) or m.group(3) or m.group(4)
        if sym:
            exports.append({'module': lp.parts[1] if len(lp.parts)>1 else '', 'symbol': sym,'kind':'function','file':lp.as_posix(),'line': text[:m.start()].count('\n')+1,'doc':''})
def wcsv(p,h,r):
    with open(p,'w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f, fieldnames=h); w.writeheader(); [w.writerow(x) for x in r]
wcsv(OUT/'modules_index.csv', ['module','path','has_otui','has_lua','has_cpp','depends_on'], mods)
wcsv(OUT/'lua_exports.csv', ['module','symbol','kind','file','line','doc'], exports)
print(f'[otmod_indexer] modules={len(mods)} exports={len(exports)}')

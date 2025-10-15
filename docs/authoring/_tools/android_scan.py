#!/usr/bin/env python3
import os, re, csv, pathlib
ROOT=pathlib.Path('android'); OUT=pathlib.Path('docs/authoring/14_android/datasets'); OUT.mkdir(parents=True, exist_ok=True)
def wcsv(p,h,r):
    with open(p,'w',encoding='utf-8',newline='') as f:
        import csv; w=csv.DictWriter(f, fieldnames=h); w.writeheader(); [w.writerow(x) for x in r]
vars=[]; deps=[]; projs=[]
if ROOT.exists():
    for gradle in ROOT.rglob('build.gradle'):
        mod=gradle.parent.as_posix()
        txt=gradle.read_text(encoding='utf-8', errors='ignore')
        abis='|'.join(sorted(set(re.findall(r'abiFilters\s+["\']([^"\']+)["\']', txt))))
        vars.append({'module':mod,'variant':'release','minSdk':'','targetSdk':'','abis':abis,'cmake_flags':''})
        for m in re.finditer(r'implementation\s+["\']([^"\']+)["\']', txt):
            deps.append({'name':m.group(1),'version':'','type':'gradle','path_or_coord':m.group(1)})
        projs.append({'module':mod,'path':mod,'type':'app' if 'applicationId' in txt else 'lib','has_cmake':'yes' if (gradle.parent/'CMakeLists.txt').exists() else 'no'})
wcsv(OUT/'build_variants.csv', ['module','variant','minSdk','targetSdk','abis','cmake_flags'], vars)
wcsv(OUT/'dependencies.csv', ['name','version','type','path_or_coord'], deps)
wcsv(OUT/'projects.csv', ['module','path','type','has_cmake'], projs)
print('[android_scan] datasets written')

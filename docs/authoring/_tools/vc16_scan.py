#!/usr/bin/env python3
import os, re, csv, pathlib
ROOT=pathlib.Path('vc16'); OUT=pathlib.Path('docs/authoring/15_vc16/datasets'); OUT.mkdir(parents=True, exist_ok=True)
def wcsv(p,h,r):
    with open(p,'w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f, fieldnames=h); w.writeheader(); [w.writerow(x) for x in r]
projects=[]; defines=[]
if ROOT.exists():
    for sln in ROOT.rglob('*.sln'):
        for line in sln.read_text(encoding='utf-8', errors='ignore').splitlines():
            m=re.match(r'Project\(".*"\)\s*=\s*"([^"]+)"\s*,\s*"([^"]+)"', line)
            if m:
                projects.append({'project':m.group(1),'path':(sln.parent/m.group(2)).as_posix(),'type':'vcxproj','platform':'','toolset':''})
    for vcx in ROOT.rglob('*.vcxproj'):
        txt=vcx.read_text(encoding='utf-8', errors='ignore')
        for m in re.finditer(r'<PreprocessorDefinitions>([^<]+)</PreprocessorDefinitions>', txt):
            for d in m.group(1).split(';'):
                d=d.strip()
                if d and d != '%(PreprocessorDefinitions)':
                    defines.append({'project':vcx.stem,'config':'','define':d})
wcsv(OUT/'projects.csv', ['project','path','type','platform','toolset'], projects)
wcsv(OUT/'defines.csv', ['project','config','define'], defines)
print('[vc16_scan] datasets written')

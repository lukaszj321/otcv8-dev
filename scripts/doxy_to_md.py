#!/usr/bin/env python3
import sys, os, xml.etree.ElementTree as ET
from collections import defaultdict

if len(sys.argv) != 2:
    print("Użycie: doxy_to_md.py <sciezka_do_xml_doxygena>", file=sys.stderr)
    sys.exit(1)

xml_dir = sys.argv[1]
index_xml = os.path.join(xml_dir, "index.xml")
if not os.path.isfile(index_xml):
    print(f"Brak {index_xml}", file=sys.stderr)
    sys.exit(2)

# Zbierz wszystkie "compounds" (klasy/struktury/namespaces/pliki)
idx = ET.parse(index_xml).getroot()
ns = defaultdict(list)     # namespace -> [(signature, brief, file, line)]
classes = defaultdict(list) # ClassName -> [(signature, brief, file, line)]
files = defaultdict(list)   # filename -> [(signature, brief, file, line)]

def get_text(elem):
    if elem is None:
        return ""
    return "".join(elem.itertext()).strip()

def load_compound(refid):
    path = os.path.join(xml_dir, refid + ".xml")
    if not os.path.isfile(path):
        return None
    return ET.parse(path).getroot()

def member_signature(m):
    # Doxygen: <definition> + <argsstring>, np. "void Game::requestQuestLog" + "()"
    definition = get_text(m.find("definition"))
    args = get_text(m.find("argsstring"))
    sig = (definition + (args or "")).strip()
    # Lokalizacja
    loc = m.find("location")
    fname = loc.get("file") if loc is not None else ""
    line = loc.get("line") if loc is not None else ""
    # Krótki opis
    brief = get_text(m.find("briefdescription"))
    return sig, brief, fname, line

compounds = []
for c in idx.findall("compound"):
    kind = c.get("kind", "")
    refid = c.get("refid", "")
    name = get_text(c.find("name"))
    compounds.append((kind, refid, name))

for kind, refid, name in compounds:
    root = load_compound(refid)
    if root is None:
        continue

    # Przejdź po memberdef kind="function"
    for m in root.findall(".//memberdef[@kind='function']"):
        prot = m.get("prot", "public")
        # filtruj tylko public/protected jeśli chcesz; tu bierzemy wszystko:
        sig, brief, fname, line = member_signature(m)

        # Spróbuj określić kontekst (namespace/klasa/plik)
        # Dla klas:
        # compounddef/kind == "class"/"struct" => chcemy etykietę klasy
        # Dla namespace:
        # compounddef/kind == "namespace"
        cdef = root.find("compounddef")
        ckind = cdef.get("kind") if cdef is not None else ""
        cname = get_text(cdef.find("compoundname")) if cdef is not None else ""

        if ckind in ("class", "struct"):
            classes[cname].append((sig, brief, fname, line))
        elif ckind == "namespace":
            ns[cname].append((sig, brief, fname, line))
        else:
            files[os.path.basename(fname)].append((sig, brief, fname, line))

# OUTPUT MARKDOWN
print("# C++ API — pełna lista funkcji\n")
print("> Generowane automatycznie z Doxygen XML (EXTRACT_ALL=YES).")
print("> Jeśli czegoś brakuje, sprawdź wzorce plików w `gen_api_cpp.sh`.\n")

# Namespaces
if ns:
    print("## Namespaces\n")
    for n in sorted(ns.keys()):
        print(f"### {n}\n")
        for sig, brief, fname, line in sorted(ns[n], key=lambda x: x[0]):
            print(f"- `{sig}`  ")
            if brief:
                print(f"  - {brief}")
            if fname:
                print(f"  - _{fname}:{line}_")
        print()

# Classes
if classes:
    print("## Klasy / Struktury\n")
    for cls in sorted(classes.keys()):
        print(f"### {cls}\n")
        for sig, brief, fname, line in sorted(classes[cls], key=lambda x: x[0]):
            print(f"- `{sig}`  ")
            if brief:
                print(f"  - {brief}")
            if fname:
                print(f"  - _{fname}:{line}_")
        print()

# Files (funkcje „globalne”/poza klasami/namespaces)
if files:
    print("## Funkcje globalne (wg plików)\n")
    for fn in sorted(files.keys()):
        print(f"### {fn}\n")
        for sig, brief, fname, line in sorted(files[fn], key=lambda x: x[0]):
            print(f"- `{sig}`  ")
            if brief:
                print(f"  - {brief}")
            if fname:
                print(f"  - _{fname}:{line}_")
        print()

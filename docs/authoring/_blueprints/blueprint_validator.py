
import csv, re
from typing import List

BOOL_TRUE = {"true","1","yes","y","t"}
BOOL_FALSE = {"false","0","no","n","f"}

ID_RX = re.compile(r"^[a-z][a-z0-9_]*$")
ICON_RX = re.compile(r"^(/images/.*|icon-[a-z0-9\-_]+)$")

def parse_bool(value: str):
    if value is None or value == "":
        return None
    v = str(value).strip().lower()
    if v in BOOL_TRUE: return True
    if v in BOOL_FALSE: return False
    raise ValueError(f"Invalid bool: {value}")

def parse_list(value: str):
    if value is None or value == "":
        return []
    return [x.strip() for x in str(value).split(";") if x.strip()]

def parse_int(value: str):
    if value is None or value == "": return None
    try:
        return int(str(value).strip())
    except Exception:
        raise ValueError(f"Invalid int: {value}")

def validate_icon(value: str):
    if value is None or value == "": return None
    v = str(value).strip()
    if not ICON_RX.match(v):
        raise ValueError("Invalid icon reference; use '/images/...' or 'icon-*' alias")

def validate_module_csv(path: str) -> List[str]:
    required = {"module","path","sandboxed","reloadable","scripts","onLoad","onUnload"}
    allowed_policies = {"prefer","skip","warn", ""}
    messages = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            missing = [c for c in required if (row.get(c) is None or row.get(c)=="")]
            if missing:
                messages.append(f"{path}: line {i}: missing required: {', '.join(missing)}")
            for b in ("sandboxed","reloadable","public_api","bot_support"):
                try: _ = parse_bool(row.get(b))
                except Exception as e: messages.append(f"{path}: line {i}: {e}")
            for lst in ("scripts","dependencies","load_later","otui_files","assets_fonts","assets_images","api_functions","hotkeys"):
                _ = parse_list(row.get(lst))
            for integer in ("panel_order",):
                try: _ = parse_int(row.get(integer))
                except Exception as e: messages.append(f"{path}: line {i}: {e}")
            policy = (row.get("hotkeys_conflict_policy") or "").strip().lower()
            if policy not in allowed_policies:
                messages.append(f"{path}: line {i}: hotkeys_conflict_policy must be one of prefer|skip|warn")
            try:
                validate_icon(row.get("panel_icon"))
            except Exception as e:
                messages.append(f"{path}: line {i}: {e}")
    return messages

def validate_widget_csv(path: str) -> List[str]:
    required = {"widget_id","class","source_file"}
    messages = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        seen_ids = set()
        for i, row in enumerate(reader, start=2):
            missing = [c for c in required if (row.get(c) is None or row.get(c)=="")]
            if missing:
                messages.append(f"{path}: line {i}: missing required: {', '.join(missing)}")
            for b in ("i18n_required",):
                try: _ = parse_bool(row.get(b))
                except Exception as e: messages.append(f"{path}: line {i}: {e}")
            # lint candidate instance id if present in notes (optional convention: id:<id_name>)
            notes = (row.get("notes") or "")
            m = re.search(r"id:([a-z0-9_]+)", notes)
            if m:
                cid = m.group(1)
                if not ID_RX.match(cid):
                    messages.append(f"{path}: line {i}: invalid id format in notes 'id:{cid}'")
                if cid in seen_ids:
                    messages.append(f"{path}: line {i}: duplicate id '{cid}'")
                seen_ids.add(cid)
    return messages

def validate_vbot_csv(path: str) -> List[str]:
    required = {"module","macro_id","title","interval_ms","action_lua"}
    messages = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            missing = [c for c in required if (row.get(c) is None or row.get(c)=="")]
            if missing:
                messages.append(f"{path}: line {i}: missing required: {', '.join(missing)}")
            for b in ("enabled_by_default",):
                try: _ = parse_bool(row.get(b))
                except Exception as e: messages.append(f"{path}: line {i}: {e}")
            for integer in ("interval_ms","panel_order"):
                try:
                    _ = int(row.get(integer) or "0")
                except Exception:
                    messages.append(f"{path}: line {i}: {integer} must be int")
            try:
                validate_icon(row.get("macro_icon"))
            except Exception as e:
                messages.append(f"{path}: line {i}: {e}")
    return messages

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python blueprint_validator.py <module_csv> <widget_csv> <vbot_csv>")
        sys.exit(2)
    msgs = []
    msgs += validate_module_csv(sys.argv[1])
    msgs += validate_widget_csv(sys.argv[2])
    msgs += validate_vbot_csv(sys.argv[3])
    if msgs:
        print("VALIDATION: FAIL")
        for m in msgs:
            print("-", m)
        sys.exit(1)
    else:
        print("VALIDATION: OK")
        sys.exit(0)


import csv, os, json, re
from pathlib import Path
from typing import Dict, List

ID_RX = re.compile(r"^[a-z][a-z0-9_]*$")
ICON_RX = re.compile(r"^(/images/.*|icon-[a-z0-9\-_]+)$")

def parse_bool(v):
    if v is None or v == "": return None
    s = str(v).strip().lower()
    return s in {"true","1","yes","y","t"}

def parse_list(v):
    if v is None or v == "": return []
    return [x.strip() for x in str(v).split(";") if x.strip()]

def load_csv(path: str):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def ensure_id(base: str, taken: set) -> str:
    base = base.lower()
    base = re.sub(r"[^a-z0-9_]", "_", base)
    if not base or not base[0].isalpha():
        base = "w_" + base
    if not ID_RX.match(base):
        base = "w_" + re.sub(r"[^a-z0-9_]", "", base)
    cand = base
    i = 2
    while cand in taken:
        cand = f"{base}_{i}"
        i += 1
    taken.add(cand)
    return cand

def make_otmod(module_row: Dict) -> str:
    deps_list = parse_list(module_row.get("dependencies"))
    deps = "\n".join(["    - " + d for d in deps_list]) if deps_list else "    # none"
    scripts = parse_list(module_row.get("scripts"))
    scripts_arr = "[ " + ", ".join(scripts) + " ]" if scripts else "[]"
    sandboxed = "true" if parse_bool(module_row.get("sandboxed")) else "false"
    reloadable = "true" if parse_bool(module_row.get("reloadable")) else "false"
    author = module_row.get("author") or "unknown"
    website = module_row.get("website") or ""
    description = module_row.get("description") or ""
    onLoad = module_row.get("onLoad") or "init()"
    onUnload = module_row.get("onUnload") or "terminate()"
    name = module_row.get("module")
    lines = []
    lines.append("Module")
    lines.append("  name: " + name)
    lines.append("  description: " + description)
    lines.append("  author: " + author)
    lines.append("  website: " + website)
    lines.append("  sandboxed: " + sandboxed)
    lines.append("  reloadable: " + reloadable)
    lines.append("  scripts: " + scripts_arr)
    lines.append("  @onLoad: " + onLoad)
    lines.append("  @onUnload: " + onUnload)
    lines.append("  dependencies:")
    lines.append(deps)
    return "\n".join(lines)

def make_module_lua(module_row: Dict) -> str:
    name = module_row.get("module")
    api_funcs = parse_list(module_row.get("api_functions"))
    hotkeys = parse_list(module_row.get("hotkeys"))
    hotkeys_ctx = (module_row.get("hotkeys_context") or "global").strip()
    hotkeys_policy = (module_row.get("hotkeys_conflict_policy") or "warn").strip()
    lua_lines = []
    lua_lines.append("-- " + name + ".lua")
    lua_lines.append("-- Auto-generated scaffold\n")
    lua_lines.append("local M = {}\n")
    lua_lines.append("function init()\n")
    lua_lines.append("  -- init UI, storage\n")
    lua_lines.append("  -- NOTE: attach UI via g_ui.loadUI('modules/" + name + "/" + name + ".otui')\n")
    if hotkeys:
        lua_lines.append("  -- Hotkeys (" + hotkeys_ctx + ", policy=" + hotkeys_policy + ")")
        for hk in hotkeys:
            lua_lines.append("  -- bind hotkey: " + hk + " -> add handler here")
    lua_lines.append("end\n")
    lua_lines.append("\nfunction terminate()\n  -- cleanup\nend\n")
    if api_funcs:
        for f in api_funcs:
            fname = f.split("(")[0].strip()
            if fname:
                lua_lines.append("\nfunction M." + fname + " end")
    else:
        lua_lines.append("\nfunction M.toggleWindow() end")
    lua_lines.append("\nreturn M\n")
    return "\n".join(lua_lines)

def make_main_otui(module_row: Dict, widget_rows: List[Dict]) -> str:
    name = module_row.get("module")
    contents_id = name + "_contents"
    taken_ids = {name + "_window", contents_id}
    # Compose window + contents
    lines = []
    lines.append("MiniWindow")
    lines.append("  # GEOMETRIA")
    lines.append("  id: " + name + "_window")
    lines.append("  width: 240")
    lines.append("  height: 160\n")
    lines.append("  # STYL")
    lines.append("  text: tr('" + name + "')")
    lines.append("  @onClose: toggle\n")
    lines.append("  MiniWindowContents")
    lines.append("    id: " + contents_id)
    lines.append("    # AUTO-INJECTED WIDGET INSTANCES BELOW")
    # Inject widget instances if they belong to this module (source_file points to this module's .otui)
    module_otui_path = "modules/" + name + "/" + name + ".otui"
    for w in widget_rows:
        if (w.get("source_file") or "").strip() == module_otui_path:
            klass = w.get("class") or "UIWidget"
            wid_base = (w.get("widget_id") or "widget").split("/")[-1].lower()
            inst_id = ensure_id(name + "_" + wid_base, taken_ids)
            lines.append("    " + klass)
            # GEOMETRIA
            h = (w.get("height") or "").strip()
            w_width = (w.get("width") or "").strip()
            lines.append("      # GEOMETRIA")
            lines.append("      id: " + inst_id)
            if w_width: lines.append("      width: " + str(w_width))
            if h: lines.append("      height: " + str(h))
            anchors = (w.get("anchors") or "").strip()
            if anchors:
                for pair in anchors.split(";"):
                    pair = pair.strip()
                    if not pair: continue
                    lines.append("      anchors." + pair.replace(":", ": "))
            margins = (w.get("margins") or "").strip()
            if margins:
                for pair in margins.split(";"):
                    pair = pair.strip()
                    if not pair: continue
                    lines.append("      margin-" + pair.replace(":", ": "))
            paddings = (w.get("paddings") or "").strip()
            if paddings:
                for pair in paddings.split(";"):
                    pair = pair.strip()
                    if not pair: continue
                    lines.append("      padding-" + pair.replace(":", ": "))
            # STYL
            lines.append("      # STYL")
            font = (w.get("font") or "").strip()
            if font: lines.append("      font: " + font)
            text_align = (w.get("text_align") or "").strip()
            if text_align: lines.append("      text-align: " + text_align)
            img = (w.get("image_source") or "").strip()
            if img: lines.append("      image-source: " + img)
            # ZACHOWANIE
            lines.append("      # ZACHOWANIE")
            onclick = (w.get("onClick") or "").strip()
            if onclick: lines.append("      @onClick: " + onclick)
    return "\n".join(lines)

def make_vbot_macros_lua(macros: List[Dict], module_row: Dict) -> str:
    out = ["-- Auto-generated vBot macros", ""]
    panel_id = module_row.get("bot_panel_id") or ""
    macro_default_group = module_row.get("macro_group") or ""
    for m in macros:
        try:
            interval = int(m.get("interval_ms") or 1000)
        except Exception:
            interval = 1000
        title = m.get("title") or m.get("macro_id")
        cond = (m.get("condition_lua") or "").strip()
        action = (m.get("action_lua") or "").strip()
        enabled = parse_bool(m.get("enabled_by_default"))
        enabled_str = "true" if enabled else "false"
        group = m.get("macro_group") or macro_default_group
        order = m.get("panel_order") or ""
        icon = m.get("macro_icon") or ""
        # icon lint
        if icon and not ICON_RX.match(icon):
            icon = "icon-invalid"
        out.append("-- panel: " + (m.get("panel_id") or panel_id) + " | group: " + group + " | order: " + str(order) + " | icon: " + icon)
        out.append("macro(" + str(interval) + ", '" + title + "', function()")
        if cond:
            out.append("  if (function() " + cond + " end)() then")
            out.append("    " + action)
            out.append("  end")
        else:
            out.append("  " + action)
        out.append("end, " + enabled_str + ")\n")
    return "\n".join(out)

def main(module_csv, widget_csv, vbot_csv, out_dir):
    modules = load_csv(module_csv)
    widgets = load_csv(widget_csv)
    vmacros = load_csv(vbot_csv)

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    for row in modules:
        name = row["module"]
        mod_dir = out / name
        mod_dir.mkdir(parents=True, exist_ok=True)

        # .otmod
        (mod_dir / (name + ".otmod")).write_text(make_otmod(row), encoding="utf-8")

        # .lua
        scripts = parse_list(row.get("scripts"))
        main_script = scripts[0] if scripts else name
        (mod_dir / (main_script + ".lua")).write_text(make_module_lua(row), encoding="utf-8")

        # .otui (main, with injected widgets)
        (mod_dir / (name + ".otui")).write_text(make_main_otui(row, widgets), encoding="utf-8")

        # vBot macros
        if parse_bool(row.get("bot_support")):
            macros_for_mod = [m for m in vmacros if (m.get("module")==name)]
            if macros_for_mod:
                macros_lua = make_vbot_macros_lua(macros_for_mod, row)
                (mod_dir / (name + "_macros.lua")).write_text(macros_lua, encoding="utf-8")

    # widgets index (for IDE consumption)
    (out / "WIDGETS_INDEX.json").write_text(
        json.dumps({"widgets": widgets}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 5:
        print("Usage: python scaffold_from_csv.py <module_csv> <widget_csv> <vbot_csv> <out_dir>")
        sys.exit(2)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

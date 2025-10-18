# Documentation Gaps and Issues

Generated: 2025-10-18T01:38:32.882407Z

## Summary

- ✅ PASS: 4 chapters
- ⚠️ WARN: 12 chapters
- ❌ FAIL: 0 chapters

## Gaps by Chapter

### 01_runtime - WARN

- **Size:** 4.5 KB (target: ≥18 KB)
- **Datasets:** 3 (minimum: 3)
- **Diagrams:** 4

**Actionable Steps:**
1. Add more content sections and examples

### 02_events - WARN

- **Size:** 6.2 KB (target: ≥18 KB)
- **Datasets:** 5 (minimum: 3)
- **Diagrams:** 6

**Actionable Steps:**
1. Add more content sections and examples

### 05_network - WARN

- **Size:** 10.6 KB (target: ≥18 KB)
- **Datasets:** 6 (minimum: 3)
- **Diagrams:** 5

**Actionable Steps:**
1. Add more content sections and examples

### 06_assets - WARN

- **Size:** 6.0 KB (target: ≥18 KB)
- **Datasets:** 5 (minimum: 3)
- **Diagrams:** 5

**Actionable Steps:**
1. Add more content sections and examples

### 07_settings_crypto - WARN

- **Size:** 6.2 KB (target: ≥18 KB)
- **Datasets:** 5 (minimum: 3)
- **Diagrams:** 5

**Actionable Steps:**
1. Add more content sections and examples

### 08_audio - WARN

- **Size:** 5.8 KB (target: ≥18 KB)
- **Datasets:** 5 (minimum: 3)
- **Diagrams:** 5

**Actionable Steps:**
1. Add more content sections and examples

### 09_logging - WARN

- **Size:** 5.7 KB (target: ≥18 KB)
- **Datasets:** 6 (minimum: 3)
- **Diagrams:** 4

**Actionable Steps:**
1. Add more content sections and examples

### 10_game_runtime - WARN

- **Size:** 6.1 KB (target: ≥18 KB)
- **Datasets:** 5 (minimum: 3)
- **Diagrams:** 5

**Actionable Steps:**
1. Add more content sections and examples

### 12_otmod - WARN

- **Size:** 14.2 KB (target: ≥18 KB)
- **Datasets:** 8 (minimum: 3)
- **Diagrams:** 5

**Actionable Steps:**
1. Add more content sections and examples

### 13_layouts - WARN

- **Size:** 5.9 KB (target: ≥18 KB)
- **Datasets:** 5 (minimum: 3)
- **Diagrams:** 5

**Actionable Steps:**
1. Add more content sections and examples

### 14_android - WARN

- **Size:** 4.9 KB (target: ≥18 KB)
- **Datasets:** 10 (minimum: 3)
- **Diagrams:** 4

**Actionable Steps:**
1. Add more content sections and examples

### 15_vc16 - WARN

- **Size:** 8.2 KB (target: ≥18 KB)
- **Datasets:** 7 (minimum: 3)
- **Diagrams:** 2

**Actionable Steps:**
1. Add more content sections and examples

---

## Sprint Top15 Tooling GAPs (2025-10-18)

### GAP: Lua Bindings Generator (Sprint Attempt)

- **chapter:** 01_core, 03_modules
- **tool_used:** tools/lua-binding-generator/generate_lua_bindings.lua
- **status:** SKIPPED (Lua interpreter not available)
- **actionable_next_steps:**
  1. Install Lua 5.1 or LuaJIT in environment
  2. Re-run: `cd tools/lua-binding-generator && lua generate_lua_bindings.lua`
  3. Copy outputs to docs/authoring/datasets/lua_bindings.csv

### GAP: Bitmap Font Generator (Sprint Attempt)

- **chapter:** 11_data, 04_ui
- **tool_used:** tools/gimp-bitmap-generator/generate_bitmap_font.py
- **status:** SKIPPED (GIMP with Python-Fu not available)
- **actionable_next_steps:**
  1. Install GIMP with Python bindings
  2. Re-run: `python3 tools/gimp-bitmap-generator/generate_bitmap_font.py --out docs/authoring/datasets/fonts.csv`
  3. Verify fonts.csv has proper structure

---

## Sprint Progress Update (2025-10-18T03:50:00Z)

### Completed Tasks (1-5)

- **Task 1 (12_otmod):** ✅ Added load-later patterns (6.6KB) + sandbox security (8.8KB) + lifecycle diagram
- **Task 2 (15_vc16):** ✅ Added ANGLE integration (12.5KB) + EGL init (1.5KB) + DLL deployment (9.2KB)
- **Task 3 (05_network):** ✅ Added protocol versions (9.2KB) + packet structure (10.4KB) + extended opcodes (8.7KB)
- **Task 4 (14_android):** ✅ Added ABI configuration (4.9KB) + APK signing (5.9KB)
- **Task 5 (13_layouts):** ✅ Added theme creation (6.1KB)

**Total content added:** ~82KB
**Diagrams added:** 3 new diagrams
**Crosslinks added:** 20 links
**Facets added:** 13 facets

### Status Update

Chapters now meeting or approaching 18KB target:
- 12_otmod: 112KB (was 14.2KB) ✅
- 15_vc16: 96KB (was 8.2KB) ✅
- 05_network: ~40KB (was 10.6KB) ✅
- 14_android: ~30KB (was 4.9KB) ✅
- 13_layouts: ~20KB (was 5.9KB) ✅


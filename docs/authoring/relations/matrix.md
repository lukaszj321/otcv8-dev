# Relations Matrix

This matrix shows relationships between chapters.

**Legend:**
- **uses** - Uses functionality from
- **calls** - Calls functions from
- **emits** - Emits events to
- **handles** - Handles events from
- **renders** - Renders components of
- **owns** - Owns data/assets of
- **logs** - Logs to
- **processes** - Processes data from
- **packages** - Packages content from
- **compiles** - Compiles code from
- **overrides** - Overrides assets from
- **loads** - Loads modules from
- **updates** - Updates state of

## Matrix

| From \ To | 01_core | 01_runtime | 02_events | 03_modules | 04_ui | 05_network | 06_assets | 07_settings_crypto | 08_audio | 09_logging | 10_game_runtime | 11_data | 12_otmod | 13_layouts | 14_android | 15_vc16 |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| **01_core** | - |  | emits | uses | renders |  |  |  |  | logs |  |  |  |  |  |  |
| **01_runtime** | uses | - | handles |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **02_events** |  |  | - | emits | handles |  |  |  |  |  |  |  |  |  |  |  |
| **03_modules** | calls |  | emits | - | uses |  |  |  |  |  |  |  |  |  |  |  |
| **04_ui** |  |  | emits |  | - |  |  |  |  |  |  | uses |  | uses |  |  |
| **05_network** | uses |  | emits |  |  | - |  |  |  | logs |  |  |  |  |  |  |
| **06_assets** |  |  |  |  | renders |  | - |  |  |  |  | processes |  |  |  |  |
| **07_settings_crypto** | uses |  |  |  |  | uses |  | - |  |  |  |  |  |  |  |  |
| **08_audio** |  |  | handles |  |  |  |  |  | - |  |  | uses |  |  |  |  |
| **09_logging** | uses |  |  |  |  |  |  |  |  | - |  |  |  |  |  |  |
| **10_game_runtime** |  | uses | emits |  | updates |  |  |  |  |  | - |  |  |  |  |  |
| **11_data** |  |  |  |  | owns |  |  |  |  |  |  | - |  | owns |  |  |
| **12_otmod** |  |  |  | loads | uses |  |  |  |  |  |  | uses | - |  |  |  |
| **13_layouts** |  |  |  |  | uses |  |  |  |  |  |  | overrides |  | - |  |  |
| **14_android** |  |  |  |  |  |  |  |  |  |  |  | packages | packages |  | - |  |
| **15_vc16** | compiles |  |  |  |  |  |  |  |  |  |  |  |  |  |  | - |


## Statistics

- Total chapters: 16
- Total relations: 37
- Relation types: 13

## Relation Types Distribution

- **uses**: 14
- **emits**: 6
- **handles**: 3
- **renders**: 2
- **logs**: 2
- **owns**: 2
- **packages**: 2
- **calls**: 1
- **processes**: 1
- **updates**: 1
- **loads**: 1
- **overrides**: 1
- **compiles**: 1

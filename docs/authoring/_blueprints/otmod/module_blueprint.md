---
title: "OTMOD Module Blueprint"
updated: "2025-10-14T00:00:00Z"
---

# OTMOD Module Blueprint

Minimalny, re-używalny szablon do opisania modułu.

## Meta

- **module:** `game_skills`
- **path:** `modules/game_skills`
- **sandboxed:** `true`

## Manifest (OTMOD)

```otmod
Module
  name: game_skills
  description: Manage skills window
  author: baxnie, edubart
  website: https://github.com/edubart/otclient
  sandboxed: true
  scripts: [ skills ]
  @onLoad: init()
  @onUnload: terminate()
  dependencies:
    - game_interface
```

## Lifecycle i powiązania

- `@onLoad` -> `init()`
- `@onUnload` -> `terminate()`
- **OTUI**: `modules/game_skills/skills.otui` (MiniWindow, SkillButton…)

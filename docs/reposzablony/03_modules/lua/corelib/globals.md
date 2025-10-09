---
doc_id: "lua-spec-5a6d71028869"
source_path: "corelib/globals.lua"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:57Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: globals.lua"
summary: "Dokumentacja modułu Lua dla corelib/globals.lua"
tags: ["lua", "module", "otclient"]
---

# corelib/globals.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla globals.

## Functions

### `scheduleEvent(callback, delay)`

@} @docfuncs @{

**Parametry:**

- `callback`
- `delay`

### `addEvent(callback, front)`

**Parametry:**

- `callback`
- `front`

### `cycleEvent(callback, interval)`

**Parametry:**

- `callback`
- `interval`

### `periodicalEvent(eventFunc, conditionFunc, delay, autoRepeatDelay)`

**Parametry:**

- `eventFunc`
- `conditionFunc`
- `delay`
- `autoRepeatDelay`

### `func()`

### `removeEvent(event)`

**Parametry:**

- `event`

## Events/Callbacks

### `getRootWidget`

@docvars @{ root widget

**Wywołanie:** `rootWidget = g_ui.getRootWidget()`

### `event`

**Wywołanie:** `function addEvent(callback, front)`

### `event`

**Wywołanie:** `local event = g_dispatcher.addEvent(desc, callback, front)`

### `ditionFunc`

**Wywołanie:** `if conditionFunc and not conditionFunc() then`

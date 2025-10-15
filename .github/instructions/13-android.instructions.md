
---
name: android
applyTo:
  - "android/**/*"
read:
  - "android/**"
  - "src/**"
write:
  - "docs/authoring/14_android/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# Android — Instructions

## Goal
Zindeksuj artefakty Android: Manifest/permissions, Gradle moduły, ABI, CMake/NDK integrację, outputs.

## Output
- `docs/authoring/14_android/index.md` (intro, TOC)
- `docs/authoring/14_android/datasets/android_manifest.csv`
  - `path,package,min_sdk,target_sdk,permissions[],activities[],services[],receivers[]`
- `docs/authoring/14_android/datasets/android_build.csv`
  - `module,gradle_path,abi[],cmake_args[],ndk_version,outputs[],notes`
- `diagrams/*.mmd`: pipeline builda (graph TD) + zależności modułów (opcjonalnie)
- Crosslinks do `01_core`, `10_game_runtime`.

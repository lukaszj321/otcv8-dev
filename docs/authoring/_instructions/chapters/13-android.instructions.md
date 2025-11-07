---
name: "android"
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

outputs:
  - "docs/authoring/14_android/index.md"
  - "docs/authoring/14_android/datasets/android_manifest.csv"
  - "docs/authoring/14_android/datasets/android_build.csv"
  - "docs/authoring/14_android/diagrams/build_pipeline.mmd"
---

# Android — Instructions

## Goal
Zindeksuj artefakty Android: Manifest/permissions, moduły Gradle, ABI, CMake/NDK, outputs.

## Datasets
- `android_manifest.csv` (kolumny):
  - `path,package,min_sdk,target_sdk,permissions[],activities[],services[],receivers[]`
- `android_build.csv` (kolumny):
  - `module,gradle_path,abi[],cmake_args[],ndk_version,outputs[],notes`
- Uwaga: pola z `[]` serializuj jako **JSON arrays** w CSV (np. `["arm64-v8a","x86_64"]`).

## Diagrams (opcjonalnie)
- `diagrams/build_pipeline.mmd` (flowchart „graph TD”).
- 1. linia wymagana:
```

%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%

```

## Crosslinks
- Dodaj xref do: `01_core` (C++/NDK) i `10_game_runtime` (artefakty uruchomieniowe).

## Index
- `index.md`: frontmatter, `{toctree}` (hidden), `{contents} :local:`,
`{csv-table}` dla obu CSV, `{mermaid}` dla pipeline (jeśli wygenerowany).

## Notes
- Manifesty parsuj z `AndroidManifest.xml`; Gradle: `settings.gradle`, `build.gradle*`.
- ABI/NDK wyciągaj z `externalNativeBuild/cmake`, `abiFilters`, `ndkVersion`.
- `outputs` zbierz z katalogów build/outputs (apk/aab/so).

## Acceptance
- [ ] Wygenerowano `index.md`
- [ ] Oba CSV istnieją i mają wskazane kolumny (listy jako JSON)
- [ ] (Jeśli diagram) Mermaid renderuje się (init w 1. linii, ASCII strzałki)
- [ ] Crosslinki do `01_core` i `10_game_runtime` istnieją

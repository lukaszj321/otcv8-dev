---
chapter: "14_android"
slug: "14_android"
title: "Android — struktura projektu, build i zasoby (OTClient v8)"
status: "agent_ready"
doc_id: "authoring.14_android"
language: "pl"
last_sync_iso: "2025-10-15T16:30:48.251568"
tags: ["otclient","android","ndk","jni","gradle","assets","rag"]
artifacts:
  datasets:
    - id: "android_project_index"
      file: "android_project_index.csv"
      headers: ["path", "kind", "summary", "notes"]
      facet: "14_android.android_project_index"
    - id: "android_libs"
      file: "android_libs.csv"
      headers: ["lib", "arch", "path", "version", "notes"]
      facet: "14_android.android_libs"
    - id: "android_assets"
      file: "android_assets.csv"
      headers: ["asset", "target_path", "origin", "size", "notes"]
      facet: "14_android.android_assets"
  diagrams:
    - id: "android_build"
      file: "android_build.mmd"
      facet: "14_android.android_build"
    - id: "android_tree"
      file: "android_tree.mmd"
      facet: "14_android.android_tree"
xrefs:
  - to: "11_data.images"
    type: "packages"
    evidence: "docs/authoring/14_android/datasets/android_assets.csv"
  - to: "15_vc16.angle_libs"
    type: "links"
    evidence: "docs/authoring/14_android/datasets/android_libs.csv"
---

# Android — struktura projektu, build i zasoby (OTClient v8)

**Cel rozdziału:** opisać strukturę katalogu `android/**`, artefakty NDK/JNI, pakowanie zasobów `data/**` do `assets/`, oraz zależności zewnętrzne (np. `SDL2`, ANGLE/ES). Rozdział zawiera **kontrakty datasetów** i diagramy procesu build.

```{contents}
:local:
:depth: 2
```

:::{admonition} Uwaga
Androidowy projekt często bywa mirrorowany z desktopu. Różnice to **ABI**, **rozmiary tekstur**, **uprawnienia** i **touch UI**. Pamiętaj o spójności z layoutem `mobile`.
:::

## Struktura `android/` (przykład)

```
android/
  AndroidManifest.xml
  build.xml | build.gradle
  assets/                 # spakowane data/** (część)
  res/                    # zasoby Android (xml, mipmap, layouty)
  include/                # nagłówki do JNI/NDK (jeśli mirrorowane)
  lib/ lib64/             # biblioteki .so lub .a per-ABI
  src/com/otclientv8/     # kod Java/Kotlin glue
  otclientv8.sln          # (opcjonalne) legacy/VS integration
  run_android.bat         # helper
```

**Cele agenta:** zbuduj tablice `android_project_index.csv` (mapa plików), `android_libs.csv` (biblioteki), `android_assets.csv` (mapowanie assetów).

## Kontrakty datasetów

### `android_project_index.csv`
| path | kind | summary | notes |
|---|---|---|---|

### `android_libs.csv`
| lib | arch | path | version | notes |
|---|---|---|---|---|

**Architektury:** `armeabi-v7a`, `arm64-v8a`, `x86`, `x86_64`.  
**Uwagi:** dopisz czy biblioteka jest static/dynamic (`.a`/`.so`) i zależności (np. `SDL2`, `GLESv2`).

### `android_assets.csv`
| asset | target_path | origin | size | notes |
|---|---|---|---|---|

`origin` wskazuje **źródło** w repo (`data/**` lub `layouts/**`), `target_path` — miejsce w APK (np. `assets/data/images/...`).

## Pipeline build

### Diagram: android_build
*Facet:* [`14_android.android_build`](#facet-14_android.android_build)

```{mermaid}
%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%
flowchart LR
   A[C++/Lua sources] --> B[NDK Build/JNI]
   B --> C[.so per-ABI]
   D[data/** + layouts/**] --> E[Assets packer]
   E --> F[assets/* in APK]
   C --> G[Gradle assembleRelease]
   F --> G
   G --> H[APK/AAB]
```

### Diagram: android_tree
*Facet:* [`14_android.android_tree`](#facet-14_android.android_tree)

```{mermaid}
%{init: { 'theme': 'neutral' } }%
graph TD
  ANDROID[android/] --> MANIFEST[AndroidManifest.xml]
  ANDROID --> ASSETS[assets/]
  ANDROID --> RES[res/]
  ANDROID --> LIB[lib*/]
  ANDROID --> SRC[src/com/otclientv8/]
  click ASSETS "./../11_data/index.html" "Zasoby bazowe"
```

## Heurystyki ekstrakcji (Agent)

- **Index plików:** rekurencyjnie przejdź `android/**`, klasyfikuj `kind` (`manifest|java|gradle|asset|lib|hdr`).
- **Biblioteki:** skanuj `lib*/**/*.(so|a)` → `android_libs.csv`, parsuj `arch` z ścieżki.
- **Pakowanie assetów:** odwzoruj `data/**`/`layouts/**` do `assets/` z zachowaniem struktury; zapisz `origin` i `target_path`.

## Hooki platformowe

- **Wejście dotykowe** → mapowane na eventy UI (klik/pinch/drag).  
- **Czujniki** (opcjonalnie) → expose do Lua (np. akcelerometr).  
- **Uprawnienia** → Internet/storage (zależnie od modułów).

:::{note}
Rozdział **nie** zmienia kodu, jedynie dokumentuje i standaryzuje artefakty pod RAG i IDE.
:::

## QA

- `dataset sanity`: komplet nagłówków, rozsądne wartości `arch/version`.
- `diagram-lint`: init header obecny.
- `idempotency`: powtórne uruchomienie narzędzi nie generuje diffów.

## See also

- `11_data` — źródła assetów
- `15_vc16` — biblioteki ANGLE/GLES dla Windows (porównanie)
- `04_ui` — UX pod touch

## Appendix / Facets

(facet-14_android.android_project_index)=
### Facet: `14_android.android_project_index`
Type: dataset

(facet-14_android.android_libs)=
### Facet: `14_android.android_libs`
Type: dataset

(facet-14_android.android_assets)=
### Facet: `14_android.android_assets`
Type: dataset

(facet-14_android.android_build)=
### Facet: `14_android.android_build`
Type: diagram

(facet-14_android.android_tree)=
### Facet: `14_android.android_tree`
Type: diagram

---
doc_id: 14_android, source_path: docs/authoring/14_android, source_sha: 92cffc0, last_sync_iso: 2025-10-18T01:36:41.413344Z, doc_class: guide, language: pl, title: 14 - Android, summary: Android assets, ABI-specific .so files, AAB/APK builds, and signing., tags: android,abi,build
---

# 14 - Android

Android assets, ABI-specific .so files, AAB/APK builds, and signing.

## Przegląd

Ten rozdział dokumentuje 14 android w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

README
abi_configuration
apk_signing
blueprints/index
datasets/index
diagrams/index
```

## Key Topics

### ABI Configuration

Multi-architecture support (arm64-v8a, armeabi-v7a, x86_64). See [ABI Configuration](./abi_configuration.md) for per-ABI build settings and optimization.

### APK/AAB Signing

Digital signing for distribution. See [APK Signing Process](./apk_signing.md) for keystore management and Play Store preparation.

## Datasets

- `android_assets.csv`
- `android_build.csv`
- `android_files.csv`

## Diagramy

```{contents}
:local:
:depth: 2
```

## Crosslinks

- [Core API](../01_core/index.md) - C++ native code and JNI
- [Data](../11_data/index.md) - Asset management on Android
- [Game Runtime](../10_game_runtime/index.md) - Android lifecycle integration
- [VC16 Build](../15_vc16/index.md) - Windows build comparison


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.413344Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [x] Diagrams added (build pipeline in datasets)
- [x] Crosslinks verified (4 links)
- [x] Content complete (ABI + signing docs added)

## Appendix / Facets

(facet-14_android.main)=
### Facet: `14_android.main`

Main documentation facet for 14_android.

# APK/AAB Signing Process

## Overview

Android requires all APK/AAB files to be digitally signed before installation. This guide covers keystore management, signing configuration, and Play Store preparation.

## Keystore Creation

### Generate Keystore

```bash
keytool -genkeypair \
    -alias otclient-key \
    -keyalg RSA \
    -keysize 2048 \
    -validity 10000 \
    -keystore otclient-release.keystore \
    -storepass <strong-password> \
    -keypass <key-password> \
    -dname "CN=OTClient, OU=Development, O=OTClient, L=City, ST=State, C=US"
```

**Important**: Store keystore securely! Loss means no updates to published app.

### Keystore Information

```bash
# View keystore details
keytool -list -v -keystore otclient-release.keystore

# View certificate fingerprint (for Play Store)
keytool -list -v -keystore otclient-release.keystore -alias otclient-key
```

## Gradle Signing Configuration

### Method 1: gradle.properties (Recommended)

```properties
# gradle.properties (DO NOT COMMIT!)
RELEASE_STORE_FILE=../otclient-release.keystore
RELEASE_STORE_PASSWORD=<strong-password>
RELEASE_KEY_ALIAS=otclient-key
RELEASE_KEY_PASSWORD=<key-password>
```

```gradle
// build.gradle (app)
android {
    signingConfigs {
        release {
            storeFile file(RELEASE_STORE_FILE)
            storePassword RELEASE_STORE_PASSWORD
            keyAlias RELEASE_KEY_ALIAS
            keyPassword RELEASE_KEY_PASSWORD
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

### Method 2: Environment Variables

```gradle
android {
    signingConfigs {
        release {
            storeFile file(System.getenv("KEYSTORE_FILE") ?: "release.keystore")
            storePassword System.getenv("KEYSTORE_PASSWORD")
            keyAlias System.getenv("KEY_ALIAS")
            keyPassword System.getenv("KEY_PASSWORD")
        }
    }
}
```

```bash
# Set environment variables
export KEYSTORE_FILE=/path/to/otclient-release.keystore
export KEYSTORE_PASSWORD=<strong-password>
export KEY_ALIAS=otclient-key
export KEY_PASSWORD=<key-password>

# Build
./gradlew assembleRelease
```

## Building Signed APK/AAB

### APK (Direct Installation)

```bash
# Build signed APK
./gradlew assembleRelease

# Output:
# app/build/outputs/apk/release/app-release.apk
```

### AAB (Play Store)

```bash
# Build signed AAB
./gradlew bundleRelease

# Output:
# app/build/outputs/bundle/release/app-release.aab
```

## Verification

### Verify APK Signature

```bash
# Using apksigner
apksigner verify --print-certs app-release.apk

# Using jarsigner
jarsigner -verify -verbose -certs app-release.apk
```

### Check APK Info

```bash
# View APK details
aapt dump badging app-release.apk

# Extract certificate
keytool -printcert -jarfile app-release.apk
```

## Play Store Preparation

### App Signing by Google Play

**Recommended**: Let Google manage app signing.

1. Generate upload key (separate from app signing key)
2. Upload AAB to Play Console
3. Google signs with app signing key
4. Users get Google-signed APK

**Benefits**:
- Google manages signing key securely
- Can reset upload key if lost
- Optimized APKs per device

### Upload Key Creation

```bash
# Generate upload key (different from release key)
keytool -genkeypair \
    -alias otclient-upload \
    -keyalg RSA \
    -keysize 2048 \
    -validity 10000 \
    -keystore otclient-upload.keystore
```

### Enrollment Steps

1. Build AAB with upload key:
   ```bash
   ./gradlew bundleRelease
```

2. Go to Play Console → Release → Setup → App integrity

3. Upload app signing key (if first time)

4. Configure upload key

5. Upload AAB

## ProGuard Configuration

### proguard-rules.pro

```proguard
# Keep OTClient classes
-keep class com.otclientv8.** { *; }

# Keep native methods
-keepclasseswithmembernames class * {
    native <methods>;
}

# Keep crash reporting
-keepattributes SourceFile,LineNumberTable
-renamesourcefileattribute SourceFile

# OpenGL
-keep class android.opengl.** { *; }
-keep class javax.microedition.khronos.** { *; }
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Build Release APK

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up JDK
        uses: actions/setup-java@v2
        with:
          java-version: '11'
      
      - name: Decode keystore
        run: |
          echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 -d > release.keystore
      
      - name: Build AAB
        env:
          KEYSTORE_FILE: release.keystore
          KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
          KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
          KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}
        run: |
          ./gradlew bundleRelease
      
      - name: Upload AAB
        uses: actions/upload-artifact@v2
        with:
          name: app-release.aab
          path: app/build/outputs/bundle/release/app-release.aab
```

## Troubleshooting

### Signature Verification Failed

**Error**: "Package ... signatures do not match previously installed version"

**Solution**: Uninstall old version or use same keystore

```bash
adb uninstall com.otclientv8
adb install app-release.apk
```

### Keystore Password Wrong

**Error**: "Keystore was tampered with, or password was incorrect"

**Solution**: Verify password, check keystore integrity

```bash
keytool -list -keystore otclient-release.keystore
```

### Missing Signing Config

**Error**: "Task :app:packageRelease FAILED"

**Solution**: Check signing configuration in build.gradle

## See Also

- [ABI Configuration](./abi_configuration.md)
- [Asset Packaging](./diagrams/android_build.mmd)
- [Android Build Pipeline](./diagrams/build_pipeline.mmd)

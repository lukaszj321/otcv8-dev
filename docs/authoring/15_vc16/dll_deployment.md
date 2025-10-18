# DLL Deployment Checklist

## Overview

OTClient v8 on Windows requires several runtime DLLs for proper operation. This guide covers identification, verification, and deployment of all necessary dependencies.

## Required DLLs

### ANGLE Graphics

| DLL | Size | Purpose | Required |
|-----|------|---------|----------|
| `libEGL.dll` | ~500 KB | EGL API implementation | **Yes** |
| `libGLESv2.dll` | ~3.5 MB | OpenGL ES 2.0/3.0 implementation | **Yes** |
| `d3dcompiler_47.dll` | ~4 MB | DirectX shader compiler | **Yes** |

### Visual C++ Runtime

| DLL | Purpose | Required |
|-----|---------|----------|
| `vcruntime140.dll` | VC++ 2019 runtime | **Yes** |
| `msvcp140.dll` | C++ standard library | **Yes** |
| `msvcp140_1.dll` | C++ additional features | **Yes** (if using C++17 features) |

### Optional Dependencies

| DLL | Purpose | When Required |
|-----|---------|---------------|
| `openal32.dll` | Audio library | If using OpenAL for audio |
| `lua51.dll` | Lua runtime | If Lua is dynamically linked |
| `zlib1.dll` | Compression | If zlib is dynamically linked |

## Deployment Structure

### Recommended Layout

```
OTClientV8/
├── otclient.exe
├── data/
├── modules/
├── mods/
└── bin/
    ├── libEGL.dll
    ├── libGLESv2.dll
    ├── d3dcompiler_47.dll
    ├── vcruntime140.dll
    ├── msvcp140.dll
    └── msvcp140_1.dll
```

Or place DLLs directly alongside executable:

```
OTClientV8/
├── otclient.exe
├── libEGL.dll
├── libGLESv2.dll
├── d3dcompiler_47.dll
├── vcruntime140.dll
├── msvcp140.dll
├── msvcp140_1.dll
├── data/
├── modules/
└── mods/
```

## Verification Script

### PowerShell Script

```powershell
# verify_dlls.ps1

$requiredDlls = @(
    "libEGL.dll",
    "libGLESv2.dll",
    "d3dcompiler_47.dll",
    "vcruntime140.dll",
    "msvcp140.dll"
)

$optionalDlls = @(
    "msvcp140_1.dll",
    "openal32.dll",
    "lua51.dll"
)

Write-Host "=== DLL Verification Script ===" -ForegroundColor Cyan
Write-Host ""

$exePath = "otclient.exe"
if (-not (Test-Path $exePath)) {
    Write-Host "ERROR: otclient.exe not found!" -ForegroundColor Red
    exit 1
}

$exeDir = Split-Path -Parent (Resolve-Path $exePath)
Write-Host "Checking directory: $exeDir" -ForegroundColor Yellow
Write-Host ""

# Check required DLLs
$missingRequired = @()
foreach ($dll in $requiredDlls) {
    $paths = @(
        Join-Path $exeDir $dll,
        Join-Path $exeDir "bin" $dll
    )
    
    $found = $false
    foreach ($path in $paths) {
        if (Test-Path $path) {
            $size = (Get-Item $path).Length / 1MB
            Write-Host "[OK] $dll (${size:F2} MB)" -ForegroundColor Green
            $found = $true
            break
        }
    }
    
    if (-not $found) {
        Write-Host "[MISSING] $dll" -ForegroundColor Red
        $missingRequired += $dll
    }
}

# Check optional DLLs
Write-Host ""
Write-Host "Optional DLLs:" -ForegroundColor Yellow
foreach ($dll in $optionalDlls) {
    $paths = @(
        Join-Path $exeDir $dll,
        Join-Path $exeDir "bin" $dll
    )
    
    $found = $false
    foreach ($path in $paths) {
        if (Test-Path $path) {
            $size = (Get-Item $path).Length / 1MB
            Write-Host "[OK] $dll (${size:F2} MB)" -ForegroundColor Green
            $found = $true
            break
        }
    }
    
    if (-not $found) {
        Write-Host "[NOT FOUND] $dll (optional)" -ForegroundColor Gray
    }
}

# Summary
Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
if ($missingRequired.Count -eq 0) {
    Write-Host "All required DLLs are present!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "Missing required DLLs: $($missingRequired -join ', ')" -ForegroundColor Red
    exit 1
}
```

### Batch Script

```batch
@echo off
REM verify_dlls.bat

echo === DLL Verification Script ===
echo.

set MISSING=0

REM Check required DLLs
call :CheckDLL libEGL.dll 1
call :CheckDLL libGLESv2.dll 1
call :CheckDLL d3dcompiler_47.dll 1
call :CheckDLL vcruntime140.dll 1
call :CheckDLL msvcp140.dll 1

echo.
echo Optional DLLs:
call :CheckDLL msvcp140_1.dll 0
call :CheckDLL openal32.dll 0
call :CheckDLL lua51.dll 0

echo.
echo === Summary ===
if %MISSING%==0 (
    echo All required DLLs are present!
    exit /b 0
) else (
    echo Some required DLLs are missing!
    exit /b 1
)

:CheckDLL
if exist "%1" (
    echo [OK] %1
) else if exist "bin\%1" (
    echo [OK] %1 (in bin/)
) else (
    if "%2"=="1" (
        echo [MISSING] %1
        set MISSING=1
    ) else (
        echo [NOT FOUND] %1 (optional^)
    )
)
goto :eof
```

## Runtime DLL Sources

### ANGLE DLLs

**Option 1**: Build from source
```bash
git clone https://chromium.googlesource.com/angle/angle
cd angle
python scripts/bootstrap.py
gn gen out/Release
ninja -C out/Release
```

**Option 2**: Download pre-built binaries
- From ANGLE releases: https://github.com/google/angle/releases
- From OTClient v8 dependencies repository

### Visual C++ Runtime

**Option 1**: Install redistributable
- Download VC++ 2019 Redistributable (x64)
- Install on target machine

**Option 2**: Include DLLs
- Copy from `C:\Program Files\Microsoft Visual Studio\2019\Community\VC\Redist\MSVC\<version>\x64\Microsoft.VC142.CRT\`

### DirectX Shader Compiler

Usually included with Windows 10, or:
- Download DirectX End-User Runtime
- Extract `d3dcompiler_47.dll` from package

## Installer Integration

### NSIS Script

```nsis
; installer.nsi

Section "Core Files"
    SetOutPath "$INSTDIR"
    File "otclient.exe"
    
    SetOutPath "$INSTDIR\bin"
    File "bin\libEGL.dll"
    File "bin\libGLESv2.dll"
    File "bin\d3dcompiler_47.dll"
    File "bin\vcruntime140.dll"
    File "bin\msvcp140.dll"
    File "bin\msvcp140_1.dll"
SectionEnd

Section "Data Files"
    SetOutPath "$INSTDIR\data"
    File /r "data\*.*"
SectionEnd
```

### WiX Script

```xml
<!-- Product.wxs -->
<Component Id="CoreDLLs" Guid="*">
    <File Source="bin\libEGL.dll" />
    <File Source="bin\libGLESv2.dll" />
    <File Source="bin\d3dcompiler_47.dll" />
    <File Source="bin\vcruntime140.dll" />
    <File Source="bin\msvcp140.dll" />
    <File Source="bin\msvcp140_1.dll" />
</Component>
```

## Troubleshooting

### DLL Load Failed

**Symptoms**: Application fails to start with error about missing DLL

**Solutions**:
1. Run verification script (see above)
2. Check Windows Event Viewer for details
3. Use Dependency Walker (depends.exe) to identify missing dependencies

```bash
# Using Dependencies (modern alternative to depends.exe)
Dependencies.exe -chain otclient.exe
```

### Wrong DLL Architecture

**Symptoms**: Error like "The application was unable to start correctly (0xc000007b)"

**Solution**: Ensure all DLLs are 64-bit (x64) if application is 64-bit:

```powershell
# Check DLL architecture
dumpbin /headers libEGL.dll | findstr machine
# Should show: 8664 machine (x64)
```

### DLL Version Conflicts

**Symptoms**: Crashes or unexpected behavior

**Solution**: Ensure consistent DLL versions:

```bash
# Check ANGLE DLL versions
Get-Item *.dll | Select-Object Name,VersionInfo
```

All ANGLE DLLs should have matching version numbers.

## Deployment Checklist

### Pre-Release

- [ ] All required DLLs present in build output
- [ ] DLLs are correct architecture (x64)
- [ ] DLL versions are consistent
- [ ] Verification script passes
- [ ] Application launches successfully
- [ ] No errors in Event Viewer

### Distribution Package

- [ ] DLLs included in installer
- [ ] Installer places DLLs in correct location
- [ ] Application shortcut includes correct working directory
- [ ] Uninstaller removes all DLLs
- [ ] README includes DLL information

### End-User Documentation

- [ ] System requirements clearly stated
- [ ] Visual C++ Redistributable requirement mentioned
- [ ] Troubleshooting guide for DLL issues
- [ ] Link to download missing dependencies

## Automated Testing

### CI/CD Integration

```yaml
# GitHub Actions example
- name: Verify DLLs
  run: |
    powershell -File scripts/verify_dlls.ps1
    
- name: Package Distribution
  run: |
    mkdir dist
    copy otclient.exe dist/
    copy bin/*.dll dist/
    7z a otclient-win64.zip dist/*
```

### Smoke Test

```cpp
// smoke_test.cpp
#include <Windows.h>
#include <iostream>

int main() {
    // Try to load ANGLE DLLs
    HMODULE egl = LoadLibrary("libEGL.dll");
    HMODULE gles = LoadLibrary("libGLESv2.dll");
    HMODULE d3d = LoadLibrary("d3dcompiler_47.dll");
    
    bool success = true;
    
    if (!egl) {
        std::cerr << "Failed to load libEGL.dll" << std::endl;
        success = false;
    }
    if (!gles) {
        std::cerr << "Failed to load libGLESv2.dll" << std::endl;
        success = false;
    }
    if (!d3d) {
        std::cerr << "Failed to load d3dcompiler_47.dll" << std::endl;
        success = false;
    }
    
    if (success) {
        std::cout << "All DLLs loaded successfully!" << std::endl;
    }
    
    // Cleanup
    if (egl) FreeLibrary(egl);
    if (gles) FreeLibrary(gles);
    if (d3d) FreeLibrary(d3d);
    
    return success ? 0 : 1;
}
```

## See Also

- [ANGLE Integration Guide](./angle_integration.md)
- [EGL Initialization](./egl_initialization.md)
- [VC16 Build Configuration](./index.md)
- [Deployment Guide](../14_android/deployment.md)

<#
.SYNOPSIS
    Przywraca pliki z kopii zapasowych .bak, nadpisując uszkodzone oryginały.
.PARAMETER Path
    Ścieżka do folderu, w którym należy szukać plików .bak (np. ".\docs").
.PARAMETER Cleanup
    Przełącznik, który po przywróceniu usunie pliki .bak. Użyj go dopiero,
    gdy upewnisz się, że wszystko wróciło do normy.
.EXAMPLE
    # Symulacja - pokazuje, co zostanie zrobione, ale nie wykonuje żadnych operacji
    powershell -NoProfile -File ".\scripts\Restore-From-Bak.ps1" -Path ".\docs" -WhatIf

.EXAMPLE
    # Rzeczywiste przywracanie plików z backupów
    powershell -NoProfile -File ".\scripts\Restore-From-Bak.ps1" -Path ".\docs"

.EXAMPLE
    # Usunięcie plików .bak PO udanym przywróceniu
    powershell -NoProfile -File ".\scripts\Restore-From-Bak.ps1" -Path ".\docs" -Cleanup
#>
[CmdletBinding(SupportsShouldProcess=$true)] # To wlacza obsluge -WhatIf
param(
    [Parameter(Mandatory=$true)]
    [string]$Path,

    [Parameter(Mandatory=$false)]
    [switch]$Cleanup
)

if (-not (Test-Path -Path $Path -PathType Container)) {
    Write-Error "BLAD: Sciezka '$Path' nie istnieje lub nie jest folderem."
    exit 1
}

$backupFiles = Get-ChildItem -Path $Path -Filter "*.bak" -Recurse

if ($null -eq $backupFiles) {
    Write-Warning "Nie znaleziono zadnych plikow .bak w sciezce '$Path'."
    exit 0
}

if($Cleanup) {
    Write-Host ">>> Tryb CZYSZCZENIA. Pliki .bak zostana usuniete." -ForegroundColor Red
} else {
    Write-Host ">>> Tryb PRZYWRACANIA. Pliki zostana odtworzone z backupow .bak." -ForegroundColor Yellow
}
Write-Host "----------------------------------------------------------------"

foreach ($bakFile in $backupFiles) {
    $originalFilePath = $bakFile.FullName -replace '\.bak$', ''

    if ($Cleanup) {
        if ($pscmdlet.ShouldProcess($bakFile.FullName, "Remove Backup")) {
            Remove-Item -Path $bakFile.FullName
        }
    }
    else {
        if ($pscmdlet.ShouldProcess($originalFilePath, "Restore from $($bakFile.Name)")) {
            Copy-Item -Path $bakFile.FullName -Destination $originalFilePath -Force
        }
    }
}

Write-Host "----------------------------------------------------------------"
Write-Host "Zakonczono."
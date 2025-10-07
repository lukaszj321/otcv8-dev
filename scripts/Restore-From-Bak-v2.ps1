<#
.SYNOPSIS
    Przywraca pliki z pojedynczych kopii zapasowych .bak, ignorujac .bak.bak itd.
#>
[CmdletBinding(SupportsShouldProcess=$true)]
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

# ZNAJDŹ WSZYSTKIE .bak, a NASTĘPNIE ODFILTRUJ te, które mają .bak.bak
$backupFiles = Get-ChildItem -Path $Path -Filter "*.bak" -Recurse | Where-Object { $_.Name -notlike "*.bak.bak" }

if ($null -eq $backupFiles) {
    Write-Warning "Nie znaleziono zadnych pasujacych plikow .bak (z pojedynczym rozszerzeniem) w sciezce '$Path'."
    exit 0
}

if($Cleanup) {
    Write-Host ">>> Tryb CZYSZCZENIA. Pliki .bak zostana usuniete." -ForegroundColor Red
} else {
    Write-Host ">>> Tryb PRZYWRACANIA. Pliki zostana odtworzone z backupow .bak." -ForegroundColor Yellow
}
Write-Host "----------------------------------------------------------------"

foreach ($bakFile in $backupFiles) {
    # Usuwamy tylko ostatnie .bak z nazwy pliku
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
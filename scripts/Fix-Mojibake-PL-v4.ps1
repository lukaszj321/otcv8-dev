<#
.SYNOPSIS
    Konwertuje kodowanie plikow tekstowych (np. .md) z Windows-1250 na UTF-8 bez BOM.
.DESCRIPTION
    Skrypt rekursywnie przeszukuje podany folder w poszukiwaniu plikow .md,
    ktore maja problemy z kodowaniem polskich znakow.
    Domyslnie dziala w trybie symulacji (Dry Run). Uzycie przelacznika -Apply
    powoduje fizyczne nadpisanie plikow w nowym kodowaniu.
.PARAMETER Path
    Sciezka do folderu, ktory ma zostac przeszukany (np. ".\docs").
.PARAMETER Apply
    Przelacznik, ktory aktywuje tryb zapisu zmian. Bez niego skrypt tylko
    wyswietli, ktore pliki zostalyby zmienione.
.EXAMPLE
    # Tryb symulacji (Dry Run)
    powershell -NoProfile -File ".\scripts\Fix-Mojibake-PL-v4.ps1" -Path ".\docs"
.EXAMPLE
    # Tryb zapisu zmian
    powershell -NoProfile -File ".\scripts\Fix-Mojibake-PL-v4.ps1" -Path ".\docs" -Apply
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$Path,

    [Parameter(Mandatory=$false)]
    [switch]$Apply
)

# --- Konfiguracja ---
$sourceEncoding = [System.Text.Encoding]::GetEncoding('windows-1250')
$targetEncoding = New-Object System.Text.UTF8Encoding($false) # UTF-8 bez BOM
$fileFilter = "*.md"
# ---

if (-not (Test-Path -Path $Path -PathType Container)) {
    Write-Error "BLAD: Podana sciezka '$Path' nie istnieje lub nie jest folderem."
    exit 1
}

$files = Get-ChildItem -Path $Path -Filter $fileFilter -Recurse

if ($null -eq $files) {
    Write-Warning "Nie znaleziono zadnych plikow '$fileFilter' w sciezce '$Path'."
    exit 0
}

if ($Apply) {
    Write-Host ">>> Tryb ZAPISU ZMIAN. Pliki zostana nadpisane kodowaniem UTF-8." -ForegroundColor Yellow
} else {
    Write-Host ">>> Tryb SYMULACJI (Dry Run). Zmiany nie zostana zapisane." -ForegroundColor Cyan
    Write-Host ">>> Aby zapisac zmiany, uruchom skrypt z przelacznikiem -Apply." -ForegroundColor Cyan
}
Write-Host "----------------------------------------------------------------"

$convertedCount = 0
$foundToConvertCount = 0
foreach ($file in $files) {
    try {
        $filePath = $file.FullName
        
        # Sprawdzamy, czy plik zawiera znaki spoza podstawowego ASCII
        $bytes = [System.IO.File]::ReadAllBytes($filePath)
        $testContentUtf8 = [System.IO.File]::ReadAllText($filePath, $targetEncoding)

        # Heurystyka: jesli odczytany jako UTF8 zawiera znak zastepczy (�) ORAZ 
        # odczytany jako cp1250 go nie zawiera, to jest kandydatem do konwersji.
        if ($testContentUtf8.Contains([char]0xFFFD)) {
             $originalContent = [System.IO.File]::ReadAllText($filePath, $sourceEncoding)
             if (-not $originalContent.Contains([char]0xFFFD)) {
                $foundToConvertCount++
                Write-Host "[OK] Znaleziono do konwersji: $filePath" -ForegroundColor White

                if ($Apply) {
                    [System.IO.File]::WriteAllText($filePath, $originalContent, $targetEncoding)
                    Write-Host "     -> Zapisano zmiany." -ForegroundColor Yellow
                    $convertedCount++
                }
             } else {
                Write-Host "[INFO] Pominieto (plik uszkodzony w obu kodowaniach): $filePath" -ForegroundColor Gray
             }
        } else {
            Write-Host "[INFO] Pominieto (prawdopodobnie juz jest UTF-8): $filePath" -ForegroundColor Green
        }
    } catch {
        Write-Error "Blad podczas przetwarzania pliku '$($file.FullName)': $_"
    }
}

Write-Host "----------------------------------------------------------------"
Write-Host "Zakonczono."
if ($Apply) {
    Write-Host "Przekonwertowano $convertedCount z $($files.Count) plikow." -ForegroundColor Green
} else {
    Write-Host "Znaleziono $foundToConvertCount plikow do konwersji. Uzyj -Apply, aby zapisac zmiany." -ForegroundColor Cyan
}
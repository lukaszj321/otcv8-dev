<# 
Fix-MkDocsMd.ps1 (v2.1 - safe, prosto)
Użycie:
  # podgląd
  powershell -NoProfile -File ".\scripts\Fix-MkDocsMd.ps1" -Path ".\docs"

  # zapis
  powershell -NoProfile -File ".\scripts\Fix-MkDocsMd.ps1" -Path ".\docs" -Apply
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Path,
    [switch]$Apply
)

# Katalogi, których NIE dotykamy
$ExcludeRegex = '\\(downloads|_rag|rag|_assets)\\'

function Get-MdFiles {
    param([string]$Root)
    if (-not (Test-Path -LiteralPath $Root)) { throw "Ścieżka nie istnieje: $Root" }

    # tylko .md, bez .bak i bez katalogów wykluczonych
    $md = Get-ChildItem -LiteralPath $Root -Recurse -File -Filter *.md |
    Where-Object {
        $_.FullName -notmatch '\.bak$' -and
        $_.FullName -notmatch $ExcludeRegex
    }
    return $md
}

function Read-TextUtf8 {
    param([string]$File)
    [System.IO.File]::ReadAllText($File, [System.Text.Encoding]::UTF8)
}
function Write-TextUtf8 {
    param([string]$File, [string]$Text)
    [System.IO.File]::WriteAllText($File, $Text, [System.Text.Encoding]::UTF8)
}

# --- Transformacje (bezpieczne) --------------------------------------------

# 1) Usuń niewidzialne znaki (ZWSP/SHY/BOM)
function Remove-InvisibleChars {
    param([string]$Text)
    $zwsp = [char]0x200B; $shy = [char]0x00AD; $bom = [char]0xFEFF
    $Text = $Text -replace [regex]::Escape("$bom"), ""
    $Text = $Text -replace [regex]::Escape("$zwsp"), ""
    $Text = $Text -replace [regex]::Escape("$shy"), ""
    return $Text
}

# 2) Ujednolicenie nagłówków: "# Tytuł", "## Sekcja", itd.
function Normalize-Headings {
    param([string]$Text)
    # Upewnij się, że po # jest spacja
    $Text = $Text -replace '(?m)^\s*(\#{1,6})\s*', '$1 '
    # Usuń nadmiarowe spacje po # i przed tekstem
    $Text = $Text -replace '(?m)^(\#{1,6})\s+(.*)$', '$1 $2'
    return $Text
}

# 3) Domknij bloki {% raw %} jeśli brakuje {% endraw %}
function Fix-RawBlocks {
    param([string]$Text)
    $open = ([regex]'{%\s*raw\s*%}').Matches($Text).Count
    $close = ([regex]'{%\s*endraw\s*%}').Matches($Text).Count
    if ($open -gt $close) {
        $diff = $open - $close
        for ($i = 0; $i -lt $diff; $i++) {
            $Text = $Text.TrimEnd() + "`r`n{% endraw %}"
        }
        $Text += "`r`n"
    }
    return $Text
}

# 4) Normalizacja pustych linii i końcówki pliku
function Normalize-BlankLines {
    param([string]$Text)
    # usuń linie z samymi białymi znakami
    $Text = ($Text -replace '(?m)^\s+$', '').TrimEnd()
    # unifikuj EOL na CRLF i zakończ jedną pustą linią
    $Text = ($Text -split "`r?`n") -join "`r`n"
    return $Text + "`r`n"
}

# --- Główna pętla -----------------------------------------------------------
$files = Get-MdFiles -Root $Path
$checked = 0; $changed = 0; $unchanged = 0; $changedList = @()

foreach ($f in $files) {
    $checked++
    $orig = Read-TextUtf8 -File $f.FullName
    $txt = $orig

    $txt = Remove-InvisibleChars  $txt
    $txt = Normalize-Headings     $txt
    $txt = Fix-RawBlocks          $txt
    $txt = Normalize-BlankLines   $txt

    if ($txt -ne $orig) {
        $changed++; $changedList += $f.FullName
        if ($Apply) {
            $bak = "$($f.FullName).bak"
            if (-not (Test-Path -LiteralPath $bak)) {
                Copy-Item -LiteralPath $f.FullName -Destination $bak -Force
            }
            Write-TextUtf8 -File $f.FullName -Text $txt
            Write-Host "Fix: $($f.FullName)" -ForegroundColor Cyan
        }
    }
    else {
        $unchanged++
    }
}

Write-Host ""
Write-Host "Checked: $checked files" -ForegroundColor Yellow
Write-Host "Changed: $changed" -ForegroundColor Green
Write-Host "Unchanged: $unchanged" -ForegroundColor Gray
Write-Host ""
if ($Apply) {
    Write-Host "Apply mode. Changes written. Backups *.bak created next to .md files." -ForegroundColor Green
}
else {
    Write-Host "Preview mode. Use -Apply to write changes (creates .bak for .md)." -ForegroundColor Yellow
}
if ($changedList.Count -gt 0) {
    Write-Host "`nChanged files:" -ForegroundColor Yellow
    $changedList | ForEach-Object { Write-Host " - $_" }
}

param(
    [string]$Path = ".\docs",
    [switch]$WhatIf
)

if (-not (Test-Path $Path)) { Write-Error "Nie ma folderu: $Path"; exit 1 }

# Backup
$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$backup = "__md_backup_$ts"
if (-not $WhatIf) { Copy-Item $Path $backup -Recurse -Force | Out-Null }
Write-Host "Backup -> .\$backup"

# Encodings
$encLatin1 = [System.Text.Encoding]::GetEncoding(28591) # ISO-8859-1
$encUtf8NoBom = New-Object System.Text.UTF8Encoding($false)
$BOM = [char]0xFEFF
$NBSP = [char]0x00A0

function Has-Mojibake([string]$s) {
    # szukamy typowych „Ã / Â / â” po złej dekodacji (regex z \uXXXX, bez polskich liter)
    return [bool]([regex]::IsMatch($s, "\u00C3|\u00C2|\u00E2"))
}

function Fix-Text([string]$s) {
    # Rekodowanie Latin1->UTF8 naprawia większość przypadków (np. Ã…‚ -> ł, â€“ -> –)
    $bytes = $encLatin1.GetBytes($s)
    $t = [System.Text.Encoding]::UTF8.GetString($bytes)

    # Usunięcie BOM na początku, NBSP -> spacja, standaryzacja EOL
    if ($t.Length -gt 0 -and $t[0] -eq $BOM) { $t = $t.Substring(1) }
    $t = $t.Replace($NBSP, ' ')
    $t = $t -replace "`r`n", "`n"
    return $t
}

$files = Get-ChildItem $Path -Recurse -Include *.md -File
$checked = 0; $changed = 0

foreach ($f in $files) {
    $checked++
    # czytaj jako UTF-8 (bez BOM) – jeśli plik ma błędne znaki, i tak naprawimy po detekcji
    $orig = [System.IO.File]::ReadAllText($f.FullName, $encUtf8NoBom)

    if (Has-Mojibake $orig) {
        $fixed = Fix-Text $orig
        if ($fixed -ne $orig) {
            $changed++
            if ($WhatIf) {
                Write-Host "Would fix: $($f.FullName)"
            }
            else {
                [System.IO.File]::WriteAllText($f.FullName, $fixed, $encUtf8NoBom)
                Write-Host "Fix: $($f.FullName)"
            }
        }
        else {
            Write-Host "OK:  $($f.FullName)"
        }
    }
    else {
        Write-Host "OK:  $($f.FullName)"
    }
}

Write-Host "Checked: $checked"
Write-Host "Changed: $changed"
if ($WhatIf) { Write-Host "(Symulacja — pliki NIE zapisane)" }

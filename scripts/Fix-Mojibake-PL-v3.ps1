param(
  [string]$Path = ".\docs",
  [switch]$WhatIf
)

if (-not (Test-Path $Path)) {
  Write-Error "Nie ma folderu: $Path"
  exit 1
}

# --- Backup ---
$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$backup = "__md_backup_$ts"
if (-not $WhatIf) { Copy-Item $Path $backup -Recurse -Force | Out-Null }
Write-Host "Backup -> .\$backup"

# Encodings
$latin1 = [System.Text.Encoding]::GetEncoding(28591) # ISO-8859-1
$utf8 = New-Object System.Text.UTF8Encoding($false)

# Znaki typowe dla mojibake (tworzymy bezpośrednio z kodów)
$CH_Ã = [char]0x00C3
$CH_Â = [char]0x00C2
$CH_â = [char]0x00E2
$CH_BOM = [char]0xFEFF
$NBSP = [char]0x00A0

function Count-Bad([string]$s) {
  ($s.ToCharArray() | Where-Object { $_ -eq $CH_Ã -or $_ -eq $CH_Â -or $_ -eq $CH_â -or $_ -eq $CH_BOM }).Count
}

function Recode-Latin1-ToUtf8([string]$s) {
  $bytes = $latin1.GetBytes($s)
  return $utf8.GetString($bytes)
}

$files = Get-ChildItem $Path -Recurse -Include *.md -File
$checked = 0; $changed = 0

foreach ($f in $files) {
  $checked++
  $orig = [System.IO.File]::ReadAllText($f.FullName, $utf8)

  $beforeBad = Count-Bad $orig

  # 1) Rekodowanie Latin1->UTF8 (typowy przypadek: "Ä…", "Å‚", "â€“", "Â ")
  $step1 = Recode-Latin1-ToUtf8 $orig

  # 2) Normalizacja spacji: NBSP -> zwykła spacja, usunięcie zbędnego "Â"
  $step2 = $step1.Replace($NBSP, ' ')
  $step2 = ($step2.ToCharArray() | Where-Object { $_ -ne $CH_Â }) -join ''

  # 3) Normalizacja końcówek linii
  $fixed = $step2 -replace "`r`n", "`n"

  $afterBad = Count-Bad $fixed

  if (($fixed -ne $orig) -and ($afterBad -lt $beforeBad)) {
    $changed++
    if ($WhatIf) {
      Write-Host "Would fix: $($f.FullName)"
    }
    else {
      [System.IO.File]::WriteAllText($f.FullName, $fixed, $utf8)
      Write-Host "Fix: $($f.FullName)"
    }
  }
  else {
    Write-Host "OK:  $($f.FullName)"
  }
}

Write-Host "Checked: $checked"
Write-Host "Changed: $changed"
if ($WhatIf) { Write-Host "(Symulacja — pliki NIE zapisane)" }

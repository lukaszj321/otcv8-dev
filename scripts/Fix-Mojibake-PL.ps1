param(
  [string]$Path = ".\docs",
  [switch]$WhatIf
)

# --- Walidacja ścieżki ---
if (-not (Test-Path $Path)) {
  Write-Error "Nie ma folderu: $Path"
  exit 1
}

# --- Backup ---
$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$backup = "__md_backup_$ts"
if (-not $WhatIf) {
  Copy-Item $Path $backup -Recurse -Force | Out-Null
}
Write-Host "Backup -> .\$backup"

# --- Mapowanie najczęstszych artefaktów PL i znaków 'smart' ---
$map = @{
  # polskie litery po podwójnym UTF-8 / CP1250->UTF8
  'Ã„…'='ą'; 'Ä…'='ą'; 'Ã„‡'='ć'; 'Ä‡'='ć'; 'Ã„™'='ę'; 'Ä™'='ę';
  'Ã…‚'='ł'; 'Å‚'='ł'; 'Ã³'='ó';  'Ã“'='Ó'; 'Ã…„'='ń'; 'Å„'='ń';
  'Ã…›'='ś'; 'Å›'='ś'; 'Ã…¼'='ż'; 'Å¼'='ż'; 'Ã…º'='ź'; 'Åº'='ź';
  'Ã„…'='ą'; 'Ã„„'='Ą'; 'Ã„‡'='ć'; 'Ã„†'='Ć'; 'Ã„™'='ę'; 'Ã„˜'='Ę';
  'Ã…‚'='ł'; 'Ã…'='Ł'; 'Ãƒ³'='ó'; 'Ã“'='Ó'; 'Ã…„'='ń'; 'Ã…'='Ń';
  'Ã…›'='ś'; 'Ã…š'='Ś'; 'Ã….¼'='ż'; 'Ã…»'='Ż'; 'Ã…º'='ź'; 'Ã…¹'='Ź';

  # spacje/nadmiary
  'Â ' = ' '; 'Â'='';

  # cudzysłowy/myślniki/punkty
  'â€“'='–'; 'â€”'='—'; 'â€ś'='“'; 'â€ť'='”'; 'â€ś'='„'; 'â€™'='’'; 'â€˘'='•'; 'â€¦'='…';
  'Ă˘â‚¬â€˜'='–'; 'â€"'='—';

  # inne częstszaki
  'Ã‚Â'=''   # często w plikach z Word/HTML
}

# --- Heurystyka: czy wygląda na mojibake? ---
function Test-Mojibake([string]$s) {
  return ($s -match 'Ã|Â|â€|Ă')
}

# --- Przetwarzanie md ---
$files = Get-ChildItem $Path -Recurse -Include *.md -File
$changed = 0; $checked = 0

foreach ($f in $files) {
  $checked++
  $bytes = [IO.File]::ReadAllBytes($f.FullName)
  $txt   = [Text.Encoding]::UTF8.GetString($bytes)

  $orig = $txt
  if (Test-Mojibake $txt) {
    foreach ($k in $map.Keys) {
      $txt = $txt -replace [regex]::Escape($k), $map[$k]
    }
    # normalizacja końcówek linii
    $txt = $txt -replace "`r`n", "`n"
  }

  if ($txt -ne $orig) {
    $changed++
    if ($WhatIf) {
      Write-Host "Would fix: $($f.FullName)"
    } else {
      [IO.File]::WriteAllText($f.FullName, $txt, (New-Object System.Text.UTF8Encoding($false)))
      Write-Host "Fix: $($f.FullName)"
    }
  } else {
    Write-Host "OK:  $($f.FullName)"
  }
}

Write-Host "Checked: $checked"
Write-Host "Changed: $changed"
if ($WhatIf) { Write-Host "(Symulacja — pliki NIE zapisane)" }

<#
  Naprawa kodowania JEDNEGO pliku .md:
   - testuje rekodacje: Latin1, CP1250, ISO-8859-2
   - wybiera: min. mojibake (Â/Ã/â), przy remisie: max. polskich znaków
   - normalizuje do UTF-8 (bez BOM) + LF
  Tryby:
    - bez przełączników  -> naprawa + zapis
    - -WhatIf            -> pokaż co by zrobił
    - -Verify            -> tylko sprawdź (exit 0 OK / 1 problem)
#>
param(
  [string]$File = "docs/api/engine/otclient_v_8_walidator_macierze_ast_i_round_trip_specyfikacja_techniczna.md",
  [switch]$WhatIf,
  [switch]$Verify
)

if (-not (Test-Path $File)) { Write-Error "Brak pliku: $File"; exit 1 }

# Encodings
$encUtf8NoBom = New-Object System.Text.UTF8Encoding($false)
$latin1 = [System.Text.Encoding]::GetEncoding(28591)  # ISO-8859-1
$cp1250 = [System.Text.Encoding]::GetEncoding(1250)   # Windows-1250
$iso88592 = [System.Text.Encoding]::GetEncoding(28592)  # ISO-8859-2
$NBSP = [char]0x00A0
$BOM = [char]0xFEFF

function Count-Mojibake([string]$s) {
  # Â (\u00C2), Ã (\u00C3), â (\u00E2)
  return ([regex]::Matches($s, '[\u00C2\u00C3\u00E2]')).Count
}
function Count-Polish([string]$s) {
  # ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ
  return ([regex]::Matches($s, '[\u0105\u0107\u0119\u0142\u0144\u00F3\u015B\u017A\u017C\u0104\u0106\u0118\u0141\u0143\u00D3\u015A\u0179\u017B]')).Count
}
function Recode([string]$s, [System.Text.Encoding]$srcEnc) {
  $b = $srcEnc.GetBytes($s)
  return [System.Text.Encoding]::UTF8.GetString($b)
}

# Wejście (czytaj jako UTF-8)
$bytes = [System.IO.File]::ReadAllBytes($File)
$text0 = [System.Text.Encoding]::UTF8.GetString($bytes)

# Wariants
$candidates = @(
  @{ name = 'orig'    ; txt = $text0 },
  @{ name = 'latin1'  ; txt = (Recode $text0 $latin1) },
  @{ name = 'cp1250'  ; txt = (Recode $text0 $cp1250) },
  @{ name = 'iso88592'; txt = (Recode $text0 $iso88592) }
)

# Oceń
$scored = foreach ($c in $candidates) {
  $t = $c.txt
  if ($t.Length -gt 0 -and $t[0] -eq $BOM) { $t = $t.Substring(1) }
  $tEval = $t.Replace($NBSP, ' ')
  [pscustomobject]@{
    Name     = $c.name
    Text     = $t
    Mojibake = (Count-Mojibake $tEval)
    Polish   = (Count-Polish  $tEval)
  }
}

$best = $scored | Sort-Object Mojibake, @{Expression = 'Polish'; Descending = $true } | Select-Object -First 1
$fixed = $best.Text
if ($fixed.Length -gt 0 -and $fixed[0] -eq $BOM) { $fixed = $fixed.Substring(1) }
$fixed = $fixed.Replace($NBSP, ' ')
$fixed = $fixed -replace "`r`n", "`n"

if ($Verify) {
  $hasCRLF = $text0 -match "`r`n"
  $hasBOMh = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF)
  $hasBOMc = ($text0.Length -gt 0 -and $text0[0] -eq $BOM)
  $m0 = Count-Mojibake $text0
  if (-not $hasCRLF -and -not $hasBOMh -and -not $hasBOMc -and $m0 -eq 0) {
    Write-Host "OK: $File (UTF-8 bez BOM + LF, brak artefaktów)"; exit 0
  }
  else {
    Write-Host "FAIL: $File"
    if ($hasCRLF) { Write-Host " - CRLF wykryte" }
    if ($hasBOMh) { Write-Host " - BOM w nagłówku pliku" }
    if ($hasBOMc) { Write-Host " - U+FEFF jako znak na początku" }
    if ($m0 -gt 0) { Write-Host (" - Mojibake: {0}" -f $m0) }
    exit 1
  }
}

Write-Host ("Best candidate: {0} (Mojibake={1}, Polish={2})" -f $best.Name, $best.Mojibake, $best.Polish)
if ($WhatIf) { Write-Host ("Would write UTF-8 (no BOM) + LF -> {0}" -f $File); exit 0 }

[System.IO.File]::WriteAllText($File, $fixed, $encUtf8NoBom)
Write-Host ("Fixed -> {0} (UTF-8 bez BOM + LF; variant={1})" -f $File, $best.Name)
exit 0

param(
  [string]$Path = ".\docs",
  [switch]$WhatIf
)

if (-not (Test-Path $Path)) { Write-Error "Nie ma folderu: $Path"; exit 1 }

# Backup
$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$backup = "__md_backup_$ts"
if (-not $WhatIf) { Copy-Item $Path $backup -Recurse -Force | Out-Null }
Write-Host ("Backup -> .\{0}" -f $backup)

# Encodings
$encLatin1 = [System.Text.Encoding]::GetEncoding(28591) # ISO-8859-1
$encUtf8NoBom = New-Object System.Text.UTF8Encoding($false)
$BOM  = [char]0xFEFF
$NBSP = [char]0x00A0

function Has-Mojibake([string]$s) {
  return [bool]([regex]::IsMatch($s, "\u00C3|\u00C2|\u00E2"))
}

function Fix-Text([string]$s) {
  $bytes = $encLatin1.GetBytes($s)
  $t = [System.Text.Encoding]::UTF8.GetString($bytes)
  if ($t.Length -gt 0 -and $t[0] -eq $BOM) { $t = $t.Substring(1) }
  $t = $t.Replace($NBSP, ' ')
  $t = $t -replace "`r`n", "`n"
  return $t
}

$files = Get-ChildItem $Path -Recurse -Include *.md -File
$checked = 0; $changed = 0

foreach ($f in $files) {
  $checked++
  $orig = [System.IO.File]::ReadAllText($f.FullName, $encUtf8NoBom)

  if (Has-Mojibake $orig) {
    $fixed = Fix-Text $orig
    if ($fixed -ne $orig) {
      $changed++
      if ($WhatIf) {
        Write-Host ("Would fix: {0}" -f $f.FullName)
      } else {
        [System.IO.File]::WriteAllText($f.FullName, $fixed, $encUtf8NoBom)
        Write-Host ("Fix: {0}" -f $f.FullName)
      }
    } else {
      Write-Host ("OK:  {0}" -f $f.FullName)
    }
  } else {
    Write-Host ("OK:  {0}" -f $f.FullName)
  }
}

Write-Host ("Checked: {0}" -f $checked)
Write-Host ("Changed: {0}" -f $changed)
if ($WhatIf) { Write-Host "Simulation mode: files NOT saved" }

# scripts/Fix-PolishEncoding.ps1
param(
  [Parameter(Mandatory = $true)][string]$Path,
  [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-Bytes($file) { [IO.File]::ReadAllBytes($file) }
function Write-Utf8NoBom($file, [string]$text) {
  $bytes = [Text.UTF8Encoding]::new($false).GetBytes($text)
  [IO.File]::WriteAllBytes($file, $bytes)
}
function Is-ValidUtf8([byte[]]$bytes) {
  try { [void][Text.UTF8Encoding]::new($true, $true).GetString($bytes); $true } catch { $false }
}

# „Odgniatanie” mojibake: traktujemy zły tekst jako bajty w 1250/1252 i dekodujemy znów jako UTF-8
function Undo-Mojibake([string]$s) {
  $enc1250 = [Text.Encoding]::GetEncoding(1250)
  $enc1252 = [Text.Encoding]::GetEncoding(1252)
  $utf8 = [Text.Encoding]::UTF8

  $hasJunk = $s -match '[ÃÂÄĹ]'

  if (-not $hasJunk) { return $s }

  # próba 1: 1250→UTF8
  $b1250 = $enc1250.GetBytes($s)
  try {
    $t1 = $utf8.GetString($b1250)
    if ($t1 -match '[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]') { return $t1 }
  }
  catch {}

  # próba 2: 1252→UTF8 (częsty przypadek)
  $b1252 = $enc1252.GetBytes($s)
  try {
    $t2 = $utf8.GetString($b1252)
    if ($t2 -match '[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]') { return $t2 }
  }
  catch {}

  return $s
}

# heurystyka: czy tekst wygląda na „dobry” (ma PL litery i brak śmieci)?
function Looks-Good([string]$s) {
  ($s -match '[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]') -and -not ($s -match '[ÃÂÄĹ]{1,}')
}

$files = Get-ChildItem -Path $Path -Recurse -File -Filter *.md
$changed = @()
$checked = 0

foreach ($f in $files) {
  $checked++

  $bytes = Get-Bytes $f.FullName
  $utf8 = [Text.Encoding]::UTF8
  $cp1250 = [Text.Encoding]::GetEncoding(1250)

  $outText = $null
  $note = $null

  if (Is-ValidUtf8 $bytes) {
    # jest poprawne UTF-8 – zobaczmy, czy to nie „utrwalone” mojibake
    $t = $utf8.GetString($bytes)
    if ($t -match '[ÃÂÄĹ]') {
      $fixed = Undo-Mojibake $t
      if ($fixed -ne $t) {
        $outText = $fixed
        $note = 'utf8+mojibake→utf8'
      }
    }
  }
  else {
    # nie-UTF8 → spróbuj CP-1250
    try {
      $t1250 = $cp1250.GetString($bytes)
      $outText = $t1250
      $note = 'cp1250→utf8'
    }
    catch {}
  }

  # jeśli nadal brak decyzji – zostaw bez zmian
  if (-not $outText) { continue }

  # drobne cleanupy po drodze
  $outText = $outText -replace '^\#\s*Â¦\s*Modul:', '# Modul:'  # nagłówek „Â¦”
  # ujednolicenie linii końcowych
  $outText = ($outText -replace "`r`n", "`n").TrimEnd() + "`n"

  if ($Apply) {
    $bak = "$($f.FullName).bak"
    if (-not (Test-Path $bak)) { Copy-Item $f.FullName $bak }
    Write-Utf8NoBom $f.FullName $outText
    $changed += , ([pscustomobject]@{ File = $f.FullName; Mode = $note })
  }
  else {
    $changed += , ([pscustomobject]@{ File = $f.FullName; Mode = "$note (preview)" })
  }
}

"{0}: {1}" -f 'Checked', $checked
"{0}: {1}" -f (if ($Apply) { 'Changed' } else { 'Would change' }), $changed.Count
if ($changed.Count) {
  "`n{0} files:`n - {1}" -f (if ($Apply) { 'Changed' } else { 'Would change' }), ($changed | ForEach-Object { "$($_.File)  [$($_.Mode)]" } -join "`n - ")
}
else {
  "`nNo changes needed."
}

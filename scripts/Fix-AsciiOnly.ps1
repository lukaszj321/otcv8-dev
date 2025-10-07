# scripts/Fix-AsciiOnly.ps1
param(
  [Parameter(Mandatory=$true)][string]$Path,
  [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Utf8NoBom { [Text.UTF8Encoding]::new($false) }
function Read-Bytes($p){ [IO.File]::ReadAllBytes($p) }
function Write-Text($p,[string]$t){ [IO.File]::WriteAllBytes($p,(Utf8NoBom).GetBytes($t)) }

# ASCII-normalizacja:
# 1) FormD (rozbicie na litera + akcent)  2) wywal akcenty  3) zamień typograficzne znaki na ASCII
# 4) usuń cokolwiek spoza ASCII
function To-Ascii([string]$s){
  if ([string]::IsNullOrEmpty($s)) { return $s }
  $norm = $s.Normalize([Text.NormalizationForm]::FormD)
  # wywal znaki łączące (akcenty)
  $noMarks = [Text.RegularExpressions.Regex]::Replace($norm, '\p{Mn}+', '')
  # proste zamiany typograficzne → ASCII
  $t = $noMarks `
    -replace '[\u2018\u2019\u201A\u2032]', "'" `
    -replace '[\u201C\u201D\u201E\u2033]', '"' `
    -replace '[\u2013\u2014\u2212]', '-' `
    -replace '[\u00A0]', ' ' `
    -replace '[\u2026]', '...' `
    -replace '[\u00AB]', '<<' `
    -replace '[\u00BB]', '>>' `
    -replace '[\u00A6]', '|'  # ¦ → |
  # wytnij wszystko spoza ASCII
  $ascii = [Text.RegularExpressions.Regex]::Replace($t, '[^\u0000-\u007F]', '')
  # normalizuj CRLF
  ($ascii -replace "`r?`n", "`r`n")
}

# sprzątanie śmieci generowanych wcześniej
function Cleanup-Artifacts([string]$text){
  $lines = ($text -replace "`r?`n","`n").Split("`n")
  $bar = [char]0x00A6  # ¦
  $Ac = [char]0x00C2   # Â
  $bt = [char]96       # `
  $trip = "$bt$bt$bt"

  $out = New-Object System.Collections.Generic.List[string]
  $inFence = $false
  foreach($line in $lines){
    $l = $line

    # usuń czyste linie z {% raw %} / {% endraw %}
    if ($l -match '^\s*\{\%\s*raw\s*\%\}\s*$') { continue }
    if ($l -match '^\s*\{\%\s*endraw\s*\%\}\s*$') { continue }

    # napraw nagłówki "# ¦ Tytuł" lub "# Â¦ Tytuł" -> "# Tytuł"
    $l = [regex]::Replace($l, '^(#+)\s*(?:' + [regex]::Escape("$Ac") + ')?' + [regex]::Escape("$bar") + '\s+', '$1 ')

    # "```$fenceInfo" -> "```"
    if ([regex]::IsMatch($l, '^\s*' + [regex]::Escape($trip + '$fenceInfo') + '\s*$')) { $l = $trip }

    # usuń samotne "`$fenceInfo"
    if ($l -match '^\s*`\$fenceInfo\s*$') { continue }

    $out.Add($l) | Out-Null
  }
  (($out -join "`n").TrimEnd() + "`n") -replace "`n","`r`n"
}

# dekoduj bajty: jeśli valid UTF-8 → użyj; inaczej spróbuj CP-1250, w ostateczności 1252
function Decode-Text([byte[]]$bytes){
  try {
    $strict = [Text.UTF8Encoding]::new($true,$true)
    return $strict.GetString($bytes)
  } catch {
    try { return [Text.Encoding]::GetEncoding(1250).GetString($bytes) }
    catch { return [Text.Encoding]::GetEncoding(1252).GetString($bytes) }
  }
}

if (-not (Test-Path $Path)) { throw "Path not found: $Path" }
$files = Get-ChildItem -Path $Path -Recurse -File -Filter *.md | Sort-Object FullName

$checked=0;$changed=0
$changedFiles = New-Object System.Collections.Generic.List[string]

foreach($f in $files){
  $checked++
  $raw = Read-Bytes $f.FullName
  $text = Decode-Text $raw

  # 1) sprzątanie artefaktów (bez zmiany liter)
  $clean = Cleanup-Artifacts $text
  # 2) twarda transliteracja do ASCII
  $ascii = To-Ascii $clean

  if ($ascii -ne $text) {
    if ($Apply) { Write-Text $f.FullName $ascii }
    $changed++; $changedFiles.Add($f.FullName) | Out-Null
  }
}

"Checked: $checked"
if ($Apply) {
  "Changed: $changed"
  "Unchanged: " + (($checked)-$changed)
} else {
  "Would change: $changed"
  "Preview mode. Use -Apply to write changes."
}
if ($changedFiles.Count) {
  "`nFiles:"
  $changedFiles | ForEach-Object { " - $_" }
}

param(
  [string]$Path = ".\docs"
)

$ErrorActionPreference = "Stop"

# Encodings
$Utf8Strict = New-Object System.Text.UTF8Encoding($false, $true) # no BOM, strict
$Utf8NoBom  = New-Object System.Text.UTF8Encoding($false)        # no BOM, lax
$Enc1250    = [System.Text.Encoding]::GetEncoding(1250)
$Enc1252    = [System.Text.Encoding]::GetEncoding(1252)

# ASCII-only map: "zepsute" -> "poprawne" (uXXXX)
$REPL = @(
  @{ from="`u00C4`u0085"; to="`u0105" } # Ä… -> ą
  @{ from="`u00C4`u0084"; to="`u0104" } # Ä„ -> Ą
  @{ from="`u00C4`u0087"; to="`u0107" } # Ä‡ -> ć
  @{ from="`u00C4`u0086"; to="`u0106" } # Ä† -> Ć
  @{ from="`u00C4`u0099"; to="`u0119" } # Ä™ -> ę
  @{ from="`u00C4`u0098"; to="`u0118" } # Ä˜ -> Ę
  @{ from="`u00C5`u0082"; to="`u0142" } # Å‚ -> ł
  @{ from="`u00C5`u0081"; to="`u0141" } # Å� -> Ł
  @{ from="`u00C5`u0084"; to="`u0144" } # Å„ -> ń
  @{ from="`u00C5`u0083"; to="`u0143" } # Åƒ -> Ń
  @{ from="`u00C3`u00B3"; to="`u00F3" } # Ã³ -> ó
  @{ from="`u00C3`u0093"; to="`u00D3" } # Ã“ -> Ó
  @{ from="`u00C5`u009B"; to="`u015B" } # Å› -> ś
  @{ from="`u00C5`u008A"; to="`u015A" } # Åš -> Ś
  @{ from="`u00C5`u00BA"; to="`u017A" } # Åº -> ź
  @{ from="`u00C5`u00B9"; to="`u0179" } # Å¹ -> Ź
  @{ from="`u00C5`u00BC"; to="`u017C" } # Å¼ -> ż
  @{ from="`u00C5`u00BB"; to="`u017B" } # Å» -> Ż

  # typowe znaki typograficzne zepsute na "â…"
  @{ from="`u00E2`u0080`u0093"; to="`u2013" } # â€“ -> –
  @{ from="`u00E2`u0080`u0094"; to="`u2014" } # â€” -> —
  @{ from="`u00E2`u0080`u009E"; to="`u201E" } # â€ž -> „
  @{ from="`u00E2`u0080`u009D"; to="`u201D" } # â€� -> ”
  @{ from="`u00E2`u0080`u009C"; to="`u201C" } # â€œ -> “
  @{ from="`u00E2`u0080`u00A2"; to="`u2022" } # â€¢ -> •
  @{ from="`u00E2`u0080`u00A6"; to="`u2026" } # â€¦ -> …

  # NBSP i pozostalosci "Â "
  @{ from="`u00C2`u00A0"; to=" " }         # Â  -> spacja
  @{ from="`u00C2`u00AB"; to="`u00AB" }    # Â« -> « (rzadkie)
  @{ from="`u00C2`u00BB"; to="`u00BB" }    # Â» -> » (rzadkie)
)

# marker "krzaków": Â, Ã, Ä, Å
$MarkerSet = New-Object System.Collections.Generic.HashSet[int]
foreach($code in @(0x00C2,0x00C3,0x00C4,0x00C5)){ [void]$MarkerSet.Add($code) }

function Has-Markers([string]$s){
  foreach($ch in $s.ToCharArray()){
    if ($MarkerSet.Contains([int][char]$ch)) { return $true }
  }
  return $false
}

function Read-Text([string]$file){
  $bytes = [System.IO.File]::ReadAllBytes($file)
  try {
    return $true, ($Utf8Strict.GetString($bytes))
  } catch {
    # nie-UTF8: spróbuj CP-1250, potem CP-1252
    $t1250 = $Enc1250.GetString($bytes)
    if($t1250){ return $false, $t1250 }
    $t1252 = $Enc1252.GetString($bytes)
    return $false, $t1252
  }
}

function Fix-One([string]$text){
  $out = $text
  foreach($pair in $REPL){
    $out = $out -replace [regex]::Escape($pair.from), [string]$pair.to
  }
  return $out
}

if(-not (Test-Path $Path)){ Write-Error "Path not found: $Path" }

$stamp = (Get-Date).ToString("yyyyMMdd_HHmmss")
$backupDir = ".\__md_backup_$stamp"
Write-Host "Backup -> $backupDir"
Copy-Item $Path $backupDir -Recurse -Force

$files = Get-ChildItem $Path -Recurse -Filter *.md
$changed = 0
$unchanged = 0

foreach($f in $files){
  $isUtf8,$t = Read-Text $f.FullName
  if([string]::IsNullOrEmpty($t)){ $unchanged++; continue }

  $orig = $t
  # Jeżeli tekst wygląda na „krzakowaty” albo ma typowe sekwencje – podmieniaj
  if(Has-Markers $t -or $t -match "`u00E2`u0080"){
    $t = Fix-One $t
  }

  if($t -ne $orig){
    [System.IO.File]::WriteAllText($f.FullName, $t, $Utf8NoBom)
    Write-Host "Fix: $($f.FullName)"
    $changed++
  } else {
    $unchanged++
  }
}

Write-Host "`nChecked:  $($files.Count)"
Write-Host "Changed:  $changed"
Write-Host "Unchanged:$unchanged"

try {
  git add -A
  git commit -m "docs: fix mojibake -> UTF-8 (no BOM)"
  Write-Host "Commit created. Run: git push"
} catch {
  Write-Warning "Commit not created (maybe no changes)."
}

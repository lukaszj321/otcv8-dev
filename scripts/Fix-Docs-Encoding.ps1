param(
  [string]$Path = ".\docs",
  [switch]$FixHeaderIds
)

$ErrorActionPreference = "Stop"

# --- encodings (no BOM) ---
$Utf8Strict = New-Object System.Text.UTF8Encoding($false, $true)
$Utf8NoBom  = New-Object System.Text.UTF8Encoding($false)
$Enc1250    = [System.Text.Encoding]::GetEncoding(1250)
$Enc1252    = [System.Text.Encoding]::GetEncoding(1252)

function Read-Bytes([string]$p) {
  return [System.IO.File]::ReadAllBytes($p)
}

function Try-Decode-UTF8([byte[]]$bytes) {
  try {
    return ,$true, ($Utf8Strict.GetString($bytes))
  } catch {
    return ,$false, $null
  }
}

# Polish letters (code points) to detect "good" text
$PolishCodes = @(
  0x0104,0x0105, # Ą ą
  0x0106,0x0107, # Ć ć
  0x0118,0x0119, # Ę ę
  0x0141,0x0142, # Ł ł
  0x0143,0x0144, # Ń ń
  0x00D3,0x00F3, # Ó ó
  0x015A,0x015B, # Ś ś
  0x0179,0x017A, # Ź ź
  0x017B,0x017C  # Ż ż
)
$PolishSet = New-Object System.Collections.Generic.HashSet[int]
[void]($PolishCodes | ForEach-Object { $PolishSet.Add($_) })

# Mojibake marker chars: Â, Ã, Ä, Å  (U+00C2,U+00C3,U+00C4,U+00C5)
$MarkerCodes = @(0x00C2,0x00C3,0x00C4,0x00C5)
$MarkerSet = New-Object System.Collections.Generic.HashSet[int]
[void]($MarkerCodes | ForEach-Object { $MarkerSet.Add($_) })

function Count-By([string]$s, [System.Collections.Generic.HashSet[int]]$set) {
  $n = 0
  foreach($ch in $s.ToCharArray()) {
    if ($set.Contains([int][char]$ch)) { $n++ }
  }
  return $n
}

function Score([string]$s) {
  if ([string]::IsNullOrWhiteSpace($s)) { return -1 }
  $pl = Count-By $s $PolishSet
  $mk = Count-By $s $MarkerSet
  # prosta metryka: więcej PL, mniej markerów
  return ($pl * 3) - ($mk * 4)
}

function Undo-Mojibake-Candidates([string]$s) {
  # A) treat current string bytes as CP-1250, reinterpret as UTF-8
  $a = $Utf8NoBom.GetString($Enc1250.GetBytes($s))
  # B) same, but CP-1252
  $b = $Utf8NoBom.GetString($Enc1252.GetBytes($s))
  # C) two-pass variants (czasem pomaga)
  $c = $Utf8NoBom.GetString($Enc1250.GetBytes($b))
  $d = $Utf8NoBom.GetString($Enc1252.GetBytes($a))
  return @($a,$b,$c,$d) | Select-Object -Unique
}

function Fix-HeaderIds([string]$text) {
  # Replace: "## Title {#id}"  -> "## Title {: #id }"
  # Only when {#...} is at end of heading line.
  $lines = $text -split "`r?`n"
  for($i=0;$i -lt $lines.Length;$i++){
    $line = $lines[$i]
    if ($line -match '^\s*#{1,6}.*\{#([A-Za-z0-9\-\._]+)\}\s*$') {
      $id = $Matches[1]
      $line = ($line -replace '\s*\{#[A-Za-z0-9\-\._]+\}\s*$', " {: #$id }")
      $lines[$i] = $line
    }
  }
  return ($lines -join "`r`n")
}

function Process-File([string]$file) {
  $bytes = Read-Bytes $file

  # case 1: bytes are valid UTF-8
  $isUtf8,$text = Try-Decode-UTF8 $bytes
  $changed = $false
  $note = ""

  if ($isUtf8) {
    $origScore = Score $text
    $markers   = Count-By $text $MarkerSet

    if ($markers -gt 0) {
      $bestText = $text
      $bestScore = $origScore
      foreach($cand in (Undo-Mojibake-Candidates $text)) {
        $s = Score $cand
        if ($s -gt $bestScore) {
          $bestScore = $s
          $bestText  = $cand
        }
      }
      if ($bestText -ne $text) {
        $text = $bestText
        $changed = $true
        $note = "utf8-mojibake->utf8"
      }
    }

    if ($FixHeaderIds) {
      $t2 = Fix-HeaderIds $text
      if ($t2 -ne $text) {
        $text = $t2
        $changed = $true
        $note = if ($note) { "$note + headerid" } else { "headerid" }
      }
    }

    if ($changed) {
      [System.IO.File]::WriteAllText($file, $text, $Utf8NoBom)
      return ,$true,$note
    } else {
      return ,$false,""
    }
  }
  else {
    # case 2: not UTF-8 -> assume CP1250, convert to UTF-8
    $text1250 = $Enc1250.GetString($bytes)
    if (-not [string]::IsNullOrEmpty($text1250)) {
      if ($FixHeaderIds) { $text1250 = Fix-HeaderIds $text1250 }
      [System.IO.File]::WriteAllText($file, $text1250, $Utf8NoBom)
      return ,$true,"cp1250->utf8"
    } else {
      # fallback: try CP-1252
      $text1252 = $Enc1252.GetString($bytes)
      if ($FixHeaderIds) { $text1252 = Fix-HeaderIds $text1252 }
      [System.IO.File]::WriteAllText($file, $text1252, $Utf8NoBom)
      return ,$true,"cp1252->utf8"
    }
  }
}

if (-not (Test-Path $Path)) { Write-Error "Path not found: $Path" }

$all = Get-ChildItem $Path -Recurse -Filter *.md
$changed = 0
$unchanged = 0

# safety backup
$stamp = (Get-Date).ToString("yyyyMMdd_HHmmss")
$backupDir = ".\__md_backup_$stamp"
Write-Host "Backup to: $backupDir"
Copy-Item $Path $backupDir -Recurse -Force

foreach($f in $all){
  $ok,$note = Process-File $f.FullName
  if ($ok) {
    $changed++
    Write-Host ("Fix: {0} ({1})" -f $f.FullName, $note)
  } else {
    $unchanged++
  }
}

Write-Host ""
Write-Host ("Checked:  {0}" -f $all.Count)
Write-Host ("Changed:  {0}" -f $changed)
Write-Host ("Unchanged:{0}" -f $unchanged)

# git commit (no push)
try {
  git add -A
  git commit -m "docs: fix encoding (mojibake CP1250/CP1252 -> UTF-8, header ids optional)"
  Write-Host "Commit created. Run: git push"
} catch {
  Write-Warning "Commit not created (maybe no changes)."
}

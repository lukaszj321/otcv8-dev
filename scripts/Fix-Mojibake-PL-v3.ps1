param(
  [string]$Path = ".\docs"
)

$ErrorActionPreference = "Stop"

# Encodings
$Utf8Strict = New-Object System.Text.UTF8Encoding($false, $true) # no BOM, strict
$Utf8NoBom  = New-Object System.Text.UTF8Encoding($false)        # no BOM
$Enc1250    = [System.Text.Encoding]::GetEncoding(1250)
$Enc1252    = [System.Text.Encoding]::GetEncoding(1252)

function Read-Text([string]$file){
  $bytes = [System.IO.File]::ReadAllBytes($file)
  try {
    return $true, ($Utf8Strict.GetString($bytes))
  } catch {
    try { return $false, $Enc1250.GetString($bytes) } catch {}
    try { return $false, $Enc1252.GetString($bytes) } catch {}
    return $false, ([System.Text.Encoding]::UTF8.GetString($bytes))
  }
}

# Ogólne sprzątanie po treści
function Tidy-Text([string]$s){
  $t = $s

  # 1) Usuń BOM na początku
  $t = $t -replace "^\uFEFF",""

  # 2) Jeśli wyglada na „podwójny UTF-8”, spróbuj 2 rund re-dekodowania CP1252->UTF8
  for($i=0; $i -lt 2; $i++){
    if($t -match "[\u00C3\u00C4\u00C5]"){  # 'Ã', 'Ä', 'Å'
      $bytes1252 = $Enc1252.GetBytes($t)
      $t = [System.Text.Encoding]::UTF8.GetString($bytes1252)
    } else {
      break
    }
  }

  # 3) Normalizacje białych znaków/specjalnych
  $t = $t -replace "\u00A0"," "    # NBSP -> spacja
  $t = $t -replace "\u2011","-"    # NO-BREAK HYPHEN -> zwykły '-'
  $t = $t -replace "\u00C2",""     # samotne 'Â' -> usuń

  # 4) Artefakty na początku pliku typu "? # ..." lub "?# ..."
  $t = $t -replace "^\?+\s*#\s","# "

  # 5) „Ł” zniekształcone jako '¦' (U+00A6)
  $t = $t -replace "\u00A6","Ł"

  # 6) Poprawka kontekstowa tytułów „Moduł” (bezpieczna, z dwukropkiem po słowie)
  $t = $t -replace "(\n|^)\#\s+Modul:","`n# Moduł:"

  return $t
}

if(-not (Test-Path $Path)){ Write-Error "Path not found: $Path" }

$stamp = (Get-Date).ToString("yyyyMMdd_HHmmss")
$backupDir = ".\__md_backup_$stamp"
Write-Host "Backup -> $backupDir"
Copy-Item $Path $backupDir -Recurse -Force

$files = Get-ChildItem $Path -Recurse -Filter *.md
$changed = 0; $unchanged = 0

foreach($f in $files){
  $isUtf8,$text = Read-Text $f.FullName
  if([string]::IsNullOrEmpty($text)){ $unchanged++; continue }

  $orig = $text
  $fix  = Tidy-Text $text

  if($fix -ne $orig){
    [System.IO.File]::WriteAllText($f.FullName, $fix, $Utf8NoBom)
    Write-Host "Fix: $($f.FullName)"
    $changed++
  } else {
    $unchanged++
  }
}

Write-Host ""
Write-Host "Checked:  $($files.Count)"
Write-Host "Changed:  $changed"
Write-Host "Unchanged:$unchanged"

try {
  git add -A
  git commit -m "docs: mojibake fix v3 (double-UTF8 decode, nbsp/nbhyphen, header/artifacts, ¦->Ł, Modul->Moduł)"
  Write-Host "Commit created. Run: git push"
} catch {
  Write-Warning "Commit not created (maybe no changes)."
}

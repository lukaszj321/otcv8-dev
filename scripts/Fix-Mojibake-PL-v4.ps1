param(
  [Parameter(Mandatory=$true)][string]$Path,
  [switch]$Apply
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Read-Bytes($p){ [System.IO.File]::ReadAllBytes($p) }
function Write-Utf8NoBom($p,[string]$s){
  $enc = New-Object System.Text.UTF8Encoding($false)
  [System.IO.File]::WriteAllText($p,$s,$enc)
}

# --- Heurystyki jakości ---
$pl = '[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]'
$junk = '[ÂÃÄÅ]|�'   # '�' to U+FFFD; w PS może się pokazać jako dziwny glif

function Score([string]$s){
  $good = ([regex]::Matches($s,$pl)).Count
  $bad  = ([regex]::Matches($s,$junk)).Count
  return $good*10 - $bad*8
}

# --- Tabele twardych zamian (typografia + PL) ---
$map = [ordered]@{}
# typografia Windows -> Unicode
$map.Add('â€”','—')
$map.Add('â€“','–')
$map.Add('â€¦','…')
$map.Add('â€ž','„')
$map.Add('â€ś','“')
$map.Add('â€ť','”')
$map.Add([string]::Concat([char]0x00E2,[char]0x20AC,[char]0x0161),[char]0x201A)
$map.Add([string]::Concat([char]0x00E2,[char]0x20AC,[char]0x2019),[char]0x2019)
$map.Add([string]::Concat([char]0x00E2,[char]0x20AC,[char]0x2018),[char]0x2018)
$map.Add('Â·','·')
$map.Add('Â non-breaking',' ') # sanity
$map.Add('Â ',' ')
# NBSP -> space (use explicit char to avoid source-encoding issues)
$map.Add([char]0x00A0,' ')

# popularne pary mojibake (CP1252)
$map.Add('Ä…','ą')
$map.Add('Ä‡','ć')
$map.Add('Ä™','ę')
$map.Add("Å‚","ł")
$map.Add('Å„','ń')
$map.Add('Ã³','ó')
$map.Add('Å›','ś')
$map.Add('Åº','ź')
$map.Add('Å¼','ż')
$map.Add('Ä„','Ą')
$map.Add("Ä†","Ć")
$map.Add("Ä˜","Ę")
$map.Add("Å�","Ł")
$map.Add("Åƒ","Ń")
$map.Add([string]::Concat([char]0x00C3,[char]0x0093),[char]0x00D3)
$map.Add([string]::Concat([char]0x00C5,[char]0x009A),[char]0x015A)
$map.Add([string]::Concat([char]0x00C5,[char]0x00B9),[char]0x0179)
$map.Add([string]::Concat([char]0x00C5,[char]0x00BB),[char]0x017B)

# mega-skaszane warianty (CP1250/Latin2)
$map.Add([string]::Concat([char]0x00C3,[char]0x0085),[char]0x00C5)
$map.Add([string]::Concat([char]0x00C3,[char]0x0084),[char]0x00C4)
$map.Add("Ã‚","Â")
$map.Add('Äą','ą'); $map.Add('Ä‡','ć'); $map.Add('Ä™','ę')
$map.Add('ÂŁ','Ł'); $map.Add('Âł','ł')

# ręczne poprawki najczęstszych tytułów
$map.Add('Modul:','Moduł:'); $map.Add('modul-','moduł-');

function Hard-Replace([string]$s){
  foreach($k in $map.Keys){ $s = $s -replace [regex]::Escape($k), $map[$k] }
  return $s
}

# --- Próby re-dekodowania ---
$encLatin1 = [System.Text.Encoding]::GetEncoding(28591) # ISO-8859-1
$enc1252   = [System.Text.Encoding]::GetEncoding(1252)
$enc1250   = [System.Text.Encoding]::GetEncoding(1250)
$utf8      = New-Object System.Text.UTF8Encoding($false)

function Try-Recode([string]$s,[System.Text.Encoding]$from){
  # interpretuj *obecną* treść jako znaki z $from -> bajty -> odczytaj jako UTF-8
  $bytes = $from.GetBytes($s)
  try { return $utf8.GetString($bytes) } catch { return $s }
}

function Demojibake([string]$s){
  $best = $s; $bestScore = Score($best)

  $candidates = New-Object System.Collections.Generic.List[string]
  $candidates.Add( (Try-Recode $s $enc1252) )
  $candidates.Add( (Try-Recode $s $enc1250) )
  $candidates.Add( (Try-Recode $s $encLatin1) )

  # wieloprzebiegowo (złóż kilka razy, bo część jest podwójnie zmasakrowana)
  foreach($c in @($candidates + ($candidates | ForEach-Object { Try-Recode $_ $enc1252 }) + ($candidates | ForEach-Object { Try-Recode $_ $enc1250 })) ){
    $t = Hard-Replace $c
    $t = $t -replace '\u00A0',' '  # NBSP
    $score = Score($t)
    if($score -gt $bestScore){ $best=$t; $bestScore=$score }
  }

  # jeszcze raz twarde zamiany na końcu
  $best = Hard-Replace $best
  return $best
}

function Fix-Headers([string]$s){
  # naprawy ID-ków: '{#id}' -> '{: #id }'
  $s = $s -replace '^(#+[^\r\n]*?)\s*\{#([^\}]+)\}\s*$','$1 {: #$2 }' -replace 'Â',''
  # normalizacja tytułów “Moduł: …”
  $s = $s -replace '^\s*#\s*Modul\s*:','# Moduł:'
  return $s
}

$root = Resolve-Path $Path
$files = Get-ChildItem $root -Recurse -Filter *.md
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupDir = Join-Path (Split-Path $root -Parent) ("__md_backup_" + $timestamp)
New-Item $backupDir -ItemType Directory | Out-Null

Write-Host "Backup -> $backupDir"

$changed=0;$checked=0
$badLeft=@()
foreach($f in $files){
  $checked++
  $bytes = Read-Bytes $f.FullName

  # 1) spróbuj UTF-8 (bez BOM)
  $text = $null
  try { $text = [System.Text.Encoding]::UTF8.GetString($bytes) } catch { $text = $null }

  if(-not $text){ # 2) jeżeli nie wyszło – czytaj binarnie jako 1250 (stare windowsowe)
    try { $text = $enc1250.GetString($bytes) } catch { $text = $enc1252.GetString($bytes) }
  }

  $orig = $text
  $t = $text

  # 3) demojibake wieloprzebiegowo
  $t = Demojibake $t

  # 4) porządki nagłówków + BOM strip
  $t = $t -replace '^\uFEFF','' | Out-String
  $t = Fix-Headers $t

  # 5) dodatkowe: zlepione backticki w blokach ``` (czasem po konwersji)
  $t = $t -replace '`\s+`','``'

  if($t -ne $orig){
    if($Apply){
      # backup pojedynczego pliku do struktury backupu
      $rel = Resolve-Path $f.FullName | Split-Path -NoQualifier
      $dst = Join-Path $backupDir $rel
      New-Item (Split-Path $dst -Parent) -ItemType Directory -Force | Out-Null
      Copy-Item $f.FullName $dst -Force

      Write-Utf8NoBom $f.FullName $t
    }
    Write-Host "Fix: $($f.FullName)"
    $changed++
  }

  # 6) raport: czy zostały śmieci?
  if($t -match $junk){ $badLeft += $f.FullName }
}

Write-Host ""
Write-Host ("Checked: {0,4}" -f $checked)
Write-Host ("Changed: {0,4}" -f $changed)
Write-Host ("Unchanged:{0,4}" -f ($checked-$changed))

if($Apply){
  try {
    git add $Path | Out-Null
    git commit -m "docs: mojibake fix v4 (UTF8<->CP1252/CP1250 multi-pass, typografia, headers, UTF-8 no BOM)" | Out-Null
    Write-Host "Commit created. Run: git push"
  } catch {
    Write-Warning "Nie udało się zrobić commita (może brak zmian)."
  }
}

# 7) twardy raport końcowy – co jeszcze jest do poprawy ręcznie
if($badLeft.Count -gt 0){
  Write-Warning "WYKRYTO RESZTKI ŚMIECI (Â/Ã/Ä/Å/�) – pliki poniżej wymagają ręcznej weryfikacji:"
  $badLeft | Sort-Object -Unique | ForEach-Object { Write-Host " - $_" }
} else {
  Write-Host "OK: brak znanych markerów mojibake w *.md"
}

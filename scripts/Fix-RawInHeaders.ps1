param(
  [Parameter(Mandatory=$true)]
  [string]$Path,          # np. ".\docs"
  [switch]$Apply          # bez -Apply działa w trybie podglądu
)

# Zbierz pliki MD
$mdFiles = Get-ChildItem -Path $Path -Recurse -Filter *.md -File

$changed = 0
foreach($f in $mdFiles){
  $orig = Get-Content $f.FullName -Raw
  $text = $orig

  # --- KROK 1: usuń "nagłówek+raw" w jednej linii ---
  # np. "# {% raw %}"
  $text = $text -replace '(?mi)^\s*#\s*\{\%\s*raw\s*\%\}\s*[\r\n]+', ''

  # --- KROK 2: jeśli raw/endraw są w pierwszych 10 liniach, usuń je ---
  $lines = $text -split "\r?\n", -1
  $limit = [Math]::Min(10, $lines.Count)
  $changedHeader = $false
  for($i=0; $i -lt $limit; $i++){
    if($lines[$i] -match '^\s*\{\%\s*(endraw|raw)\s*\%\}\s*$'){
      $lines[$i] = ''
      $changedHeader = $true
    }
  }
  if($changedHeader){ $text = ($lines -join "`r`n") }

  # --- KROK 3: sprzątanie: usuń nadmiar pustych linii na początku ---
  $lines = $text -split "\r?\n", -1
  while($lines.Count -gt 0 -and $lines[0] -match '^\s*$'){ $lines = $lines[1..($lines.Count-1)] }

  # --- KROK 4: jeśli pierwsza linia to już nie H1, spróbuj zachować istniejący tytuł albo wstawić domyślny ---
  if($lines.Count -eq 0){
    $lines = @('# Documentation', '')
  } elseif($lines[0] -notmatch '^\s*#\s+'){
    # jeżeli pierwsza linia wygląda jak nagłówek bez hashy (np. sam tekst), podnieś do H1
    if($lines[0] -match '^[^\#\s].{0,120}$'){
      $lines = @('# ' + $lines[0], '') + $lines[1..($lines.Count-1)]
    } else {
      $lines = @('# Documentation', '') + $lines
    }
  }

  $newText = ($lines -join "`r`n")

  if($newText -ne $orig){
    if($Apply){
      # backup
      Copy-Item $f.FullName ($f.FullName + ".bak") -Force
      Set-Content $f.FullName $newText -Encoding UTF8
      Write-Host "Fix: $($f.FullName)"
    } else {
      Write-Host "Would fix: $($f.FullName)"
    }
    $changed++
  }
}

Write-Host ""
Write-Host "Checked: $($mdFiles.Count)"
Write-Host "Changed: $changed"
Write-Host "Unchanged: $($mdFiles.Count - $changed)"
Write-Host ""
if(-not $Apply){ Write-Host "Preview mode. Use -Apply to write changes (creates .bak)." }

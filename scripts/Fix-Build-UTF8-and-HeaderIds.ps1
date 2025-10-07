param(
  [Parameter(Mandatory=$true)]
  [string]$Path # np. ".\docs"
)

if(-not (Test-Path $Path)){ Write-Error "Nie znaleziono: $Path"; exit 1 }

Write-Host "=== 1/2: Normalizacja kodowania na UTF-8 (bez BOM) dla *.md ==="

# Funkcja: bezpieczny zapis UTF-8 (bez BOM) także na Windows PowerShell 5.x
function Save-Utf8NoBom([string]$File, [string]$Content){
  $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
  [System.IO.File]::WriteAllText((Resolve-Path $File), $Content, $utf8NoBom)
}

# Przejście po wszystkich .md i wymuszenie UTF-8 + LF
$mdFiles = Get-ChildItem -Path $Path -Recurse -Filter *.md
$utfFixed = 0
foreach($f in $mdFiles){
  # wczytaj surowo (nie zmieniaj niczego w treści poza końcami linii)
  $raw = Get-Content -LiteralPath $f.FullName -Raw
  # Ujednolicenie końców linii do \n (Linux), żeby nie mieszać CRLF/LF
  $nl = $raw -replace "`r`n", "`n"
  # Zapis UTF-8 bez BOM
  Save-Utf8NoBom -File $f.FullName -Content $nl
  $utfFixed++
}
Write-Host ("Zapisano w UTF-8 (bez BOM): {0} plików .md" -f $utfFixed)

Write-Host "`n=== 2/2: Naprawa ID w nagłówkach '{#id}' -> '{: #id }' ==="

# Wzorzec: linie nagłówków (# ... ) zawierające goły '{#...}'
# Zamieniamy TYLKO w nagłówkach, na składnię attr_list '{: #... }'
$headersFixed = 0
$targetFiles = Get-ChildItem -Path $Path -Recurse -Filter *.md
foreach($f in $targetFiles){
  $text = Get-Content -LiteralPath $f.FullName -Raw
  $before = $text

  # Tylko w liniach nagłówków (początek linii: 1..6 #)
  # Zamień '{#coś}' na '{: #coś }'
  $text = [Regex]::Replace(
    $text,
    '^(#{1,6}[^\r\n]*?)\s*\{#([A-Za-z0-9\-_:.]+)\}\s*$',
    '$1 {: #$2 }',
    [System.Text.RegularExpressions.RegexOptions]::Multiline
  )

  if($text -ne $before){
    Save-Utf8NoBom -File $f.FullName -Content $text
    $headersFixed++
  }
}

Write-Host ("Naprawione nagłówki z ID: {0} plik(ów)" -f $headersFixed)

Write-Host "`nDone."

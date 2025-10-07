# Zapisz jako: scripts\Fix-CorelibUi-Jinja.ps1
param(
  [Parameter(Mandatory=$true)][string]$Path # np. ".\docs\modules\structured\dev_tools\modul-corelib-ui.md"
)

if(-not (Test-Path $Path)){ Write-Error "Nie ma pliku: $Path"; exit 1 }

$txt = Get-Content -Raw -LiteralPath $Path

# Minimalna i bezpieczna zmiana: zamieniamy podwójne klamry na zwykły literał tablicy Lua
# Przykład:
#   ... , {{text='Ok', callback=defaultCallback}}, ...
# staje się
#   ... , { { text = 'Ok', callback = defaultCallback } }, ...

$replacements = @(
  @{ from = "\{\{text='Ok',\s*callback=defaultCallback\}\}"
     to   = "{ { text = 'Ok', callback = defaultCallback } }" },
  @{ from = "\{\{text='Cancel',\s*callback=defaultCallback\}\}"
     to   = "{ { text = 'Cancel', callback = defaultCallback } }" }
)

$changed = $false
foreach($r in $replacements){
  $new = [regex]::Replace($txt, $r.from, $r.to)
  if($new -ne $txt){ $changed = $true; $txt = $new }
}

if($changed){
  Copy-Item -LiteralPath $Path -Destination ($Path + ".bak") -Force
  Set-Content -LiteralPath $Path -Value $txt -NoNewline
  Write-Host "Poprawiono: $Path (backup: $Path.bak)"
}else{
  Write-Host "Brak zmian: $Path (nie znaleziono wzorców)"
}

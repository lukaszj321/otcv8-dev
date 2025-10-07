<# 
Fix-MkDocsMd.ps1 (v2 - safe)
Użycie:
  # podgląd (bez zapisu)
  powershell -NoProfile -File ".\scripts\Fix-MkDocsMd.ps1" -Path ".\docs"

  # zapisz zmiany (tworzy *.bak obok plików .md)
  powershell -NoProfile -File ".\scripts\Fix-MkDocsMd.ps1" -Path ".\docs" -Apply
#>

[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [string]$Path,
  [switch]$Apply
)

# --- tylko .md, bez .bak i z wykluczeniami katalogów -----------------------
$ExcludeDirs = @(
  '\downloads\', '\_rag\', '\rag\', '\_assets\'   # nic tu nie tykamy
)

function Get-MdFiles {
  param([string]$Root)
  if (-not (Test-Path -LiteralPath $Root)) { throw "Ścieżka nie istnieje: $Root" }

  $all = Get-ChildItem -LiteralPath $Root -Recurse -File
  $md  = $all | Where-Object {
    $_.Extension -ieq '.md' -and
    $_.FullName -notmatch '\.bak$' -and
    ($ExcludeDirs | ForEach-Object { $_ -notmatch '' } | Out-Null; $true) -and
    ($ExcludeDirs | Where-Object { $_ -and ($_.ToLower() -as [string]) } | Out-Null; $true)
  }

  # ręcznie odfiltruj katalogi wykluczone
  $md = $md | Where-Object {
    $full = $_.FullName.ToLower()
    -not ($ExcludeDirs | Where-Object { $full -like "*$($_.Trim('\')).ToLower()*" })
  }

  return $md
}

function Read-TextUtf8 { param([string]$File) [System.IO.File]::ReadAllText($File,[System.Text.Encoding]::UTF8) }
function Write-TextUtf8 { param([string]$File,[string]$Text) [System.IO.File]::WriteAllText($File,$Text,[System.Text.Encoding]::UTF8) }

# --- Transformacje ----------------------------------------------------------
function Remove-InvisibleChars {
  param([string]$Text)
  $zwsp = [char]0x200B; $shy  = [char]0x00AD; $bom  = [char]0xFEFF
  $Text = $Text -replace [regex]::Escape("$bom"), ""
  $Text = $Text -replace [regex]::Escape("$zwsp"), ""
  $Text = $Text -replace [regex]::Escape("$shy"), ""
  return $Text
}
function Normalize-Headings {
  param([string]$Text)
  $Text = $Text -replace '(?m)^\s*(\#{1,6})\s*', '$1 '
  $Text = $Text -replace '(?m)^(\#{1,6})\s+(.*)$', '$1 $2'
  return $Text
}
function Join-OneCharLines {
  param([string]$Text)
  $lines = $Text -split "`r?`n",-1
  $out = New-Object System.Collections.Generic.List[string]
  $buffer = New-Object System.Collections.Generic.List[string]

  function Flush-Buffer([System.Collections.Generic.List[string]]$buf,[System.Collections.Generic.List[string]]$dst){
    if ($buf.Count -ge 6) { $dst.Add((($buf -join '') -replace '\s{2,}',' ')) }
    else { foreach ($b in $buf) { $dst.Add($b) } }
    $buf.Clear()
  }

  foreach ($ln in $lines) {
    $trim = $ln.Trim()
    if ($trim -match '^[\p{L}\p{N}\p{P}]{1,2}$') { $buffer.Add($trim) }
    else { if ($buffer.Count -gt 0) { Flush-Buffer $buffer $out }; $out.Add($ln) }
  }
  if ($buffer.Count -gt 0) { Flush-Buffer $buffer $out }
  return ($out -join "`r`n")
}
function Fix-RawBlocks {
  param([string]$Text)
  $open  = ([regex]'{%\s*raw\s*%}').Matches($Text).Count
  $close = ([regex]'{%\s*endraw\s*%}').Matches($Text).Count
  if ($open -gt $close) { $Text = $Text.TrimEnd() + "`r`n" + ("{% endraw %}`r`n" * ($open - $close)) }
  return $Text
}
function Normalize-BlankLines {
  param([string]$Text)
  $Text = ($Text -replace '(?m)^\s+$','').TrimEnd()
  $Text = ($Text -split "`r?`n") -join "`r`n"
  return $Text + "`r`n"
}

# --- Główna pętla -----------------------------------------------------------
$files = Get-MdFiles -Root $Path
$checked = 0; $changed = 0; $unchanged = 0; $changedList = @()

foreach ($f in $files) {
  $checked++
  $orig = Read-TextUtf8 -File $f.FullName
  $txt  = $orig

  $txt = Remove-InvisibleChars  $txt
  $txt = Normalize-Headings     $txt
  $txt = Join-OneCharLines      $txt
  $txt = Fix-RawBlocks          $txt
  $txt = Normalize-BlankLines   $txt

  if ($txt -ne $orig) {
    $changed++; $changedList += $f.FullName
    if ($Apply) {
      $bak = "$($f.FullName).bak"
      if (-not (Test-Path $bak)) { Copy-Item -LiteralPath $f.FullName -Destination $bak -Force }
      Write-TextUtf8 -File $f.FullName -Text $txt
      Write-Host "Fix: $($f.FullName)" -ForegroundColor Cyan
    }
  } else { $unchanged++ }
}

Write-Host ""
Write-Host "Checked: $checked files" -ForegroundColor Yellow
Write-Host "Changed: $changed" -ForegroundColor Green
Write-Host "Unchanged: $unchanged" -ForegroundColor Gray
Write-Host ""
if ($Apply) { Write-Host "Apply mode. Changes written. Backups *.bak created next to .md files." -ForegroundColor Green }
else { Write-Host "Preview mode. Use -Apply to write changes (creates .bak for .md)." -ForegroundColor Yellow }
if ($changedList.Count -gt 0) {
  Write-Host "`nChanged files:" -ForegroundColor Yellow
  $changedList | ForEach-Object { Write-Host " - $_" }
}

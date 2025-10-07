<#  Fix-MkDocsMd.ps1
    - Walks docs/, fixes broken headings (one-letter-per-line blocks),
      ensures a proper H1/title, trims BOMs, normalizes line endings,
      and optionally writes changes with .bak backups.

    Usage:
      # preview
      powershell -NoProfile -File .\scripts\Fix-MkDocsMd.ps1 -Path .\docs

      # apply (creates .bak next to each changed file)
      powershell -NoProfile -File .\scripts\Fix-MkDocsMd.ps1 -Path .\docs -Apply
#>

[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [string]$Path,
  [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-MdFiles([string]$root) {
  if (-not (Test-Path $root)) { throw "Path not found: $root" }
  Get-ChildItem -Path $root -Recurse -Include *.md -File
}

function Normalize-LineEndings([string]$text) {
  $text -replace "(`r`n|`r|`n)", "`r`n"
}

function Remove-UTF8-BOM([byte[]]$bytes) {
  if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    return ,$bytes[3..($bytes.Length-1)]
  }
  return ,$bytes
}

function Join-OneCharLines([string]$text) {
  $lines = $text -split "`r`n"
  $out = New-Object System.Collections.Generic.List[string]
  $i = 0
  while ($i -lt $lines.Count) {
    $j = $i
    while ($j -lt $lines.Count) {
      $l = $lines[$j].Trim()
      if ($l.Length -le 2 -and $l -ne '') { $j++; continue }
      break
    }
    $runLen = $j - $i
    if ($runLen -ge 10) {
      $joined = ($lines[$i..($j-1)] | ForEach-Object { $_.Trim() }) -join ''
      if ($out.Count -gt 0 -and $out[$out.Count-1] -ne '') { $out.Add('') }
      $out.Add($joined)
      $out.Add('')
      $i = $j
    } else {
      $out.Add($lines[$i])
      $i++
    }
  }
  ($out -join "`r`n")
}

function Ensure-H1([string]$text, [string]$filePath) {
  # Work on a List[string], not an array (PS 5.1 safe)
  $arr = $text -split "`r`n"
  $lines = New-Object System.Collections.Generic.List[string]
  $lines.AddRange($arr)

  # skip YAML front matter
  $start = 0
  if ($lines.Count -gt 0 -and $lines[0].Trim() -eq '---') {
    $k = 1
    while ($k -lt $lines.Count -and $lines[$k].Trim() -ne '---') { $k++ }
    if ($k -lt $lines.Count) { $start = $k + 1 }
  }

  # find first non-empty line
  $firstIdx = -1
  for ($ix = $start; $ix -lt $lines.Count; $ix++) {
    if ($lines[$ix] -match '\S') { $firstIdx = [int]$ix; break }
  }

  if ($firstIdx -eq -1) {
    $title = [IO.Path]::GetFileNameWithoutExtension($filePath) -replace '_',' ' -replace '-',' '
    return "# $title`r`n"
  }

  $firstLine = $lines[$firstIdx]

  if ($firstLine -match '^\s*#\s+') {
    $title = $firstLine -replace '^\s*#\s+','# '
    $lines[$firstIdx] = $title.TrimEnd()
  }
  elseif ($firstLine -match '^\s*<h1[^>]*>.*</h1>\s*$') {
    $titleText = ($firstLine -replace '^\s*<h1[^>]*>','' -replace '</h1>\s*$','').Trim()
    $lines[$firstIdx] = "# $titleText"
  }
  else {
    if ($firstLine -notmatch '^\s*#{2,}\s+') {
      $lines[$firstIdx] = ("# " + $firstLine).TrimEnd()
    }
  }

  # remove duplicate H1 within next 5 lines
  $toRemove = @()
  $maxCheck = [Math]::Min($firstIdx + 5, $lines.Count - 1)
  for ($j = $firstIdx + 1; $j -le $maxCheck; $j++) {
    if ($lines[$j] -match '^\s*#\s+') { $toRemove += $j }
  }
  # remove from bottom to top to keep indices valid
  foreach ($idx in ($toRemove | Sort-Object -Descending)) {
    $lines.RemoveAt([int]$idx)
  }

  ($lines -join "`r`n")
}

function Fix-File([IO.FileInfo]$file, [switch]$apply) {
  $raw = [IO.File]::ReadAllBytes($file.FullName)
  $raw = Remove-UTF8-BOM $raw
  $text = [System.Text.Encoding]::UTF8.GetString($raw)

  $orig = $text

  $text = Normalize-LineEndings $text
  $text = Join-OneCharLines $text
  $text = Ensure-H1 $text $file.FullName

  $changed = ($text -ne $orig)
  if ($changed -and $apply) {
    $bak = "$($file.FullName).bak"
    if (-not (Test-Path $bak)) { Copy-Item -Path $file.FullName -Destination $bak -Force }
    [IO.File]::WriteAllText($file.FullName, $text, (New-Object System.Text.UTF8Encoding($false)))
  }

  [PSCustomObject]@{
    File    = $file.FullName
    Changed = $changed
  }
}

# MAIN
$files = Get-MdFiles -root $Path
if ($files.Count -eq 0) {
  Write-Host "No markdown files found under: $Path" -ForegroundColor Yellow
  exit 0
}

$results = foreach ($f in $files) { Fix-File -file $f -apply:$Apply.IsPresent }

$changed = $results | Where-Object { $_.Changed }
$unchanged = $results | Where-Object { -not $_.Changed }

Write-Host "Checked: $($results.Count) files" -ForegroundColor Cyan
Write-Host "Changed: $($changed.Count)" -ForegroundColor Cyan
Write-Host "Unchanged: $($unchanged.Count)" -ForegroundColor DarkGray

if (-not $Apply) {
  Write-Host ""
  Write-Host "Preview mode. Use -Apply to write changes (creates .bak)." -ForegroundColor Yellow
} else {
  Write-Host ""
  Write-Host "Apply mode. Changes written. Backups *.bak created next to files." -ForegroundColor Green
}

if ($changed.Count -gt 0) {
  Write-Host ""
  Write-Host "Changed files:" -ForegroundColor Cyan
  $changed.File | ForEach-Object { Write-Host " - $_" }
}

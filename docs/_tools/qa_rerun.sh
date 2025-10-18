#!/usr/bin/env pwsh
# Requires: PowerShell 7+, Python 3
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# 1) Fix/normalize Mermaid blocks (nie przerywaj na błędach)
try {
  python3 docs/authoring/_tools/diagram_lint_fix.py
} catch {
  Write-Warning "diagram_lint_fix.py: $_"
}

# 2) Link lint -> docs/authoring/qa/link_lint.csv
$qaDir = Join-Path "docs/authoring" "qa"
$null = New-Item -ItemType Directory -Force -Path $qaDir

$outCsv = Join-Path $qaDir "link_lint.csv"
$rows = New-Object System.Collections.Generic.List[object]

Get-ChildItem -Path "docs/authoring" -Recurse -Filter "*.md" | ForEach-Object {
  $md = $_
  $relFile = $md.FullName.Substring((Resolve-Path "docs/authoring").Path.Length + 1).Replace('\','/')
  $txt = Get-Content -LiteralPath $md.FullName -Raw -Encoding UTF8

  $matches = [regex]::Matches($txt, '\]\(([^)#]+)\)')
  foreach ($m in $matches) {
    $link = $m.Groups[1].Value
    if ($link.StartsWith('http') -or $link.StartsWith('mailto') -or $link.StartsWith('#')) { continue }

    # Znormalizuj ścieżkę docelową względem pliku .md
    $targetPath = Join-Path $md.DirectoryName $link
    try {
      $full = [System.IO.Path]::GetFullPath($targetPath)
    } catch {
      $full = $targetPath
    }
    $status = if (Test-Path -LiteralPath $full) { 'OK' } else { 'BROKEN' }
    $rows.Add([pscustomobject]@{ file = $relFile; status = $status; link = $link }) | Out-Null
  }
}

# Zapis CSV (UTF-8 bez BOM)
$rows | Sort-Object file, link | Export-Csv -Path $outCsv -NoTypeInformation -UseQuotes AsNeeded -Encoding utf8
Write-Host "link_lint -> $outCsv"

# 3) CSV sanity (opcjonalnie; nie przerywa)
try {
  python3 docs/authoring/_tools/csv_sanity.py --in docs/authoring/datasets --out docs/authoring/qa/dataset_sanity.csv
} catch {
  Write-Warning "csv_sanity.py: $_"
}

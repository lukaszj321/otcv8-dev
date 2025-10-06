# tools/Split-ModulesDoc.ps1
param(
  [Parameter(Mandatory=$true)][string]$InputFile,
  [string]$OutDir = "",
  [switch]$WrapWithRaw  # add to disable Jinja/macros on pages
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $InputFile)) { throw "File not found: $InputFile" }

# Destination directory (default: alongside source, folder = source name without .md)
$srcDir   = [IO.Path]::GetDirectoryName((Resolve-Path -LiteralPath $InputFile))
$baseName = [IO.Path]::GetFileNameWithoutExtension($InputFile)
if ([string]::IsNullOrWhiteSpace($OutDir)) { $OutDir = Join-Path $srcDir $baseName }
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function New-Slug([string]$s) {
  if ([string]::IsNullOrWhiteSpace($s)) { return "modul" }
  $t = $s.ToLowerInvariant()
  $t = ($t -replace '\s+', '-') -replace '[-_]+','-'
  $t = $t -replace '[^a-z0-9\-]+',''
  $t = $t -replace '^-+','' -replace '-+$',''
  if ([string]::IsNullOrWhiteSpace($t)) { $t = "modul" }
  return $t
}

# Section header regex: "# | Modul:" or "# ¦ Modul:" (pipe or broken bar)
$SectionRegex = '^\s*#\s*[\|\xA6]\s*Modul\s*:\s*(.+?)\s*$'

# Prepare index
$indexPath = Join-Path $OutDir "index.md"
[IO.File]::WriteAllText($indexPath, "# $baseName`n`n## Spis treści`n", $Utf8NoBom)

$currentWriter = $null
$currentTitle  = $null
$sections      = New-Object System.Collections.Generic.List[object]

$in = [System.IO.File]::OpenText((Resolve-Path -LiteralPath $InputFile))
try {
  while (($line = $in.ReadLine()) -ne $null) {
    $m = [regex]::Match($line, $SectionRegex, 'IgnoreCase, CultureInvariant')
    if ($m.Success) {
      # finish previous
      if ($null -ne $currentWriter) {
        if ($WrapWithRaw) { $currentWriter.WriteLine("{% endraw %}") }
        $currentWriter.Flush(); $currentWriter.Dispose(); $currentWriter = $null
      }
      $title = $m.Groups[1].Value.Trim()
      $slug  = New-Slug $title
      $filePath = Join-Path $OutDir ($slug + ".md")
      $currentWriter = New-Object System.IO.StreamWriter($filePath, $false, $Utf8NoBom)

      # page header
      $currentWriter.WriteLine("# $title")
      $currentWriter.WriteLine()
      if ($WrapWithRaw) { $currentWriter.WriteLine("{% raw %}") }

      $sections.Add([pscustomobject]@{ Title = $title; Slug = $slug }) | Out-Null
      continue
    }

    if ($null -ne $currentWriter) {
      $currentWriter.WriteLine($line)
    }
  }
}
finally {
  if ($null -ne $currentWriter) {
    if ($WrapWithRaw) { $currentWriter.WriteLine("{% endraw %}") }
    $currentWriter.Flush(); $currentWriter.Dispose()
  }
  $in.Close(); $in.Dispose()
}

# Build index list
$sb = New-Object System.Text.StringBuilder
foreach ($s in $sections) { [void]$sb.AppendLine("- [$($s.Title)]($($s.Slug)/)") }
[IO.File]::AppendAllText($indexPath, $sb.ToString(), $Utf8NoBom)

Write-Host "[OK] Sections: $($sections.Count)"
Write-Host "[OK] Out dir:  $OutDir"
Write-Host "[OK] Index:    $indexPath"

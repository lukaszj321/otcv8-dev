param(
    [Parameter(Mandatory = $true)] [string]$Path,
    [switch]$Apply,
    [switch]$WrapJinjaInCode
)

function Utf8NoBom { New-Object System.Text.UTF8Encoding($false) }
function Info { param([string]$m) Write-Host $m }

if (-not (Test-Path $Path)) { throw "Path not found: $Path" }

# ===== mapa zamian (‚zly|dobry’) =====
$mapLines = @'
Ä…|ą
Ä‡|ć
Ä™|ę
Å‚|ł
Å„|ń
Ã³|ó
Å›|ś
Å¼|ż
Åº|ź
Ä„|Ą
Ä†|Ć
Ä˜|Ę
Å|Ł
Åƒ|Ń
Ã“|Ó
Åš|Ś
Å»|Ż
Å¹|Ź
Â§|§
Â«|«
Â»|»
Â·|·
Â—|—
Â–|–
â€“|–
â€”|—
â€˘|•
â€ž|„
â€ť|”
â€ś|“
â€º|›
â€¹|‹
Ă˘â‚¬â€ť|—
Ă˘â‚¬Ëœ|‘
Ă˘â‚¬â„˘|’
Ă‹â€Ś|“
Ă‹â€™|”
Ă‰|É
ĂŠ|é
Ăł|ó
'@

$map = [System.Collections.Specialized.OrderedDictionary]::new()
foreach ($line in ($mapLines -split "`r?`n")) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    $parts = $line -split '\|', 2
    if ($parts.Count -eq 2) {
        $k = $parts[0]; $v = $parts[1]
        if (-not $map.Contains($k)) { $map.Add($k, $v) }
    }
}

$files = Get-ChildItem -Path $Path -Recurse -Filter *.md | Sort-Object FullName
$checked = 0; $changed = 0
$changedFiles = New-Object System.Collections.Generic.List[string]

# regex dla nagłówków z ID: {#id} -> {: #id }
$reHeader = [regex]'(?m)^\s{0,3}#{1,6}.*\{#([A-Za-z0-9_.:\-]+)\}\s*$'

foreach ($f in $files) {
    $checked++
    $orig = Get-Content $f.FullName -Raw
    $text = $orig

    # 1) remap „krzaczków”
    foreach ($k in $map.Keys) {
        $text = $text -replace [regex]::Escape([string]$k), [string]$map[$k]
    }

    # 2) {#id} -> {: #id }
    $text = $reHeader.Replace($text, { param($m) ($m.Value -replace '\{#([^\}]+)\}', '{: #' + $m.Groups[1].Value + ' }') })

    # 3) opcjonalnie: wrap {% raw %} dla bloków kodu z '{{' (tylko gdy faktycznie coś owinięto)
    if ($WrapJinjaInCode) {
        $lines = $text -split "`r?`n"
        $out = New-Object System.Collections.Generic.List[string]
        $inFence = $false
        $fenceInfo = ""
        $block = New-Object System.Collections.Generic.List[string]
        $wrapApplied = $false

        for ($i = 0; $i -lt $lines.Count; $i++) {
            $line = $lines[$i]

            if (-not $inFence) {
                if ($line -match '^\s*```') {
                    $inFence = $true
                    $fenceInfo = ($line -replace '^\s*```', '')
                    $block.Clear()
                }
                else {
                    $out.Add($line) | Out-Null
                }
                continue
            }

            # wewnątrz fence
            if ($line -match '^\s*```') {
                $codeJoined = ($block -join "`n")
                $hasDoubleBraces = ($codeJoined -match '\{\{')
                $alreadyRaw = ($codeJoined -match '\{\%\s*raw\s*\%\}') -or ($codeJoined -match '\{\%\s*endraw\s*\%\}')

                if ($hasDoubleBraces -and -not $alreadyRaw) {
                    $out.Add('{% raw %}') | Out-Null
                    $out.Add("```$fenceInfo") | Out-Null
                    foreach ($l in $block) { $out.Add($l) | Out-Null }
                    $out.Add('```') | Out-Null
                    $out.Add('{% endraw %}') | Out-Null
                    $wrapApplied = $true
                }
                else {
                    $out.Add("```$fenceInfo") | Out-Null
                    foreach ($l in $block) { $out.Add($l) | Out-Null }
                    $out.Add('```') | Out-Null
                }

                # zamknięcie
                $inFence = $false
                $fenceInfo = ""
                $block.Clear()
                continue
            }
            else {
                $block.Add($line) | Out-Null
                continue
            }
        }

        # niedomknięty fence – przepisz jak było
        if ($inFence) {
            $out.Add("```$fenceInfo") | Out-Null
            foreach ($l in $block) { $out.Add($l) | Out-Null }
        }

        if ($wrapApplied) {
            $text = ($out -join "`r`n")
        }
    }

    if ($text -ne $orig) {
        if ($Apply) {
            [System.IO.File]::WriteAllText($f.FullName, $text, (Utf8NoBom))
        }
        $changed++; $changedFiles.Add($f.FullName) | Out-Null
    }
}

Info "Checked: $checked"
if ($Apply) {
    Info "Changed: $changed"
    Info ("Unchanged: " + (($checked) - $changed))
}
else {
    Info "Would change: $changed"
    Info "Preview mode. Use -Apply to write changes."
}

if ($changedFiles.Count -gt 0) {
    Write-Host ""
    Write-Host ($(if ($Apply) { "Changed files:" }else { "Would change files:" }))
    $changedFiles | ForEach-Object { Write-Host " - $_" }
}

Info "`n=== Raport resztek nienormalnych znaków (poza ASCII) ==="
# BEZPIECZNY wzorzec (ASCII): pokaż pliki z nie-ASCII
$hits = Select-String -Path $files.FullName -Pattern '[^\u0000-\u007F]' -List
if ($hits) { "Potential leftovers:"; $hits | ForEach-Object { " - $($_.Path)" } } else { "No obvious leftovers found." }

Info "`nPamiętaj o force rebuild Pages (empty commit)."

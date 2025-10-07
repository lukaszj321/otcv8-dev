param(
    [string]$Path = ".\docs",
    [switch]$Apply,
    [string]$StructuredTitle = "Structured modules" # zmień jeśli chcesz inny H1
)

function Fix-File($file, $StructuredTitle) {
    $orig = Get-Content -LiteralPath $file -Raw
    $text = $orig

    # 1) Fix rozjechanych nagłówków: "# # x" -> "# x", "## # y" -> "## y", itd.
    $text = [regex]::Replace($text, '^(?<hash>#{1,6})\s+#\s+(?<rest>.+)$', '${hash} ${rest}', 'Multiline')

    # 2) Specjalna obróbka README w modules/structured
    $rel = $file -replace '\\', '/'
    if ($rel -match '/modules/structured/README\.md$') {

        # usuń surowe dyrektywy w pierwszych ~10 liniach, jeśli są
        $lines = $text -split "`r?`n"
        $limit = [math]::Min($lines.Count, 10)
        for ($i = 0; $i -lt $limit; $i++) {
            if ($lines[$i] -match '^\s*\{\%\s*(raw|endraw)\s*\%\}\s*$') {
                $lines[$i] = ''
            }
        }

        # znajdź pierwszą niepustą linię
        $firstIdx = -1
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i].Trim() -ne '') { $firstIdx = $i; break }
        }

        if ($firstIdx -ge 0) {
            # jeśli to nieprawidłowy H1 (albo "# {% raw %}" wcześniej), ustaw poprawny
            if ($lines[$firstIdx] -notmatch '^\s*#\s+\S') {
                $lines[$firstIdx] = "# $StructuredTitle"
            }
            elseif ($lines[$firstIdx] -match '^\s*#\s*\{\%\s*raw\s*\%\}\s*$') {
                $lines[$firstIdx] = "# $StructuredTitle"
            }
        }
        else {
            # plik pusty? — wstaw H1
            $lines = @("# $StructuredTitle")
        }

        $text = ($lines -join "`r`n")
    }

    if ($text -ne $orig) {
        if ($Apply) {
            Set-Content -LiteralPath $file -Value $text -Encoding UTF8
            "Fix: $file"
        }
        else {
            "Would fix: $file"
        }
        return $true
    }
    return $false
}

# ===== MAIN =====
$changed = 0
$checked = 0

Get-ChildItem -LiteralPath $Path -Recurse -Filter *.md | ForEach-Object {
    $checked++
    if (Fix-File -file $_.FullName -StructuredTitle $StructuredTitle) { $changed++ }
}

""
"Checked: $checked"
"Changed: $changed"
"Unchanged: " + ($checked - $changed)
if (-not $Apply) { "`nPreview mode. Use -Apply to write changes." }

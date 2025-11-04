$ErrorActionPreference = 'Stop'

function Update-ApiCsv {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return }
    $rows = Import-Csv -LiteralPath $Path
    foreach ($row in $rows) {
        $p = $row.source_path
        if ([string]::IsNullOrWhiteSpace($p)) { continue }
        if ($p -notmatch '^src/') {
            if ($p -eq 'resource.h' -or $p -match '^(framework|android|client)(/|\\)') {
                $row.source_path = 'src/' + $p
            }
        }
    }
    $rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding UTF8
}

function Update-ModulesCsv {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return }
    $rows = Import-Csv -LiteralPath $Path
    foreach ($row in $rows) {
        $p = $row.source_path
        if ([string]::IsNullOrWhiteSpace($p)) { continue }
        if ($p -notmatch '^modules/') {
            $row.source_path = 'modules/' + $p
        }
    }
    $rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding UTF8
}

function Update-UiCsv {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return }
    $rows = Import-Csv -LiteralPath $Path
    foreach ($row in $rows) {
        $p = $row.source_path
        if ([string]::IsNullOrWhiteSpace($p)) { continue }
        if ($p -notmatch '^modules/') {
            $row.source_path = 'modules/' + $p
        }
    }
    $rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding UTF8
}

Update-ApiCsv -Path 'docs/authoring/datasets/api.csv'
Update-ModulesCsv -Path 'docs/authoring/datasets/modules.csv'
Update-UiCsv -Path 'docs/authoring/datasets/ui.csv'

Write-Host 'Dataset paths updated.'



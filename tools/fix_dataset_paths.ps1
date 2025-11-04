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

# Additional targeted fixes based on repo layout discovery
try {
    # 1) modules.csv: healthbars lives under mods/, not modules/
    $modulesPath = 'docs/authoring/datasets/modules.csv'
    if (Test-Path -LiteralPath $modulesPath) {
        $rows = Import-Csv -LiteralPath $modulesPath
        $changed = $false
        foreach ($row in $rows) {
            if ($row.source_path -like 'modules/game_healthbars/*') {
                $row.source_path = $row.source_path -replace '^modules/', 'mods/'
                $changed = $true
            }
        }
        if ($changed) {
            $rows | Export-Csv -LiteralPath $modulesPath -NoTypeInformation -Encoding UTF8
            Write-Host 'Adjusted modules.csv: modules/game_healthbars -> mods/game_healthbars'
        }
    }

    # 2) vc16_angle_headers.csv: headers under vc16/angle/include
    $vcHeadersPath = 'docs/authoring/datasets/vc16_angle_headers.csv'
    if (Test-Path -LiteralPath $vcHeadersPath) {
        $rows = Import-Csv -LiteralPath $vcHeadersPath
        $changed = $false
        foreach ($row in $rows) {
            $p = $row.include_path
            if (![string]::IsNullOrWhiteSpace($p) -and $p -like 'vc16/include/*') {
                $row.include_path = $p -replace '^vc16/include/', 'vc16/angle/include/'
                $changed = $true
            }
        }
        if ($changed) {
            $rows | Export-Csv -LiteralPath $vcHeadersPath -NoTypeInformation -Encoding UTF8
            Write-Host 'Adjusted vc16_angle_headers.csv: vc16/include -> vc16/angle/include'
        }
    }
}
catch { Write-Warning $_ }



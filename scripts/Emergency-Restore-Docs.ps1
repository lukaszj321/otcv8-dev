param(
    [string]$Path = ".\docs",
    [switch]$NoGit
)

$ErrorActionPreference = "Stop"

function Timestamp { (Get-Date).ToString("yyyyMMdd_HHmmss") }

if (-not (Test-Path $Path)) {
    Write-Error "Docs folder not found: $Path"
}

# 0) Backup current state
$backupDir = ".\__docs_backup_{0}" -f (Timestamp)
Write-Host "Backup: $backupDir"
Copy-Item $Path $backupDir -Recurse -Force

# 1) Restore from *.md.bak if present
$bakFiles = Get-ChildItem $Path -Recurse -Filter *.md.bak -ErrorAction SilentlyContinue
$restored = 0
if ($bakFiles) {
    foreach ($b in $bakFiles) {
        $dst = $b.FullName -replace '\.bak$', ''
        Copy-Item $b.FullName $dst -Force
        $restored++
    }
    Write-Host "Restored from .md.bak: $restored file(s)."
}
else {
    Write-Warning "No .md.bak files in $Path."
    if (-not $NoGit) {
        try {
            git rev-parse --is-inside-work-tree *> $null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "Trying: git restore --source=HEAD~1 -- docs"
                git restore --worktree --staged --source=HEAD~1 -- docs 2>$null
                if ($LASTEXITCODE -ne 0) {
                    Write-Host "Fallback: git checkout HEAD~1 -- docs"
                    git checkout HEAD~1 -- docs
                }
                Write-Host "Git fallback done."
            }
            else {
                Write-Warning "Not a git repo or git unavailable."
            }
        }
        catch {
            Write-Warning ("Git fallback failed: " + $_.Exception.Message)
        }
    }
}

# 2) Quick scan for mojibake markers (build regex from Unicode code points)
# Markers: U+00C2 (Â), U+0102 (Ă), U+00C4 (Ä), U+0139 (Ĺ), U+013A (ĺ)
$badChars = @([char]0x00C2, [char]0x0102, [char]0x00C4, [char]0x0139, [char]0x013A)
$escaped = $badChars | ForEach-Object { [regex]::Escape([string]$_) }
$pattern = '[' + (($escaped) -join '') + ']'

$bad = @()
try {
    $bad = Select-String -Path (Join-Path $Path "**\*.md") -Pattern $pattern -AllMatches -List -ErrorAction SilentlyContinue
}
catch {}

if ($bad -and $bad.Count -gt 0) {
    Write-Warning "Possible mojibake found in:"
    $bad | ForEach-Object { $_.Path } | Sort-Object -Unique | ForEach-Object { " - $_" }
}
else {
    Write-Host "No obvious mojibake markers in .md (OK)."
}

# 3) Prepare commit (no push)
try {
    git add -A
    git commit -m "docs: emergency restore (.md.bak/HEAD~1) - revert encoding damage"
    Write-Host "Commit created. Next: git push"
}
catch {
    Write-Warning "Commit not created (maybe no changes)."
}

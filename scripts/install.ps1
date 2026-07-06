param(
    [string]$Destination = "$env:USERPROFILE\.codex\skills"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repoRoot "skills"

if (-not (Test-Path $source)) {
    throw "Missing skills directory: $source"
}

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

Get-ChildItem -LiteralPath $source -Directory | ForEach-Object {
    $target = Join-Path $Destination $_.Name
    if (Test-Path $target) {
        Remove-Item -LiteralPath $target -Recurse -Force
    }
    Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force
}

Write-Host "Installed skills to $Destination"

# build-cockpit.ps1
# Regenerates the Claude Project ("cockpit") files from the knowledge base.
# Run after any change to the profile or core notes:
#     powershell -ExecutionPolicy Bypass -File tools/build-cockpit.ps1
#
# Outputs to dist/:
#   - cockpit-custom-instructions.md  -> paste into the Project's "custom instructions"
#   - cockpit-knowledge-bundle.md     -> upload into the Project's "knowledge"

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$dist = Join-Path $root 'dist'
if (-not (Test-Path $dist)) { New-Item -ItemType Directory -Path $dist | Out-Null }

# 1) Custom instructions = the system prompt (the persona + 7-section output)
$sysPrompt = Join-Path $root 'prompts/system-mentor.md'
Copy-Item $sysPrompt (Join-Path $dist 'cockpit-custom-instructions.md') -Force

# 2) Knowledge bundle = the decision-relevant notes, concatenated in priority order
$bundleParts = @(
    'profiles/first-trader.md',
    'library/first-trader/strategy-notes/crypnuevo-trading-dna.md',
    'library/first-trader/setup-examples/crypnuevo-visual-chart-style.md',
    'library/first-trader/setup-examples/crypnuevo-antipatterns-no-trade-rules.md',
    'library/first-trader/strategy-notes/crypnuevo-strategy-map.md',
    'library/first-trader/setup-examples/crypnuevo-before-after-patterns.md',
    'library/first-trader/coverage-and-evolution-audit.md'
)

$bundlePath = Join-Path $dist 'cockpit-knowledge-bundle.md'
$header = @"
# CrypNuevo Trading Mentor — Knowledge Bundle
Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm')
This file is auto-built by tools/build-cockpit.ps1. Do not edit by hand — edit the source notes and rebuild.
Upload this to your Claude Project's knowledge. Set custom instructions from cockpit-custom-instructions.md.

"@
Set-Content -Path $bundlePath -Value $header -Encoding utf8

$included = 0
foreach ($rel in $bundleParts) {
    $full = Join-Path $root $rel
    if (Test-Path $full) {
        Add-Content -Path $bundlePath -Value "`n`n<!-- ===== SOURCE: $rel ===== -->`n" -Encoding utf8
        Add-Content -Path $bundlePath -Value (Get-Content $full -Raw) -Encoding utf8
        $included++
        Write-Host "  + $rel"
    } else {
        Write-Host "  ! missing (skipped): $rel" -ForegroundColor Yellow
    }
}

$sizeKB = [math]::Round((Get-Item $bundlePath).Length / 1KB, 1)
Write-Host ""
Write-Host "Built dist/cockpit-custom-instructions.md"
Write-Host "Built dist/cockpit-knowledge-bundle.md ($included files, $sizeKB KB)"
Write-Host "Next: upload the bundle to your Claude Project knowledge; paste the custom instructions."

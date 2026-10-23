#Requires -Version 5.1
<#
.SYNOPSIS
Packages the manifest, icons, and registered skills as a Copilot Cowork plugin.
.EXAMPLE
.\scripts\Package-Plugin.ps1
.EXAMPLE
.\scripts\Package-Plugin.ps1 -OutputPath output\custom-plugin.zip -Force
#>
[CmdletBinding()]
param(
    [string]$OutputPath = 'output\cowork-exercise-builders.zip',
    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$repoRoot = Split-Path -Parent $PSScriptRoot
$rootPrefix = $repoRoot + [IO.Path]::DirectorySeparatorChar
$files = [Collections.Generic.Dictionary[string, string]]::new([StringComparer]::OrdinalIgnoreCase)

function Resolve-PackagePath {
    param([string]$RelativePath)

    if ([string]::IsNullOrWhiteSpace($RelativePath) -or [IO.Path]::IsPathRooted($RelativePath)) {
        throw "Manifest package paths must be nonempty and relative: '$RelativePath'."
    }
    $path = [IO.Path]::GetFullPath((Join-Path $repoRoot $RelativePath))
    if (-not $path.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Manifest path is outside the repository: '$RelativePath'."
    }
    return $path
}

function Add-PackageFile {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required package file is missing: '$Path'."
    }
    $entryName = $Path.Substring($rootPrefix.Length).Replace('\', '/')
    $files[$entryName] = $Path
}

$manifestPath = Join-Path $repoRoot 'manifest.json'
Add-PackageFile $manifestPath
$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($icon in @($manifest.icons.color, $manifest.icons.outline)) {
    Add-PackageFile (Resolve-PackagePath $icon)
}
if (@($manifest.agentSkills).Count -eq 0) {
    throw 'The manifest must register at least one agent skill.'
}
$skillFolders = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
foreach ($skill in $manifest.agentSkills) {
    $folder = Resolve-PackagePath $skill.folder
    if (-not $skillFolders.Add($folder)) {
        throw "Duplicate skill folder in manifest: '$($skill.folder)'."
    }
    Add-PackageFile (Join-Path $folder 'SKILL.md')
    foreach ($file in Get-ChildItem -LiteralPath $folder -Recurse -File -Force) {
        Add-PackageFile $file.FullName
    }
}

if (-not [IO.Path]::IsPathRooted($OutputPath)) {
    $OutputPath = Join-Path $repoRoot $OutputPath
}
$OutputPath = [IO.Path]::GetFullPath($OutputPath)
if ([IO.Path]::GetExtension($OutputPath) -ine '.zip') {
    throw 'OutputPath must have a .zip extension.'
}
foreach ($folder in $skillFolders) {
    if ($OutputPath.StartsWith($folder + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw 'OutputPath cannot be inside a packaged skill folder.'
    }
}
if ((Test-Path -LiteralPath $OutputPath) -and -not $Force) {
    throw "Output already exists: '$OutputPath'. Use -Force to replace it."
}
if (Test-Path -LiteralPath $OutputPath -PathType Container) {
    throw "OutputPath is a directory: '$OutputPath'."
}

$temporaryZip = [IO.Path]::GetTempFileName()
try {
    $stream = [IO.File]::Open($temporaryZip, [IO.FileMode]::Create)
    try {
        $archive = [IO.Compression.ZipArchive]::new($stream, [IO.Compression.ZipArchiveMode]::Create, $true)
        try {
            foreach ($entryName in ($files.Keys | Sort-Object)) {
                [IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
                    $archive, $files[$entryName], $entryName, [IO.Compression.CompressionLevel]::Optimal
                ) | Out-Null
            }
        }
        finally {
            $archive.Dispose()
        }
    }
    finally {
        $stream.Dispose()
    }
    $outputDirectory = Split-Path -Parent $OutputPath
    if (-not (Test-Path -LiteralPath $outputDirectory -PathType Container)) {
        New-Item -ItemType Directory -Path $outputDirectory | Out-Null
    }
    Move-Item -LiteralPath $temporaryZip -Destination $OutputPath -Force:$Force
}
finally {
    if (Test-Path -LiteralPath $temporaryZip) {
        Remove-Item -LiteralPath $temporaryZip -Force
    }
}

Write-Host "Packaged $($skillFolders.Count) skills and $($files.Count) files: $OutputPath"
Get-Item -LiteralPath $OutputPath

# Copilot Cowork Skills: Exercise Builders

This repository is a [Microsoft Copilot Cowork plugin](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development):
an M365 app package of [agent skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development#step-1-create-your-first-skill)
for creating Microsoft Copilot exercises, workshop scenarios, agent-building
labs, Microsoft Fabric data agent labs, and styled HTML handouts.

## Included skills

| Skill | Purpose |
|---|---|
| `copilot-cowork-exercise-builder` | Builds persona-based Copilot Cowork exercises and connected workshop tracks. |
| `copilot-exercise-html-formatter` | Renders exercise content as accessible, branded HTML handouts. |
| `copilot-exercise-builder` | Creates exercises for Copilot Chat, Researcher, Analyst, Notebook, and Microsoft 365 apps. |
| `copilot-studio-exercise-builder` | Creates hands-on Copilot Studio agent-building walkthroughs. |
| `fabric-data-agent-exercise-builder` | Creates hands-on Microsoft Fabric data agent labs with synthetic data, validated SQL, and a scheduled ingestion notebook. |

Each skill lives in its own subdirectory of [`skills/`](skills/), with a
`SKILL.md` file and, when present, `references/` and `scripts/` directories. [`manifest.json`](manifest.json)
is the M365 Unified App Manifest that declares them as `agentSkills`.

The Fabric data agent skill includes Python scripts and a sample scenario spec
in [`scripts/`](skills/fabric-data-agent-exercise-builder/scripts/). The scripts
use the Python standard library; optional Excel workbook output requires
`openpyxl`.

Published handouts are participant-focused, with authoring and facilitator notes
kept out of the deliverables. The formatter places required sources alongside
each exercise and specifies progressive desktop navigation with reading-position
preservation, a no-script fallback, and mobile overlay behavior. The Studio skill
also covers runtime selection, knowledge-source routing, and current topic
authoring patterns.

> [!IMPORTANT]
> [`outline.png`](outline.png) is currently a resized copy of the color icon,
> not a true single-color glyph. Replace it with a real 32×32 outline icon
> before packaging for real use.

## Package

From a clone or downloaded copy of this repository, run the bundled
[`Package-Plugin.ps1`](scripts/Package-Plugin.ps1) script:

```powershell
.\scripts\Package-Plugin.ps1
```

Requires Windows PowerShell 5.1 or PowerShell 7, with no additional modules,
Python, Node.js, or Azure tools needed for packaging. The script works from any
working directory when invoked by its path.

The output is `output\cowork-exercise-builders.zip`. Share that ZIP with users
for sideloading or with an administrator for tenant deployment. It contains
the manifest and icons at the archive root, plus only the skill folders
registered in the manifest, including their references and scripts. Repository
documentation, tests, and unregistered skill folders are not included.

To rebuild an existing package or choose another output location:

```powershell
.\scripts\Package-Plugin.ps1 -Force
.\scripts\Package-Plugin.ps1 -OutputPath output\my-plugin.zip -Force
```

Relative output paths are resolved from the repository root. Existing output is
not overwritten unless `-Force` is supplied. Missing manifest files, icons,
or registered skill entry points cause packaging to fail.

This script checks package inputs and creates the ZIP; it does not validate
the full Microsoft 365 manifest schema, certify icon artwork, install the plugin,
or provision any services. Address the outline-icon warning above before
distribution.

For a manual ZIP from the repository root (includes the entire `skills/`
directory rather than only registered folders):

```powershell
New-Item -ItemType Directory -Path output -Force | Out-Null
Compress-Archive -Path manifest.json, color.png, outline.png, skills -DestinationPath output\cowork-exercise-builders.zip
```

Alternatively, use the [Microsoft 365 Agents Toolkit CLI](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/microsoft-365-agents-toolkit-cli) (`atk`):

```shell
npm install -g @microsoft/m365agentstoolkit-cli
atk package --manifest-file ./manifest.json --output-package-file ./build/cowork-exercise-builders.zip --output-folder ./build
```

## Install (end users / personal testing)

Sideload the package into your own Microsoft 365 account with `atk`:

```shell
atk auth login
atk install --file-path "./output/cowork-exercise-builders.zip" --scope Personal
```

Then open **Cowork** in Microsoft 365 Copilot and start a session that
matches one of the skills' trigger phrases (for example, "build a Cowork
demo for a CFO at a manufacturing company"). The skill appears in the
session's side panel when it loads.

## Deploy (IT admins)

1. In the **Microsoft 365 admin center**, go to **Manage apps** > **Upload
   custom app**, select the ellipsis (**...**) > **Add agent**, and upload
   the `.zip` package.
2. In **Cowork** > **Sources & Skills** > **Plugins**, the plugin appears
   under **Discover** for users in your tenant. Pin or assign it as needed
   using your standard Copilot governance tools.

For public distribution through the Microsoft 365 App Store, submit the
package via [Partner Center](https://partner.microsoft.com). See
[Publish agents for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/publish).

## Use

Invoke a skill by describing the exercise or handout you want to create. Each
skill's `SKILL.md` contains its supported scenarios, required inputs, workflow,
and guardrails.

Product behavior and user-interface paths can change. Re-verify
version-sensitive guidance against the linked Microsoft Learn documentation
before delivering a workshop or publishing generated guidance.

## License

Licensed under the [MIT License](LICENSE).

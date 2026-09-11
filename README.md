# Copilot Cowork Skills: Exercise Builders

This repository is a [Microsoft Copilot Cowork plugin](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development):
an M365 app package of [agent skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development#step-1-create-your-first-skill)
for creating Microsoft Copilot exercises, workshop scenarios, agent-building
labs, and styled HTML handouts.

## Included skills

| Skill | Purpose |
|---|---|
| `copilot-cowork-exercise-builder` | Builds persona-based Copilot Cowork exercises and connected workshop tracks. |
| `copilot-exercise-html-formatter` | Renders exercise content as accessible, branded HTML handouts. |
| `copilot-se-demo-builder` | Creates exercises for Copilot Chat, Researcher, Analyst, Notebook, and Microsoft 365 apps. |
| `copilot-studio-agent-builder` | Creates hands-on Copilot Studio agent-building walkthroughs. |

Each skill lives in its own subdirectory of [`skills/`](skills/), with a
`SKILL.md` file and, when present, a `references/` directory. [`manifest.json`](manifest.json)
is the M365 Unified App Manifest that declares them as `agentSkills`.

> [!IMPORTANT]
> [`outline.png`](outline.png) is currently a resized copy of the color icon,
> not a true single-color glyph. Replace it with a real 32×32 outline icon
> before packaging for real use.

## Package

Zip the manifest, icons, and skills together at the root of the archive:

```powershell
Compress-Archive -Path manifest.json, color.png, outline.png, skills -DestinationPath cowork-exercise-builders.zip
```

```bash
zip -r cowork-exercise-builders.zip manifest.json color.png outline.png skills/
```

Or with the [Microsoft 365 Agents Toolkit CLI](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/microsoft-365-agents-toolkit-cli) (`atk`):

```shell
npm install -g @microsoft/m365agentstoolkit-cli
atk package --manifest-file ./manifest.json --output-package-file ./build/cowork-exercise-builders.zip --output-folder ./build
```

## Install (end users / personal testing)

Sideload the package into your own Microsoft 365 account with `atk`:

```shell
atk auth login
atk install --file-path "./cowork-exercise-builders.zip" --scope Personal
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

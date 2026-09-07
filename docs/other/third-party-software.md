# Third-party software

Community projects that talk to NIIMBOT printers. None of them are affiliated with NIIMBOT,
and listing here is not an endorsement or a review: the table records what each project says
it is, so you can pick one and judge it yourself.

!!! note

    Model support varies a lot between projects, and a project that names your model may still
    behave differently on your unit. The [hardware pages](../hardware/models.md) are the
    reference for what a given printer actually is.

Metadata below was read from each repository. "Licence: not declared" means the repository has
no licence file, which means the default is *all rights reserved* regardless of the code being
public.

## Applications

| Project                                                                                                                                                                          | Platform              | Language   | Licence    | What it is                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------- |
| [android_niimprint](https://github.com/terratempest/android_niimprint)<br>![Last Commit](https://img.shields.io/github/last-commit/terratempest/android_niimprint)               | Android               | Kotlin     | MIT        | Client for the D11, meant to be embedded in other Android apps.                                                           |
| [catlabel](https://github.com/lukaszliniewicz/catlabel)<br>![Last Commit](https://img.shields.io/github/last-commit/lukaszliniewicz/catlabel)                                    | Web (local)           | Python     | Apache-2.0 | Local design and printing studio with a visual canvas, batch printing from CSV. Also covers Phomemo and generic printers. |
| [NiimBlue](https://github.com/MultiMote/niimblue) ([niim.blue](https://niim.blue))<br>![Last Commit](https://img.shields.io/github/last-commit/MultiMote/niimblue)               | Browser               | TypeScript | MIT        | Design and print labels from a desktop or mobile browser.                                                                 |
| [niimbot-printer](https://github.com/ooguz/niimbot-printer)<br>![Last Commit](https://img.shields.io/github/last-commit/ooguz/niimbot-printer)                                   | Desktop               | Python     | GPL-3.0    | Prints labels on the B1, with Pretix integration.                                                                         |
| [printrow](https://github.com/slastra/printrow) ([printrow.lastra.us](https://printrow.lastra.us))<br>![Last Commit](https://img.shields.io/github/last-commit/slastra/printrow) | Browser               | Svelte     | MIT        | Label designer over Web Bluetooth. Binds `{{vars}}` to CSV columns for batch printing. Covers the B1 and the KNAON Y50P.  |
| [Thermalith](https://github.com/EvilGeniusLabs-ca/Thermalith)<br>![Last Commit](https://img.shields.io/github/last-commit/EvilGeniusLabs-ca/Thermalith)                          | Windows, macOS, Linux | C#         | GPL-3.0    | Desktop label designer over USB or Bluetooth, with the driver split into a reusable .NET library.                         |
| [ThermoTask](https://github.com/alefaraci/ThermoTask)<br>![Last Commit](https://img.shields.io/github/last-commit/alefaraci/ThermoTask)                                          | macOS                 | Swift      | Apache-2.0 | Prints Apple Calendar events and Reminders as thermal tickets.                                                            |
| [TiMini-Print](https://github.com/Dejniel/TiMini-Print)<br>![Last Commit](https://img.shields.io/github/last-commit/Dejniel/TiMini-Print)                                        | Desktop               | Python     | Apache-2.0 | Prints images, PDFs and text to Chinese Bluetooth "cat" thermal mini printers.                                            |
| [vooki-thermo-printer](https://github.com/vookimedlo/vooki-thermo-printer)<br>![Last Commit](https://img.shields.io/github/last-commit/vookimedlo/vooki-thermo-printer)          | macOS                 | Swift      | GPL-3.0    | Lightweight printing tool.                                                                                                |
| [NiimPrintX](https://github.com/labbots/NiimPrintX)<br>![Last Commit](https://img.shields.io/github/last-commit/labbots/NiimPrintX)                                              | Python                | Python     | GPL-3.0    | Bluetooth. Names D11, B21, B1, D110 and B18. Based on niimprint but doesn't mention any credits to the original project.  |

## Libraries and drivers

| Project                                                                                                                                                                        | Runs in | Language   | Licence      | What it covers                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ---------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [niimblue-node](https://github.com/MultiMote/niimblue-node)<br>![Last Commit](https://img.shields.io/github/last-commit/MultiMote/niimblue-node)                               | Node.js | TypeScript | not declared | niimbluelib CLI and a basic REST print server.                                                                                                                                               |
| [niimbluelib](https://github.com/MultiMote/niimbluelib) ([docs](https://libdocs.niim.blue))<br>![Last Commit](https://img.shields.io/github/last-commit/MultiMote/niimbluelib) | Browser | TypeScript | MIT          | The library behind NiimBlue. The most complete implementation of the protocol.                                                                                                               |
| [niimbot-web-bluetooth](https://github.com/iscarelli/niimbot-web-bluetooth)<br>![Last Commit](https://img.shields.io/github/last-commit/iscarelli/niimbot-web-bluetooth)       | Browser | JavaScript | MIT          | Single-file Web Bluetooth driver for embedding printing in an existing page, with no dependencies or build step. Carries per-model notes on flow control, printhead width and page handling. |
| [niimbotjs](https://github.com/dtgreene/niimbotjs)<br>![Last Commit](https://img.shields.io/github/last-commit/dtgreene/niimbotjs)                                             | Node.js | TypeScript | not declared | Printer client.                                                                                                                                                                              |
| [niimprint](https://github.com/AndBondStyle/niimprint) (fork of kjy00302/niimprint)<br>![Last Commit](https://img.shields.io/github/last-commit/AndBondStyle/niimprint)        | Python  | Python     | MIT          | Bluetooth or USB. Names D11, B21 and B1.                                                                                                                                                     |

## Integrations and utilities

| Project                                                                                                                                                                                                                                           | Language   | Licence      | What it is                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------ | ------------------------------------------------------------------------------------ |
| [hass-niimbot](https://github.com/eigger/hass-niimbot)<br>![Last Commit](https://img.shields.io/github/last-commit/eigger/hass-niimbot)                                                                                                           | Python     | MIT          | Home Assistant custom integration, installable through HACS.                         |
| [niimbot-web-ble-terminal](https://github.com/MultiMote/niimbot-web-ble-terminal) ([live](https://multimote.github.io/niimbot-web-ble-terminal/))<br>![Last Commit](https://img.shields.io/github/last-commit/MultiMote/niimbot-web-ble-terminal) | JavaScript | not declared | Sends raw commands to a printer from the browser. Useful when investigating a model. |
| [niimbotjs-tools](https://github.com/dtgreene/niimbotjs-tools) ([live](https://dtgreene.github.io/niimbotjs-tools/dist/))<br>![Last Commit](https://img.shields.io/github/last-commit/dtgreene/niimbotjs-tools)                                   | JavaScript | not declared | Browser tools built on niimbotjs.                                                    |

## Adding a project

Open a pull request adding a row. Keep the description to what the project does, in the same
neutral tone as the rest of the table, and please do not reorder the tables to move your own
entry: rows are alphabetical within each table.

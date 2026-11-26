# Permanent Wi-Fi patch — persistence qualification

## Product goal
Install once; corrected Wi-Fi code active automatically on every full boot; no PC, manual recovery script or daily user action after installation. Preserve stock PCI runtime PM (auto). Provide a reversible installation, uninstall, firmware compatibility gates and a reproducible patch from the user's own supported firmware artifacts; do not redistribute proprietary binaries. Native vendor integration is the preferred ultimate solution.

## Evidence and current state (2026-11-26)
V2 Java candidate, JAR/ODEX/VDEX and ART mappings qualified on Thor_V1.0.0.377_20260206_165408_user. V2.7 crossover 8/8 auto and 8/8 on; no demonstrated need for on. V2.8 30-minute session, runtime suspension and user-confirmed Internet; V3.0-alpha manual activation and watchdog disarm verified. V3.0 is volatile, not the permanent deliverable. One transient disconnect with automatic recovery recorded. Multi-hour stability, duplicate activation rejection, explicit disable launcher and full firmware recovery remain unqualified.

## Stage A — parallel stability and boot inventory
Keep the current live session intact for normal-use evidence. Read-only inventory of stock system/vendor init services, native AYN Settings and privileged service APKs, manifest receivers and supported startup facilities. No native automatic boot mechanism is assumed. Prefer a documented/supported native startup hook if one exists. Determine execution order relative to zygote/system_server and Wi-Fi service; do not automatically restart the framework on each boot without explicit qualification.

## Stage B — design and offline verification
If a supported early-boot hook exists, evaluate verified bind-mount activation before ART loads the Wi-Fi code. If only BOOT_COMPLETED is available, determine whether a safe delayed activation is feasible; app receivers alone do not grant privileged mounts, and late activation may require disruptive framework restart. Treat a privileged helper as fixed-function, narrowly scoped; no arbitrary command interface, no remote commands. Harden local executable and candidate storage (root-owned, not writable by shell/other apps), verify exact build and all stock/candidate hashes, atomic staging, duplicate protection, one attempt per boot, failure marker and opt-out accessible without relying on the corrected Android UI. No automatic reboot loop. Test watchdog failure path and independent recovery before enabling any auto-start.

## Stage C — installation and recovery gates
Qualify stock firmware recovery for exact build or equivalent verified recovery method, including backup and restoration plan. First qualify installer/uninstaller and manual boot activation, then supervised cold/warm boots. No partition writes, AVB changes, boot image changes or automatic persistence before recovery and safety gates are met. If no viable supported hook, evaluate vendor integration or a separately reviewed recovery-qualified firmware approach rather than claim persistent installation. Do not publish a stable release before validation.

## Acceptance
- Install once; candidate hashes and executable ART mapping verified on repeated cold and warm boots without user interaction.
- No framework restart loop, no unexpected reboot, no boot lockout, stock PM auto.
- Real Internet connectivity, fresh scans, network changes, sleep/wake and extended normal use.
- Unsupported firmware and OTA mismatch fail closed; no partial activation.
- Opt-out/uninstall and recovery independently verified; next boot returns to original artifacts with no reapplication.
- Document limitations, exact supported builds, install/uninstall and recovery. Publish source and patch/build tooling only; no private logs or proprietary binaries.

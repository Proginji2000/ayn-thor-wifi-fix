# Manual Edition — experimental guide (documentation preview)

**Availability: read-only preflight and local stock extraction only. The complete activation workflow is not yet available as a working installer.**

## Goal and scope

Prepare a local candidate and manually activate the correction from AYN Settings after a boot. No partition flash, slot change, PCI policy change or boot modification. A full reboot removes volatile mounts. Full firmware recovery media is not a prerequisite for this manual workflow. Save games before any future activation because the framework restart closes applications.

Only exact build Thor_V1.0.0.377_20260206_165408_user, kalama, API 33, slot a, has been tested on one device. Unknown builds, OTA changes, non-stock hashes or another active patch must stop. Native AYN root launcher availability must also be established.

## Available steps

1. Install Python 3 and official Android SDK Platform-Tools; clone or download this repository.
2. Enable USB debugging on the Thor, connect it and approve USB authorization.
3. At repository root run:

```bash
python tools/manual_preflight.py
```

Use `py -3` on Windows or `python3` on Linux/WSL if necessary. Specify `--adb /path/to/adb` if not in PATH (adb.exe for Windows/WSL). Connect exactly one USB device.

4. Extract the original components privately into a new local directory:

```bash
python tools/manual_preflight.py --extract-stock thor-stock-private
```

Do not redistribute proprietary stock files. This script is read-only on the device, never launches root commands, and does not reboot or activate anything. The new utility has not yet been qualified on a second console. READ_ONLY_PREFLIGHT_PASS is not deployment authorization.

## Steps not yet available

5. Rebuild the corrected JAR from stock using the standalone builder and compile matching ART artifacts locally. The existing build still depends on a private historical archive and a reference binary; the independent builder is not shipped yet.
6. Verify a locally built candidate with `python tools/manual_preflight.py --bundle path-to-candidate`. This verifies hashes, not functionality or installation permission.
7. The future portable installer will transfer the candidate and manual launcher. It must verify stock, stage a protected worker, arm the watchdog, verify ART mappings and scanner after settling, and retain the patch until reboot only after successful checks. This combined manual workflow must be physically qualified before releasing its activation script as usable.
8. After a volatile activation a full reboot restores stock. V3.5-r3 and V3.6 demonstrate normal and watchdog rollback, not boot partition recovery.

Do not use session-specific historical scripts as a public installer, flash shared images, switch slots or change AVB.

## Evidence

Historical V3.0 manual activation until reboot demonstrated. V3.5-r3 new candidate strict scans 8/8, scanner responsive 8/8, IP probes 2/2, ART mappings and stock rollback PASS. V3.6 independent watchdog rollback after worker termination PASS. Combined Manual Edition, portable standalone build, hardening and extended use remain pending.

See [compatibility matrix](../compatibility/firmware-matrix.json), [test results](TEST_RESULTS.md), [recovery gate](RECOVERY_GATE.md).

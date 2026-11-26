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

5. Rebuild the corrected JAR from stock using the standalone builder and compile matching ART artifacts locally. The standalone build passed privately without a historical archive or reference binary; the builder and portable ART generation are not yet shipped.
6. Verify a locally built candidate with `python tools/manual_preflight.py --bundle path-to-candidate`. This verifies hashes, not functionality or installation permission.
7. The future portable installer will transfer the candidate and manual launcher. It must verify stock, stage a protected worker, arm the watchdog, verify ART mappings and scanner after settling, and retain the patch until reboot only after successful checks. The combined private pilot passed physical qualification on one device; public security review and ART generation integration remain pending.
8. After a volatile activation a full reboot restores stock. V3.5-r3 and V3.6 demonstrate normal and watchdog rollback, not boot partition recovery.

Do not use session-specific historical scripts as a public installer, flash shared images, switch slots or change AVB.

## Evidence

Historical V3.0 manual activation until reboot demonstrated. V3.5-r3 new candidate strict scans 8/8, scanner responsive 8/8, IP probes 2/2, ART mappings and stock rollback PASS. V3.6 independent watchdog rollback after worker termination PASS. Combined private pilot installation, activation, duplicate rejection and reboot reuse PASS; portability, hardening, uninstall and extended use remain pending.

See [compatibility matrix](../compatibility/firmware-matrix.json), [test results](TEST_RESULTS.md), [recovery gate](RECOVERY_GATE.md).

### Builder progress
The private standalone builder has been assembled from both verified historical sources. It no longer requires the historical archive or V2 reference JAR. Syntax, DEX integrity and packaging tests passed; full build with the reference tool versions passed privately. Portable activation is still pending.


### Standalone reconstruction validated
One complete WSL build reproduced the exact qualified JAR and DEX without historical archive or reference JAR. A private reusable manual-launcher pilot passed device qualification; local file installation only, no automatic boot activation. Public builder, portable ART generation and complete installer remain pending review and testing. No repeat eight-scan trial required for identical artifacts.


## Daily use after private pilot installation
After a full reboot, run the same Enable launcher from AYN Settings once. Save games first; Android framework restarts. Wait for the readiness check (about 70 s observed). The fix remains active until the next full reboot, with no PC needed for activation. To return to stock, reboot and do not run Enable; this disables the fix but retains local files. Complete uninstall is not qualified. Do not activate after an unsupported OTA.

Both manual activations passed ART mapping, fresh scan (9.13 s and 9.14 s) and IP checks; duplicate activation was rejected without framework changes. A full reboot retained installation files and restored the stock tuple; the same launcher reactivated without file transfer. This workflow is not yet available as a standalone public download. Full firmware is not required for Manual Edition.


## RC2 — release engineering
Private kit combines standalone builder, portable ART compiler, hardened pilot and reversible uninstall. 30 local checks PASS; no new Android execution. Public [manual_verify_bundle.py](../tools/manual_verify_bundle.py) checks the exact tuple offline: `python3 tools/manual_verify_bundle.py path-to-bundle`. It does not build, transfer or activate anything. Complete kit stays private pending ART output repeatability, bootstrap, uninstall and security review. Full firmware not required for Manual Edition.

RC2 physical trial: native compilation and ART metadata PASS, exact VDEX, differing ODEX. Strict bundle gate refused the output; active system unchanged. Offline binary comparison required before distribution; no recompilation required for this analysis.

Final OAT comparison: observed pair equivalent outside checksum, metadata size and permitted path metadata; every other byte identical. Exact-hash activation gate unchanged. Private standalone equivalence verifier pending real-pair validation; no alternate bundle activation. Next: RC2 reversible uninstall and hardened bootstrap at a planned stock reboot.

Standalone verifier passed both real ODEX files. Exact activation gate unchanged. Test reversible uninstall and hardened bootstrap using the original exact qualified tuple; uninstall retains its lock until reboot.

# Development handoff — 2026-11-26

## Current gate
V3.3-r3 local full-build repeatability PASS. Two independent clean work directories produced byte-identical JARs; 3138 disassembled classes match historical V2. Historical binary equality is false. Offline-only candidate; deployment_allowed=false. See TEST_RESULTS.md and the firmware compatibility manifest for exact hashes and toolchain versions.

## Runtime and recovery
Historical V2 JAR/ODEX/VDEX was tested on .377 with manual volatile V3.0 activation; ART mappings and scanner response verified. V2.7 comparison 8/8 auto and 8/8 on; keep PCI runtime PM auto. Stock defect recurred after controlled Fastboot return; scanner timeout and repeated busy parser stack recorded. User subsequently reported V3.0 reactivated and Wi-Fi available; current state needs read-only confirmation if further device work is requested. Backups of both init_boot slots and native Fastboot transport verified, but actual partition restoration and full recovery are not qualified. Bootloader remains unchanged by this project; no partition flash performed. Manual activation is not permanent persistence.

## Next action (V3.4)
Qualify native ART compilation of the new serial candidate in isolated output storage; no replacement of active components, no reboot, no partition write. Verify input SHA256, firmware, active tuple (known stock or known historical V2 only), class-loader context and boot/PID/hash/PM before and after. Record compiler status, generated ODEX/VDEX digests, header checks, scanner health and retained logs. Stop on mismatch, missing prerequisites or failed check; distinguish compilation success from scanner health. Do not reuse historical ODEX/VDEX for the new JAR. Proposed procedure has not yet been executed. Do not repeat completed offline builds unless the inputs or toolchain change.

## Remaining engineering
- Remove dependence on historical private scripts and reference binary for ordinary supported builds; pin dependencies and validate on a second clean environment. Keep reference comparison as regression evidence.
- Develop narrowly scoped and integrity-checked installer, uninstall and supported persistence approach; qualify independent recovery before boot modifications. No automatic flash, slot switch, security-policy changes or automatic activation on unknown firmware.
- Qualify new ART bundle dynamically, fresh scans, Internet, reconnection, sleep/wake and repeated boots under explicit authorization; keep rollback evidence.
- Maintain FR/EN documentation, machine-readable compatibility and preflight contract, CI offline tests, OTA fail-closed behavior, checksummed releases.
- Coordinate private vendor report and community release. No proprietary binaries, raw private logs, device IDs or triggering-input details in public repository.

Read AGENTS.md, TEST_RESULTS.md, PERSISTENCE_PLAN.md and compatibility/firmware-matrix.json before further work. Historical experiments are evidence, not install instructions. No stable release authorized.

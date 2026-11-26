# Development handoff — 2026-11-26

## Current gate
V3.3-r3 local full-build repeatability PASS. Two independent clean work directories produced byte-identical JARs; 3138 disassembled classes match historical V2. Historical binary equality is false. V3.4-r2 native ART qualification PASS on the same .377 device; new bundle has distinct matching JAR/ODEX/VDEX hashes. V3.5-r3 functional runtime qualification PASS on exact .377 firmware with 45 s startup stabilization: fresh scan cycles 8/8, scanner responsive 8/8, interface-bound IP probes 2/2, framework stability and executable ODEX/VDEX mapping checks PASS, normal cleanup reboot and exact stock tuple rollback PASS. Historical r2 7/8 remains recorded. HTTPS not automated; watchdog expiry rollback, new-bundle extended use, partition restoration, installer and boot persistence not qualified. Deployment remains denied. See TEST_RESULTS.md and the firmware compatibility manifest for exact hashes and toolchain versions.

## Runtime and recovery
Historical V2 JAR/ODEX/VDEX was tested on .377 with manual volatile V3.0 activation; ART mappings and scanner response verified. V2.7 comparison 8/8 auto and 8/8 on; keep PCI runtime PM auto. Stock defect recurred after controlled Fastboot return; scanner timeout and repeated busy parser stack recorded. V3.4-r2 confirmed historical V2 active, scanner responsive before/after isolated compilation, PCI auto, boot/PID/active tuple unchanged. Recheck current state before further device work. Backups of both init_boot slots and native Fastboot transport verified, but actual partition restoration and full recovery are not qualified. Bootloader remains unchanged by this project; no partition flash performed. Manual activation is not permanent persistence.

## Next action (V3.6 / V3.7)
Last measured device state: exact stock after r3 rollback. Preserve r2 and r3 proof; no further eight-cycle scans or ART rebuild without changed inputs or evidence. Qualify watchdog expiry independently with a bounded, explicitly approved volatile fault-path trial, requiring stock precheck and exact stock rollback after reboot. Develop offline installer and recovery plan in parallel; first identify verified exact-build recovery path, no partition writes, slot switch, AVB or persistent boot activation before recovery gates and explicit approval. No proprietary artifacts or raw logs in Git.

## Remaining engineering
- Remove dependence on historical private scripts and reference binary for ordinary supported builds; pin dependencies and validate on a second clean environment. Keep reference comparison as regression evidence.
- Develop narrowly scoped and integrity-checked installer, uninstall and supported persistence approach; qualify independent recovery before boot modifications. No automatic flash, slot switch, security-policy changes or automatic activation on unknown firmware.
- New ART bundle strict dynamic scan gate PASS. Remaining HTTPS, reconnection, sleep/wake, extended use and repeated boots under explicit authorization; keep rollback evidence.
- Maintain FR/EN documentation, machine-readable compatibility and preflight contract, CI offline tests, OTA fail-closed behavior, checksummed releases.
- Coordinate private vendor report and community release. No proprietary binaries, raw private logs, device IDs or triggering-input details in public repository.

Read AGENTS.md, TEST_RESULTS.md, PERSISTENCE_PLAN.md and compatibility/firmware-matrix.json before further work. Historical experiments are evidence, not install instructions. No stable release authorized.

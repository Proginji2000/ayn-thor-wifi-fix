# Development handoff — 2026-11-26

## Current gate
V3.3-r3 local full-build repeatability PASS. Two independent clean work directories produced byte-identical JARs; 3138 disassembled classes match historical V2. Historical binary equality is false. V3.4-r2 native ART qualification PASS on the same .377 device; new bundle has distinct matching JAR/ODEX/VDEX hashes. Runtime qualification pending; deployment_allowed=false. See TEST_RESULTS.md and the firmware compatibility manifest for exact hashes and toolchain versions.

## Runtime and recovery
Historical V2 JAR/ODEX/VDEX was tested on .377 with manual volatile V3.0 activation; ART mappings and scanner response verified. V2.7 comparison 8/8 auto and 8/8 on; keep PCI runtime PM auto. Stock defect recurred after controlled Fastboot return; scanner timeout and repeated busy parser stack recorded. V3.4-r2 confirmed historical V2 active, scanner responsive before/after isolated compilation, PCI auto, boot/PID/active tuple unchanged. Recheck current state before further device work. Backups of both init_boot slots and native Fastboot transport verified, but actual partition restoration and full recovery are not qualified. Bootloader remains unchanged by this project; no partition flash performed. Manual activation is not permanent persistence.

## Next action (V3.5)
Prepare a controlled volatile runtime qualification of the new ART bundle, without partition writes or persistence. Review the previously qualified temporary activation and rollback harness, require verified exact stock/historical/new tuples and explicit approval before any live replacement or disruptive restart. Establish recovery readiness and bounded rollback; verify actual executable ODEX/VDEX mappings, stable framework, fresh scan publication, scanner responsiveness, PCI auto and connectivity. Distinguish new runtime evidence from historical V2 measurements. No repeat of V3.4 needed unless inputs or evidence change. ART compilation repeatability across independent runs is not yet established. Keep all proprietary files and raw logs private.

## Remaining engineering
- Remove dependence on historical private scripts and reference binary for ordinary supported builds; pin dependencies and validate on a second clean environment. Keep reference comparison as regression evidence.
- Develop narrowly scoped and integrity-checked installer, uninstall and supported persistence approach; qualify independent recovery before boot modifications. No automatic flash, slot switch, security-policy changes or automatic activation on unknown firmware.
- Qualify new ART bundle dynamically, fresh scans, Internet, reconnection, sleep/wake and repeated boots under explicit authorization; keep rollback evidence.
- Maintain FR/EN documentation, machine-readable compatibility and preflight contract, CI offline tests, OTA fail-closed behavior, checksummed releases.
- Coordinate private vendor report and community release. No proprietary binaries, raw private logs, device IDs or triggering-input details in public repository.

Read AGENTS.md, TEST_RESULTS.md, PERSISTENCE_PLAN.md and compatibility/firmware-matrix.json before further work. Historical experiments are evidence, not install instructions. No stable release authorized.

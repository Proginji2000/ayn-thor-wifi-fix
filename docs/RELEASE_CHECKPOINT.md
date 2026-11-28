# Consolidated release gates — 2026-11-28

**Owner reference evidence: PASS for exact binary reconstruction, historical runtime correction, and RC4 storage lifecycle. Public installation: NO-GO.**

This is a current-state checkpoint, not an installation guide. The detailed history remains in COMMUNITY_RELEASE.md and HANDOFF.md. The firmware matrix is authoritative for machine-readable qualification scope.

| Lot | Verified | Remaining exit gate |
|---|---|---|
| A — Reproducible build | Exact owner JAR/DEX/ODEX/VDEX, isolated replay and identical V4.3 ZIP | Independent clean host, dependency provenance, independent compatible device |
| B — Manual, authorized root | Linux 16/16 synthetic scenarios and real payload lifecycle; Android inert 8/8; owner stock storage cycle 9/9 ordered markers; original RC1 restored | Clean host-to-device input staging, independently verified final installation/activation and rollback on a compatible independent device; interruption handling and explicit recovery plan |
| C — Manual, native without Magisk | Historical RC1 private activation; native launcher line-oriented dispatch and discarded response established | Supported vendor execution contract and independent install/uninstall qualification; RC3 remains blocked |
| D — Permanent | Exact V4.3 owner lifecycle, automatic health commitment, strict installed preflight, exact rebuilt ZIP | Stock preflight, ownership-aware rollback review, recovery readiness, independent compatible device; no mixed-module support |
| E — Release | Eight documentation drafts, initial static review | Independent security review, licensing and dependency inventory, private vendor coordination, translation review and explicit release approval |

## Stop repeating reference-device tests

Do not repeat the same build, ART compilation, scans, reboot, or storage lifecycle solely to accumulate PASS results. A changed binary, new input path, previously untested failure mode or independent environment justifies new testing.

## Current owner state

The last reported RC4 storage cycle completed successfully with the permanent module disabled and stock Wi-Fi. Original Manual files were restored. The storage workspace and activation exclusion lock were deliberately retained. Normal reactivation of the previously qualified V4.3 module and reboot are appropriate after successful completion; confirm installed-mode preflight after the health commit. This final reactivation has not yet been observed for the latest session.

## Bounded remaining work

1. Owner restores normal V4.3 use and records the existing read-only preflight once. No Manual launcher while V4.3 is active.
2. Develop clean-input staging offline, with strict hashes, no overwrite, explicit transaction states and independent final-state verification. Do not treat the owner storage-cycle controller as a clean installer. Do not implement a new privilege mechanism.
3. Review Permanent recovery and rollback and all source/dependency licenses. Obtain supported vendor recovery and native-execution documentation. No forced power loss or new flash merely for evidence.
4. Recruit one consenting independent compatible tester, with verified recovery and exact prerequisites; group only genuinely untested paths into a bounded session. Owner reference results do not authorize that session.
5. Make separate release decisions for each edition. Do not conflate an authorized-root Manual workflow with the no-Magisk objective.

No APK, proprietary binaries, raw logs, private scripts or detailed vendor implementation have been added by this checkpoint. No device action was performed by this documentation update.

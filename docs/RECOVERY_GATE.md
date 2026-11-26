# V3.7 — Independent firmware recovery gate

Status: BLOCKED for boot modification. Last verified device state: stock .377, slot a, PCI auto. Normal and watchdog-expiry volatile rollback PASS. Both init_boot backups (8 MiB each) and bootloader Fastboot transport previously verified. Actual partition restoration and full recovery remain untested.

## Recovery source leads checked 2026-11-26
- Official AYN firmware page https://www.ayntec.com/pages/software does not list Thor full recovery media in the retrieved page.
- Official support: https://www.ayntec.com/pages/contact-us (info@ayn.hk). Request exact Thor_V1.0.0.377_20260206_165408_user full package, official Windows recovery procedure/tool and prerequisites, model/storage compatibility, checksum or authenticated download, whether recovery works without Android, and data-loss implications.
- Community report https://www.reddit.com/r/AynThor/comments/1xe8pji/ayn_thor_hardreboots_whenever_an_app_turns_on_the/ describes a seller-provided Thor_20260206 full package and QFIL/EDL recovery. This is a lead only, not verified media or proof for this device.
- Community-linked Google Drive package in https://www.reddit.com/r/AynThor/comments/1vghph7/could_anyone_point_me_to_the_original_thor/ resolves to Thor_20260112.7z, an earlier date. Not approved for .377 recovery. Do not flash or treat as exact-build recovery.

## Gates
1. Obtain and authenticate compatible full recovery media and official instructions; inspect offline and record package hash, manifest, platform and partition scope. Preserve both local init_boot backups and personal data separately.
2. Verify Windows recovery tooling and independent access path without partition writes. Prior Fastboot entry/exit evidence need not be repeated unless environment changes; EDL not yet qualified.
3. Review a narrowly scoped restoration strategy for any proposed boot modification, including loss-of-Android failure, original images, and full recovery fallback. No destructive recovery test just to generate evidence; require separate explicit approval, backup and assessed risk for any write.
4. Continue offline installer/uninstaller and persistence design in parallel. Prefer official fix or supported native hook; Magisk remains a candidate, not selected or installed. No automatic flash, slot switch, AVB change, or boot persistence until recovery and authorization gates met.

No vendor contact or package download has been performed by this update. No binaries or raw logs published.

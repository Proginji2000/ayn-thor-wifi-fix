# Permanent Edition — V4.0 preparation (2026-11-27)

Status: design selected, boot writes denied. Magisk is the preferred candidate framework, not installed or qualified on Thor. RC1 remains the owner fallback. No need to repeat scanner trials, native ART compilation, boot inventory or backup parsing for unchanged evidence.

## Evidence baseline
- Exact .377 kalama API 33, slot a last measured; unlocked bootloader; verified Fastboot transport and return to Android.
- Both 8 MiB init_boot backups independently hashed and parsed in V3.2, Android boot v4, kernel size zero, LZ4 legacy ramdisk, AVB metadata present (chain authentication not established). Slot a and b differ. Never interchange.
- Vendor pservice observed starting after Zygote by approximately 433 ms; no confirmed supported user auto-start hook. Existing native launcher is not a suitable demonstrated early-boot facility.
- Exact candidate bundle already qualified under volatile manual activation. All existing activation integrity gates remain in effect.

## Decision: staged Magisk feasibility
Official references: https://topjohnwu.github.io/Magisk/install ; https://topjohnwu.github.io/Magisk/guides.html ; https://topjohnwu.github.io/Magisk/details.html ; https://topjohnwu.github.io/Magisk/faq.html .
The official app can prepare a local image on its intended device without flashing. Magisk changes the boot environment and its own security policy; it is not just a Wi-Fi patch. No manual AVB disabling, policy weakening or slot switch is planned. Full stock firmware is useful fallback, not mandatory input for image preparation.

### Gate P0 — prepare only
Verify current firmware and slot with read-only properties; exact local slot-a backup hash fd3ad6ea2cf36aecec54d3ce1abc5239d06d21557e64db50224010ebda220afe, size 8388608. Keep original on PC and copy only to device shared storage under a new filename. Use official Magisk app from https://github.com/topjohnwu/Magisk/releases and its file/image patch option on this device. Do not use Direct Install, install to inactive slot, flash, reboot or accept an environment setup that changes partitions. Retrieve patched file privately and inspect header, ramdisk, version, output size and expected changes. No flash approval implied. If app does not offer image-only preparation, stop. Keep existing Manual Edition active.
### Gate P1 — independent recovery review
Reconfirm scope of proposed write, active slot, exact original image, independent hardware entry to Fastboot, compatible driver, restoration procedure and fallback. Existing transport and backup evidence are not a physical restore test. A full recovery package remains optional if a separately reviewed independent targeted recovery route is sufficient. No write without explicit approval and recovery gate. Do not perform a destructive test solely for evidence.
### Gate P2 — framework-only trial
Only after P1 approval: separate root framework qualification from Wi-Fi activation. No module at first boot. Verify ordinary Android boot and independent disable/restore mechanism. Review Magisk's own SELinux changes, device security implications and OTA behavior before any write.
### Gate P3 — observation-only module
Design a nonblocking observer of init/APEX/ART/Zygote and boot completion, with no mounts, policy changes, framework restart or network actions. Establish actual ordering rather than infer that post-fs-data runs before the needed APEX paths are available. Official Magisk post-fs-data is blocking; avoid long checks there. Service scripts are later/nonblocking.
### Gate P4 — candidate module
Select earliest demonstrated safe point. Exact build and original/qualified artifact hashes, root-owned files, no activation on mismatch, one attempt per boot, no automated restart loop, module disable and recovery independently available. Do not reuse the RC1 live-restart worker verbatim at early boot. If early placement cannot be demonstrated safely, design a separate late activation mode with explicitly assessed disruption. Test offline and then supervised device trials.
### Gate P5 — release
Repeated cold/warm boot, mappings, Wi-Fi readiness, sleep/wake, HTTPS, extended use, unsupported OTA refusal, module disable/uninstall and independent recovery. Public source and scripts only, no proprietary images or trigger details. Coordinate disclosure. Manual Edition RC2 remains a separate unqualified release-engineering task.

No new physical tests performed in this update. No flash command, root module or boot-writing tool delivered. Current device state after owner reported RC1 re-enable has not been independently remeasured.

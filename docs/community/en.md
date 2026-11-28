# AYN Thor Wi-Fi Fix — Community guide

[English](en.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [한국어](ko.md) · [Русский](ru.md)

**Preview — not a public installer.** Manual Edition RC1 and Permanent Edition V4.3 RC1 have been tested privately on one console. Public distribution is not approved.

## Compatibility
Only `Thor_V1.0.0.377_20260206_165408_user`, kalama, Android 13 (API 33), slot a, has been tested. Other firmware, slots, hardware variants and OTA updates are unqualified. Stop if the build or integrity checks differ.

## Choose an edition
- Manual Edition: private reusable launcher; enable after each full boot. Activation restarts Android's framework and closes applications. A full reboot restores stock Wi-Fi components. Complete uninstall and hardened RC2 installation remain unqualified.
- Permanent Edition: private V4.3 RC1 module for Magisk 31.1 on the tested device. Activates before Zygote and checks boot health twice. Three corrected boots, six health checks, normal recurrence, simulated unconfirmed-boot guard, disable, uninstall and reinstall passed. Never use both editions simultaneously.

## Available now
On a stock, fully booted device, install Python 3 and official [Android Platform-Tools](https://developer.android.com/tools/releases/platform-tools). Enable USB debugging, connect one USB device and approve the connection. From the repository root, run:
```bash
python3 tools/manual_preflight.py
python3 tools/manual_preflight.py --extract-stock thor-stock-private
```

On Windows use `py -3` instead of `python3` if needed. Use `--adb /path/to/adb` for a non-default ADB executable (on WSL with Windows ADB use adb.exe). The second command creates a new private local directory. The tool reads the device only; it does not root, flash, install or reboot. Do not run stock checks against an active patch. Keep the extracted files private.

If you already possess a locally built candidate, the offline verifier is available:
```bash
python3 tools/manual_verify_bundle.py path-to-candidate
```

A PASS proves exact file hashes only. It is not installation approval. The public builder and complete installation workflow are not available yet.

## Safety and recovery
Back up your data before any future installation. The permanent edition requires an existing independently qualified root/recovery setup; do not use a shared patched boot image, unlock or flash based on this preview. Do not change slots or AVB. Stop on an unknown firmware, unexpected hash, unconfirmed boot or any error. Do not manually clear `pending`. On the tested private installation, disable or remove the module in Magisk, then reboot normally; this returns Wi-Fi components to stock, not the boot partition or root state. Manual users reboot without running Enable. Real boot failure recovery, power-loss durability, physical init_boot restoration and long-term stability are unqualified. No other console has been qualified.

## Support
Report edition, firmware, error stage and redacted diagnostic markers only. Remove serial numbers, boot IDs, SSIDs, BSSIDs, addresses and personal data. Do not upload firmware, JAR/ODEX/VDEX files or boot images. Use the repository issue tracker once support is available. This is an independent project, not an official AYN release.

[Compatibility matrix](../../compatibility/firmware-matrix.json) · [Release gates](../COMMUNITY_RELEASE.md)

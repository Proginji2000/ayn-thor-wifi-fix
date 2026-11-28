# AYN Thor Wi-Fi Fix

[English](docs/community/en.md) · [Français](docs/community/fr.md) · [Español](docs/community/es.md) · [Deutsch](docs/community/de.md) · [简体中文](docs/community/zh-CN.md) · [日本語](docs/community/ja.md) · [한국어](docs/community/ko.md) · [Русский](docs/community/ru.md)

**Private device qualification PASS — public installer not yet available.**

An independent project for a reproducible, reversible Wi-Fi correction. Only one AYN Thor, `Thor_V1.0.0.377_20260206_165408_user` (kalama, Android 13 / API 33, slot a), has been qualified.

| Edition | Private evidence | Community availability |
|---|---|---|
| Manual RC1 | Reusable activation after boot; runtime and reboot rollback passed | Read-only preflight and offline verifier only |
| Permanent V4.3 RC1 | Magisk 31.1; 3 corrected boots, 6 health checks, recurrence, guard-state simulation, disable, uninstall and reinstall passed | Private module; no public installer |

Start with the [community guide](docs/community/en.md). The eight-language guides are documentation previews, not installation authorization.

## Available tools
- [Read-only compatibility and stock extraction](tools/manual_preflight.py)
- [Offline exact-bundle verification](tools/manual_verify_bundle.py)

## Technical documentation
- [Community release gates](docs/COMMUNITY_RELEASE.md)
- [Current development handoff](docs/HANDOFF.md)
- [Field evidence](docs/TEST_RESULTS.md)
- [Firmware matrix](compatibility/firmware-matrix.json)
- [Manual Edition history](docs/MANUAL_EDITION.md)
- [Permanent Edition history](docs/PERMANENT_EDITION.md)
- [Recovery gate](docs/RECOVERY_GATE.md)
- [Upstream report draft](docs/UPSTREAM_REPORT.md)

## Safety
Do not combine editions. Unknown firmware or OTA changes must fail closed. The private Magisk trial involved a narrowly authorized boot-partition write on the owner's device; V4.3 itself does not write boot partitions. Normal Wi-Fi stock rollback does not restore root or boot partitions. Actual failed-boot recovery, physical init_boot restoration, power-loss durability, prolonged stability and other devices remain unqualified. Do not flash shared images or redistribute proprietary artifacts. No public release approved.

Reference: [JoelMomo/AYN-Thor-WiFi-Recovery](https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery). No upstream affiliation implied.

# AYN Thor Wi-Fi Fix

[Français](README.fr.md)

**Experimental — runtime recovery tested; permanent installation not yet qualified.**

On a single AYN Thor running Android 13 firmware `Thor_V1.0.0.377_20260206_165408_user`, repeated stock diagnostics identified an unresponsive Android Wi-Fi scanner during scan-result parsing. The historical Java correction V2 has been tested on the device with its matching ART artifacts and stock PCI runtime power management (auto). V3.0 provides manual volatile activation; a full reboot returns to stock. Keeping the PCI device active alone is not a demonstrated permanent solution.

V3.3-r3 produces identical JARs in two complete local builds, with all 3138 disassembled classes matching the historical candidate. Its binary differs from V2; native ART and strict volatile scan qualification passed (V3.5-r3, 8/8). Autonomous rollback after forced worker termination passed (V3.6). Permanent installation and stable distribution remain unapproved.

## Manual Edition — community preparation
- [Experimental tutorial and availability](docs/MANUAL_EDITION.md)
- [Read-only preflight and stock extraction script](tools/manual_preflight.py)

Standalone candidate generation passed privately on the original WSL environment; the builder and reusable manual launcher are not yet published. The portable complete workflow remains pending.

## Documentation
- [Current development handoff](docs/HANDOFF.md)
- [Field evidence and limitations](docs/TEST_RESULTS.md)
- [Firmware compatibility matrix](compatibility/firmware-matrix.json)
- [Persistence and lifecycle plan](docs/PERSISTENCE_PLAN.md)
- [Draft upstream report (not submitted)](docs/UPSTREAM_REPORT.md)
- [Agent instructions](AGENTS.md)

## Safety and scope
Only the exact tested firmware is in scope. Unknown firmware or OTA changes must fail closed. No permanent installation, partition restoration or automatic boot activation is qualified. No partition flash has been performed. The project aims for a maintainable and reversible fix, preferably integrated by the vendor; do not redistribute proprietary firmware. No stable release is available. Historical recovery experiments are not installation instructions.

Reference: [JoelMomo/AYN-Thor-WiFi-Recovery](https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery), which motivated the diagnostic work. No upstream affiliation implied.

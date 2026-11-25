# AYN Thor Wi-Fi runtime PM workaround

[Français](README.fr.md)

**Experimental — one successful recovery, not a proven permanent fix.**

On an AYN Thor running Android 13 firmware `Thor_V1.0.0.377_20260206_165408_user`, the Qualcomm kernel driver completed scans while Android's scanner remained stuck. Keeping the Wi-Fi PCI device runtime-active and subsequently restarting the Android framework restored 17 scan results, association and Internet access.

The runtime PM change alone did not recover an already stuck scanner. Automatic startup, long-term prevention and battery impact are not qualified.

## Documentation
- [Field evidence and limitations](docs/TEST_RESULTS.md)
- [Persistence qualification plan](docs/PERSISTENCE_PLAN.md)
- [Draft upstream report](docs/UPSTREAM_REPORT.md)

## Safety
Only the exact tested firmware and PCI identity (17cb:1107 at 0000:01:00.0) are in scope. This uses the manufacturer's stock root script facility. No flash, partition modification or SELinux change is proposed. Runtime PM changes may increase power use. Framework restart closes apps: save games first. Restore the original power policy (auto) if adverse effects occur.

Reference: [JoelMomo/AYN-Thor-WiFi-Recovery](https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery), which motivated the diagnostic work. No upstream affiliation implied.

# Persistence qualification

Goal: reapply the temporary PCI runtime-PM workaround after boot, without flashing, changing SELinux, modifying vendor partitions, or restarting Android automatically.

## Stage A — present session
Keep current on setting; validate normal usage, suspend/resume cycles, Wi-Fi reconnect and battery impact. Record duration, failures, charging state and conditions. Roll back on excessive heat, battery drain or instability. A single recovery is not prevention proof.

## Stage B — native boot mechanism inventory
Read-only inventory of stock AYN Settings / startup-script capability and package metadata. Prefer a supported native boot hook if it exists. No such hook is assumed or verified yet.

## Stage C — fallback implementation
If no suitable native hook exists, evaluate a minimal local Android app using AYN's native privileged interface (reference: JoelMomo/AYN-Thor-WiFi-Recovery, MIT). User opt-in, explicit firmware and PCI identity allowlist, fixed command only, bounded wait for PCI device, readback validation, no internet permission, no arbitrary command interface. Evaluate BOOT_COMPLETED and Android background constraints; do not claim early-boot execution. Never restart Zygote automatically. Offer separate explicit recovery after saving games. Disable automatic application and restore auto on opt-out. Stop on unsupported firmware or failed verification.

## Acceptance
- Normal cold boot and warm reboot, mode on verified after each.
- Repeat sleep/resume and Wi-Fi reconnect tests; verify setting has not reverted.
- Confirm real connection and fresh scan results.
- Compare battery usage and temperature against equivalent baseline.
- Verify disabled/uninstalled state does not reapply on; restore auto and verify.
- Record failures and unknowns; no stable release until evidence supports it.

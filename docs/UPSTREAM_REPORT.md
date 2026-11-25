# Draft upstream report — not submitted

Subject: AYN Thor .377: scan lockup recovered by keeping Qualcomm PCI runtime PM active before framework restart

Thanks for your recovery work. On one Thor running Android 13 and Thor_V1.0.0.377_20260206_165408_user, v0.3.0 reported probable lockup and recovery did not restore scans (scanner still stuck after 93.5 s). Kernel kiwi_v2 scans nevertheless found 14–19 BSS with COMPLETED status; Android returned zero.

PCI device 0000:01:00.0 (17cb:1107, cnss_pci) was runtime-suspended with power/control=auto. Using the stock root script launcher, setting its power/control to on woke the device, but Android remained stuck. A subsequent explicit zygote restart restored 17 Android scan results, IdleState, carrier=1 and Internet access. The previous framework-only attempt failed.

Potential optional experiment: validate the exact firmware and PCI identity, set power/control=on, verify readback, then offer an explicit framework restart if needed. Provide rollback to auto, disclose potential battery impact and avoid automatic restart. No permanent fix claimed; only one combined successful field trial. Prevention, battery and boot persistence remain untested. EHT/MLO warnings were also observed; their role is unknown.

Evidence and qualification plan: https://github.com/Proginji2000/ayn-thor-wifi-fix

Reference: https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery (v0.3.0). No raw private logs included.

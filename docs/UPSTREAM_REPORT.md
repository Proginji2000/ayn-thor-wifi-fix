# Draft upstream report — not submitted

Subject: AYN Thor .377: scan lockup recovered by keeping Qualcomm PCI runtime PM active before framework restart

Thanks for your recovery work. On one Thor running Android 13 and Thor_V1.0.0.377_20260206_165408_user, v0.3.0 reported probable lockup and recovery did not restore scans (scanner still stuck after 93.5 s). Kernel kiwi_v2 scans nevertheless found 14–19 BSS with COMPLETED status; Android returned zero.

PCI device 0000:01:00.0 (17cb:1107, cnss_pci) was runtime-suspended with power/control=auto. Using the stock root script launcher, setting its power/control to on woke the device, but Android remained stuck. A subsequent explicit zygote restart restored 17 Android scan results, IdleState, carrier=1 and Internet access. The previous framework-only attempt failed.

Potential optional experiment: validate the exact firmware and PCI identity, set power/control=on, verify readback, then offer an explicit framework restart if needed. Provide rollback to auto, disclose potential battery impact and avoid automatic restart. No permanent fix claimed; only one combined successful field trial. Prevention, battery and boot persistence remain untested. EHT/MLO warnings were also observed; their role is unknown.

Evidence and qualification plan: https://github.com/Proginji2000/ayn-thor-wifi-fix

Reference: https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery (v0.3.0). No raw private logs included.

## Follow-up — important limitation
A second verified framework restart with PCI power/control=on recovered a first scan (18 results), then Android's next scan became stuck despite PCI remaining active and carrier=1. Kernel scan 40963 completed with 15 BSS. The runtime PM workaround is therefore not sufficient prevention; do not integrate it as a permanent fix. Investigation of Android scan result delivery/processing continues.

## Current assessment (2026-11-26) — supersedes the initial PM proposal
Repeated stock diagnostics support a non-progressing Wi-Fi scan-result parser in Android; stock recurrence was observed after return from Fastboot. Historical Java candidate V2 and matching ART artifacts restored scanner responsiveness with PCI runtime PM auto; the crossover test did not establish a need to force PCI on. V3.0 manual volatile activation was verified, not permanent startup. V3.3-r3 local repeatability PASS (two complete builds); V3.4-r2 isolated native ART compilation PASS, with distinct ODEX/VDEX hashes and unchanged active historical V2 system. New runtime qualification and permanent installation remain pending. Request a supported vendor correction and coordinate technical details privately. Do not recommend the initial PM workaround as permanent prevention. This document is a historical draft; no submission or vendor acknowledgment is established.

V3.5-r2: new native bundle loaded successfully; seven of eight fresh scan cycles passed, all eight scanner health checks and both IP probes passed. First scan did not refresh within 30 s; reason unresolved. Stock rollback verified. No permanent installation or complete runtime qualification claimed.

V3.5-r3 functional runtime qualification PASS on exact .377 firmware with 45 s startup stabilization: fresh scan cycles 8/8, scanner responsive 8/8, interface-bound IP probes 2/2, framework stability and executable ODEX/VDEX mapping checks PASS, normal cleanup reboot and exact stock tuple rollback PASS. Historical r2 7/8 remains recorded. HTTPS not automated; watchdog expiry rollback, new-bundle extended use, partition restoration, installer and boot persistence not qualified. Deployment remains denied.

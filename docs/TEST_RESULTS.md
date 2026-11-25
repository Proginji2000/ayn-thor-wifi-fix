# Field test — 2026-11-25

Status: recovery PASS on one AYN Thor; prevention and persistence NOT QUALIFIED.

## Device
- Android 13 / API 33; firmware `Thor_V1.0.0.377_20260206_165408_user`.
- Linux 5.15.123; Qualcomm PCI 17cb:1107 at 0000:01:00.0; driver cnss_pci, modules kiwi_v2 and cnss2.
- Native Thor Settings root script launcher confirmed uid=0, context u:r:pservice:s0.
- No firmware or system partition changes.

## Observations
- Android wifiscanner stuck in ScanningState; dumpsys timeout; no Android scan results; carrier 0.
- Kernel scans completed with 14–19 BSS even during failure. Firmware ready events observed.
- Logs showed EHT/802.11be and MLO parsing warnings, not established causal.
- PCI power/control=auto; runtime_status=suspended. WLAN INI gRuntimePM=2, gRuntimePMDelay=500. Suspension alone is normal and not proof of a defect.
- Earlier PowerShell scalar matching gave misleading counts of 1; corrected line-by-line counting returned 0 during failure.

## Intervention matrix
| Intervention | Result |
|---|---|
| Framework restart only | FAIL |
| Custom deep recovery scripts | Execution not fully proven |
| JoelMomo recovery app v0.3.0 | FAIL: scanner still stuck after reported 93.5 s |
| PCI power/control=on alone | PASS for configuration, FAIL for recovery |
| PCI power/control=on followed by framework restart | PASS |

## Successful trial
At 19:41:08 CET, framework restart requested after PCI setting on/active confirmed. At 19:41:17.456 kernel scan started; at 19:41:20.113 it completed with 17 BSS. Android returned 17 results, transitioned ScanningState to IdleState at 19:41:20.122, and carrier=1. User confirmed YouTube access. PCI remained on/active.

## Limits
Single device, single successful combined trial. No controlled repeated A/B trials. No proof of causality or prevention. Internet access confirmed by user, not measured by automated test. No battery measurement, boot persistence, or wake-cycle qualification. Do not infer a permanent fix. Avoid PCI unbind/reset until independently justified.

Raw logs are intentionally not published: they may contain MAC addresses, network identifiers or local paths.

## Full reboot follow-up — 19:52 CET
User rebooted the device and reported loss of Wi-Fi. ADB confirmed power/control=auto, runtime_status=suspended, carrier=0 and Android scanner entering ScanningState at 19:52:06.321, followed by a 5-second dumpsys timeout. The temporary runtime PM setting does not survive this reboot. This does not establish causality. A second manual combined recovery trial is pending; defer boot automation until reproducibility is demonstrated.

## Second recovery attempt — 19:55 CET
After full reboot, manual PCI policy write was verified on/active. Following the requested framework restart, readback was auto/suspended, carrier=0 and Android scan count=0. Scanner history retained the exact 19:52:06.321 transition; framework restart execution was not established. Treat as failed recovery with an inconclusive protocol, not a controlled negative replication. Next trial must use uniquely named scripts, a fresh execution marker, system_server PID and boot ID before/after, and PCI readback. Boot automation remains deferred.

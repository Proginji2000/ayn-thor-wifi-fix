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

## Controlled replication — 19:57–19:58 CET
PCI policy verified on/active before and after framework restart. Fresh execution marker at 19:57:15; system_server PID changed 2142 -> 8552, Linux boot ID unchanged. First scan returned to IdleState at 19:57:26.836. Android scan cache contained 18 entries and carrier=1 at final check. A subsequent scan entered ScanningState at 19:58:04.114 and dumpsys timed out after 5 seconds. Thus initial recovery was reproduced, but scanner timeout recurred with runtime PM disabled. Current Internet connectivity not yet confirmed; cache count and carrier do not prove a fresh scan or Internet access. A timeout alone does not establish indefinite deadlock; follow-up needed. Do not treat PCI power policy alone as adequate prevention or ship automatic boot persistence. Investigate fresh kernel completion versus framework notification/processing and EHT/MLO warnings.

## Follow-up of the second scan
Kernel scan 40963 started at 19:58:04.124 and completed at 19:58:09.395 with 15 BSS, while Android remained in ScanningState and a later 10-second dumpsys timed out. PCI remained on/active and carrier=1. EHT operation IE length, MLO partner offset and regulatory opclass errors were observed. Causation not established. Next diagnostic: targeted Java thread stacks from system_server, then inspect wificond if indicated. No further boot automation until prevention is qualified.

## Java thread dump — MLO parser localization
A debuggerd Java stack snapshot on system_server PID 8552 identified WifiScanningService (tid 93, sysTid 8679) Runnable, cumulative CPU time ~165 s, at InformationElementUtil$MultiLink.parseLinkInfoField (line 975), called by MultiLink.from (1096), NetworkDetail constructor (261), WifiNative.convertNativeScanResults (1837), getScanResults (1750), and WificondScannerImpl.pollLatestScanData (396). The scanner held a Java monitor; two Binder dump threads waited for that same monitor at WificondScannerImpl.dump (509). This explains the dumpsys timeout and localizes the stall to MLO information-element processing. Infinite loop is strongly suspected, not yet proven by inspecting the exact shipped bytecode or repeated independent stack snapshots. An independent October 11 2026 community report names the same method and reports improvement after disabling router MLO and rebooting: https://www.reddit.com/r/AynThor/comments/1x308wu/wifi_issues_finally_resolved/ . Router-side mitigation is not a universal fix because nearby networks may advertise MLO. Next: read-only inventory and extraction of actual Wi-Fi module JAR for offline inspection, and controlled MLO-off test if feasible. No system modifications, no automated boot workaround. Raw thread dump withheld for privacy.

## Offline inspection of shipped Wi-Fi module
The user supplied service-wifi-1.jar (SHA-256 69884bb5f83314f50a5b3fd41bf5119f07969c5a7c48c97b78dde9757f811b90). Its classes.dex was inspected directly using a read-only DEX parser. The exact MultiLink.parseLinkInfoField method contains a backward branch that returns to the loop head without advancing the input cursor on an unsupported subelement path. This confirms a static non-progress defect consistent with the Runnable scanner thread and held monitor observed on-device. The actual triggering radio input was not captured or reproduced offline. An AOSP comparison shows subsequent MLO parser changes (including fragmentation handling), but an exact applicable upstream fix has not been verified. Corrective design: guarantee forward progress or safely reject unsupported/malformed data, validate bounds and preserve normal MLO parsing. Next gate: identify installed APEX version, update channel and integrity constraints; prefer official signed update. No JAR replacement, AVB bypass, or firmware change attempted. Do not publish original proprietary binary or triggering radio data. Runtime PM persistence is not a definitive fix.

## Deployment inventory — 2026-11-25
ADB reports verifiedbootstate=orange, vbmeta.device_state=unlocked, flash.locked=0, ro.debuggable=0, user build, security patch 2024-01-01. ro.apex.updatable unset; apexservice unavailable; /system/apex/com.android.wifi is a directory. Active /apex/com.android.wifi is mounted from dm-14 ext4 read-only. service-wifi.jar size 4,720,881 bytes. These observations strongly suggest a flattened APEX; confirm mountinfo and source/active hashes. AOSP docs state flattened APEXes are normally updated through regular OTA, not independent APEX installation: https://source.android.com/docs/core/ota/apex . Unlocked status does not establish writability, verity status or safe rollback. No mount writes, flashing, security changes or patch installation performed. Prefer OEM correction; offline parser regression tests and exact matching recovery material are required before device deployment.

## Deployment gate — verified system protection
Mountinfo confirms flattened com.android.wifi bind mount from system dm-14, read-only; device mapper name system-verity; ro.boot.veritymode=enforcing, AVB 1.2, slot _a, dynamic partitions and Virtual A/B enabled. Source and mounted service-wifi.jar SHA-256 both match the supplied archive. The find command was interrupted by shell permission error; absence of ART precompiled files is not established. Do not remount system rw, disable verity, change slots or flash. Recovery image and rollback path not qualified.

## Static analysis refinement
Reinspection of the local archive confirms the exact hash, one classes.dex, and the target method. The loop computes a next cursor from the current cursor and a length field, and the common backward path copies this calculated cursor before returning to the loop head. This refines the earlier shorthand that an unsupported subelement always leaves the cursor unchanged: progress depends on the length, and is not guaranteed. A candidate fix must reject non-progressing or out-of-bounds elements and preserve supported parsing. No specific over-the-air triggering input has been established. No corrected binary built or tested yet. Offline disassembly and regression tests precede any device deployment. AOSP changes to fragmentation handling are useful comparison, not a verified direct fix.

## Independent WSL disassembly
User SHA-256 verification, extraction and Android SDK 36.0.0 dexdump succeeded. The method contains 100 code units, and the cursor arithmetic and back edge match the original archive inspected locally. The subelement length accounting and progress invariant require correction, together with minimum per-profile length and upper bounds. Android's upstream Wi-Fi module contains subsequent MLO parser/fragmentation changes (AOSP commit 483d4341545993f3b0a450d9c4e325223c3c424d), but the exact applicable corrective revision has not been established. Do not publish trigger inputs or original binaries; report detailed reproduction to AYN privately. smali/baksmali/jadx were not found in WSL PATH. Next: obtain trusted assembler/disassembler, qualify a minimal source-level correction against the exact local JAR, then conduct offline tests. Deployment remains blocked by enforcing system verity and unqualified restoration. No corrected JAR built or installed yet.

## Offline toolchain ready
WSL installation of smali and baksmali 2.5.2.git2771eae-debian succeeded; full disassembly completed and target class located. A local experimental builder was prepared to require the known original JAR hash, replace only the target method, enforce header-inclusive cursor progression and payload bounds, reassemble and compare re-disassembled class inventory and all non-target methods/classes, and preserve non-DEX archive entries. Python syntax and synthetic method-selection checks executed successfully in assistant environment. Actual smali assembly and ART execution have NOT yet been run; no candidate JAR has been produced or installed. Fragmentation behavior and compatibility require dedicated tests. Deployment remains blocked; no verity or partition changes.

## Offline candidate build — PARTIAL
User ran the experimental builder in WSL. Original disassembly, candidate assembly and candidate redisassembly completed; the exact-text non-target comparison stopped at com/android/server/wifi/HalDeviceManager.smali. No final candidate JAR produced by this run. The cause of the difference is not established. Next: independently round-trip the unmodified DEX using the same toolchain and API level, inspect original/baseline differences and compare baseline against candidate excluding the single intended method. A matching baseline does not alone establish semantic equivalence: inspect all distinct transformations before accepting the gate. No relaxation of the integrity gate, device installation or partition changes.

## Baseline round-trip comparison
Unmodified DEX round-trip produced 14 differing Smali class files. Candidate versus round-tripped baseline produced exactly one differing class: InformationElementUtil$MultiLink. The displayed HalDeviceManager difference removes an explicit static boolean false initializer, which is the DEX default; the remaining 13 classes have not yet been classified. A local follow-up checker was prepared to accept only exact removal of primitive static default initializers, require identical class inventories and exact equality outside the target method relative to the baseline, check DEX header integrity and preserve non-DEX JAR entries. Python syntax and six synthetic acceptance/rejection checks passed; actual full-tree qualification remains pending. Candidate JAR must remain offline; no ART behavior or device test, no deployment.

## Full static comparison — PASS; archive packaging retry pending
User verifier reported 3,138 classes, all 14 baseline differences classified as removal of explicit static boolean false initializers, and only the target parseLinkInfoField method differing from the baseline. DEX header checks completed before archive verification failed with Python zipfile.BadZipFile: Truncated file header. Root cause in verifier: passing original ZipInfo objects to writestr mutates their offsets, invalidating later source reads. Original supplied JAR SHA-256 independently verified and all 9 entries passed testzip. A revised local verifier copies metadata, snapshots original entries, checks output in a temporary file, and publishes under a new name without overwrite only after successful verification. Python syntax, original DEX header, and packaging tests on the actual supplied archive passed with unchanged and changed-size test payloads (latter is a packaging-only synthetic payload, not executable). All non-DEX entries preserved in tests, overwrite rejected, temporary files cleaned and source unchanged. Actual patched candidate packaging retry on WSL pending. Previous partial artifact not trusted. ART execution, parser regression behavior and deployment remain unqualified.

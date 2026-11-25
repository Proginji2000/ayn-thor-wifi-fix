# Manual recovery (experimental)

Only tested on one AYN Thor with firmware Thor_V1.0.0.377_20260206_165408_user and PCI identity 17cb:1107 at 0000:01:00.0. Save all games and close apps. Use ADB USB to read back the firmware, vendor/device IDs and original power/control value before any intervention. Stop on mismatch, missing device, or unexpected initial state.

Use the stock Thor Settings root script launcher with individual simple shell files (LF, UTF-8 without BOM). Complex variants previously failed to produce complete logs. These are the commands used in the successful trial, not a persistent installation.

1. Confirm original power/control is auto. Execute a shell script containing:
```sh
#!/system/bin/sh
echo on > /sys/bus/pci/devices/0000:01:00.0/power/control
```
2. Read back power/control=on and power/runtime_status=active via ADB. Stop if not confirmed.
3. Only if the scanner is already stuck, save games and execute a separate root script:
```sh
#!/system/bin/sh
setprop ctl.restart zygote
```
4. Wait for Android to return. Confirm PCI mode is still on, fresh scan results, scanner responsiveness, actual association and Internet access.
5. If the change causes adverse effects or is no longer desired, restore the recorded original mode using a separate root script:
```sh
#!/system/bin/sh
echo auto > /sys/bus/pci/devices/0000:01:00.0/power/control
```
Verify readback. Rollback was prepared but not yet exercised on the test device. Do not automatically restart the framework on boot.

No firmware edits, SELinux changes, PCI reset or network deletion. The combined recovery succeeded once; prevention and battery effects are not established. 

#!/usr/bin/env python3
"""Read-only preflight for AYN Thor Manual Edition. No activation or root commands."""
import argparse
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def adb(executable, *args):
    # -d selects a single USB device and refuses ambiguous connections.
    p = subprocess.run([executable, "-d", *args], capture_output=True,
                       timeout=30, check=False)
    require(p.returncode == 0, "ADB command failed; check USB authorization")
    return p.stdout

def shell(executable, command):
    return adb(executable, "shell", command).decode("utf-8", errors="strict").strip()

def preflight(executable, firmware):
    for prop, expected in (
        ("ro.build.display.id", firmware["build_id"]),
        ("ro.product.device", firmware["device"]),
        ("ro.build.version.sdk", str(firmware["android_api"])),
        ("ro.boot.slot_suffix", "_a"),
        ("sys.boot_completed", "1"),
    ):
        require(shell(executable, "getprop " + prop) == expected,
                "Unexpected " + prop)
    require(shell(executable, "cat /sys/bus/pci/devices/0000:01:00.0/power/control") == "auto",
            "Unexpected PCI policy")
    require(shell(executable, "service check wifi") == "Service wifi: found",
            "Wi-Fi service unavailable")
    for a in firmware["artifacts"]:
        result = shell(executable, "sha256sum < " + shlex.quote(a["path"]))
        require(result.split()[:1] == [a["stock_sha256"]], "Non-stock or unknown " + a["name"])
        print("STOCK_HASH_PASS", a["name"])

def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--adb", default="adb", help="ADB executable or absolute path")
    parser.add_argument("--extract-stock", type=Path, help="New local directory for private stock files")
    parser.add_argument("--bundle", type=Path, help="Optional local candidate directory to verify")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "compatibility/firmware-matrix.json").read_text(encoding="utf-8"))
    require(manifest["default_policy"] == "deny_activation", "Unexpected manifest policy")
    require(len(manifest["firmwares"]) == 1, "Unexpected compatibility matrix")
    fw = manifest["firmwares"][0]
    require(fw["build_id"] == "Thor_V1.0.0.377_20260206_165408_user", "Unexpected manifest build")
    require(adb(args.adb, "get-state").strip() == b"device", "USB device not ready")
    boot = shell(args.adb, "cat /proc/sys/kernel/random/boot_id")
    require(bool(boot), "Missing boot identity")
    preflight(args.adb, fw)
    if args.bundle:
        candidate = fw["offline_candidate_v33r3"]
        for name, key in (("input.jar", "jar_sha256"), ("service-wifi.odex", "odex_sha256"),
                          ("service-wifi.vdex", "vdex_sha256")):
            require(sha((args.bundle / name).read_bytes()) == candidate[key], "Candidate mismatch: " + name)
            print("CANDIDATE_HASH_PASS", name)
    if args.extract_stock:
        args.extract_stock.mkdir(mode=0o700, parents=False, exist_ok=False)
        for a in fw["artifacts"]:
            data = adb(args.adb, "exec-out", "cat", a["path"])
            require(sha(data) == a["stock_sha256"], "Stock extraction mismatch: " + a["name"])
            with (args.extract_stock / a["name"]).open("xb") as out:
                out.write(data)
            print("STOCK_EXTRACT_PASS", a["name"])
        print("Keep the extracted stock files private; do not upload them to GitHub.")
    require(shell(args.adb, "cat /proc/sys/kernel/random/boot_id") == boot, "Device rebooted during preflight")
    preflight(args.adb, fw)
    print("READ_ONLY_PREFLIGHT_PASS")
    return 0

if __name__ == "__main__":
    try:
        rc = run()
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print("STOP:", type(exc).__name__, str(exc), file=sys.stderr)
        rc = 1
    finally:
        print("DEPLOYMENT_ALLOWED=false")
    sys.exit(rc)

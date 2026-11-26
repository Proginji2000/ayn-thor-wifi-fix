#!/usr/bin/env python3
"""Offline exact-bundle check. No ADB, compilation, activation or writes."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

EXPECTED = {
    "input.jar": "3a4f3d5df69a2c7ed733c5454599921ab98974d243b4c4448391812a3e468202",
    "service-wifi.odex": "5f52a3e8434bc473821d661fcb56cafee666960c42068cb57673176fe8460d41",
    "service-wifi.vdex": "cd07ab2a5645cae97b114c5c33b3f60b2f96cfe4ad15d300dddf7c3c89efd67c",
}


def verify(bundle, expected=EXPECTED):
    results = {}
    for name, digest in expected.items():
        path = bundle / name
        if path.is_symlink() or not path.is_file():
            results[name] = "MISSING_OR_NOT_REGULAR"
            continue
        with path.open("rb") as stream:
            h = hashlib.sha256()
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                h.update(chunk)
        results[name] = "PASS" if h.hexdigest() == digest else "HASH_MISMATCH"
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    args = parser.parse_args()
    try:
        results = verify(args.bundle)
        ok = all(value == "PASS" for value in results.values())
        print(json.dumps({"status": "PASS" if ok else "FAIL", "files": results,
                          "deployment_allowed": False}, indent=2))
        return 0 if ok else 1
    except OSError as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc),
                          "deployment_allowed": False}, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())

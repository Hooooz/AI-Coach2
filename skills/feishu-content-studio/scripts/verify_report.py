#!/usr/bin/env python3
import json
import sys

REQUIRED_STATUS = {"success", "partial", "failed"}


def fail(msg: str):
    print(f"INVALID: {msg}")
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        fail("usage: verify_report.py <report.json>")

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        r = json.load(f)

    if r.get("status") not in REQUIRED_STATUS:
        fail("status must be success|partial|failed")

    art = r.get("artifact") or {}
    if not art.get("type") or not art.get("token"):
        fail("artifact.type and artifact.token are required")

    v = r.get("validation") or {}
    if "input_valid" not in v or "readback_pass" not in v:
        fail("validation.input_valid and validation.readback_pass are required")

    checks = r.get("api_checks") or {}
    if "scopes_ok" not in checks or not isinstance(checks.get("operations", []), list):
        fail("api_checks.scopes_ok and api_checks.operations[] are required")

    print("VALID")


if __name__ == "__main__":
    main()

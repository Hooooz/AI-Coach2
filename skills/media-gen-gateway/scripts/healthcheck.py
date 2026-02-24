#!/usr/bin/env python3
import os
import sys
import urllib.request


def main():
    base = os.getenv("MEDIA_API_BASE", "").strip()
    cookie = os.getenv("MEDIA_AUTH_COOKIE", "").strip()

    if not base:
        print("INVALID: MEDIA_API_BASE missing")
        sys.exit(1)
    if not cookie:
        print("INVALID: MEDIA_AUTH_COOKIE missing")
        sys.exit(1)

    req = urllib.request.Request(base)
    req.add_header("Cookie", cookie)

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"OK: {resp.status}")
    except Exception as e:
        print(f"FAIL: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()

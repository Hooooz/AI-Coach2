#!/usr/bin/env python3
import hashlib
import json
import os
import sys
import time
import urllib.request


VALID_TYPES = {"text2image", "image2image", "text2video"}


def die(msg, code=1):
    print(msg)
    sys.exit(code)


def request_json(url, method="GET", body=None, headers=None, timeout=30):
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, method=method, data=data)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    if len(sys.argv) != 2:
        die("usage: submit_and_poll.py <request.json>")

    base = os.getenv("MEDIA_API_BASE", "").rstrip("/")
    cookie = os.getenv("MEDIA_AUTH_COOKIE", "")
    outdir = os.getenv("MEDIA_OUTPUT_DIR", "./outputs")
    timeout_seconds = int(os.getenv("MEDIA_TIMEOUT_SECONDS", "300"))

    if not base or not cookie:
        die("MEDIA_API_BASE and MEDIA_AUTH_COOKIE are required")

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        payload = json.load(f)

    if payload.get("task_type") not in VALID_TYPES:
        die("invalid task_type")
    if payload.get("task_type") == "image2image" and not payload.get("source_image_path"):
        die("source_image_path required for image2image")

    headers = {"Content-Type": "application/json", "Cookie": cookie}
    req_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    submit = request_json(f"{base}/submit", method="POST", body=payload, headers=headers)
    job_id = submit.get("job_id")
    if not job_id:
        die("submit failed: missing job_id", 2)

    start = time.time()
    status = "pending"
    result = None
    while time.time() - start < timeout_seconds:
        info = request_json(f"{base}/status/{job_id}", headers=headers)
        status = info.get("status", "unknown")
        if status in {"success", "failed"}:
            result = info
            break
        time.sleep(3)

    os.makedirs(outdir, exist_ok=True)
    manifest = {
        "status": status if result else "timeout",
        "task_type": payload["task_type"],
        "job_id": job_id,
        "request_hash": req_hash,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(start)),
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "outputs": (result or {}).get("outputs", []),
        "params": payload,
        "error": (result or {}).get("error"),
    }

    mp = os.path.join(outdir, f"{job_id}.manifest.json")
    with open(mp, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(mp)


if __name__ == "__main__":
    main()

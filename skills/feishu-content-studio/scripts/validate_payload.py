#!/usr/bin/env python3
import json
import sys

REQUIRED_TYPES = {"doc", "sheet", "ppt", "mindmap", "flowchart"}


def fail(msg: str):
    print(f"INVALID: {msg}")
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        fail("usage: validate_payload.py <job_spec.json>")

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)

    t = data.get("artifact_type")
    if t not in REQUIRED_TYPES:
        fail("artifact_type must be one of doc|sheet|ppt|mindmap|flowchart")

    title = (data.get("title") or "").strip()
    if not title:
        fail("title is required")

    content = data.get("content") or {}
    sections = content.get("sections") or []
    if not isinstance(sections, list):
        fail("content.sections must be a list")

    for i, sec in enumerate(sections):
        if not isinstance(sec, dict):
            fail(f"section[{i}] must be object")
        if not (sec.get("heading") or "").strip():
            fail(f"section[{i}].heading required")

    print("VALID")


if __name__ == "__main__":
    main()

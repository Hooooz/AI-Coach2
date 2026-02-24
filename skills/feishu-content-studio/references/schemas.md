# Schemas

## Job Spec (input)

```json
{
  "artifact_type": "doc|sheet|ppt|mindmap|flowchart",
  "title": "string",
  "content": {
    "sections": [
      {"heading": "string", "body": "string"}
    ]
  },
  "target": {
    "folder_token": "optional-string",
    "wiki_space_id": "optional-string"
  },
  "options": {
    "idempotent": true,
    "strict_validation": true,
    "language": "zh-CN"
  }
}
```

## Verification Report (output)

```json
{
  "status": "success|partial|failed",
  "artifact": {
    "type": "doc|sheet|ppt|mindmap|flowchart",
    "token": "string",
    "title": "string"
  },
  "validation": {
    "input_valid": true,
    "readback_pass": true,
    "missing_sections": []
  },
  "api_checks": {
    "scopes_ok": true,
    "operations": [
      {"name": "create", "ok": true, "detail": "..."}
    ]
  },
  "notes": ["optional warnings"],
  "next_actions": ["optional follow-ups"]
}
```

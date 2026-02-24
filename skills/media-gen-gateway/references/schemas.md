# Schemas

## Request

```json
{
  "task_type": "text2image|image2image|text2video",
  "prompt": "string",
  "negative_prompt": "optional",
  "style": "optional",
  "size": "1024x1024",
  "duration": 5,
  "source_image_path": "required for image2image",
  "options": {
    "seed": 12345,
    "count": 1,
    "timeout_seconds": 300
  }
}
```

## Manifest

```json
{
  "status": "success|failed|timeout",
  "task_type": "text2image|image2image|text2video",
  "job_id": "string",
  "request_hash": "string",
  "created_at": "iso8601",
  "completed_at": "iso8601",
  "outputs": [
    {"path": "string", "mime": "image/png|video/mp4"}
  ],
  "params": {},
  "error": "optional string"
}
```

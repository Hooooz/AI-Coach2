---
name: media-gen-gateway
description: Generate images/videos through authorized media gateways with text-to-image, image-to-image, and text-to-video workflows, plus polling, result download, and reliability checks. Use when users request compliant creative generation pipelines, cookie/env based auth configuration, health checks, or reproducible output metadata.
---

# Media Gen Gateway

Implement media generation via authorized endpoints only.

## Safety and compliance

- Require explicit authorization to use the target endpoint/account.
- Do not provide or execute bypass logic for unauthorized/reverse-engineered services.
- Keep secrets in environment variables; never hardcode cookies/tokens in skill files.

## Execution workflow

1. Build runtime config.
   - `MEDIA_API_BASE`
   - `MEDIA_AUTH_COOKIE` or token equivalent
   - timeout/retry settings
2. Validate request payload.
   - `task_type`: `text2image|image2image|text2video`
   - prompt, size/aspect, model/style, negative prompt (optional)
   - source image required for `image2image`
3. Submit job.
   - Capture `job_id`, created time, request hash.
4. Poll job status until done/failed/timeout.
5. Download artifacts and write metadata manifest.
6. Return concise result summary and file paths.

## Reliability rules

- Retry transient 5xx/timeout up to 3 times with backoff.
- Stop immediately on 401/403 and surface auth failure.
- Save a JSON manifest for every run, including seed/params/job id.

## Use bundled scripts

- `scripts/healthcheck.py`: verify endpoint/auth reachability.
- `scripts/submit_and_poll.py`: submit task and poll completion.

## References

- Request and manifest schema: `references/schemas.md`
- Operational runbook: `references/runbook.md`

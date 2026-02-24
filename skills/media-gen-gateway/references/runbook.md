# Runbook

## Environment

- `MEDIA_API_BASE` required
- `MEDIA_AUTH_COOKIE` or provider token required
- `MEDIA_OUTPUT_DIR` optional (default `./outputs`)

## Health check

```bash
python3 scripts/healthcheck.py
```

## Submit and poll

```bash
python3 scripts/submit_and_poll.py request.json
```

## Failure handling

- 401/403: refresh auth and retry manually
- 429: increase retry backoff
- timeout: reduce generation complexity or increase timeout

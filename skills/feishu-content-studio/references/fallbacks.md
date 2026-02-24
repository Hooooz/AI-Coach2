# Fallback Matrix

## Capability fallbacks

1. If `feishu_doc` block-level update fails:
   - fallback to full `write` replacement with clear warning.
2. If sheet cell-level editing is unavailable:
   - create sheet object + companion doc table content.
3. If PPT fine-grained editing is unavailable:
   - create PPT object + companion doc slide script.
4. If mindnote object creation unavailable:
   - use hierarchical markdown in doc.

## Retry policy

- Retry transient failures up to 2 times with exponential backoff.
- Do not retry permission-denied errors.

## Output rule

Always return a verification report even on partial failure.

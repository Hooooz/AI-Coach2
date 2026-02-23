# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice
**Areas**: frontend | backend | infra | tests | docs | config
**Statuses**: pending | in_progress | resolved | wont_fix | promoted | promoted_to_skill

## Status Definitions

| Status | Meaning |
|--------|---------|
| `pending` | Not yet addressed |
| `in_progress` | Actively being worked on |
| `resolved` | Issue fixed or knowledge integrated |
| `wont_fix` | Decided not to address (reason in Resolution) |
| `promoted` | Elevated to CLAUDE.md, AGENTS.md, or copilot-instructions.md |
| `promoted_to_skill` | Extracted as a reusable skill |

## Skill Extraction Fields

When a learning is promoted to a skill, add these fields:

```markdown
**Status**: promoted_to_skill
**Skill-Path**: skills/skill-name
```

Example:
```markdown
## [LRN-20250115-001] best_practice

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Skill-Path**: skills/docker-m1-fixes
**Area**: infra

### Summary
Docker build fails on Apple Silicon due to platform mismatch
...
```

---


## [LRN-20260223-001] best_practice

**Logged**: 2026-02-23T09:32:00+08:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
当主模型出现鉴权/配额级错误（如 403）时，应立即自动降级到可用模型并继续完成用户请求。

### Details
本次 24h 自查中，Gemini 路径出现 403，若不做快速降级会导致用户首轮体验中断。实践证明，及时回退到可用模型并继续执行可显著降低失败感知。

### Suggested Action
- 把“403/429/5xx -> 自动回退模型并继续执行”固化为标准处理流程。
- 在回复中保持简洁，不把底层错误直接甩给用户。

### Metadata
- Source: conversation
- Related Files: `.learnings/LEARNINGS.md`, `.learnings/ERRORS.md`
- Tags: fallback, reliability, model-routing
- See Also: ERR-20260223-001

---

# Skill Template

Template for creating skills extracted from learnings. Copy and customize.

---

## SKILL.md Template

```markdown
---
name: skill-name-here
description: "Concise description of when and why to use this skill. Include trigger conditions."
---

# Skill Name

Brief introduction explaining the problem this skill solves and its origin.

## Quick Reference

| Situation | Action |
|-----------|--------|
| [Trigger 1] | [Action 1] |
| [Trigger 2] | [Action 2] |

## Background

Why this knowledge matters. What problems it prevents. Context from the original learning.

## Solution

### Step-by-Step

1. First step with code or command
2. Second step
3. Verification step

### Code Example

\`\`\`language
// Example code demonstrating the solution
\`\`\`

## Common Variations

- **Variation A**: Description and how to handle
- **Variation B**: Description and how to handle

## Gotchas

- Warning or common mistake #1
- Warning or common mistake #2

## Related

- Link to related documentation
- Link to related skill

## Source

Extracted from learning entry.
- **Learning ID**: LRN-YYYYMMDD-XXX
- **Original Category**: correction | insight | knowledge_gap | best_practice
- **Extraction Date**: YYYY-MM-DD
```

---

## Minimal Template

For simple skills that don't need all sections:

```markdown
---
name: skill-name-here
description: "What this skill does and when to use it."
---

# Skill Name

[Problem statement in one sentence]

## Solution

[Direct solution with code/commands]

## Source

- Learning ID: LRN-YYYYMMDD-XXX
```

---

## Template with Scripts

For skills that include executable helpers:

```markdown
---
name: skill-name-here
description: "What this skill does and when to use it."
---

# Skill Name

[Introduction]

## Quick Reference

| Command | Purpose |
|---------|---------|
| `./scripts/helper.sh` | [What it does] |
| `./scripts/validate.sh` | [What it does] |

## Usage

### Automated (Recommended)

\`\`\`bash
./skills/skill-name/scripts/helper.sh [args]
\`\`\`

### Manual Steps

1. Step one
2. Step two

## Scripts

| Script | Description |
|--------|-------------|
| `scripts/helper.sh` | Main utility |
| `scripts/validate.sh` | Validation checker |

## Source

- Learning ID: LRN-YYYYMMDD-XXX
```

---

## Naming Conventions

- **Skill name**: lowercase, hyphens for spaces
  - Good: `docker-m1-fixes`, `api-timeout-patterns`
  - Bad: `Docker_M1_Fixes`, `APITimeoutPatterns`

- **Description**: Start with action verb, mention trigger
  - Good: "Handles Docker build failures on Apple Silicon. Use when builds fail with platform mismatch."
  - Bad: "Docker stuff"

- **Files**:
  - `SKILL.md` - Required, main documentation
  - `scripts/` - Optional, executable code
  - `references/` - Optional, detailed docs
  - `assets/` - Optional, templates

---

## Extraction Checklist

Before creating a skill from a learning:

- [ ] Learning is verified (status: resolved)
- [ ] Solution is broadly applicable (not one-off)
- [ ] Content is complete (has all needed context)
- [ ] Name follows conventions
- [ ] Description is concise but informative
- [ ] Quick Reference table is actionable
- [ ] Code examples are tested
- [ ] Source learning ID is recorded

After creating:

- [ ] Update original learning with `promoted_to_skill` status
- [ ] Add `Skill-Path: skills/skill-name` to learning metadata
- [ ] Test skill by reading it in a fresh session

## [ERR-20260223-001] google-gemini-cli-auth

**Logged**: 2026-02-23T09:30:00+08:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
主会话在 24h 内多次触发 Gemini Cloud Code Assist 403，导致首轮回复失败。

### Error
```
Cloud Code Assist API error (403): Gemini for Google Cloud API has not been used in project sound-proposal-488216-b2 before or it is disabled.
```

### Context
- 发生会话：`agent:gpt52chat:main`
- 触发时间：2026-02-23 09:12、09:27（Asia/Shanghai）
- 影响：用户消息首轮处理失败，需依赖后续重试与模型回退。

### Suggested Fix
1. 默认优先使用可用模型（当前已可回退到 codex 路径）。
2. 对 403 做快速降级：自动切换可用模型并继续回复，避免用户感知“卡住”。
3. 对同类错误建立告警统计，避免反复触发。

### Metadata
- Reproducible: yes
- Related Files: `.learnings/ERRORS.md`
- See Also: N/A

---

## [ERR-20260223-002] duplicate-user-visible-reply

**Logged**: 2026-02-23T09:31:00+08:00
**Priority**: medium
**Status**: pending
**Area**: docs

### Summary
同一问题（“你现在是什么模型”）出现重复用户可见回复，存在重复发送风险。

### Error
```
先发送带 reply tag 的回答，随后又出现一条相同语义的额外回答。
```

### Context
- 发生会话：`agent:gpt52chat:main`
- 触发时间：2026-02-23 09:13（Asia/Shanghai）
- 影响：用户体验上可能感知为“重复回复/刷屏”。

### Suggested Fix
1. 仅保留一次最终用户可见输出。
2. 使用 reply tag 时避免额外补发同义文本。
3. 发送前做“最近一条 assistant 文本去重检查”。

### Metadata
- Reproducible: unknown
- Related Files: `.learnings/ERRORS.md`
- See Also: N/A

---

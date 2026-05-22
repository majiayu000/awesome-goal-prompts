# Quality Bar

Use this reference before finalizing high-risk goals or reviewing an existing goal.

## Accept Good Goals

Accept or generate goals that:

- Have one real engineering scenario and one primary objective.
- Include deterministic verification where possible.
- Protect tests, data, secrets, user-visible behavior, and production systems.
- Name real context instead of asking the agent to guess.
- Teach or reuse a pattern that is meaningfully different from existing examples.
- Include an incomplete state when local verification or access is impossible.

## Reject Weak Goals

Reject or tighten goals that:

- Say only "optimize the app", "fix all bugs", "make it better", or similar.
- Ask the agent to weaken tests, swallow errors, invent contracts, or bypass auth.
- Require reading, printing, or hardcoding secrets.
- Ask for automatic merge, force push, or production deployment without explicit human approval.
- Differ from an existing goal only by framework, language, or wording.
- Claim completion without fresh verification.

## Non-Negotiable Sections

Every full goal needs:

- `GOAL`: one objective, not a backlog.
- `CONTEXT`: what the agent must inspect before acting.
- `CONSTRAINTS`: boundaries, non-goals, and safety rules.
- `DONE WHEN`: a measurable completion state.
- `VERIFY`: exact command, artifact, report, screenshot, or manual evidence.
- `OUTPUT`: what the final report must contain.
- `STOP RULES`: when to pause instead of guessing.

## Safety Constraints By Risk

Security and auth:

- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use unsafe HTML injection, `eval`, shell string concatenation, or string-built SQL.
- Validate URLs and links with allowlists such as protocol allowlists instead of blacklist-only checks.
- Do not print, copy, rotate, or exfiltrate real secrets.

Data and migrations:

- Do not destroy or rewrite data without the goal explicitly naming `dry-run`. Require a `dry-run` when supported; if true dry-run is unavailable, state that and require a disposable-environment rehearsal instead. Also require rollback or forward-only recovery notes, and row-count/checksum or equivalent evidence.
- Do not hide database errors behind warnings or silent fallbacks.
- Stop if production credentials or destructive operations are required.

Tests and CI:

- Do not weaken lint, typecheck, coverage, or test rules to create a green result.
- Do not delete or weaken failing tests.
- Reproduce failures or locate current failing evidence before changing production code.
- Final verification must come from the current run, not stale claims.

Frontend and design:

- Do not rewrite unrelated routes or replace the design system.
- Preserve accessibility and keyboard behavior unless the goal explicitly changes them.
- Use browser, screenshot, or Playwright evidence for user-visible changes when feasible.

Investigation:

- Separate observed evidence from hypotheses.
- Do not patch production code until the root cause is reproduced or strongly evidenced.
- If the goal is read-only, make the non-edit boundary explicit.

Agent workflow:

- Do not claim a goal is complete without auditing the current goal text and state.
- Pause if the goal text, branch state, permission context, or repository rules conflict.
- Preserve AGENTS.md/CLAUDE.md rules through long-running work and compaction.

## Deduplication

- Same goal plus same verification is a duplicate.
- Prefer a more specific goal over a broad goal.
- Prefer concrete verification over subjective judgment.
- Keep broad categories as references, not as excuses to create vague goals.

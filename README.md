# awesome-goal-prompts

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Curated, production-grade `/goal` examples for coding agents.

This repository treats a good goal as an executable task contract: one clear objective, the context the agent must read, hard constraints, deterministic verification, and stop rules. It is not a prompt dump, a jailbreak collection, or a list of vague wishes.

## Start Here

- Browse [200 complete `/goal` examples](prompts/200-goal-examples.md).
- Copy the [full template](templates/full-goal-template.md) for high-risk work.
- Copy the [compact template](templates/compact-goal-template.md) for routine work.
- Read [SOURCES.md](SOURCES.md) before making claims about tool behavior.
- Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding new examples.

## Example

```text
/goal
GOAL:
Complete API Contract Drift Audit for a backend API service: Compare OpenAPI, implementation, and tests to find field or status-code drift.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `npx openapi-diff old.yaml new.yaml && pytest tests/api`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies the contract drift audit.
- The verification command or evidence path succeeds.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx openapi-diff old.yaml new.yaml && pytest tests/api` or the closest repo-local equivalent.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
```

## What Is Included

- [200 complete `/goal` examples](prompts/200-goal-examples.md)
- [Structured JSON data](data/examples.json)
- [Reusable full template](templates/full-goal-template.md)
- [Compact template](templates/compact-goal-template.md)
- [Source notes and caveats](SOURCES.md)
- [Contribution quality rules](CONTRIBUTING.md)

## Categories

The first 200 examples cover:

- `backend-api`, `backend-data`
- `devops-ci`, `devops-runtime`
- `security-appsec`, `security-ops`
- `data-eng`, `data-analytics`
- `ai-evals`, `ai-ops`
- `frontend`, `design`, `mobile`
- `docs`, `product`, `qa`
- `accessibility`, `performance`
- `workflow`

## Quick Template

```text
/goal
GOAL:
Complete one measurable objective.

CONTEXT:
Read the project instructions, current issue, relevant source files, and failing logs before editing.

CONSTRAINTS:
Keep scope tight. Do not weaken tests, hide errors, invent APIs, expose secrets, or perform destructive operations without explicit approval.

DONE WHEN:
The current repository state satisfies the stated behavior and the verification evidence proves it.

VERIFY:
Run the exact tests, build, lint, eval, screenshot, or audit commands required for this goal.

OUTPUT:
Summarize changed files, decisions, verification output, and remaining risk.

STOP RULES:
Pause on missing credentials, production access, product decisions, destructive data changes, or repeated failed fixes.
```

## Why The Examples Are Structured This Way

OpenAI's Codex docs describe `/goal` as useful for long-running work with a verifiable stopping condition. The examples here follow that principle: a goal should define how to continue, how to prove completion, and when to pause.

The core pattern is:

1. One objective.
2. Required context.
3. Hard constraints.
4. Verifiable done condition.
5. Exact verification evidence.
6. Stop rules for uncertainty and risk.

## Non-Goals

- This repository does not claim that `/goal` behaves identically across Codex, Claude Code, Hermes, or other tools.
- This repository does not include undocumented slash-command subcommands.
- This repository does not encourage autonomous production deploys, forced pushes, secret access, or bypassing tests.

## License

MIT

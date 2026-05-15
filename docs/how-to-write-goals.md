# How To Write A Good `/goal`

A good `/goal` is a task contract, not a wish. It tells the agent what goal to reach, what context to inspect, what must not change, how completion will be proven, and when to stop instead of guessing.

Use the catalog for examples, then rewrite the contract with your repository's real files, commands, and constraints.

## The Contract Shape

```text
/goal
GOAL:
<One measurable goal. Do not include unrelated backlog items.>

CONTEXT:
- Repository, product area, or issue:
- Files, docs, logs, screenshots, or plans to read first:
- Current baseline or known failure:
- Project conventions:

CONSTRAINTS:
- Do not change:
- Must preserve:
- Security, data, test, or product constraints:
- Scope boundaries and non-goals:

DONE WHEN:
- <Concrete completion condition 1>
- <Concrete completion condition 2>
- <Concrete completion condition 3>

VERIFY:
- Run:
- Inspect:
- Capture:
- If verification cannot run, stop and explain the exact blocker.

OUTPUT:
- Changed files:
- Key decisions:
- Verification output:
- Remaining risk:
- Follow-up:

STOP RULES:
- Stop on missing secrets, production credentials, destructive data operations, or product decisions.
- Stop after three failed attempts on the same symptom and revisit the root-cause hypothesis.
- Do not mark complete until the current state has been checked against DONE WHEN.
```

## Write It In Six Moves

### 1. Make The Goal Singular

Bad:

```text
/goal fix the app, clean up the code, improve performance, and make no mistakes
```

Good:

```text
/goal
GOAL:
Fix the intermittent login white-screen bug and keep the auth test suite green.
```

One goal can be large, but it still needs one finish line.

### 2. Point At The Real Context

The agent should not guess where the truth lives. Name the issue, files, logs, failing command, design doc, or branch state that should be read first.

```text
CONTEXT:
- Read `AGENTS.md`, `docs/auth-flow.md`, and issue #184 before editing.
- Start from the failing output of `npm test -- auth`.
- The bug appears after OAuth callback when a stale session cookie is present.
```

### 3. Add Hard Constraints

Constraints are where you kill scope creep. Include API compatibility, forbidden files, data safety, security rules, and test integrity.

```text
CONSTRAINTS:
- Do not change public API response shapes.
- Do not delete or weaken existing tests.
- Do not add new auth dependencies.
- Keep changes scoped to auth callback handling and tests.
```

### 4. Define Completion Mechanically

`DONE WHEN` should be auditable without trusting the agent's confidence.

```text
DONE WHEN:
- The white-screen reproduction no longer fails.
- Existing auth tests pass.
- A regression test covers the stale-cookie callback case.
- The final diff has no unrelated formatting churn.
```

### 5. Require Fresh Verification

Use commands, reports, screenshots, logs, or generated artifacts. If the exact command may not exist in every repo, require the closest repo-local equivalent and an explicit blocker if it cannot run.

```text
VERIFY:
- Run `npm test -- auth`.
- Run `npm run lint`.
- Capture the before/after reproduction result.
- If local OAuth credentials are missing, stop and report the missing variable name.
```

### 6. Give The Agent An Escape Hatch

Long-running goals need a safe incomplete state. This is especially important for production access, destructive data work, missing secrets, unclear product decisions, or repeated failed fixes.

```text
STOP RULES:
- Stop if production credentials, destructive database changes, or stakeholder decisions are required.
- Stop after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- If part of the goal is impossible locally, mark that part incomplete with evidence and continue only on independent safe work.
```

## Reusable Patterns Worth Keeping

These patterns are starting points, not ready-to-run goals. Keep the useful shape, then bind it to your repository's current files, commands, constraints, and verification evidence.

| Pattern | Use it when | Catalog entry |
| --- | --- | --- |
| Meta goal writer | The task is vague and the repo has useful history/docs. First ask the agent to inspect context and draft the `/goal`. | `x-meta-goal-prompt-generator` |
| Tests and lint loop | The desired goal is purely mechanical: all tests pass, lint is clean, typecheck is clean. | `x-tests-lint-completion` |
| Escape hatch | A long-running goal may contain impossible or blocked subtasks. | `x-goal-escape-hatch` |
| AGENTS/CLAUDE rules with goal | Repo-specific rules must survive a long session or compaction. | `x-agentsmd-goal-workflow` |
| Plan then goal | The work needs design first, then execution against a stable plan. | `x-plan-then-goal-execution` |
| Measurable proof and limits | The goal is at risk of becoming vague todo-list work. | `x-measurable-goal-structure` |

## Copyable Examples

### Quick Fix Loop

```text
/goal auth tests pass and lint is clean

Read first: `AGENTS.md`, failing auth test output, and auth route handlers.
Constraints: Do not change public API shapes. Do not delete or weaken tests.
Done when: auth tests pass, lint passes, and the fix includes a regression test for the reproduced bug.
Verify with: `npm test -- auth` and `npm run lint`.
Stop if: credentials, production access, or a product decision is required.
Final output: changed files, root cause, verification output, remaining risk.
```

### Refactor With Behavior Lock

```text
/goal
GOAL:
Split `UserService` into smaller modules while preserving public behavior.

CONTEXT:
- Read `AGENTS.md`, `src/services/UserService.ts`, current callers, and existing service tests.
- Establish a baseline with `npm test -- UserService`.

CONSTRAINTS:
- Do not change exported method names, request/response shapes, or error semantics.
- Do not introduce a new framework or dependency.
- Do not combine unrelated cleanup with this refactor.

DONE WHEN:
- `UserService` responsibilities are split into focused modules.
- Existing callers compile without API changes.
- Existing service tests and a behavior characterization test pass.
- The final diff is scoped to the service and tests.

VERIFY:
- Run `npm test -- UserService`.
- Run `npx tsc --noEmit`.
- Capture any behavior differences found during characterization.

OUTPUT:
- Changed files, module split rationale, verification output, remaining risk.

STOP RULES:
- Stop if preserving behavior conflicts with the requested split.
- Stop after three failed attempts on the same failing test and revisit the hypothesis.
```

### Research Before Writing A Goal

```text
Read this session and repository, then write the best `/goal` prompt for the task we are trying to achieve.

Requirements:
- Inspect current docs, issue context, failing logs, and relevant source files before drafting.
- Separate confirmed facts from assumptions.
- Ask at most three concrete questions only if the missing answer changes the goal contract.
- Output a complete `/goal` with GOAL, CONTEXT, CONSTRAINTS, DONE WHEN, VERIFY, OUTPUT, and STOP RULES.
- Do not edit files yet.
```

## Review Checklist

Before running a goal, check:

- The goal has exactly one primary goal.
- The context names real files, issues, logs, docs, or commands.
- The constraints say what must not change.
- `DONE WHEN` can be audited from repository state or artifacts.
- `VERIFY` uses fresh commands or evidence from this run.
- Stop rules cover secrets, production access, destructive operations, unclear decisions, and repeated failed fixes.
- The final output asks for changed files, verification, decisions, risks, and next action.

## What Not To Add

Avoid goal text that asks for confidence instead of proof:

- `make no mistakes`
- `fix everything`
- `do whatever it takes`
- `improve the codebase`
- `keep going until perfect`
- `use your best judgment` without constraints

Replace those with a measurable end state, real verification, and explicit stop rules.

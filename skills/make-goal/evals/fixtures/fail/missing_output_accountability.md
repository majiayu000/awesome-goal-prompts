/goal
GOAL:
Fix the failing auth tests while preserving the existing auth API behavior.

CONTEXT:
- Read `AGENTS.md`, `src/auth/routes.ts`, `tests/auth.test.ts`, and the current `npm test -- auth` failure output.

CONSTRAINTS:
- Keep the scope limited to auth route behavior and related tests.
- Do not change public API response shapes.
- Verification integrity: do not weaken or bypass tests, assertions, lint, typecheck, validation, generated-output checks, screenshots, or external blockers to make the goal pass; fix the root cause or report the blocker.

DONE WHEN:
- `npm test -- auth` passes after a root-cause fix.
- `npm run lint` passes without unrelated formatting churn.

VERIFY:
- Run `npm test -- auth`.
- Run `npm run lint`.
- If verification cannot run, stop and report the exact blocker.

OUTPUT:
- Summary of what changed.

STOP RULES:
- Stop on secrets, production credentials, destructive operations, or repository settings changes requiring owner approval.
- Stop after three failed attempts on the same auth failure and revisit the root-cause hypothesis.
- Do not mark complete until the current state has been checked against DONE WHEN.

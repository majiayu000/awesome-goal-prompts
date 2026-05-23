/goal
GOAL:
Complete the smallest PR-ready launch-readiness pass for `awesome-goal-prompts` without treating GitHub Trending placement as a guaranteed outcome.

CONTEXT:
- Read `AGENTS.md`, `README.md`, `docs/index.html`, `docs/app.js`, and issue #2 before editing.
- Establish the current branch state with `git status --short --branch`.

CONSTRAINTS:
- Keep scope limited to launch readiness; do not add catalog entries or redesign unrelated UI.
- If the work expands into multiple independent PR-sized changes, keep this goal to the smallest launch-readiness pass and list follow-up PRs instead of expanding scope.
- Treat GitHub Trending as an external outcome, not guaranteed.
- Verification integrity: do not weaken or bypass tests, assertions, lint, typecheck, validation, generated-output checks, screenshots, or external blockers to make the goal pass; fix the root cause or report the blocker.

DONE WHEN:
- README and Pages first viewport clearly describe the project, credible counts, and how to try a goal.
- Repository settings that require owner approval are documented as manual steps with exact steps.

VERIFY:
- Run `python3 scripts/validate_data.py`.
- Run `python3 scripts/evaluate_search.py`.
- Capture desktop and mobile screenshots, or report the exact blocker if browser evidence cannot run.

OUTPUT:
- Changed files, key decisions, verification output, manual settings blockers, remaining risk, and follow-up PRs.

STOP RULES:
- Stop on secrets, production credentials, destructive operations, or repository settings changes requiring owner approval.
- Stop after three failed attempts on the same symptom and revisit the root-cause hypothesis.
- Do not mark complete until the current state has been checked against DONE WHEN.

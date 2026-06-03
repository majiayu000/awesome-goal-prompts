/goal
GOAL:
Produce a source-backed 5000-star growth plan for `awesome-goal-prompts` that defines the smallest credible launch sequence, first PR scope, metrics baseline, and distribution checklist without claiming stars, GitHub Trending placement, or awesome-list acceptance are guaranteed.

CONTEXT:
- Read `README.md`, `docs/index.html`, `docs/catalog-health.md`, `SOURCES.md`, `CONTRIBUTING.md`, and issue #2.
- Inspect current GitHub metadata with `gh repo view majiayu000/awesome-goal-prompts --json description,stargazerCount,forkCount,repositoryTopics,homepageUrl,url,createdAt,pushedAt`.
- Inspect GitHub traffic with `gh api repos/majiayu000/awesome-goal-prompts/traffic/views`, `/traffic/clones`, `/traffic/popular/referrers`, and `/traffic/popular/paths`.
- Run `npx --yes awesome-lint` and group failures by blocker type.

CONSTRAINTS:
- Do not edit repository files in this pass; output a report/plan only.
- Treat 5000 stars, GitHub Trending, and awesome-list acceptance as external outcome targets, not guaranteed done conditions.
- If this expands into multiple independent PR-sized changes, keep the goal to the smallest growth/readiness plan and list follow-up PRs instead of expanding scope.
- Do not recommend spam, fake stars, bought traffic, misleading badges, or AI-generated PR submission text.
- Verification integrity: do not weaken or bypass tests, assertions, lint, typecheck, validation, generated-output checks, screenshots, awesome-lint failures, or external blockers to make the goal pass; fix the root cause or report the blocker.

DONE WHEN:
- The report states the current baseline: stars, forks, topics, traffic, clone/view ratio, top referrers, top paths, open marketing issue, and validation status.
- The report diagnoses whether the repo is currently ready to pursue 5000 stars and identifies the top 3 blockers, ordered by impact and backed by evidence.
- The report defines a 3-phase path: trust/readiness, launch/distribution, retention/community.
- The report gives a first PR scope that can be executed independently and verified.

VERIFY:
- Capture fresh `gh repo view` output for repository metadata.
- Capture fresh GitHub traffic API output or exact permission blockers.
- Capture fresh `npx --yes awesome-lint` output summarized by blocker bucket.
- Run `python3 scripts/validate_data.py`, `python3 scripts/validate_metadata.py`, and `python3 scripts/evaluate_search.py`.

OUTPUT:
- Concise growth plan with baseline evidence, blockers, launch sequence, first PR scope, distribution checklist, metric cadence, manual platform blockers, and remaining risks.
- Changed files: none.
- Explicit decision on whether issue #2 is ready now, blocked until 2026-06-13, or blocked by awesome-lint/category fit.

STOP RULES:
- Stop on secrets, production credentials, destructive operations, force push, direct main push, unavailable traffic permissions, or repository settings changes requiring owner approval.
- Stop if awesome-list requirements conflict with the repository's real product shape and document the mismatch instead of forcing compliance.
- Stop if the plan would require fake engagement, paid stars, misleading claims, automated social posting, or external submission without approval.
- Stop after three failed attempts to satisfy the same lint/submission blocker and revisit whether awesome-list submission is the right channel.

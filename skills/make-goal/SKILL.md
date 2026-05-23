---
name: make-goal
description: Create, tighten, or review runnable /goal contracts for coding agents such as Codex, Claude Code, Cursor, and similar agent tools. Use when the user asks to write, make, generate, improve, productize, or critique a goal prompt, rescue contract, GOAL.md-style task, done-when contract, verification prompt, stop-rule prompt, or when they want to convert a vague engineering request, issue, PR, CI failure, bug report, plan, or backlog item into one measurable coding-agent task. Prefer source-backed goal patterns when available, use seed patterns only as raw reusable shapes, and output the goal contract or review rather than implementing the underlying code task.
---

# Make Goal

Use this skill to turn engineering intent into a runnable task contract for an agent. The output is a `/goal` contract, a review of an existing goal, or a catalog-entry draft when explicitly requested. Do not implement the underlying software task unless the user separately asks for execution.

A good goal is not a wish. It is a contract with one measurable objective, real context to inspect, hard constraints, auditable completion, fresh verification, and stop rules for uncertainty or risk.

## Operating Modes

- `create`: The user gives a task, issue, failure, plan, or vague request and wants a new `/goal`.
- `tighten`: The user gives an existing draft and wants it made safer or more executable.
- `review`: The user asks whether a goal is good; lead with defects, missing evidence, and risk.
- `catalog`: The user wants to add a goal pattern to an awesome-goal-prompts style catalog; read `references/catalog-contribution.md`.

If the user asks for a goal and also asks you to execute it, first produce the goal contract. Execute only after the user confirms or separately asks for execution.

## Read Context First

Before drafting, inspect available context instead of guessing:

1. Read the user's latest request and any pasted error, issue, plan, or draft.
2. If working in a repository, read the nearest `AGENTS.md` or `CLAUDE.md`, relevant issue/PLAN/docs/logs, and the files or commands named by the user.
3. If the task references CI, tests, browser behavior, screenshots, migrations, production, data, auth, or security, include the concrete evidence source in `CONTEXT`.
4. Separate confirmed facts from assumptions. Do not present assumptions as facts.

Ask at most three concise questions only when missing information changes the contract. The highest-value questions are:

- What is the one finish line for this goal?
- What real files, issue, logs, screenshots, failing command, or baseline must be read first?
- What must not change, and what command/report/screenshot proves completion?

If the request is only "make this project better", "fix everything", or similarly broad, use `clarify_first`: ask for the primary goal, context, and done-when condition instead of drafting a fake comprehensive goal.

## Choose The Shape

Use the full shape by default. Use compact only for routine, low-risk work with clear context and a simple verification command.

Use full when any of these are true:

- The task is high-risk, multi-step, long-running, cross-module, migration, security, auth, data, deployment, production, or user-visible frontend work.
- The user mentions plan mode, AGENTS/CLAUDE rules, screenshots, browser smoke tests, CI repair, database changes, or PR readiness.
- The constraints are unclear or the task could drift into unrelated cleanup.

Read `references/contract-shape.md` for the full and compact templates.

## Pattern Selection

Use source-backed patterns first when a close match exists. They are trusted shapes backed by public examples, not text to copy verbatim.

Use seed patterns only as raw reusable shapes when no source-backed pattern fits. Never describe a seed as collected from X, GitHub, docs, or a named author.

Read:

- `references/pattern-selection.md` when choosing between source-backed and seed patterns.
- `references/source-backed-index.md` for common rescue contracts and goal-workflow patterns.
- `references/seed-patterns-index.md` only when the source-backed index lacks a close shape.

## Optional Lint

When reviewing generated output, run the bundled linter if a local shell is available:

```bash
python3 scripts/lint_goal.py <goal-or-response.md>
```

Use `--profile compact`, `--profile data-migration`, `--profile security-xss`, `--profile read-only`, or `--profile clarify` when the task type is known. Use `--json` when another script will consume the result.

## Required Contract

Every full goal must contain exactly these sections:

```text
/goal
GOAL:
<One measurable goal.>

CONTEXT:
- <Files, docs, issues, logs, screenshots, commands, baseline, and conventions to inspect first.>

CONSTRAINTS:
- <What must not change; what must be preserved; safety, data, security, test, and scope boundaries.>

DONE WHEN:
- <Mechanically auditable completion condition.>

VERIFY:
- <Fresh command, report, screenshot, artifact, manual check, or explicit blocker.>

OUTPUT:
- <Changed files if execution occurs, key decisions, verification output, remaining risk, follow-up.>

STOP RULES:
- <When to pause instead of guessing.>
```

Compact form:

```text
/goal <single measurable goal>

Read first: <files/issues/logs>.
Constraints: <what must not change; what must be preserved>.
Done when: <mechanically checkable end state>.
Verify with: <commands/reports/screenshots/evidence>.
Stop if: <missing input, destructive operation, repeated failed fixes, production access, or unclear product decision>.
Final output: <changed files, verification, risks, next action>.
```

## Safety Defaults

Include these constraints unless they conflict with a more specific user requirement:

- Keep scope limited to this goal; do not add unrelated cleanup or "easy improvements".
- Do not weaken tests, delete assertions, bypass lint/typecheck, or mask errors to make verification pass.
- Respect repository instructions and existing patterns.
- Stop if secrets, production access, destructive data operations, missing credentials, or product decisions are required.
- Stop after three failed attempts on the same symptom and revisit the root-cause hypothesis.
- Do not mark complete until the current state has been checked against `DONE WHEN`.

For full goals that may lead to file edits, include the scope, test-integrity, and repository-instruction defaults as actual `CONSTRAINTS` text, not only as internal guidance.

Add category-specific constraints when relevant:

- Security: preserve auth/authz, validate inputs, avoid unsafe HTML sinks, string-built SQL, shell string execution, and secret exposure.
- Data and migrations: write the literal term `dry-run` into the goal. Require a `dry-run` when the stack supports it; if true dry-run is unavailable, say so explicitly and require a disposable-environment rehearsal instead. Also require rollback or forward-only recovery notes, row-count/checksum or equivalent integrity evidence, and no silent data loss.
- Frontend: preserve accessibility, keyboard behavior, existing design system, and include browser or screenshot evidence for user-visible changes.
- CI/testing: reproduce or locate the current failure, fix production or fixture causes before changing assertions, and require fresh command output.
- Investigation: keep changes read-only unless the goal explicitly asks for a fix; separate evidence from hypotheses.

Read `references/quality-bar.md` before finalizing high-risk goals.

## Output Rules

When creating or tightening a goal:

1. Output the final contract in one fenced `text` block.
2. After the block, add a short note only if needed: assumptions made, missing context, or why full/compact was chosen.
3. Do not include lengthy internal analysis or catalog trivia.

When reviewing a goal:

1. Lead with findings ordered by severity.
2. Cite missing sections, vague done conditions, unverifiable `VERIFY`, unsafe constraints, or weak stop rules.
3. Provide a revised contract if the user asked for one.

When writing a catalog entry:

1. Read `references/catalog-contribution.md`.
2. Distinguish `source-backed` from `seed`.
3. Do not invent source metadata.

## Final Self-Check

Before responding, verify:

- There is one primary goal, not a backlog.
- `CONTEXT` names real files, issues, logs, docs, commands, screenshots, or baselines when available.
- `CONSTRAINTS` say what must not change.
- `DONE WHEN` is mechanically checkable or evidence-based.
- `VERIFY` requires fresh evidence from the actual run or an exact blocker.
- `STOP RULES` cover secrets, production access, destructive operations, unclear decisions, and repeated failed fixes.
- Seed patterns are not presented as source-backed evidence.

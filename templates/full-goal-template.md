# Full Goal Template

```text
/goal
GOAL:
<One clear, measurable outcome. Do not include unrelated backlog items.>

CONTEXT:
- Repository or product area:
- Files, docs, issues, logs, screenshots, or plans to read first:
- Current known failure, gap, or baseline:
- Important project conventions:

CONSTRAINTS:
- Do not change:
- Must preserve:
- Security/data/test constraints:
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

/goal
GOAL:
Investigate why active subscriptions show an empty billing state.

CONTEXT:
- Read `src/billing/state.ts`, `tests/billing_state.test.ts`, and the failing screenshot.

CONSTRAINTS:
- This is read-only. Do not edit files.

DONE WHEN:
- The root cause report includes evidence.

VERIFY:
- Inspect the named files and capture the root cause evidence.

OUTPUT:
- Root cause, evidence, and a patch the code recommendation.

STOP RULES:
- Stop on secrets, production credentials, or destructive operations.
- Stop after three failed attempts on the same symptom.

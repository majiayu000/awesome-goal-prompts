/goal
GOAL:
Add a unique index to `users.email` in the production database.

CONTEXT:
- Read `migrations/`, `db/schema.sql`, and the current duplicate email report.

CONSTRAINTS:
- Do not perform destructive production database operations.
- Include rollback notes and row count evidence.
- Do not weaken tests.

DONE WHEN:
- The unique index migration is ready for review and duplicate rows are accounted for.

VERIFY:
- Run `python3 scripts/check_migrations.py`.
- Capture row count and duplicate email reports.

OUTPUT:
- Changed files, migration notes, rollback notes, and verification output.

STOP RULES:
- Stop on production credentials, destructive operations, or missing database access.
- Stop after three failed attempts on the same migration failure.

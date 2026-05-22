# Seed Patterns Index

Use seed patterns only as raw reusable shapes when no close source-backed pattern fits. Do not cite them as external evidence.

## Category Taxonomy

- `backend-api`: routes, OpenAPI specs, handlers, middleware, API tests.
- `backend-data`: schema files, migrations, models, repositories, data tests.
- `devops-ci`: workflow files, build scripts, package manifests, CI logs.
- `devops-runtime`: Dockerfiles, deployment manifests, runtime config, health checks.
- `security-appsec`: auth, input handling, rendering, upload, boundary tests.
- `security-ops`: workflow permissions, cloud IAM, release artifacts, audit evidence.
- `data-eng`: ETL jobs, schemas, source contracts, transformations, data quality tests.
- `data-analytics`: metric SQL, event schemas, dashboards, validation queries.
- `ai-evals`: eval datasets, rubrics, model outputs, judge code, regression reports.
- `ai-ops`: prompts, retrieval, routing, tracing, cost logs.
- `frontend`: routes, components, state, stories, tests, screenshots.
- `design`: design tokens, component variants, layouts, visual states, screenshots.
- `mobile`: mobile routes, forms, gestures, device matrix, viewport tests.
- `docs`: README, docs, examples, runbooks, lint config.
- `product`: PRDs, analytics events, permission models, acceptance criteria.
- `qa`: test suites, fixtures, bug templates, release checklists.
- `accessibility`: interactive elements, semantics, focus management, a11y reports.
- `performance`: Lighthouse reports, bundles, traces, critical routes.
- `workflow`: goal text, progress logs, branch state, verification artifacts.
- `migration`: legacy code, target implementation, compatibility tests, snapshots.
- `prototype`: PLAN.md, milestones, app code, tests, browser checks.
- `prompt-optimization`: prompt files, eval cases, scoring reports, failures.
- `testing`: tests, lint config, CI logs, coverage reports, failing output.
- `investigation`: logs, traces, reproduction notes, source paths, final report.
- `cli`: CLI entrypoints, argument parsing, filesystem behavior, fixtures.
- `refactor`: target module, call sites, public API, tests, compatibility notes.

## High-Value Seed Shapes

Backend API:

- API Contract Drift Audit: compare OpenAPI, implementation, and tests.
- Request Validation Boundary: move validation to the API boundary and reject unknown fields.
- Resource-Level Authorization: prevent cross-resource access.
- Idempotent Create Endpoint: add idempotency keys and replay-safe semantics.
- API Error Taxonomy: unify HTTP status, machine codes, user messages, and logs.

Backend data:

- Database Migration Safety: review rollback, online execution, and lock risk.
- Transaction Boundary Audit: find missing or oversized transactions.
- Cache Invalidation Map: map write paths to cache keys and stale reads.
- Schema Drift Detector: compare models, migrations, and live schema.
- Read Replica Lag Guard: prevent stale read-after-write behavior.

Security:

- SQL Injection Audit: replace string-built SQL with parameterized queries and tests.
- Command Injection Audit: replace shell strings with argument arrays and validation.
- SSRF Defense Review: add URL allowlists and DNS/IP checks.
- XSS Output Encoding: audit rendering sinks and missing encoding.
- IDOR Audit: verify ownership or scope checks for direct object access.

Frontend and design:

- Form Validation UX: align client/server validation and error display.
- Empty State Behavior: ensure no-data states are honest and recoverable.
- Accessibility Color Contrast: verify contrast and state visibility.
- Keyboard Navigation Repair: preserve focus order and shortcuts.
- Component API Consistency: align props, states, stories, and tests.

Testing and CI:

- CI Flaky Test Triage: separate flakes from real failures.
- Dependency Update Gate: require tests, licenses, and vulnerabilities checks.
- Monorepo Affected Tests: run affected tests without missing contracts.
- Coverage Gap Closure: add tests for critical uncovered branches.

AI/evals:

- LLM Golden Set Build: build evals from real failures and frequent tasks.
- LLM Regression Gate: compare old and new model or prompt outputs.
- Judge Calibration: measure judge agreement against human labels.
- Tool Use Eval: evaluate tool selection, order, and validation.
- Hallucination Probe Suite: add negative cases for nonexistent files, fields, APIs, and sources.

Docs and maintenance:

- Docs Quickstart: verify install, run, test, and first-success path.
- Public API Docs Coverage: add examples for public functions.
- Repo Maintenance Audit: find dead code, unused dependencies, stale files.
- Release Notes From Diff: produce user-facing notes from commits and PR labels.

Use a seed by copying its task shape into the full contract and binding it to the user's actual context and verification.

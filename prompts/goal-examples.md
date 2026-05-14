# Goal Prompt Examples

Each example is a complete `/goal` task contract. Replace placeholder commands, paths, and project names with your repository's real values before running.

These examples intentionally use only the documented `/goal <objective>` form. They do not rely on unofficial subcommands.

## Index

### backend-api
- [API Contract Drift Audit](#api-contract-drift-audit) - Compare OpenAPI, implementation, and tests to find field or status-code drift.
- [Idempotent Create Endpoint](#idempotent-create-endpoint) - Add idempotency keys and replay-safe semantics to a create endpoint.
- [API Error Taxonomy](#api-error-taxonomy) - Unify HTTP status codes, machine error codes, user messages, and logs.
- [Pagination Consistency](#pagination-consistency) - Fix cursor or offset pagination so rows are not skipped, duplicated, or reordered.
- [Request Validation Boundary](#request-validation-boundary) - Move input validation to the API boundary and reject unknown fields.
- [API Rate Limit Policy](#api-rate-limit-policy) - Implement rate limit behavior, headers, and over-limit responses for critical routes.
- [Webhook Retry Contract](#webhook-retry-contract) - Define webhook signature verification, retry, dedupe, and failure observability.
- [Backward-Compatible Response](#backward-compatible-response) - Add response fields without breaking old clients and document removal paths.
- [gRPC Timeout Propagation](#grpc-timeout-propagation) - Propagate deadlines across service calls and cancel work correctly.
- [Async Job State Machine](#async-job-state-machine) - Make async job transitions explicit and tested across pending/running/succeeded/failed/canceled.
- [Resource-Level Authorization](#authz-resource-scope) - Prevent logged-in users from accessing resources they do not own.
- [API Versioning Plan](#api-versioning-plan) - Create a v1/v2 coexistence plan with deprecation headers and migration tests.

### backend-data
- [Database Migration Safety](#db-migration-safety) - Review a migration for rollback, online execution, and lock risk.
- [Transaction Boundary Audit](#transaction-boundary-audit) - Find missing or oversized transactions in multi-table write paths.
- [Cache Invalidation Map](#cache-invalidation-map) - Map write paths to cache keys and fix stale reads.
- [N+1 Query Fix](#n-plus-one-query-fix) - Reduce list endpoint query count with batching or preloading.
- [Optimistic Locking Rollout](#optimistic-locking-rollout) - Add version checks and conflict responses for concurrent edits.
- [Soft Delete Integrity](#soft-delete-integrity) - Make queries, unique indexes, and restore flows respect soft deletion.
- [Index Regression Check](#db-index-regression) - Add or adjust indexes and prove read gains do not create unacceptable write cost.
- [Outbox Reliable Events](#outbox-pattern-adoption) - Use an outbox table to prevent lost events after successful database commits.
- [Read Replica Lag Guard](#read-replica-lag-guard) - Prevent write-after-read paths from hitting stale replicas.
- [Schema Drift Detector](#schema-drift-detector) - Compare ORM models, migrations, and the live database schema.

### devops-ci
- [CI Flaky Test Triage](#ci-flaky-test-triage) - Identify flaky tests, separate real failures, and fix unstable waits or fixtures.
- [Build Cache Correctness](#build-cache-correctness) - Check whether CI cache keys cause stale dependencies or cross-branch pollution.
- [Dependency Update Gate](#dependency-update-gate) - Add dependency upgrade checks for tests, licenses, and vulnerabilities.
- [Monorepo Affected Tests](#monorepo-affected-tests) - Run only affected tests without missing cross-package contracts.
- [Release Notes From Diff](#release-note-from-diff) - Generate user-facing release notes from commits, PR labels, and breaking changes.
- [Artifact Provenance](#artifact-provenance) - Trace a package or image back to the commit and workflow that produced it.
- [CI Permission Minimization](#ci-permission-minimize) - Tighten GitHub Actions token permissions without breaking workflows.
- [Branch Protection Audit](#branch-protection-audit) - Audit required checks, reviews, linear history, and admin bypasses.
- [Release Rollback Drill](#release-rollback-drill) - Create and test a rollback path for the latest release.
- [Semantic Version Check](#semantic-version-check) - Infer the correct semver bump from API, behavior, and changelog diffs.

### devops-runtime
- [Docker Image Slimming](#docker-image-slimming) - Reduce image size while keeping runtime dependencies and security scans green.
- [Kubernetes Probe Repair](#k8s-readiness-liveness) - Separate startup, readiness, and liveness probes to avoid bad restarts.
- [Terraform Plan Review](#terraform-plan-review) - Review infrastructure changes for deletes, replacements, and permission expansion.
- [Helm Values Drift](#helm-values-drift) - Compare environment values to find hidden staging/prod differences.
- [Autoscaling Thresholds](#autoscaling-thresholds) - Tune HPA or worker scaling thresholds against real load and queue depth.
- [Runtime Config Validation](#runtime-config-validation) - Fail startup on missing or invalid environment and config values.
- [Zero-Downtime Migration](#zero-downtime-migration) - Plan and verify expand-migrate-contract deployment steps.
- [Observability Minimum](#observability-minimum) - Add logs, metrics, traces, and alerts for a service's critical paths.
- [Incident Runbook Gap](#incident-runbook-gap) - Turn a recent incident timeline into missing runbook and alert updates.
- [Queue Backpressure](#queue-backpressure) - Protect databases and external APIs when worker queues build up.

### security-appsec
- [SQL Injection Audit](#sql-injection-audit) - Replace SQL string concatenation with parameterized queries and tests.
- [Command Injection Audit](#command-injection-audit) - Replace shell string execution with argument arrays and validation.
- [SSRF Defense Review](#ssrf-defense-review) - Add URL allowlists and DNS/IP checks for fetch or callback features.
- [XSS Output Encoding](#xss-output-encoding) - Audit HTML and Markdown rendering for unsafe sinks and missing encoding.
- [CSRF Sensitive Action](#csrf-sensitive-action) - Protect cookie-authenticated writes from cross-site requests.
- [Auth Bypass Route Map](#auth-bypass-route-map) - Enumerate routes and verify unauthenticated and unauthorized behavior.
- [File Upload Security](#file-upload-security) - Validate MIME, extension, size, scanning, and storage isolation.
- [Tenant Isolation Test](#tenant-isolation-test) - Verify tenant IDs are enforced in queries, caches, and background jobs.
- [Replay Attack Defense](#replay-attack-defense) - Add nonce, timestamp, and expiration checks to signed requests.
- [IDOR Audit](#insecure-direct-object-ref) - Verify direct object ID access always checks ownership or scope.

### security-ops
- [Secret Scan Baseline](#secret-scan-baseline) - Add secret scanning and triage historical findings safely.
- [IAM Least Privilege](#iam-least-privilege) - Reduce cloud permissions to observed API usage and documented needs.
- [GitHub Actions Supply Chain](#github-actions-supply-chain) - Pin third-party actions and review workflow permissions.
- [Container Vulnerability Triage](#container-vuln-triage) - Prioritize image CVEs by exploitability and runtime exposure.
- [Audit Log Coverage](#audit-log-coverage) - Add audit logs for login, permission changes, and sensitive data access.
- [Secret Rotation Drill](#secret-rotation-drill) - Verify rotating a key does not interrupt the service.
- [Dependency Confusion Guard](#dependency-confusion-guard) - Lock private package scopes and registries to prevent wrong-source installs.
- [SBOM Generation](#sbom-generation) - Generate an SBOM and attach it to release artifacts.
- [Production Access Review](#prod-access-review) - Inventory production access, approval paths, and audit evidence.
- [Backup Restore Security](#backup-restore-security) - Verify encrypted backups and a restricted restore path.
- [NPM Audit Clean Remediation](#explainx-npm-audit-clean) - Patch npm audit vulnerabilities without breaking tests or public APIs. Source-backed.

### data-eng
- [ETL Contract Tests](#etl-contract-tests) - Add schema and sample-data contracts between source and target tables.
- [Data Quality Rules](#data-quality-rules) - Define null, uniqueness, range, and reference checks for key datasets.
- [Backfill Safety Plan](#backfill-safety-plan) - Design a sharded, resumable, verifiable historical backfill.
- [Incremental Load Watermark](#incremental-load-watermark) - Fix missing or duplicate rows in incremental sync logic.
- [Late-Arriving Data](#late-arriving-data) - Handle delayed events and metric corrections safely.
- [Data Lineage Map](#data-lineage-map) - Map critical report fields from source to consumers.
- [PII Classification](#pii-classification) - Classify sensitive fields and document masking rules.
- [Data Retention Enforcement](#data-retention-enforcement) - Verify expiration, archival, deletion, and audit behavior.
- [Warehouse Cost Audit](#warehouse-cost-audit) - Find expensive queries, duplicate tables, and unused scheduled jobs.
- [Stream Processing Lag](#stream-processing-lag) - Diagnose Kafka/Flink/Spark lag and checkpoint bottlenecks.

### data-analytics
- [Metric Definition Lock](#metric-definition-lock) - Turn core metric definitions into tested SQL or semantic-layer checks.
- [Dashboard Trust Audit](#dashboard-trust-audit) - Check filters, timezone, refresh cadence, permissions, and source reconciliation.
- [A/B Test SRM Check](#ab-test-srm-check) - Detect sample ratio mismatch in experiment assignment.
- [Funnel Dropoff Diagnosis](#funnel-dropoff-diagnosis) - Validate funnel events, step counts, and latency before interpreting dropoff.
- [Cohort Retention Query](#cohort-retention-query) - Create reusable retention SQL with hand-checked small samples.
- [Revenue Reconciliation](#revenue-reconciliation) - Reconcile payments, orders, refunds, and finance definitions.
- [Event Taxonomy Cleanup](#event-taxonomy-cleanup) - Deduplicate event names, properties, and version changes.
- [Anomaly Detection Baseline](#anomaly-detection-baseline) - Backtest alert thresholds against historical metrics.
- [Attribution Window Review](#attribution-window-review) - Verify campaign attribution windows and dedupe rules.
- [Self-Serve Data Contract](#self-serve-data-contract) - Define trusted datasets and usage limits for business users.

### ai-evals
- [LLM Golden Set Build](#llm-golden-set-build) - Build an eval set from real failures and frequent tasks.
- [LLM Regression Gate](#llm-regression-gate) - Compare old and new model or prompt outputs in PRs.
- [Judge Calibration](#judge-calibration) - Measure LLM judge agreement against human labels.
- [Hallucination Probe Suite](#hallucination-probe-suite) - Add negative cases for nonexistent files, fields, APIs, and sources.
- [RAG Answer Faithfulness](#rag-answer-faithfulness) - Check that answers are supported by retrieved evidence.
- [Tool Use Eval](#tool-use-eval) - Evaluate whether an agent selects, orders, and validates tools correctly.
- [Prompt Injection Red Team](#adversarial-prompt-redteam) - Test prompt leakage, unauthorized tools, and instruction override attempts.
- [Eval Data Dedup](#eval-data-dedup) - Remove duplicates, leakage, and near-identical eval samples.
- [Cost Quality Frontier](#cost-quality-frontier) - Compare models by quality, latency, and cost to choose routing tiers.
- [Rubric-Driven Eval](#rubric-driven-eval) - Replace binary scores with multi-dimensional rubrics for complex tasks.

### ai-ops
- [Prompt Version Registry](#prompt-version-registry) - Bind prompt versions to eval results and deployment history.
- [RAG Chunking Experiment](#rag-chunking-experiment) - Compare chunk size, overlap, and metadata on retrieval and answer quality.
- [Vector Index Refresh](#vector-index-refresh) - Verify document updates are indexed completely and can be rolled back.
- [Model Routing Policy](#model-routing-policy) - Route by risk, cost, latency, and quality evidence.
- [LLM Timeout Budget](#llm-timeout-budget) - Define timeout, retry, fallback, and user-visible error behavior.
- [Token Cost Attribution](#token-cost-attribution) - Attribute model costs by user, feature, model, and request ID.
- [RAG Prompt Injection Filter](#prompt-injection-filter) - Detect and isolate malicious instructions in retrieved documents.
- [AI Output Schema Guard](#ai-output-schema-guard) - Validate structured AI output and fail or retry safely.
- [Human Review Threshold](#human-review-threshold) - Escalate high-risk AI outputs based on confidence and policy rules.
- [AI Observability Traces](#ai-observability-traces) - Trace prompts, retrieval, tools, models, scores, and request IDs.

### frontend
- [Empty State System](#frontend-empty-states) - Design real empty states for lists, search, permissions, and first use.
- [Error Boundary Experience](#frontend-error-boundary) - Add recoverable page and component fallback UI for crashes.
- [Loading Skeletons](#frontend-loading-skeletons) - Replace layout-shifting spinners with stable skeleton states.
- [Form Validation](#frontend-form-validation) - Cover inline, submit, server error, and dirty-state validation.
- [Data Table Density](#frontend-table-density) - Improve columns, filters, sorting, pagination, and bulk actions.
- [Command Palette](#frontend-command-palette) - Add a keyboard-first entry point for high-frequency actions.
- [Navigation Map](#frontend-navigation-map) - Clarify primary navigation, breadcrumbs, and detail-page return paths.
- [State Recovery](#frontend-state-recovery) - Restore filters and context after refresh, back, and deep links.
- [Permission State UI](#frontend-permission-ui) - Separate unauthenticated, unauthorized, and missing-resource states.
- [Bulk Actions](#frontend-bulk-actions) - Handle selection, confirm, undo, partial failure, and feedback.
- [Search Filter Experience](#frontend-search-filter) - Unify search, filter chips, clear actions, and result counts.
- [Realtime Update Prompts](#frontend-realtime-updates) - Handle background changes, conflicts, and refresh prompts.

### design
- [Visual Hierarchy Pass](#design-visual-hierarchy) - Reorder headings, metadata, primary actions, and secondary actions.
- [Design Token Audit](#design-token-audit) - Check colors, spacing, radii, and shadows against tokens.
- [Component Variant Matrix](#design-component-variants) - Complete button, input, card, and modal state coverage.
- [Dashboard Layout Pass](#design-dashboard-layout) - Make an operational dashboard easier to scan and compare.
- [Modal Discipline](#design-modal-discipline) - Replace modal misuse with drawers, popovers, or pages where appropriate.
- [Iconography System](#design-iconography) - Unify icon semantics for tools, statuses, and empty states.
- [Color Contrast Pass](#design-color-contrast) - Fix low contrast text, icons, and state colors.
- [Motion Rules](#design-motion-rules) - Define entry, exit, feedback, and reduced-motion behavior.
- [Responsive Grid](#design-responsive-grid) - Define breakpoints, columns, and fixed-format constraints.
- [Toolbar Usability](#design-toolbar-usability) - Improve icon buttons, tooltips, grouping, and disabled states.
- [Data Card System](#design-data-card-system) - Define metric cards with value, trend, anomaly, and source states.
- [Brand Fit Pass](#design-brand-fit) - Align the interface language with the product's audience and use case.

### mobile
- [Mobile Bottom Navigation](#mobile-bottom-nav) - Design thumb-friendly mobile navigation for core paths.
- [Mobile Touch Targets](#mobile-touch-targets) - Ensure buttons, checkboxes, and rows have usable tap areas.
- [Mobile Form Flow](#mobile-form-flow) - Handle long forms, keyboard occlusion, and error positioning.
- [Mobile Table Adaptation](#mobile-table-adaptation) - Convert wide tables into cards, horizontal scroll, or drill-downs.
- [Mobile Filter Drawer](#mobile-filter-drawer) - Add mobile filters with apply, reset, count, and URL state.
- [Mobile Offline State](#mobile-offline-state) - Show offline, cached data, and retry paths clearly.
- [Mobile Image Performance](#mobile-image-performance) - Optimize image sizes, lazy loading, placeholders, and formats.
- [Mobile Safe Area](#mobile-safe-area) - Handle iOS notch, bottom bars, and sticky actions.
- [Mobile Gesture Conflicts](#mobile-gesture-conflicts) - Resolve conflicts between swipe, drag, and scroll interactions.
- [Mobile Login Flow](#mobile-login-flow) - Improve magic link, OTP, password manager, and autofill behavior.
- [Mobile Onboarding](#mobile-onboarding) - Create a short, skippable, restorable first-run path.
- [Mobile Device Matrix](#mobile-device-matrix) - Cover small screen, large screen, iOS, and Android key paths.

### docs
- [Quickstart](#docs-quickstart) - Write the shortest fresh-clone path that runs successfully in five minutes.
- [Install Troubleshooting](#docs-install-troubleshooting) - Document common install failures, causes, and fixes.
- [API Examples](#docs-api-examples) - Add minimal request, response, and error examples for core APIs.
- [Architecture Overview](#docs-architecture-overview) - Explain module boundaries, data flow, and explicit non-goals.
- [Contribution Guide](#docs-contribution-guide) - Document development, testing, commit, and PR review rules.
- [Release Notes](#docs-release-notes) - Create user-facing change, migration, and breaking-change notes.
- [Environment Variables](#docs-env-vars) - List env names, defaults, requiredness, and safety notes.
- [Operator Runbook](#docs-runbook) - Document alerts, recovery, rollback, and data repair steps.
- [Architecture Decision Records](#docs-decision-records) - Add ADR templates and indexes for major technical decisions.
- [Glossary](#docs-glossary) - Unify product, engineering, and data-field terms.
- [Screenshot Docs](#docs-screenshot-docs) - Add real screenshots and labels for UI workflows.
- [Docs Lint Gate](#docs-docs-lint) - Add link, spelling, and executable code block checks.
- [Weekly Changelog Coverage](#claude-weekly-changelog) - Ensure CHANGELOG.md includes an entry for every PR merged this week. Source-backed.

### product
- [User Journeys](#product-user-journeys) - Map persona tasks into pages, events, and success states.
- [PRD Skeleton](#product-prd-skeleton) - Write goals, non-goals, constraints, and acceptance criteria.
- [Onboarding Metrics](#product-onboarding-metrics) - Define activation events, dropoff points, and dashboard queries.
- [Feature Prioritization](#product-feature-prioritization) - Split MVP and later work by impact, cost, and risk.
- [Permission Model](#product-permission-model) - Map roles, resources, actions, and UI visibility.
- [Notification Strategy](#product-notification-strategy) - Define triggers, channels, frequency, and unsubscribe behavior.
- [Empty Data Policy](#product-empty-data-policy) - Choose blank, sample data, import, or CTA by user state.
- [Upgrade Path](#product-upgrade-path) - Design limits, paywalls, trials, and upgrade conversion paths.
- [Feedback Loop](#product-feedback-loop) - Collect, classify, track, and close user feedback.
- [Search Relevance](#product-search-relevance) - Define query handling, ranking, typo tolerance, and no-result behavior.
- [Admin Workflows](#product-admin-workflows) - Design review, undo, audit log, and bulk moderation flows.
- [Success Criteria](#product-success-criteria) - Define quantitative and qualitative completion measures for a feature.

### qa
- [Critical Path Tests](#qa-critical-paths) - Cover signup, create, edit, delete, export, and recovery flows.
- [Regression Matrix](#qa-regression-matrix) - Build feature/browser/role/data-state regression coverage.
- [Fixture Strategy](#qa-fixture-strategy) - Create deterministic seed, mock, factory, and cleanup patterns.
- [Visual Regression](#qa-visual-regression) - Add screenshot diffs for critical pages with controlled thresholds.
- [API Contracts](#qa-api-contracts) - Validate frontend/backend schema, error codes, and boundary values.
- [Flaky Test Audit](#qa-flaky-test-audit) - Find unstable tests and fix waits, isolation, or fixtures.
- [Error Injection](#qa-error-injection) - Simulate 500s, timeouts, network failure, and partial success.
- [Cross-Browser Coverage](#qa-cross-browser) - Run critical flows across Chromium, Firefox, and WebKit.
- [Release Smoke](#qa-release-smoke) - Define the smallest pre-release verification checklist.
- [Data Migration Test](#qa-data-migration) - Verify counts, constraints, and rollback around data migration.
- [Security Smoke](#qa-security-smoke) - Check auth, permission bypass, and sensitive info leakage.
- [Bug Reproduction Template](#qa-bug-repro-template) - Standardize environment, steps, expected, actual, and evidence.

### accessibility
- [Keyboard Navigation](#accessibility-keyboard-nav) - Ensure the whole app works with Tab, Enter, and Escape.
- [Screen Reader Semantics](#accessibility-screen-reader) - Check landmarks, labels, aria-live, and button names.
- [Focus Visible](#accessibility-focus-visible) - Give every interactive element a clear focus state.
- [Color Contrast](#accessibility-color-contrast) - Meet WCAG AA for text, icons, and state colors.
- [Accessible Form Errors](#accessibility-form-errors) - Associate errors with fields so screen readers announce them.
- [Modal Focus Trap](#accessibility-modal-trap) - Focus opens, cycles, closes, and returns correctly.
- [Reduced Motion](#accessibility-reduced-motion) - Respect prefers-reduced-motion for all nonessential motion.
- [Alt Text Audit](#accessibility-alt-text) - Separate decorative, content, and product images.
- [Heading Order](#accessibility-heading-order) - Fix skipped headings and fake styled headings.
- [Live Region Feedback](#accessibility-live-region) - Announce toasts, async completion, and errors accessibly.
- [Touch Accessibility](#accessibility-touch-a11y) - Check tap targets, zoom, and orientation on mobile.
- [Accessibility Audit Report](#accessibility-audit-report) - Produce prioritized issues, impact, fixes, and acceptance checks.

### performance
- [LCP Optimization](#performance-lcp) - Find and optimize the largest contentful paint element.
- [CLS Fix](#performance-cls) - Reserve space for images, ads, and dynamic content.
- [INP Optimization](#performance-inp) - Reduce long tasks and blocking interaction handlers.
- [Bundle Budget](#performance-bundle-budget) - Set route and dependency size budgets in CI.
- [Code Splitting](#performance-code-splitting) - Lazy-load low-frequency routes, charts, and editors.
- [Image Pipeline](#performance-image-pipeline) - Use srcset, modern formats, lazy loading, and cache headers.
- [Font Loading](#performance-font-loading) - Optimize font-display, subsets, and preload hints.
- [API Waterfall](#performance-api-waterfall) - Remove serial requests and prefetch critical data.
- [Cache Strategy](#performance-cache-strategy) - Define browser, CDN, and service-worker cache boundaries.
- [Memory Leak Audit](#performance-memory-leaks) - Check long sessions, lists, subscriptions, and charts for leaks.
- [Render Count Audit](#performance-render-count) - Find unnecessary React renders and expensive selectors.
- [Performance CI Gate](#performance-ci-gate) - Add Lighthouse or trace thresholds to CI.
- [Lighthouse And Core Web Vitals Gate](#explainx-lighthouse-core-web-vitals) - Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions. Source-backed.

### workflow
- [Goal Prompt Writer](#goal-meta-prompt-writer) - Ask the agent to inspect a repo and write a precise goal prompt before execution.
- [Goal Continuation Audit](#goal-continuation-audit) - Check that a long-running goal keeps its done_when and verification contract after compaction.
- [Verifiable End-State Contract](#codex-verifiable-end-state) - Complete one objective only when a verifiable end state is met. Source-backed.
- [Four Files Walkthrough](#hermes-four-files-walkthrough) - Create four note files across turns and verify each contains its number. Source-backed.

### migration
- [Visual Migration With Playwright](#codex-visual-migration-playwright) - Migrate a project while preserving screen output and checking it with Playwright. Source-backed.
- [Feature Port With CI Green](#hermes-feature-port-ci-green) - Port a feature from another repo, include tests, and get CI green. Source-backed.
- [Vue 2 To Vue 3 Visual And Unit Gate](#qiita-vue2-vue3-visual-unit) - Migrate listed Vue screens and stop only when visual and unit tests pass. Source-backed.

### prototype
- [PLAN.md Milestone Prototype](#codex-plan-milestone-prototype) - Implement a PLAN.md-driven prototype with tests at each milestone and browser verification. Source-backed.
- [Canvas Puzzle PLAN.md Prototype](#qiita-canvas-puzzle-plan) - Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes. Source-backed.

### prompt-optimization
- [Eval-Driven Prompt Optimization](#codex-eval-prompt-optimization) - Optimize prompts against an eval suite until the target score or pass rate is reached. Source-backed.
- [Router Prompt Eval Score](#qiita-router-eval-score) - Improve a router prompt against an eval directory until the result score reaches a target. Source-backed.

### testing
- [Auth Tests And Lint Clean](#claude-auth-tests-lint) - Keep working until auth tests pass and the lint step is clean. Source-backed.
- [Ruff Clean Source Tree](#hermes-ruff-src-clean) - Fix every lint error in src and prove ruff passes. Source-backed.
- [TypeScript ESLint Coverage Gate](#explainx-typescript-eslint-coverage) - Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold. Source-backed.

### investigation
- [Session Drift Report](#hermes-session-drift-report) - Investigate session ID drift during mid-run compression and write a report. Source-backed.

### cli
- [EXIF Rename CLI](#hermes-exif-rename-cli) - Build a small CLI that renames photos by EXIF date and test it on a photos folder. Source-backed.

### refactor
- [Auth Dependency Injection Refactor](#explainx-auth-di-refactor) - Refactor auth code to dependency injection while preserving tests, coverage, and public API. Source-backed.

## Examples

<a id="api-contract-drift-audit"></a>
### API Contract Drift Audit

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Compare OpenAPI, implementation, and tests to find field or status-code drift.
- Verification: `npx openapi-diff old.yaml new.yaml && pytest tests/api`

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
- The implementation or documentation directly satisfies: Compare OpenAPI, implementation, and tests to find field or status-code drift.
- The verification command or evidence path succeeds: `npx openapi-diff old.yaml new.yaml && pytest tests/api`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx openapi-diff old.yaml new.yaml && pytest tests/api` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="idempotent-create-endpoint"></a>
### Idempotent Create Endpoint

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add idempotency keys and replay-safe semantics to a create endpoint.
- Verification: `pytest -k idempotency`

```text
/goal
GOAL:
Complete Idempotent Create Endpoint for a backend API service: Add idempotency keys and replay-safe semantics to a create endpoint.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k idempotency`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Add idempotency keys and replay-safe semantics to a create endpoint.
- The verification command or evidence path succeeds: `pytest -k idempotency`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k idempotency` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="api-error-taxonomy"></a>
### API Error Taxonomy

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Unify HTTP status codes, machine error codes, user messages, and logs.
- Verification: `pytest -k error_response`

```text
/goal
GOAL:
Complete API Error Taxonomy for a backend API service: Unify HTTP status codes, machine error codes, user messages, and logs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k error_response`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Unify HTTP status codes, machine error codes, user messages, and logs.
- The verification command or evidence path succeeds: `pytest -k error_response`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k error_response` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="pagination-consistency"></a>
### Pagination Consistency

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Fix cursor or offset pagination so rows are not skipped, duplicated, or reordered.
- Verification: `pytest -k pagination`

```text
/goal
GOAL:
Complete Pagination Consistency for a backend API service: Fix cursor or offset pagination so rows are not skipped, duplicated, or reordered.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k pagination`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix cursor or offset pagination so rows are not skipped, duplicated, or reordered.
- The verification command or evidence path succeeds: `pytest -k pagination`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k pagination` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="request-validation-boundary"></a>
### Request Validation Boundary

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Move input validation to the API boundary and reject unknown fields.
- Verification: `pytest -k validation`

```text
/goal
GOAL:
Complete Request Validation Boundary for a backend API service: Move input validation to the API boundary and reject unknown fields.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k validation`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Move input validation to the API boundary and reject unknown fields.
- The verification command or evidence path succeeds: `pytest -k validation`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k validation` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="api-rate-limit-policy"></a>
### API Rate Limit Policy

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Implement rate limit behavior, headers, and over-limit responses for critical routes.
- Verification: `k6 run rate_limit.js`

```text
/goal
GOAL:
Complete API Rate Limit Policy for a backend API service: Implement rate limit behavior, headers, and over-limit responses for critical routes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `k6 run rate_limit.js`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Implement rate limit behavior, headers, and over-limit responses for critical routes.
- The verification command or evidence path succeeds: `k6 run rate_limit.js`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `k6 run rate_limit.js` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="webhook-retry-contract"></a>
### Webhook Retry Contract

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define webhook signature verification, retry, dedupe, and failure observability.
- Verification: `pytest -k webhook`

```text
/goal
GOAL:
Complete Webhook Retry Contract for a backend API service: Define webhook signature verification, retry, dedupe, and failure observability.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k webhook`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Define webhook signature verification, retry, dedupe, and failure observability.
- The verification command or evidence path succeeds: `pytest -k webhook`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k webhook` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="backward-compatible-response"></a>
### Backward-Compatible Response

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add response fields without breaking old clients and document removal paths.
- Verification: `pytest -k contract`

```text
/goal
GOAL:
Complete Backward-Compatible Response for a backend API service: Add response fields without breaking old clients and document removal paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k contract`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Add response fields without breaking old clients and document removal paths.
- The verification command or evidence path succeeds: `pytest -k contract`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k contract` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="grpc-timeout-propagation"></a>
### gRPC Timeout Propagation

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Propagate deadlines across service calls and cancel work correctly.
- Verification: `go test ./...`

```text
/goal
GOAL:
Complete gRPC Timeout Propagation for a backend API service: Propagate deadlines across service calls and cancel work correctly.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `go test ./...`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Propagate deadlines across service calls and cancel work correctly.
- The verification command or evidence path succeeds: `go test ./...`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `go test ./...` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="async-job-state-machine"></a>
### Async Job State Machine

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Make async job transitions explicit and tested across pending/running/succeeded/failed/canceled.
- Verification: `pytest -k job_state`

```text
/goal
GOAL:
Complete Async Job State Machine for a backend API service: Make async job transitions explicit and tested across pending/running/succeeded/failed/canceled.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k job_state`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Make async job transitions explicit and tested across pending/running/succeeded/failed/canceled.
- The verification command or evidence path succeeds: `pytest -k job_state`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k job_state` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="authz-resource-scope"></a>
### Resource-Level Authorization

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Prevent logged-in users from accessing resources they do not own.
- Verification: `pytest -k authz`

```text
/goal
GOAL:
Complete Resource-Level Authorization for a backend API service: Prevent logged-in users from accessing resources they do not own.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k authz`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Prevent logged-in users from accessing resources they do not own.
- The verification command or evidence path succeeds: `pytest -k authz`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k authz` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="api-versioning-plan"></a>
### API Versioning Plan

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Create a v1/v2 coexistence plan with deprecation headers and migration tests.
- Verification: `pytest -k api_version`

```text
/goal
GOAL:
Complete API Versioning Plan for a backend API service: Create a v1/v2 coexistence plan with deprecation headers and migration tests.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `pytest -k api_version`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Create a v1/v2 coexistence plan with deprecation headers and migration tests.
- The verification command or evidence path succeeds: `pytest -k api_version`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k api_version` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="db-migration-safety"></a>
### Database Migration Safety

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Review a migration for rollback, online execution, and lock risk.
- Verification: `npm run migrate:dry-run`

```text
/goal
GOAL:
Complete Database Migration Safety for a data-backed backend service: Review a migration for rollback, online execution, and lock risk.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `npm run migrate:dry-run`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Review a migration for rollback, online execution, and lock risk.
- The verification command or evidence path succeeds: `npm run migrate:dry-run`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run migrate:dry-run` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="transaction-boundary-audit"></a>
### Transaction Boundary Audit

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Find missing or oversized transactions in multi-table write paths.
- Verification: `pytest -k transaction`

```text
/goal
GOAL:
Complete Transaction Boundary Audit for a data-backed backend service: Find missing or oversized transactions in multi-table write paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k transaction`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Find missing or oversized transactions in multi-table write paths.
- The verification command or evidence path succeeds: `pytest -k transaction`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k transaction` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="cache-invalidation-map"></a>
### Cache Invalidation Map

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Map write paths to cache keys and fix stale reads.
- Verification: `pytest -k cache`

```text
/goal
GOAL:
Complete Cache Invalidation Map for a data-backed backend service: Map write paths to cache keys and fix stale reads.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k cache`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Map write paths to cache keys and fix stale reads.
- The verification command or evidence path succeeds: `pytest -k cache`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k cache` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="n-plus-one-query-fix"></a>
### N+1 Query Fix

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Reduce list endpoint query count with batching or preloading.
- Verification: `pytest -k query_count`

```text
/goal
GOAL:
Complete N+1 Query Fix for a data-backed backend service: Reduce list endpoint query count with batching or preloading.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k query_count`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Reduce list endpoint query count with batching or preloading.
- The verification command or evidence path succeeds: `pytest -k query_count`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k query_count` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="optimistic-locking-rollout"></a>
### Optimistic Locking Rollout

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add version checks and conflict responses for concurrent edits.
- Verification: `pytest -k optimistic_lock`

```text
/goal
GOAL:
Complete Optimistic Locking Rollout for a data-backed backend service: Add version checks and conflict responses for concurrent edits.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k optimistic_lock`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Add version checks and conflict responses for concurrent edits.
- The verification command or evidence path succeeds: `pytest -k optimistic_lock`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k optimistic_lock` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="soft-delete-integrity"></a>
### Soft Delete Integrity

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Make queries, unique indexes, and restore flows respect soft deletion.
- Verification: `pytest -k soft_delete`

```text
/goal
GOAL:
Complete Soft Delete Integrity for a data-backed backend service: Make queries, unique indexes, and restore flows respect soft deletion.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k soft_delete`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Make queries, unique indexes, and restore flows respect soft deletion.
- The verification command or evidence path succeeds: `pytest -k soft_delete`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k soft_delete` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="db-index-regression"></a>
### Index Regression Check

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add or adjust indexes and prove read gains do not create unacceptable write cost.
- Verification: `pytest -k slow_query`

```text
/goal
GOAL:
Complete Index Regression Check for a data-backed backend service: Add or adjust indexes and prove read gains do not create unacceptable write cost.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k slow_query`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Add or adjust indexes and prove read gains do not create unacceptable write cost.
- The verification command or evidence path succeeds: `pytest -k slow_query`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k slow_query` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="outbox-pattern-adoption"></a>
### Outbox Reliable Events

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Use an outbox table to prevent lost events after successful database commits.
- Verification: `pytest -k outbox`

```text
/goal
GOAL:
Complete Outbox Reliable Events for a data-backed backend service: Use an outbox table to prevent lost events after successful database commits.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k outbox`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Use an outbox table to prevent lost events after successful database commits.
- The verification command or evidence path succeeds: `pytest -k outbox`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k outbox` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="read-replica-lag-guard"></a>
### Read Replica Lag Guard

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Prevent write-after-read paths from hitting stale replicas.
- Verification: `pytest -k replica_lag`

```text
/goal
GOAL:
Complete Read Replica Lag Guard for a data-backed backend service: Prevent write-after-read paths from hitting stale replicas.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `pytest -k replica_lag`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Prevent write-after-read paths from hitting stale replicas.
- The verification command or evidence path succeeds: `pytest -k replica_lag`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k replica_lag` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="schema-drift-detector"></a>
### Schema Drift Detector

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Compare ORM models, migrations, and the live database schema.
- Verification: `prisma migrate diff`

```text
/goal
GOAL:
Complete Schema Drift Detector for a data-backed backend service: Compare ORM models, migrations, and the live database schema.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `prisma migrate diff`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Compare ORM models, migrations, and the live database schema.
- The verification command or evidence path succeeds: `prisma migrate diff`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `prisma migrate diff` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="ci-flaky-test-triage"></a>
### CI Flaky Test Triage

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Identify flaky tests, separate real failures, and fix unstable waits or fixtures.
- Verification: `gh run view --log`

```text
/goal
GOAL:
Complete CI Flaky Test Triage for a repository with CI/CD automation: Identify flaky tests, separate real failures, and fix unstable waits or fixtures.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `gh run view --log`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Identify flaky tests, separate real failures, and fix unstable waits or fixtures.
- The verification command or evidence path succeeds: `gh run view --log`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `gh run view --log` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="build-cache-correctness"></a>
### Build Cache Correctness

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check whether CI cache keys cause stale dependencies or cross-branch pollution.
- Verification: `npm ci && npm test`

```text
/goal
GOAL:
Complete Build Cache Correctness for a repository with CI/CD automation: Check whether CI cache keys cause stale dependencies or cross-branch pollution.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `npm ci && npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Check whether CI cache keys cause stale dependencies or cross-branch pollution.
- The verification command or evidence path succeeds: `npm ci && npm test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm ci && npm test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="dependency-update-gate"></a>
### Dependency Update Gate

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add dependency upgrade checks for tests, licenses, and vulnerabilities.
- Verification: `npm audit && npm test`

```text
/goal
GOAL:
Complete Dependency Update Gate for a repository with CI/CD automation: Add dependency upgrade checks for tests, licenses, and vulnerabilities.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `npm audit && npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Add dependency upgrade checks for tests, licenses, and vulnerabilities.
- The verification command or evidence path succeeds: `npm audit && npm test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm audit && npm test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="monorepo-affected-tests"></a>
### Monorepo Affected Tests

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Run only affected tests without missing cross-package contracts.
- Verification: `nx affected:test`

```text
/goal
GOAL:
Complete Monorepo Affected Tests for a repository with CI/CD automation: Run only affected tests without missing cross-package contracts.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `nx affected:test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Run only affected tests without missing cross-package contracts.
- The verification command or evidence path succeeds: `nx affected:test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `nx affected:test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="release-note-from-diff"></a>
### Release Notes From Diff

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Generate user-facing release notes from commits, PR labels, and breaking changes.
- Verification: `git log --oneline last..HEAD`

```text
/goal
GOAL:
Complete Release Notes From Diff for a repository with CI/CD automation: Generate user-facing release notes from commits, PR labels, and breaking changes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `git log --oneline last..HEAD`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Generate user-facing release notes from commits, PR labels, and breaking changes.
- The verification command or evidence path succeeds: `git log --oneline last..HEAD`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `git log --oneline last..HEAD` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="artifact-provenance"></a>
### Artifact Provenance

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Trace a package or image back to the commit and workflow that produced it.
- Verification: `gh run view`

```text
/goal
GOAL:
Complete Artifact Provenance for a repository with CI/CD automation: Trace a package or image back to the commit and workflow that produced it.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `gh run view`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Trace a package or image back to the commit and workflow that produced it.
- The verification command or evidence path succeeds: `gh run view`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `gh run view` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="ci-permission-minimize"></a>
### CI Permission Minimization

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Tighten GitHub Actions token permissions without breaking workflows.
- Verification: `gh workflow run ci.yml`

```text
/goal
GOAL:
Complete CI Permission Minimization for a repository with CI/CD automation: Tighten GitHub Actions token permissions without breaking workflows.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `gh workflow run ci.yml`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Tighten GitHub Actions token permissions without breaking workflows.
- The verification command or evidence path succeeds: `gh workflow run ci.yml`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `gh workflow run ci.yml` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="branch-protection-audit"></a>
### Branch Protection Audit

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Audit required checks, reviews, linear history, and admin bypasses.
- Verification: `gh api repos/OWNER/REPO/branches/main/protection`

```text
/goal
GOAL:
Complete Branch Protection Audit for a repository with CI/CD automation: Audit required checks, reviews, linear history, and admin bypasses.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `gh api repos/OWNER/REPO/branches/main/protection`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Audit required checks, reviews, linear history, and admin bypasses.
- The verification command or evidence path succeeds: `gh api repos/OWNER/REPO/branches/main/protection`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `gh api repos/OWNER/REPO/branches/main/protection` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="release-rollback-drill"></a>
### Release Rollback Drill

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Create and test a rollback path for the latest release.
- Verification: `npm run smoke`

```text
/goal
GOAL:
Complete Release Rollback Drill for a repository with CI/CD automation: Create and test a rollback path for the latest release.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `npm run smoke`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Create and test a rollback path for the latest release.
- The verification command or evidence path succeeds: `npm run smoke`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run smoke` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="semantic-version-check"></a>
### Semantic Version Check

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Infer the correct semver bump from API, behavior, and changelog diffs.
- Verification: `npm test`

```text
/goal
GOAL:
Complete Semantic Version Check for a repository with CI/CD automation: Infer the correct semver bump from API, behavior, and changelog diffs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Infer the correct semver bump from API, behavior, and changelog diffs.
- The verification command or evidence path succeeds: `npm test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docker-image-slimming"></a>
### Docker Image Slimming

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Reduce image size while keeping runtime dependencies and security scans green.
- Verification: `docker build . && trivy image IMAGE`

```text
/goal
GOAL:
Complete Docker Image Slimming for a deployed service: Reduce image size while keeping runtime dependencies and security scans green.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `docker build . && trivy image IMAGE`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Reduce image size while keeping runtime dependencies and security scans green.
- The verification command or evidence path succeeds: `docker build . && trivy image IMAGE`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `docker build . && trivy image IMAGE` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="k8s-readiness-liveness"></a>
### Kubernetes Probe Repair

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Separate startup, readiness, and liveness probes to avoid bad restarts.
- Verification: `kubectl describe pod`

```text
/goal
GOAL:
Complete Kubernetes Probe Repair for a deployed service: Separate startup, readiness, and liveness probes to avoid bad restarts.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `kubectl describe pod`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Separate startup, readiness, and liveness probes to avoid bad restarts.
- The verification command or evidence path succeeds: `kubectl describe pod`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `kubectl describe pod` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="terraform-plan-review"></a>
### Terraform Plan Review

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Review infrastructure changes for deletes, replacements, and permission expansion.
- Verification: `terraform plan -out=tfplan`

```text
/goal
GOAL:
Complete Terraform Plan Review for a deployed service: Review infrastructure changes for deletes, replacements, and permission expansion.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `terraform plan -out=tfplan`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Review infrastructure changes for deletes, replacements, and permission expansion.
- The verification command or evidence path succeeds: `terraform plan -out=tfplan`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `terraform plan -out=tfplan` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="helm-values-drift"></a>
### Helm Values Drift

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Compare environment values to find hidden staging/prod differences.
- Verification: `helm diff upgrade`

```text
/goal
GOAL:
Complete Helm Values Drift for a deployed service: Compare environment values to find hidden staging/prod differences.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `helm diff upgrade`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Compare environment values to find hidden staging/prod differences.
- The verification command or evidence path succeeds: `helm diff upgrade`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `helm diff upgrade` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="autoscaling-thresholds"></a>
### Autoscaling Thresholds

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Tune HPA or worker scaling thresholds against real load and queue depth.
- Verification: `kubectl get hpa`

```text
/goal
GOAL:
Complete Autoscaling Thresholds for a deployed service: Tune HPA or worker scaling thresholds against real load and queue depth.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `kubectl get hpa`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Tune HPA or worker scaling thresholds against real load and queue depth.
- The verification command or evidence path succeeds: `kubectl get hpa`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `kubectl get hpa` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="runtime-config-validation"></a>
### Runtime Config Validation

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Fail startup on missing or invalid environment and config values.
- Verification: `docker run --env-file .env.example IMAGE`

```text
/goal
GOAL:
Complete Runtime Config Validation for a deployed service: Fail startup on missing or invalid environment and config values.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `docker run --env-file .env.example IMAGE`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Fail startup on missing or invalid environment and config values.
- The verification command or evidence path succeeds: `docker run --env-file .env.example IMAGE`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `docker run --env-file .env.example IMAGE` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="zero-downtime-migration"></a>
### Zero-Downtime Migration

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Plan and verify expand-migrate-contract deployment steps.
- Verification: `npm run smoke`

```text
/goal
GOAL:
Complete Zero-Downtime Migration for a deployed service: Plan and verify expand-migrate-contract deployment steps.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `npm run smoke`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Plan and verify expand-migrate-contract deployment steps.
- The verification command or evidence path succeeds: `npm run smoke`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run smoke` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="observability-minimum"></a>
### Observability Minimum

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add logs, metrics, traces, and alerts for a service's critical paths.
- Verification: `npm test && curl localhost:PORT/metrics`

```text
/goal
GOAL:
Complete Observability Minimum for a deployed service: Add logs, metrics, traces, and alerts for a service's critical paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `npm test && curl localhost:PORT/metrics`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Add logs, metrics, traces, and alerts for a service's critical paths.
- The verification command or evidence path succeeds: `npm test && curl localhost:PORT/metrics`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test && curl localhost:PORT/metrics` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="incident-runbook-gap"></a>
### Incident Runbook Gap

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Turn a recent incident timeline into missing runbook and alert updates.
- Verification: `markdownlint docs/runbooks`

```text
/goal
GOAL:
Complete Incident Runbook Gap for a deployed service: Turn a recent incident timeline into missing runbook and alert updates.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `markdownlint docs/runbooks`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Turn a recent incident timeline into missing runbook and alert updates.
- The verification command or evidence path succeeds: `markdownlint docs/runbooks`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/runbooks` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="queue-backpressure"></a>
### Queue Backpressure

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Protect databases and external APIs when worker queues build up.
- Verification: `pytest -k backpressure`

```text
/goal
GOAL:
Complete Queue Backpressure for a deployed service: Protect databases and external APIs when worker queues build up.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `pytest -k backpressure`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Protect databases and external APIs when worker queues build up.
- The verification command or evidence path succeeds: `pytest -k backpressure`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k backpressure` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="sql-injection-audit"></a>
### SQL Injection Audit

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Replace SQL string concatenation with parameterized queries and tests.
- Verification: `pytest -k injection`

```text
/goal
GOAL:
Complete SQL Injection Audit for an application with security-sensitive code paths: Replace SQL string concatenation with parameterized queries and tests.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k injection`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Replace SQL string concatenation with parameterized queries and tests.
- The verification command or evidence path succeeds: `pytest -k injection`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k injection` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="command-injection-audit"></a>
### Command Injection Audit

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Replace shell string execution with argument arrays and validation.
- Verification: `pytest -k command_injection`

```text
/goal
GOAL:
Complete Command Injection Audit for an application with security-sensitive code paths: Replace shell string execution with argument arrays and validation.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k command_injection`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Replace shell string execution with argument arrays and validation.
- The verification command or evidence path succeeds: `pytest -k command_injection`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k command_injection` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="ssrf-defense-review"></a>
### SSRF Defense Review

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add URL allowlists and DNS/IP checks for fetch or callback features.
- Verification: `pytest -k ssrf`

```text
/goal
GOAL:
Complete SSRF Defense Review for an application with security-sensitive code paths: Add URL allowlists and DNS/IP checks for fetch or callback features.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k ssrf`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Add URL allowlists and DNS/IP checks for fetch or callback features.
- The verification command or evidence path succeeds: `pytest -k ssrf`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k ssrf` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="xss-output-encoding"></a>
### XSS Output Encoding

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Audit HTML and Markdown rendering for unsafe sinks and missing encoding.
- Verification: `npm test -- xss`

```text
/goal
GOAL:
Complete XSS Output Encoding for an application with security-sensitive code paths: Audit HTML and Markdown rendering for unsafe sinks and missing encoding.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `npm test -- xss`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Audit HTML and Markdown rendering for unsafe sinks and missing encoding.
- The verification command or evidence path succeeds: `npm test -- xss`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test -- xss` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="csrf-sensitive-action"></a>
### CSRF Sensitive Action

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Protect cookie-authenticated writes from cross-site requests.
- Verification: `pytest -k csrf`

```text
/goal
GOAL:
Complete CSRF Sensitive Action for an application with security-sensitive code paths: Protect cookie-authenticated writes from cross-site requests.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k csrf`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Protect cookie-authenticated writes from cross-site requests.
- The verification command or evidence path succeeds: `pytest -k csrf`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k csrf` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="auth-bypass-route-map"></a>
### Auth Bypass Route Map

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Enumerate routes and verify unauthenticated and unauthorized behavior.
- Verification: `pytest -k auth`

```text
/goal
GOAL:
Complete Auth Bypass Route Map for an application with security-sensitive code paths: Enumerate routes and verify unauthenticated and unauthorized behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k auth`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Enumerate routes and verify unauthenticated and unauthorized behavior.
- The verification command or evidence path succeeds: `pytest -k auth`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k auth` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="file-upload-security"></a>
### File Upload Security

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Validate MIME, extension, size, scanning, and storage isolation.
- Verification: `pytest -k upload_security`

```text
/goal
GOAL:
Complete File Upload Security for an application with security-sensitive code paths: Validate MIME, extension, size, scanning, and storage isolation.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k upload_security`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Validate MIME, extension, size, scanning, and storage isolation.
- The verification command or evidence path succeeds: `pytest -k upload_security`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k upload_security` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="tenant-isolation-test"></a>
### Tenant Isolation Test

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Verify tenant IDs are enforced in queries, caches, and background jobs.
- Verification: `pytest -k tenant`

```text
/goal
GOAL:
Complete Tenant Isolation Test for an application with security-sensitive code paths: Verify tenant IDs are enforced in queries, caches, and background jobs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k tenant`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify tenant IDs are enforced in queries, caches, and background jobs.
- The verification command or evidence path succeeds: `pytest -k tenant`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k tenant` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="replay-attack-defense"></a>
### Replay Attack Defense

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add nonce, timestamp, and expiration checks to signed requests.
- Verification: `pytest -k replay`

```text
/goal
GOAL:
Complete Replay Attack Defense for an application with security-sensitive code paths: Add nonce, timestamp, and expiration checks to signed requests.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k replay`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Add nonce, timestamp, and expiration checks to signed requests.
- The verification command or evidence path succeeds: `pytest -k replay`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k replay` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="insecure-direct-object-ref"></a>
### IDOR Audit

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Verify direct object ID access always checks ownership or scope.
- Verification: `pytest -k idor`

```text
/goal
GOAL:
Complete IDOR Audit for an application with security-sensitive code paths: Verify direct object ID access always checks ownership or scope.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `pytest -k idor`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify direct object ID access always checks ownership or scope.
- The verification command or evidence path succeeds: `pytest -k idor`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k idor` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="secret-scan-baseline"></a>
### Secret Scan Baseline

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add secret scanning and triage historical findings safely.
- Verification: `gitleaks detect`

```text
/goal
GOAL:
Complete Secret Scan Baseline for a production operations environment: Add secret scanning and triage historical findings safely.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `gitleaks detect`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Add secret scanning and triage historical findings safely.
- The verification command or evidence path succeeds: `gitleaks detect`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `gitleaks detect` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="iam-least-privilege"></a>
### IAM Least Privilege

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Reduce cloud permissions to observed API usage and documented needs.
- Verification: `terraform plan`

```text
/goal
GOAL:
Complete IAM Least Privilege for a production operations environment: Reduce cloud permissions to observed API usage and documented needs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `terraform plan`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Reduce cloud permissions to observed API usage and documented needs.
- The verification command or evidence path succeeds: `terraform plan`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `terraform plan` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-actions-supply-chain"></a>
### GitHub Actions Supply Chain

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Pin third-party actions and review workflow permissions.
- Verification: `rg "uses:" .github/workflows`

```text
/goal
GOAL:
Complete GitHub Actions Supply Chain for a production operations environment: Pin third-party actions and review workflow permissions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `rg "uses:" .github/workflows`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Pin third-party actions and review workflow permissions.
- The verification command or evidence path succeeds: `rg "uses:" .github/workflows`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `rg "uses:" .github/workflows` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="container-vuln-triage"></a>
### Container Vulnerability Triage

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Prioritize image CVEs by exploitability and runtime exposure.
- Verification: `trivy image IMAGE`

```text
/goal
GOAL:
Complete Container Vulnerability Triage for a production operations environment: Prioritize image CVEs by exploitability and runtime exposure.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `trivy image IMAGE`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Prioritize image CVEs by exploitability and runtime exposure.
- The verification command or evidence path succeeds: `trivy image IMAGE`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `trivy image IMAGE` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="audit-log-coverage"></a>
### Audit Log Coverage

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add audit logs for login, permission changes, and sensitive data access.
- Verification: `pytest -k audit_log`

```text
/goal
GOAL:
Complete Audit Log Coverage for a production operations environment: Add audit logs for login, permission changes, and sensitive data access.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `pytest -k audit_log`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Add audit logs for login, permission changes, and sensitive data access.
- The verification command or evidence path succeeds: `pytest -k audit_log`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k audit_log` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="secret-rotation-drill"></a>
### Secret Rotation Drill

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Verify rotating a key does not interrupt the service.
- Verification: `npm run smoke`

```text
/goal
GOAL:
Complete Secret Rotation Drill for a production operations environment: Verify rotating a key does not interrupt the service.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `npm run smoke`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify rotating a key does not interrupt the service.
- The verification command or evidence path succeeds: `npm run smoke`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run smoke` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="dependency-confusion-guard"></a>
### Dependency Confusion Guard

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Lock private package scopes and registries to prevent wrong-source installs.
- Verification: `npm ci`

```text
/goal
GOAL:
Complete Dependency Confusion Guard for a production operations environment: Lock private package scopes and registries to prevent wrong-source installs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `npm ci`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Lock private package scopes and registries to prevent wrong-source installs.
- The verification command or evidence path succeeds: `npm ci`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm ci` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="sbom-generation"></a>
### SBOM Generation

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Generate an SBOM and attach it to release artifacts.
- Verification: `syft packages dir:.`

```text
/goal
GOAL:
Complete SBOM Generation for a production operations environment: Generate an SBOM and attach it to release artifacts.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `syft packages dir:.`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Generate an SBOM and attach it to release artifacts.
- The verification command or evidence path succeeds: `syft packages dir:.`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `syft packages dir:.` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="prod-access-review"></a>
### Production Access Review

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Inventory production access, approval paths, and audit evidence.
- Verification: `terraform state list`

```text
/goal
GOAL:
Complete Production Access Review for a production operations environment: Inventory production access, approval paths, and audit evidence.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `terraform state list`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Inventory production access, approval paths, and audit evidence.
- The verification command or evidence path succeeds: `terraform state list`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `terraform state list` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="backup-restore-security"></a>
### Backup Restore Security

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Verify encrypted backups and a restricted restore path.
- Verification: `./scripts/restore-dry-run.sh`

```text
/goal
GOAL:
Complete Backup Restore Security for a production operations environment: Verify encrypted backups and a restricted restore path.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `./scripts/restore-dry-run.sh`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify encrypted backups and a restricted restore path.
- The verification command or evidence path succeeds: `./scripts/restore-dry-run.sh`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `./scripts/restore-dry-run.sh` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="etl-contract-tests"></a>
### ETL Contract Tests

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add schema and sample-data contracts between source and target tables.
- Verification: `pytest tests/etl`

```text
/goal
GOAL:
Complete ETL Contract Tests for a data pipeline project: Add schema and sample-data contracts between source and target tables.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `pytest tests/etl`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Add schema and sample-data contracts between source and target tables.
- The verification command or evidence path succeeds: `pytest tests/etl`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/etl` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="data-quality-rules"></a>
### Data Quality Rules

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define null, uniqueness, range, and reference checks for key datasets.
- Verification: `great_expectations checkpoint run main`

```text
/goal
GOAL:
Complete Data Quality Rules for a data pipeline project: Define null, uniqueness, range, and reference checks for key datasets.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `great_expectations checkpoint run main`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Define null, uniqueness, range, and reference checks for key datasets.
- The verification command or evidence path succeeds: `great_expectations checkpoint run main`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `great_expectations checkpoint run main` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="backfill-safety-plan"></a>
### Backfill Safety Plan

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Design a sharded, resumable, verifiable historical backfill.
- Verification: `pytest -k backfill`

```text
/goal
GOAL:
Complete Backfill Safety Plan for a data pipeline project: Design a sharded, resumable, verifiable historical backfill.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `pytest -k backfill`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Design a sharded, resumable, verifiable historical backfill.
- The verification command or evidence path succeeds: `pytest -k backfill`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k backfill` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="incremental-load-watermark"></a>
### Incremental Load Watermark

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Fix missing or duplicate rows in incremental sync logic.
- Verification: `pytest -k watermark`

```text
/goal
GOAL:
Complete Incremental Load Watermark for a data pipeline project: Fix missing or duplicate rows in incremental sync logic.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `pytest -k watermark`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix missing or duplicate rows in incremental sync logic.
- The verification command or evidence path succeeds: `pytest -k watermark`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k watermark` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="late-arriving-data"></a>
### Late-Arriving Data

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Handle delayed events and metric corrections safely.
- Verification: `pytest -k late_arrival`

```text
/goal
GOAL:
Complete Late-Arriving Data for a data pipeline project: Handle delayed events and metric corrections safely.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `pytest -k late_arrival`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Handle delayed events and metric corrections safely.
- The verification command or evidence path succeeds: `pytest -k late_arrival`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k late_arrival` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="data-lineage-map"></a>
### Data Lineage Map

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Map critical report fields from source to consumers.
- Verification: `dbt docs generate`

```text
/goal
GOAL:
Complete Data Lineage Map for a data pipeline project: Map critical report fields from source to consumers.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `dbt docs generate`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Map critical report fields from source to consumers.
- The verification command or evidence path succeeds: `dbt docs generate`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `dbt docs generate` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="pii-classification"></a>
### PII Classification

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Classify sensitive fields and document masking rules.
- Verification: `pytest -k pii`

```text
/goal
GOAL:
Complete PII Classification for a data pipeline project: Classify sensitive fields and document masking rules.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `pytest -k pii`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Classify sensitive fields and document masking rules.
- The verification command or evidence path succeeds: `pytest -k pii`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k pii` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="data-retention-enforcement"></a>
### Data Retention Enforcement

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Verify expiration, archival, deletion, and audit behavior.
- Verification: `pytest -k retention`

```text
/goal
GOAL:
Complete Data Retention Enforcement for a data pipeline project: Verify expiration, archival, deletion, and audit behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `pytest -k retention`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify expiration, archival, deletion, and audit behavior.
- The verification command or evidence path succeeds: `pytest -k retention`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k retention` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="warehouse-cost-audit"></a>
### Warehouse Cost Audit

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Find expensive queries, duplicate tables, and unused scheduled jobs.
- Verification: `dbt test`

```text
/goal
GOAL:
Complete Warehouse Cost Audit for a data pipeline project: Find expensive queries, duplicate tables, and unused scheduled jobs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `dbt test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Find expensive queries, duplicate tables, and unused scheduled jobs.
- The verification command or evidence path succeeds: `dbt test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `dbt test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="stream-processing-lag"></a>
### Stream Processing Lag

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Diagnose Kafka/Flink/Spark lag and checkpoint bottlenecks.
- Verification: `pytest -k stream_lag`

```text
/goal
GOAL:
Complete Stream Processing Lag for a data pipeline project: Diagnose Kafka/Flink/Spark lag and checkpoint bottlenecks.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `pytest -k stream_lag`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Diagnose Kafka/Flink/Spark lag and checkpoint bottlenecks.
- The verification command or evidence path succeeds: `pytest -k stream_lag`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k stream_lag` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="metric-definition-lock"></a>
### Metric Definition Lock

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Turn core metric definitions into tested SQL or semantic-layer checks.
- Verification: `dbt test`

```text
/goal
GOAL:
Complete Metric Definition Lock for an analytics or BI project: Turn core metric definitions into tested SQL or semantic-layer checks.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `dbt test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Turn core metric definitions into tested SQL or semantic-layer checks.
- The verification command or evidence path succeeds: `dbt test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `dbt test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="dashboard-trust-audit"></a>
### Dashboard Trust Audit

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check filters, timezone, refresh cadence, permissions, and source reconciliation.
- Verification: `dbt test && pytest tests/dashboard`

```text
/goal
GOAL:
Complete Dashboard Trust Audit for an analytics or BI project: Check filters, timezone, refresh cadence, permissions, and source reconciliation.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `dbt test && pytest tests/dashboard`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Check filters, timezone, refresh cadence, permissions, and source reconciliation.
- The verification command or evidence path succeeds: `dbt test && pytest tests/dashboard`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `dbt test && pytest tests/dashboard` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="ab-test-srm-check"></a>
### A/B Test SRM Check

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Detect sample ratio mismatch in experiment assignment.
- Verification: `pytest -k srm`

```text
/goal
GOAL:
Complete A/B Test SRM Check for an analytics or BI project: Detect sample ratio mismatch in experiment assignment.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `pytest -k srm`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Detect sample ratio mismatch in experiment assignment.
- The verification command or evidence path succeeds: `pytest -k srm`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k srm` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="funnel-dropoff-diagnosis"></a>
### Funnel Dropoff Diagnosis

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Validate funnel events, step counts, and latency before interpreting dropoff.
- Verification: `pytest -k funnel`

```text
/goal
GOAL:
Complete Funnel Dropoff Diagnosis for an analytics or BI project: Validate funnel events, step counts, and latency before interpreting dropoff.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `pytest -k funnel`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Validate funnel events, step counts, and latency before interpreting dropoff.
- The verification command or evidence path succeeds: `pytest -k funnel`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k funnel` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="cohort-retention-query"></a>
### Cohort Retention Query

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Create reusable retention SQL with hand-checked small samples.
- Verification: `dbt test -s retention`

```text
/goal
GOAL:
Complete Cohort Retention Query for an analytics or BI project: Create reusable retention SQL with hand-checked small samples.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `dbt test -s retention`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Create reusable retention SQL with hand-checked small samples.
- The verification command or evidence path succeeds: `dbt test -s retention`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `dbt test -s retention` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="revenue-reconciliation"></a>
### Revenue Reconciliation

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Reconcile payments, orders, refunds, and finance definitions.
- Verification: `pytest -k revenue_reconciliation`

```text
/goal
GOAL:
Complete Revenue Reconciliation for an analytics or BI project: Reconcile payments, orders, refunds, and finance definitions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `pytest -k revenue_reconciliation`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Reconcile payments, orders, refunds, and finance definitions.
- The verification command or evidence path succeeds: `pytest -k revenue_reconciliation`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k revenue_reconciliation` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="event-taxonomy-cleanup"></a>
### Event Taxonomy Cleanup

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Deduplicate event names, properties, and version changes.
- Verification: `pytest -k event_schema`

```text
/goal
GOAL:
Complete Event Taxonomy Cleanup for an analytics or BI project: Deduplicate event names, properties, and version changes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `pytest -k event_schema`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Deduplicate event names, properties, and version changes.
- The verification command or evidence path succeeds: `pytest -k event_schema`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k event_schema` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="anomaly-detection-baseline"></a>
### Anomaly Detection Baseline

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Backtest alert thresholds against historical metrics.
- Verification: `pytest -k anomaly`

```text
/goal
GOAL:
Complete Anomaly Detection Baseline for an analytics or BI project: Backtest alert thresholds against historical metrics.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `pytest -k anomaly`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Backtest alert thresholds against historical metrics.
- The verification command or evidence path succeeds: `pytest -k anomaly`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k anomaly` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="attribution-window-review"></a>
### Attribution Window Review

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Verify campaign attribution windows and dedupe rules.
- Verification: `dbt test -s attribution`

```text
/goal
GOAL:
Complete Attribution Window Review for an analytics or BI project: Verify campaign attribution windows and dedupe rules.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `dbt test -s attribution`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify campaign attribution windows and dedupe rules.
- The verification command or evidence path succeeds: `dbt test -s attribution`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `dbt test -s attribution` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="self-serve-data-contract"></a>
### Self-Serve Data Contract

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define trusted datasets and usage limits for business users.
- Verification: `dbt test -s semantic`

```text
/goal
GOAL:
Complete Self-Serve Data Contract for an analytics or BI project: Define trusted datasets and usage limits for business users.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `dbt test -s semantic`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Define trusted datasets and usage limits for business users.
- The verification command or evidence path succeeds: `dbt test -s semantic`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `dbt test -s semantic` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="llm-golden-set-build"></a>
### LLM Golden Set Build

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Build an eval set from real failures and frequent tasks.
- Verification: `pytest evals`

```text
/goal
GOAL:
Complete LLM Golden Set Build for an AI evaluation project: Build an eval set from real failures and frequent tasks.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Build an eval set from real failures and frequent tasks.
- The verification command or evidence path succeeds: `pytest evals`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="llm-regression-gate"></a>
### LLM Regression Gate

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Compare old and new model or prompt outputs in PRs.
- Verification: `pytest evals`

```text
/goal
GOAL:
Complete LLM Regression Gate for an AI evaluation project: Compare old and new model or prompt outputs in PRs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Compare old and new model or prompt outputs in PRs.
- The verification command or evidence path succeeds: `pytest evals`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="judge-calibration"></a>
### Judge Calibration

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Measure LLM judge agreement against human labels.
- Verification: `pytest evals/judges`

```text
/goal
GOAL:
Complete Judge Calibration for an AI evaluation project: Measure LLM judge agreement against human labels.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals/judges`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Measure LLM judge agreement against human labels.
- The verification command or evidence path succeeds: `pytest evals/judges`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/judges` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="hallucination-probe-suite"></a>
### Hallucination Probe Suite

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Add negative cases for nonexistent files, fields, APIs, and sources.
- Verification: `pytest evals/hallucination`

```text
/goal
GOAL:
Complete Hallucination Probe Suite for an AI evaluation project: Add negative cases for nonexistent files, fields, APIs, and sources.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals/hallucination`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Add negative cases for nonexistent files, fields, APIs, and sources.
- The verification command or evidence path succeeds: `pytest evals/hallucination`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/hallucination` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="rag-answer-faithfulness"></a>
### RAG Answer Faithfulness

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Check that answers are supported by retrieved evidence.
- Verification: `pytest evals/rag`

```text
/goal
GOAL:
Complete RAG Answer Faithfulness for an AI evaluation project: Check that answers are supported by retrieved evidence.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals/rag`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Check that answers are supported by retrieved evidence.
- The verification command or evidence path succeeds: `pytest evals/rag`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/rag` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="tool-use-eval"></a>
### Tool Use Eval

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Evaluate whether an agent selects, orders, and validates tools correctly.
- Verification: `pytest evals/tool_use`

```text
/goal
GOAL:
Complete Tool Use Eval for an AI evaluation project: Evaluate whether an agent selects, orders, and validates tools correctly.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals/tool_use`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Evaluate whether an agent selects, orders, and validates tools correctly.
- The verification command or evidence path succeeds: `pytest evals/tool_use`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/tool_use` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="adversarial-prompt-redteam"></a>
### Prompt Injection Red Team

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Test prompt leakage, unauthorized tools, and instruction override attempts.
- Verification: `pytest evals/redteam`

```text
/goal
GOAL:
Complete Prompt Injection Red Team for an AI evaluation project: Test prompt leakage, unauthorized tools, and instruction override attempts.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals/redteam`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Test prompt leakage, unauthorized tools, and instruction override attempts.
- The verification command or evidence path succeeds: `pytest evals/redteam`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/redteam` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="eval-data-dedup"></a>
### Eval Data Dedup

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Remove duplicates, leakage, and near-identical eval samples.
- Verification: `python scripts/dedup_evals.py`

```text
/goal
GOAL:
Complete Eval Data Dedup for an AI evaluation project: Remove duplicates, leakage, and near-identical eval samples.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `python scripts/dedup_evals.py`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Remove duplicates, leakage, and near-identical eval samples.
- The verification command or evidence path succeeds: `python scripts/dedup_evals.py`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `python scripts/dedup_evals.py` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="cost-quality-frontier"></a>
### Cost Quality Frontier

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Compare models by quality, latency, and cost to choose routing tiers.
- Verification: `pytest evals --record-costs`

```text
/goal
GOAL:
Complete Cost Quality Frontier for an AI evaluation project: Compare models by quality, latency, and cost to choose routing tiers.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals --record-costs`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Compare models by quality, latency, and cost to choose routing tiers.
- The verification command or evidence path succeeds: `pytest evals --record-costs`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals --record-costs` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="rubric-driven-eval"></a>
### Rubric-Driven Eval

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Replace binary scores with multi-dimensional rubrics for complex tasks.
- Verification: `pytest evals/rubrics`

```text
/goal
GOAL:
Complete Rubric-Driven Eval for an AI evaluation project: Replace binary scores with multi-dimensional rubrics for complex tasks.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `pytest evals/rubrics`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Replace binary scores with multi-dimensional rubrics for complex tasks.
- The verification command or evidence path succeeds: `pytest evals/rubrics`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/rubrics` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="prompt-version-registry"></a>
### Prompt Version Registry

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Bind prompt versions to eval results and deployment history.
- Verification: `pytest tests/prompt_registry`

```text
/goal
GOAL:
Complete Prompt Version Registry for an AI application runtime: Bind prompt versions to eval results and deployment history.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/prompt_registry`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Bind prompt versions to eval results and deployment history.
- The verification command or evidence path succeeds: `pytest tests/prompt_registry`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/prompt_registry` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="rag-chunking-experiment"></a>
### RAG Chunking Experiment

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Compare chunk size, overlap, and metadata on retrieval and answer quality.
- Verification: `pytest evals/rag_chunking`

```text
/goal
GOAL:
Complete RAG Chunking Experiment for an AI application runtime: Compare chunk size, overlap, and metadata on retrieval and answer quality.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest evals/rag_chunking`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Compare chunk size, overlap, and metadata on retrieval and answer quality.
- The verification command or evidence path succeeds: `pytest evals/rag_chunking`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/rag_chunking` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="vector-index-refresh"></a>
### Vector Index Refresh

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Verify document updates are indexed completely and can be rolled back.
- Verification: `pytest tests/index_refresh`

```text
/goal
GOAL:
Complete Vector Index Refresh for an AI application runtime: Verify document updates are indexed completely and can be rolled back.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/index_refresh`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify document updates are indexed completely and can be rolled back.
- The verification command or evidence path succeeds: `pytest tests/index_refresh`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/index_refresh` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="model-routing-policy"></a>
### Model Routing Policy

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Route by risk, cost, latency, and quality evidence.
- Verification: `pytest tests/model_routing`

```text
/goal
GOAL:
Complete Model Routing Policy for an AI application runtime: Route by risk, cost, latency, and quality evidence.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/model_routing`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Route by risk, cost, latency, and quality evidence.
- The verification command or evidence path succeeds: `pytest tests/model_routing`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/model_routing` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="llm-timeout-budget"></a>
### LLM Timeout Budget

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Define timeout, retry, fallback, and user-visible error behavior.
- Verification: `pytest tests/llm_timeouts`

```text
/goal
GOAL:
Complete LLM Timeout Budget for an AI application runtime: Define timeout, retry, fallback, and user-visible error behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/llm_timeouts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Define timeout, retry, fallback, and user-visible error behavior.
- The verification command or evidence path succeeds: `pytest tests/llm_timeouts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/llm_timeouts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="token-cost-attribution"></a>
### Token Cost Attribution

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Attribute model costs by user, feature, model, and request ID.
- Verification: `pytest tests/costs`

```text
/goal
GOAL:
Complete Token Cost Attribution for an AI application runtime: Attribute model costs by user, feature, model, and request ID.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/costs`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Attribute model costs by user, feature, model, and request ID.
- The verification command or evidence path succeeds: `pytest tests/costs`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/costs` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="prompt-injection-filter"></a>
### RAG Prompt Injection Filter

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Detect and isolate malicious instructions in retrieved documents.
- Verification: `pytest evals/prompt_injection`

```text
/goal
GOAL:
Complete RAG Prompt Injection Filter for an AI application runtime: Detect and isolate malicious instructions in retrieved documents.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest evals/prompt_injection`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Detect and isolate malicious instructions in retrieved documents.
- The verification command or evidence path succeeds: `pytest evals/prompt_injection`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest evals/prompt_injection` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="ai-output-schema-guard"></a>
### AI Output Schema Guard

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Validate structured AI output and fail or retry safely.
- Verification: `pytest tests/schema_guard`

```text
/goal
GOAL:
Complete AI Output Schema Guard for an AI application runtime: Validate structured AI output and fail or retry safely.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/schema_guard`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Validate structured AI output and fail or retry safely.
- The verification command or evidence path succeeds: `pytest tests/schema_guard`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/schema_guard` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="human-review-threshold"></a>
### Human Review Threshold

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Escalate high-risk AI outputs based on confidence and policy rules.
- Verification: `pytest tests/human_review`

```text
/goal
GOAL:
Complete Human Review Threshold for an AI application runtime: Escalate high-risk AI outputs based on confidence and policy rules.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/human_review`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Escalate high-risk AI outputs based on confidence and policy rules.
- The verification command or evidence path succeeds: `pytest tests/human_review`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/human_review` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="ai-observability-traces"></a>
### AI Observability Traces

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `seed`
- Intent: Trace prompts, retrieval, tools, models, scores, and request IDs.
- Verification: `pytest tests/tracing`

```text
/goal
GOAL:
Complete AI Observability Traces for an AI application runtime: Trace prompts, retrieval, tools, models, scores, and request IDs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `pytest tests/tracing`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Trace prompts, retrieval, tools, models, scores, and request IDs.
- The verification command or evidence path succeeds: `pytest tests/tracing`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/tracing` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-empty-states"></a>
### Empty State System

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Design real empty states for lists, search, permissions, and first use.
- Verification: `npm run test -- EmptyState`

```text
/goal
GOAL:
Complete Empty State System for a web frontend application: Design real empty states for lists, search, permissions, and first use.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npm run test -- EmptyState`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Design real empty states for lists, search, permissions, and first use.
- The verification command or evidence path succeeds: `npm run test -- EmptyState`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run test -- EmptyState` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-error-boundary"></a>
### Error Boundary Experience

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add recoverable page and component fallback UI for crashes.
- Verification: `npm test -- ErrorBoundary`

```text
/goal
GOAL:
Complete Error Boundary Experience for a web frontend application: Add recoverable page and component fallback UI for crashes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npm test -- ErrorBoundary`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Add recoverable page and component fallback UI for crashes.
- The verification command or evidence path succeeds: `npm test -- ErrorBoundary`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test -- ErrorBoundary` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-loading-skeletons"></a>
### Loading Skeletons

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Replace layout-shifting spinners with stable skeleton states.
- Verification: `npm run lighthouse`

```text
/goal
GOAL:
Complete Loading Skeletons for a web frontend application: Replace layout-shifting spinners with stable skeleton states.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npm run lighthouse`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Replace layout-shifting spinners with stable skeleton states.
- The verification command or evidence path succeeds: `npm run lighthouse`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-form-validation"></a>
### Form Validation

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Cover inline, submit, server error, and dirty-state validation.
- Verification: `npm test -- form`

```text
/goal
GOAL:
Complete Form Validation for a web frontend application: Cover inline, submit, server error, and dirty-state validation.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npm test -- form`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Cover inline, submit, server error, and dirty-state validation.
- The verification command or evidence path succeeds: `npm test -- form`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test -- form` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-table-density"></a>
### Data Table Density

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Improve columns, filters, sorting, pagination, and bulk actions.
- Verification: `npx playwright test table.spec.ts`

```text
/goal
GOAL:
Complete Data Table Density for a web frontend application: Improve columns, filters, sorting, pagination, and bulk actions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test table.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Improve columns, filters, sorting, pagination, and bulk actions.
- The verification command or evidence path succeeds: `npx playwright test table.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test table.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-command-palette"></a>
### Command Palette

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add a keyboard-first entry point for high-frequency actions.
- Verification: `npx playwright test command-palette.spec.ts`

```text
/goal
GOAL:
Complete Command Palette for a web frontend application: Add a keyboard-first entry point for high-frequency actions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test command-palette.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Add a keyboard-first entry point for high-frequency actions.
- The verification command or evidence path succeeds: `npx playwright test command-palette.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test command-palette.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-navigation-map"></a>
### Navigation Map

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Clarify primary navigation, breadcrumbs, and detail-page return paths.
- Verification: `npx playwright test navigation.spec.ts`

```text
/goal
GOAL:
Complete Navigation Map for a web frontend application: Clarify primary navigation, breadcrumbs, and detail-page return paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test navigation.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Clarify primary navigation, breadcrumbs, and detail-page return paths.
- The verification command or evidence path succeeds: `npx playwright test navigation.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test navigation.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-state-recovery"></a>
### State Recovery

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Restore filters and context after refresh, back, and deep links.
- Verification: `npx playwright test state-recovery.spec.ts`

```text
/goal
GOAL:
Complete State Recovery for a web frontend application: Restore filters and context after refresh, back, and deep links.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test state-recovery.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Restore filters and context after refresh, back, and deep links.
- The verification command or evidence path succeeds: `npx playwright test state-recovery.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test state-recovery.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-permission-ui"></a>
### Permission State UI

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Separate unauthenticated, unauthorized, and missing-resource states.
- Verification: `npx playwright test permissions.spec.ts`

```text
/goal
GOAL:
Complete Permission State UI for a web frontend application: Separate unauthenticated, unauthorized, and missing-resource states.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test permissions.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Separate unauthenticated, unauthorized, and missing-resource states.
- The verification command or evidence path succeeds: `npx playwright test permissions.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test permissions.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-bulk-actions"></a>
### Bulk Actions

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Handle selection, confirm, undo, partial failure, and feedback.
- Verification: `npx playwright test bulk-actions.spec.ts`

```text
/goal
GOAL:
Complete Bulk Actions for a web frontend application: Handle selection, confirm, undo, partial failure, and feedback.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test bulk-actions.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Handle selection, confirm, undo, partial failure, and feedback.
- The verification command or evidence path succeeds: `npx playwright test bulk-actions.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test bulk-actions.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-search-filter"></a>
### Search Filter Experience

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Unify search, filter chips, clear actions, and result counts.
- Verification: `npx playwright test search-filter.spec.ts`

```text
/goal
GOAL:
Complete Search Filter Experience for a web frontend application: Unify search, filter chips, clear actions, and result counts.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test search-filter.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Unify search, filter chips, clear actions, and result counts.
- The verification command or evidence path succeeds: `npx playwright test search-filter.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test search-filter.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="frontend-realtime-updates"></a>
### Realtime Update Prompts

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Handle background changes, conflicts, and refresh prompts.
- Verification: `npx playwright test realtime.spec.ts`

```text
/goal
GOAL:
Complete Realtime Update Prompts for a web frontend application: Handle background changes, conflicts, and refresh prompts.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test realtime.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Handle background changes, conflicts, and refresh prompts.
- The verification command or evidence path succeeds: `npx playwright test realtime.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test realtime.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-visual-hierarchy"></a>
### Visual Hierarchy Pass

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Reorder headings, metadata, primary actions, and secondary actions.
- Verification: `npx playwright test visual-hierarchy.spec.ts`

```text
/goal
GOAL:
Complete Visual Hierarchy Pass for a product UI codebase: Reorder headings, metadata, primary actions, and secondary actions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test visual-hierarchy.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Reorder headings, metadata, primary actions, and secondary actions.
- The verification command or evidence path succeeds: `npx playwright test visual-hierarchy.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test visual-hierarchy.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-token-audit"></a>
### Design Token Audit

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check colors, spacing, radii, and shadows against tokens.
- Verification: `npm run lint:styles`

```text
/goal
GOAL:
Complete Design Token Audit for a product UI codebase: Check colors, spacing, radii, and shadows against tokens.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npm run lint:styles`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Check colors, spacing, radii, and shadows against tokens.
- The verification command or evidence path succeeds: `npm run lint:styles`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lint:styles` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-component-variants"></a>
### Component Variant Matrix

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Complete button, input, card, and modal state coverage.
- Verification: `npm run storybook:test`

```text
/goal
GOAL:
Complete Component Variant Matrix for a product UI codebase: Complete button, input, card, and modal state coverage.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npm run storybook:test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Complete button, input, card, and modal state coverage.
- The verification command or evidence path succeeds: `npm run storybook:test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run storybook:test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-dashboard-layout"></a>
### Dashboard Layout Pass

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Make an operational dashboard easier to scan and compare.
- Verification: `npx playwright test dashboard.spec.ts`

```text
/goal
GOAL:
Complete Dashboard Layout Pass for a product UI codebase: Make an operational dashboard easier to scan and compare.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test dashboard.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Make an operational dashboard easier to scan and compare.
- The verification command or evidence path succeeds: `npx playwright test dashboard.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test dashboard.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-modal-discipline"></a>
### Modal Discipline

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Replace modal misuse with drawers, popovers, or pages where appropriate.
- Verification: `npx playwright test modal.spec.ts`

```text
/goal
GOAL:
Complete Modal Discipline for a product UI codebase: Replace modal misuse with drawers, popovers, or pages where appropriate.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test modal.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Replace modal misuse with drawers, popovers, or pages where appropriate.
- The verification command or evidence path succeeds: `npx playwright test modal.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test modal.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-iconography"></a>
### Iconography System

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Unify icon semantics for tools, statuses, and empty states.
- Verification: `npm run lint:icons`

```text
/goal
GOAL:
Complete Iconography System for a product UI codebase: Unify icon semantics for tools, statuses, and empty states.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npm run lint:icons`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Unify icon semantics for tools, statuses, and empty states.
- The verification command or evidence path succeeds: `npm run lint:icons`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lint:icons` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-color-contrast"></a>
### Color Contrast Pass

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Fix low contrast text, icons, and state colors.
- Verification: `npx axe http://localhost:3000`

```text
/goal
GOAL:
Complete Color Contrast Pass for a product UI codebase: Fix low contrast text, icons, and state colors.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx axe http://localhost:3000`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix low contrast text, icons, and state colors.
- The verification command or evidence path succeeds: `npx axe http://localhost:3000`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx axe http://localhost:3000` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-motion-rules"></a>
### Motion Rules

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define entry, exit, feedback, and reduced-motion behavior.
- Verification: `npx playwright test motion.spec.ts`

```text
/goal
GOAL:
Complete Motion Rules for a product UI codebase: Define entry, exit, feedback, and reduced-motion behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test motion.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Define entry, exit, feedback, and reduced-motion behavior.
- The verification command or evidence path succeeds: `npx playwright test motion.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test motion.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-responsive-grid"></a>
### Responsive Grid

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define breakpoints, columns, and fixed-format constraints.
- Verification: `npx playwright test responsive.spec.ts`

```text
/goal
GOAL:
Complete Responsive Grid for a product UI codebase: Define breakpoints, columns, and fixed-format constraints.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test responsive.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Define breakpoints, columns, and fixed-format constraints.
- The verification command or evidence path succeeds: `npx playwright test responsive.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test responsive.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-toolbar-usability"></a>
### Toolbar Usability

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Improve icon buttons, tooltips, grouping, and disabled states.
- Verification: `npx playwright test toolbar.spec.ts`

```text
/goal
GOAL:
Complete Toolbar Usability for a product UI codebase: Improve icon buttons, tooltips, grouping, and disabled states.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test toolbar.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Improve icon buttons, tooltips, grouping, and disabled states.
- The verification command or evidence path succeeds: `npx playwright test toolbar.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test toolbar.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-data-card-system"></a>
### Data Card System

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define metric cards with value, trend, anomaly, and source states.
- Verification: `npm run storybook:test`

```text
/goal
GOAL:
Complete Data Card System for a product UI codebase: Define metric cards with value, trend, anomaly, and source states.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npm run storybook:test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Define metric cards with value, trend, anomaly, and source states.
- The verification command or evidence path succeeds: `npm run storybook:test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run storybook:test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="design-brand-fit"></a>
### Brand Fit Pass

- Category: `design`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Align the interface language with the product's audience and use case.
- Verification: `npx playwright test brand.spec.ts`

```text
/goal
GOAL:
Complete Brand Fit Pass for a product UI codebase: Align the interface language with the product's audience and use case.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `npx playwright test brand.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Align the interface language with the product's audience and use case.
- The verification command or evidence path succeeds: `npx playwright test brand.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test brand.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-bottom-nav"></a>
### Mobile Bottom Navigation

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Design thumb-friendly mobile navigation for core paths.
- Verification: `npx playwright test --project=mobile navigation.spec.ts`

```text
/goal
GOAL:
Complete Mobile Bottom Navigation for a mobile or responsive application: Design thumb-friendly mobile navigation for core paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile navigation.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Design thumb-friendly mobile navigation for core paths.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile navigation.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile navigation.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-touch-targets"></a>
### Mobile Touch Targets

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Ensure buttons, checkboxes, and rows have usable tap areas.
- Verification: `npx playwright test --project=mobile touch.spec.ts`

```text
/goal
GOAL:
Complete Mobile Touch Targets for a mobile or responsive application: Ensure buttons, checkboxes, and rows have usable tap areas.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile touch.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Ensure buttons, checkboxes, and rows have usable tap areas.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile touch.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile touch.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-form-flow"></a>
### Mobile Form Flow

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Handle long forms, keyboard occlusion, and error positioning.
- Verification: `npx playwright test --project=mobile form.spec.ts`

```text
/goal
GOAL:
Complete Mobile Form Flow for a mobile or responsive application: Handle long forms, keyboard occlusion, and error positioning.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile form.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Handle long forms, keyboard occlusion, and error positioning.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile form.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile form.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-table-adaptation"></a>
### Mobile Table Adaptation

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Convert wide tables into cards, horizontal scroll, or drill-downs.
- Verification: `npx playwright test --project=mobile table.spec.ts`

```text
/goal
GOAL:
Complete Mobile Table Adaptation for a mobile or responsive application: Convert wide tables into cards, horizontal scroll, or drill-downs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile table.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Convert wide tables into cards, horizontal scroll, or drill-downs.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile table.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile table.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-filter-drawer"></a>
### Mobile Filter Drawer

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add mobile filters with apply, reset, count, and URL state.
- Verification: `npx playwright test --project=mobile filter.spec.ts`

```text
/goal
GOAL:
Complete Mobile Filter Drawer for a mobile or responsive application: Add mobile filters with apply, reset, count, and URL state.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile filter.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Add mobile filters with apply, reset, count, and URL state.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile filter.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile filter.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-offline-state"></a>
### Mobile Offline State

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Show offline, cached data, and retry paths clearly.
- Verification: `npx playwright test --project=mobile offline.spec.ts`

```text
/goal
GOAL:
Complete Mobile Offline State for a mobile or responsive application: Show offline, cached data, and retry paths clearly.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile offline.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Show offline, cached data, and retry paths clearly.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile offline.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile offline.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-image-performance"></a>
### Mobile Image Performance

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Optimize image sizes, lazy loading, placeholders, and formats.
- Verification: `npm run lighthouse:mobile`

```text
/goal
GOAL:
Complete Mobile Image Performance for a mobile or responsive application: Optimize image sizes, lazy loading, placeholders, and formats.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npm run lighthouse:mobile`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Optimize image sizes, lazy loading, placeholders, and formats.
- The verification command or evidence path succeeds: `npm run lighthouse:mobile`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse:mobile` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-safe-area"></a>
### Mobile Safe Area

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Handle iOS notch, bottom bars, and sticky actions.
- Verification: `npx playwright test --project=mobile safe-area.spec.ts`

```text
/goal
GOAL:
Complete Mobile Safe Area for a mobile or responsive application: Handle iOS notch, bottom bars, and sticky actions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile safe-area.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Handle iOS notch, bottom bars, and sticky actions.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile safe-area.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile safe-area.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-gesture-conflicts"></a>
### Mobile Gesture Conflicts

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Resolve conflicts between swipe, drag, and scroll interactions.
- Verification: `npx playwright test --project=mobile gestures.spec.ts`

```text
/goal
GOAL:
Complete Mobile Gesture Conflicts for a mobile or responsive application: Resolve conflicts between swipe, drag, and scroll interactions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile gestures.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Resolve conflicts between swipe, drag, and scroll interactions.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile gestures.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile gestures.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-login-flow"></a>
### Mobile Login Flow

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Improve magic link, OTP, password manager, and autofill behavior.
- Verification: `npx playwright test --project=mobile login.spec.ts`

```text
/goal
GOAL:
Complete Mobile Login Flow for a mobile or responsive application: Improve magic link, OTP, password manager, and autofill behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile login.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Improve magic link, OTP, password manager, and autofill behavior.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile login.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile login.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-onboarding"></a>
### Mobile Onboarding

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Create a short, skippable, restorable first-run path.
- Verification: `npx playwright test --project=mobile onboarding.spec.ts`

```text
/goal
GOAL:
Complete Mobile Onboarding for a mobile or responsive application: Create a short, skippable, restorable first-run path.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile onboarding.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Create a short, skippable, restorable first-run path.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile onboarding.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile onboarding.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="mobile-device-matrix"></a>
### Mobile Device Matrix

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Cover small screen, large screen, iOS, and Android key paths.
- Verification: `npx playwright test --project=mobile`

```text
/goal
GOAL:
Complete Mobile Device Matrix for a mobile or responsive application: Cover small screen, large screen, iOS, and Android key paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Cover small screen, large screen, iOS, and Android key paths.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-quickstart"></a>
### Quickstart

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Write the shortest fresh-clone path that runs successfully in five minutes.
- Verification: `markdownlint README.md`

```text
/goal
GOAL:
Complete Quickstart for a developer-facing documentation site or repository: Write the shortest fresh-clone path that runs successfully in five minutes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint README.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Write the shortest fresh-clone path that runs successfully in five minutes.
- The verification command or evidence path succeeds: `markdownlint README.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint README.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-install-troubleshooting"></a>
### Install Troubleshooting

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Document common install failures, causes, and fixes.
- Verification: `markdownlint docs`

```text
/goal
GOAL:
Complete Install Troubleshooting for a developer-facing documentation site or repository: Document common install failures, causes, and fixes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint docs`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Document common install failures, causes, and fixes.
- The verification command or evidence path succeeds: `markdownlint docs`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-api-examples"></a>
### API Examples

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add minimal request, response, and error examples for core APIs.
- Verification: `pytest -k docs_api_examples`

```text
/goal
GOAL:
Complete API Examples for a developer-facing documentation site or repository: Add minimal request, response, and error examples for core APIs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `pytest -k docs_api_examples`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Add minimal request, response, and error examples for core APIs.
- The verification command or evidence path succeeds: `pytest -k docs_api_examples`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k docs_api_examples` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-architecture-overview"></a>
### Architecture Overview

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Explain module boundaries, data flow, and explicit non-goals.
- Verification: `markdownlint docs/architecture.md`

```text
/goal
GOAL:
Complete Architecture Overview for a developer-facing documentation site or repository: Explain module boundaries, data flow, and explicit non-goals.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint docs/architecture.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Explain module boundaries, data flow, and explicit non-goals.
- The verification command or evidence path succeeds: `markdownlint docs/architecture.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/architecture.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-contribution-guide"></a>
### Contribution Guide

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Document development, testing, commit, and PR review rules.
- Verification: `markdownlint CONTRIBUTING.md`

```text
/goal
GOAL:
Complete Contribution Guide for a developer-facing documentation site or repository: Document development, testing, commit, and PR review rules.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint CONTRIBUTING.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Document development, testing, commit, and PR review rules.
- The verification command or evidence path succeeds: `markdownlint CONTRIBUTING.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint CONTRIBUTING.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-release-notes"></a>
### Release Notes

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Create user-facing change, migration, and breaking-change notes.
- Verification: `markdownlint CHANGELOG.md`

```text
/goal
GOAL:
Complete Release Notes for a developer-facing documentation site or repository: Create user-facing change, migration, and breaking-change notes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint CHANGELOG.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Create user-facing change, migration, and breaking-change notes.
- The verification command or evidence path succeeds: `markdownlint CHANGELOG.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint CHANGELOG.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-env-vars"></a>
### Environment Variables

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: List env names, defaults, requiredness, and safety notes.
- Verification: `pytest -k env_config`

```text
/goal
GOAL:
Complete Environment Variables for a developer-facing documentation site or repository: List env names, defaults, requiredness, and safety notes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `pytest -k env_config`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: List env names, defaults, requiredness, and safety notes.
- The verification command or evidence path succeeds: `pytest -k env_config`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k env_config` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-runbook"></a>
### Operator Runbook

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Document alerts, recovery, rollback, and data repair steps.
- Verification: `markdownlint docs/runbooks`

```text
/goal
GOAL:
Complete Operator Runbook for a developer-facing documentation site or repository: Document alerts, recovery, rollback, and data repair steps.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint docs/runbooks`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Document alerts, recovery, rollback, and data repair steps.
- The verification command or evidence path succeeds: `markdownlint docs/runbooks`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/runbooks` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-decision-records"></a>
### Architecture Decision Records

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add ADR templates and indexes for major technical decisions.
- Verification: `markdownlint docs/adr`

```text
/goal
GOAL:
Complete Architecture Decision Records for a developer-facing documentation site or repository: Add ADR templates and indexes for major technical decisions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint docs/adr`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Add ADR templates and indexes for major technical decisions.
- The verification command or evidence path succeeds: `markdownlint docs/adr`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/adr` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-glossary"></a>
### Glossary

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Unify product, engineering, and data-field terms.
- Verification: `markdownlint docs/glossary.md`

```text
/goal
GOAL:
Complete Glossary for a developer-facing documentation site or repository: Unify product, engineering, and data-field terms.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint docs/glossary.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Unify product, engineering, and data-field terms.
- The verification command or evidence path succeeds: `markdownlint docs/glossary.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/glossary.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-screenshot-docs"></a>
### Screenshot Docs

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add real screenshots and labels for UI workflows.
- Verification: `markdownlint docs`

```text
/goal
GOAL:
Complete Screenshot Docs for a developer-facing documentation site or repository: Add real screenshots and labels for UI workflows.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint docs`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Add real screenshots and labels for UI workflows.
- The verification command or evidence path succeeds: `markdownlint docs`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="docs-docs-lint"></a>
### Docs Lint Gate

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add link, spelling, and executable code block checks.
- Verification: `markdownlint . && lychee .`

```text
/goal
GOAL:
Complete Docs Lint Gate for a developer-facing documentation site or repository: Add link, spelling, and executable code block checks.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `markdownlint . && lychee .`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Add link, spelling, and executable code block checks.
- The verification command or evidence path succeeds: `markdownlint . && lychee .`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint . && lychee .` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-user-journeys"></a>
### User Journeys

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Map persona tasks into pages, events, and success states.
- Verification: `markdownlint docs/product`

```text
/goal
GOAL:
Complete User Journeys for a product planning and implementation repo: Map persona tasks into pages, events, and success states.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `markdownlint docs/product`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Map persona tasks into pages, events, and success states.
- The verification command or evidence path succeeds: `markdownlint docs/product`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/product` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-prd-skeleton"></a>
### PRD Skeleton

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Write goals, non-goals, constraints, and acceptance criteria.
- Verification: `markdownlint docs/prd.md`

```text
/goal
GOAL:
Complete PRD Skeleton for a product planning and implementation repo: Write goals, non-goals, constraints, and acceptance criteria.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `markdownlint docs/prd.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Write goals, non-goals, constraints, and acceptance criteria.
- The verification command or evidence path succeeds: `markdownlint docs/prd.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/prd.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-onboarding-metrics"></a>
### Onboarding Metrics

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define activation events, dropoff points, and dashboard queries.
- Verification: `pytest -k analytics_events`

```text
/goal
GOAL:
Complete Onboarding Metrics for a product planning and implementation repo: Define activation events, dropoff points, and dashboard queries.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `pytest -k analytics_events`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Define activation events, dropoff points, and dashboard queries.
- The verification command or evidence path succeeds: `pytest -k analytics_events`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k analytics_events` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-feature-prioritization"></a>
### Feature Prioritization

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Split MVP and later work by impact, cost, and risk.
- Verification: `markdownlint docs/roadmap.md`

```text
/goal
GOAL:
Complete Feature Prioritization for a product planning and implementation repo: Split MVP and later work by impact, cost, and risk.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `markdownlint docs/roadmap.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Split MVP and later work by impact, cost, and risk.
- The verification command or evidence path succeeds: `markdownlint docs/roadmap.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/roadmap.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-permission-model"></a>
### Permission Model

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Map roles, resources, actions, and UI visibility.
- Verification: `pytest -k permissions`

```text
/goal
GOAL:
Complete Permission Model for a product planning and implementation repo: Map roles, resources, actions, and UI visibility.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `pytest -k permissions`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Map roles, resources, actions, and UI visibility.
- The verification command or evidence path succeeds: `pytest -k permissions`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k permissions` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-notification-strategy"></a>
### Notification Strategy

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define triggers, channels, frequency, and unsubscribe behavior.
- Verification: `pytest -k notifications`

```text
/goal
GOAL:
Complete Notification Strategy for a product planning and implementation repo: Define triggers, channels, frequency, and unsubscribe behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `pytest -k notifications`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Define triggers, channels, frequency, and unsubscribe behavior.
- The verification command or evidence path succeeds: `pytest -k notifications`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k notifications` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-empty-data-policy"></a>
### Empty Data Policy

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Choose blank, sample data, import, or CTA by user state.
- Verification: `npx playwright test empty-data.spec.ts`

```text
/goal
GOAL:
Complete Empty Data Policy for a product planning and implementation repo: Choose blank, sample data, import, or CTA by user state.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `npx playwright test empty-data.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Choose blank, sample data, import, or CTA by user state.
- The verification command or evidence path succeeds: `npx playwright test empty-data.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test empty-data.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-upgrade-path"></a>
### Upgrade Path

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Design limits, paywalls, trials, and upgrade conversion paths.
- Verification: `pytest -k entitlement`

```text
/goal
GOAL:
Complete Upgrade Path for a product planning and implementation repo: Design limits, paywalls, trials, and upgrade conversion paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `pytest -k entitlement`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Design limits, paywalls, trials, and upgrade conversion paths.
- The verification command or evidence path succeeds: `pytest -k entitlement`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k entitlement` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-feedback-loop"></a>
### Feedback Loop

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Collect, classify, track, and close user feedback.
- Verification: `markdownlint docs/feedback.md`

```text
/goal
GOAL:
Complete Feedback Loop for a product planning and implementation repo: Collect, classify, track, and close user feedback.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `markdownlint docs/feedback.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Collect, classify, track, and close user feedback.
- The verification command or evidence path succeeds: `markdownlint docs/feedback.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/feedback.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-search-relevance"></a>
### Search Relevance

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define query handling, ranking, typo tolerance, and no-result behavior.
- Verification: `pytest -k search_relevance`

```text
/goal
GOAL:
Complete Search Relevance for a product planning and implementation repo: Define query handling, ranking, typo tolerance, and no-result behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `pytest -k search_relevance`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Define query handling, ranking, typo tolerance, and no-result behavior.
- The verification command or evidence path succeeds: `pytest -k search_relevance`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k search_relevance` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-admin-workflows"></a>
### Admin Workflows

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Design review, undo, audit log, and bulk moderation flows.
- Verification: `npx playwright test admin.spec.ts`

```text
/goal
GOAL:
Complete Admin Workflows for a product planning and implementation repo: Design review, undo, audit log, and bulk moderation flows.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `npx playwright test admin.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Design review, undo, audit log, and bulk moderation flows.
- The verification command or evidence path succeeds: `npx playwright test admin.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test admin.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="product-success-criteria"></a>
### Success Criteria

- Category: `product`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define quantitative and qualitative completion measures for a feature.
- Verification: `markdownlint docs/success.md`

```text
/goal
GOAL:
Complete Success Criteria for a product planning and implementation repo: Define quantitative and qualitative completion measures for a feature.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `markdownlint docs/success.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Define quantitative and qualitative completion measures for a feature.
- The verification command or evidence path succeeds: `markdownlint docs/success.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint docs/success.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-critical-paths"></a>
### Critical Path Tests

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Cover signup, create, edit, delete, export, and recovery flows.
- Verification: `npx playwright test critical-paths.spec.ts`

```text
/goal
GOAL:
Complete Critical Path Tests for a product with automated and manual QA coverage: Cover signup, create, edit, delete, export, and recovery flows.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `npx playwright test critical-paths.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Cover signup, create, edit, delete, export, and recovery flows.
- The verification command or evidence path succeeds: `npx playwright test critical-paths.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test critical-paths.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-regression-matrix"></a>
### Regression Matrix

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Build feature/browser/role/data-state regression coverage.
- Verification: `npx playwright test`

```text
/goal
GOAL:
Complete Regression Matrix for a product with automated and manual QA coverage: Build feature/browser/role/data-state regression coverage.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `npx playwright test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Build feature/browser/role/data-state regression coverage.
- The verification command or evidence path succeeds: `npx playwright test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-fixture-strategy"></a>
### Fixture Strategy

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Create deterministic seed, mock, factory, and cleanup patterns.
- Verification: `pytest -k fixtures`

```text
/goal
GOAL:
Complete Fixture Strategy for a product with automated and manual QA coverage: Create deterministic seed, mock, factory, and cleanup patterns.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `pytest -k fixtures`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Create deterministic seed, mock, factory, and cleanup patterns.
- The verification command or evidence path succeeds: `pytest -k fixtures`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k fixtures` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-visual-regression"></a>
### Visual Regression

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add screenshot diffs for critical pages with controlled thresholds.
- Verification: `npx playwright test visual.spec.ts`

```text
/goal
GOAL:
Complete Visual Regression for a product with automated and manual QA coverage: Add screenshot diffs for critical pages with controlled thresholds.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `npx playwright test visual.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Add screenshot diffs for critical pages with controlled thresholds.
- The verification command or evidence path succeeds: `npx playwright test visual.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test visual.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-api-contracts"></a>
### API Contracts

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Validate frontend/backend schema, error codes, and boundary values.
- Verification: `pytest -k contract`

```text
/goal
GOAL:
Complete API Contracts for a product with automated and manual QA coverage: Validate frontend/backend schema, error codes, and boundary values.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `pytest -k contract`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Validate frontend/backend schema, error codes, and boundary values.
- The verification command or evidence path succeeds: `pytest -k contract`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k contract` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-flaky-test-audit"></a>
### Flaky Test Audit

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Find unstable tests and fix waits, isolation, or fixtures.
- Verification: `pytest --count=20`

```text
/goal
GOAL:
Complete Flaky Test Audit for a product with automated and manual QA coverage: Find unstable tests and fix waits, isolation, or fixtures.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `pytest --count=20`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Find unstable tests and fix waits, isolation, or fixtures.
- The verification command or evidence path succeeds: `pytest --count=20`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest --count=20` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-error-injection"></a>
### Error Injection

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Simulate 500s, timeouts, network failure, and partial success.
- Verification: `npx playwright test error-injection.spec.ts`

```text
/goal
GOAL:
Complete Error Injection for a product with automated and manual QA coverage: Simulate 500s, timeouts, network failure, and partial success.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `npx playwright test error-injection.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Simulate 500s, timeouts, network failure, and partial success.
- The verification command or evidence path succeeds: `npx playwright test error-injection.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test error-injection.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-cross-browser"></a>
### Cross-Browser Coverage

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Run critical flows across Chromium, Firefox, and WebKit.
- Verification: `npx playwright test --project=chromium --project=firefox --project=webkit`

```text
/goal
GOAL:
Complete Cross-Browser Coverage for a product with automated and manual QA coverage: Run critical flows across Chromium, Firefox, and WebKit.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=chromium --project=firefox --project=webkit`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Run critical flows across Chromium, Firefox, and WebKit.
- The verification command or evidence path succeeds: `npx playwright test --project=chromium --project=firefox --project=webkit`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=chromium --project=firefox --project=webkit` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-release-smoke"></a>
### Release Smoke

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define the smallest pre-release verification checklist.
- Verification: `npm run smoke`

```text
/goal
GOAL:
Complete Release Smoke for a product with automated and manual QA coverage: Define the smallest pre-release verification checklist.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `npm run smoke`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Define the smallest pre-release verification checklist.
- The verification command or evidence path succeeds: `npm run smoke`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run smoke` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-data-migration"></a>
### Data Migration Test

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Verify counts, constraints, and rollback around data migration.
- Verification: `pytest -k migration`

```text
/goal
GOAL:
Complete Data Migration Test for a product with automated and manual QA coverage: Verify counts, constraints, and rollback around data migration.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `pytest -k migration`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify counts, constraints, and rollback around data migration.
- The verification command or evidence path succeeds: `pytest -k migration`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k migration` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-security-smoke"></a>
### Security Smoke

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check auth, permission bypass, and sensitive info leakage.
- Verification: `pytest -k security_smoke`

```text
/goal
GOAL:
Complete Security Smoke for a product with automated and manual QA coverage: Check auth, permission bypass, and sensitive info leakage.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `pytest -k security_smoke`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Check auth, permission bypass, and sensitive info leakage.
- The verification command or evidence path succeeds: `pytest -k security_smoke`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -k security_smoke` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qa-bug-repro-template"></a>
### Bug Reproduction Template

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Standardize environment, steps, expected, actual, and evidence.
- Verification: `markdownlint .github/ISSUE_TEMPLATE`

```text
/goal
GOAL:
Complete Bug Reproduction Template for a product with automated and manual QA coverage: Standardize environment, steps, expected, actual, and evidence.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `markdownlint .github/ISSUE_TEMPLATE`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Standardize environment, steps, expected, actual, and evidence.
- The verification command or evidence path succeeds: `markdownlint .github/ISSUE_TEMPLATE`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint .github/ISSUE_TEMPLATE` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-keyboard-nav"></a>
### Keyboard Navigation

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Ensure the whole app works with Tab, Enter, and Escape.
- Verification: `npx playwright test keyboard.spec.ts`

```text
/goal
GOAL:
Complete Keyboard Navigation for a web or mobile interface: Ensure the whole app works with Tab, Enter, and Escape.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx playwright test keyboard.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Ensure the whole app works with Tab, Enter, and Escape.
- The verification command or evidence path succeeds: `npx playwright test keyboard.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test keyboard.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-screen-reader"></a>
### Screen Reader Semantics

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check landmarks, labels, aria-live, and button names.
- Verification: `npx axe http://localhost:3000`

```text
/goal
GOAL:
Complete Screen Reader Semantics for a web or mobile interface: Check landmarks, labels, aria-live, and button names.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx axe http://localhost:3000`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Check landmarks, labels, aria-live, and button names.
- The verification command or evidence path succeeds: `npx axe http://localhost:3000`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx axe http://localhost:3000` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-focus-visible"></a>
### Focus Visible

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Give every interactive element a clear focus state.
- Verification: `npx playwright test focus.spec.ts`

```text
/goal
GOAL:
Complete Focus Visible for a web or mobile interface: Give every interactive element a clear focus state.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx playwright test focus.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Give every interactive element a clear focus state.
- The verification command or evidence path succeeds: `npx playwright test focus.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test focus.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-color-contrast"></a>
### Color Contrast

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Meet WCAG AA for text, icons, and state colors.
- Verification: `npx axe http://localhost:3000`

```text
/goal
GOAL:
Complete Color Contrast for a web or mobile interface: Meet WCAG AA for text, icons, and state colors.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx axe http://localhost:3000`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Meet WCAG AA for text, icons, and state colors.
- The verification command or evidence path succeeds: `npx axe http://localhost:3000`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx axe http://localhost:3000` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-form-errors"></a>
### Accessible Form Errors

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Associate errors with fields so screen readers announce them.
- Verification: `npx playwright test form-a11y.spec.ts`

```text
/goal
GOAL:
Complete Accessible Form Errors for a web or mobile interface: Associate errors with fields so screen readers announce them.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx playwright test form-a11y.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Associate errors with fields so screen readers announce them.
- The verification command or evidence path succeeds: `npx playwright test form-a11y.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test form-a11y.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-modal-trap"></a>
### Modal Focus Trap

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Focus opens, cycles, closes, and returns correctly.
- Verification: `npx playwright test modal-a11y.spec.ts`

```text
/goal
GOAL:
Complete Modal Focus Trap for a web or mobile interface: Focus opens, cycles, closes, and returns correctly.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx playwright test modal-a11y.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Focus opens, cycles, closes, and returns correctly.
- The verification command or evidence path succeeds: `npx playwright test modal-a11y.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test modal-a11y.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-reduced-motion"></a>
### Reduced Motion

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Respect prefers-reduced-motion for all nonessential motion.
- Verification: `npx playwright test reduced-motion.spec.ts`

```text
/goal
GOAL:
Complete Reduced Motion for a web or mobile interface: Respect prefers-reduced-motion for all nonessential motion.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx playwright test reduced-motion.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Respect prefers-reduced-motion for all nonessential motion.
- The verification command or evidence path succeeds: `npx playwright test reduced-motion.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test reduced-motion.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-alt-text"></a>
### Alt Text Audit

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Separate decorative, content, and product images.
- Verification: `npx axe http://localhost:3000`

```text
/goal
GOAL:
Complete Alt Text Audit for a web or mobile interface: Separate decorative, content, and product images.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx axe http://localhost:3000`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Separate decorative, content, and product images.
- The verification command or evidence path succeeds: `npx axe http://localhost:3000`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx axe http://localhost:3000` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-heading-order"></a>
### Heading Order

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Fix skipped headings and fake styled headings.
- Verification: `npx axe http://localhost:3000`

```text
/goal
GOAL:
Complete Heading Order for a web or mobile interface: Fix skipped headings and fake styled headings.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx axe http://localhost:3000`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix skipped headings and fake styled headings.
- The verification command or evidence path succeeds: `npx axe http://localhost:3000`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx axe http://localhost:3000` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-live-region"></a>
### Live Region Feedback

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Announce toasts, async completion, and errors accessibly.
- Verification: `npx playwright test live-region.spec.ts`

```text
/goal
GOAL:
Complete Live Region Feedback for a web or mobile interface: Announce toasts, async completion, and errors accessibly.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx playwright test live-region.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Announce toasts, async completion, and errors accessibly.
- The verification command or evidence path succeeds: `npx playwright test live-region.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test live-region.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-touch-a11y"></a>
### Touch Accessibility

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check tap targets, zoom, and orientation on mobile.
- Verification: `npx playwright test --project=mobile a11y.spec.ts`

```text
/goal
GOAL:
Complete Touch Accessibility for a web or mobile interface: Check tap targets, zoom, and orientation on mobile.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx playwright test --project=mobile a11y.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Check tap targets, zoom, and orientation on mobile.
- The verification command or evidence path succeeds: `npx playwright test --project=mobile a11y.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test --project=mobile a11y.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="accessibility-audit-report"></a>
### Accessibility Audit Report

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Produce prioritized issues, impact, fixes, and acceptance checks.
- Verification: `npx axe http://localhost:3000 --save results.json`

```text
/goal
GOAL:
Complete Accessibility Audit Report for a web or mobile interface: Produce prioritized issues, impact, fixes, and acceptance checks.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `npx axe http://localhost:3000 --save results.json`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Produce prioritized issues, impact, fixes, and acceptance checks.
- The verification command or evidence path succeeds: `npx axe http://localhost:3000 --save results.json`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx axe http://localhost:3000 --save results.json` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-lcp"></a>
### LCP Optimization

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Find and optimize the largest contentful paint element.
- Verification: `npm run lighthouse`

```text
/goal
GOAL:
Complete LCP Optimization for a web application with measurable performance goals: Find and optimize the largest contentful paint element.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run lighthouse`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Find and optimize the largest contentful paint element.
- The verification command or evidence path succeeds: `npm run lighthouse`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-cls"></a>
### CLS Fix

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Reserve space for images, ads, and dynamic content.
- Verification: `npm run lighthouse`

```text
/goal
GOAL:
Complete CLS Fix for a web application with measurable performance goals: Reserve space for images, ads, and dynamic content.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run lighthouse`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Reserve space for images, ads, and dynamic content.
- The verification command or evidence path succeeds: `npm run lighthouse`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-inp"></a>
### INP Optimization

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Reduce long tasks and blocking interaction handlers.
- Verification: `npm run trace`

```text
/goal
GOAL:
Complete INP Optimization for a web application with measurable performance goals: Reduce long tasks and blocking interaction handlers.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run trace`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Reduce long tasks and blocking interaction handlers.
- The verification command or evidence path succeeds: `npm run trace`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run trace` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-bundle-budget"></a>
### Bundle Budget

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Set route and dependency size budgets in CI.
- Verification: `npm run analyze`

```text
/goal
GOAL:
Complete Bundle Budget for a web application with measurable performance goals: Set route and dependency size budgets in CI.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run analyze`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Set route and dependency size budgets in CI.
- The verification command or evidence path succeeds: `npm run analyze`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run analyze` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-code-splitting"></a>
### Code Splitting

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Lazy-load low-frequency routes, charts, and editors.
- Verification: `npm run analyze`

```text
/goal
GOAL:
Complete Code Splitting for a web application with measurable performance goals: Lazy-load low-frequency routes, charts, and editors.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run analyze`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Lazy-load low-frequency routes, charts, and editors.
- The verification command or evidence path succeeds: `npm run analyze`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run analyze` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-image-pipeline"></a>
### Image Pipeline

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Use srcset, modern formats, lazy loading, and cache headers.
- Verification: `npm run lighthouse`

```text
/goal
GOAL:
Complete Image Pipeline for a web application with measurable performance goals: Use srcset, modern formats, lazy loading, and cache headers.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run lighthouse`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Use srcset, modern formats, lazy loading, and cache headers.
- The verification command or evidence path succeeds: `npm run lighthouse`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-font-loading"></a>
### Font Loading

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Optimize font-display, subsets, and preload hints.
- Verification: `npm run lighthouse`

```text
/goal
GOAL:
Complete Font Loading for a web application with measurable performance goals: Optimize font-display, subsets, and preload hints.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run lighthouse`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Optimize font-display, subsets, and preload hints.
- The verification command or evidence path succeeds: `npm run lighthouse`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-api-waterfall"></a>
### API Waterfall

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Remove serial requests and prefetch critical data.
- Verification: `npx playwright test performance.spec.ts`

```text
/goal
GOAL:
Complete API Waterfall for a web application with measurable performance goals: Remove serial requests and prefetch critical data.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npx playwright test performance.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Remove serial requests and prefetch critical data.
- The verification command or evidence path succeeds: `npx playwright test performance.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test performance.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-cache-strategy"></a>
### Cache Strategy

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Define browser, CDN, and service-worker cache boundaries.
- Verification: `npx playwright test cache.spec.ts`

```text
/goal
GOAL:
Complete Cache Strategy for a web application with measurable performance goals: Define browser, CDN, and service-worker cache boundaries.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npx playwright test cache.spec.ts`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Define browser, CDN, and service-worker cache boundaries.
- The verification command or evidence path succeeds: `npx playwright test cache.spec.ts`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test cache.spec.ts` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-memory-leaks"></a>
### Memory Leak Audit

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check long sessions, lists, subscriptions, and charts for leaks.
- Verification: `npm run test:memory`

```text
/goal
GOAL:
Complete Memory Leak Audit for a web application with measurable performance goals: Check long sessions, lists, subscriptions, and charts for leaks.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run test:memory`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Check long sessions, lists, subscriptions, and charts for leaks.
- The verification command or evidence path succeeds: `npm run test:memory`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run test:memory` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-render-count"></a>
### Render Count Audit

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Find unnecessary React renders and expensive selectors.
- Verification: `npm run profile`

```text
/goal
GOAL:
Complete Render Count Audit for a web application with measurable performance goals: Find unnecessary React renders and expensive selectors.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run profile`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Find unnecessary React renders and expensive selectors.
- The verification command or evidence path succeeds: `npm run profile`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run profile` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="performance-ci-gate"></a>
### Performance CI Gate

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Add Lighthouse or trace thresholds to CI.
- Verification: `npm run lighthouse:ci`

```text
/goal
GOAL:
Complete Performance CI Gate for a web application with measurable performance goals: Add Lighthouse or trace thresholds to CI.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run lighthouse:ci`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Add Lighthouse or trace thresholds to CI.
- The verification command or evidence path succeeds: `npm run lighthouse:ci`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse:ci` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-meta-prompt-writer"></a>
### Goal Prompt Writer

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Ask the agent to inspect a repo and write a precise goal prompt before execution.
- Verification: `markdownlint generated-goal.md`

```text
/goal
GOAL:
Complete Goal Prompt Writer for a coding-agent workflow repository: Ask the agent to inspect a repo and write a precise goal prompt before execution.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `markdownlint generated-goal.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Ask the agent to inspect a repo and write a precise goal prompt before execution.
- The verification command or evidence path succeeds: `markdownlint generated-goal.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `markdownlint generated-goal.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-continuation-audit"></a>
### Goal Continuation Audit

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `seed`
- Intent: Check that a long-running goal keeps its done_when and verification contract after compaction.
- Verification: `rg -e "DONE WHEN" -e "VERIFY" -e "STOP RULES" progress-log.md`

```text
/goal
GOAL:
Complete Goal Continuation Audit for a coding-agent workflow repository: Check that a long-running goal keeps its done_when and verification contract after compaction.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `rg -e "DONE WHEN" -e "VERIFY" -e "STOP RULES" progress-log.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Check that a long-running goal keeps its done_when and verification contract after compaction.
- The verification command or evidence path succeeds: `rg -e "DONE WHEN" -e "VERIFY" -e "STOP RULES" progress-log.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `rg -e "DONE WHEN" -e "VERIFY" -e "STOP RULES" progress-log.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="codex-verifiable-end-state"></a>
### Verifiable End-State Contract

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Complete one objective only when a verifiable end state is met.
- Verification: `manual status plus repo-local verification`
- Source: [OpenAI Codex docs](https://developers.openai.com/codex/use-cases/follow-goals)

```text
/goal
GOAL:
Complete Verifiable End-State Contract for a coding-agent workflow repository: Complete one objective only when a verifiable end state is met.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `manual status plus repo-local verification`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Complete one objective only when a verifiable end state is met.
- The verification command or evidence path succeeds: `manual status plus repo-local verification`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `manual status plus repo-local verification` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="codex-visual-migration-playwright"></a>
### Visual Migration With Playwright

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Migrate a project while preserving screen output and checking it with Playwright.
- Verification: `npx playwright test`
- Source: [OpenAI Codex docs](https://developers.openai.com/codex/use-cases/follow-goals)

```text
/goal
GOAL:
Complete Visual Migration With Playwright for a migration project: Migrate a project while preserving screen output and checking it with Playwright.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `npx playwright test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Migrate a project while preserving screen output and checking it with Playwright.
- The verification command or evidence path succeeds: `npx playwright test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="codex-plan-milestone-prototype"></a>
### PLAN.md Milestone Prototype

- Category: `prototype`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Implement a PLAN.md-driven prototype with tests at each milestone and browser verification.
- Verification: `npx playwright test`
- Source: [OpenAI Codex docs](https://developers.openai.com/codex/use-cases/follow-goals)

```text
/goal
GOAL:
Complete PLAN.md Milestone Prototype for a prototype project: Implement a PLAN.md-driven prototype with tests at each milestone and browser verification.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PLAN.md, milestones, app code, tests, browser checks, and demo notes.
- Establish a baseline by running or locating evidence for: `npx playwright test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Follow the stated PLAN.md or acceptance criteria instead of adding unrequested features.
- Keep the prototype runnable and demonstrable at every completed milestone.

DONE WHEN:
- The implementation or documentation directly satisfies: Implement a PLAN.md-driven prototype with tests at each milestone and browser verification.
- The verification command or evidence path succeeds: `npx playwright test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npx playwright test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="codex-eval-prompt-optimization"></a>
### Eval-Driven Prompt Optimization

- Category: `prompt-optimization`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Optimize prompts against an eval suite until the target score or pass rate is reached.
- Verification: `python -m pytest evals`
- Source: [OpenAI Codex docs](https://developers.openai.com/codex/use-cases/follow-goals)

```text
/goal
GOAL:
Complete Eval-Driven Prompt Optimization for an eval-backed prompt project: Optimize prompts against an eval suite until the target score or pass rate is reached.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompt files, eval cases, scoring reports, regressions, and failure examples.
- Establish a baseline by running or locating evidence for: `python -m pytest evals`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete, weaken, or cherry-pick eval cases to improve the score.
- Report representative failures as well as the final score.

DONE WHEN:
- The implementation or documentation directly satisfies: Optimize prompts against an eval suite until the target score or pass rate is reached.
- The verification command or evidence path succeeds: `python -m pytest evals`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `python -m pytest evals` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-auth-tests-lint"></a>
### Auth Tests And Lint Clean

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Keep working until auth tests pass and the lint step is clean.
- Verification: `npm test -- test/auth && npm run lint`
- Source: [Claude Code docs](https://code.claude.com/docs/en/goal)

```text
/goal
GOAL:
Complete Auth Tests And Lint Clean for a project with failing or missing verification gates: Keep working until auth tests pass and the lint step is clean.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `npm test -- test/auth && npm run lint`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Keep working until auth tests pass and the lint step is clean.
- The verification command or evidence path succeeds: `npm test -- test/auth && npm run lint`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test -- test/auth && npm run lint` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-weekly-changelog"></a>
### Weekly Changelog Coverage

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Ensure CHANGELOG.md includes an entry for every PR merged this week.
- Verification: `git log --since='7 days ago' --merges && rg '^-' CHANGELOG.md`
- Source: [Claude Code docs](https://code.claude.com/docs/en/goal)

```text
/goal
GOAL:
Complete Weekly Changelog Coverage for a developer-facing documentation site or repository: Ensure CHANGELOG.md includes an entry for every PR merged this week.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `git log --since='7 days ago' --merges && rg '^-' CHANGELOG.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Ensure CHANGELOG.md includes an entry for every PR merged this week.
- The verification command or evidence path succeeds: `git log --since='7 days ago' --merges && rg '^-' CHANGELOG.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `git log --since='7 days ago' --merges && rg '^-' CHANGELOG.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="hermes-ruff-src-clean"></a>
### Ruff Clean Source Tree

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Fix every lint error in src and prove ruff passes.
- Verification: `ruff check src/`
- Source: [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)

```text
/goal
GOAL:
Complete Ruff Clean Source Tree for a project with failing or missing verification gates: Fix every lint error in src and prove ruff passes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `ruff check src/`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix every lint error in src and prove ruff passes.
- The verification command or evidence path succeeds: `ruff check src/`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `ruff check src/` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="hermes-feature-port-ci-green"></a>
### Feature Port With CI Green

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Port a feature from another repo, include tests, and get CI green.
- Verification: `pytest && npm test`
- Source: [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)

```text
/goal
GOAL:
Complete Feature Port With CI Green for a migration project: Port a feature from another repo, include tests, and get CI green.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `pytest && npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Port a feature from another repo, include tests, and get CI green.
- The verification command or evidence path succeeds: `pytest && npm test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest && npm test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="hermes-session-drift-report"></a>
### Session Drift Report

- Category: `investigation`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Investigate session ID drift during mid-run compression and write a report.
- Verification: `test -f reports/session-drift.md`
- Source: [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)

```text
/goal
GOAL:
Complete Session Drift Report for an investigation task: Investigate session ID drift during mid-run compression and write a report.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect logs, traces, reproduction notes, source paths, and the final report.
- Establish a baseline by running or locating evidence for: `test -f reports/session-drift.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Separate observed evidence from hypotheses.
- Do not patch production code until the root cause is reproduced or strongly evidenced.

DONE WHEN:
- The implementation or documentation directly satisfies: Investigate session ID drift during mid-run compression and write a report.
- The verification command or evidence path succeeds: `test -f reports/session-drift.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `test -f reports/session-drift.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="hermes-exif-rename-cli"></a>
### EXIF Rename CLI

- Category: `cli`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Build a small CLI that renames photos by EXIF date and test it on a photos folder.
- Verification: `pytest tests/cli && ./rename-exif photos/ --dry-run`
- Source: [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)

```text
/goal
GOAL:
Complete EXIF Rename CLI for a command-line tool: Build a small CLI that renames photos by EXIF date and test it on a photos folder.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect CLI entrypoints, argument parsing, filesystem behavior, dry-run mode, and fixtures.
- Establish a baseline by running or locating evidence for: `pytest tests/cli && ./rename-exif photos/ --dry-run`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not perform destructive filesystem operations without a dry-run or explicit confirmation.
- Keep command output deterministic enough for tests.

DONE WHEN:
- The implementation or documentation directly satisfies: Build a small CLI that renames photos by EXIF date and test it on a photos folder.
- The verification command or evidence path succeeds: `pytest tests/cli && ./rename-exif photos/ --dry-run`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest tests/cli && ./rename-exif photos/ --dry-run` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="hermes-four-files-walkthrough"></a>
### Four Files Walkthrough

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Create four note files across turns and verify each contains its number.
- Verification: `for i in 1 2 3 4; do test "$(cat /tmp/note_$i.txt)" = "$i"; done`
- Source: [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)

```text
/goal
GOAL:
Complete Four Files Walkthrough for a coding-agent workflow repository: Create four note files across turns and verify each contains its number.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `for i in 1 2 3 4; do test "$(cat /tmp/note_$i.txt)" = "$i"; done`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Create four note files across turns and verify each contains its number.
- The verification command or evidence path succeeds: `for i in 1 2 3 4; do test "$(cat /tmp/note_$i.txt)" = "$i"; done`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `for i in 1 2 3 4; do test "$(cat /tmp/note_$i.txt)" = "$i"; done` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="explainx-typescript-eslint-coverage"></a>
### TypeScript ESLint Coverage Gate

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold.
- Verification: `npm run typecheck && npm test && npm run lint && npm run coverage`
- Source: [ExplainX blog](https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026)

```text
/goal
GOAL:
Complete TypeScript ESLint Coverage Gate for a project with failing or missing verification gates: Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `npm run typecheck && npm test && npm run lint && npm run coverage`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold.
- The verification command or evidence path succeeds: `npm run typecheck && npm test && npm run lint && npm run coverage`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run typecheck && npm test && npm run lint && npm run coverage` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="explainx-auth-di-refactor"></a>
### Auth Dependency Injection Refactor

- Category: `refactor`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Refactor auth code to dependency injection while preserving tests, coverage, and public API.
- Verification: `npm test -- auth && npm run coverage`
- Source: [ExplainX blog](https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026)

```text
/goal
GOAL:
Complete Auth Dependency Injection Refactor for a refactoring task: Refactor auth code to dependency injection while preserving tests, coverage, and public API.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect the target module, call sites, public API, tests, and compatibility notes.
- Establish a baseline by running or locating evidence for: `npm test -- auth && npm run coverage`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change public APIs, data formats, or user-visible behavior unless the goal requires it.
- Keep behavior characterization tests before large internal changes.

DONE WHEN:
- The implementation or documentation directly satisfies: Refactor auth code to dependency injection while preserving tests, coverage, and public API.
- The verification command or evidence path succeeds: `npm test -- auth && npm run coverage`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test -- auth && npm run coverage` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="explainx-npm-audit-clean"></a>
### NPM Audit Clean Remediation

- Category: `security-ops`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Patch npm audit vulnerabilities without breaking tests or public APIs.
- Verification: `npm audit && npm test`
- Source: [ExplainX blog](https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026)

```text
/goal
GOAL:
Complete NPM Audit Clean Remediation for a production operations environment: Patch npm audit vulnerabilities without breaking tests or public APIs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow permissions, cloud IAM, release artifacts, and audit evidence.
- Establish a baseline by running or locating evidence for: `npm audit && npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not print, copy, rotate, or exfiltrate real secrets.
- Do not widen production permissions without a documented least-privilege reason.

DONE WHEN:
- The implementation or documentation directly satisfies: Patch npm audit vulnerabilities without breaking tests or public APIs.
- The verification command or evidence path succeeds: `npm audit && npm test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm audit && npm test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="explainx-lighthouse-core-web-vitals"></a>
### Lighthouse And Core Web Vitals Gate

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions.
- Verification: `npm run lighthouse`
- Source: [ExplainX blog](https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026)

```text
/goal
GOAL:
Complete Lighthouse And Core Web Vitals Gate for a web application with measurable performance goals: Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run lighthouse`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions.
- The verification command or evidence path succeeds: `npm run lighthouse`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run lighthouse` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qiita-vue2-vue3-visual-unit"></a>
### Vue 2 To Vue 3 Visual And Unit Gate

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Migrate listed Vue screens and stop only when visual and unit tests pass.
- Verification: `pnpm test:visual && pnpm test:unit`
- Source: [Qiita article](https://qiita.com/y-morimatsu/items/a314e5bbfdc83616d3ae)

```text
/goal
GOAL:
Complete Vue 2 To Vue 3 Visual And Unit Gate for a migration project: Migrate listed Vue screens and stop only when visual and unit tests pass.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `pnpm test:visual && pnpm test:unit`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Migrate listed Vue screens and stop only when visual and unit tests pass.
- The verification command or evidence path succeeds: `pnpm test:visual && pnpm test:unit`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pnpm test:visual && pnpm test:unit` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qiita-canvas-puzzle-plan"></a>
### Canvas Puzzle PLAN.md Prototype

- Category: `prototype`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes.
- Verification: `pnpm e2e`
- Source: [Qiita article](https://qiita.com/y-morimatsu/items/a314e5bbfdc83616d3ae)

```text
/goal
GOAL:
Complete Canvas Puzzle PLAN.md Prototype for a prototype project: Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PLAN.md, milestones, app code, tests, browser checks, and demo notes.
- Establish a baseline by running or locating evidence for: `pnpm e2e`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Follow the stated PLAN.md or acceptance criteria instead of adding unrequested features.
- Keep the prototype runnable and demonstrable at every completed milestone.

DONE WHEN:
- The implementation or documentation directly satisfies: Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes.
- The verification command or evidence path succeeds: `pnpm e2e`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pnpm e2e` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="qiita-router-eval-score"></a>
### Router Prompt Eval Score

- Category: `prompt-optimization`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Improve a router prompt against an eval directory until the result score reaches a target.
- Verification: `python -m pytest evals/router`
- Source: [Qiita article](https://qiita.com/y-morimatsu/items/a314e5bbfdc83616d3ae)

```text
/goal
GOAL:
Complete Router Prompt Eval Score for an eval-backed prompt project: Improve a router prompt against an eval directory until the result score reaches a target.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompt files, eval cases, scoring reports, regressions, and failure examples.
- Establish a baseline by running or locating evidence for: `python -m pytest evals/router`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete, weaken, or cherry-pick eval cases to improve the score.
- Report representative failures as well as the final score.

DONE WHEN:
- The implementation or documentation directly satisfies: Improve a router prompt against an eval directory until the result score reaches a target.
- The verification command or evidence path succeeds: `python -m pytest evals/router`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `python -m pytest evals/router` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

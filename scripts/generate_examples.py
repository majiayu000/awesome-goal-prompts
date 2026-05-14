#!/usr/bin/env python3
"""Generate the curated `/goal` example catalog.

The source list is intentionally compact. The generated Markdown and JSON are
the published artifacts people read or consume.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


RAW_ENTRIES = """
api-contract-drift-audit|backend-api|API Contract Drift Audit|Compare OpenAPI, implementation, and tests to find field or status-code drift.|npx openapi-diff old.yaml new.yaml && pytest tests/api
idempotent-create-endpoint|backend-api|Idempotent Create Endpoint|Add idempotency keys and replay-safe semantics to a create endpoint.|pytest -k idempotency
api-error-taxonomy|backend-api|API Error Taxonomy|Unify HTTP status codes, machine error codes, user messages, and logs.|pytest -k error_response
pagination-consistency|backend-api|Pagination Consistency|Fix cursor or offset pagination so rows are not skipped, duplicated, or reordered.|pytest -k pagination
request-validation-boundary|backend-api|Request Validation Boundary|Move input validation to the API boundary and reject unknown fields.|pytest -k validation
api-rate-limit-policy|backend-api|API Rate Limit Policy|Implement rate limit behavior, headers, and over-limit responses for critical routes.|k6 run rate_limit.js
webhook-retry-contract|backend-api|Webhook Retry Contract|Define webhook signature verification, retry, dedupe, and failure observability.|pytest -k webhook
backward-compatible-response|backend-api|Backward-Compatible Response|Add response fields without breaking old clients and document removal paths.|pytest -k contract
grpc-timeout-propagation|backend-api|gRPC Timeout Propagation|Propagate deadlines across service calls and cancel work correctly.|go test ./...
async-job-state-machine|backend-api|Async Job State Machine|Make async job transitions explicit and tested across pending/running/succeeded/failed/canceled.|pytest -k job_state
authz-resource-scope|backend-api|Resource-Level Authorization|Prevent logged-in users from accessing resources they do not own.|pytest -k authz
api-versioning-plan|backend-api|API Versioning Plan|Create a v1/v2 coexistence plan with deprecation headers and migration tests.|pytest -k api_version
db-migration-safety|backend-data|Database Migration Safety|Review a migration for rollback, online execution, and lock risk.|npm run migrate:dry-run
transaction-boundary-audit|backend-data|Transaction Boundary Audit|Find missing or oversized transactions in multi-table write paths.|pytest -k transaction
cache-invalidation-map|backend-data|Cache Invalidation Map|Map write paths to cache keys and fix stale reads.|pytest -k cache
n-plus-one-query-fix|backend-data|N+1 Query Fix|Reduce list endpoint query count with batching or preloading.|pytest -k query_count
optimistic-locking-rollout|backend-data|Optimistic Locking Rollout|Add version checks and conflict responses for concurrent edits.|pytest -k optimistic_lock
soft-delete-integrity|backend-data|Soft Delete Integrity|Make queries, unique indexes, and restore flows respect soft deletion.|pytest -k soft_delete
db-index-regression|backend-data|Index Regression Check|Add or adjust indexes and prove read gains do not create unacceptable write cost.|pytest -k slow_query
outbox-pattern-adoption|backend-data|Outbox Reliable Events|Use an outbox table to prevent lost events after successful database commits.|pytest -k outbox
read-replica-lag-guard|backend-data|Read Replica Lag Guard|Prevent write-after-read paths from hitting stale replicas.|pytest -k replica_lag
schema-drift-detector|backend-data|Schema Drift Detector|Compare ORM models, migrations, and the live database schema.|prisma migrate diff
ci-flaky-test-triage|devops-ci|CI Flaky Test Triage|Identify flaky tests, separate real failures, and fix unstable waits or fixtures.|gh run view --log
build-cache-correctness|devops-ci|Build Cache Correctness|Check whether CI cache keys cause stale dependencies or cross-branch pollution.|npm ci && npm test
dependency-update-gate|devops-ci|Dependency Update Gate|Add dependency upgrade checks for tests, licenses, and vulnerabilities.|npm audit && npm test
monorepo-affected-tests|devops-ci|Monorepo Affected Tests|Run only affected tests without missing cross-package contracts.|nx affected:test
release-note-from-diff|devops-ci|Release Notes From Diff|Generate user-facing release notes from commits, PR labels, and breaking changes.|git log --oneline last..HEAD
artifact-provenance|devops-ci|Artifact Provenance|Trace a package or image back to the commit and workflow that produced it.|gh run view
ci-permission-minimize|devops-ci|CI Permission Minimization|Tighten GitHub Actions token permissions without breaking workflows.|gh workflow run ci.yml
branch-protection-audit|devops-ci|Branch Protection Audit|Audit required checks, reviews, linear history, and admin bypasses.|gh api repos/OWNER/REPO/branches/main/protection
release-rollback-drill|devops-ci|Release Rollback Drill|Create and test a rollback path for the latest release.|npm run smoke
semantic-version-check|devops-ci|Semantic Version Check|Infer the correct semver bump from API, behavior, and changelog diffs.|npm test
docker-image-slimming|devops-runtime|Docker Image Slimming|Reduce image size while keeping runtime dependencies and security scans green.|docker build . && trivy image IMAGE
k8s-readiness-liveness|devops-runtime|Kubernetes Probe Repair|Separate startup, readiness, and liveness probes to avoid bad restarts.|kubectl describe pod
terraform-plan-review|devops-runtime|Terraform Plan Review|Review infrastructure changes for deletes, replacements, and permission expansion.|terraform plan -out=tfplan
helm-values-drift|devops-runtime|Helm Values Drift|Compare environment values to find hidden staging/prod differences.|helm diff upgrade
autoscaling-thresholds|devops-runtime|Autoscaling Thresholds|Tune HPA or worker scaling thresholds against real load and queue depth.|kubectl get hpa
runtime-config-validation|devops-runtime|Runtime Config Validation|Fail startup on missing or invalid environment and config values.|docker run --env-file .env.example IMAGE
zero-downtime-migration|devops-runtime|Zero-Downtime Migration|Plan and verify expand-migrate-contract deployment steps.|npm run smoke
observability-minimum|devops-runtime|Observability Minimum|Add logs, metrics, traces, and alerts for a service's critical paths.|npm test && curl localhost:PORT/metrics
incident-runbook-gap|devops-runtime|Incident Runbook Gap|Turn a recent incident timeline into missing runbook and alert updates.|markdownlint docs/runbooks
queue-backpressure|devops-runtime|Queue Backpressure|Protect databases and external APIs when worker queues build up.|pytest -k backpressure
sql-injection-audit|security-appsec|SQL Injection Audit|Replace SQL string concatenation with parameterized queries and tests.|pytest -k injection
command-injection-audit|security-appsec|Command Injection Audit|Replace shell string execution with argument arrays and validation.|pytest -k command_injection
ssrf-defense-review|security-appsec|SSRF Defense Review|Add URL allowlists and DNS/IP checks for fetch or callback features.|pytest -k ssrf
xss-output-encoding|security-appsec|XSS Output Encoding|Audit HTML and Markdown rendering for unsafe sinks and missing encoding.|npm test -- xss
csrf-sensitive-action|security-appsec|CSRF Sensitive Action|Protect cookie-authenticated writes from cross-site requests.|pytest -k csrf
auth-bypass-route-map|security-appsec|Auth Bypass Route Map|Enumerate routes and verify unauthenticated and unauthorized behavior.|pytest -k auth
file-upload-security|security-appsec|File Upload Security|Validate MIME, extension, size, scanning, and storage isolation.|pytest -k upload_security
tenant-isolation-test|security-appsec|Tenant Isolation Test|Verify tenant IDs are enforced in queries, caches, and background jobs.|pytest -k tenant
replay-attack-defense|security-appsec|Replay Attack Defense|Add nonce, timestamp, and expiration checks to signed requests.|pytest -k replay
insecure-direct-object-ref|security-appsec|IDOR Audit|Verify direct object ID access always checks ownership or scope.|pytest -k idor
secret-scan-baseline|security-ops|Secret Scan Baseline|Add secret scanning and triage historical findings safely.|gitleaks detect
iam-least-privilege|security-ops|IAM Least Privilege|Reduce cloud permissions to observed API usage and documented needs.|terraform plan
github-actions-supply-chain|security-ops|GitHub Actions Supply Chain|Pin third-party actions and review workflow permissions.|rg "uses:" .github/workflows
container-vuln-triage|security-ops|Container Vulnerability Triage|Prioritize image CVEs by exploitability and runtime exposure.|trivy image IMAGE
audit-log-coverage|security-ops|Audit Log Coverage|Add audit logs for login, permission changes, and sensitive data access.|pytest -k audit_log
secret-rotation-drill|security-ops|Secret Rotation Drill|Verify rotating a key does not interrupt the service.|npm run smoke
dependency-confusion-guard|security-ops|Dependency Confusion Guard|Lock private package scopes and registries to prevent wrong-source installs.|npm ci
sbom-generation|security-ops|SBOM Generation|Generate an SBOM and attach it to release artifacts.|syft packages dir:.
prod-access-review|security-ops|Production Access Review|Inventory production access, approval paths, and audit evidence.|terraform state list
backup-restore-security|security-ops|Backup Restore Security|Verify encrypted backups and a restricted restore path.|./scripts/restore-dry-run.sh
etl-contract-tests|data-eng|ETL Contract Tests|Add schema and sample-data contracts between source and target tables.|pytest tests/etl
data-quality-rules|data-eng|Data Quality Rules|Define null, uniqueness, range, and reference checks for key datasets.|great_expectations checkpoint run main
backfill-safety-plan|data-eng|Backfill Safety Plan|Design a sharded, resumable, verifiable historical backfill.|pytest -k backfill
incremental-load-watermark|data-eng|Incremental Load Watermark|Fix missing or duplicate rows in incremental sync logic.|pytest -k watermark
late-arriving-data|data-eng|Late-Arriving Data|Handle delayed events and metric corrections safely.|pytest -k late_arrival
data-lineage-map|data-eng|Data Lineage Map|Map critical report fields from source to consumers.|dbt docs generate
pii-classification|data-eng|PII Classification|Classify sensitive fields and document masking rules.|pytest -k pii
data-retention-enforcement|data-eng|Data Retention Enforcement|Verify expiration, archival, deletion, and audit behavior.|pytest -k retention
warehouse-cost-audit|data-eng|Warehouse Cost Audit|Find expensive queries, duplicate tables, and unused scheduled jobs.|dbt test
stream-processing-lag|data-eng|Stream Processing Lag|Diagnose Kafka/Flink/Spark lag and checkpoint bottlenecks.|pytest -k stream_lag
metric-definition-lock|data-analytics|Metric Definition Lock|Turn core metric definitions into tested SQL or semantic-layer checks.|dbt test
dashboard-trust-audit|data-analytics|Dashboard Trust Audit|Check filters, timezone, refresh cadence, permissions, and source reconciliation.|dbt test && pytest tests/dashboard
ab-test-srm-check|data-analytics|A/B Test SRM Check|Detect sample ratio mismatch in experiment assignment.|pytest -k srm
funnel-dropoff-diagnosis|data-analytics|Funnel Dropoff Diagnosis|Validate funnel events, step counts, and latency before interpreting dropoff.|pytest -k funnel
cohort-retention-query|data-analytics|Cohort Retention Query|Create reusable retention SQL with hand-checked small samples.|dbt test -s retention
revenue-reconciliation|data-analytics|Revenue Reconciliation|Reconcile payments, orders, refunds, and finance definitions.|pytest -k revenue_reconciliation
event-taxonomy-cleanup|data-analytics|Event Taxonomy Cleanup|Deduplicate event names, properties, and version changes.|pytest -k event_schema
anomaly-detection-baseline|data-analytics|Anomaly Detection Baseline|Backtest alert thresholds against historical metrics.|pytest -k anomaly
attribution-window-review|data-analytics|Attribution Window Review|Verify campaign attribution windows and dedupe rules.|dbt test -s attribution
self-serve-data-contract|data-analytics|Self-Serve Data Contract|Define trusted datasets and usage limits for business users.|dbt test -s semantic
llm-golden-set-build|ai-evals|LLM Golden Set Build|Build an eval set from real failures and frequent tasks.|pytest evals
llm-regression-gate|ai-evals|LLM Regression Gate|Compare old and new model or prompt outputs in PRs.|pytest evals
judge-calibration|ai-evals|Judge Calibration|Measure LLM judge agreement against human labels.|pytest evals/judges
hallucination-probe-suite|ai-evals|Hallucination Probe Suite|Add negative cases for nonexistent files, fields, APIs, and sources.|pytest evals/hallucination
rag-answer-faithfulness|ai-evals|RAG Answer Faithfulness|Check that answers are supported by retrieved evidence.|pytest evals/rag
tool-use-eval|ai-evals|Tool Use Eval|Evaluate whether an agent selects, orders, and validates tools correctly.|pytest evals/tool_use
adversarial-prompt-redteam|ai-evals|Prompt Injection Red Team|Test prompt leakage, unauthorized tools, and instruction override attempts.|pytest evals/redteam
eval-data-dedup|ai-evals|Eval Data Dedup|Remove duplicates, leakage, and near-identical eval samples.|python scripts/dedup_evals.py
cost-quality-frontier|ai-evals|Cost Quality Frontier|Compare models by quality, latency, and cost to choose routing tiers.|pytest evals --record-costs
rubric-driven-eval|ai-evals|Rubric-Driven Eval|Replace binary scores with multi-dimensional rubrics for complex tasks.|pytest evals/rubrics
prompt-version-registry|ai-ops|Prompt Version Registry|Bind prompt versions to eval results and deployment history.|pytest tests/prompt_registry
rag-chunking-experiment|ai-ops|RAG Chunking Experiment|Compare chunk size, overlap, and metadata on retrieval and answer quality.|pytest evals/rag_chunking
vector-index-refresh|ai-ops|Vector Index Refresh|Verify document updates are indexed completely and can be rolled back.|pytest tests/index_refresh
model-routing-policy|ai-ops|Model Routing Policy|Route by risk, cost, latency, and quality evidence.|pytest tests/model_routing
llm-timeout-budget|ai-ops|LLM Timeout Budget|Define timeout, retry, fallback, and user-visible error behavior.|pytest tests/llm_timeouts
token-cost-attribution|ai-ops|Token Cost Attribution|Attribute model costs by user, feature, model, and request ID.|pytest tests/costs
prompt-injection-filter|ai-ops|RAG Prompt Injection Filter|Detect and isolate malicious instructions in retrieved documents.|pytest evals/prompt_injection
ai-output-schema-guard|ai-ops|AI Output Schema Guard|Validate structured AI output and fail or retry safely.|pytest tests/schema_guard
human-review-threshold|ai-ops|Human Review Threshold|Escalate high-risk AI outputs based on confidence and policy rules.|pytest tests/human_review
ai-observability-traces|ai-ops|AI Observability Traces|Trace prompts, retrieval, tools, models, scores, and request IDs.|pytest tests/tracing
frontend-empty-states|frontend|Empty State System|Design real empty states for lists, search, permissions, and first use.|npm run test -- EmptyState
frontend-error-boundary|frontend|Error Boundary Experience|Add recoverable page and component fallback UI for crashes.|npm test -- ErrorBoundary
frontend-loading-skeletons|frontend|Loading Skeletons|Replace layout-shifting spinners with stable skeleton states.|npm run lighthouse
frontend-form-validation|frontend|Form Validation|Cover inline, submit, server error, and dirty-state validation.|npm test -- form
frontend-table-density|frontend|Data Table Density|Improve columns, filters, sorting, pagination, and bulk actions.|npx playwright test table.spec.ts
frontend-command-palette|frontend|Command Palette|Add a keyboard-first entry point for high-frequency actions.|npx playwright test command-palette.spec.ts
frontend-navigation-map|frontend|Navigation Map|Clarify primary navigation, breadcrumbs, and detail-page return paths.|npx playwright test navigation.spec.ts
frontend-state-recovery|frontend|State Recovery|Restore filters and context after refresh, back, and deep links.|npx playwright test state-recovery.spec.ts
frontend-permission-ui|frontend|Permission State UI|Separate unauthenticated, unauthorized, and missing-resource states.|npx playwright test permissions.spec.ts
frontend-bulk-actions|frontend|Bulk Actions|Handle selection, confirm, undo, partial failure, and feedback.|npx playwright test bulk-actions.spec.ts
frontend-search-filter|frontend|Search Filter Experience|Unify search, filter chips, clear actions, and result counts.|npx playwright test search-filter.spec.ts
frontend-realtime-updates|frontend|Realtime Update Prompts|Handle background changes, conflicts, and refresh prompts.|npx playwright test realtime.spec.ts
design-visual-hierarchy|design|Visual Hierarchy Pass|Reorder headings, metadata, primary actions, and secondary actions.|npx playwright test visual-hierarchy.spec.ts
design-token-audit|design|Design Token Audit|Check colors, spacing, radii, and shadows against tokens.|npm run lint:styles
design-component-variants|design|Component Variant Matrix|Complete button, input, card, and modal state coverage.|npm run storybook:test
design-dashboard-layout|design|Dashboard Layout Pass|Make an operational dashboard easier to scan and compare.|npx playwright test dashboard.spec.ts
design-modal-discipline|design|Modal Discipline|Replace modal misuse with drawers, popovers, or pages where appropriate.|npx playwright test modal.spec.ts
design-iconography|design|Iconography System|Unify icon semantics for tools, statuses, and empty states.|npm run lint:icons
design-color-contrast|design|Color Contrast Pass|Fix low contrast text, icons, and state colors.|npx axe http://localhost:3000
design-motion-rules|design|Motion Rules|Define entry, exit, feedback, and reduced-motion behavior.|npx playwright test motion.spec.ts
design-responsive-grid|design|Responsive Grid|Define breakpoints, columns, and fixed-format constraints.|npx playwright test responsive.spec.ts
design-toolbar-usability|design|Toolbar Usability|Improve icon buttons, tooltips, grouping, and disabled states.|npx playwright test toolbar.spec.ts
design-data-card-system|design|Data Card System|Define metric cards with value, trend, anomaly, and source states.|npm run storybook:test
design-brand-fit|design|Brand Fit Pass|Align the interface language with the product's audience and use case.|npx playwright test brand.spec.ts
mobile-bottom-nav|mobile|Mobile Bottom Navigation|Design thumb-friendly mobile navigation for core paths.|npx playwright test --project=mobile navigation.spec.ts
mobile-touch-targets|mobile|Mobile Touch Targets|Ensure buttons, checkboxes, and rows have usable tap areas.|npx playwright test --project=mobile touch.spec.ts
mobile-form-flow|mobile|Mobile Form Flow|Handle long forms, keyboard occlusion, and error positioning.|npx playwright test --project=mobile form.spec.ts
mobile-table-adaptation|mobile|Mobile Table Adaptation|Convert wide tables into cards, horizontal scroll, or drill-downs.|npx playwright test --project=mobile table.spec.ts
mobile-filter-drawer|mobile|Mobile Filter Drawer|Add mobile filters with apply, reset, count, and URL state.|npx playwright test --project=mobile filter.spec.ts
mobile-offline-state|mobile|Mobile Offline State|Show offline, cached data, and retry paths clearly.|npx playwright test --project=mobile offline.spec.ts
mobile-image-performance|mobile|Mobile Image Performance|Optimize image sizes, lazy loading, placeholders, and formats.|npm run lighthouse:mobile
mobile-safe-area|mobile|Mobile Safe Area|Handle iOS notch, bottom bars, and sticky actions.|npx playwright test --project=mobile safe-area.spec.ts
mobile-gesture-conflicts|mobile|Mobile Gesture Conflicts|Resolve conflicts between swipe, drag, and scroll interactions.|npx playwright test --project=mobile gestures.spec.ts
mobile-login-flow|mobile|Mobile Login Flow|Improve magic link, OTP, password manager, and autofill behavior.|npx playwright test --project=mobile login.spec.ts
mobile-onboarding|mobile|Mobile Onboarding|Create a short, skippable, restorable first-run path.|npx playwright test --project=mobile onboarding.spec.ts
mobile-device-matrix|mobile|Mobile Device Matrix|Cover small screen, large screen, iOS, and Android key paths.|npx playwright test --project=mobile
docs-quickstart|docs|Quickstart|Write the shortest fresh-clone path that runs successfully in five minutes.|markdownlint README.md
docs-install-troubleshooting|docs|Install Troubleshooting|Document common install failures, causes, and fixes.|markdownlint docs
docs-api-examples|docs|API Examples|Add minimal request, response, and error examples for core APIs.|pytest -k docs_api_examples
docs-architecture-overview|docs|Architecture Overview|Explain module boundaries, data flow, and explicit non-goals.|markdownlint docs/architecture.md
docs-contribution-guide|docs|Contribution Guide|Document development, testing, commit, and PR review rules.|markdownlint CONTRIBUTING.md
docs-release-notes|docs|Release Notes|Create user-facing change, migration, and breaking-change notes.|markdownlint CHANGELOG.md
docs-env-vars|docs|Environment Variables|List env names, defaults, requiredness, and safety notes.|pytest -k env_config
docs-runbook|docs|Operator Runbook|Document alerts, recovery, rollback, and data repair steps.|markdownlint docs/runbooks
docs-decision-records|docs|Architecture Decision Records|Add ADR templates and indexes for major technical decisions.|markdownlint docs/adr
docs-glossary|docs|Glossary|Unify product, engineering, and data-field terms.|markdownlint docs/glossary.md
docs-screenshot-docs|docs|Screenshot Docs|Add real screenshots and labels for UI workflows.|markdownlint docs
docs-docs-lint|docs|Docs Lint Gate|Add link, spelling, and executable code block checks.|markdownlint . && lychee .
product-user-journeys|product|User Journeys|Map persona tasks into pages, events, and success states.|markdownlint docs/product
product-prd-skeleton|product|PRD Skeleton|Write goals, non-goals, constraints, and acceptance criteria.|markdownlint docs/prd.md
product-onboarding-metrics|product|Onboarding Metrics|Define activation events, dropoff points, and dashboard queries.|pytest -k analytics_events
product-feature-prioritization|product|Feature Prioritization|Split MVP and later work by impact, cost, and risk.|markdownlint docs/roadmap.md
product-permission-model|product|Permission Model|Map roles, resources, actions, and UI visibility.|pytest -k permissions
product-notification-strategy|product|Notification Strategy|Define triggers, channels, frequency, and unsubscribe behavior.|pytest -k notifications
product-empty-data-policy|product|Empty Data Policy|Choose blank, sample data, import, or CTA by user state.|npx playwright test empty-data.spec.ts
product-upgrade-path|product|Upgrade Path|Design limits, paywalls, trials, and upgrade conversion paths.|pytest -k entitlement
product-feedback-loop|product|Feedback Loop|Collect, classify, track, and close user feedback.|markdownlint docs/feedback.md
product-search-relevance|product|Search Relevance|Define query handling, ranking, typo tolerance, and no-result behavior.|pytest -k search_relevance
product-admin-workflows|product|Admin Workflows|Design review, undo, audit log, and bulk moderation flows.|npx playwright test admin.spec.ts
product-success-criteria|product|Success Criteria|Define quantitative and qualitative completion measures for a feature.|markdownlint docs/success.md
qa-critical-paths|qa|Critical Path Tests|Cover signup, create, edit, delete, export, and recovery flows.|npx playwright test critical-paths.spec.ts
qa-regression-matrix|qa|Regression Matrix|Build feature/browser/role/data-state regression coverage.|npx playwright test
qa-fixture-strategy|qa|Fixture Strategy|Create deterministic seed, mock, factory, and cleanup patterns.|pytest -k fixtures
qa-visual-regression|qa|Visual Regression|Add screenshot diffs for critical pages with controlled thresholds.|npx playwright test visual.spec.ts
qa-api-contracts|qa|API Contracts|Validate frontend/backend schema, error codes, and boundary values.|pytest -k contract
qa-flaky-test-audit|qa|Flaky Test Audit|Find unstable tests and fix waits, isolation, or fixtures.|pytest --count=20
qa-error-injection|qa|Error Injection|Simulate 500s, timeouts, network failure, and partial success.|npx playwright test error-injection.spec.ts
qa-cross-browser|qa|Cross-Browser Coverage|Run critical flows across Chromium, Firefox, and WebKit.|npx playwright test --project=chromium --project=firefox --project=webkit
qa-release-smoke|qa|Release Smoke|Define the smallest pre-release verification checklist.|npm run smoke
qa-data-migration|qa|Data Migration Test|Verify counts, constraints, and rollback around data migration.|pytest -k migration
qa-security-smoke|qa|Security Smoke|Check auth, permission bypass, and sensitive info leakage.|pytest -k security_smoke
qa-bug-repro-template|qa|Bug Reproduction Template|Standardize environment, steps, expected, actual, and evidence.|markdownlint .github/ISSUE_TEMPLATE
accessibility-keyboard-nav|accessibility|Keyboard Navigation|Ensure the whole app works with Tab, Enter, and Escape.|npx playwright test keyboard.spec.ts
accessibility-screen-reader|accessibility|Screen Reader Semantics|Check landmarks, labels, aria-live, and button names.|npx axe http://localhost:3000
accessibility-focus-visible|accessibility|Focus Visible|Give every interactive element a clear focus state.|npx playwright test focus.spec.ts
accessibility-color-contrast|accessibility|Color Contrast|Meet WCAG AA for text, icons, and state colors.|npx axe http://localhost:3000
accessibility-form-errors|accessibility|Accessible Form Errors|Associate errors with fields so screen readers announce them.|npx playwright test form-a11y.spec.ts
accessibility-modal-trap|accessibility|Modal Focus Trap|Focus opens, cycles, closes, and returns correctly.|npx playwright test modal-a11y.spec.ts
accessibility-reduced-motion|accessibility|Reduced Motion|Respect prefers-reduced-motion for all nonessential motion.|npx playwright test reduced-motion.spec.ts
accessibility-alt-text|accessibility|Alt Text Audit|Separate decorative, content, and product images.|npx axe http://localhost:3000
accessibility-heading-order|accessibility|Heading Order|Fix skipped headings and fake styled headings.|npx axe http://localhost:3000
accessibility-live-region|accessibility|Live Region Feedback|Announce toasts, async completion, and errors accessibly.|npx playwright test live-region.spec.ts
accessibility-touch-a11y|accessibility|Touch Accessibility|Check tap targets, zoom, and orientation on mobile.|npx playwright test --project=mobile a11y.spec.ts
accessibility-audit-report|accessibility|Accessibility Audit Report|Produce prioritized issues, impact, fixes, and acceptance checks.|npx axe http://localhost:3000 --save results.json
performance-lcp|performance|LCP Optimization|Find and optimize the largest contentful paint element.|npm run lighthouse
performance-cls|performance|CLS Fix|Reserve space for images, ads, and dynamic content.|npm run lighthouse
performance-inp|performance|INP Optimization|Reduce long tasks and blocking interaction handlers.|npm run trace
performance-bundle-budget|performance|Bundle Budget|Set route and dependency size budgets in CI.|npm run analyze
performance-code-splitting|performance|Code Splitting|Lazy-load low-frequency routes, charts, and editors.|npm run analyze
performance-image-pipeline|performance|Image Pipeline|Use srcset, modern formats, lazy loading, and cache headers.|npm run lighthouse
performance-font-loading|performance|Font Loading|Optimize font-display, subsets, and preload hints.|npm run lighthouse
performance-api-waterfall|performance|API Waterfall|Remove serial requests and prefetch critical data.|npx playwright test performance.spec.ts
performance-cache-strategy|performance|Cache Strategy|Define browser, CDN, and service-worker cache boundaries.|npx playwright test cache.spec.ts
performance-memory-leaks|performance|Memory Leak Audit|Check long sessions, lists, subscriptions, and charts for leaks.|npm run test:memory
performance-render-count|performance|Render Count Audit|Find unnecessary React renders and expensive selectors.|npm run profile
performance-ci-gate|performance|Performance CI Gate|Add Lighthouse or trace thresholds to CI.|npm run lighthouse:ci
goal-meta-prompt-writer|workflow|Goal Prompt Writer|Ask the agent to inspect a repo and write a precise goal prompt before execution.|markdownlint generated-goal.md
goal-continuation-audit|workflow|Goal Continuation Audit|Check that a long-running goal keeps its done_when and verification contract after compaction.|rg -e "DONE WHEN" -e "VERIFY" -e "STOP RULES" progress-log.md
""".strip()


SOURCE_BACKED_ENTRIES = """
codex-verifiable-end-state|workflow|Verifiable End-State Contract|Complete one objective only when a verifiable end state is met.|manual status plus repo-local verification|https://developers.openai.com/codex/use-cases/follow-goals|OpenAI Codex docs
codex-visual-migration-playwright|migration|Visual Migration With Playwright|Migrate a project while preserving screen output and checking it with Playwright.|npx playwright test|https://developers.openai.com/codex/use-cases/follow-goals|OpenAI Codex docs
codex-plan-milestone-prototype|prototype|PLAN.md Milestone Prototype|Implement a PLAN.md-driven prototype with tests at each milestone and browser verification.|npx playwright test|https://developers.openai.com/codex/use-cases/follow-goals|OpenAI Codex docs
codex-eval-prompt-optimization|prompt-optimization|Eval-Driven Prompt Optimization|Optimize prompts against an eval suite until the target score or pass rate is reached.|python -m pytest evals|https://developers.openai.com/codex/use-cases/follow-goals|OpenAI Codex docs
claude-auth-tests-lint|testing|Auth Tests And Lint Clean|Keep working until auth tests pass and the lint step is clean.|npm test -- test/auth && npm run lint|https://code.claude.com/docs/en/goal|Claude Code docs
claude-weekly-changelog|docs|Weekly Changelog Coverage|Ensure CHANGELOG.md includes an entry for every PR merged this week.|git log --since='7 days ago' --merges && rg '^-' CHANGELOG.md|https://code.claude.com/docs/en/goal|Claude Code docs
hermes-ruff-src-clean|testing|Ruff Clean Source Tree|Fix every lint error in src and prove ruff passes.|ruff check src/|https://hermes-agent.nousresearch.com/docs/user-guide/features/goals|Hermes docs
hermes-feature-port-ci-green|migration|Feature Port With CI Green|Port a feature from another repo, include tests, and get CI green.|pytest && npm test|https://hermes-agent.nousresearch.com/docs/user-guide/features/goals|Hermes docs
hermes-session-drift-report|investigation|Session Drift Report|Investigate session ID drift during mid-run compression and write a report.|test -f reports/session-drift.md|https://hermes-agent.nousresearch.com/docs/user-guide/features/goals|Hermes docs
hermes-exif-rename-cli|cli|EXIF Rename CLI|Build a small CLI that renames photos by EXIF date and test it on a photos folder.|pytest tests/cli && ./rename-exif photos/ --dry-run|https://hermes-agent.nousresearch.com/docs/user-guide/features/goals|Hermes docs
hermes-four-files-walkthrough|workflow|Four Files Walkthrough|Create four note files across turns and verify each contains its number.|for i in 1 2 3 4; do test \"$(cat /tmp/note_$i.txt)\" = \"$i\"; done|https://hermes-agent.nousresearch.com/docs/user-guide/features/goals|Hermes docs
explainx-typescript-eslint-coverage|testing|TypeScript ESLint Coverage Gate|Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold.|npm run typecheck && npm test && npm run lint && npm run coverage|https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026|ExplainX blog
explainx-auth-di-refactor|refactor|Auth Dependency Injection Refactor|Refactor auth code to dependency injection while preserving tests, coverage, and public API.|npm test -- auth && npm run coverage|https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026|ExplainX blog
explainx-npm-audit-clean|security-ops|NPM Audit Clean Remediation|Patch npm audit vulnerabilities without breaking tests or public APIs.|npm audit && npm test|https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026|ExplainX blog
explainx-lighthouse-core-web-vitals|performance|Lighthouse And Core Web Vitals Gate|Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions.|npm run lighthouse|https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026|ExplainX blog
qiita-vue2-vue3-visual-unit|migration|Vue 2 To Vue 3 Visual And Unit Gate|Migrate listed Vue screens and stop only when visual and unit tests pass.|pnpm test:visual && pnpm test:unit|https://qiita.com/y-morimatsu/items/a314e5bbfdc83616d3ae|Qiita article
qiita-canvas-puzzle-plan|prototype|Canvas Puzzle PLAN.md Prototype|Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes.|pnpm e2e|https://qiita.com/y-morimatsu/items/a314e5bbfdc83616d3ae|Qiita article
qiita-router-eval-score|prompt-optimization|Router Prompt Eval Score|Improve a router prompt against an eval directory until the result score reaches a target.|python -m pytest evals/router|https://qiita.com/y-morimatsu/items/a314e5bbfdc83616d3ae|Qiita article
""".strip()


CATEGORY_CONTEXT = {
    "backend-api": ("a backend API service", "API routes, OpenAPI specs, handlers, middleware, and API tests"),
    "backend-data": ("a data-backed backend service", "schema files, migrations, models, repositories, and data tests"),
    "devops-ci": ("a repository with CI/CD automation", "workflow files, build scripts, package manifests, and recent CI logs"),
    "devops-runtime": ("a deployed service", "Dockerfiles, deployment manifests, runtime config, and health checks"),
    "security-appsec": ("an application with security-sensitive code paths", "auth, input handling, rendering, upload, and boundary tests"),
    "security-ops": ("a production operations environment", "workflow permissions, cloud IAM, release artifacts, and audit evidence"),
    "data-eng": ("a data pipeline project", "ETL jobs, schemas, source contracts, transformations, and data quality tests"),
    "data-analytics": ("an analytics or BI project", "metric SQL, event schemas, dashboard definitions, and validation queries"),
    "ai-evals": ("an AI evaluation project", "eval datasets, rubrics, model outputs, judge code, and regression reports"),
    "ai-ops": ("an AI application runtime", "prompts, retrieval code, routing policies, tracing, and cost logs"),
    "frontend": ("a web frontend application", "routes, components, state, stories, tests, and screenshots"),
    "design": ("a product UI codebase", "design tokens, component variants, layouts, visual states, and screenshots"),
    "mobile": ("a mobile or responsive application", "mobile routes, forms, gestures, device matrix, and viewport tests"),
    "docs": ("a developer-facing documentation site or repository", "README, docs, examples, runbooks, and lint configuration"),
    "product": ("a product planning and implementation repo", "PRDs, analytics events, permission models, and acceptance criteria"),
    "qa": ("a product with automated and manual QA coverage", "test suites, fixtures, bug templates, and release checklists"),
    "accessibility": ("a web or mobile interface", "interactive elements, semantics, focus management, and a11y reports"),
    "performance": ("a web application with measurable performance goals", "Lighthouse reports, bundles, traces, and critical routes"),
    "workflow": ("a coding-agent workflow repository", "goal text, progress logs, branch state, and verification artifacts"),
    "migration": ("a migration project", "legacy code, target implementation, compatibility tests, visual snapshots, and migration notes"),
    "prototype": ("a prototype project", "PLAN.md, milestones, app code, tests, browser checks, and demo notes"),
    "prompt-optimization": ("an eval-backed prompt project", "prompt files, eval cases, scoring reports, regressions, and failure examples"),
    "testing": ("a project with failing or missing verification gates", "test suites, lint config, CI logs, coverage reports, and failing output"),
    "investigation": ("an investigation task", "logs, traces, reproduction notes, source paths, and the final report"),
    "cli": ("a command-line tool", "CLI entrypoints, argument parsing, filesystem behavior, dry-run mode, and fixtures"),
    "refactor": ("a refactoring task", "the target module, call sites, public API, tests, and compatibility notes"),
}


CATEGORY_CONSTRAINTS = {
    "security-appsec": [
        "Do not bypass authentication, authorization, validation, or audit checks.",
        "Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.",
    ],
    "security-ops": [
        "Do not print, copy, rotate, or exfiltrate real secrets.",
        "Do not widen production permissions without a documented least-privilege reason.",
    ],
    "backend-data": [
        "Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.",
        "Do not hide database errors behind warnings or silent fallbacks.",
    ],
    "devops-runtime": [
        "Do not deploy to production automatically; stop with a verified plan if live credentials are required.",
        "Keep rollback and health-check evidence attached to the final output.",
    ],
    "devops-ci": [
        "Do not weaken tests, remove required checks, or bypass branch protection.",
        "Keep workflow permissions as narrow as the task allows.",
    ],
    "ai-evals": [
        "Do not tune prompts against hidden labels or delete failing eval cases to improve the score.",
        "Keep before/after eval evidence and representative failures.",
    ],
    "ai-ops": [
        "Do not silently fall back to a lower-quality model for user-visible critical paths.",
        "Keep request IDs, cost evidence, and schema validation errors visible.",
    ],
    "frontend": [
        "Do not change unrelated routes or rewrite the design system.",
        "Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.",
    ],
    "design": [
        "Do not replace the app with a landing-page style redesign.",
        "Preserve domain workflows and use existing design tokens where they exist.",
    ],
    "mobile": [
        "Do not optimize only desktop behavior.",
        "Keep touch targets, safe areas, and keyboard overlap in scope.",
    ],
    "docs": [
        "Do not invent APIs, flags, commands, or product behavior.",
        "Mark unverified commands clearly instead of presenting guesses as facts.",
    ],
    "product": [
        "Do not implement new product scope unless it is in the stated acceptance criteria.",
        "Separate product decisions from engineering assumptions.",
    ],
    "qa": [
        "Do not delete or weaken failing tests to make the suite pass.",
        "Reproduce failures before changing production code.",
    ],
    "accessibility": [
        "Do not hide controls from assistive technology to silence audit findings.",
        "Keep keyboard, focus, semantic, and visual checks together.",
    ],
    "performance": [
        "Do not trade correctness, accessibility, or security for faster synthetic scores.",
        "Compare before/after metrics on the same route and environment.",
    ],
    "workflow": [
        "Do not claim a goal is complete without a current audit of the stated contract.",
        "Pause if the goal text, branch state, or permissions are inconsistent.",
    ],
    "migration": [
        "Preserve existing user-visible behavior unless the goal explicitly names a behavior change.",
        "Keep compatibility evidence for the old and new paths until the migration is verified.",
    ],
    "prototype": [
        "Follow the stated PLAN.md or acceptance criteria instead of adding unrequested features.",
        "Keep the prototype runnable and demonstrable at every completed milestone.",
    ],
    "prompt-optimization": [
        "Do not delete, weaken, or cherry-pick eval cases to improve the score.",
        "Report representative failures as well as the final score.",
    ],
    "testing": [
        "Do not weaken lint, typecheck, or test rules to create a green result.",
        "Fix production or fixture causes before changing expectations.",
    ],
    "investigation": [
        "Separate observed evidence from hypotheses.",
        "Do not patch production code until the root cause is reproduced or strongly evidenced.",
    ],
    "cli": [
        "Do not perform destructive filesystem operations without a dry-run or explicit confirmation.",
        "Keep command output deterministic enough for tests.",
    ],
    "refactor": [
        "Do not change public APIs, data formats, or user-visible behavior unless the goal requires it.",
        "Keep behavior characterization tests before large internal changes.",
    ],
}


def parse_entries() -> list[dict[str, str | None]]:
    entries: list[dict[str, str | None]] = []
    for line in RAW_ENTRIES.splitlines():
        slug, category, title, intent, verify = line.split("|")
        entries.append(
            {
                "id": slug,
                "slug": slug,
                "category": category,
                "title": title,
                "intent": intent,
                "verify": verify,
                "difficulty": difficulty_for(category),
                "origin": "seed",
                "source_url": None,
                "source_name": None,
            }
        )
    for line in SOURCE_BACKED_ENTRIES.splitlines():
        slug, category, title, intent, verify, source_url, source_name = line.split("|")
        entries.append(
            {
                "id": slug,
                "slug": slug,
                "category": category,
                "title": title,
                "intent": intent,
                "verify": verify,
                "difficulty": difficulty_for(category),
                "origin": "source-backed",
                "source_url": source_url,
                "source_name": source_name,
            }
        )
    slugs = [str(entry["slug"]) for entry in entries]
    if len(slugs) != len(set(slugs)):
        duplicates = sorted({slug for slug in slugs if slugs.count(slug) > 1})
        raise SystemExit(f"duplicate slugs: {', '.join(duplicates)}")
    return entries


def difficulty_for(category: str) -> str:
    if category.startswith("security") or category in {"backend-data", "devops-runtime", "ai-evals", "ai-ops", "migration"}:
        return "advanced"
    if category in {"docs", "product", "design", "workflow", "testing", "prototype", "cli", "refactor", "investigation", "prompt-optimization"}:
        return "intermediate"
    return "intermediate"


def constraints_for(category: str) -> list[str]:
    base = [
        "Keep the scope limited to this goal; do not expand into unrelated cleanup.",
        "Do not weaken tests, delete assertions, or mask errors to make verification pass.",
        "Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.",
    ]
    return base + CATEGORY_CONSTRAINTS.get(category, [])


def prompt_for(entry: dict[str, str | None]) -> str:
    context_label, inspect_scope = CATEGORY_CONTEXT[entry["category"]]
    constraints = "\n".join(f"- {item}" for item in constraints_for(entry["category"]))
    return f"""/goal
GOAL:
Complete {entry["title"]} for {context_label}: {entry["intent"]}

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect {inspect_scope}.
- Establish a baseline by running or locating evidence for: `{entry["verify"]}`.

CONSTRAINTS:
{constraints}

DONE WHEN:
- The implementation or documentation directly satisfies: {entry["intent"]}
- The verification command or evidence path succeeds: `{entry["verify"]}`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `{entry["verify"]}` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN."""


def by_category(entries: list[dict[str, str | None]]) -> dict[str, list[dict[str, str | None]]]:
    grouped: dict[str, list[dict[str, str | None]]] = {}
    for entry in entries:
        grouped.setdefault(str(entry["category"]), []).append(entry)
    return grouped


def source_line(entry: dict[str, str | None]) -> str | None:
    if entry.get("source_url") and entry.get("source_name"):
        return f"- Source: [{entry['source_name']}]({entry['source_url']})"
    return None


def build_markdown(entries: list[dict[str, str | None]]) -> str:
    lines = [
        "# Goal Prompt Examples",
        "",
        "Each example is a complete `/goal` task contract. Replace placeholder commands, paths, and project names with your repository's real values before running.",
        "",
        "These examples intentionally use only the documented `/goal <objective>` form. They do not rely on unofficial subcommands.",
        "",
        "## Index",
        "",
    ]
    for category, category_entries in by_category(entries).items():
        lines.append(f"### {category}")
        for entry in category_entries:
            suffix = " Source-backed." if entry["origin"] == "source-backed" else ""
            lines.append(f"- [{entry['title']}](#{entry['slug']}) - {entry['intent']}{suffix}")
        lines.append("")
    lines.append("## Examples")
    lines.append("")
    for entry in entries:
        source = source_line(entry)
        lines.extend(
            [
                f'<a id="{entry["slug"]}"></a>',
                f"### {entry['title']}",
                "",
                f"- Category: `{entry['category']}`",
                f"- Difficulty: `{entry['difficulty']}`",
                f"- Origin: `{entry['origin']}`",
                f"- Intent: {entry['intent']}",
                f"- Verification: `{entry['verify']}`",
            ]
        )
        if source:
            lines.append(source)
        lines.extend(
            [
                "",
                "```text",
                prompt_for(entry),
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_readme(entries: list[dict[str, str | None]]) -> str:
    grouped = by_category(entries)
    lines = [
        "# Awesome Goal Prompts",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)",
        "",
        "A curated list of `/goal` task contracts for coding agents.",
        "",
        "A good goal is not a wish. It is a runnable contract: one objective, enough context to inspect, hard constraints, verifiable completion, and stop rules for uncertainty or risk.",
        "",
        "## Contents",
        "",
        "- [Goal Prompts](#goal-prompts)",
        "- [Templates](#templates)",
        "- [Quality Bar](#quality-bar)",
        "- [Sources And Caveats](#sources-and-caveats)",
        "- [Contributing](#contributing)",
        "",
        "## Goal Prompts",
        "",
        "Full prompt bodies live in [prompts/goal-examples.md](prompts/goal-examples.md).",
        "",
    ]
    for category, category_entries in grouped.items():
        lines.append(f"### {category}")
        for entry in category_entries:
            marker = " _(source-backed)_" if entry["origin"] == "source-backed" else ""
            lines.append(f"- [{entry['title']}](prompts/goal-examples.md#{entry['slug']}) - {entry['intent']}{marker}")
        lines.append("")
    lines.extend(
        [
            "## Templates",
            "",
            "- [Full template](templates/full-goal-template.md) for high-risk or multi-step work.",
            "- [Compact template](templates/compact-goal-template.md) for routine work.",
            "- [Structured JSON data](data/examples.json) for search, tooling, or site generation.",
            "",
            "## Quality Bar",
            "",
            "- One example should cover one measurable objective.",
            "- The prompt must include verification that can run in a real repository or produce a concrete artifact.",
            "- New externally sourced examples must include `source_name` and `source_url` in `data/examples.json`.",
            "- Do not add undocumented slash-command behavior, fake tool capabilities, or examples copied from private/non-verifiable sources.",
            "",
            "## Sources And Caveats",
            "",
            "See [SOURCES.md](SOURCES.md) for public sources used by source-backed examples and notes about cross-tool differences.",
            "",
            "This repository does not claim that `/goal` behaves identically across Codex, Claude Code, Hermes, or other tools.",
            "",
            "## Contributing",
            "",
            "Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding examples. Keep descriptions short, source-backed when based on external material, and scoped to verifiable engineering work.",
            "",
            "## License",
            "",
            "MIT",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    entries = parse_entries()
    for entry in entries:
        entry["prompt"] = prompt_for(entry)
    (ROOT / "prompts").mkdir(exist_ok=True)
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "README.md").write_text(build_readme(entries), encoding="utf-8")
    (ROOT / "prompts" / "goal-examples.md").write_text(build_markdown(entries), encoding="utf-8")
    (ROOT / "data" / "examples.json").write_text(
        json.dumps(entries, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print("generated goal catalog")


if __name__ == "__main__":
    main()

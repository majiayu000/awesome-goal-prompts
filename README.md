# Awesome Goal Prompts

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A curated list of `/goal` task contracts for coding agents.

A good goal is not a wish. It is a runnable contract: one objective, enough context to inspect, hard constraints, verifiable completion, and stop rules for uncertainty or risk.

## Contents

- [Goal Prompts](#goal-prompts)
- [Templates](#templates)
- [Quality Bar](#quality-bar)
- [Sources And Caveats](#sources-and-caveats)
- [Contributing](#contributing)

## Goal Prompts

Full prompt bodies live in [prompts/goal-examples.md](prompts/goal-examples.md).

### backend-api
- [API Contract Drift Audit](prompts/goal-examples.md#api-contract-drift-audit) - Compare OpenAPI, implementation, and tests to find field or status-code drift.
- [Idempotent Create Endpoint](prompts/goal-examples.md#idempotent-create-endpoint) - Add idempotency keys and replay-safe semantics to a create endpoint.
- [API Error Taxonomy](prompts/goal-examples.md#api-error-taxonomy) - Unify HTTP status codes, machine error codes, user messages, and logs.
- [Pagination Consistency](prompts/goal-examples.md#pagination-consistency) - Fix cursor or offset pagination so rows are not skipped, duplicated, or reordered.
- [Request Validation Boundary](prompts/goal-examples.md#request-validation-boundary) - Move input validation to the API boundary and reject unknown fields.
- [API Rate Limit Policy](prompts/goal-examples.md#api-rate-limit-policy) - Implement rate limit behavior, headers, and over-limit responses for critical routes.
- [Webhook Retry Contract](prompts/goal-examples.md#webhook-retry-contract) - Define webhook signature verification, retry, dedupe, and failure observability.
- [Backward-Compatible Response](prompts/goal-examples.md#backward-compatible-response) - Add response fields without breaking old clients and document removal paths.
- [gRPC Timeout Propagation](prompts/goal-examples.md#grpc-timeout-propagation) - Propagate deadlines across service calls and cancel work correctly.
- [Async Job State Machine](prompts/goal-examples.md#async-job-state-machine) - Make async job transitions explicit and tested across pending/running/succeeded/failed/canceled.
- [Resource-Level Authorization](prompts/goal-examples.md#authz-resource-scope) - Prevent logged-in users from accessing resources they do not own.
- [API Versioning Plan](prompts/goal-examples.md#api-versioning-plan) - Create a v1/v2 coexistence plan with deprecation headers and migration tests.

### backend-data
- [Database Migration Safety](prompts/goal-examples.md#db-migration-safety) - Review a migration for rollback, online execution, and lock risk.
- [Transaction Boundary Audit](prompts/goal-examples.md#transaction-boundary-audit) - Find missing or oversized transactions in multi-table write paths.
- [Cache Invalidation Map](prompts/goal-examples.md#cache-invalidation-map) - Map write paths to cache keys and fix stale reads.
- [N+1 Query Fix](prompts/goal-examples.md#n-plus-one-query-fix) - Reduce list endpoint query count with batching or preloading.
- [Optimistic Locking Rollout](prompts/goal-examples.md#optimistic-locking-rollout) - Add version checks and conflict responses for concurrent edits.
- [Soft Delete Integrity](prompts/goal-examples.md#soft-delete-integrity) - Make queries, unique indexes, and restore flows respect soft deletion.
- [Index Regression Check](prompts/goal-examples.md#db-index-regression) - Add or adjust indexes and prove read gains do not create unacceptable write cost.
- [Outbox Reliable Events](prompts/goal-examples.md#outbox-pattern-adoption) - Use an outbox table to prevent lost events after successful database commits.
- [Read Replica Lag Guard](prompts/goal-examples.md#read-replica-lag-guard) - Prevent write-after-read paths from hitting stale replicas.
- [Schema Drift Detector](prompts/goal-examples.md#schema-drift-detector) - Compare ORM models, migrations, and the live database schema.

### devops-ci
- [CI Flaky Test Triage](prompts/goal-examples.md#ci-flaky-test-triage) - Identify flaky tests, separate real failures, and fix unstable waits or fixtures.
- [Build Cache Correctness](prompts/goal-examples.md#build-cache-correctness) - Check whether CI cache keys cause stale dependencies or cross-branch pollution.
- [Dependency Update Gate](prompts/goal-examples.md#dependency-update-gate) - Add dependency upgrade checks for tests, licenses, and vulnerabilities.
- [Monorepo Affected Tests](prompts/goal-examples.md#monorepo-affected-tests) - Run only affected tests without missing cross-package contracts.
- [Release Notes From Diff](prompts/goal-examples.md#release-note-from-diff) - Generate user-facing release notes from commits, PR labels, and breaking changes.
- [Artifact Provenance](prompts/goal-examples.md#artifact-provenance) - Trace a package or image back to the commit and workflow that produced it.
- [CI Permission Minimization](prompts/goal-examples.md#ci-permission-minimize) - Tighten GitHub Actions token permissions without breaking workflows.
- [Branch Protection Audit](prompts/goal-examples.md#branch-protection-audit) - Audit required checks, reviews, linear history, and admin bypasses.
- [Release Rollback Drill](prompts/goal-examples.md#release-rollback-drill) - Create and test a rollback path for the latest release.
- [Semantic Version Check](prompts/goal-examples.md#semantic-version-check) - Infer the correct semver bump from API, behavior, and changelog diffs.

### devops-runtime
- [Docker Image Slimming](prompts/goal-examples.md#docker-image-slimming) - Reduce image size while keeping runtime dependencies and security scans green.
- [Kubernetes Probe Repair](prompts/goal-examples.md#k8s-readiness-liveness) - Separate startup, readiness, and liveness probes to avoid bad restarts.
- [Terraform Plan Review](prompts/goal-examples.md#terraform-plan-review) - Review infrastructure changes for deletes, replacements, and permission expansion.
- [Helm Values Drift](prompts/goal-examples.md#helm-values-drift) - Compare environment values to find hidden staging/prod differences.
- [Autoscaling Thresholds](prompts/goal-examples.md#autoscaling-thresholds) - Tune HPA or worker scaling thresholds against real load and queue depth.
- [Runtime Config Validation](prompts/goal-examples.md#runtime-config-validation) - Fail startup on missing or invalid environment and config values.
- [Zero-Downtime Migration](prompts/goal-examples.md#zero-downtime-migration) - Plan and verify expand-migrate-contract deployment steps.
- [Observability Minimum](prompts/goal-examples.md#observability-minimum) - Add logs, metrics, traces, and alerts for a service's critical paths.
- [Incident Runbook Gap](prompts/goal-examples.md#incident-runbook-gap) - Turn a recent incident timeline into missing runbook and alert updates.
- [Queue Backpressure](prompts/goal-examples.md#queue-backpressure) - Protect databases and external APIs when worker queues build up.

### security-appsec
- [SQL Injection Audit](prompts/goal-examples.md#sql-injection-audit) - Replace SQL string concatenation with parameterized queries and tests.
- [Command Injection Audit](prompts/goal-examples.md#command-injection-audit) - Replace shell string execution with argument arrays and validation.
- [SSRF Defense Review](prompts/goal-examples.md#ssrf-defense-review) - Add URL allowlists and DNS/IP checks for fetch or callback features.
- [XSS Output Encoding](prompts/goal-examples.md#xss-output-encoding) - Audit HTML and Markdown rendering for unsafe sinks and missing encoding.
- [CSRF Sensitive Action](prompts/goal-examples.md#csrf-sensitive-action) - Protect cookie-authenticated writes from cross-site requests.
- [Auth Bypass Route Map](prompts/goal-examples.md#auth-bypass-route-map) - Enumerate routes and verify unauthenticated and unauthorized behavior.
- [File Upload Security](prompts/goal-examples.md#file-upload-security) - Validate MIME, extension, size, scanning, and storage isolation.
- [Tenant Isolation Test](prompts/goal-examples.md#tenant-isolation-test) - Verify tenant IDs are enforced in queries, caches, and background jobs.
- [Replay Attack Defense](prompts/goal-examples.md#replay-attack-defense) - Add nonce, timestamp, and expiration checks to signed requests.
- [IDOR Audit](prompts/goal-examples.md#insecure-direct-object-ref) - Verify direct object ID access always checks ownership or scope.

### security-ops
- [Secret Scan Baseline](prompts/goal-examples.md#secret-scan-baseline) - Add secret scanning and triage historical findings safely.
- [IAM Least Privilege](prompts/goal-examples.md#iam-least-privilege) - Reduce cloud permissions to observed API usage and documented needs.
- [GitHub Actions Supply Chain](prompts/goal-examples.md#github-actions-supply-chain) - Pin third-party actions and review workflow permissions.
- [Container Vulnerability Triage](prompts/goal-examples.md#container-vuln-triage) - Prioritize image CVEs by exploitability and runtime exposure.
- [Audit Log Coverage](prompts/goal-examples.md#audit-log-coverage) - Add audit logs for login, permission changes, and sensitive data access.
- [Secret Rotation Drill](prompts/goal-examples.md#secret-rotation-drill) - Verify rotating a key does not interrupt the service.
- [Dependency Confusion Guard](prompts/goal-examples.md#dependency-confusion-guard) - Lock private package scopes and registries to prevent wrong-source installs.
- [SBOM Generation](prompts/goal-examples.md#sbom-generation) - Generate an SBOM and attach it to release artifacts.
- [Production Access Review](prompts/goal-examples.md#prod-access-review) - Inventory production access, approval paths, and audit evidence.
- [Backup Restore Security](prompts/goal-examples.md#backup-restore-security) - Verify encrypted backups and a restricted restore path.
- [NPM Audit Clean Remediation](prompts/goal-examples.md#explainx-npm-audit-clean) - Patch npm audit vulnerabilities without breaking tests or public APIs. _(source-backed)_

### data-eng
- [ETL Contract Tests](prompts/goal-examples.md#etl-contract-tests) - Add schema and sample-data contracts between source and target tables.
- [Data Quality Rules](prompts/goal-examples.md#data-quality-rules) - Define null, uniqueness, range, and reference checks for key datasets.
- [Backfill Safety Plan](prompts/goal-examples.md#backfill-safety-plan) - Design a sharded, resumable, verifiable historical backfill.
- [Incremental Load Watermark](prompts/goal-examples.md#incremental-load-watermark) - Fix missing or duplicate rows in incremental sync logic.
- [Late-Arriving Data](prompts/goal-examples.md#late-arriving-data) - Handle delayed events and metric corrections safely.
- [Data Lineage Map](prompts/goal-examples.md#data-lineage-map) - Map critical report fields from source to consumers.
- [PII Classification](prompts/goal-examples.md#pii-classification) - Classify sensitive fields and document masking rules.
- [Data Retention Enforcement](prompts/goal-examples.md#data-retention-enforcement) - Verify expiration, archival, deletion, and audit behavior.
- [Warehouse Cost Audit](prompts/goal-examples.md#warehouse-cost-audit) - Find expensive queries, duplicate tables, and unused scheduled jobs.
- [Stream Processing Lag](prompts/goal-examples.md#stream-processing-lag) - Diagnose Kafka/Flink/Spark lag and checkpoint bottlenecks.

### data-analytics
- [Metric Definition Lock](prompts/goal-examples.md#metric-definition-lock) - Turn core metric definitions into tested SQL or semantic-layer checks.
- [Dashboard Trust Audit](prompts/goal-examples.md#dashboard-trust-audit) - Check filters, timezone, refresh cadence, permissions, and source reconciliation.
- [A/B Test SRM Check](prompts/goal-examples.md#ab-test-srm-check) - Detect sample ratio mismatch in experiment assignment.
- [Funnel Dropoff Diagnosis](prompts/goal-examples.md#funnel-dropoff-diagnosis) - Validate funnel events, step counts, and latency before interpreting dropoff.
- [Cohort Retention Query](prompts/goal-examples.md#cohort-retention-query) - Create reusable retention SQL with hand-checked small samples.
- [Revenue Reconciliation](prompts/goal-examples.md#revenue-reconciliation) - Reconcile payments, orders, refunds, and finance definitions.
- [Event Taxonomy Cleanup](prompts/goal-examples.md#event-taxonomy-cleanup) - Deduplicate event names, properties, and version changes.
- [Anomaly Detection Baseline](prompts/goal-examples.md#anomaly-detection-baseline) - Backtest alert thresholds against historical metrics.
- [Attribution Window Review](prompts/goal-examples.md#attribution-window-review) - Verify campaign attribution windows and dedupe rules.
- [Self-Serve Data Contract](prompts/goal-examples.md#self-serve-data-contract) - Define trusted datasets and usage limits for business users.

### ai-evals
- [LLM Golden Set Build](prompts/goal-examples.md#llm-golden-set-build) - Build an eval set from real failures and frequent tasks.
- [LLM Regression Gate](prompts/goal-examples.md#llm-regression-gate) - Compare old and new model or prompt outputs in PRs.
- [Judge Calibration](prompts/goal-examples.md#judge-calibration) - Measure LLM judge agreement against human labels.
- [Hallucination Probe Suite](prompts/goal-examples.md#hallucination-probe-suite) - Add negative cases for nonexistent files, fields, APIs, and sources.
- [RAG Answer Faithfulness](prompts/goal-examples.md#rag-answer-faithfulness) - Check that answers are supported by retrieved evidence.
- [Tool Use Eval](prompts/goal-examples.md#tool-use-eval) - Evaluate whether an agent selects, orders, and validates tools correctly.
- [Prompt Injection Red Team](prompts/goal-examples.md#adversarial-prompt-redteam) - Test prompt leakage, unauthorized tools, and instruction override attempts.
- [Eval Data Dedup](prompts/goal-examples.md#eval-data-dedup) - Remove duplicates, leakage, and near-identical eval samples.
- [Cost Quality Frontier](prompts/goal-examples.md#cost-quality-frontier) - Compare models by quality, latency, and cost to choose routing tiers.
- [Rubric-Driven Eval](prompts/goal-examples.md#rubric-driven-eval) - Replace binary scores with multi-dimensional rubrics for complex tasks.

### ai-ops
- [Prompt Version Registry](prompts/goal-examples.md#prompt-version-registry) - Bind prompt versions to eval results and deployment history.
- [RAG Chunking Experiment](prompts/goal-examples.md#rag-chunking-experiment) - Compare chunk size, overlap, and metadata on retrieval and answer quality.
- [Vector Index Refresh](prompts/goal-examples.md#vector-index-refresh) - Verify document updates are indexed completely and can be rolled back.
- [Model Routing Policy](prompts/goal-examples.md#model-routing-policy) - Route by risk, cost, latency, and quality evidence.
- [LLM Timeout Budget](prompts/goal-examples.md#llm-timeout-budget) - Define timeout, retry, fallback, and user-visible error behavior.
- [Token Cost Attribution](prompts/goal-examples.md#token-cost-attribution) - Attribute model costs by user, feature, model, and request ID.
- [RAG Prompt Injection Filter](prompts/goal-examples.md#prompt-injection-filter) - Detect and isolate malicious instructions in retrieved documents.
- [AI Output Schema Guard](prompts/goal-examples.md#ai-output-schema-guard) - Validate structured AI output and fail or retry safely.
- [Human Review Threshold](prompts/goal-examples.md#human-review-threshold) - Escalate high-risk AI outputs based on confidence and policy rules.
- [AI Observability Traces](prompts/goal-examples.md#ai-observability-traces) - Trace prompts, retrieval, tools, models, scores, and request IDs.

### frontend
- [Empty State System](prompts/goal-examples.md#frontend-empty-states) - Design real empty states for lists, search, permissions, and first use.
- [Error Boundary Experience](prompts/goal-examples.md#frontend-error-boundary) - Add recoverable page and component fallback UI for crashes.
- [Loading Skeletons](prompts/goal-examples.md#frontend-loading-skeletons) - Replace layout-shifting spinners with stable skeleton states.
- [Form Validation](prompts/goal-examples.md#frontend-form-validation) - Cover inline, submit, server error, and dirty-state validation.
- [Data Table Density](prompts/goal-examples.md#frontend-table-density) - Improve columns, filters, sorting, pagination, and bulk actions.
- [Command Palette](prompts/goal-examples.md#frontend-command-palette) - Add a keyboard-first entry point for high-frequency actions.
- [Navigation Map](prompts/goal-examples.md#frontend-navigation-map) - Clarify primary navigation, breadcrumbs, and detail-page return paths.
- [State Recovery](prompts/goal-examples.md#frontend-state-recovery) - Restore filters and context after refresh, back, and deep links.
- [Permission State UI](prompts/goal-examples.md#frontend-permission-ui) - Separate unauthenticated, unauthorized, and missing-resource states.
- [Bulk Actions](prompts/goal-examples.md#frontend-bulk-actions) - Handle selection, confirm, undo, partial failure, and feedback.
- [Search Filter Experience](prompts/goal-examples.md#frontend-search-filter) - Unify search, filter chips, clear actions, and result counts.
- [Realtime Update Prompts](prompts/goal-examples.md#frontend-realtime-updates) - Handle background changes, conflicts, and refresh prompts.

### design
- [Visual Hierarchy Pass](prompts/goal-examples.md#design-visual-hierarchy) - Reorder headings, metadata, primary actions, and secondary actions.
- [Design Token Audit](prompts/goal-examples.md#design-token-audit) - Check colors, spacing, radii, and shadows against tokens.
- [Component Variant Matrix](prompts/goal-examples.md#design-component-variants) - Complete button, input, card, and modal state coverage.
- [Dashboard Layout Pass](prompts/goal-examples.md#design-dashboard-layout) - Make an operational dashboard easier to scan and compare.
- [Modal Discipline](prompts/goal-examples.md#design-modal-discipline) - Replace modal misuse with drawers, popovers, or pages where appropriate.
- [Iconography System](prompts/goal-examples.md#design-iconography) - Unify icon semantics for tools, statuses, and empty states.
- [Color Contrast Pass](prompts/goal-examples.md#design-color-contrast) - Fix low contrast text, icons, and state colors.
- [Motion Rules](prompts/goal-examples.md#design-motion-rules) - Define entry, exit, feedback, and reduced-motion behavior.
- [Responsive Grid](prompts/goal-examples.md#design-responsive-grid) - Define breakpoints, columns, and fixed-format constraints.
- [Toolbar Usability](prompts/goal-examples.md#design-toolbar-usability) - Improve icon buttons, tooltips, grouping, and disabled states.
- [Data Card System](prompts/goal-examples.md#design-data-card-system) - Define metric cards with value, trend, anomaly, and source states.
- [Brand Fit Pass](prompts/goal-examples.md#design-brand-fit) - Align the interface language with the product's audience and use case.

### mobile
- [Mobile Bottom Navigation](prompts/goal-examples.md#mobile-bottom-nav) - Design thumb-friendly mobile navigation for core paths.
- [Mobile Touch Targets](prompts/goal-examples.md#mobile-touch-targets) - Ensure buttons, checkboxes, and rows have usable tap areas.
- [Mobile Form Flow](prompts/goal-examples.md#mobile-form-flow) - Handle long forms, keyboard occlusion, and error positioning.
- [Mobile Table Adaptation](prompts/goal-examples.md#mobile-table-adaptation) - Convert wide tables into cards, horizontal scroll, or drill-downs.
- [Mobile Filter Drawer](prompts/goal-examples.md#mobile-filter-drawer) - Add mobile filters with apply, reset, count, and URL state.
- [Mobile Offline State](prompts/goal-examples.md#mobile-offline-state) - Show offline, cached data, and retry paths clearly.
- [Mobile Image Performance](prompts/goal-examples.md#mobile-image-performance) - Optimize image sizes, lazy loading, placeholders, and formats.
- [Mobile Safe Area](prompts/goal-examples.md#mobile-safe-area) - Handle iOS notch, bottom bars, and sticky actions.
- [Mobile Gesture Conflicts](prompts/goal-examples.md#mobile-gesture-conflicts) - Resolve conflicts between swipe, drag, and scroll interactions.
- [Mobile Login Flow](prompts/goal-examples.md#mobile-login-flow) - Improve magic link, OTP, password manager, and autofill behavior.
- [Mobile Onboarding](prompts/goal-examples.md#mobile-onboarding) - Create a short, skippable, restorable first-run path.
- [Mobile Device Matrix](prompts/goal-examples.md#mobile-device-matrix) - Cover small screen, large screen, iOS, and Android key paths.

### docs
- [Quickstart](prompts/goal-examples.md#docs-quickstart) - Write the shortest fresh-clone path that runs successfully in five minutes.
- [Install Troubleshooting](prompts/goal-examples.md#docs-install-troubleshooting) - Document common install failures, causes, and fixes.
- [API Examples](prompts/goal-examples.md#docs-api-examples) - Add minimal request, response, and error examples for core APIs.
- [Architecture Overview](prompts/goal-examples.md#docs-architecture-overview) - Explain module boundaries, data flow, and explicit non-goals.
- [Contribution Guide](prompts/goal-examples.md#docs-contribution-guide) - Document development, testing, commit, and PR review rules.
- [Release Notes](prompts/goal-examples.md#docs-release-notes) - Create user-facing change, migration, and breaking-change notes.
- [Environment Variables](prompts/goal-examples.md#docs-env-vars) - List env names, defaults, requiredness, and safety notes.
- [Operator Runbook](prompts/goal-examples.md#docs-runbook) - Document alerts, recovery, rollback, and data repair steps.
- [Architecture Decision Records](prompts/goal-examples.md#docs-decision-records) - Add ADR templates and indexes for major technical decisions.
- [Glossary](prompts/goal-examples.md#docs-glossary) - Unify product, engineering, and data-field terms.
- [Screenshot Docs](prompts/goal-examples.md#docs-screenshot-docs) - Add real screenshots and labels for UI workflows.
- [Docs Lint Gate](prompts/goal-examples.md#docs-docs-lint) - Add link, spelling, and executable code block checks.
- [Weekly Changelog Coverage](prompts/goal-examples.md#claude-weekly-changelog) - Ensure CHANGELOG.md includes an entry for every PR merged this week. _(source-backed)_

### product
- [User Journeys](prompts/goal-examples.md#product-user-journeys) - Map persona tasks into pages, events, and success states.
- [PRD Skeleton](prompts/goal-examples.md#product-prd-skeleton) - Write goals, non-goals, constraints, and acceptance criteria.
- [Onboarding Metrics](prompts/goal-examples.md#product-onboarding-metrics) - Define activation events, dropoff points, and dashboard queries.
- [Feature Prioritization](prompts/goal-examples.md#product-feature-prioritization) - Split MVP and later work by impact, cost, and risk.
- [Permission Model](prompts/goal-examples.md#product-permission-model) - Map roles, resources, actions, and UI visibility.
- [Notification Strategy](prompts/goal-examples.md#product-notification-strategy) - Define triggers, channels, frequency, and unsubscribe behavior.
- [Empty Data Policy](prompts/goal-examples.md#product-empty-data-policy) - Choose blank, sample data, import, or CTA by user state.
- [Upgrade Path](prompts/goal-examples.md#product-upgrade-path) - Design limits, paywalls, trials, and upgrade conversion paths.
- [Feedback Loop](prompts/goal-examples.md#product-feedback-loop) - Collect, classify, track, and close user feedback.
- [Search Relevance](prompts/goal-examples.md#product-search-relevance) - Define query handling, ranking, typo tolerance, and no-result behavior.
- [Admin Workflows](prompts/goal-examples.md#product-admin-workflows) - Design review, undo, audit log, and bulk moderation flows.
- [Success Criteria](prompts/goal-examples.md#product-success-criteria) - Define quantitative and qualitative completion measures for a feature.

### qa
- [Critical Path Tests](prompts/goal-examples.md#qa-critical-paths) - Cover signup, create, edit, delete, export, and recovery flows.
- [Regression Matrix](prompts/goal-examples.md#qa-regression-matrix) - Build feature/browser/role/data-state regression coverage.
- [Fixture Strategy](prompts/goal-examples.md#qa-fixture-strategy) - Create deterministic seed, mock, factory, and cleanup patterns.
- [Visual Regression](prompts/goal-examples.md#qa-visual-regression) - Add screenshot diffs for critical pages with controlled thresholds.
- [API Contracts](prompts/goal-examples.md#qa-api-contracts) - Validate frontend/backend schema, error codes, and boundary values.
- [Flaky Test Audit](prompts/goal-examples.md#qa-flaky-test-audit) - Find unstable tests and fix waits, isolation, or fixtures.
- [Error Injection](prompts/goal-examples.md#qa-error-injection) - Simulate 500s, timeouts, network failure, and partial success.
- [Cross-Browser Coverage](prompts/goal-examples.md#qa-cross-browser) - Run critical flows across Chromium, Firefox, and WebKit.
- [Release Smoke](prompts/goal-examples.md#qa-release-smoke) - Define the smallest pre-release verification checklist.
- [Data Migration Test](prompts/goal-examples.md#qa-data-migration) - Verify counts, constraints, and rollback around data migration.
- [Security Smoke](prompts/goal-examples.md#qa-security-smoke) - Check auth, permission bypass, and sensitive info leakage.
- [Bug Reproduction Template](prompts/goal-examples.md#qa-bug-repro-template) - Standardize environment, steps, expected, actual, and evidence.

### accessibility
- [Keyboard Navigation](prompts/goal-examples.md#accessibility-keyboard-nav) - Ensure the whole app works with Tab, Enter, and Escape.
- [Screen Reader Semantics](prompts/goal-examples.md#accessibility-screen-reader) - Check landmarks, labels, aria-live, and button names.
- [Focus Visible](prompts/goal-examples.md#accessibility-focus-visible) - Give every interactive element a clear focus state.
- [Color Contrast](prompts/goal-examples.md#accessibility-color-contrast) - Meet WCAG AA for text, icons, and state colors.
- [Accessible Form Errors](prompts/goal-examples.md#accessibility-form-errors) - Associate errors with fields so screen readers announce them.
- [Modal Focus Trap](prompts/goal-examples.md#accessibility-modal-trap) - Focus opens, cycles, closes, and returns correctly.
- [Reduced Motion](prompts/goal-examples.md#accessibility-reduced-motion) - Respect prefers-reduced-motion for all nonessential motion.
- [Alt Text Audit](prompts/goal-examples.md#accessibility-alt-text) - Separate decorative, content, and product images.
- [Heading Order](prompts/goal-examples.md#accessibility-heading-order) - Fix skipped headings and fake styled headings.
- [Live Region Feedback](prompts/goal-examples.md#accessibility-live-region) - Announce toasts, async completion, and errors accessibly.
- [Touch Accessibility](prompts/goal-examples.md#accessibility-touch-a11y) - Check tap targets, zoom, and orientation on mobile.
- [Accessibility Audit Report](prompts/goal-examples.md#accessibility-audit-report) - Produce prioritized issues, impact, fixes, and acceptance checks.

### performance
- [LCP Optimization](prompts/goal-examples.md#performance-lcp) - Find and optimize the largest contentful paint element.
- [CLS Fix](prompts/goal-examples.md#performance-cls) - Reserve space for images, ads, and dynamic content.
- [INP Optimization](prompts/goal-examples.md#performance-inp) - Reduce long tasks and blocking interaction handlers.
- [Bundle Budget](prompts/goal-examples.md#performance-bundle-budget) - Set route and dependency size budgets in CI.
- [Code Splitting](prompts/goal-examples.md#performance-code-splitting) - Lazy-load low-frequency routes, charts, and editors.
- [Image Pipeline](prompts/goal-examples.md#performance-image-pipeline) - Use srcset, modern formats, lazy loading, and cache headers.
- [Font Loading](prompts/goal-examples.md#performance-font-loading) - Optimize font-display, subsets, and preload hints.
- [API Waterfall](prompts/goal-examples.md#performance-api-waterfall) - Remove serial requests and prefetch critical data.
- [Cache Strategy](prompts/goal-examples.md#performance-cache-strategy) - Define browser, CDN, and service-worker cache boundaries.
- [Memory Leak Audit](prompts/goal-examples.md#performance-memory-leaks) - Check long sessions, lists, subscriptions, and charts for leaks.
- [Render Count Audit](prompts/goal-examples.md#performance-render-count) - Find unnecessary React renders and expensive selectors.
- [Performance CI Gate](prompts/goal-examples.md#performance-ci-gate) - Add Lighthouse or trace thresholds to CI.
- [Lighthouse And Core Web Vitals Gate](prompts/goal-examples.md#explainx-lighthouse-core-web-vitals) - Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions. _(source-backed)_

### workflow
- [Goal Prompt Writer](prompts/goal-examples.md#goal-meta-prompt-writer) - Ask the agent to inspect a repo and write a precise goal prompt before execution.
- [Goal Continuation Audit](prompts/goal-examples.md#goal-continuation-audit) - Check that a long-running goal keeps its done_when and verification contract after compaction.
- [Verifiable End-State Contract](prompts/goal-examples.md#codex-verifiable-end-state) - Complete one objective only when a verifiable end state is met. _(source-backed)_
- [Four Files Walkthrough](prompts/goal-examples.md#hermes-four-files-walkthrough) - Create four note files across turns and verify each contains its number. _(source-backed)_

### migration
- [Visual Migration With Playwright](prompts/goal-examples.md#codex-visual-migration-playwright) - Migrate a project while preserving screen output and checking it with Playwright. _(source-backed)_
- [Feature Port With CI Green](prompts/goal-examples.md#hermes-feature-port-ci-green) - Port a feature from another repo, include tests, and get CI green. _(source-backed)_
- [Vue 2 To Vue 3 Visual And Unit Gate](prompts/goal-examples.md#qiita-vue2-vue3-visual-unit) - Migrate listed Vue screens and stop only when visual and unit tests pass. _(source-backed)_

### prototype
- [PLAN.md Milestone Prototype](prompts/goal-examples.md#codex-plan-milestone-prototype) - Implement a PLAN.md-driven prototype with tests at each milestone and browser verification. _(source-backed)_
- [Canvas Puzzle PLAN.md Prototype](prompts/goal-examples.md#qiita-canvas-puzzle-plan) - Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes. _(source-backed)_

### prompt-optimization
- [Eval-Driven Prompt Optimization](prompts/goal-examples.md#codex-eval-prompt-optimization) - Optimize prompts against an eval suite until the target score or pass rate is reached. _(source-backed)_
- [Router Prompt Eval Score](prompts/goal-examples.md#qiita-router-eval-score) - Improve a router prompt against an eval directory until the result score reaches a target. _(source-backed)_

### testing
- [Auth Tests And Lint Clean](prompts/goal-examples.md#claude-auth-tests-lint) - Keep working until auth tests pass and the lint step is clean. _(source-backed)_
- [Ruff Clean Source Tree](prompts/goal-examples.md#hermes-ruff-src-clean) - Fix every lint error in src and prove ruff passes. _(source-backed)_
- [TypeScript ESLint Coverage Gate](prompts/goal-examples.md#explainx-typescript-eslint-coverage) - Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold. _(source-backed)_

### investigation
- [Session Drift Report](prompts/goal-examples.md#hermes-session-drift-report) - Investigate session ID drift during mid-run compression and write a report. _(source-backed)_

### cli
- [EXIF Rename CLI](prompts/goal-examples.md#hermes-exif-rename-cli) - Build a small CLI that renames photos by EXIF date and test it on a photos folder. _(source-backed)_

### refactor
- [Auth Dependency Injection Refactor](prompts/goal-examples.md#explainx-auth-di-refactor) - Refactor auth code to dependency injection while preserving tests, coverage, and public API. _(source-backed)_

## Templates

- [Full template](templates/full-goal-template.md) for high-risk or multi-step work.
- [Compact template](templates/compact-goal-template.md) for routine work.
- [Structured JSON data](data/examples.json) for search, tooling, or site generation.

## Quality Bar

- One example should cover one measurable objective.
- The prompt must include verification that can run in a real repository or produce a concrete artifact.
- New externally sourced examples must include `source_name` and `source_url` in `data/examples.json`.
- Do not add undocumented slash-command behavior, fake tool capabilities, or examples copied from private/non-verifiable sources.

## Sources And Caveats

See [SOURCES.md](SOURCES.md) for public sources used by source-backed examples and notes about cross-tool differences.

This repository does not claim that `/goal` behaves identically across Codex, Claude Code, Hermes, or other tools.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding examples. Keep descriptions short, source-backed when based on external material, and scoped to verifiable engineering work.

## License

MIT

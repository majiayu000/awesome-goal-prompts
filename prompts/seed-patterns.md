# Seed Goal Patterns

These reusable patterns are not presented as collected from public sources. Prefer source-backed contracts first when credibility matters.

## Index

### backend-api
<a id="api-contract-drift-audit"></a>
- [API Contract Drift Audit](goal-examples.md#api-contract-drift-audit) - Compare OpenAPI, implementation, and tests to find field or status-code drift.
<a id="idempotent-create-endpoint"></a>
- [Idempotent Create Endpoint](goal-examples.md#idempotent-create-endpoint) - Add idempotency keys and replay-safe semantics to a create endpoint.
<a id="api-error-taxonomy"></a>
- [API Error Taxonomy](goal-examples.md#api-error-taxonomy) - Unify HTTP status codes, machine error codes, user messages, and logs.
<a id="pagination-consistency"></a>
- [Pagination Consistency](goal-examples.md#pagination-consistency) - Fix cursor or offset pagination so rows are not skipped, duplicated, or reordered.
<a id="request-validation-boundary"></a>
- [Request Validation Boundary](goal-examples.md#request-validation-boundary) - Move input validation to the API boundary and reject unknown fields.
<a id="api-rate-limit-policy"></a>
- [API Rate Limit Policy](goal-examples.md#api-rate-limit-policy) - Implement rate limit behavior, headers, and over-limit responses for critical routes.
<a id="webhook-retry-contract"></a>
- [Webhook Retry Contract](goal-examples.md#webhook-retry-contract) - Define webhook signature verification, retry, dedupe, and failure observability.
<a id="backward-compatible-response"></a>
- [Backward-Compatible Response](goal-examples.md#backward-compatible-response) - Add response fields without breaking old clients and document removal paths.
<a id="grpc-timeout-propagation"></a>
- [gRPC Timeout Propagation](goal-examples.md#grpc-timeout-propagation) - Propagate deadlines across service calls and cancel work correctly.
<a id="async-job-state-machine"></a>
- [Async Job State Machine](goal-examples.md#async-job-state-machine) - Make async job transitions explicit and tested across pending/running/succeeded/failed/canceled.
<a id="authz-resource-scope"></a>
- [Resource-Level Authorization](goal-examples.md#authz-resource-scope) - Prevent logged-in users from accessing resources they do not own.
<a id="api-versioning-plan"></a>
- [API Versioning Plan](goal-examples.md#api-versioning-plan) - Create a v1/v2 coexistence plan with deprecation headers and migration tests.

### backend-data
<a id="db-migration-safety"></a>
- [Database Migration Safety](goal-examples.md#db-migration-safety) - Review a migration for rollback, online execution, and lock risk.
<a id="transaction-boundary-audit"></a>
- [Transaction Boundary Audit](goal-examples.md#transaction-boundary-audit) - Find missing or oversized transactions in multi-table write paths.
<a id="cache-invalidation-map"></a>
- [Cache Invalidation Map](goal-examples.md#cache-invalidation-map) - Map write paths to cache keys and fix stale reads.
<a id="n-plus-one-query-fix"></a>
- [N+1 Query Fix](goal-examples.md#n-plus-one-query-fix) - Reduce list endpoint query count with batching or preloading.
<a id="optimistic-locking-rollout"></a>
- [Optimistic Locking Rollout](goal-examples.md#optimistic-locking-rollout) - Add version checks and conflict responses for concurrent edits.
<a id="soft-delete-integrity"></a>
- [Soft Delete Integrity](goal-examples.md#soft-delete-integrity) - Make queries, unique indexes, and restore flows respect soft deletion.
<a id="db-index-regression"></a>
- [Index Regression Check](goal-examples.md#db-index-regression) - Add or adjust indexes and prove read gains do not create unacceptable write cost.
<a id="outbox-pattern-adoption"></a>
- [Outbox Reliable Events](goal-examples.md#outbox-pattern-adoption) - Use an outbox table to prevent lost events after successful database commits.
<a id="read-replica-lag-guard"></a>
- [Read Replica Lag Guard](goal-examples.md#read-replica-lag-guard) - Prevent write-after-read paths from hitting stale replicas.
<a id="schema-drift-detector"></a>
- [Schema Drift Detector](goal-examples.md#schema-drift-detector) - Compare ORM models, migrations, and the live database schema.

### devops-ci
<a id="ci-flaky-test-triage"></a>
- [CI Flaky Test Triage](goal-examples.md#ci-flaky-test-triage) - Identify flaky tests, separate real failures, and fix unstable waits or fixtures.
<a id="build-cache-correctness"></a>
- [Build Cache Correctness](goal-examples.md#build-cache-correctness) - Check whether CI cache keys cause stale dependencies or cross-branch pollution.
<a id="dependency-update-gate"></a>
- [Dependency Update Gate](goal-examples.md#dependency-update-gate) - Add dependency upgrade checks for tests, licenses, and vulnerabilities.
<a id="monorepo-affected-tests"></a>
- [Monorepo Affected Tests](goal-examples.md#monorepo-affected-tests) - Run only affected tests without missing cross-package contracts.
<a id="release-note-from-diff"></a>
- [Release Notes From Diff](goal-examples.md#release-note-from-diff) - Generate user-facing release notes from commits, PR labels, and breaking changes.
<a id="artifact-provenance"></a>
- [Artifact Provenance](goal-examples.md#artifact-provenance) - Trace a package or image back to the commit and workflow that produced it.
<a id="ci-permission-minimize"></a>
- [CI Permission Minimization](goal-examples.md#ci-permission-minimize) - Tighten GitHub Actions token permissions without breaking workflows.
<a id="branch-protection-audit"></a>
- [Branch Protection Audit](goal-examples.md#branch-protection-audit) - Audit required checks, reviews, linear history, and admin bypasses.
<a id="release-rollback-drill"></a>
- [Release Rollback Drill](goal-examples.md#release-rollback-drill) - Create and test a rollback path for the latest release.
<a id="semantic-version-check"></a>
- [Semantic Version Check](goal-examples.md#semantic-version-check) - Infer the correct semver bump from API, behavior, and changelog diffs.

### devops-runtime
<a id="docker-image-slimming"></a>
- [Docker Image Slimming](goal-examples.md#docker-image-slimming) - Reduce image size while keeping runtime dependencies and security scans green.
<a id="k8s-readiness-liveness"></a>
- [Kubernetes Probe Repair](goal-examples.md#k8s-readiness-liveness) - Separate startup, readiness, and liveness probes to avoid bad restarts.
<a id="terraform-plan-review"></a>
- [Terraform Plan Review](goal-examples.md#terraform-plan-review) - Review infrastructure changes for deletes, replacements, and permission expansion.
<a id="helm-values-drift"></a>
- [Helm Values Drift](goal-examples.md#helm-values-drift) - Compare environment values to find hidden staging/prod differences.
<a id="autoscaling-thresholds"></a>
- [Autoscaling Thresholds](goal-examples.md#autoscaling-thresholds) - Tune HPA or worker scaling thresholds against real load and queue depth.
<a id="runtime-config-validation"></a>
- [Runtime Config Validation](goal-examples.md#runtime-config-validation) - Fail startup on missing or invalid environment and config values.
<a id="zero-downtime-migration"></a>
- [Zero-Downtime Migration](goal-examples.md#zero-downtime-migration) - Plan and verify expand-migrate-contract deployment steps.
<a id="observability-minimum"></a>
- [Observability Minimum](goal-examples.md#observability-minimum) - Add logs, metrics, traces, and alerts for a service's critical paths.
<a id="incident-runbook-gap"></a>
- [Incident Runbook Gap](goal-examples.md#incident-runbook-gap) - Turn a recent incident timeline into missing runbook and alert updates.
<a id="queue-backpressure"></a>
- [Queue Backpressure](goal-examples.md#queue-backpressure) - Protect databases and external APIs when worker queues build up.

### security-appsec
<a id="sql-injection-audit"></a>
- [SQL Injection Audit](goal-examples.md#sql-injection-audit) - Replace SQL string concatenation with parameterized queries and tests.
<a id="command-injection-audit"></a>
- [Command Injection Audit](goal-examples.md#command-injection-audit) - Replace shell string execution with argument arrays and validation.
<a id="ssrf-defense-review"></a>
- [SSRF Defense Review](goal-examples.md#ssrf-defense-review) - Add URL allowlists and DNS/IP checks for fetch or callback features.
<a id="xss-output-encoding"></a>
- [XSS Output Encoding](goal-examples.md#xss-output-encoding) - Audit HTML and Markdown rendering for unsafe sinks and missing encoding.
<a id="csrf-sensitive-action"></a>
- [CSRF Sensitive Action](goal-examples.md#csrf-sensitive-action) - Protect cookie-authenticated writes from cross-site requests.
<a id="auth-bypass-route-map"></a>
- [Auth Bypass Route Map](goal-examples.md#auth-bypass-route-map) - Enumerate routes and verify unauthenticated and unauthorized behavior.
<a id="file-upload-security"></a>
- [File Upload Security](goal-examples.md#file-upload-security) - Validate MIME, extension, size, scanning, and storage isolation.
<a id="tenant-isolation-test"></a>
- [Tenant Isolation Test](goal-examples.md#tenant-isolation-test) - Verify tenant IDs are enforced in queries, caches, and background jobs.
<a id="replay-attack-defense"></a>
- [Replay Attack Defense](goal-examples.md#replay-attack-defense) - Add nonce, timestamp, and expiration checks to signed requests.
<a id="insecure-direct-object-ref"></a>
- [IDOR Audit](goal-examples.md#insecure-direct-object-ref) - Verify direct object ID access always checks ownership or scope.

### security-ops
<a id="secret-scan-baseline"></a>
- [Secret Scan Baseline](goal-examples.md#secret-scan-baseline) - Add secret scanning and triage historical findings safely.
<a id="iam-least-privilege"></a>
- [IAM Least Privilege](goal-examples.md#iam-least-privilege) - Reduce cloud permissions to observed API usage and documented needs.
<a id="github-actions-supply-chain"></a>
- [GitHub Actions Supply Chain](goal-examples.md#github-actions-supply-chain) - Pin third-party actions and review workflow permissions.
<a id="container-vuln-triage"></a>
- [Container Vulnerability Triage](goal-examples.md#container-vuln-triage) - Prioritize image CVEs by exploitability and runtime exposure.
<a id="audit-log-coverage"></a>
- [Audit Log Coverage](goal-examples.md#audit-log-coverage) - Add audit logs for login, permission changes, and sensitive data access.
<a id="secret-rotation-drill"></a>
- [Secret Rotation Drill](goal-examples.md#secret-rotation-drill) - Verify rotating a key does not interrupt the service.
<a id="dependency-confusion-guard"></a>
- [Dependency Confusion Guard](goal-examples.md#dependency-confusion-guard) - Lock private package scopes and registries to prevent wrong-source installs.
<a id="sbom-generation"></a>
- [SBOM Generation](goal-examples.md#sbom-generation) - Generate an SBOM and attach it to release artifacts.
<a id="prod-access-review"></a>
- [Production Access Review](goal-examples.md#prod-access-review) - Inventory production access, approval paths, and audit evidence.
<a id="backup-restore-security"></a>
- [Backup Restore Security](goal-examples.md#backup-restore-security) - Verify encrypted backups and a restricted restore path.

### data-eng
<a id="etl-contract-tests"></a>
- [ETL Contract Tests](goal-examples.md#etl-contract-tests) - Add schema and sample-data contracts between source and target tables.
<a id="data-quality-rules"></a>
- [Data Quality Rules](goal-examples.md#data-quality-rules) - Define null, uniqueness, range, and reference checks for key datasets.
<a id="backfill-safety-plan"></a>
- [Backfill Safety Plan](goal-examples.md#backfill-safety-plan) - Design a sharded, resumable, verifiable historical backfill.
<a id="incremental-load-watermark"></a>
- [Incremental Load Watermark](goal-examples.md#incremental-load-watermark) - Fix missing or duplicate rows in incremental sync logic.
<a id="late-arriving-data"></a>
- [Late-Arriving Data](goal-examples.md#late-arriving-data) - Handle delayed events and metric corrections safely.
<a id="data-lineage-map"></a>
- [Data Lineage Map](goal-examples.md#data-lineage-map) - Map critical report fields from source to consumers.
<a id="pii-classification"></a>
- [PII Classification](goal-examples.md#pii-classification) - Classify sensitive fields and document masking rules.
<a id="data-retention-enforcement"></a>
- [Data Retention Enforcement](goal-examples.md#data-retention-enforcement) - Verify expiration, archival, deletion, and audit behavior.
<a id="warehouse-cost-audit"></a>
- [Warehouse Cost Audit](goal-examples.md#warehouse-cost-audit) - Find expensive queries, duplicate tables, and unused scheduled jobs.
<a id="stream-processing-lag"></a>
- [Stream Processing Lag](goal-examples.md#stream-processing-lag) - Diagnose Kafka/Flink/Spark lag and checkpoint bottlenecks.

### data-analytics
<a id="metric-definition-lock"></a>
- [Metric Definition Lock](goal-examples.md#metric-definition-lock) - Turn core metric definitions into tested SQL or semantic-layer checks.
<a id="dashboard-trust-audit"></a>
- [Dashboard Trust Audit](goal-examples.md#dashboard-trust-audit) - Check filters, timezone, refresh cadence, permissions, and source reconciliation.
<a id="ab-test-srm-check"></a>
- [A/B Test SRM Check](goal-examples.md#ab-test-srm-check) - Detect sample ratio mismatch in experiment assignment.
<a id="funnel-dropoff-diagnosis"></a>
- [Funnel Dropoff Diagnosis](goal-examples.md#funnel-dropoff-diagnosis) - Validate funnel events, step counts, and latency before interpreting dropoff.
<a id="cohort-retention-query"></a>
- [Cohort Retention Query](goal-examples.md#cohort-retention-query) - Create reusable retention SQL with hand-checked small samples.
<a id="revenue-reconciliation"></a>
- [Revenue Reconciliation](goal-examples.md#revenue-reconciliation) - Reconcile payments, orders, refunds, and finance definitions.
<a id="event-taxonomy-cleanup"></a>
- [Event Taxonomy Cleanup](goal-examples.md#event-taxonomy-cleanup) - Deduplicate event names, properties, and version changes.
<a id="anomaly-detection-baseline"></a>
- [Anomaly Detection Baseline](goal-examples.md#anomaly-detection-baseline) - Backtest alert thresholds against historical metrics.
<a id="attribution-window-review"></a>
- [Attribution Window Review](goal-examples.md#attribution-window-review) - Verify campaign attribution windows and dedupe rules.
<a id="self-serve-data-contract"></a>
- [Self-Serve Data Contract](goal-examples.md#self-serve-data-contract) - Define trusted datasets and usage limits for business users.

### ai-evals
<a id="llm-golden-set-build"></a>
- [LLM Golden Set Build](goal-examples.md#llm-golden-set-build) - Build an eval set from real failures and frequent tasks.
<a id="llm-regression-gate"></a>
- [LLM Regression Gate](goal-examples.md#llm-regression-gate) - Compare old and new model or prompt outputs in PRs.
<a id="judge-calibration"></a>
- [Judge Calibration](goal-examples.md#judge-calibration) - Measure LLM judge agreement against human labels.
<a id="hallucination-probe-suite"></a>
- [Hallucination Probe Suite](goal-examples.md#hallucination-probe-suite) - Add negative cases for nonexistent files, fields, APIs, and sources.
<a id="rag-answer-faithfulness"></a>
- [RAG Answer Faithfulness](goal-examples.md#rag-answer-faithfulness) - Check that answers are supported by retrieved evidence.
<a id="tool-use-eval"></a>
- [Tool Use Eval](goal-examples.md#tool-use-eval) - Evaluate whether an agent selects, orders, and validates tools correctly.
<a id="adversarial-prompt-redteam"></a>
- [Prompt Injection Red Team](goal-examples.md#adversarial-prompt-redteam) - Test prompt leakage, unauthorized tools, and instruction override attempts.
<a id="eval-data-dedup"></a>
- [Eval Data Dedup](goal-examples.md#eval-data-dedup) - Remove duplicates, leakage, and near-identical eval samples.
<a id="cost-quality-frontier"></a>
- [Cost Quality Frontier](goal-examples.md#cost-quality-frontier) - Compare models by quality, latency, and cost to choose routing tiers.
<a id="rubric-driven-eval"></a>
- [Rubric-Driven Eval](goal-examples.md#rubric-driven-eval) - Replace binary scores with multi-dimensional rubrics for complex tasks.

### ai-ops
<a id="prompt-version-registry"></a>
- [Prompt Version Registry](goal-examples.md#prompt-version-registry) - Bind prompt versions to eval results and deployment history.
<a id="rag-chunking-experiment"></a>
- [RAG Chunking Experiment](goal-examples.md#rag-chunking-experiment) - Compare chunk size, overlap, and metadata on retrieval and answer quality.
<a id="vector-index-refresh"></a>
- [Vector Index Refresh](goal-examples.md#vector-index-refresh) - Verify document updates are indexed completely and can be rolled back.
<a id="model-routing-policy"></a>
- [Model Routing Policy](goal-examples.md#model-routing-policy) - Route by risk, cost, latency, and quality evidence.
<a id="llm-timeout-budget"></a>
- [LLM Timeout Budget](goal-examples.md#llm-timeout-budget) - Define timeout, retry, fallback, and user-visible error behavior.
<a id="token-cost-attribution"></a>
- [Token Cost Attribution](goal-examples.md#token-cost-attribution) - Attribute model costs by user, feature, model, and request ID.
<a id="prompt-injection-filter"></a>
- [RAG Prompt Injection Filter](goal-examples.md#prompt-injection-filter) - Detect and isolate malicious instructions in retrieved documents.
<a id="ai-output-schema-guard"></a>
- [AI Output Schema Guard](goal-examples.md#ai-output-schema-guard) - Validate structured AI output and fail or retry safely.
<a id="human-review-threshold"></a>
- [Human Review Threshold](goal-examples.md#human-review-threshold) - Escalate high-risk AI outputs based on confidence and policy rules.
<a id="ai-observability-traces"></a>
- [AI Observability Traces](goal-examples.md#ai-observability-traces) - Trace prompts, retrieval, tools, models, scores, and request IDs.

### frontend
<a id="frontend-empty-states"></a>
- [Empty State System](goal-examples.md#frontend-empty-states) - Design real empty states for lists, search, permissions, and first use.
<a id="frontend-error-boundary"></a>
- [Error Boundary Experience](goal-examples.md#frontend-error-boundary) - Add recoverable page and component fallback UI for crashes.
<a id="frontend-loading-skeletons"></a>
- [Loading Skeletons](goal-examples.md#frontend-loading-skeletons) - Replace layout-shifting spinners with stable skeleton states.
<a id="frontend-form-validation"></a>
- [Form Validation](goal-examples.md#frontend-form-validation) - Cover inline, submit, server error, and dirty-state validation.
<a id="frontend-table-density"></a>
- [Data Table Density](goal-examples.md#frontend-table-density) - Improve columns, filters, sorting, pagination, and bulk actions.
<a id="frontend-command-palette"></a>
- [Command Palette](goal-examples.md#frontend-command-palette) - Add a keyboard-first entry point for high-frequency actions.
<a id="frontend-navigation-map"></a>
- [Navigation Map](goal-examples.md#frontend-navigation-map) - Clarify primary navigation, breadcrumbs, and detail-page return paths.
<a id="frontend-state-recovery"></a>
- [State Recovery](goal-examples.md#frontend-state-recovery) - Restore filters and context after refresh, back, and deep links.
<a id="frontend-permission-ui"></a>
- [Permission State UI](goal-examples.md#frontend-permission-ui) - Separate unauthenticated, unauthorized, and missing-resource states.
<a id="frontend-bulk-actions"></a>
- [Bulk Actions](goal-examples.md#frontend-bulk-actions) - Handle selection, confirm, undo, partial failure, and feedback.
<a id="frontend-search-filter"></a>
- [Search Filter Experience](goal-examples.md#frontend-search-filter) - Unify search, filter chips, clear actions, and result counts.
<a id="frontend-realtime-updates"></a>
- [Realtime Update Prompts](goal-examples.md#frontend-realtime-updates) - Handle background changes, conflicts, and refresh prompts.

### design
<a id="design-visual-hierarchy"></a>
- [Visual Hierarchy Pass](goal-examples.md#design-visual-hierarchy) - Reorder headings, metadata, primary actions, and secondary actions.
<a id="design-token-audit"></a>
- [Design Token Audit](goal-examples.md#design-token-audit) - Check colors, spacing, radii, and shadows against tokens.
<a id="design-component-variants"></a>
- [Component Variant Matrix](goal-examples.md#design-component-variants) - Complete button, input, card, and modal state coverage.
<a id="design-dashboard-layout"></a>
- [Dashboard Layout Pass](goal-examples.md#design-dashboard-layout) - Make an operational dashboard easier to scan and compare.
<a id="design-modal-discipline"></a>
- [Modal Discipline](goal-examples.md#design-modal-discipline) - Replace modal misuse with drawers, popovers, or pages where appropriate.
<a id="design-iconography"></a>
- [Iconography System](goal-examples.md#design-iconography) - Unify icon semantics for tools, statuses, and empty states.
<a id="design-color-contrast"></a>
- [Color Contrast Pass](goal-examples.md#design-color-contrast) - Fix low contrast text, icons, and state colors.
<a id="design-motion-rules"></a>
- [Motion Rules](goal-examples.md#design-motion-rules) - Define entry, exit, feedback, and reduced-motion behavior.
<a id="design-responsive-grid"></a>
- [Responsive Grid](goal-examples.md#design-responsive-grid) - Define breakpoints, columns, and fixed-format constraints.
<a id="design-toolbar-usability"></a>
- [Toolbar Usability](goal-examples.md#design-toolbar-usability) - Improve icon buttons, tooltips, grouping, and disabled states.
<a id="design-data-card-system"></a>
- [Data Card System](goal-examples.md#design-data-card-system) - Define metric cards with value, trend, anomaly, and source states.
<a id="design-brand-fit"></a>
- [Brand Fit Pass](goal-examples.md#design-brand-fit) - Align the interface language with the product's audience and use case.

### mobile
<a id="mobile-bottom-nav"></a>
- [Mobile Bottom Navigation](goal-examples.md#mobile-bottom-nav) - Design thumb-friendly mobile navigation for core paths.
<a id="mobile-touch-targets"></a>
- [Mobile Touch Targets](goal-examples.md#mobile-touch-targets) - Ensure buttons, checkboxes, and rows have usable tap areas.
<a id="mobile-form-flow"></a>
- [Mobile Form Flow](goal-examples.md#mobile-form-flow) - Handle long forms, keyboard occlusion, and error positioning.
<a id="mobile-table-adaptation"></a>
- [Mobile Table Adaptation](goal-examples.md#mobile-table-adaptation) - Convert wide tables into cards, horizontal scroll, or drill-downs.
<a id="mobile-filter-drawer"></a>
- [Mobile Filter Drawer](goal-examples.md#mobile-filter-drawer) - Add mobile filters with apply, reset, count, and URL state.
<a id="mobile-offline-state"></a>
- [Mobile Offline State](goal-examples.md#mobile-offline-state) - Show offline, cached data, and retry paths clearly.
<a id="mobile-image-performance"></a>
- [Mobile Image Performance](goal-examples.md#mobile-image-performance) - Optimize image sizes, lazy loading, placeholders, and formats.
<a id="mobile-safe-area"></a>
- [Mobile Safe Area](goal-examples.md#mobile-safe-area) - Handle iOS notch, bottom bars, and sticky actions.
<a id="mobile-gesture-conflicts"></a>
- [Mobile Gesture Conflicts](goal-examples.md#mobile-gesture-conflicts) - Resolve conflicts between swipe, drag, and scroll interactions.
<a id="mobile-login-flow"></a>
- [Mobile Login Flow](goal-examples.md#mobile-login-flow) - Improve magic link, OTP, password manager, and autofill behavior.
<a id="mobile-onboarding"></a>
- [Mobile Onboarding](goal-examples.md#mobile-onboarding) - Create a short, skippable, restorable first-run path.
<a id="mobile-device-matrix"></a>
- [Mobile Device Matrix](goal-examples.md#mobile-device-matrix) - Cover small screen, large screen, iOS, and Android key paths.

### docs
<a id="docs-quickstart"></a>
- [Quickstart](goal-examples.md#docs-quickstart) - Write the shortest fresh-clone path that runs successfully in five minutes.
<a id="docs-install-troubleshooting"></a>
- [Install Troubleshooting](goal-examples.md#docs-install-troubleshooting) - Document common install failures, causes, and fixes.
<a id="docs-api-examples"></a>
- [API Examples](goal-examples.md#docs-api-examples) - Add minimal request, response, and error examples for core APIs.
<a id="docs-architecture-overview"></a>
- [Architecture Overview](goal-examples.md#docs-architecture-overview) - Explain module boundaries, data flow, and explicit non-goals.
<a id="docs-contribution-guide"></a>
- [Contribution Guide](goal-examples.md#docs-contribution-guide) - Document development, testing, commit, and PR review rules.
<a id="docs-release-notes"></a>
- [Release Notes](goal-examples.md#docs-release-notes) - Create user-facing change, migration, and breaking-change notes.
<a id="docs-env-vars"></a>
- [Environment Variables](goal-examples.md#docs-env-vars) - List env names, defaults, requiredness, and safety notes.
<a id="docs-runbook"></a>
- [Operator Runbook](goal-examples.md#docs-runbook) - Document alerts, recovery, rollback, and data repair steps.
<a id="docs-decision-records"></a>
- [Architecture Decision Records](goal-examples.md#docs-decision-records) - Add ADR templates and indexes for major technical decisions.
<a id="docs-glossary"></a>
- [Glossary](goal-examples.md#docs-glossary) - Unify product, engineering, and data-field terms.
<a id="docs-screenshot-docs"></a>
- [Screenshot Docs](goal-examples.md#docs-screenshot-docs) - Add real screenshots and labels for UI workflows.
<a id="docs-docs-lint"></a>
- [Docs Lint Gate](goal-examples.md#docs-docs-lint) - Add link, spelling, and executable code block checks.

### product
<a id="product-user-journeys"></a>
- [User Journeys](goal-examples.md#product-user-journeys) - Map persona tasks into pages, events, and success states.
<a id="product-prd-skeleton"></a>
- [PRD Skeleton](goal-examples.md#product-prd-skeleton) - Write goals, non-goals, constraints, and acceptance criteria.
<a id="product-onboarding-metrics"></a>
- [Onboarding Metrics](goal-examples.md#product-onboarding-metrics) - Define activation events, dropoff points, and dashboard queries.
<a id="product-feature-prioritization"></a>
- [Feature Prioritization](goal-examples.md#product-feature-prioritization) - Split MVP and later work by impact, cost, and risk.
<a id="product-permission-model"></a>
- [Permission Model](goal-examples.md#product-permission-model) - Map roles, resources, actions, and UI visibility.
<a id="product-notification-strategy"></a>
- [Notification Strategy](goal-examples.md#product-notification-strategy) - Define triggers, channels, frequency, and unsubscribe behavior.
<a id="product-empty-data-policy"></a>
- [Empty Data Policy](goal-examples.md#product-empty-data-policy) - Choose blank, sample data, import, or CTA by user state.
<a id="product-upgrade-path"></a>
- [Upgrade Path](goal-examples.md#product-upgrade-path) - Design limits, paywalls, trials, and upgrade conversion paths.
<a id="product-feedback-loop"></a>
- [Feedback Loop](goal-examples.md#product-feedback-loop) - Collect, classify, track, and close user feedback.
<a id="product-search-relevance"></a>
- [Search Relevance](goal-examples.md#product-search-relevance) - Define query handling, ranking, typo tolerance, and no-result behavior.
<a id="product-admin-workflows"></a>
- [Admin Workflows](goal-examples.md#product-admin-workflows) - Design review, undo, audit log, and bulk moderation flows.
<a id="product-success-criteria"></a>
- [Success Criteria](goal-examples.md#product-success-criteria) - Define quantitative and qualitative completion measures for a feature.

### qa
<a id="qa-critical-paths"></a>
- [Critical Path Tests](goal-examples.md#qa-critical-paths) - Cover signup, create, edit, delete, export, and recovery flows.
<a id="qa-regression-matrix"></a>
- [Regression Matrix](goal-examples.md#qa-regression-matrix) - Build feature/browser/role/data-state regression coverage.
<a id="qa-fixture-strategy"></a>
- [Fixture Strategy](goal-examples.md#qa-fixture-strategy) - Create deterministic seed, mock, factory, and cleanup patterns.
<a id="qa-visual-regression"></a>
- [Visual Regression](goal-examples.md#qa-visual-regression) - Add screenshot diffs for critical pages with controlled thresholds.
<a id="qa-api-contracts"></a>
- [API Contracts](goal-examples.md#qa-api-contracts) - Validate frontend/backend schema, error codes, and boundary values.
<a id="qa-flaky-test-audit"></a>
- [Flaky Test Audit](goal-examples.md#qa-flaky-test-audit) - Find unstable tests and fix waits, isolation, or fixtures.
<a id="qa-error-injection"></a>
- [Error Injection](goal-examples.md#qa-error-injection) - Simulate 500s, timeouts, network failure, and partial success.
<a id="qa-cross-browser"></a>
- [Cross-Browser Coverage](goal-examples.md#qa-cross-browser) - Run critical flows across Chromium, Firefox, and WebKit.
<a id="qa-release-smoke"></a>
- [Release Smoke](goal-examples.md#qa-release-smoke) - Define the smallest pre-release verification checklist.
<a id="qa-data-migration"></a>
- [Data Migration Test](goal-examples.md#qa-data-migration) - Verify counts, constraints, and rollback around data migration.
<a id="qa-security-smoke"></a>
- [Security Smoke](goal-examples.md#qa-security-smoke) - Check auth, permission bypass, and sensitive info leakage.
<a id="qa-bug-repro-template"></a>
- [Bug Reproduction Template](goal-examples.md#qa-bug-repro-template) - Standardize environment, steps, expected, actual, and evidence.

### accessibility
<a id="accessibility-keyboard-nav"></a>
- [Keyboard Navigation](goal-examples.md#accessibility-keyboard-nav) - Ensure the whole app works with Tab, Enter, and Escape.
<a id="accessibility-screen-reader"></a>
- [Screen Reader Semantics](goal-examples.md#accessibility-screen-reader) - Check landmarks, labels, aria-live, and button names.
<a id="accessibility-focus-visible"></a>
- [Focus Visible](goal-examples.md#accessibility-focus-visible) - Give every interactive element a clear focus state.
<a id="accessibility-color-contrast"></a>
- [Color Contrast](goal-examples.md#accessibility-color-contrast) - Meet WCAG AA for text, icons, and state colors.
<a id="accessibility-form-errors"></a>
- [Accessible Form Errors](goal-examples.md#accessibility-form-errors) - Associate errors with fields so screen readers announce them.
<a id="accessibility-modal-trap"></a>
- [Modal Focus Trap](goal-examples.md#accessibility-modal-trap) - Focus opens, cycles, closes, and returns correctly.
<a id="accessibility-reduced-motion"></a>
- [Reduced Motion](goal-examples.md#accessibility-reduced-motion) - Respect prefers-reduced-motion for all nonessential motion.
<a id="accessibility-alt-text"></a>
- [Alt Text Audit](goal-examples.md#accessibility-alt-text) - Separate decorative, content, and product images.
<a id="accessibility-heading-order"></a>
- [Heading Order](goal-examples.md#accessibility-heading-order) - Fix skipped headings and fake styled headings.
<a id="accessibility-live-region"></a>
- [Live Region Feedback](goal-examples.md#accessibility-live-region) - Announce toasts, async completion, and errors accessibly.
<a id="accessibility-touch-a11y"></a>
- [Touch Accessibility](goal-examples.md#accessibility-touch-a11y) - Check tap targets, zoom, and orientation on mobile.
<a id="accessibility-audit-report"></a>
- [Accessibility Audit Report](goal-examples.md#accessibility-audit-report) - Produce prioritized issues, impact, fixes, and acceptance checks.

### performance
<a id="performance-lcp"></a>
- [LCP Optimization](goal-examples.md#performance-lcp) - Find and optimize the largest contentful paint element.
<a id="performance-cls"></a>
- [CLS Fix](goal-examples.md#performance-cls) - Reserve space for images, ads, and dynamic content.
<a id="performance-inp"></a>
- [INP Optimization](goal-examples.md#performance-inp) - Reduce long tasks and blocking interaction handlers.
<a id="performance-bundle-budget"></a>
- [Bundle Budget](goal-examples.md#performance-bundle-budget) - Set route and dependency size budgets in CI.
<a id="performance-code-splitting"></a>
- [Code Splitting](goal-examples.md#performance-code-splitting) - Lazy-load low-frequency routes, charts, and editors.
<a id="performance-image-pipeline"></a>
- [Image Pipeline](goal-examples.md#performance-image-pipeline) - Use srcset, modern formats, lazy loading, and cache headers.
<a id="performance-font-loading"></a>
- [Font Loading](goal-examples.md#performance-font-loading) - Optimize font-display, subsets, and preload hints.
<a id="performance-api-waterfall"></a>
- [API Waterfall](goal-examples.md#performance-api-waterfall) - Remove serial requests and prefetch critical data.
<a id="performance-cache-strategy"></a>
- [Cache Strategy](goal-examples.md#performance-cache-strategy) - Define browser, CDN, and service-worker cache boundaries.
<a id="performance-memory-leaks"></a>
- [Memory Leak Audit](goal-examples.md#performance-memory-leaks) - Check long sessions, lists, subscriptions, and charts for leaks.
<a id="performance-render-count"></a>
- [Render Count Audit](goal-examples.md#performance-render-count) - Find unnecessary React renders and expensive selectors.
<a id="performance-ci-gate"></a>
- [Performance CI Gate](goal-examples.md#performance-ci-gate) - Add Lighthouse or trace thresholds to CI.

### workflow
<a id="goal-meta-prompt-writer"></a>
- [Goal Prompt Writer](goal-examples.md#goal-meta-prompt-writer) - Ask the agent to inspect a repo and write a precise goal prompt before execution.
<a id="goal-continuation-audit"></a>
- [Goal Continuation Audit](goal-examples.md#goal-continuation-audit) - Check that a long-running goal keeps its done_when and verification contract after compaction.

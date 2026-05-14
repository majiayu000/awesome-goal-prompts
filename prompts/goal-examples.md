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
- [CI Pipeline Green](#explainx-ci-pipeline-green) - Repair CI test, lint, typecheck, and security scan failures until checks pass. Source-backed.

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
- [Analyze Product Usage Patterns](#cursor-usage-pattern-analysis) - Analyze product usage patterns between tab view and agent panels. Source-backed.

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
- [Fix Freezing Chart Tooltips](#cursor-chart-tooltip-freeze) - Debug and fix chart tooltips that freeze on hover. Source-backed.
- [Improve Common Error Messages](#github-copilot-error-messages) - Use a cloud coding agent to implement user-friendly messages for common errors. Source-backed.
- [Visual Feedback With Test Guard](#qiita-aochan-visual-feedback) - Add correct and wrong answer visual feedback while keeping tests green. Source-backed.
- [Theme Toggle Persistence](#apidog-theme-toggle) - Add a dark and light theme toggle that persists across refreshes. Source-backed.
- [Button Console Error Fix](#hn-button-console-error-fix) - Use browser automation to click a button, inspect console errors, fix the issue, and prove it. Source-backed.
- [Next.js Chat History Sidebar](#video-nextjs-chat-sidebar) - Replace a Next.js sidebar with chat history, then test, fix build issues, and push. Source-backed.

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
- [Contributor README Rewrite](#apidog-contributor-readme) - Rewrite README installation, run, test, and architecture guidance for new contributors. Source-backed.
- [Public API Docs Coverage](#explainx-public-api-jsdoc) - Add JSDoc and examples for public functions while keeping documentation links valid. Source-backed.

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
- [Design Doc Acceptance Complete](#claude-design-doc-acceptance) - Implement a design document until every acceptance criterion is satisfied. Source-backed.

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
- [QA Engineer Simulation](#x-qa-engineer-simulation) - Use `/goal` as a quality loop until tests pass and lint is clean. Source-backed.

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
- [Bundle Size Reduction](#udit-bundle-size-reduction) - Iteratively reduce bundle size below the documented threshold. Source-backed.
- [Benchmark Optimization](#udit-benchmark-optimization) - Optimize performance against a benchmark command until the goal is reached. Source-backed.

### workflow
- [Goal Prompt Writer](#goal-meta-prompt-writer) - Ask the agent to inspect a repo and write a precise goal prompt before execution.
- [Goal Continuation Audit](#goal-continuation-audit) - Check that a long-running goal keeps its done_when and verification contract after compaction.
- [Verifiable End-State Contract](#codex-verifiable-end-state) - Complete one objective only when a verifiable end state is met. Source-backed.
- [Four Files Walkthrough](#hermes-four-files-walkthrough) - Create four note files across turns and verify each contains its number. Source-backed.
- [Meta Goal Prompt Generator](#x-meta-goal-prompt-generator) - Ask the agent to inspect the session, repo, history, and docs before writing the actual `/goal` prompt. Source-backed.
- [AGENTS.md Goal Workflow](#x-agentsmd-goal-workflow) - Use AGENTS.md rules together with `/goal` so long-running work keeps repo-specific constraints. Source-backed.
- [Plan-Then-Goal Execution](#x-plan-then-goal-execution) - Use plan mode to define the work, then start a new goal session to implement the plan completely. Source-backed.
- [Measurable Goal Structure](#x-measurable-goal-structure) - Write goals with a clear target, proof requirement, and explicit limits. Source-backed.
- [Non-Interactive Goal Creation](#github-noninteractive-goal-creation) - Create and confirm an active goal during non-interactive Codex execution before continuing. Source-backed.
- [Prep A Goal Workspace](#github-goalbuddy-workspace) - Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command. Source-backed.
- [Long Goal With Constraints](#github-claude-long-goal-template) - Use a longer goal template with repo path, constraints, plan pointer, and execution order. Source-backed.

### migration
- [Visual Migration With Playwright](#codex-visual-migration-playwright) - Migrate a project while preserving screen output and checking it with Playwright. Source-backed.
- [Feature Port With CI Green](#hermes-feature-port-ci-green) - Port a feature from another repo, include tests, and get CI green. Source-backed.
- [Vue 2 To Vue 3 Visual And Unit Gate](#qiita-vue2-vue3-visual-unit) - Migrate listed Vue screens and stop only when visual and unit tests pass. Source-backed.
- [Finish Migration Keep Tests Green](#openai-slash-finish-migration) - Use `/goal` to complete a migration while keeping the relevant tests green. Source-backed.
- [Module API Migration](#claude-module-api-migration) - Migrate a module to a new API while keeping call sites compiling and tests passing. Source-backed.
- [Moment To Day.js Migration](#explainx-moment-dayjs-migration) - Replace Moment.js with Day.js while preserving date output across edge cases. Source-backed.
- [React 19 Migration](#cursor-forum-react19-migration) - Migrate a project to React 19 and continue until the build passes. Source-backed.
- [Pydantic V1 To V2 Migration](#github-pydantic-v2-migration) - Migrate a project from Pydantic v1 to v2 while preserving API behavior. Source-backed.

### prototype
- [PLAN.md Milestone Prototype](#codex-plan-milestone-prototype) - Implement a PLAN.md-driven prototype with tests at each milestone and browser verification. Source-backed.
- [Canvas Puzzle PLAN.md Prototype](#qiita-canvas-puzzle-plan) - Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes. Source-backed.
- [Rift Salvage Game Goal](#video-rift-salvage-game) - Build a 2D combat game prototype with assets, combat, boss logic, and browser verification. Source-backed.

### prompt-optimization
- [Eval-Driven Prompt Optimization](#codex-eval-prompt-optimization) - Optimize prompts against an eval suite until the target score or pass rate is reached. Source-backed.
- [Router Prompt Eval Score](#qiita-router-eval-score) - Improve a router prompt against an eval directory until the result score reaches a target. Source-backed.
- [RAG Chat Flywheel](#reddit-rag-chat-flywheel) - Iterate on code, tests, and metrics to improve a document-chat RAG system. Source-backed.

### testing
- [Auth Tests And Lint Clean](#claude-auth-tests-lint) - Keep working until auth tests pass and the lint step is clean. Source-backed.
- [Ruff Clean Source Tree](#hermes-ruff-src-clean) - Fix every lint error in src and prove ruff passes. Source-backed.
- [TypeScript ESLint Coverage Gate](#explainx-typescript-eslint-coverage) - Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold. Source-backed.
- [Fix Hermes CLI Tests](#hermes-cli-tests-pass) - Fix failing Hermes CLI tests until the project test script passes. Source-backed.
- [Add Authentication Tests](#google-jules-auth-tests) - Create unit tests for an authentication module in a Jules session. Source-backed.
- [Add UserService Unit Tests](#openhands-userservice-tests) - Add unit tests for UserService and raise target coverage to the documented threshold. Source-backed.
- [Parallel Test Coverage Recovery](#devin-parallel-coverage-recovery) - Find low-coverage modules and open separate test-improvement PRs for each module. Source-backed.
- [Single Vitest Case Fix](#qiita-aochan-single-vitest-fix) - Fix a quiz application until one named Vitest case passes. Source-backed.
- [Full Quiz Test Recovery](#qiita-aochan-full-vitest-recovery) - Repair the quiz app until the full Vitest suite exits cleanly. Source-backed.
- [Auth Coverage Lift](#jdhodges-auth-coverage-lift) - Raise authentication code coverage from the documented baseline to the documented target within a scoped edit boundary. Source-backed.
- [Auth Test Repair Boundary](#apidog-auth-test-repair) - Fix failing auth tests while preserving the documented file boundary. Source-backed.
- [Coverage Autoresearch Loop](#udit-coverage-autoresearch) - Iterate on tests until coverage reaches the documented target. Source-backed.
- [Test And TypeScript Clean](#theaidaily-test-typescript-clean) - Keep working until tests exit cleanly and TypeScript errors are gone. Source-backed.
- [Go Race Cleanup](#cursor-forum-go-race-cleanup) - Eliminate data races detected by the Go race detector. Source-backed.
- [Tests And Lint Completion](#x-tests-lint-completion) - Run a `/goal` loop until all tests pass and lint is clean. Source-backed.
- [Tests Pass And PR Ready](#reddit-tests-pass-pr-ready) - Keep Claude Code working until tests pass and the PR is ready for review. Source-backed.
- [Flaky Auth Tests Goal](#github-claude-goal-flaky-auth) - Use a Claude goal plugin example to find and fix flaky authentication tests. Source-backed.
- [Improve Benchmark Coverage](#github-benchmark-coverage-goal) - Use `/goal` to improve benchmark coverage and persist the command in history. Source-backed.
- [Batch Fix Bugs](#github-claude-batch-bugs) - Use a Claude Code goal to fix a numbered batch of bugs without looping on missing skills. Source-backed.

### investigation
- [Session Drift Report](#hermes-session-drift-report) - Investigate session ID drift during mid-run compression and write a report. Source-backed.
- [Billing Empty State Root Cause](#reddit-billing-empty-state) - Find why active subscriptions show an empty state without changing pricing or webhook code. Source-backed.

### cli
- [EXIF Rename CLI](#hermes-exif-rename-cli) - Build a small CLI that renames photos by EXIF date and test it on a photos folder. Source-backed.

### refactor
- [Auth Dependency Injection Refactor](#explainx-auth-di-refactor) - Refactor auth code to dependency injection while preserving tests, coverage, and public API. Source-backed.
- [Split Oversized File](#claude-split-oversized-file) - Split an oversized source file into focused modules while preserving behavior. Source-backed.

### greenfield-build
- [Build Design Tool From Scratch](#openai-long-horizon-design-tool) - Run a long-horizon Codex task to build a design tool with milestone verification. Source-backed.

### backlog
- [Clear Labeled Issue Backlog](#claude-clear-labeled-issues) - Work through a labeled issue queue until no matching issues remain. Source-backed.
- [Clear Trading App Backlog](#reddit-trading-backlog-clearance) - Generate a roadmap backlog for a trading app and then clear it with goals. Source-backed.
- [Ship Backlog Features](#reddit-ship-backlog-features) - Implement the feature list from BACKLOG.md until CI is green. Source-backed.

### research
- [Read-Only Font Match](#jdhodges-read-only-font-match) - Research font matches in read-only mode and produce a report without purchasing or downloading assets. Source-backed.
- [Public Benchmark Table](#apidog-benchmark-table) - Collect distinct public benchmarks and build a date-sorted comparison table. Source-backed.
- [Review Sentiment JSON Agent](#hn-review-sentiment-json-agent) - Fetch reviews with browser automation, classify sentiment, and write structured JSON output. Source-backed.

### maintenance
- [Repo Maintenance Audit](#apidog-repo-maintenance-audit) - Find dead code, unused dependencies, and stale files, then produce a PR-ready justification list. Source-backed.
- [Clean Worktree File Budget](#theaidaily-clean-worktree-budget) - Keep the worktree clean and enforce a source file size budget. Source-backed.

### goal-maintenance
- [Goal Escape Hatch](#x-goal-escape-hatch) - Add an explicit incomplete state for impossible subtasks so a goal loop can stop safely. Source-backed.
- [Goal-Forge Done-When Loop](#x-goal-forge-done-when) - Write a GOAL.md-style contract where `done_when` controls completion instead of vague success claims. Source-backed.
- [Review Plan Until No Gaps](#github-review-plan-no-gaps) - Loop on implementation-plan review until a fresh review finds no remaining gaps. Source-backed.
- [Long Task Until Verification](#github-long-task-verification) - Continue a long-running task until final verification passes rather than stopping on partial progress. Source-backed.
- [Completion Audit Before Done](#github-completion-audit-before-done) - Audit completion criteria before calling the goal complete. Source-backed.
- [Goal Permission Context Sync](#github-goal-permission-context) - Ensure goal continuation uses the current permission context after approval mode changes. Source-backed.
- [Real CLI Goal Loop](#github-hermes-real-cli-loop) - Verify a real CLI goal loop where the second judge round confirms completion. Source-backed.
- [Verify File Creation](#github-hermes-file-verification) - Verify that a requested file was actually created instead of trusting the agent claim. Source-backed.
- [Queue Follow-Up Goals](#github-hermes-goal-queue) - Promote queued follow-up goals: fix tests, run full tests, then produce coverage. Source-backed.

### orchestration
- [DAG Agent Dispatch](#hn-dag-agent-dispatch) - Split a goal into a dependency graph and dispatch independent agents into isolated worktrees. Source-backed.

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
- Source type: `official-goal`
- Evidence: verifiable stopping condition

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
- Source type: `official-goal`
- Evidence: visual migration

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
- Source type: `official-goal`
- Evidence: PLAN.md

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
- Source type: `official-goal`
- Evidence: eval suite

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
- Source type: `official-goal`
- Evidence: test/auth pass

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
- Source type: `official-goal`
- Evidence: CHANGELOG.md has an entry

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
- Source type: `official-goal`
- Evidence: ruff check

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
- Source type: `official-goal`
- Evidence: CI green

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
- Source type: `official-goal`
- Evidence: write up a report

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
- Source type: `official-goal`
- Evidence: photos/ folder

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
- Source type: `official-goal`
- Evidence: Create four files

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
- Source type: `third-party-tutorial`
- Evidence: TypeScript errors resolved

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
- Source type: `third-party-tutorial`
- Evidence: auth.ts dependency injection

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
- Source type: `third-party-tutorial`
- Evidence: npm audit vulnerabilities patched

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
- Source type: `third-party-tutorial`
- Evidence: Lighthouse performance score >95

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
- Source type: `third-party-tutorial`
- Evidence: pnpm test:visual

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
- Source type: `third-party-tutorial`
- Evidence: canvas puzzle

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
- Source type: `third-party-tutorial`
- Evidence: router prompt

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

<a id="openai-slash-finish-migration"></a>
### Finish Migration Keep Tests Green

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Use `/goal` to complete a migration while keeping the relevant tests green.
- Verification: `repo-local migration tests`
- Source: [OpenAI Codex slash commands](https://developers.openai.com/codex/cli/slash-commands#set-an-experimental-goal-with-goal)
- Source type: `official-goal`
- Evidence: Finish the migration

```text
/goal
GOAL:
Complete Finish Migration Keep Tests Green for a migration project: Use `/goal` to complete a migration while keeping the relevant tests green.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `repo-local migration tests`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Use `/goal` to complete a migration while keeping the relevant tests green.
- The verification command or evidence path succeeds: `repo-local migration tests`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `repo-local migration tests` or the closest repo-local equivalent if the exact command is not available.
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

<a id="openai-long-horizon-design-tool"></a>
### Build Design Tool From Scratch

- Category: `greenfield-build`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Run a long-horizon Codex task to build a design tool with milestone verification.
- Verification: `tests, lint, and typecheck per milestone`
- Source: [OpenAI Codex blog](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
- Source type: `official-workflow`
- Evidence: verification steps

```text
/goal
GOAL:
Complete Build Design Tool From Scratch for a greenfield implementation task: Run a long-horizon Codex task to build a design tool with milestone verification.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect product requirements, milestones, tests, and verification notes.
- Establish a baseline by running or locating evidence for: `tests, lint, and typecheck per milestone`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Keep implementation tied to the stated product requirements.
- Do not ship a demo-only path without tests or runnable verification.

DONE WHEN:
- The implementation or documentation directly satisfies: Run a long-horizon Codex task to build a design tool with milestone verification.
- The verification command or evidence path succeeds: `tests, lint, and typecheck per milestone`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `tests, lint, and typecheck per milestone` or the closest repo-local equivalent if the exact command is not available.
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

<a id="claude-module-api-migration"></a>
### Module API Migration

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Migrate a module to a new API while keeping call sites compiling and tests passing.
- Verification: `compile call sites && tests pass`
- Source: [Claude Code docs](https://code.claude.com/docs/en/goal)
- Source type: `official-goal`
- Evidence: new API

```text
/goal
GOAL:
Complete Module API Migration for a migration project: Migrate a module to a new API while keeping call sites compiling and tests passing.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `compile call sites && tests pass`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Migrate a module to a new API while keeping call sites compiling and tests passing.
- The verification command or evidence path succeeds: `compile call sites && tests pass`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `compile call sites && tests pass` or the closest repo-local equivalent if the exact command is not available.
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

<a id="claude-design-doc-acceptance"></a>
### Design Doc Acceptance Complete

- Category: `product`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Implement a design document until every acceptance criterion is satisfied.
- Verification: `acceptance criteria review`
- Source: [Claude Code docs](https://code.claude.com/docs/en/goal)
- Source type: `official-goal`
- Evidence: acceptance criteria

```text
/goal
GOAL:
Complete Design Doc Acceptance Complete for a product planning and implementation repo: Implement a design document until every acceptance criterion is satisfied.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `acceptance criteria review`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Implement a design document until every acceptance criterion is satisfied.
- The verification command or evidence path succeeds: `acceptance criteria review`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `acceptance criteria review` or the closest repo-local equivalent if the exact command is not available.
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

<a id="claude-split-oversized-file"></a>
### Split Oversized File

- Category: `refactor`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Split an oversized source file into focused modules while preserving behavior.
- Verification: `module size budget && tests pass`
- Source: [Claude Code docs](https://code.claude.com/docs/en/goal)
- Source type: `official-goal`
- Evidence: size budget

```text
/goal
GOAL:
Complete Split Oversized File for a refactoring task: Split an oversized source file into focused modules while preserving behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect the target module, call sites, public API, tests, and compatibility notes.
- Establish a baseline by running or locating evidence for: `module size budget && tests pass`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change public APIs, data formats, or user-visible behavior unless the goal requires it.
- Keep behavior characterization tests before large internal changes.

DONE WHEN:
- The implementation or documentation directly satisfies: Split an oversized source file into focused modules while preserving behavior.
- The verification command or evidence path succeeds: `module size budget && tests pass`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `module size budget && tests pass` or the closest repo-local equivalent if the exact command is not available.
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

<a id="claude-clear-labeled-issues"></a>
### Clear Labeled Issue Backlog

- Category: `backlog`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Work through a labeled issue queue until no matching issues remain.
- Verification: `issue queue empty`
- Source: [Claude Code docs](https://code.claude.com/docs/en/goal)
- Source type: `official-goal`
- Evidence: queue is empty

```text
/goal
GOAL:
Complete Clear Labeled Issue Backlog for a backlog execution task: Work through a labeled issue queue until no matching issues remain.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect roadmaps, backlog files, issue queues, acceptance criteria, and CI evidence.
- Establish a baseline by running or locating evidence for: `issue queue empty`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not expand the backlog while executing it.
- Keep each finished item tied to its original acceptance criteria.

DONE WHEN:
- The implementation or documentation directly satisfies: Work through a labeled issue queue until no matching issues remain.
- The verification command or evidence path succeeds: `issue queue empty`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `issue queue empty` or the closest repo-local equivalent if the exact command is not available.
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

<a id="hermes-cli-tests-pass"></a>
### Fix Hermes CLI Tests

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Fix failing Hermes CLI tests until the project test script passes.
- Verification: `scripts/run_tests.sh`
- Source: [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)
- Source type: `official-goal`
- Evidence: scripts/run_tests.sh passes

```text
/goal
GOAL:
Complete Fix Hermes CLI Tests for a project with failing or missing verification gates: Fix failing Hermes CLI tests until the project test script passes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `scripts/run_tests.sh`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix failing Hermes CLI tests until the project test script passes.
- The verification command or evidence path succeeds: `scripts/run_tests.sh`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `scripts/run_tests.sh` or the closest repo-local equivalent if the exact command is not available.
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

<a id="cursor-usage-pattern-analysis"></a>
### Analyze Product Usage Patterns

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Analyze product usage patterns between tab view and agent panels.
- Verification: `analysis files and tests shown`
- Source: [Cursor product page](https://cursor.com/en-US/product)
- Source type: `official-agent-task`
- Evidence: Analyze Tab vs Agent Usage Patterns

```text
/goal
GOAL:
Complete Analyze Product Usage Patterns for an analytics or BI project: Analyze product usage patterns between tab view and agent panels.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `analysis files and tests shown`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Analyze product usage patterns between tab view and agent panels.
- The verification command or evidence path succeeds: `analysis files and tests shown`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `analysis files and tests shown` or the closest repo-local equivalent if the exact command is not available.
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

<a id="cursor-chart-tooltip-freeze"></a>
### Fix Freezing Chart Tooltips

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Debug and fix chart tooltips that freeze on hover.
- Verification: `frontend diff plus interaction verification`
- Source: [Cursor product page](https://cursor.com/en-US/product)
- Source type: `official-agent-task`
- Evidence: Chart tooltips freeze

```text
/goal
GOAL:
Complete Fix Freezing Chart Tooltips for a web frontend application: Debug and fix chart tooltips that freeze on hover.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `frontend diff plus interaction verification`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Debug and fix chart tooltips that freeze on hover.
- The verification command or evidence path succeeds: `frontend diff plus interaction verification`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `frontend diff plus interaction verification` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-copilot-error-messages"></a>
### Improve Common Error Messages

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use a cloud coding agent to implement user-friendly messages for common errors.
- Verification: `pushed code changes`
- Source: [GitHub Copilot docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions)
- Source type: `official-agent-task`
- Evidence: user friendly message

```text
/goal
GOAL:
Complete Improve Common Error Messages for a web frontend application: Use a cloud coding agent to implement user-friendly messages for common errors.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `pushed code changes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Use a cloud coding agent to implement user-friendly messages for common errors.
- The verification command or evidence path succeeds: `pushed code changes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pushed code changes` or the closest repo-local equivalent if the exact command is not available.
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

<a id="google-jules-auth-tests"></a>
### Add Authentication Tests

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Create unit tests for an authentication module in a Jules session.
- Verification: `session completed with PR output`
- Source: [Google Jules sessions docs](https://jules.google/docs/api/reference/sessions/)
- Source type: `official-agent-task`
- Evidence: Add auth tests

```text
/goal
GOAL:
Complete Add Authentication Tests for a project with failing or missing verification gates: Create unit tests for an authentication module in a Jules session.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `session completed with PR output`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Create unit tests for an authentication module in a Jules session.
- The verification command or evidence path succeeds: `session completed with PR output`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `session completed with PR output` or the closest repo-local equivalent if the exact command is not available.
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

<a id="openhands-userservice-tests"></a>
### Add UserService Unit Tests

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add unit tests for UserService and raise target coverage to the documented threshold.
- Verification: `coverage target evidence`
- Source: [OpenHands tutorials](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Target coverage: 80%

```text
/goal
GOAL:
Complete Add UserService Unit Tests for a project with failing or missing verification gates: Add unit tests for UserService and raise target coverage to the documented threshold.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `coverage target evidence`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Add unit tests for UserService and raise target coverage to the documented threshold.
- The verification command or evidence path succeeds: `coverage target evidence`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `coverage target evidence` or the closest repo-local equivalent if the exact command is not available.
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

<a id="devin-parallel-coverage-recovery"></a>
### Parallel Test Coverage Recovery

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Find low-coverage modules and open separate test-improvement PRs for each module.
- Verification: `separate PR per module`
- Source: [Devin advanced capabilities](https://docs.devin.ai/product-guides/advanced-mode)
- Source type: `official-agent-task`
- Evidence: below 50% coverage

```text
/goal
GOAL:
Complete Parallel Test Coverage Recovery for a project with failing or missing verification gates: Find low-coverage modules and open separate test-improvement PRs for each module.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `separate PR per module`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Find low-coverage modules and open separate test-improvement PRs for each module.
- The verification command or evidence path succeeds: `separate PR per module`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `separate PR per module` or the closest repo-local equivalent if the exact command is not available.
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

<a id="qiita-aochan-single-vitest-fix"></a>
### Single Vitest Case Fix

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Fix a quiz application until one named Vitest case passes.
- Verification: `pnpm exec vitest run -t "increments score only on correct answer"`
- Source: [Qiita Aochan0604](https://qiita.com/Aochan0604/items/8cc5f28901455097095c)
- Source type: `third-party-tutorial`
- Evidence: pnpm exec vitest run -t

```text
/goal
GOAL:
Complete Single Vitest Case Fix for a project with failing or missing verification gates: Fix a quiz application until one named Vitest case passes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `pnpm exec vitest run -t "increments score only on correct answer"`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix a quiz application until one named Vitest case passes.
- The verification command or evidence path succeeds: `pnpm exec vitest run -t "increments score only on correct answer"`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pnpm exec vitest run -t "increments score only on correct answer"` or the closest repo-local equivalent if the exact command is not available.
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

<a id="qiita-aochan-full-vitest-recovery"></a>
### Full Quiz Test Recovery

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Repair the quiz app until the full Vitest suite exits cleanly.
- Verification: `pnpm exec vitest run`
- Source: [Qiita Aochan0604](https://qiita.com/Aochan0604/items/8cc5f28901455097095c)
- Source type: `third-party-tutorial`
- Evidence: pnpm exec vitest run exits 0

```text
/goal
GOAL:
Complete Full Quiz Test Recovery for a project with failing or missing verification gates: Repair the quiz app until the full Vitest suite exits cleanly.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `pnpm exec vitest run`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Repair the quiz app until the full Vitest suite exits cleanly.
- The verification command or evidence path succeeds: `pnpm exec vitest run`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pnpm exec vitest run` or the closest repo-local equivalent if the exact command is not available.
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

<a id="qiita-aochan-visual-feedback"></a>
### Visual Feedback With Test Guard

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add correct and wrong answer visual feedback while keeping tests green.
- Verification: `pnpm exec vitest run && git status --short`
- Source: [Qiita Aochan0604](https://qiita.com/Aochan0604/items/8cc5f28901455097095c)
- Source type: `third-party-tutorial`
- Evidence: .correct and .wrong

```text
/goal
GOAL:
Complete Visual Feedback With Test Guard for a web frontend application: Add correct and wrong answer visual feedback while keeping tests green.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `pnpm exec vitest run && git status --short`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Add correct and wrong answer visual feedback while keeping tests green.
- The verification command or evidence path succeeds: `pnpm exec vitest run && git status --short`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pnpm exec vitest run && git status --short` or the closest repo-local equivalent if the exact command is not available.
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

<a id="jdhodges-read-only-font-match"></a>
### Read-Only Font Match

- Category: `research`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Research font matches in read-only mode and produce a report without purchasing or downloading assets.
- Verification: `written report`
- Source: [J.D. Hodges blog](https://www.jdhodges.com/blog/codex-goal-feature-review/)
- Source type: `third-party-review`
- Evidence: read-only font-match

```text
/goal
GOAL:
Complete Read-Only Font Match for a research task: Research font matches in read-only mode and produce a report without purchasing or downloading assets.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect source lists, citation notes, evidence files, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `written report`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not present unsourced claims as facts.
- Keep direct quotes short and attach a public URL for every external claim.

DONE WHEN:
- The implementation or documentation directly satisfies: Research font matches in read-only mode and produce a report without purchasing or downloading assets.
- The verification command or evidence path succeeds: `written report`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `written report` or the closest repo-local equivalent if the exact command is not available.
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

<a id="jdhodges-auth-coverage-lift"></a>
### Auth Coverage Lift

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Raise authentication code coverage from the documented baseline to the documented target within a scoped edit boundary.
- Verification: `npm test`
- Source: [J.D. Hodges blog](https://www.jdhodges.com/blog/codex-goal-feature-review/)
- Source type: `third-party-review`
- Evidence: coverage from 38% to 75%

```text
/goal
GOAL:
Complete Auth Coverage Lift for a project with failing or missing verification gates: Raise authentication code coverage from the documented baseline to the documented target within a scoped edit boundary.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Raise authentication code coverage from the documented baseline to the documented target within a scoped edit boundary.
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

<a id="apidog-auth-test-repair"></a>
### Auth Test Repair Boundary

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Fix failing auth tests while preserving the documented file boundary.
- Verification: `npm test`
- Source: [Apidog blog](https://apidog.com/blog/goal-command-codex-claude-code-autonomous-agents/)
- Source type: `third-party-tutorial`
- Evidence: npm test exits 0

```text
/goal
GOAL:
Complete Auth Test Repair Boundary for a project with failing or missing verification gates: Fix failing auth tests while preserving the documented file boundary.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Fix failing auth tests while preserving the documented file boundary.
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

<a id="apidog-benchmark-table"></a>
### Public Benchmark Table

- Category: `research`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Collect distinct public benchmarks and build a date-sorted comparison table.
- Verification: `table covers 10 sources`
- Source: [Apidog blog](https://apidog.com/blog/goal-command-codex-claude-code-autonomous-agents/)
- Source type: `third-party-tutorial`
- Evidence: 10 distinct benchmarks

```text
/goal
GOAL:
Complete Public Benchmark Table for a research task: Collect distinct public benchmarks and build a date-sorted comparison table.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect source lists, citation notes, evidence files, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `table covers 10 sources`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not present unsourced claims as facts.
- Keep direct quotes short and attach a public URL for every external claim.

DONE WHEN:
- The implementation or documentation directly satisfies: Collect distinct public benchmarks and build a date-sorted comparison table.
- The verification command or evidence path succeeds: `table covers 10 sources`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `table covers 10 sources` or the closest repo-local equivalent if the exact command is not available.
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

<a id="apidog-repo-maintenance-audit"></a>
### Repo Maintenance Audit

- Category: `maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Find dead code, unused dependencies, and stale files, then produce a PR-ready justification list.
- Verification: `each item has justification`
- Source: [Apidog blog](https://apidog.com/blog/goal-command-codex-claude-code-autonomous-agents/)
- Source type: `third-party-tutorial`
- Evidence: dead code, unused dependencies

```text
/goal
GOAL:
Complete Repo Maintenance Audit for a repository maintenance task: Find dead code, unused dependencies, and stale files, then produce a PR-ready justification list.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect dead code, dependencies, file structure, scripts, and PR notes.
- Establish a baseline by running or locating evidence for: `each item has justification`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete files, dependencies, or scripts without evidence that they are unused.
- Keep every proposed removal tied to a specific verification step.

DONE WHEN:
- The implementation or documentation directly satisfies: Find dead code, unused dependencies, and stale files, then produce a PR-ready justification list.
- The verification command or evidence path succeeds: `each item has justification`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `each item has justification` or the closest repo-local equivalent if the exact command is not available.
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

<a id="apidog-contributor-readme"></a>
### Contributor README Rewrite

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Rewrite README installation, run, test, and architecture guidance for new contributors.
- Verification: `commands and expected output documented`
- Source: [Apidog blog](https://apidog.com/blog/goal-command-codex-claude-code-autonomous-agents/)
- Source type: `third-party-tutorial`
- Evidence: README.md install/run/test

```text
/goal
GOAL:
Complete Contributor README Rewrite for a developer-facing documentation site or repository: Rewrite README installation, run, test, and architecture guidance for new contributors.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `commands and expected output documented`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Rewrite README installation, run, test, and architecture guidance for new contributors.
- The verification command or evidence path succeeds: `commands and expected output documented`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `commands and expected output documented` or the closest repo-local equivalent if the exact command is not available.
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

<a id="apidog-theme-toggle"></a>
### Theme Toggle Persistence

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add a dark and light theme toggle that persists across refreshes.
- Verification: `browser refresh verification`
- Source: [Apidog blog](https://apidog.com/blog/goal-command-codex-claude-code-autonomous-agents/)
- Source type: `third-party-tutorial`
- Evidence: dark/light theme toggle

```text
/goal
GOAL:
Complete Theme Toggle Persistence for a web frontend application: Add a dark and light theme toggle that persists across refreshes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `browser refresh verification`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Add a dark and light theme toggle that persists across refreshes.
- The verification command or evidence path succeeds: `browser refresh verification`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `browser refresh verification` or the closest repo-local equivalent if the exact command is not available.
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

<a id="explainx-ci-pipeline-green"></a>
### CI Pipeline Green

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Repair CI test, lint, typecheck, and security scan failures until checks pass.
- Verification: `local CI rerun and remote CI`
- Source: [ExplainX blog](https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026)
- Source type: `third-party-tutorial`
- Evidence: All CI checks passing

```text
/goal
GOAL:
Complete CI Pipeline Green for a repository with CI/CD automation: Repair CI test, lint, typecheck, and security scan failures until checks pass.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `local CI rerun and remote CI`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Repair CI test, lint, typecheck, and security scan failures until checks pass.
- The verification command or evidence path succeeds: `local CI rerun and remote CI`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `local CI rerun and remote CI` or the closest repo-local equivalent if the exact command is not available.
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

<a id="explainx-moment-dayjs-migration"></a>
### Moment To Day.js Migration

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Replace Moment.js with Day.js while preserving date output across edge cases.
- Verification: `tests and edge-case output compare`
- Source: [ExplainX blog](https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026)
- Source type: `third-party-tutorial`
- Evidence: Moment.js usage with Day.js

```text
/goal
GOAL:
Complete Moment To Day.js Migration for a migration project: Replace Moment.js with Day.js while preserving date output across edge cases.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `tests and edge-case output compare`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Replace Moment.js with Day.js while preserving date output across edge cases.
- The verification command or evidence path succeeds: `tests and edge-case output compare`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `tests and edge-case output compare` or the closest repo-local equivalent if the exact command is not available.
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

<a id="explainx-public-api-jsdoc"></a>
### Public API Docs Coverage

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add JSDoc and examples for public functions while keeping documentation links valid.
- Verification: `docs coverage and broken link check`
- Source: [ExplainX blog](https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026)
- Source type: `third-party-tutorial`
- Evidence: public functions ... JSDoc

```text
/goal
GOAL:
Complete Public API Docs Coverage for a developer-facing documentation site or repository: Add JSDoc and examples for public functions while keeping documentation links valid.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `docs coverage and broken link check`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Add JSDoc and examples for public functions while keeping documentation links valid.
- The verification command or evidence path succeeds: `docs coverage and broken link check`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `docs coverage and broken link check` or the closest repo-local equivalent if the exact command is not available.
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

<a id="udit-coverage-autoresearch"></a>
### Coverage Autoresearch Loop

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Iterate on tests until coverage reaches the documented target.
- Verification: `npm test -- --coverage`
- Source: [Udit Autoresearch](https://udit.co/projects/autoresearch)
- Source type: `third-party-project`
- Evidence: Increase test coverage to 95%

```text
/goal
GOAL:
Complete Coverage Autoresearch Loop for a project with failing or missing verification gates: Iterate on tests until coverage reaches the documented target.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `npm test -- --coverage`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Iterate on tests until coverage reaches the documented target.
- The verification command or evidence path succeeds: `npm test -- --coverage`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test -- --coverage` or the closest repo-local equivalent if the exact command is not available.
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

<a id="udit-bundle-size-reduction"></a>
### Bundle Size Reduction

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Iteratively reduce bundle size below the documented threshold.
- Verification: `npm run build and size report`
- Source: [Udit Autoresearch](https://udit.co/projects/autoresearch)
- Source type: `third-party-project`
- Evidence: Reduce bundle size below 200KB

```text
/goal
GOAL:
Complete Bundle Size Reduction for a web application with measurable performance goals: Iteratively reduce bundle size below the documented threshold.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run build and size report`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Iteratively reduce bundle size below the documented threshold.
- The verification command or evidence path succeeds: `npm run build and size report`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run build and size report` or the closest repo-local equivalent if the exact command is not available.
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

<a id="udit-benchmark-optimization"></a>
### Benchmark Optimization

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Optimize performance against a benchmark command until the goal is reached.
- Verification: `npm run bench`
- Source: [Udit Autoresearch](https://udit.co/projects/autoresearch)
- Source type: `third-party-project`
- Evidence: npm run bench

```text
/goal
GOAL:
Complete Benchmark Optimization for a web application with measurable performance goals: Optimize performance against a benchmark command until the goal is reached.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `npm run bench`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Optimize performance against a benchmark command until the goal is reached.
- The verification command or evidence path succeeds: `npm run bench`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm run bench` or the closest repo-local equivalent if the exact command is not available.
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

<a id="theaidaily-test-typescript-clean"></a>
### Test And TypeScript Clean

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Keep working until tests exit cleanly and TypeScript errors are gone.
- Verification: `npm test && npx tsc --noEmit`
- Source: [TheAIDaily](https://theaidaily.nl/zo-gebruik-je-claude-code-goal-slash-command/)
- Source type: `third-party-tutorial`
- Evidence: npm test exit code 0

```text
/goal
GOAL:
Complete Test And TypeScript Clean for a project with failing or missing verification gates: Keep working until tests exit cleanly and TypeScript errors are gone.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `npm test && npx tsc --noEmit`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Keep working until tests exit cleanly and TypeScript errors are gone.
- The verification command or evidence path succeeds: `npm test && npx tsc --noEmit`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `npm test && npx tsc --noEmit` or the closest repo-local equivalent if the exact command is not available.
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

<a id="theaidaily-clean-worktree-budget"></a>
### Clean Worktree File Budget

- Category: `maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Keep the worktree clean and enforce a source file size budget.
- Verification: `git status --short && file length check`
- Source: [TheAIDaily](https://theaidaily.nl/zo-gebruik-je-claude-code-goal-slash-command/)
- Source type: `third-party-tutorial`
- Evidence: git status is clean

```text
/goal
GOAL:
Complete Clean Worktree File Budget for a repository maintenance task: Keep the worktree clean and enforce a source file size budget.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect dead code, dependencies, file structure, scripts, and PR notes.
- Establish a baseline by running or locating evidence for: `git status --short && file length check`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete files, dependencies, or scripts without evidence that they are unused.
- Keep every proposed removal tied to a specific verification step.

DONE WHEN:
- The implementation or documentation directly satisfies: Keep the worktree clean and enforce a source file size budget.
- The verification command or evidence path succeeds: `git status --short && file length check`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `git status --short && file length check` or the closest repo-local equivalent if the exact command is not available.
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

<a id="cursor-forum-react19-migration"></a>
### React 19 Migration

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Migrate a project to React 19 and continue until the build passes.
- Verification: `build passes`
- Source: [Cursor Forum](https://forum.cursor.com/t/add-autonomous-goal-mode-similar-to-claude-code-s-goal/160374)
- Source type: `public-forum`
- Evidence: React 19 until build passes

```text
/goal
GOAL:
Complete React 19 Migration for a migration project: Migrate a project to React 19 and continue until the build passes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `build passes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Migrate a project to React 19 and continue until the build passes.
- The verification command or evidence path succeeds: `build passes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `build passes` or the closest repo-local equivalent if the exact command is not available.
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

<a id="cursor-forum-go-race-cleanup"></a>
### Go Race Cleanup

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Eliminate data races detected by the Go race detector.
- Verification: `go test -race`
- Source: [Cursor Forum](https://forum.cursor.com/t/add-autonomous-goal-mode-similar-to-claude-code-s-goal/160374)
- Source type: `public-forum`
- Evidence: go test -race

```text
/goal
GOAL:
Complete Go Race Cleanup for a project with failing or missing verification gates: Eliminate data races detected by the Go race detector.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `go test -race`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Eliminate data races detected by the Go race detector.
- The verification command or evidence path succeeds: `go test -race`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `go test -race` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-meta-goal-prompt-generator"></a>
### Meta Goal Prompt Generator

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Ask the agent to inspect the session, repo, history, and docs before writing the actual `/goal` prompt.
- Verification: `generated goal prompt with clarified uncertainties`
- Source: [@meta_alchemist on X](https://x.com/meta_alchemist/status/2054214497443995694)
- Source type: `x-post`
- Evidence: write me the /goal prompt for this

```text
/goal
GOAL:
Complete Meta Goal Prompt Generator for a coding-agent workflow repository: Ask the agent to inspect the session, repo, history, and docs before writing the actual `/goal` prompt.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `generated goal prompt with clarified uncertainties`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Ask the agent to inspect the session, repo, history, and docs before writing the actual `/goal` prompt.
- The verification command or evidence path succeeds: `generated goal prompt with clarified uncertainties`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `generated goal prompt with clarified uncertainties` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-tests-lint-completion"></a>
### Tests And Lint Completion

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Run a `/goal` loop until all tests pass and lint is clean.
- Verification: `tests pass && lint clean`
- Source: [@sairahul1 on X](https://x.com/sairahul1/status/2054821159066386482)
- Source type: `x-post`
- Evidence: /goal all tests pass and lint is clean

```text
/goal
GOAL:
Complete Tests And Lint Completion for a project with failing or missing verification gates: Run a `/goal` loop until all tests pass and lint is clean.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `tests pass && lint clean`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Run a `/goal` loop until all tests pass and lint is clean.
- The verification command or evidence path succeeds: `tests pass && lint clean`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `tests pass && lint clean` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-goal-escape-hatch"></a>
### Goal Escape Hatch

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add an explicit incomplete state for impossible subtasks so a goal loop can stop safely.
- Verification: `incomplete marker and rationale`
- Source: [@KingBootoshi on X](https://x.com/KingBootoshi/status/2054837169748152645)
- Source type: `x-post`
- Evidence: /GOAL NEEDED AN ESCAPE HATCH

```text
/goal
GOAL:
Complete Goal Escape Hatch for a goal-management workflow: Add an explicit incomplete state for impossible subtasks so a goal loop can stop safely.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `incomplete marker and rationale`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Add an explicit incomplete state for impossible subtasks so a goal loop can stop safely.
- The verification command or evidence path succeeds: `incomplete marker and rationale`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `incomplete marker and rationale` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-agentsmd-goal-workflow"></a>
### AGENTS.md Goal Workflow

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use AGENTS.md rules together with `/goal` so long-running work keeps repo-specific constraints.
- Verification: `AGENTS.md rules honored`
- Source: [@dhruvbaldawa on X](https://x.com/dhruvbaldawa/status/2053745268118733252)
- Source type: `x-post`
- Evidence: combine it with /goal

```text
/goal
GOAL:
Complete AGENTS.md Goal Workflow for a coding-agent workflow repository: Use AGENTS.md rules together with `/goal` so long-running work keeps repo-specific constraints.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `AGENTS.md rules honored`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Use AGENTS.md rules together with `/goal` so long-running work keeps repo-specific constraints.
- The verification command or evidence path succeeds: `AGENTS.md rules honored`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `AGENTS.md rules honored` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-goal-forge-done-when"></a>
### Goal-Forge Done-When Loop

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Write a GOAL.md-style contract where `done_when` controls completion instead of vague success claims.
- Verification: `done_when audit`
- Source: [@Michaelzsguo on X](https://x.com/Michaelzsguo/status/2053508788431511637)
- Source type: `x-post`
- Evidence: done_when is intrinsic

```text
/goal
GOAL:
Complete Goal-Forge Done-When Loop for a goal-management workflow: Write a GOAL.md-style contract where `done_when` controls completion instead of vague success claims.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `done_when audit`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Write a GOAL.md-style contract where `done_when` controls completion instead of vague success claims.
- The verification command or evidence path succeeds: `done_when audit`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `done_when audit` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-plan-then-goal-execution"></a>
### Plan-Then-Goal Execution

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use plan mode to define the work, then start a new goal session to implement the plan completely.
- Verification: `plan completed against checklist`
- Source: [@ivangdavila on X](https://x.com/ivangdavila/status/2053867892064616481)
- Source type: `x-post`
- Evidence: Use /plan mode to define the goal

```text
/goal
GOAL:
Complete Plan-Then-Goal Execution for a coding-agent workflow repository: Use plan mode to define the work, then start a new goal session to implement the plan completely.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `plan completed against checklist`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Use plan mode to define the work, then start a new goal session to implement the plan completely.
- The verification command or evidence path succeeds: `plan completed against checklist`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `plan completed against checklist` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-measurable-goal-structure"></a>
### Measurable Goal Structure

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Write goals with a clear target, proof requirement, and explicit limits.
- Verification: `proof and limits present`
- Source: [@Arslandev97 on X](https://x.com/Arslandev97/status/2054781760194711978)
- Source type: `x-post`
- Evidence: Set a clear goal. Make it measurable.

```text
/goal
GOAL:
Complete Measurable Goal Structure for a coding-agent workflow repository: Write goals with a clear target, proof requirement, and explicit limits.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `proof and limits present`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Write goals with a clear target, proof requirement, and explicit limits.
- The verification command or evidence path succeeds: `proof and limits present`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `proof and limits present` or the closest repo-local equivalent if the exact command is not available.
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

<a id="x-qa-engineer-simulation"></a>
### QA Engineer Simulation

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use `/goal` as a quality loop until tests pass and lint is clean.
- Verification: `tests pass && lint clean`
- Source: [@LenaWithAI on X](https://x.com/LenaWithAI/status/2054845479502930372)
- Source type: `x-post`
- Evidence: runs until tests pass and lint is clean

```text
/goal
GOAL:
Complete QA Engineer Simulation for a product with automated and manual QA coverage: Use `/goal` as a quality loop until tests pass and lint is clean.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `tests pass && lint clean`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Use `/goal` as a quality loop until tests pass and lint is clean.
- The verification command or evidence path succeeds: `tests pass && lint clean`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `tests pass && lint clean` or the closest repo-local equivalent if the exact command is not available.
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

<a id="reddit-trading-backlog-clearance"></a>
### Clear Trading App Backlog

- Category: `backlog`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Generate a roadmap backlog for a trading app and then clear it with goals.
- Verification: `backlog cleared`
- Source: [Reddit r/codex](https://www.reddit.com/r/codex/comments/1t7b3x1/goal_in_the_codex_app_is_amazing/)
- Source type: `public-forum`
- Evidence: 210 task backlog

```text
/goal
GOAL:
Complete Clear Trading App Backlog for a backlog execution task: Generate a roadmap backlog for a trading app and then clear it with goals.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect roadmaps, backlog files, issue queues, acceptance criteria, and CI evidence.
- Establish a baseline by running or locating evidence for: `backlog cleared`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not expand the backlog while executing it.
- Keep each finished item tied to its original acceptance criteria.

DONE WHEN:
- The implementation or documentation directly satisfies: Generate a roadmap backlog for a trading app and then clear it with goals.
- The verification command or evidence path succeeds: `backlog cleared`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `backlog cleared` or the closest repo-local equivalent if the exact command is not available.
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

<a id="reddit-ship-backlog-features"></a>
### Ship Backlog Features

- Category: `backlog`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Implement the feature list from BACKLOG.md until CI is green.
- Verification: `CI green`
- Source: [Reddit r/WebAfterAI](https://www.reddit.com/r/WebAfterAI/comments/1t6lgsb/openai_just_dropped_goal_in_codex_set_a_goal_and/)
- Source type: `public-forum`
- Evidence: /goal ship the 18 features

```text
/goal
GOAL:
Complete Ship Backlog Features for a backlog execution task: Implement the feature list from BACKLOG.md until CI is green.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect roadmaps, backlog files, issue queues, acceptance criteria, and CI evidence.
- Establish a baseline by running or locating evidence for: `CI green`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not expand the backlog while executing it.
- Keep each finished item tied to its original acceptance criteria.

DONE WHEN:
- The implementation or documentation directly satisfies: Implement the feature list from BACKLOG.md until CI is green.
- The verification command or evidence path succeeds: `CI green`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `CI green` or the closest repo-local equivalent if the exact command is not available.
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

<a id="reddit-tests-pass-pr-ready"></a>
### Tests Pass And PR Ready

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Keep Claude Code working until tests pass and the PR is ready for review.
- Verification: `tests pass`
- Source: [Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1taty8a/claude_code_just_shipped_a_run_until_done_mode/)
- Source type: `public-forum`
- Evidence: all tests pass and the PR is ready

```text
/goal
GOAL:
Complete Tests Pass And PR Ready for a project with failing or missing verification gates: Keep Claude Code working until tests pass and the PR is ready for review.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `tests pass`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Keep Claude Code working until tests pass and the PR is ready for review.
- The verification command or evidence path succeeds: `tests pass`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `tests pass` or the closest repo-local equivalent if the exact command is not available.
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

<a id="reddit-billing-empty-state"></a>
### Billing Empty State Root Cause

- Category: `investigation`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Find why active subscriptions show an empty state without changing pricing or webhook code.
- Verification: `npm test`
- Source: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1taelgl/what_improved_my_claude_code_workflow_stop/)
- Source type: `public-forum`
- Evidence: billing page shows an empty state

```text
/goal
GOAL:
Complete Billing Empty State Root Cause for an investigation task: Find why active subscriptions show an empty state without changing pricing or webhook code.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect logs, traces, reproduction notes, source paths, and the final report.
- Establish a baseline by running or locating evidence for: `npm test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Separate observed evidence from hypotheses.
- Do not patch production code until the root cause is reproduced or strongly evidenced.

DONE WHEN:
- The implementation or documentation directly satisfies: Find why active subscriptions show an empty state without changing pricing or webhook code.
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

<a id="reddit-rag-chat-flywheel"></a>
### RAG Chat Flywheel

- Category: `prompt-optimization`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Iterate on code, tests, and metrics to improve a document-chat RAG system.
- Verification: `Playwright tests and metric review`
- Source: [Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1pe5nnw/update_1_creating_a_claude_code_flywheel/)
- Source type: `public-forum`
- Evidence: continually improve my RAG based document chat

```text
/goal
GOAL:
Complete RAG Chat Flywheel for an eval-backed prompt project: Iterate on code, tests, and metrics to improve a document-chat RAG system.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompt files, eval cases, scoring reports, regressions, and failure examples.
- Establish a baseline by running or locating evidence for: `Playwright tests and metric review`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete, weaken, or cherry-pick eval cases to improve the score.
- Report representative failures as well as the final score.

DONE WHEN:
- The implementation or documentation directly satisfies: Iterate on code, tests, and metrics to improve a document-chat RAG system.
- The verification command or evidence path succeeds: `Playwright tests and metric review`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `Playwright tests and metric review` or the closest repo-local equivalent if the exact command is not available.
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

<a id="hn-button-console-error-fix"></a>
### Button Console Error Fix

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use browser automation to click a button, inspect console errors, fix the issue, and prove it.
- Verification: `Playwright interaction`
- Source: [HN Playwright Skill](https://news.ycombinator.com/item?id=45642911)
- Source type: `public-forum`
- Evidence: console error when you click the button

```text
/goal
GOAL:
Complete Button Console Error Fix for a web frontend application: Use browser automation to click a button, inspect console errors, fix the issue, and prove it.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `Playwright interaction`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Use browser automation to click a button, inspect console errors, fix the issue, and prove it.
- The verification command or evidence path succeeds: `Playwright interaction`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `Playwright interaction` or the closest repo-local equivalent if the exact command is not available.
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

<a id="hn-review-sentiment-json-agent"></a>
### Review Sentiment JSON Agent

- Category: `research`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Fetch reviews with browser automation, classify sentiment, and write structured JSON output.
- Verification: `JSON files written`
- Source: [HN You Should Write An Agent](https://news.ycombinator.com/item?id=45840088)
- Source type: `public-forum`
- Evidence: fetch ten reviews

```text
/goal
GOAL:
Complete Review Sentiment JSON Agent for a research task: Fetch reviews with browser automation, classify sentiment, and write structured JSON output.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect source lists, citation notes, evidence files, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `JSON files written`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not present unsourced claims as facts.
- Keep direct quotes short and attach a public URL for every external claim.

DONE WHEN:
- The implementation or documentation directly satisfies: Fetch reviews with browser automation, classify sentiment, and write structured JSON output.
- The verification command or evidence path succeeds: `JSON files written`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `JSON files written` or the closest repo-local equivalent if the exact command is not available.
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

<a id="hn-dag-agent-dispatch"></a>
### DAG Agent Dispatch

- Category: `orchestration`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Split a goal into a dependency graph and dispatch independent agents into isolated worktrees.
- Verification: `PR output`
- Source: [HN Astro](https://news.ycombinator.com/item?id=47355676)
- Source type: `public-forum`
- Evidence: isolated git worktree and opens a PR

```text
/goal
GOAL:
Complete DAG Agent Dispatch for an agent orchestration task: Split a goal into a dependency graph and dispatch independent agents into isolated worktrees.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect plans, worktrees, subtask ownership, PRs, and coordination notes.
- Establish a baseline by running or locating evidence for: `PR output`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Keep subtask ownership explicit and avoid overlapping write scopes.
- Do not merge or deploy automatically unless the goal explicitly allows it.

DONE WHEN:
- The implementation or documentation directly satisfies: Split a goal into a dependency graph and dispatch independent agents into isolated worktrees.
- The verification command or evidence path succeeds: `PR output`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `PR output` or the closest repo-local equivalent if the exact command is not available.
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

<a id="video-nextjs-chat-sidebar"></a>
### Next.js Chat History Sidebar

- Category: `frontend`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Replace a Next.js sidebar with chat history, then test, fix build issues, and push.
- Verification: `tests and build`
- Source: [VideoHighlight YouTube summary](https://videohighlight.com/v/AJpK3YTTKZ4)
- Source type: `video-summary`
- Evidence: replace a sidebar with chat history

```text
/goal
GOAL:
Complete Next.js Chat History Sidebar for a web frontend application: Replace a Next.js sidebar with chat history, then test, fix build issues, and push.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect routes, components, state, stories, tests, and screenshots.
- Establish a baseline by running or locating evidence for: `tests and build`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change unrelated routes or rewrite the design system.
- Preserve existing accessibility and keyboard behavior unless the goal explicitly improves it.

DONE WHEN:
- The implementation or documentation directly satisfies: Replace a Next.js sidebar with chat history, then test, fix build issues, and push.
- The verification command or evidence path succeeds: `tests and build`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `tests and build` or the closest repo-local equivalent if the exact command is not available.
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

<a id="video-rift-salvage-game"></a>
### Rift Salvage Game Goal

- Category: `prototype`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Build a 2D combat game prototype with assets, combat, boss logic, and browser verification.
- Verification: `browser verification`
- Source: [Pogovet YouTube summary](https://pogovet.com/youtube/codex-just-became-the-best-long-running-agentic-harness)
- Source type: `video-summary`
- Evidence: 2D combat game Rift Salvage

```text
/goal
GOAL:
Complete Rift Salvage Game Goal for a prototype project: Build a 2D combat game prototype with assets, combat, boss logic, and browser verification.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PLAN.md, milestones, app code, tests, browser checks, and demo notes.
- Establish a baseline by running or locating evidence for: `browser verification`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Follow the stated PLAN.md or acceptance criteria instead of adding unrequested features.
- Keep the prototype runnable and demonstrable at every completed milestone.

DONE WHEN:
- The implementation or documentation directly satisfies: Build a 2D combat game prototype with assets, combat, boss logic, and browser verification.
- The verification command or evidence path succeeds: `browser verification`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `browser verification` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-claude-goal-flaky-auth"></a>
### Flaky Auth Tests Goal

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use a Claude goal plugin example to find and fix flaky authentication tests.
- Verification: `python3 -m pytest tests`
- Source: [jthack/claude-goal](https://github.com/jthack/claude-goal)
- Source type: `tool-readme`
- Evidence: find and fix the flaky auth tests

```text
/goal
GOAL:
Complete Flaky Auth Tests Goal for a project with failing or missing verification gates: Use a Claude goal plugin example to find and fix flaky authentication tests.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `python3 -m pytest tests`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Use a Claude goal plugin example to find and fix flaky authentication tests.
- The verification command or evidence path succeeds: `python3 -m pytest tests`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `python3 -m pytest tests` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-pydantic-v2-migration"></a>
### Pydantic V1 To V2 Migration

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Migrate a project from Pydantic v1 to v2 while preserving API behavior.
- Verification: `pytest -q`
- Source: [jailbreak-autoresearch docs](https://github.com/davidondrej/jailbreak-autoresearch/blob/main/docs-slash-goal.md)
- Source type: `tool-readme`
- Evidence: Migrate this project from Pydantic v1 to v2

```text
/goal
GOAL:
Complete Pydantic V1 To V2 Migration for a migration project: Migrate a project from Pydantic v1 to v2 while preserving API behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `pytest -q`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Migrate a project from Pydantic v1 to v2 while preserving API behavior.
- The verification command or evidence path succeeds: `pytest -q`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `pytest -q` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-review-plan-no-gaps"></a>
### Review Plan Until No Gaps

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Loop on implementation-plan review until a fresh review finds no remaining gaps.
- Verification: `fresh plan review has no new gaps`
- Source: [openai/codex issue 21176](https://github.com/openai/codex/issues/21176)
- Source type: `github-issue`
- Evidence: review the plan ImplementationPlan.md

```text
/goal
GOAL:
Complete Review Plan Until No Gaps for a goal-management workflow: Loop on implementation-plan review until a fresh review finds no remaining gaps.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `fresh plan review has no new gaps`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Loop on implementation-plan review until a fresh review finds no remaining gaps.
- The verification command or evidence path succeeds: `fresh plan review has no new gaps`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `fresh plan review has no new gaps` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-noninteractive-goal-creation"></a>
### Non-Interactive Goal Creation

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Create and confirm an active goal during non-interactive Codex execution before continuing.
- Verification: `get_goal and thread_goals evidence`
- Source: [openai/codex discussion 21764](https://github.com/openai/codex/discussions/21764)
- Source type: `github-discussion`
- Evidence: Build the Meta0 LifeOS ontology boundary artifact

```text
/goal
GOAL:
Complete Non-Interactive Goal Creation for a coding-agent workflow repository: Create and confirm an active goal during non-interactive Codex execution before continuing.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `get_goal and thread_goals evidence`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Create and confirm an active goal during non-interactive Codex execution before continuing.
- The verification command or evidence path succeeds: `get_goal and thread_goals evidence`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `get_goal and thread_goals evidence` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-long-task-verification"></a>
### Long Task Until Verification

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Continue a long-running task until final verification passes rather than stopping on partial progress.
- Verification: `final verification`
- Source: [openai/codex issue 22049](https://github.com/openai/codex/issues/22049)
- Source type: `github-issue`
- Evidence: Complete a long-running task until final verification passes

```text
/goal
GOAL:
Complete Long Task Until Verification for a goal-management workflow: Continue a long-running task until final verification passes rather than stopping on partial progress.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `final verification`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Continue a long-running task until final verification passes rather than stopping on partial progress.
- The verification command or evidence path succeeds: `final verification`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `final verification` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-benchmark-coverage-goal"></a>
### Improve Benchmark Coverage

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use `/goal` to improve benchmark coverage and persist the command in history.
- Verification: `cargo test -p codex-tui goal_slash_command -- --nocapture`
- Source: [openai/codex PR 21860](https://github.com/openai/codex/pull/21860)
- Source type: `github-pr`
- Evidence: /goal improve benchmark coverage

```text
/goal
GOAL:
Complete Improve Benchmark Coverage for a project with failing or missing verification gates: Use `/goal` to improve benchmark coverage and persist the command in history.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `cargo test -p codex-tui goal_slash_command -- --nocapture`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Use `/goal` to improve benchmark coverage and persist the command in history.
- The verification command or evidence path succeeds: `cargo test -p codex-tui goal_slash_command -- --nocapture`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `cargo test -p codex-tui goal_slash_command -- --nocapture` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-completion-audit-before-done"></a>
### Completion Audit Before Done

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Audit completion criteria before calling the goal complete.
- Verification: `focused coverage and evals`
- Source: [openai/codex PR 22045](https://github.com/openai/codex/pull/22045)
- Source type: `github-pr`
- Evidence: completion audits before calling update_goal

```text
/goal
GOAL:
Complete Completion Audit Before Done for a goal-management workflow: Audit completion criteria before calling the goal complete.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `focused coverage and evals`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Audit completion criteria before calling the goal complete.
- The verification command or evidence path succeeds: `focused coverage and evals`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `focused coverage and evals` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-goal-permission-context"></a>
### Goal Permission Context Sync

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Ensure goal continuation uses the current permission context after approval mode changes.
- Verification: `cargo check focused crates`
- Source: [openai/codex issue 22090](https://github.com/openai/codex/issues/22090)
- Source type: `github-issue`
- Evidence: uses stale permission context

```text
/goal
GOAL:
Complete Goal Permission Context Sync for a goal-management workflow: Ensure goal continuation uses the current permission context after approval mode changes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `cargo check focused crates`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Ensure goal continuation uses the current permission context after approval mode changes.
- The verification command or evidence path succeeds: `cargo check focused crates`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `cargo check focused crates` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-goalbuddy-workspace"></a>
### Prep A Goal Workspace

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command.
- Verification: `board, receipts, and verify files`
- Source: [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy)
- Source type: `tool-readme`
- Evidence: prints the exact /goal command

```text
/goal
GOAL:
Complete Prep A Goal Workspace for a coding-agent workflow repository: Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `board, receipts, and verify files`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command.
- The verification command or evidence path succeeds: `board, receipts, and verify files`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `board, receipts, and verify files` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-claude-batch-bugs"></a>
### Batch Fix Bugs

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use a Claude Code goal to fix a numbered batch of bugs without looping on missing skills.
- Verification: `no unsatisfied skill loop`
- Source: [anthropics/claude-code issue 58348](https://github.com/anthropics/claude-code/issues/58348)
- Source type: `github-issue`
- Evidence: /goal Fix bugs #1-#6

```text
/goal
GOAL:
Complete Batch Fix Bugs for a project with failing or missing verification gates: Use a Claude Code goal to fix a numbered batch of bugs without looping on missing skills.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `no unsatisfied skill loop`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Use a Claude Code goal to fix a numbered batch of bugs without looping on missing skills.
- The verification command or evidence path succeeds: `no unsatisfied skill loop`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `no unsatisfied skill loop` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-claude-long-goal-template"></a>
### Long Goal With Constraints

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use a longer goal template with repo path, constraints, plan pointer, and execution order.
- Verification: `stop hook evaluates cleanly`
- Source: [anthropics/claude-code issue 58192](https://github.com/anthropics/claude-code/issues/58192)
- Source type: `github-issue`
- Evidence: Goal: <several lines of overarching aim>

```text
/goal
GOAL:
Complete Long Goal With Constraints for a coding-agent workflow repository: Use a longer goal template with repo path, constraints, plan pointer, and execution order.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `stop hook evaluates cleanly`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Use a longer goal template with repo path, constraints, plan pointer, and execution order.
- The verification command or evidence path succeeds: `stop hook evaluates cleanly`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `stop hook evaluates cleanly` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-hermes-real-cli-loop"></a>
### Real CLI Goal Loop

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Verify a real CLI goal loop where the second judge round confirms completion.
- Verification: `live judge round-trip`
- Source: [NousResearch/hermes-agent PR 18262](https://github.com/NousResearch/hermes-agent/pull/18262)
- Source type: `github-pr`
- Evidence: print hello, Ralph loop

```text
/goal
GOAL:
Complete Real CLI Goal Loop for a goal-management workflow: Verify a real CLI goal loop where the second judge round confirms completion.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `live judge round-trip`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify a real CLI goal loop where the second judge round confirms completion.
- The verification command or evidence path succeeds: `live judge round-trip`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `live judge round-trip` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-hermes-file-verification"></a>
### Verify File Creation

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Verify that a requested file was actually created instead of trusting the agent claim.
- Verification: `find and read_file evidence`
- Source: [NousResearch/hermes-agent issue 18421](https://github.com/NousResearch/hermes-agent/issues/18421)
- Source type: `github-issue`
- Evidence: /home/ubuntu/ml-resumo.md

```text
/goal
GOAL:
Complete Verify File Creation for a goal-management workflow: Verify that a requested file was actually created instead of trusting the agent claim.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `find and read_file evidence`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Verify that a requested file was actually created instead of trusting the agent claim.
- The verification command or evidence path succeeds: `find and read_file evidence`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `find and read_file evidence` or the closest repo-local equivalent if the exact command is not available.
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

<a id="github-hermes-goal-queue"></a>
### Queue Follow-Up Goals

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Promote queued follow-up goals: fix tests, run full tests, then produce coverage.
- Verification: `queue promotion evidence`
- Source: [NousResearch/hermes-agent issue 22617](https://github.com/NousResearch/hermes-agent/issues/22617)
- Source type: `github-issue`
- Evidence: /goal Fix failing tests

```text
/goal
GOAL:
Complete Queue Follow-Up Goals for a goal-management workflow: Promote queued follow-up goals: fix tests, run full tests, then produce coverage.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `queue promotion evidence`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Promote queued follow-up goals: fix tests, run full tests, then produce coverage.
- The verification command or evidence path succeeds: `queue promotion evidence`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `queue promotion evidence` or the closest repo-local equivalent if the exact command is not available.
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

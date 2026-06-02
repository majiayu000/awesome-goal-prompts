# Goal Prompt Examples

Each example is a complete `/goal` task contract. Replace placeholder commands, paths, and project names with your repository's real values before running.

These examples intentionally use only the documented `/goal <goal>` form. They do not rely on unofficial subcommands.

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
- [API Integration Tests](#openhands-api-integration-tests) - Add end-to-end tests for product API endpoints with success and error cases. Source-backed.
- [User Preferences API](#openhands-user-preferences-api) - Add GET, PUT, and PATCH endpoints for user preferences with validation, service logic, OpenAPI docs, and tests. Source-backed.
- [SPARC Payment Processing Plan](#claude-flow-sparc-payment-plan) - Plan and implement payment processing through SPARC phases with requirements, pseudocode, architecture, TDD refinement, and integration. Source-backed.

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
- [Dev Database Migration Proof](#claude-dev-database-migration) - Write a migration, run it against the dev database, and confirm the schema matches. Source-backed.
- [Slow Query Optimization Report](#openhands-slow-query-optimization) - Analyze slow query logs, explain bottlenecks, recommend indexes or rewrites, and produce prioritized SQL changes. Source-backed.
- [Deadlock-Minimizing Transaction Rewrite](#github-copilot-deadlock-minimization) - Rewrite transaction ordering and locking to reduce deadlock risk without adverse performance or data-integrity regressions. Source-backed.

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
- [Bounded Autopilot CI Repair](#github-copilot-autopilot-ci-repair) - Run a bounded autonomous CI repair after plan acceptance, with explicit continuation limits, permissions, validation commands, and blocker reporting. Source-backed.

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
- [Remote Agent Server Smoke](#openhands-remote-agent-server-smoke) - Deploy an isolated remote agent server and prove event streaming, workspace access, and command execution work. Source-backed.

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
- [Tool Guardrails For AppSec](#openai-tool-guardrails-appsec) - Add tool guardrails around high-risk agent tool calls and stop unsafe input or output before execution continues. Source-backed.
- [Security PR Review](#openhands-security-pr-review) - Review a pull request for input validation, authentication, injection, XSS, and secrets risks with file-level fixes. Source-backed.
- [Unsafe innerHTML XSS Fix](#github-copilot-xss-innerhtml-fix) - Find and fix XSS caused by unsafe innerHTML rendering while preserving the user-visible text and adding a regression guard. Source-backed.

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
- [CSV Processing Report](#openhands-csv-processing-report) - Create a data processing script that validates CSV input and generates an analysis report. Source-backed.
- [Rate-Limited Web Scraper](#openhands-rate-limited-web-scraper) - Build a scraper that extracts product data across paginated pages while respecting rate limits and logging progress. Source-backed.

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
- [Copilot Usage Metrics Reconciliation](#github-copilot-usage-metrics-reconciliation) - Reconcile Copilot dashboard, API, and export metrics before reporting agent adoption or pull-request impact trends. Source-backed.

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
- [Trace-Graded Agent Regression](#openai-agent-trace-evals) - Create trace-based evals that catch workflow regressions across tool calls and handoffs. Source-backed.
- [Promptfoo Eval Suite](#openai-promptfoo-eval-suite) - Add a runnable Promptfoo eval suite for an AI application before changing production prompts or model behavior. Source-backed.

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
- [Agent Trace Observability](#openai-agent-tracing-observability) - Instrument agent runs so LLM generations, tool calls, handoffs, guardrails, and custom events are traceable. Source-backed.
- [OpenSpec Rerank Provider Goal](#goal-builder-openspec-rerank-provider) - Implement an OpenSpec feature change exactly as specified, adding a new rerank provider with contract tests, integration coverage, docs, and changelog evidence. Source-backed.

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
- [Reference Layout Match](#claude-reference-layout-design) - Build a settings page that follows an existing profile page layout instead of inventing a new pattern. Source-backed.
- [Design System Context Export](#layout-design-system-context-export) - Extract design tokens, components, and visual patterns into agent-readable context so generated UI follows the product design system. Source-backed.

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
- [Mobile Agent Task Handoff](#github-mobile-agent-task-handoff) - Prepare and track a coding-agent task started from GitHub Mobile with review-ready evidence. Source-backed.
- [Expo React Native App Slice](#openai-expo-react-native-app) - Build a working React Native app slice with Expo Router conventions, Expo-compatible packages, and native-feeling UI states. Source-backed.

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
- [Payment Retry Logic Diagram](#claude-payment-retry-diagram) - Explain payment retry behavior as a browsable HTML page with a diagram for developer or support review. Source-backed.
- [Implementation Notes Decision Ledger](#deadreckon-implementation-notes-ledger) - Keep live implementation notes and the final run decisions document aligned around decisions, deviations, tradeoffs, and open questions. Source-backed.
- [Repository Agent Instructions](#github-copilot-repository-instructions) - Add repository-level agent instructions that document project structure, build/test/validate commands, coding standards, and documentation expectations. Source-backed.
- [Documentation Matches Code](#github-copilot-doc-code-sync) - Update stale API or function documentation so parameters, behavior, examples, thrown errors, and links match the current implementation. Source-backed.

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
- [Feature Flag System](#openhands-feature-flag-system) - Implement boolean, percentage, and user-based feature flags with service logic, API middleware, a React hook, docs, and tests. Source-backed.
- [OKR Development From Vague Priorities](#claude-recipes-okr-development) - Turn vague strategic priorities into measurable OKRs with objectives, key results, alignment, scoring, guardrails, and a communication summary. Source-backed.

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
- [Terminal Agentic Code Review](#github-copilot-cli-agentic-review) - Review a diff from the terminal with a scoped prompt, path, or file pattern, inspect suggested commands, and apply or reject findings before commit. Source-backed.

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
- [HTML WCAG Instruction Audit](#github-accessibility-html-wcag) - Audit HTML changes against WCAG guidance and prove the Lighthouse accessibility audit passes. Source-backed.

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
- [Order Service Performance Review](#openhands-orderservice-performance-review) - Inspect service code for N+1 queries, missing indexes, inefficient loops, missing caches, and unnecessary fetching. Source-backed.
- [Node Memory Leak Fix](#openhands-node-memory-leak-fix) - Investigate a growing-memory Node.js process, isolate the leak source, fix it, and add monitoring for recurrence. Source-backed.
- [GOAP API Latency Reduction](#claude-flow-api-latency-goap) - Reduce API latency by profiling current performance, optimizing database queries, adding caching, and improving code paths. Source-backed.
- [Checkout P95 Latency Goal](#halmob-checkout-p95-goal) - Reduce checkout p95 latency below a numeric target while keeping the correctness suite green and logging each experiment. Source-backed.

### workflow
- [Goal Prompt Writer](#goal-meta-prompt-writer) - Ask the agent to inspect a repo and write a precise goal prompt before execution.
- [Goal Continuation Audit](#goal-continuation-audit) - Check that a long-running goal keeps its done_when and verification contract after compaction.
- [Verifiable End-State Contract](#codex-verifiable-end-state) - Complete one goal only when a verifiable end state is met. Source-backed.
- [Four Files Walkthrough](#hermes-four-files-walkthrough) - Create four note files across turns and verify each contains its number. Source-backed.
- [Meta Goal Prompt Generator](#x-meta-goal-prompt-generator) - Ask the agent to inspect the session, repo, history, and docs before writing the actual `/goal` prompt. Source-backed.
- [AGENTS.md Goal Workflow](#x-agentsmd-goal-workflow) - Use AGENTS.md rules together with `/goal` so long-running work keeps repo-specific constraints. Source-backed.
- [Plan-Then-Goal Execution](#x-plan-then-goal-execution) - Use plan mode to define the work, then start a new goal session to implement the plan completely. Source-backed.
- [Measurable Goal Structure](#x-measurable-goal-structure) - Write goals with a clear target, proof requirement, and explicit limits. Source-backed.
- [Interview-Driven Goal Prompt Generator](#x-interview-driven-goal-prompt-generator) - Use a meta prompt to interview the user with clarifying questions until 'done' can be expressed in specific, measurable, verifiable terms, then output a high-quality structured /goal prompt. Source-backed.
- [Non-Interactive Goal Creation](#github-noninteractive-goal-creation) - Create and confirm an active goal during non-interactive Codex execution before continuing. Source-backed.
- [Prep A Goal Workspace](#github-goalbuddy-workspace) - Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command. Source-backed.
- [Long Goal With Constraints](#github-claude-long-goal-template) - Use a longer goal template with repo path, constraints, plan pointer, and execution order. Source-backed.
- [User-Facing Coherence Closure](#deadreckon-coherence-closure) - Finish a coherence pass so CLI help, docs, JSON/plain output, colors, prompts, flags, and next-action grammar stay aligned. Source-backed.
- [Three Questions Goal Framework](#x-three-questions-goal-framework) - Write higher quality goals by explicitly answering three core questions: what needs to be done, how success will be measured, and what is off-limits. Source-backed.
- [Explicit Stop Rules for Goal Loops](#x-explicit-stop-rules-goal-loops) - Prevent infinite loops, cost overruns, and unsafe behavior in autonomous /goal executions by defining clear, explicit stop conditions and escalation rules. Source-backed.
- [Dual-Model Evaluator Loop for Goals](#x-dual-model-evaluator-goal-loop) - Run long /goal sessions reliably and cost-effectively by using a strong worker model for execution paired with a cheap fast evaluator model (typically Haiku) that periodically judges progress against the goal criteria and decides whether to continue or stop. Source-backed.
- [CLAUDE.md + Goal Workflow](#x-claude-md-goal-workflow) - Combine a persistent project-level CLAUDE.md (or AGENTS.md) file containing rules, standards, and context with /goal commands so long-running autonomous agent work stays aligned with repository-specific constraints and learned lessons. Source-backed.
- [Goal Ledger for Long-Running Runs](#x-goal-ledger) - Maintain a live, browser-viewable HTML progress ledger during extended /goal executions to provide visibility, persistent memory, decision logging, and self-reflection, reducing drift in long autonomous sessions. Source-backed.
- [Well-Scoped Agent Issue](#github-copilot-well-scoped-agent-issue) - Turn a backlog item into a coding-agent-ready issue with a clear problem statement, acceptance criteria, file directions, and test expectations. Source-backed.
- [Research And Plan Before PR](#github-copilot-plan-before-pr) - Have an agent research the repository, create an implementation plan, and iterate on a branch before deciding whether to open a pull request. Source-backed.
- [Goalcraft Six-Field Contract Spine](#codex-goalcraft-six-field-contract) - Write any /goal as a compact, evidence-first, thread-scoped completion contract with explicit outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop conditions instead of vague effort descriptions. Source-backed.
- [Strong Verifiable Goal Contract After Alignment Interview](#chinese-v2ex-grillme-strong-goal-contract) - After a structured alignment interview, produce a binding /goal contract with explicit success evidence, hard constraints, file boundaries, iteration strategy, and blocking/escape handling so a Ralph-loop or native /goal agent can run autonomously until evidence-based completion. Source-backed.

### migration
- [Visual Migration With Playwright](#codex-visual-migration-playwright) - Migrate a project while preserving screen output and checking it with Playwright. Source-backed.
- [Feature Port With CI Green](#hermes-feature-port-ci-green) - Port a feature from another repo, include tests, and get CI green. Source-backed.
- [Vue 2 To Vue 3 Visual And Unit Gate](#qiita-vue2-vue3-visual-unit) - Migrate listed Vue screens and stop only when visual and unit tests pass. Source-backed.
- [Finish Migration Keep Tests Green](#openai-slash-finish-migration) - Use `/goal` to complete a migration while keeping the relevant tests green. Source-backed.
- [Module API Migration](#claude-module-api-migration) - Migrate a module to a new API while keeping call sites compiling and tests passing. Source-backed.
- [Moment To Day.js Migration](#explainx-moment-dayjs-migration) - Replace Moment.js with Day.js while preserving date output across edge cases. Source-backed.
- [React 19 Migration](#cursor-forum-react19-migration) - Migrate a project to React 19 and continue until the build passes. Source-backed.
- [Pydantic V1 To V2 Migration](#github-pydantic-v2-migration) - Migrate a project from Pydantic v1 to v2 while preserving API behavior. Source-backed.
- [Code Migration Checkpoints](#openai-code-migration-checkpoints) - Inventory legacy assumptions, map them to a target stack, and execute the migration through validated checkpoints. Source-backed.

### prototype
- [PLAN.md Milestone Prototype](#codex-plan-milestone-prototype) - Implement a PLAN.md-driven prototype with tests at each milestone and browser verification. Source-backed.
- [Canvas Puzzle PLAN.md Prototype](#qiita-canvas-puzzle-plan) - Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes. Source-backed.
- [Rift Salvage Game Goal](#video-rift-salvage-game) - Build a 2D combat game prototype with assets, combat, boss logic, and browser verification. Source-backed.

### prompt-optimization
- [Eval-Driven Prompt Optimization](#codex-eval-prompt-optimization) - Optimize prompts against an eval suite until the target score or pass rate is reached. Source-backed.
- [Router Prompt Eval Score](#qiita-router-eval-score) - Improve a router prompt against an eval directory until the result score reaches a target. Source-backed.
- [RAG Chat Flywheel](#reddit-rag-chat-flywheel) - Iterate on code, tests, and metrics to improve a document-chat RAG system. Source-backed.
- [Difficult Task Eval Loop](#openai-difficult-task-eval-loop) - Run a difficult task as an eval-driven improvement loop with one focused change, rerun scores, and direct artifact inspection each iteration. Source-backed.
- [Fitness Function Dual-Score Improvement Loop](#goal-md-fitness-dual-score-loop) - For goals without natural scalar metric (docs quality, code health, consistency), construct an explicit runnable fitness function plus dual-score (outcome + instrument quality guard) and drive an improvement loop with iterations.jsonl ledger until converge criteria. Source-backed.

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
- [GOAP Coverage Target Plan](#claude-flow-coverage-goap) - Raise test coverage with an explicit test pyramid across unit, integration, and end-to-end coverage targets. Source-backed.
- [Playwright Test Instructions](#github-copilot-playwright-instructions) - Create path-specific Playwright instructions that enforce stable locators, isolated tests, explicit assertions, cross-browser coverage, and CI behavior. Source-backed.
- [Voice E2E Goal Contract](#tecton-codex-voice-e2e-contract) - Run a long-horizon Codex goal against a TypeScript voice system using a reading list, working rules, concrete done-when criteria, and anti-pattern fences. Source-backed.

### investigation
- [Session Drift Report](#hermes-session-drift-report) - Investigate session ID drift during mid-run compression and write a report. Source-backed.
- [Billing Empty State Root Cause](#reddit-billing-empty-state) - Find why active subscriptions show an empty state without changing pricing or webhook code. Source-backed.
- [Checkout Crash Regression Fix](#openhands-checkout-crash-regression) - Reproduce a checkout crash from a stack trace, identify the root cause, fix it, and add a regression test. Source-backed.
- [Build Log Failure Diagnosis](#claude-build-log-diagnosis) - Use a provided build log to explain why the build fails and identify the smallest verified fix path. Source-backed.

### cli
- [EXIF Rename CLI](#hermes-exif-rename-cli) - Build a small CLI that renames photos by EXIF date and test it on a photos folder. Source-backed.
- [Agent-Friendly CLI And Skill](#openai-agent-friendly-cli-skill) - Create a composable CLI and companion skill so future agent tasks can search, read, download, or draft against a recurring source safely. Source-backed.

### refactor
- [Auth Dependency Injection Refactor](#explainx-auth-di-refactor) - Refactor auth code to dependency injection while preserving tests, coverage, and public API. Source-backed.
- [Split Oversized File](#claude-split-oversized-file) - Split an oversized source file into focused modules while preserving behavior. Source-backed.
- [Centralize Cross-Cutting Logging](#github-copilot-cross-cutting-logging) - Centralize scattered logging, validation, security, or error-handling behavior without changing the core business behavior of the services. Source-backed.

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
- [Clinical Research AI Safety Boundary](#clinical-research-ai-safety-boundary) - Review clinical research AI work with evidence-first boundaries so agents do not invent medical sources, expose private data, or turn research notes into patient-specific advice. Source-backed.
- [Cited Architecture Research Report](#github-copilot-research-architecture-report) - Produce a saved, cited Markdown architecture report after inspecting the local codebase, relevant repositories, and web sources. Source-backed.
- [Evidence-Backed Research Reproduction](#halmob-research-reproduction-goal) - Reproduce a paper or research result as far as local materials allow while separating confirmed findings, approximate reconstructions, blocked claims, and remaining uncertainty. Source-backed.

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
- [Daily Goal Priority Loop](#goal-agent-daily-priority-loop) - Use a persistent goal profile to compute daily priorities, execute them, log progress, and refresh status across sessions. Source-backed.
- [Goal-Aligned Profile Optimization](#goal-agent-profile-optimization) - Audit and update professional profiles against a stated goal while recording the resulting progress and gaps. Source-backed.
- [Content And Audience Engagement Loop](#goal-agent-content-engagement-loop) - Generate goal-aligned content, publish or promote it, engage with target audience posts, and log the session outcome. Source-backed.
- [Define Goal Quality Bar](#openai-define-goal-quality-bar) - Turn a fuzzy intention into a concrete measurable goal with evidence, scope boundaries, and honest stop conditions before creating it. Source-backed.
- [Audit-Friendly Goal Template](#goal-builder-audit-friendly-template) - Rewrite a vague /goal into a mappable contract with objective, scope, constraints, done-when evidence, stop rules, and token budget. Source-backed.
- [Single-File HTML Goal Ledger with Resume Block and Structured Incomplete Escape](#goal-ledger-html-resume-incomplete-hatch) - Maintain one canonical browser-viewable implementation-notes.html containing Resume Here block, inline progressEvents timeline, and explicit [incomplete]/[blocked] states with full reason/proof/impact so long-running /goal can safely pause and resume across compaction or handoff without drift. Source-backed.

### orchestration
- [DAG Agent Dispatch](#hn-dag-agent-dispatch) - Split a goal into a dependency graph and dispatch independent agents into isolated worktrees. Source-backed.
- [DAG-Aware Semantic Merge Repair](#deadreckon-semantic-merge-repair) - Make orchestration merge failures repairable by using plan DAG context, conflict bundles, planner-mediated repair, and bounded retry. Source-backed.
- [Plan EventBus Live UX](#deadreckon-orchestration-eventbus) - Unify plan, fork, merge, and orchestrate around shared builders and a live plan event stream. Source-backed.
- [Fleet Parallel Test Suite](#github-copilot-fleet-parallel-test-suite) - Break a large test expansion into independent subtasks that subagents can execute in parallel while the orchestrator manages dependencies and final integration. Source-backed.

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
- Intent: Complete one goal only when a verifiable end state is met.
- Verification: `manual status plus repo-local verification`
- Source: [OpenAI Codex docs](https://developers.openai.com/codex/use-cases/follow-goals)
- Source type: `official-goal`
- Evidence: verifiable stopping condition
- Evidence summary: verifiable stopping condition; source: OpenAI Codex docs; type: official-goal; verification: manual status plus repo-local verification

```text
/goal
GOAL:
Complete Verifiable End-State Contract for a coding-agent workflow repository: Complete one goal only when a verifiable end state is met.

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
- The implementation or documentation directly satisfies: Complete one goal only when a verifiable end state is met.
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
- Evidence summary: visual migration; source: OpenAI Codex docs; type: official-goal; verification: npx playwright test

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
- Evidence summary: PLAN.md; source: OpenAI Codex docs; type: official-goal; verification: npx playwright test

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
- Evidence summary: eval suite; source: OpenAI Codex docs; type: official-goal; verification: python -m pytest evals

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
- Evidence summary: test/auth pass; source: Claude Code docs; type: official-goal; verification: npm test -- test/auth && npm run lint

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
- Evidence summary: CHANGELOG.md has an entry; source: Claude Code docs; type: official-goal; verification: git log --since='7 days ago' --merges && rg '^-' CHANGELOG.md

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
- Evidence summary: ruff check; source: Hermes docs; type: official-goal; verification: ruff check src/

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
- Evidence summary: CI green; source: Hermes docs; type: official-goal; verification: pytest && npm test

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
- Evidence summary: write up a report; source: Hermes docs; type: official-goal; verification: test -f reports/session-drift.md

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
- Evidence summary: photos/ folder; source: Hermes docs; type: official-goal; verification: pytest tests/cli && ./rename-exif photos/ --dry-run

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
- Evidence summary: Create four files; source: Hermes docs; type: official-goal; verification: for i in 1 2 3 4; do test "$(cat /tmp/note_$i.txt)" = "$i"; done

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
- Evidence summary: TypeScript errors resolved; source: ExplainX blog; type: third-party-tutorial; verification: npm run typecheck && npm test && npm run lint && npm run coverage

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
- Evidence summary: auth.ts dependency injection; source: ExplainX blog; type: third-party-tutorial; verification: npm test -- auth && npm run coverage

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
- Evidence summary: npm audit vulnerabilities patched; source: ExplainX blog; type: third-party-tutorial; verification: npm audit && npm test

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
- Evidence summary: Lighthouse performance score >95; source: ExplainX blog; type: third-party-tutorial; verification: npm run lighthouse

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
- Evidence summary: pnpm test:visual; source: Qiita article; type: third-party-tutorial; verification: pnpm test:visual && pnpm test:unit

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
- Evidence summary: canvas puzzle; source: Qiita article; type: third-party-tutorial; verification: pnpm e2e

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
- Evidence summary: router prompt; source: Qiita article; type: third-party-tutorial; verification: python -m pytest evals/router

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
- Evidence summary: Finish the migration; source: OpenAI Codex slash commands; type: official-goal; verification: repo-local migration tests

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
- Evidence summary: verification steps; source: OpenAI Codex blog; type: official-workflow; verification: tests, lint, and typecheck per milestone

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
- Evidence summary: new API; source: Claude Code docs; type: official-goal; verification: compile call sites && tests pass

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
- Evidence summary: acceptance criteria; source: Claude Code docs; type: official-goal; verification: acceptance criteria review

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
- Evidence summary: size budget; source: Claude Code docs; type: official-goal; verification: module size budget && tests pass

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
- Evidence summary: queue is empty; source: Claude Code docs; type: official-goal; verification: issue queue empty

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
- Evidence summary: scripts/run_tests.sh passes; source: Hermes docs; type: official-goal; verification: scripts/run_tests.sh

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
- Evidence summary: Analyze Tab vs Agent Usage Patterns; source: Cursor product page; type: official-agent-task; verification: analysis files and tests shown

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
- Evidence summary: Chart tooltips freeze; source: Cursor product page; type: official-agent-task; verification: frontend diff plus interaction verification

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
- Evidence summary: user friendly message; source: GitHub Copilot docs; type: official-agent-task; verification: pushed code changes

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
- Evidence summary: Add auth tests; source: Google Jules sessions docs; type: official-agent-task; verification: session completed with PR output

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
- Evidence summary: Target coverage: 80%; source: OpenHands tutorials; type: official-agent-task; verification: coverage target evidence

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
- Evidence summary: below 50% coverage; source: Devin advanced capabilities; type: official-agent-task; verification: separate PR per module

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
- Evidence summary: pnpm exec vitest run -t; source: Qiita Aochan0604; type: third-party-tutorial; verification: pnpm exec vitest run -t "increments score only on correct answer"

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
- Evidence summary: pnpm exec vitest run exits 0; source: Qiita Aochan0604; type: third-party-tutorial; verification: pnpm exec vitest run

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
- Evidence summary: .correct and .wrong; source: Qiita Aochan0604; type: third-party-tutorial; verification: pnpm exec vitest run && git status --short

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
- Evidence summary: read-only font-match; source: J.D. Hodges blog; type: third-party-review; verification: written report

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
- Evidence summary: coverage from 38% to 75%; source: J.D. Hodges blog; type: third-party-review; verification: npm test

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
- Evidence summary: npm test exits 0; source: Apidog blog; type: third-party-tutorial; verification: npm test

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
- Evidence summary: 10 distinct benchmarks; source: Apidog blog; type: third-party-tutorial; verification: table covers 10 sources

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
- Evidence summary: dead code, unused dependencies; source: Apidog blog; type: third-party-tutorial; verification: each item has justification

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
- Evidence summary: README.md install/run/test; source: Apidog blog; type: third-party-tutorial; verification: commands and expected output documented

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
- Evidence summary: dark/light theme toggle; source: Apidog blog; type: third-party-tutorial; verification: browser refresh verification

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
- Evidence summary: All CI checks passing; source: ExplainX blog; type: third-party-tutorial; verification: local CI rerun and remote CI

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
- Evidence summary: Moment.js usage with Day.js; source: ExplainX blog; type: third-party-tutorial; verification: tests and edge-case output compare

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
- Evidence summary: public functions ... JSDoc; source: ExplainX blog; type: third-party-tutorial; verification: docs coverage and broken link check

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
- Evidence summary: Increase test coverage to 95%; source: Udit Autoresearch; type: third-party-project; verification: npm test -- --coverage

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
- Evidence summary: Reduce bundle size below 200KB; source: Udit Autoresearch; type: third-party-project; verification: npm run build and size report

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
- Evidence summary: npm run bench; source: Udit Autoresearch; type: third-party-project; verification: npm run bench

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
- Evidence summary: npm test exit code 0; source: TheAIDaily; type: third-party-tutorial; verification: npm test && npx tsc --noEmit

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
- Evidence summary: git status is clean; source: TheAIDaily; type: third-party-tutorial; verification: git status --short && file length check

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
- Evidence summary: React 19 until build passes; source: Cursor Forum; type: public-forum; verification: build passes

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
- Evidence summary: go test -race; source: Cursor Forum; type: public-forum; verification: go test -race

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
- Evidence summary: write me the /goal prompt for this; source: @meta_alchemist on X; type: x-post; verification: generated goal prompt with clarified uncertainties

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
- Evidence summary: /goal all tests pass and lint is clean; source: @sairahul1 on X; type: x-post; verification: tests pass && lint clean

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
- Evidence summary: /GOAL NEEDED AN ESCAPE HATCH; source: @KingBootoshi on X; type: x-post; verification: incomplete marker and rationale

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
- Evidence summary: combine it with /goal; source: @dhruvbaldawa on X; type: x-post; verification: AGENTS.md rules honored

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
- Evidence summary: done_when is intrinsic; source: @Michaelzsguo on X; type: x-post; verification: done_when audit

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
- Evidence summary: Use /plan mode to define the goal; source: @ivangdavila on X; type: x-post; verification: plan completed against checklist

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
- Evidence summary: Set a clear goal. Make it measurable.; source: @Arslandev97 on X; type: x-post; verification: proof and limits present

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
- Evidence summary: runs until tests pass and lint is clean; source: @LenaWithAI on X; type: x-post; verification: tests pass && lint clean

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
- Evidence summary: 210 task backlog; source: Reddit r/codex; type: public-forum; verification: backlog cleared

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
- Evidence summary: /goal ship the 18 features; source: Reddit r/WebAfterAI; type: public-forum; verification: CI green

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
- Evidence summary: all tests pass and the PR is ready; source: Reddit r/ClaudeCode; type: public-forum; verification: tests pass

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

<a id="x-interview-driven-goal-prompt-generator"></a>
### Interview-Driven Goal Prompt Generator

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use a meta prompt to interview the user with clarifying questions until 'done' can be expressed in specific, measurable, verifiable terms, then output a high-quality structured /goal prompt.
- Verification: `generated goal contains clear, binary, verifiable DONE WHEN criteria after clarification interview`
- Source: [@itsolelehmann on X](https://x.com/itsolelehmann/status/2054649363234992401)
- Source type: `x-post`
- Evidence: Write me a /goal prompt. Ask me what I'm trying to do first, then keep asking follow-up questions until you can describe 'done' in specific, measurable terms.
- Evidence summary: Write me a /goal prompt. Ask me what I'm trying to do first, then keep asking follow-up questions until you can describe 'done' in specific, measurable terms.; source: @itsolelehmann on X; type: x-post; verification: generated goal contains clear, binary, verifiable DONE WHEN criteria after clarification interview

```text
/goal
GOAL:
Complete Interview-Driven Goal Prompt Generator for a coding-agent workflow repository: Use a meta prompt to interview the user with clarifying questions until 'done' can be expressed in specific, measurable, verifiable terms, then output a high-quality structured /goal prompt.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `generated goal contains clear, binary, verifiable DONE WHEN criteria after clarification interview`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Use a meta prompt to interview the user with clarifying questions until 'done' can be expressed in specific, measurable, verifiable terms, then output a high-quality structured /goal prompt.
- The verification command or evidence path succeeds: `generated goal contains clear, binary, verifiable DONE WHEN criteria after clarification interview`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `generated goal contains clear, binary, verifiable DONE WHEN criteria after clarification interview` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
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
- Evidence summary: billing page shows an empty state; source: Reddit r/ClaudeAI; type: public-forum; verification: npm test

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
- Evidence summary: continually improve my RAG based document chat; source: Reddit r/ClaudeCode; type: public-forum; verification: Playwright tests and metric review

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
- Evidence summary: console error when you click the button; source: HN Playwright Skill; type: public-forum; verification: Playwright interaction

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
- Evidence summary: fetch ten reviews; source: HN You Should Write An Agent; type: public-forum; verification: JSON files written

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
- Evidence summary: isolated git worktree and opens a PR; source: HN Astro; type: public-forum; verification: PR output

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
- Evidence summary: replace a sidebar with chat history; source: VideoHighlight YouTube summary; type: video-summary; verification: tests and build

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
- Evidence summary: 2D combat game Rift Salvage; source: Pogovet YouTube summary; type: video-summary; verification: browser verification

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
- Evidence summary: find and fix the flaky auth tests; source: jthack/claude-goal; type: tool-readme; verification: python3 -m pytest tests

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
- Evidence summary: Migrate this project from Pydantic v1 to v2; source: jailbreak-autoresearch docs; type: tool-readme; verification: pytest -q

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
- Evidence summary: review the plan ImplementationPlan.md; source: openai/codex issue 21176; type: github-issue; verification: fresh plan review has no new gaps

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
- Evidence summary: Build the Meta0 LifeOS ontology boundary artifact; source: openai/codex discussion 21764; type: github-discussion; verification: get_goal and thread_goals evidence

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
- Evidence summary: Complete a long-running task until final verification passes; source: openai/codex issue 22049; type: github-issue; verification: final verification

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
- Evidence summary: /goal improve benchmark coverage; source: openai/codex PR 21860; type: github-pr; verification: cargo test -p codex-tui goal_slash_command -- --nocapture

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
- Evidence summary: completion audits before calling update_goal; source: openai/codex PR 22045; type: github-pr; verification: focused coverage and evals

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
- Evidence summary: uses stale permission context; source: openai/codex issue 22090; type: github-issue; verification: cargo check focused crates

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
- Evidence summary: prints the exact /goal command; source: tolibear/goalbuddy; type: tool-readme; verification: board, receipts, and verify files

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
- Evidence summary: /goal Fix bugs #1-#6; source: anthropics/claude-code issue 58348; type: github-issue; verification: no unsatisfied skill loop

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
- Evidence summary: Goal: <several lines of overarching aim>; source: anthropics/claude-code issue 58192; type: github-issue; verification: stop hook evaluates cleanly

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
- Evidence summary: print hello, Ralph loop; source: NousResearch/hermes-agent PR 18262; type: github-pr; verification: live judge round-trip

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
- Evidence summary: /home/ubuntu/ml-resumo.md; source: NousResearch/hermes-agent issue 18421; type: github-issue; verification: find and read_file evidence

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
- Evidence summary: /goal Fix failing tests; source: NousResearch/hermes-agent issue 22617; type: github-issue; verification: queue promotion evidence

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

<a id="openhands-api-integration-tests"></a>
### API Integration Tests

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add end-to-end tests for product API endpoints with success and error cases.
- Verification: `jest integration tests with test database`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Add integration tests for the /api/products endpoints
- Evidence summary: Add integration tests for the /api/products endpoints; source: OpenHands tutorial library; type: official-agent-task; verification: jest integration tests with test database

```text
/goal
GOAL:
Complete API Integration Tests for a backend API service: Add end-to-end tests for product API endpoints with success and error cases.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `jest integration tests with test database`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Add end-to-end tests for product API endpoints with success and error cases.
- The verification command or evidence path succeeds: `jest integration tests with test database`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `jest integration tests with test database` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-dev-database-migration"></a>
### Dev Database Migration Proof

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Write a migration, run it against the dev database, and confirm the schema matches.
- Verification: `migration applied to dev DB and schema comparison`
- Source: [Claude Code prompt library](https://code.claude.com/docs/en/prompt-library)
- Source type: `official-agent-task`
- Evidence: write the migration, run it against the dev database, and confirm the schema matches
- Evidence summary: write the migration, run it against the dev database, and confirm the schema matches; source: Claude Code prompt library; type: official-agent-task; verification: migration applied to dev DB and schema comparison

```text
/goal
GOAL:
Complete Dev Database Migration Proof for a data-backed backend service: Write a migration, run it against the dev database, and confirm the schema matches.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `migration applied to dev DB and schema comparison`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Write a migration, run it against the dev database, and confirm the schema matches.
- The verification command or evidence path succeeds: `migration applied to dev DB and schema comparison`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `migration applied to dev DB and schema comparison` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-accessibility-html-wcag"></a>
### HTML WCAG Instruction Audit

- Category: `accessibility`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Audit HTML changes against WCAG guidance and prove the Lighthouse accessibility audit passes.
- Verification: `Lighthouse accessibility audit`
- Source: [GitHub Copilot accessibility auditor](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/accessibility-auditor)
- Source type: `official-agent-task`
- Evidence: generate accessible, inclusive HTML that follows WCAG guidelines
- Evidence summary: generate accessible, inclusive HTML that follows WCAG guidelines; source: GitHub Copilot accessibility auditor; type: official-agent-task; verification: Lighthouse accessibility audit

```text
/goal
GOAL:
Complete HTML WCAG Instruction Audit for a web or mobile interface: Audit HTML changes against WCAG guidance and prove the Lighthouse accessibility audit passes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect interactive elements, semantics, focus management, and a11y reports.
- Establish a baseline by running or locating evidence for: `Lighthouse accessibility audit`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not hide controls from assistive technology to silence audit findings.
- Keep keyboard, focus, semantic, and visual checks together.

DONE WHEN:
- The implementation or documentation directly satisfies: Audit HTML changes against WCAG guidance and prove the Lighthouse accessibility audit passes.
- The verification command or evidence path succeeds: `Lighthouse accessibility audit`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `Lighthouse accessibility audit` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-reference-layout-design"></a>
### Reference Layout Match

- Category: `design`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Build a settings page that follows an existing profile page layout instead of inventing a new pattern.
- Verification: `visual comparison against profile page`
- Source: [Claude Code prompt library](https://code.claude.com/docs/en/prompt-library)
- Source type: `official-agent-task`
- Evidence: add a settings page that follows the same layout as the profile page
- Evidence summary: add a settings page that follows the same layout as the profile page; source: Claude Code prompt library; type: official-agent-task; verification: visual comparison against profile page

```text
/goal
GOAL:
Complete Reference Layout Match for a product UI codebase: Build a settings page that follows an existing profile page layout instead of inventing a new pattern.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `visual comparison against profile page`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Build a settings page that follows an existing profile page layout instead of inventing a new pattern.
- The verification command or evidence path succeeds: `visual comparison against profile page`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `visual comparison against profile page` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-mobile-agent-task-handoff"></a>
### Mobile Agent Task Handoff

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Prepare and track a coding-agent task started from GitHub Mobile with review-ready evidence.
- Verification: `GitHub Mobile agent task creates a PR`
- Source: [GitHub Copilot coding agent docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/assign-copilot-to-an-issue)
- Source type: `official-agent-task`
- Evidence: assign an issue to Copilot on GitHub Mobile
- Evidence summary: assign an issue to Copilot on GitHub Mobile; source: GitHub Copilot coding agent docs; type: official-agent-task; verification: GitHub Mobile agent task creates a PR

```text
/goal
GOAL:
Complete Mobile Agent Task Handoff for a mobile or responsive application: Prepare and track a coding-agent task started from GitHub Mobile with review-ready evidence.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `GitHub Mobile agent task creates a PR`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Prepare and track a coding-agent task started from GitHub Mobile with review-ready evidence.
- The verification command or evidence path succeeds: `GitHub Mobile agent task creates a PR`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `GitHub Mobile agent task creates a PR` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-agent-trace-evals"></a>
### Trace-Graded Agent Regression

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Create trace-based evals that catch workflow regressions across tool calls and handoffs.
- Verification: `agent eval report with graded traces`
- Source: [OpenAI agent evals docs](https://platform.openai.com/docs/guides/agent-evals)
- Source type: `official-workflow`
- Evidence: trace grading functionality
- Evidence summary: trace grading functionality; source: OpenAI agent evals docs; type: official-workflow; verification: agent eval report with graded traces

```text
/goal
GOAL:
Complete Trace-Graded Agent Regression for an AI evaluation project: Create trace-based evals that catch workflow regressions across tool calls and handoffs.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `agent eval report with graded traces`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Create trace-based evals that catch workflow regressions across tool calls and handoffs.
- The verification command or evidence path succeeds: `agent eval report with graded traces`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `agent eval report with graded traces` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-agent-tracing-observability"></a>
### Agent Trace Observability

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Instrument agent runs so LLM generations, tool calls, handoffs, guardrails, and custom events are traceable.
- Verification: `trace dashboard shows spans for one agent run`
- Source: [OpenAI Agents SDK tracing docs](https://openai.github.io/openai-agents-python/tracing/)
- Source type: `official-workflow`
- Evidence: built-in tracing collects LLM generations, tool calls, handoffs, guardrails
- Evidence summary: built-in tracing collects LLM generations, tool calls, handoffs, guardrails; source: OpenAI Agents SDK tracing docs; type: official-workflow; verification: trace dashboard shows spans for one agent run

```text
/goal
GOAL:
Complete Agent Trace Observability for an AI application runtime: Instrument agent runs so LLM generations, tool calls, handoffs, guardrails, and custom events are traceable.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `trace dashboard shows spans for one agent run`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Instrument agent runs so LLM generations, tool calls, handoffs, guardrails, and custom events are traceable.
- The verification command or evidence path succeeds: `trace dashboard shows spans for one agent run`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `trace dashboard shows spans for one agent run` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-csv-processing-report"></a>
### CSV Processing Report

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Create a data processing script that validates CSV input and generates an analysis report.
- Verification: `script output report and validation checks`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Process CSV data and generate a report
- Evidence summary: Process CSV data and generate a report; source: OpenHands tutorial library; type: official-agent-task; verification: script output report and validation checks

```text
/goal
GOAL:
Complete CSV Processing Report for a data pipeline project: Create a data processing script that validates CSV input and generates an analysis report.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `script output report and validation checks`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Create a data processing script that validates CSV input and generates an analysis report.
- The verification command or evidence path succeeds: `script output report and validation checks`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `script output report and validation checks` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-remote-agent-server-smoke"></a>
### Remote Agent Server Smoke

- Category: `devops-runtime`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Deploy an isolated remote agent server and prove event streaming, workspace access, and command execution work.
- Verification: `remote server smoke run and websocket event evidence`
- Source: [OpenHands remote agent server docs](https://docs.openhands.dev/sdk/guides/agent-server/overview)
- Source type: `official-workflow`
- Evidence: Remote Agent Servers package the Software Agent SDK into containers
- Evidence summary: Remote Agent Servers package the Software Agent SDK into containers; source: OpenHands remote agent server docs; type: official-workflow; verification: remote server smoke run and websocket event evidence

```text
/goal
GOAL:
Complete Remote Agent Server Smoke for a deployed service: Deploy an isolated remote agent server and prove event streaming, workspace access, and command execution work.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Dockerfiles, deployment manifests, runtime config, and health checks.
- Establish a baseline by running or locating evidence for: `remote server smoke run and websocket event evidence`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not deploy to production automatically; stop with a verified plan if live credentials are required.
- Keep rollback and health-check evidence attached to the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Deploy an isolated remote agent server and prove event streaming, workspace access, and command execution work.
- The verification command or evidence path succeeds: `remote server smoke run and websocket event evidence`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `remote server smoke run and websocket event evidence` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-tool-guardrails-appsec"></a>
### Tool Guardrails For AppSec

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Add tool guardrails around high-risk agent tool calls and stop unsafe input or output before execution continues.
- Verification: `guardrail tests trigger on unsafe tool input/output`
- Source: [OpenAI Agents SDK guardrails docs](https://openai.github.io/openai-agents-python/guardrails/)
- Source type: `official-workflow`
- Evidence: tool guardrails run on every custom function-tool invocation
- Evidence summary: tool guardrails run on every custom function-tool invocation; source: OpenAI Agents SDK guardrails docs; type: official-workflow; verification: guardrail tests trigger on unsafe tool input/output

```text
/goal
GOAL:
Complete Tool Guardrails For AppSec for an application with security-sensitive code paths: Add tool guardrails around high-risk agent tool calls and stop unsafe input or output before execution continues.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `guardrail tests trigger on unsafe tool input/output`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Add tool guardrails around high-risk agent tool calls and stop unsafe input or output before execution continues.
- The verification command or evidence path succeeds: `guardrail tests trigger on unsafe tool input/output`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `guardrail tests trigger on unsafe tool input/output` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-slow-query-optimization"></a>
### Slow Query Optimization Report

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Analyze slow query logs, explain bottlenecks, recommend indexes or rewrites, and produce prioritized SQL changes.
- Verification: `EXPLAIN plans and reports/query_optimization.md`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Analyze our slow query log and identify optimization opportunities
- Evidence summary: Analyze our slow query log and identify optimization opportunities; source: OpenHands tutorial library; type: official-agent-task; verification: EXPLAIN plans and reports/query_optimization.md

```text
/goal
GOAL:
Complete Slow Query Optimization Report for a data-backed backend service: Analyze slow query logs, explain bottlenecks, recommend indexes or rewrites, and produce prioritized SQL changes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `EXPLAIN plans and reports/query_optimization.md`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Analyze slow query logs, explain bottlenecks, recommend indexes or rewrites, and produce prioritized SQL changes.
- The verification command or evidence path succeeds: `EXPLAIN plans and reports/query_optimization.md`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `EXPLAIN plans and reports/query_optimization.md` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-rate-limited-web-scraper"></a>
### Rate-Limited Web Scraper

- Category: `data-eng`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Build a scraper that extracts product data across paginated pages while respecting rate limits and logging progress.
- Verification: `scraper smoke run and products.json schema check`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Create a web scraper to extract product information
- Evidence summary: Create a web scraper to extract product information; source: OpenHands tutorial library; type: official-agent-task; verification: scraper smoke run and products.json schema check

```text
/goal
GOAL:
Complete Rate-Limited Web Scraper for a data pipeline project: Build a scraper that extracts product data across paginated pages while respecting rate limits and logging progress.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect ETL jobs, schemas, source contracts, transformations, and data quality tests.
- Establish a baseline by running or locating evidence for: `scraper smoke run and products.json schema check`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Build a scraper that extracts product data across paginated pages while respecting rate limits and logging progress.
- The verification command or evidence path succeeds: `scraper smoke run and products.json schema check`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `scraper smoke run and products.json schema check` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-security-pr-review"></a>
### Security PR Review

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Review a pull request for input validation, authentication, injection, XSS, and secrets risks with file-level fixes.
- Verification: `Markdown PR review with severity, affected lines, and suggested fixes`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Review this pull request for security issues
- Evidence summary: Review this pull request for security issues; source: OpenHands tutorial library; type: official-agent-task; verification: Markdown PR review with severity, affected lines, and suggested fixes

```text
/goal
GOAL:
Complete Security PR Review for an application with security-sensitive code paths: Review a pull request for input validation, authentication, injection, XSS, and secrets risks with file-level fixes.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `Markdown PR review with severity, affected lines, and suggested fixes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Review a pull request for input validation, authentication, injection, XSS, and secrets risks with file-level fixes.
- The verification command or evidence path succeeds: `Markdown PR review with severity, affected lines, and suggested fixes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `Markdown PR review with severity, affected lines, and suggested fixes` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-orderservice-performance-review"></a>
### Order Service Performance Review

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Inspect service code for N+1 queries, missing indexes, inefficient loops, missing caches, and unnecessary fetching.
- Verification: `performance review report with impact and optimized code paths`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Review the OrderService class for performance issues
- Evidence summary: Review the OrderService class for performance issues; source: OpenHands tutorial library; type: official-agent-task; verification: performance review report with impact and optimized code paths

```text
/goal
GOAL:
Complete Order Service Performance Review for a web application with measurable performance goals: Inspect service code for N+1 queries, missing indexes, inefficient loops, missing caches, and unnecessary fetching.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `performance review report with impact and optimized code paths`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Inspect service code for N+1 queries, missing indexes, inefficient loops, missing caches, and unnecessary fetching.
- The verification command or evidence path succeeds: `performance review report with impact and optimized code paths`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `performance review report with impact and optimized code paths` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-checkout-crash-regression"></a>
### Checkout Crash Regression Fix

- Category: `investigation`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Reproduce a checkout crash from a stack trace, identify the root cause, fix it, and add a regression test.
- Verification: `crash reproduction test and checkout regression test`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Fix the crash in the checkout process
- Evidence summary: Fix the crash in the checkout process; source: OpenHands tutorial library; type: official-agent-task; verification: crash reproduction test and checkout regression test

```text
/goal
GOAL:
Complete Checkout Crash Regression Fix for an investigation task: Reproduce a checkout crash from a stack trace, identify the root cause, fix it, and add a regression test.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect logs, traces, reproduction notes, source paths, and the final report.
- Establish a baseline by running or locating evidence for: `crash reproduction test and checkout regression test`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Separate observed evidence from hypotheses.
- Do not patch production code until the root cause is reproduced or strongly evidenced.

DONE WHEN:
- The implementation or documentation directly satisfies: Reproduce a checkout crash from a stack trace, identify the root cause, fix it, and add a regression test.
- The verification command or evidence path succeeds: `crash reproduction test and checkout regression test`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `crash reproduction test and checkout regression test` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-node-memory-leak-fix"></a>
### Node Memory Leak Fix

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Investigate a growing-memory Node.js process, isolate the leak source, fix it, and add monitoring for recurrence.
- Verification: `heap comparison or load test plus monitoring evidence`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Investigate and fix the memory leak in our Node.js application
- Evidence summary: Investigate and fix the memory leak in our Node.js application; source: OpenHands tutorial library; type: official-agent-task; verification: heap comparison or load test plus monitoring evidence

```text
/goal
GOAL:
Complete Node Memory Leak Fix for a web application with measurable performance goals: Investigate a growing-memory Node.js process, isolate the leak source, fix it, and add monitoring for recurrence.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `heap comparison or load test plus monitoring evidence`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Investigate a growing-memory Node.js process, isolate the leak source, fix it, and add monitoring for recurrence.
- The verification command or evidence path succeeds: `heap comparison or load test plus monitoring evidence`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `heap comparison or load test plus monitoring evidence` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-user-preferences-api"></a>
### User Preferences API

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add GET, PUT, and PATCH endpoints for user preferences with validation, service logic, OpenAPI docs, and tests.
- Verification: `unit and integration tests plus OpenAPI endpoint documentation`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Add a user preferences API endpoint
- Evidence summary: Add a user preferences API endpoint; source: OpenHands tutorial library; type: official-agent-task; verification: unit and integration tests plus OpenAPI endpoint documentation

```text
/goal
GOAL:
Complete User Preferences API for a backend API service: Add GET, PUT, and PATCH endpoints for user preferences with validation, service logic, OpenAPI docs, and tests.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `unit and integration tests plus OpenAPI endpoint documentation`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Add GET, PUT, and PATCH endpoints for user preferences with validation, service logic, OpenAPI docs, and tests.
- The verification command or evidence path succeeds: `unit and integration tests plus OpenAPI endpoint documentation`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `unit and integration tests plus OpenAPI endpoint documentation` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openhands-feature-flag-system"></a>
### Feature Flag System

- Category: `product`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Implement boolean, percentage, and user-based feature flags with service logic, API middleware, a React hook, docs, and tests.
- Verification: `feature flag service, hook, middleware, and rollout tests`
- Source: [OpenHands tutorial library](https://docs.openhands.dev/openhands/usage/get-started/tutorials)
- Source type: `official-agent-task`
- Evidence: Implement a feature flag system for our application
- Evidence summary: Implement a feature flag system for our application; source: OpenHands tutorial library; type: official-agent-task; verification: feature flag service, hook, middleware, and rollout tests

```text
/goal
GOAL:
Complete Feature Flag System for a product planning and implementation repo: Implement boolean, percentage, and user-based feature flags with service logic, API middleware, a React hook, docs, and tests.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `feature flag service, hook, middleware, and rollout tests`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Implement boolean, percentage, and user-based feature flags with service logic, API middleware, a React hook, docs, and tests.
- The verification command or evidence path succeeds: `feature flag service, hook, middleware, and rollout tests`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `feature flag service, hook, middleware, and rollout tests` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-build-log-diagnosis"></a>
### Build Log Failure Diagnosis

- Category: `investigation`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use a provided build log to explain why the build fails and identify the smallest verified fix path.
- Verification: `failing build command reproduced or build.log root-cause report`
- Source: [Claude Code prompt library](https://code.claude.com/docs/en/prompt-library)
- Source type: `official-agent-task`
- Evidence: why is the build failing? @build.log
- Evidence summary: why is the build failing? @build.log; source: Claude Code prompt library; type: official-agent-task; verification: failing build command reproduced or build.log root-cause report

```text
/goal
GOAL:
Complete Build Log Failure Diagnosis for an investigation task: Use a provided build log to explain why the build fails and identify the smallest verified fix path.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect logs, traces, reproduction notes, source paths, and the final report.
- Establish a baseline by running or locating evidence for: `failing build command reproduced or build.log root-cause report`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Separate observed evidence from hypotheses.
- Do not patch production code until the root cause is reproduced or strongly evidenced.

DONE WHEN:
- The implementation or documentation directly satisfies: Use a provided build log to explain why the build fails and identify the smallest verified fix path.
- The verification command or evidence path succeeds: `failing build command reproduced or build.log root-cause report`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `failing build command reproduced or build.log root-cause report` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-payment-retry-diagram"></a>
### Payment Retry Logic Diagram

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Explain payment retry behavior as a browsable HTML page with a diagram for developer or support review.
- Verification: `HTML page opens locally and diagram matches the retry code path`
- Source: [Claude Code prompt library](https://code.claude.com/docs/en/prompt-library)
- Source type: `official-agent-task`
- Evidence: explain how the payment retry logic works as an HTML page with a diagram
- Evidence summary: explain how the payment retry logic works as an HTML page with a diagram; source: Claude Code prompt library; type: official-agent-task; verification: HTML page opens locally and diagram matches the retry code path

```text
/goal
GOAL:
Complete Payment Retry Logic Diagram for a developer-facing documentation site or repository: Explain payment retry behavior as a browsable HTML page with a diagram for developer or support review.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `HTML page opens locally and diagram matches the retry code path`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Explain payment retry behavior as a browsable HTML page with a diagram for developer or support review.
- The verification command or evidence path succeeds: `HTML page opens locally and diagram matches the retry code path`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `HTML page opens locally and diagram matches the retry code path` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="deadreckon-coherence-closure"></a>
### User-Facing Coherence Closure

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Finish a coherence pass so CLI help, docs, JSON/plain output, colors, prompts, flags, and next-action grammar stay aligned.
- Verification: `snapshot tests, JSON leak tests, TUI render tests, docs examples, cargo workspace checks`
- Source: [deadreckon goal corpus](https://github.com/gregce/deadreckon/blob/main/docs/goals/2026-05-17-1403-deadreckon-coherence-closure-goal.md)
- Source type: `third-party-project`
- Evidence: same words, colors, streams, flags, prompts, and next-action grammar
- Evidence summary: same words, colors, streams, flags, prompts, and next-action grammar; source: deadreckon goal corpus; type: third-party-project; verification: snapshot tests, JSON leak tests, TUI render tests, docs examples, cargo workspace checks

```text
/goal
GOAL:
Complete User-Facing Coherence Closure for a coding-agent workflow repository: Finish a coherence pass so CLI help, docs, JSON/plain output, colors, prompts, flags, and next-action grammar stay aligned.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `snapshot tests, JSON leak tests, TUI render tests, docs examples, cargo workspace checks`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Finish a coherence pass so CLI help, docs, JSON/plain output, colors, prompts, flags, and next-action grammar stay aligned.
- The verification command or evidence path succeeds: `snapshot tests, JSON leak tests, TUI render tests, docs examples, cargo workspace checks`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `snapshot tests, JSON leak tests, TUI render tests, docs examples, cargo workspace checks` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="deadreckon-semantic-merge-repair"></a>
### DAG-Aware Semantic Merge Repair

- Category: `orchestration`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Make orchestration merge failures repairable by using plan DAG context, conflict bundles, planner-mediated repair, and bounded retry.
- Verification: `DAG smoke, repair smoke, refusal smoke, cargo build/test/clippy/fmt`
- Source: [deadreckon goal corpus](https://github.com/gregce/deadreckon/blob/main/docs/goals/2026-05-16-1122-deadreckon-semantic-merge-repair-goal.md)
- Source type: `third-party-project`
- Evidence: Land DAG-aware merge plus automatic planner-mediated repair for true conflicts
- Evidence summary: Land DAG-aware merge plus automatic planner-mediated repair for true conflicts; source: deadreckon goal corpus; type: third-party-project; verification: DAG smoke, repair smoke, refusal smoke, cargo build/test/clippy/fmt

```text
/goal
GOAL:
Complete DAG-Aware Semantic Merge Repair for an agent orchestration task: Make orchestration merge failures repairable by using plan DAG context, conflict bundles, planner-mediated repair, and bounded retry.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect plans, worktrees, subtask ownership, PRs, and coordination notes.
- Establish a baseline by running or locating evidence for: `DAG smoke, repair smoke, refusal smoke, cargo build/test/clippy/fmt`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Keep subtask ownership explicit and avoid overlapping write scopes.
- Do not merge or deploy automatically unless the goal explicitly allows it.

DONE WHEN:
- The implementation or documentation directly satisfies: Make orchestration merge failures repairable by using plan DAG context, conflict bundles, planner-mediated repair, and bounded retry.
- The verification command or evidence path succeeds: `DAG smoke, repair smoke, refusal smoke, cargo build/test/clippy/fmt`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `DAG smoke, repair smoke, refusal smoke, cargo build/test/clippy/fmt` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="deadreckon-orchestration-eventbus"></a>
### Plan EventBus Live UX

- Category: `orchestration`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Unify plan, fork, merge, and orchestrate around shared builders and a live plan event stream.
- Verification: `orchestrate, coherence, attach_plan, plan_event_bus, plan_event, fmt, targeted clippy`
- Source: [deadreckon goal corpus](https://github.com/gregce/deadreckon/blob/main/docs/goals/2026-05-18-2226-deadreckon-orchestration-eventbus-goal.md)
- Source type: `third-party-project`
- Evidence: move plan attach onto a shared plan event stream
- Evidence summary: move plan attach onto a shared plan event stream; source: deadreckon goal corpus; type: third-party-project; verification: orchestrate, coherence, attach_plan, plan_event_bus, plan_event, fmt, targeted clippy

```text
/goal
GOAL:
Complete Plan EventBus Live UX for an agent orchestration task: Unify plan, fork, merge, and orchestrate around shared builders and a live plan event stream.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect plans, worktrees, subtask ownership, PRs, and coordination notes.
- Establish a baseline by running or locating evidence for: `orchestrate, coherence, attach_plan, plan_event_bus, plan_event, fmt, targeted clippy`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Keep subtask ownership explicit and avoid overlapping write scopes.
- Do not merge or deploy automatically unless the goal explicitly allows it.

DONE WHEN:
- The implementation or documentation directly satisfies: Unify plan, fork, merge, and orchestrate around shared builders and a live plan event stream.
- The verification command or evidence path succeeds: `orchestrate, coherence, attach_plan, plan_event_bus, plan_event, fmt, targeted clippy`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `orchestrate, coherence, attach_plan, plan_event_bus, plan_event, fmt, targeted clippy` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="deadreckon-implementation-notes-ledger"></a>
### Implementation Notes Decision Ledger

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Keep live implementation notes and the final run decisions document aligned around decisions, deviations, tradeoffs, and open questions.
- Verification: `self-documenting run tests, doc kind tests, implementation notes freshness smoke, fmt, targeted clippy`
- Source: [deadreckon goal corpus](https://github.com/gregce/deadreckon/blob/main/docs/goals/2026-05-18-2336-deadreckon-implementation-notes-goal.md)
- Source type: `third-party-project`
- Evidence: canonical implementation decision ledger
- Evidence summary: canonical implementation decision ledger; source: deadreckon goal corpus; type: third-party-project; verification: self-documenting run tests, doc kind tests, implementation notes freshness smoke, fmt, targeted clippy

```text
/goal
GOAL:
Complete Implementation Notes Decision Ledger for a developer-facing documentation site or repository: Keep live implementation notes and the final run decisions document aligned around decisions, deviations, tradeoffs, and open questions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `self-documenting run tests, doc kind tests, implementation notes freshness smoke, fmt, targeted clippy`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Keep live implementation notes and the final run decisions document aligned around decisions, deviations, tradeoffs, and open questions.
- The verification command or evidence path succeeds: `self-documenting run tests, doc kind tests, implementation notes freshness smoke, fmt, targeted clippy`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `self-documenting run tests, doc kind tests, implementation notes freshness smoke, fmt, targeted clippy` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-agent-daily-priority-loop"></a>
### Daily Goal Priority Loop

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Use a persistent goal profile to compute daily priorities, execute them, log progress, and refresh status across sessions.
- Verification: `/goal:next priorities, /goal:log entry, /goal:status dashboard, progress-tracker.md updated`
- Source: [Goal Agent README](https://github.com/ishaquehassan/goal-agent)
- Source type: `tool-readme`
- Evidence: Your daily loop: /goal:next to see what to do, execute it, /goal:log to record it
- Evidence summary: Your daily loop: /goal:next to see what to do, execute it, /goal:log to record it; source: Goal Agent README; type: tool-readme; verification: /goal:next priorities, /goal:log entry, /goal:status dashboard, progress-tracker.md updated

```text
/goal
GOAL:
Complete Daily Goal Priority Loop for a goal-management workflow: Use a persistent goal profile to compute daily priorities, execute them, log progress, and refresh status across sessions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `/goal:next priorities, /goal:log entry, /goal:status dashboard, progress-tracker.md updated`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Use a persistent goal profile to compute daily priorities, execute them, log progress, and refresh status across sessions.
- The verification command or evidence path succeeds: `/goal:next priorities, /goal:log entry, /goal:status dashboard, progress-tracker.md updated`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `/goal:next priorities, /goal:log entry, /goal:status dashboard, progress-tracker.md updated` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-agent-profile-optimization"></a>
### Goal-Aligned Profile Optimization

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Audit and update professional profiles against a stated goal while recording the resulting progress and gaps.
- Verification: `/goal:optimize platform output plus updated goal memory files`
- Source: [Goal Agent README](https://github.com/ishaquehassan/goal-agent)
- Source type: `tool-readme`
- Evidence: /goal:optimize [platform]
- Evidence summary: /goal:optimize [platform]; source: Goal Agent README; type: tool-readme; verification: /goal:optimize platform output plus updated goal memory files

```text
/goal
GOAL:
Complete Goal-Aligned Profile Optimization for a goal-management workflow: Audit and update professional profiles against a stated goal while recording the resulting progress and gaps.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `/goal:optimize platform output plus updated goal memory files`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Audit and update professional profiles against a stated goal while recording the resulting progress and gaps.
- The verification command or evidence path succeeds: `/goal:optimize platform output plus updated goal memory files`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `/goal:optimize platform output plus updated goal memory files` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-agent-content-engagement-loop"></a>
### Content And Audience Engagement Loop

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Generate goal-aligned content, publish or promote it, engage with target audience posts, and log the session outcome.
- Verification: `/goal:write output, /goal:engage actions, /goal:log entry, content-calendar.md updated`
- Source: [Goal Agent README](https://github.com/ishaquehassan/goal-agent)
- Source type: `tool-readme`
- Evidence: /goal:write article
- Evidence summary: /goal:write article; source: Goal Agent README; type: tool-readme; verification: /goal:write output, /goal:engage actions, /goal:log entry, content-calendar.md updated

```text
/goal
GOAL:
Complete Content And Audience Engagement Loop for a goal-management workflow: Generate goal-aligned content, publish or promote it, engage with target audience posts, and log the session outcome.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `/goal:write output, /goal:engage actions, /goal:log entry, content-calendar.md updated`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Generate goal-aligned content, publish or promote it, engage with target audience posts, and log the session outcome.
- The verification command or evidence path succeeds: `/goal:write output, /goal:engage actions, /goal:log entry, content-calendar.md updated`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `/goal:write output, /goal:engage actions, /goal:log entry, content-calendar.md updated` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-flow-sparc-payment-plan"></a>
### SPARC Payment Processing Plan

- Category: `backend-api`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Plan and implement payment processing through SPARC phases with requirements, pseudocode, architecture, TDD refinement, and integration.
- Verification: `acceptance criteria, API contracts, unit and integration tests, coverage target, integration validation`
- Source: [claude-flow code-goal-planner skill](https://github.com/ruvnet/claude-flow/blob/main/.agents/skills/agent-code-goal-planner/SKILL.md)
- Source type: `tool-readme`
- Evidence: goal: implement_payment_processing_with_sparc
- Evidence summary: goal: implement_payment_processing_with_sparc; source: claude-flow code-goal-planner skill; type: tool-readme; verification: acceptance criteria, API contracts, unit and integration tests, coverage target, integration validation

```text
/goal
GOAL:
Complete SPARC Payment Processing Plan for a backend API service: Plan and implement payment processing through SPARC phases with requirements, pseudocode, architecture, TDD refinement, and integration.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect API routes, OpenAPI specs, handlers, middleware, and API tests.
- Establish a baseline by running or locating evidence for: `acceptance criteria, API contracts, unit and integration tests, coverage target, integration validation`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Plan and implement payment processing through SPARC phases with requirements, pseudocode, architecture, TDD refinement, and integration.
- The verification command or evidence path succeeds: `acceptance criteria, API contracts, unit and integration tests, coverage target, integration validation`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `acceptance criteria, API contracts, unit and integration tests, coverage target, integration validation` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-flow-api-latency-goap"></a>
### GOAP API Latency Reduction

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Reduce API latency by profiling current performance, optimizing database queries, adding caching, and improving code paths.
- Verification: `p50 latency, p99 latency, throughput, database explain, before/after performance evidence`
- Source: [claude-flow code-goal-planner skill](https://github.com/ruvnet/claude-flow/blob/main/.agents/skills/agent-code-goal-planner/SKILL.md)
- Source type: `tool-readme`
- Evidence: goal: reduce_api_latency_50_percent
- Evidence summary: goal: reduce_api_latency_50_percent; source: claude-flow code-goal-planner skill; type: tool-readme; verification: p50 latency, p99 latency, throughput, database explain, before/after performance evidence

```text
/goal
GOAL:
Complete GOAP API Latency Reduction for a web application with measurable performance goals: Reduce API latency by profiling current performance, optimizing database queries, adding caching, and improving code paths.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `p50 latency, p99 latency, throughput, database explain, before/after performance evidence`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Reduce API latency by profiling current performance, optimizing database queries, adding caching, and improving code paths.
- The verification command or evidence path succeeds: `p50 latency, p99 latency, throughput, database explain, before/after performance evidence`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `p50 latency, p99 latency, throughput, database explain, before/after performance evidence` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-flow-coverage-goap"></a>
### GOAP Coverage Target Plan

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Raise test coverage with an explicit test pyramid across unit, integration, and end-to-end coverage targets.
- Verification: `coverage report reaches target and critical paths have passing unit, integration, and e2e tests`
- Source: [claude-flow code-goal-planner skill](https://github.com/ruvnet/claude-flow/blob/main/.agents/skills/agent-code-goal-planner/SKILL.md)
- Source type: `tool-readme`
- Evidence: goal: achieve_80_percent_coverage
- Evidence summary: goal: achieve_80_percent_coverage; source: claude-flow code-goal-planner skill; type: tool-readme; verification: coverage report reaches target and critical paths have passing unit, integration, and e2e tests

```text
/goal
GOAL:
Complete GOAP Coverage Target Plan for a project with failing or missing verification gates: Raise test coverage with an explicit test pyramid across unit, integration, and end-to-end coverage targets.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `coverage report reaches target and critical paths have passing unit, integration, and e2e tests`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Raise test coverage with an explicit test pyramid across unit, integration, and end-to-end coverage targets.
- The verification command or evidence path succeeds: `coverage report reaches target and critical paths have passing unit, integration, and e2e tests`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `coverage report reaches target and critical paths have passing unit, integration, and e2e tests` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="claude-recipes-okr-development"></a>
### OKR Development From Vague Priorities

- Category: `product`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Turn vague strategic priorities into measurable OKRs with objectives, key results, alignment, scoring, guardrails, and a communication summary.
- Verification: `3-5 objectives, 2-4 measurable key results each, alignment notes, scoring guide, red flags, one-page summary`
- Source: [claude-code-recipes](https://github.com/sgharlow/claude-code-recipes/blob/main/recipes/Recipe-017-OKR-Goal-Setting.md)
- Source type: `third-party-tutorial`
- Evidence: PRIMARY PROMPT: OKR Development
- Evidence summary: PRIMARY PROMPT: OKR Development; source: claude-code-recipes; type: third-party-tutorial; verification: 3-5 objectives, 2-4 measurable key results each, alignment notes, scoring guide, red flags, one-page summary

```text
/goal
GOAL:
Complete OKR Development From Vague Priorities for a product planning and implementation repo: Turn vague strategic priorities into measurable OKRs with objectives, key results, alignment, scoring, guardrails, and a communication summary.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect PRDs, analytics events, permission models, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `3-5 objectives, 2-4 measurable key results each, alignment notes, scoring guide, red flags, one-page summary`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not implement new product scope unless it is in the stated acceptance criteria.
- Separate product decisions from engineering assumptions.

DONE WHEN:
- The implementation or documentation directly satisfies: Turn vague strategic priorities into measurable OKRs with objectives, key results, alignment, scoring, guardrails, and a communication summary.
- The verification command or evidence path succeeds: `3-5 objectives, 2-4 measurable key results each, alignment notes, scoring guide, red flags, one-page summary`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `3-5 objectives, 2-4 measurable key results each, alignment notes, scoring guide, red flags, one-page summary` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="clinical-research-ai-safety-boundary"></a>
### Clinical Research AI Safety Boundary

- Category: `research`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Review clinical research AI work with evidence-first boundaries so agents do not invent medical sources, expose private data, or turn research notes into patient-specific advice.
- Verification: `manual review checklist for source facts, uncertainty, safety note, inspected files, and human-review needs`
- Source: [Clinical AI Agent Skills README](https://github.com/2023Anita/clinical-ai-agent-skills)
- Source type: `tool-readme`
- Evidence: Evidence Before Confidence
- Evidence summary: Evidence Before Confidence; source: Clinical AI Agent Skills README; type: tool-readme; verification: manual review checklist for source facts, uncertainty, safety note, inspected files, and human-review needs

```text
/goal
GOAL:
Complete Clinical Research AI Safety Boundary for a research task: Review clinical research AI work with evidence-first boundaries so agents do not invent medical sources, expose private data, or turn research notes into patient-specific advice.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect source lists, citation notes, evidence files, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `manual review checklist for source facts, uncertainty, safety note, inspected files, and human-review needs`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not present unsourced claims as facts.
- Keep direct quotes short and attach a public URL for every external claim.

DONE WHEN:
- The implementation or documentation directly satisfies: Review clinical research AI work with evidence-first boundaries so agents do not invent medical sources, expose private data, or turn research notes into patient-specific advice.
- The verification command or evidence path succeeds: `manual review checklist for source facts, uncertainty, safety note, inspected files, and human-review needs`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `manual review checklist for source facts, uncertainty, safety note, inspected files, and human-review needs` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-code-migration-checkpoints"></a>
### Code Migration Checkpoints

- Category: `migration`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Inventory legacy assumptions, map them to a target stack, and execute the migration through validated checkpoints.
- Verification: `legacy assumption inventory, checkpoint migration plan, lint, type-check, focused tests after each milestone, rollback notes`
- Source: [OpenAI Codex code migrations use case](https://developers.openai.com/codex/use-cases/code-migrations)
- Source type: `official-agent-task`
- Evidence: Migrate this codebase from [legacy stack or system] to [target stack or system]
- Evidence summary: Migrate this codebase from [legacy stack or system] to [target stack or system]; source: OpenAI Codex code migrations use case; type: official-agent-task; verification: legacy assumption inventory, checkpoint migration plan, lint, type-check, focused tests after each milestone, rollback notes

```text
/goal
GOAL:
Complete Code Migration Checkpoints for a migration project: Inventory legacy assumptions, map them to a target stack, and execute the migration through validated checkpoints.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect legacy code, target implementation, compatibility tests, visual snapshots, and migration notes.
- Establish a baseline by running or locating evidence for: `legacy assumption inventory, checkpoint migration plan, lint, type-check, focused tests after each milestone, rollback notes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Preserve existing user-visible behavior unless the goal explicitly names a behavior change.
- Keep compatibility evidence for the old and new paths until the migration is verified.

DONE WHEN:
- The implementation or documentation directly satisfies: Inventory legacy assumptions, map them to a target stack, and execute the migration through validated checkpoints.
- The verification command or evidence path succeeds: `legacy assumption inventory, checkpoint migration plan, lint, type-check, focused tests after each milestone, rollback notes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `legacy assumption inventory, checkpoint migration plan, lint, type-check, focused tests after each milestone, rollback notes` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-difficult-task-eval-loop"></a>
### Difficult Task Eval Loop

- Category: `prompt-optimization`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Run a difficult task as an eval-driven improvement loop with one focused change, rerun scores, and direct artifact inspection each iteration.
- Verification: `score command found, per-iteration score log, artifact inspection, overall score and LLM average above target`
- Source: [OpenAI Codex difficult problems use case](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems)
- Source type: `official-agent-task`
- Evidence: run it as an eval-driven improvement loop
- Evidence summary: run it as an eval-driven improvement loop; source: OpenAI Codex difficult problems use case; type: official-agent-task; verification: score command found, per-iteration score log, artifact inspection, overall score and LLM average above target

```text
/goal
GOAL:
Complete Difficult Task Eval Loop for an eval-backed prompt project: Run a difficult task as an eval-driven improvement loop with one focused change, rerun scores, and direct artifact inspection each iteration.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompt files, eval cases, scoring reports, regressions, and failure examples.
- Establish a baseline by running or locating evidence for: `score command found, per-iteration score log, artifact inspection, overall score and LLM average above target`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete, weaken, or cherry-pick eval cases to improve the score.
- Report representative failures as well as the final score.

DONE WHEN:
- The implementation or documentation directly satisfies: Run a difficult task as an eval-driven improvement loop with one focused change, rerun scores, and direct artifact inspection each iteration.
- The verification command or evidence path succeeds: `score command found, per-iteration score log, artifact inspection, overall score and LLM average above target`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `score command found, per-iteration score log, artifact inspection, overall score and LLM average above target` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-promptfoo-eval-suite"></a>
### Promptfoo Eval Suite

- Category: `ai-evals`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Add a runnable Promptfoo eval suite for an AI application before changing production prompts or model behavior.
- Verification: `target adapter, seed cases, assertions, files, env requirements, local eval command, passing and failing cases`
- Source: [OpenAI Codex AI app evals use case](https://developers.openai.com/codex/use-cases/ai-app-evals)
- Source type: `official-agent-task`
- Evidence: Use $promptfoo-evals to add a Promptfoo eval suite
- Evidence summary: Use $promptfoo-evals to add a Promptfoo eval suite; source: OpenAI Codex AI app evals use case; type: official-agent-task; verification: target adapter, seed cases, assertions, files, env requirements, local eval command, passing and failing cases

```text
/goal
GOAL:
Complete Promptfoo Eval Suite for an AI evaluation project: Add a runnable Promptfoo eval suite for an AI application before changing production prompts or model behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect eval datasets, rubrics, model outputs, judge code, and regression reports.
- Establish a baseline by running or locating evidence for: `target adapter, seed cases, assertions, files, env requirements, local eval command, passing and failing cases`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not tune prompts against hidden labels or delete failing eval cases to improve the score.
- Keep before/after eval evidence and representative failures.

DONE WHEN:
- The implementation or documentation directly satisfies: Add a runnable Promptfoo eval suite for an AI application before changing production prompts or model behavior.
- The verification command or evidence path succeeds: `target adapter, seed cases, assertions, files, env requirements, local eval command, passing and failing cases`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `target adapter, seed cases, assertions, files, env requirements, local eval command, passing and failing cases` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-expo-react-native-app"></a>
### Expo React Native App Slice

- Category: `mobile`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Build a working React Native app slice with Expo Router conventions, Expo-compatible packages, and native-feeling UI states.
- Verification: `working app slice, run command, verification path with Expo Go, device, simulator, dev client, or EAS`
- Source: [OpenAI Codex Expo app use case](https://developers.openai.com/codex/use-cases/react-native-expo-apps)
- Source type: `official-agent-task`
- Evidence: Use the Expo plugin to build a React Native app with Expo
- Evidence summary: Use the Expo plugin to build a React Native app with Expo; source: OpenAI Codex Expo app use case; type: official-agent-task; verification: working app slice, run command, verification path with Expo Go, device, simulator, dev client, or EAS

```text
/goal
GOAL:
Complete Expo React Native App Slice for a mobile or responsive application: Build a working React Native app slice with Expo Router conventions, Expo-compatible packages, and native-feeling UI states.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect mobile routes, forms, gestures, device matrix, and viewport tests.
- Establish a baseline by running or locating evidence for: `working app slice, run command, verification path with Expo Go, device, simulator, dev client, or EAS`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not optimize only desktop behavior.
- Keep touch targets, safe areas, and keyboard overlap in scope.

DONE WHEN:
- The implementation or documentation directly satisfies: Build a working React Native app slice with Expo Router conventions, Expo-compatible packages, and native-feeling UI states.
- The verification command or evidence path succeeds: `working app slice, run command, verification path with Expo Go, device, simulator, dev client, or EAS`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `working app slice, run command, verification path with Expo Go, device, simulator, dev client, or EAS` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-agent-friendly-cli-skill"></a>
### Agent-Friendly CLI And Skill

- Category: `cli`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Create a composable CLI and companion skill so future agent tasks can search, read, download, or draft against a recurring source safely.
- Verification: `proposed command surface, command installed on PATH, help output, setup check, safe discovery command, exact read command, companion skill`
- Source: [OpenAI Codex agent-friendly CLI use case](https://developers.openai.com/codex/use-cases/agent-friendly-clis)
- Source type: `official-agent-task`
- Evidence: Use $cli-creator to create a CLI you can use, and use $skill-creator to create the companion skill
- Evidence summary: Use $cli-creator to create a CLI you can use, and use $skill-creator to create the companion skill; source: OpenAI Codex agent-friendly CLI use case; type: official-agent-task; verification: proposed command surface, command installed on PATH, help output, setup check, safe discovery command, exact read command, companion skill

```text
/goal
GOAL:
Complete Agent-Friendly CLI And Skill for a command-line tool: Create a composable CLI and companion skill so future agent tasks can search, read, download, or draft against a recurring source safely.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect CLI entrypoints, argument parsing, filesystem behavior, dry-run mode, and fixtures.
- Establish a baseline by running or locating evidence for: `proposed command surface, command installed on PATH, help output, setup check, safe discovery command, exact read command, companion skill`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not perform destructive filesystem operations without a dry-run or explicit confirmation.
- Keep command output deterministic enough for tests.

DONE WHEN:
- The implementation or documentation directly satisfies: Create a composable CLI and companion skill so future agent tasks can search, read, download, or draft against a recurring source safely.
- The verification command or evidence path succeeds: `proposed command surface, command installed on PATH, help output, setup check, safe discovery command, exact read command, companion skill`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `proposed command surface, command installed on PATH, help output, setup check, safe discovery command, exact read command, companion skill` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="openai-define-goal-quality-bar"></a>
### Define Goal Quality Bar

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Turn a fuzzy intention into a concrete measurable goal with evidence, scope boundaries, and honest stop conditions before creating it.
- Verification: `objective names outcome, evidence, success threshold, scope boundaries, and stop condition before create_goal`
- Source: [OpenAI define-goal skill](https://github.com/openai/skills/blob/main/skills/.curated/define-goal/SKILL.md)
- Source type: `tool-readme`
- Evidence: Before create_goal, the objective should answer
- Evidence summary: Before create_goal, the objective should answer; source: OpenAI define-goal skill; type: tool-readme; verification: objective names outcome, evidence, success threshold, scope boundaries, and stop condition before create_goal

```text
/goal
GOAL:
Complete Define Goal Quality Bar for a goal-management workflow: Turn a fuzzy intention into a concrete measurable goal with evidence, scope boundaries, and honest stop conditions before creating it.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `objective names outcome, evidence, success threshold, scope boundaries, and stop condition before create_goal`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Turn a fuzzy intention into a concrete measurable goal with evidence, scope boundaries, and honest stop conditions before creating it.
- The verification command or evidence path succeeds: `objective names outcome, evidence, success threshold, scope boundaries, and stop condition before create_goal`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `objective names outcome, evidence, success threshold, scope boundaries, and stop condition before create_goal` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="x-three-questions-goal-framework"></a>
### Three Questions Goal Framework

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Write higher quality goals by explicitly answering three core questions: what needs to be done, how success will be measured, and what is off-limits.
- Verification: `goal explicitly addresses what to do, how it will be verified as done, and clear boundaries`
- Source: [@aashatwt on X](https://x.com/aashatwt/status/2054810622131585515)
- Source type: `x-post`
- Evidence: A good /goal prompt answers these three questions: What needs to be done? How will we know it's done? What's off-limits?
- Evidence summary: A good /goal prompt answers these three questions: What needs to be done? How will we know it's done? What's off-limits?; source: @aashatwt on X; type: x-post; verification: goal explicitly addresses what to do, how it will be verified as done, and clear boundaries

```text
/goal
GOAL:
Complete Three Questions Goal Framework for a coding-agent workflow repository: Write higher quality goals by explicitly answering three core questions: what needs to be done, how success will be measured, and what is off-limits.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `goal explicitly addresses what to do, how it will be verified as done, and clear boundaries`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Write higher quality goals by explicitly answering three core questions: what needs to be done, how success will be measured, and what is off-limits.
- The verification command or evidence path succeeds: `goal explicitly addresses what to do, how it will be verified as done, and clear boundaries`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `goal explicitly addresses what to do, how it will be verified as done, and clear boundaries` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="x-explicit-stop-rules-goal-loops"></a>
### Explicit Stop Rules for Goal Loops

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Prevent infinite loops, cost overruns, and unsafe behavior in autonomous /goal executions by defining clear, explicit stop conditions and escalation rules.
- Verification: `goal prompt contains a dedicated STOP RULES section with concrete halt conditions (turns, cost, repeated failures, risk triggers)`
- Source: [@_avichawla on X](https://x.com/_avichawla/status/2055930732930122158)
- Source type: `x-post`
- Evidence: Without strong stop rules a slightly wrong condition loops forever
- Evidence summary: Without strong stop rules a slightly wrong condition loops forever; source: @_avichawla on X; type: x-post; verification: goal prompt contains a dedicated STOP RULES section with concrete halt conditions (turns, cost, repeated failures, risk triggers)

```text
/goal
GOAL:
Complete Explicit Stop Rules for Goal Loops for a coding-agent workflow repository: Prevent infinite loops, cost overruns, and unsafe behavior in autonomous /goal executions by defining clear, explicit stop conditions and escalation rules.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `goal prompt contains a dedicated STOP RULES section with concrete halt conditions (turns, cost, repeated failures, risk triggers)`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Prevent infinite loops, cost overruns, and unsafe behavior in autonomous /goal executions by defining clear, explicit stop conditions and escalation rules.
- The verification command or evidence path succeeds: `goal prompt contains a dedicated STOP RULES section with concrete halt conditions (turns, cost, repeated failures, risk triggers)`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `goal prompt contains a dedicated STOP RULES section with concrete halt conditions (turns, cost, repeated failures, risk triggers)` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="x-dual-model-evaluator-goal-loop"></a>
### Dual-Model Evaluator Loop for Goals

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Run long /goal sessions reliably and cost-effectively by using a strong worker model for execution paired with a cheap fast evaluator model (typically Haiku) that periodically judges progress against the goal criteria and decides whether to continue or stop.
- Verification: `goal execution uses distinct worker and evaluator models with the evaluator checking against explicit DONE WHEN conditions`
- Source: [@_avichawla on X](https://x.com/_avichawla/status/2055930732930122158)
- Source type: `x-post`
- Evidence: worker model + cheap Haiku evaluator loop for goal completion decisions
- Evidence summary: worker model + cheap Haiku evaluator loop for goal completion decisions; source: @_avichawla on X; type: x-post; verification: goal execution uses distinct worker and evaluator models with the evaluator checking against explicit DONE WHEN conditions

```text
/goal
GOAL:
Complete Dual-Model Evaluator Loop for Goals for a coding-agent workflow repository: Run long /goal sessions reliably and cost-effectively by using a strong worker model for execution paired with a cheap fast evaluator model (typically Haiku) that periodically judges progress against the goal criteria and decides whether to continue or stop.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `goal execution uses distinct worker and evaluator models with the evaluator checking against explicit DONE WHEN conditions`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Run long /goal sessions reliably and cost-effectively by using a strong worker model for execution paired with a cheap fast evaluator model (typically Haiku) that periodically judges progress against the goal criteria and decides whether to continue or stop.
- The verification command or evidence path succeeds: `goal execution uses distinct worker and evaluator models with the evaluator checking against explicit DONE WHEN conditions`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `goal execution uses distinct worker and evaluator models with the evaluator checking against explicit DONE WHEN conditions` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="x-claude-md-goal-workflow"></a>
### CLAUDE.md + Goal Workflow

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Combine a persistent project-level CLAUDE.md (or AGENTS.md) file containing rules, standards, and context with /goal commands so long-running autonomous agent work stays aligned with repository-specific constraints and learned lessons.
- Verification: `CLAUDE.md is present and referenced; /goal executions respect the documented rules and patterns`
- Source: [@nateherk on X](https://x.com/nateherk/status/2059377638896971985)
- Source type: `x-post`
- Evidence: CLAUDE.md as persistent context paired with /goal for autonomous execution
- Evidence summary: CLAUDE.md as persistent context paired with /goal for autonomous execution; source: @nateherk on X; type: x-post; verification: CLAUDE.md is present and referenced; /goal executions respect the documented rules and patterns

```text
/goal
GOAL:
Complete CLAUDE.md + Goal Workflow for a coding-agent workflow repository: Combine a persistent project-level CLAUDE.md (or AGENTS.md) file containing rules, standards, and context with /goal commands so long-running autonomous agent work stays aligned with repository-specific constraints and learned lessons.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `CLAUDE.md is present and referenced; /goal executions respect the documented rules and patterns`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Combine a persistent project-level CLAUDE.md (or AGENTS.md) file containing rules, standards, and context with /goal commands so long-running autonomous agent work stays aligned with repository-specific constraints and learned lessons.
- The verification command or evidence path succeeds: `CLAUDE.md is present and referenced; /goal executions respect the documented rules and patterns`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `CLAUDE.md is present and referenced; /goal executions respect the documented rules and patterns` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="x-goal-ledger"></a>
### Goal Ledger for Long-Running Runs

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Maintain a live, browser-viewable HTML progress ledger during extended /goal executions to provide visibility, persistent memory, decision logging, and self-reflection, reducing drift in long autonomous sessions.
- Verification: `an updatable HTML ledger file is created and actively maintained by the agent throughout the goal run`
- Source: [@KingBootoshi on X](https://x.com/KingBootoshi/status/2056876283204866293)
- Source type: `x-post`
- Evidence: single-file HTML progress tracker and ledger for /goal runs
- Evidence summary: single-file HTML progress tracker and ledger for /goal runs; source: @KingBootoshi on X; type: x-post; verification: an updatable HTML ledger file is created and actively maintained by the agent throughout the goal run

```text
/goal
GOAL:
Complete Goal Ledger for Long-Running Runs for a coding-agent workflow repository: Maintain a live, browser-viewable HTML progress ledger during extended /goal executions to provide visibility, persistent memory, decision logging, and self-reflection, reducing drift in long autonomous sessions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `an updatable HTML ledger file is created and actively maintained by the agent throughout the goal run`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Maintain a live, browser-viewable HTML progress ledger during extended /goal executions to provide visibility, persistent memory, decision logging, and self-reflection, reducing drift in long autonomous sessions.
- The verification command or evidence path succeeds: `an updatable HTML ledger file is created and actively maintained by the agent throughout the goal run`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `an updatable HTML ledger file is created and actively maintained by the agent throughout the goal run` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-builder-audit-friendly-template"></a>
### Audit-Friendly Goal Template

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Rewrite a vague /goal into a mappable contract with objective, scope, constraints, done-when evidence, stop rules, and token budget.
- Verification: `audit-friendliness score, rendered /goal, Objective/Scope/Constraints/Done when/Stop if sections`
- Source: [goal-prompt-builder README](https://github.com/win4r/goal-prompt-builder)
- Source type: `tool-readme`
- Evidence: 5-section golden template (Objective / Scope / Constraints / Done when / Stop if)
- Evidence summary: 5-section golden template (Objective / Scope / Constraints / Done when / Stop if); source: goal-prompt-builder README; type: tool-readme; verification: audit-friendliness score, rendered /goal, Objective/Scope/Constraints/Done when/Stop if sections

```text
/goal
GOAL:
Complete Audit-Friendly Goal Template for a goal-management workflow: Rewrite a vague /goal into a mappable contract with objective, scope, constraints, done-when evidence, stop rules, and token budget.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `audit-friendliness score, rendered /goal, Objective/Scope/Constraints/Done when/Stop if sections`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Rewrite a vague /goal into a mappable contract with objective, scope, constraints, done-when evidence, stop rules, and token budget.
- The verification command or evidence path succeeds: `audit-friendliness score, rendered /goal, Objective/Scope/Constraints/Done when/Stop if sections`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `audit-friendliness score, rendered /goal, Objective/Scope/Constraints/Done when/Stop if sections` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-builder-openspec-rerank-provider"></a>
### OpenSpec Rerank Provider Goal

- Category: `ai-ops`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Implement an OpenSpec feature change exactly as specified, adding a new rerank provider with contract tests, integration coverage, docs, and changelog evidence.
- Verification: `tasks checked off with file evidence, SHALL tests, GIVEN/WHEN/THEN integration tests, npx tsc --noEmit, npm test, README and CHANGELOG updates`
- Source: [goal-prompt-builder README](https://github.com/win4r/goal-prompt-builder)
- Source type: `tool-readme`
- Evidence: Implement openspec/changes/add-cohere-rerank/ exactly as specified
- Evidence summary: Implement openspec/changes/add-cohere-rerank/ exactly as specified; source: goal-prompt-builder README; type: tool-readme; verification: tasks checked off with file evidence, SHALL tests, GIVEN/WHEN/THEN integration tests, npx tsc --noEmit, npm test, README and CHANGELOG updates

```text
/goal
GOAL:
Complete OpenSpec Rerank Provider Goal for an AI application runtime: Implement an OpenSpec feature change exactly as specified, adding a new rerank provider with contract tests, integration coverage, docs, and changelog evidence.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompts, retrieval code, routing policies, tracing, and cost logs.
- Establish a baseline by running or locating evidence for: `tasks checked off with file evidence, SHALL tests, GIVEN/WHEN/THEN integration tests, npx tsc --noEmit, npm test, README and CHANGELOG updates`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not silently fall back to a lower-quality model for user-visible critical paths.
- Keep request IDs, cost evidence, and schema validation errors visible.

DONE WHEN:
- The implementation or documentation directly satisfies: Implement an OpenSpec feature change exactly as specified, adding a new rerank provider with contract tests, integration coverage, docs, and changelog evidence.
- The verification command or evidence path succeeds: `tasks checked off with file evidence, SHALL tests, GIVEN/WHEN/THEN integration tests, npx tsc --noEmit, npm test, README and CHANGELOG updates`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `tasks checked off with file evidence, SHALL tests, GIVEN/WHEN/THEN integration tests, npx tsc --noEmit, npm test, README and CHANGELOG updates` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-well-scoped-agent-issue"></a>
### Well-Scoped Agent Issue

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Turn a backlog item into a coding-agent-ready issue with a clear problem statement, acceptance criteria, file directions, and test expectations.
- Verification: `issue includes problem description, acceptance criteria, file hints, expected tests, and review notes`
- Source: [GitHub Copilot cloud agent best practices](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results)
- Source type: `official-agent-task`
- Evidence: clear description of the problem to be solved or the work required
- Evidence summary: clear description of the problem to be solved or the work required; source: GitHub Copilot cloud agent best practices; type: official-agent-task; verification: issue includes problem description, acceptance criteria, file hints, expected tests, and review notes

```text
/goal
GOAL:
Complete Well-Scoped Agent Issue for a coding-agent workflow repository: Turn a backlog item into a coding-agent-ready issue with a clear problem statement, acceptance criteria, file directions, and test expectations.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `issue includes problem description, acceptance criteria, file hints, expected tests, and review notes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Turn a backlog item into a coding-agent-ready issue with a clear problem statement, acceptance criteria, file directions, and test expectations.
- The verification command or evidence path succeeds: `issue includes problem description, acceptance criteria, file hints, expected tests, and review notes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `issue includes problem description, acceptance criteria, file hints, expected tests, and review notes` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-plan-before-pr"></a>
### Research And Plan Before PR

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Have an agent research the repository, create an implementation plan, and iterate on a branch before deciding whether to open a pull request.
- Verification: `implementation plan, reviewed diff, branch commits, explicit PR-open decision, and remaining-risk notes`
- Source: [GitHub Copilot cloud agent best practices](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results)
- Source type: `official-agent-task`
- Evidence: research a repository, create an implementation plan, and make iterative code changes on a branch first
- Evidence summary: research a repository, create an implementation plan, and make iterative code changes on a branch first; source: GitHub Copilot cloud agent best practices; type: official-agent-task; verification: implementation plan, reviewed diff, branch commits, explicit PR-open decision, and remaining-risk notes

```text
/goal
GOAL:
Complete Research And Plan Before PR for a coding-agent workflow repository: Have an agent research the repository, create an implementation plan, and iterate on a branch before deciding whether to open a pull request.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `implementation plan, reviewed diff, branch commits, explicit PR-open decision, and remaining-risk notes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Have an agent research the repository, create an implementation plan, and iterate on a branch before deciding whether to open a pull request.
- The verification command or evidence path succeeds: `implementation plan, reviewed diff, branch commits, explicit PR-open decision, and remaining-risk notes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `implementation plan, reviewed diff, branch commits, explicit PR-open decision, and remaining-risk notes` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-repository-instructions"></a>
### Repository Agent Instructions

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Add repository-level agent instructions that document project structure, build/test/validate commands, coding standards, and documentation expectations.
- Verification: `.github/copilot-instructions.md or AGENTS.md present, commands verified, repository structure covered, standards documented`
- Source: [GitHub Copilot cloud agent best practices](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results)
- Source type: `official-agent-task`
- Evidence: guide Copilot on how to understand your project and how to build, test and validate its changes
- Evidence summary: guide Copilot on how to understand your project and how to build, test and validate its changes; source: GitHub Copilot cloud agent best practices; type: official-agent-task; verification: .github/copilot-instructions.md or AGENTS.md present, commands verified, repository structure covered, standards documented

```text
/goal
GOAL:
Complete Repository Agent Instructions for a developer-facing documentation site or repository: Add repository-level agent instructions that document project structure, build/test/validate commands, coding standards, and documentation expectations.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `.github/copilot-instructions.md or AGENTS.md present, commands verified, repository structure covered, standards documented`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Add repository-level agent instructions that document project structure, build/test/validate commands, coding standards, and documentation expectations.
- The verification command or evidence path succeeds: `.github/copilot-instructions.md or AGENTS.md present, commands verified, repository structure covered, standards documented`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `.github/copilot-instructions.md or AGENTS.md present, commands verified, repository structure covered, standards documented` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-playwright-instructions"></a>
### Playwright Test Instructions

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Create path-specific Playwright instructions that enforce stable locators, isolated tests, explicit assertions, cross-browser coverage, and CI behavior.
- Verification: `.github/instructions/playwright-tests.instructions.md with glob front matter, sample e2e test, and passing Playwright command`
- Source: [GitHub Copilot cloud agent best practices](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results)
- Source type: `official-agent-task`
- Evidence: Use stable locators
- Evidence summary: Use stable locators; source: GitHub Copilot cloud agent best practices; type: official-agent-task; verification: .github/instructions/playwright-tests.instructions.md with glob front matter, sample e2e test, and passing Playwright command

```text
/goal
GOAL:
Complete Playwright Test Instructions for a project with failing or missing verification gates: Create path-specific Playwright instructions that enforce stable locators, isolated tests, explicit assertions, cross-browser coverage, and CI behavior.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `.github/instructions/playwright-tests.instructions.md with glob front matter, sample e2e test, and passing Playwright command`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Create path-specific Playwright instructions that enforce stable locators, isolated tests, explicit assertions, cross-browser coverage, and CI behavior.
- The verification command or evidence path succeeds: `.github/instructions/playwright-tests.instructions.md with glob front matter, sample e2e test, and passing Playwright command`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `.github/instructions/playwright-tests.instructions.md with glob front matter, sample e2e test, and passing Playwright command` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-autopilot-ci-repair"></a>
### Bounded Autopilot CI Repair

- Category: `devops-ci`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Run a bounded autonomous CI repair after plan acceptance, with explicit continuation limits, permissions, validation commands, and blocker reporting.
- Verification: `accepted plan, max continuation limit, CI command outputs, final green run or blocker report`
- Source: [GitHub Copilot CLI autopilot docs](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot)
- Source type: `official-workflow`
- Evidence: Accept plan and build on autopilot
- Evidence summary: Accept plan and build on autopilot; source: GitHub Copilot CLI autopilot docs; type: official-workflow; verification: accepted plan, max continuation limit, CI command outputs, final green run or blocker report

```text
/goal
GOAL:
Complete Bounded Autopilot CI Repair for a repository with CI/CD automation: Run a bounded autonomous CI repair after plan acceptance, with explicit continuation limits, permissions, validation commands, and blocker reporting.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect workflow files, build scripts, package manifests, and recent CI logs.
- Establish a baseline by running or locating evidence for: `accepted plan, max continuation limit, CI command outputs, final green run or blocker report`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken tests, remove required checks, or bypass branch protection.
- Keep workflow permissions as narrow as the task allows.

DONE WHEN:
- The implementation or documentation directly satisfies: Run a bounded autonomous CI repair after plan acceptance, with explicit continuation limits, permissions, validation commands, and blocker reporting.
- The verification command or evidence path succeeds: `accepted plan, max continuation limit, CI command outputs, final green run or blocker report`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `accepted plan, max continuation limit, CI command outputs, final green run or blocker report` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-fleet-parallel-test-suite"></a>
### Fleet Parallel Test Suite

- Category: `orchestration`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Break a large test expansion into independent subtasks that subagents can execute in parallel while the orchestrator manages dependencies and final integration.
- Verification: `task split, subagent ownership, dependency notes, merged test output, and conflict audit`
- Source: [GitHub Copilot CLI fleet docs](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet)
- Source type: `official-workflow`
- Evidence: creating a suite of tests for a new feature, are well suited to parallelization
- Evidence summary: creating a suite of tests for a new feature, are well suited to parallelization; source: GitHub Copilot CLI fleet docs; type: official-workflow; verification: task split, subagent ownership, dependency notes, merged test output, and conflict audit

```text
/goal
GOAL:
Complete Fleet Parallel Test Suite for an agent orchestration task: Break a large test expansion into independent subtasks that subagents can execute in parallel while the orchestrator manages dependencies and final integration.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect plans, worktrees, subtask ownership, PRs, and coordination notes.
- Establish a baseline by running or locating evidence for: `task split, subagent ownership, dependency notes, merged test output, and conflict audit`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Keep subtask ownership explicit and avoid overlapping write scopes.
- Do not merge or deploy automatically unless the goal explicitly allows it.

DONE WHEN:
- The implementation or documentation directly satisfies: Break a large test expansion into independent subtasks that subagents can execute in parallel while the orchestrator manages dependencies and final integration.
- The verification command or evidence path succeeds: `task split, subagent ownership, dependency notes, merged test output, and conflict audit`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `task split, subagent ownership, dependency notes, merged test output, and conflict audit` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-research-architecture-report"></a>
### Cited Architecture Research Report

- Category: `research`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Produce a saved, cited Markdown architecture report after inspecting the local codebase, relevant repositories, and web sources.
- Verification: `Markdown report path or gist URL, citations, assumptions, confidence assessment, and architecture summary`
- Source: [GitHub Copilot CLI research docs](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/research)
- Source type: `official-agent-task`
- Evidence: /research What is the architecture of this codebase?
- Evidence summary: /research What is the architecture of this codebase?; source: GitHub Copilot CLI research docs; type: official-agent-task; verification: Markdown report path or gist URL, citations, assumptions, confidence assessment, and architecture summary

```text
/goal
GOAL:
Complete Cited Architecture Research Report for a research task: Produce a saved, cited Markdown architecture report after inspecting the local codebase, relevant repositories, and web sources.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect source lists, citation notes, evidence files, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `Markdown report path or gist URL, citations, assumptions, confidence assessment, and architecture summary`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not present unsourced claims as facts.
- Keep direct quotes short and attach a public URL for every external claim.

DONE WHEN:
- The implementation or documentation directly satisfies: Produce a saved, cited Markdown architecture report after inspecting the local codebase, relevant repositories, and web sources.
- The verification command or evidence path succeeds: `Markdown report path or gist URL, citations, assumptions, confidence assessment, and architecture summary`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `Markdown report path or gist URL, citations, assumptions, confidence assessment, and architecture summary` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-cli-agentic-review"></a>
### Terminal Agentic Code Review

- Category: `qa`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Review a diff from the terminal with a scoped prompt, path, or file pattern, inspect suggested commands, and apply or reject findings before commit.
- Verification: `/review output, inspected diff evidence, applied fixes or explicit rejects, and final clean diff summary`
- Source: [GitHub Copilot CLI code review docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/agentic-code-review)
- Source type: `official-agent-task`
- Evidence: /review slash command to have Copilot analyze code changes
- Evidence summary: /review slash command to have Copilot analyze code changes; source: GitHub Copilot CLI code review docs; type: official-agent-task; verification: /review output, inspected diff evidence, applied fixes or explicit rejects, and final clean diff summary

```text
/goal
GOAL:
Complete Terminal Agentic Code Review for a product with automated and manual QA coverage: Review a diff from the terminal with a scoped prompt, path, or file pattern, inspect suggested commands, and apply or reject findings before commit.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, fixtures, bug templates, and release checklists.
- Establish a baseline by running or locating evidence for: `/review output, inspected diff evidence, applied fixes or explicit rejects, and final clean diff summary`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete or weaken failing tests to make the suite pass.
- Reproduce failures before changing production code.

DONE WHEN:
- The implementation or documentation directly satisfies: Review a diff from the terminal with a scoped prompt, path, or file pattern, inspect suggested commands, and apply or reject findings before commit.
- The verification command or evidence path succeeds: `/review output, inspected diff evidence, applied fixes or explicit rejects, and final clean diff summary`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `/review output, inspected diff evidence, applied fixes or explicit rejects, and final clean diff summary` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-cross-cutting-logging"></a>
### Centralize Cross-Cutting Logging

- Category: `refactor`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Centralize scattered logging, validation, security, or error-handling behavior without changing the core business behavior of the services.
- Verification: `central middleware/decorator/config module, duplicate removal, focused regression tests, and unchanged public behavior`
- Source: [GitHub Copilot Cookbook](https://docs.github.com/en/copilot/tutorials/copilot-cookbook/refactor-code/handle-cross-cutting)
- Source type: `official-agent-task`
- Evidence: logging, security, data validation, and error handling
- Evidence summary: logging, security, data validation, and error handling; source: GitHub Copilot Cookbook; type: official-agent-task; verification: central middleware/decorator/config module, duplicate removal, focused regression tests, and unchanged public behavior

```text
/goal
GOAL:
Complete Centralize Cross-Cutting Logging for a refactoring task: Centralize scattered logging, validation, security, or error-handling behavior without changing the core business behavior of the services.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect the target module, call sites, public API, tests, and compatibility notes.
- Establish a baseline by running or locating evidence for: `central middleware/decorator/config module, duplicate removal, focused regression tests, and unchanged public behavior`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not change public APIs, data formats, or user-visible behavior unless the goal requires it.
- Keep behavior characterization tests before large internal changes.

DONE WHEN:
- The implementation or documentation directly satisfies: Centralize scattered logging, validation, security, or error-handling behavior without changing the core business behavior of the services.
- The verification command or evidence path succeeds: `central middleware/decorator/config module, duplicate removal, focused regression tests, and unchanged public behavior`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `central middleware/decorator/config module, duplicate removal, focused regression tests, and unchanged public behavior` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-deadlock-minimization"></a>
### Deadlock-Minimizing Transaction Rewrite

- Category: `backend-data`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Rewrite transaction ordering and locking to reduce deadlock risk without adverse performance or data-integrity regressions.
- Verification: `consistent lock order, shorter transaction evidence, database tests, and before/after query or lock notes`
- Source: [GitHub Copilot Cookbook](https://docs.github.com/en/copilot/tutorials/copilot-cookbook/refactor-code/fix-database-deadlocks)
- Source type: `official-agent-task`
- Evidence: reduce the chance of deadlock to a minimum while not adversely affecting performance
- Evidence summary: reduce the chance of deadlock to a minimum while not adversely affecting performance; source: GitHub Copilot Cookbook; type: official-agent-task; verification: consistent lock order, shorter transaction evidence, database tests, and before/after query or lock notes

```text
/goal
GOAL:
Complete Deadlock-Minimizing Transaction Rewrite for a data-backed backend service: Rewrite transaction ordering and locking to reduce deadlock risk without adverse performance or data-integrity regressions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect schema files, migrations, models, repositories, and data tests.
- Establish a baseline by running or locating evidence for: `consistent lock order, shorter transaction evidence, database tests, and before/after query or lock notes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not destroy or rewrite data without a dry-run, rollback, and row-count/checksum evidence.
- Do not hide database errors behind warnings or silent fallbacks.

DONE WHEN:
- The implementation or documentation directly satisfies: Rewrite transaction ordering and locking to reduce deadlock risk without adverse performance or data-integrity regressions.
- The verification command or evidence path succeeds: `consistent lock order, shorter transaction evidence, database tests, and before/after query or lock notes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `consistent lock order, shorter transaction evidence, database tests, and before/after query or lock notes` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-xss-innerhtml-fix"></a>
### Unsafe innerHTML XSS Fix

- Category: `security-appsec`
- Difficulty: `advanced`
- Origin: `source-backed`
- Intent: Find and fix XSS caused by unsafe innerHTML rendering while preserving the user-visible text and adding a regression guard.
- Verification: `unsafe sink replaced, security or DOM test added, no sanitizer bypass, and UI output preserved`
- Source: [GitHub Copilot Cookbook](https://docs.github.com/en/copilot/tutorials/copilot-cookbook/analyze-security/find-vulnerabilities)
- Source type: `official-agent-task`
- Evidence: innerHTML = `Showing results for "${name}"`
- Evidence summary: innerHTML = `Showing results for "${name}"`; source: GitHub Copilot Cookbook; type: official-agent-task; verification: unsafe sink replaced, security or DOM test added, no sanitizer bypass, and UI output preserved

```text
/goal
GOAL:
Complete Unsafe innerHTML XSS Fix for an application with security-sensitive code paths: Find and fix XSS caused by unsafe innerHTML rendering while preserving the user-visible text and adding a regression guard.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect auth, input handling, rendering, upload, and boundary tests.
- Establish a baseline by running or locating evidence for: `unsafe sink replaced, security or DOM test added, no sanitizer bypass, and UI output preserved`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not bypass authentication, authorization, validation, or audit checks.
- Do not use eval, unsafe HTML injection, shell string concatenation, or string-built SQL.

DONE WHEN:
- The implementation or documentation directly satisfies: Find and fix XSS caused by unsafe innerHTML rendering while preserving the user-visible text and adding a regression guard.
- The verification command or evidence path succeeds: `unsafe sink replaced, security or DOM test added, no sanitizer bypass, and UI output preserved`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `unsafe sink replaced, security or DOM test added, no sanitizer bypass, and UI output preserved` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-doc-code-sync"></a>
### Documentation Matches Code

- Category: `docs`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Update stale API or function documentation so parameters, behavior, examples, thrown errors, and links match the current implementation.
- Verification: `documentation diff matches code signature, examples compile or type-check, docs lint passes`
- Source: [GitHub Copilot Cookbook](https://docs.github.com/en/copilot/tutorials/copilot-cookbook/document-code/sync-documentation)
- Source type: `official-agent-task`
- Evidence: Update the existing documentation for the getByCategoryName function to reflect the current implementation
- Evidence summary: Update the existing documentation for the getByCategoryName function to reflect the current implementation; source: GitHub Copilot Cookbook; type: official-agent-task; verification: documentation diff matches code signature, examples compile or type-check, docs lint passes

```text
/goal
GOAL:
Complete Documentation Matches Code for a developer-facing documentation site or repository: Update stale API or function documentation so parameters, behavior, examples, thrown errors, and links match the current implementation.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect README, docs, examples, runbooks, and lint configuration.
- Establish a baseline by running or locating evidence for: `documentation diff matches code signature, examples compile or type-check, docs lint passes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not invent APIs, flags, commands, or product behavior.
- Mark unverified commands clearly instead of presenting guesses as facts.

DONE WHEN:
- The implementation or documentation directly satisfies: Update stale API or function documentation so parameters, behavior, examples, thrown errors, and links match the current implementation.
- The verification command or evidence path succeeds: `documentation diff matches code signature, examples compile or type-check, docs lint passes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `documentation diff matches code signature, examples compile or type-check, docs lint passes` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="tecton-codex-voice-e2e-contract"></a>
### Voice E2E Goal Contract

- Category: `testing`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Run a long-horizon Codex goal against a TypeScript voice system using a reading list, working rules, concrete done-when criteria, and anti-pattern fences.
- Verification: `four target end-to-end voice scenarios pass, transcript review shows no prompt loops, and unavailable metrics are documented honestly`
- Source: [Tecton & Tide Codex goal run](https://www.tectontide.com/en/blog/codex-goal-six-hour-run/)
- Source type: `third-party-review`
- Evidence: All four target end-to-end voice scenarios passed verification
- Evidence summary: All four target end-to-end voice scenarios passed verification; source: Tecton & Tide Codex goal run; type: third-party-review; verification: four target end-to-end voice scenarios pass, transcript review shows no prompt loops, and unavailable metrics are documented honestly

```text
/goal
GOAL:
Complete Voice E2E Goal Contract for a project with failing or missing verification gates: Run a long-horizon Codex goal against a TypeScript voice system using a reading list, working rules, concrete done-when criteria, and anti-pattern fences.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect test suites, lint config, CI logs, coverage reports, and failing output.
- Establish a baseline by running or locating evidence for: `four target end-to-end voice scenarios pass, transcript review shows no prompt loops, and unavailable metrics are documented honestly`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not weaken lint, typecheck, or test rules to create a green result.
- Fix production or fixture causes before changing expectations.

DONE WHEN:
- The implementation or documentation directly satisfies: Run a long-horizon Codex goal against a TypeScript voice system using a reading list, working rules, concrete done-when criteria, and anti-pattern fences.
- The verification command or evidence path succeeds: `four target end-to-end voice scenarios pass, transcript review shows no prompt loops, and unavailable metrics are documented honestly`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `four target end-to-end voice scenarios pass, transcript review shows no prompt loops, and unavailable metrics are documented honestly` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="halmob-checkout-p95-goal"></a>
### Checkout P95 Latency Goal

- Category: `performance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Reduce checkout p95 latency below a numeric target while keeping the correctness suite green and logging each experiment.
- Verification: `checkout benchmark p95 below 120 ms, correctness suite green, iteration log, and blocker report if the benchmark cannot run`
- Source: [Halmob Codex goals guide](https://halmob.com/blog/openai-codex-goals-persistent-objectives-guide)
- Source type: `third-party-tutorial`
- Evidence: Reduce p95 checkout latency below 120 ms
- Evidence summary: Reduce p95 checkout latency below 120 ms; source: Halmob Codex goals guide; type: third-party-tutorial; verification: checkout benchmark p95 below 120 ms, correctness suite green, iteration log, and blocker report if the benchmark cannot run

```text
/goal
GOAL:
Complete Checkout P95 Latency Goal for a web application with measurable performance goals: Reduce checkout p95 latency below a numeric target while keeping the correctness suite green and logging each experiment.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect Lighthouse reports, bundles, traces, and critical routes.
- Establish a baseline by running or locating evidence for: `checkout benchmark p95 below 120 ms, correctness suite green, iteration log, and blocker report if the benchmark cannot run`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not trade correctness, accessibility, or security for faster synthetic scores.
- Compare before/after metrics on the same route and environment.

DONE WHEN:
- The implementation or documentation directly satisfies: Reduce checkout p95 latency below a numeric target while keeping the correctness suite green and logging each experiment.
- The verification command or evidence path succeeds: `checkout benchmark p95 below 120 ms, correctness suite green, iteration log, and blocker report if the benchmark cannot run`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `checkout benchmark p95 below 120 ms, correctness suite green, iteration log, and blocker report if the benchmark cannot run` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="halmob-research-reproduction-goal"></a>
### Evidence-Backed Research Reproduction

- Category: `research`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Reproduce a paper or research result as far as local materials allow while separating confirmed findings, approximate reconstructions, blocked claims, and remaining uncertainty.
- Verification: `report with confirmed findings, approximate reconstructions, blocked claims, remaining uncertainty, and inspected outputs`
- Source: [Halmob Codex goals guide](https://halmob.com/blog/openai-codex-goals-persistent-objectives-guide)
- Source type: `third-party-tutorial`
- Evidence: Produce the strongest evidence-backed reproduction of the paper
- Evidence summary: Produce the strongest evidence-backed reproduction of the paper; source: Halmob Codex goals guide; type: third-party-tutorial; verification: report with confirmed findings, approximate reconstructions, blocked claims, remaining uncertainty, and inspected outputs

```text
/goal
GOAL:
Complete Evidence-Backed Research Reproduction for a research task: Reproduce a paper or research result as far as local materials allow while separating confirmed findings, approximate reconstructions, blocked claims, and remaining uncertainty.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect source lists, citation notes, evidence files, and acceptance criteria.
- Establish a baseline by running or locating evidence for: `report with confirmed findings, approximate reconstructions, blocked claims, remaining uncertainty, and inspected outputs`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not present unsourced claims as facts.
- Keep direct quotes short and attach a public URL for every external claim.

DONE WHEN:
- The implementation or documentation directly satisfies: Reproduce a paper or research result as far as local materials allow while separating confirmed findings, approximate reconstructions, blocked claims, and remaining uncertainty.
- The verification command or evidence path succeeds: `report with confirmed findings, approximate reconstructions, blocked claims, remaining uncertainty, and inspected outputs`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `report with confirmed findings, approximate reconstructions, blocked claims, remaining uncertainty, and inspected outputs` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="codex-goalcraft-six-field-contract"></a>
### Goalcraft Six-Field Contract Spine

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Write any /goal as a compact, evidence-first, thread-scoped completion contract with explicit outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop conditions instead of vague effort descriptions.
- Verification: `activated goal text passes length and structure validation (under 4000 chars, all 6 fields present); subsequent agent run produces claim-by-claim evidence audit instead of proxy claims`
- Source: [goalcraft SKILL.md](https://raw.githubusercontent.com/grp06/goalcraft/main/SKILL.md)
- Source type: `tool-readme`
- Evidence: six-field spine: Outcome + Verification surface + Constraints + Boundaries + Iteration policy + Blocked stop condition
- Evidence summary: six-field spine: Outcome + Verification surface + Constraints + Boundaries + Iteration policy + Blocked stop condition; source: goalcraft SKILL.md; type: tool-readme; verification: activated goal text passes length and structure validation (under 4000 chars, all 6 fields present); subsequent agent run produces claim-by-claim evidence audit instead of proxy claims

```text
/goal
GOAL:
Complete Goalcraft Six-Field Contract Spine for a coding-agent workflow repository: Write any /goal as a compact, evidence-first, thread-scoped completion contract with explicit outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop conditions instead of vague effort descriptions.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `activated goal text passes length and structure validation (under 4000 chars, all 6 fields present); subsequent agent run produces claim-by-claim evidence audit instead of proxy claims`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: Write any /goal as a compact, evidence-first, thread-scoped completion contract with explicit outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop conditions instead of vague effort descriptions.
- The verification command or evidence path succeeds: `activated goal text passes length and structure validation (under 4000 chars, all 6 fields present); subsequent agent run produces claim-by-claim evidence audit instead of proxy claims`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `activated goal text passes length and structure validation (under 4000 chars, all 6 fields present); subsequent agent run produces claim-by-claim evidence audit instead of proxy claims` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-md-fitness-dual-score-loop"></a>
### Fitness Function Dual-Score Improvement Loop

- Category: `prompt-optimization`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: For goals without natural scalar metric (docs quality, code health, consistency), construct an explicit runnable fitness function plus dual-score (outcome + instrument quality guard) and drive an improvement loop with iterations.jsonl ledger until converge criteria.
- Verification: `./scripts/score.sh --json outputs numeric scores; iterations.jsonl shows progress without instrument gaming; final report matches When to Stop template`
- Source: [goal-md template](https://raw.githubusercontent.com/jmilinovich/goal-md/main/template/GOAL.md)
- Source type: `tool-readme`
- Evidence: dual-score split + measure/diagnose/act/verify/revert loop + Action Catalog + machine-checkable stopping conditions
- Evidence summary: dual-score split + measure/diagnose/act/verify/revert loop + Action Catalog + machine-checkable stopping conditions; source: goal-md template; type: tool-readme; verification: ./scripts/score.sh --json outputs numeric scores; iterations.jsonl shows progress without instrument gaming; final report matches When to Stop template

```text
/goal
GOAL:
Complete Fitness Function Dual-Score Improvement Loop for an eval-backed prompt project: For goals without natural scalar metric (docs quality, code health, consistency), construct an explicit runnable fitness function plus dual-score (outcome + instrument quality guard) and drive an improvement loop with iterations.jsonl ledger until converge criteria.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect prompt files, eval cases, scoring reports, regressions, and failure examples.
- Establish a baseline by running or locating evidence for: `./scripts/score.sh --json outputs numeric scores; iterations.jsonl shows progress without instrument gaming; final report matches When to Stop template`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not delete, weaken, or cherry-pick eval cases to improve the score.
- Report representative failures as well as the final score.

DONE WHEN:
- The implementation or documentation directly satisfies: For goals without natural scalar metric (docs quality, code health, consistency), construct an explicit runnable fitness function plus dual-score (outcome + instrument quality guard) and drive an improvement loop with iterations.jsonl ledger until converge criteria.
- The verification command or evidence path succeeds: `./scripts/score.sh --json outputs numeric scores; iterations.jsonl shows progress without instrument gaming; final report matches When to Stop template`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `./scripts/score.sh --json outputs numeric scores; iterations.jsonl shows progress without instrument gaming; final report matches When to Stop template` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="goal-ledger-html-resume-incomplete-hatch"></a>
### Single-File HTML Goal Ledger with Resume Block and Structured Incomplete Escape

- Category: `goal-maintenance`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Maintain one canonical browser-viewable implementation-notes.html containing Resume Here block, inline progressEvents timeline, and explicit [incomplete]/[blocked] states with full reason/proof/impact so long-running /goal can safely pause and resume across compaction or handoff without drift.
- Verification: `.agent/runs/<goal-id>/implementation-notes.html exists, opens in browser, is appended at every checkpoint, and any incomplete item carries structured explanation instead of silent drop`
- Source: [kingbootoshi/goal-ledger SKILL.md](https://raw.githubusercontent.com/kingbootoshi/goal-ledger/main/plugins/goal-ledger/skills/goal/SKILL.md)
- Source type: `tool-readme`
- Evidence: Resume Here + progressEvents array + 6 states including [incomplete] with mandatory explanation fields
- Evidence summary: Resume Here + progressEvents array + 6 states including [incomplete] with mandatory explanation fields; source: kingbootoshi/goal-ledger SKILL.md; type: tool-readme; verification: .agent/runs/<goal-id>/implementation-notes.html exists, opens in browser, is appended at every checkpoint, and any incomplete item carries structured explanation instead of silent drop

```text
/goal
GOAL:
Complete Single-File HTML Goal Ledger with Resume Block and Structured Incomplete Escape for a goal-management workflow: Maintain one canonical browser-viewable implementation-notes.html containing Resume Here block, inline progressEvents timeline, and explicit [incomplete]/[blocked] states with full reason/proof/impact so long-running /goal can safely pause and resume across compaction or handoff without drift.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect active goals, done conditions, audit logs, and continuation state.
- Establish a baseline by running or locating evidence for: `.agent/runs/<goal-id>/implementation-notes.html exists, opens in browser, is appended at every checkpoint, and any incomplete item carries structured explanation instead of silent drop`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not mark a goal complete without auditing the current done condition.
- Keep goal edits and completion reasons visible in the final output.

DONE WHEN:
- The implementation or documentation directly satisfies: Maintain one canonical browser-viewable implementation-notes.html containing Resume Here block, inline progressEvents timeline, and explicit [incomplete]/[blocked] states with full reason/proof/impact so long-running /goal can safely pause and resume across compaction or handoff without drift.
- The verification command or evidence path succeeds: `.agent/runs/<goal-id>/implementation-notes.html exists, opens in browser, is appended at every checkpoint, and any incomplete item carries structured explanation instead of silent drop`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `.agent/runs/<goal-id>/implementation-notes.html exists, opens in browser, is appended at every checkpoint, and any incomplete item carries structured explanation instead of silent drop` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="chinese-v2ex-grillme-strong-goal-contract"></a>
### Strong Verifiable Goal Contract After Alignment Interview

- Category: `workflow`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: After a structured alignment interview, produce a binding /goal contract with explicit success evidence, hard constraints, file boundaries, iteration strategy, and blocking/escape handling so a Ralph-loop or native /goal agent can run autonomously until evidence-based completion.
- Verification: `final agent output includes scoped diff + passing verification commands + iteration/token log; DONE WHEN audited against original contract without subjective claims; escape triggered on budget or blocker`
- Source: [V2EX Chinese engineering community (JustW post)](https://v2ex.com/t/1214285)
- Source type: `public-forum`
- Evidence: grill-me + goal 6-element strong contract pattern with Ralph loop execution
- Evidence summary: grill-me + goal 6-element strong contract pattern with Ralph loop execution; source: V2EX Chinese engineering community (JustW post); type: public-forum; verification: final agent output includes scoped diff + passing verification commands + iteration/token log; DONE WHEN audited against original contract without subjective claims; escape triggered on budget or blocker

```text
/goal
GOAL:
Complete Strong Verifiable Goal Contract After Alignment Interview for a coding-agent workflow repository: After a structured alignment interview, produce a binding /goal contract with explicit success evidence, hard constraints, file boundaries, iteration strategy, and blocking/escape handling so a Ralph-loop or native /goal agent can run autonomously until evidence-based completion.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect goal text, progress logs, branch state, and verification artifacts.
- Establish a baseline by running or locating evidence for: `final agent output includes scoped diff + passing verification commands + iteration/token log; DONE WHEN audited against original contract without subjective claims; escape triggered on budget or blocker`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not claim a goal is complete without a current audit of the stated contract.
- Pause if the goal text, branch state, or permissions are inconsistent.

DONE WHEN:
- The implementation or documentation directly satisfies: After a structured alignment interview, produce a binding /goal contract with explicit success evidence, hard constraints, file boundaries, iteration strategy, and blocking/escape handling so a Ralph-loop or native /goal agent can run autonomously until evidence-based completion.
- The verification command or evidence path succeeds: `final agent output includes scoped diff + passing verification commands + iteration/token log; DONE WHEN audited against original contract without subjective claims; escape triggered on budget or blocker`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `final agent output includes scoped diff + passing verification commands + iteration/token log; DONE WHEN audited against original contract without subjective claims; escape triggered on budget or blocker` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="github-copilot-usage-metrics-reconciliation"></a>
### Copilot Usage Metrics Reconciliation

- Category: `data-analytics`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Reconcile Copilot dashboard, API, and export metrics before reporting agent adoption or pull-request impact trends.
- Verification: `metrics reconciliation report with dashboard/API/export fields, documented exclusions, and team-level join notes`
- Source: [GitHub Copilot usage metrics reconciliation docs](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/reconciling-usage-metrics)
- Source type: `official-workflow`
- Evidence: dashboard, APIs, and export files all use the same underlying telemetry data, but they aggregate and present it differently
- Evidence summary: dashboard, APIs, and export files all use the same underlying telemetry data, but they aggregate and present it differently; source: GitHub Copilot usage metrics reconciliation docs; type: official-workflow; verification: metrics reconciliation report with dashboard/API/export fields, documented exclusions, and team-level join notes

```text
/goal
GOAL:
Complete Copilot Usage Metrics Reconciliation for an analytics or BI project: Reconcile Copilot dashboard, API, and export metrics before reporting agent adoption or pull-request impact trends.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect metric SQL, event schemas, dashboard definitions, and validation queries.
- Establish a baseline by running or locating evidence for: `metrics reconciliation report with dashboard/API/export fields, documented exclusions, and team-level join notes`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.

DONE WHEN:
- The implementation or documentation directly satisfies: Reconcile Copilot dashboard, API, and export metrics before reporting agent adoption or pull-request impact trends.
- The verification command or evidence path succeeds: `metrics reconciliation report with dashboard/API/export fields, documented exclusions, and team-level join notes`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `metrics reconciliation report with dashboard/API/export fields, documented exclusions, and team-level join notes` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

<a id="layout-design-system-context-export"></a>
### Design System Context Export

- Category: `design`
- Difficulty: `intermediate`
- Origin: `source-backed`
- Intent: Extract design tokens, components, and visual patterns into agent-readable context so generated UI follows the product design system.
- Verification: `layout.md and token export reviewed, component variant preview checked, and design-system health score or screenshot evidence captured`
- Source: [Layout design system docs](https://layout.design/docs)
- Source type: `third-party-project`
- Evidence: Pull design tokens, components, fonts, and screenshots from Figma files or live websites
- Evidence summary: Pull design tokens, components, fonts, and screenshots from Figma files or live websites; source: Layout design system docs; type: third-party-project; verification: layout.md and token export reviewed, component variant preview checked, and design-system health score or screenshot evidence captured

```text
/goal
GOAL:
Complete Design System Context Export for a product UI codebase: Extract design tokens, components, and visual patterns into agent-readable context so generated UI follows the product design system.

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect design tokens, component variants, layouts, visual states, and screenshots.
- Establish a baseline by running or locating evidence for: `layout.md and token export reviewed, component variant preview checked, and design-system health score or screenshot evidence captured`.

CONSTRAINTS:
- Keep the scope limited to this goal; do not expand into unrelated cleanup.
- Do not weaken tests, delete assertions, or mask errors to make verification pass.
- Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.
- Do not replace the app with a landing-page style redesign.
- Preserve domain workflows and use existing design tokens where they exist.

DONE WHEN:
- The implementation or documentation directly satisfies: Extract design tokens, components, and visual patterns into agent-readable context so generated UI follows the product design system.
- The verification command or evidence path succeeds: `layout.md and token export reviewed, component variant preview checked, and design-system health score or screenshot evidence captured`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `layout.md and token export reviewed, component variant preview checked, and design-system health score or screenshot evidence captured` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN.
```

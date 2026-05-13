# 200 Goal Prompt Examples

Each example is a complete `/goal` task contract. Replace placeholder commands, paths, and project names with your repository's real values before running.

These examples intentionally use only the documented `/goal <objective>` form. They do not rely on unofficial subcommands.

## Index

### backend-api
- [001. API Contract Drift Audit](#001-api-contract-drift-audit)
- [002. Idempotent Create Endpoint](#002-idempotent-create-endpoint)
- [003. API Error Taxonomy](#003-api-error-taxonomy)
- [004. Pagination Consistency](#004-pagination-consistency)
- [005. Request Validation Boundary](#005-request-validation-boundary)
- [006. API Rate Limit Policy](#006-api-rate-limit-policy)
- [007. Webhook Retry Contract](#007-webhook-retry-contract)
- [008. Backward-Compatible Response](#008-backward-compatible-response)
- [009. gRPC Timeout Propagation](#009-grpc-timeout-propagation)
- [010. Async Job State Machine](#010-async-job-state-machine)
- [011. Resource-Level Authorization](#011-authz-resource-scope)
- [012. API Versioning Plan](#012-api-versioning-plan)

### backend-data
- [013. Database Migration Safety](#013-db-migration-safety)
- [014. Transaction Boundary Audit](#014-transaction-boundary-audit)
- [015. Cache Invalidation Map](#015-cache-invalidation-map)
- [016. N+1 Query Fix](#016-n-plus-one-query-fix)
- [017. Optimistic Locking Rollout](#017-optimistic-locking-rollout)
- [018. Soft Delete Integrity](#018-soft-delete-integrity)
- [019. Index Regression Check](#019-db-index-regression)
- [020. Outbox Reliable Events](#020-outbox-pattern-adoption)
- [021. Read Replica Lag Guard](#021-read-replica-lag-guard)
- [022. Schema Drift Detector](#022-schema-drift-detector)

### devops-ci
- [023. CI Flaky Test Triage](#023-ci-flaky-test-triage)
- [024. Build Cache Correctness](#024-build-cache-correctness)
- [025. Dependency Update Gate](#025-dependency-update-gate)
- [026. Monorepo Affected Tests](#026-monorepo-affected-tests)
- [027. Release Notes From Diff](#027-release-note-from-diff)
- [028. Artifact Provenance](#028-artifact-provenance)
- [029. CI Permission Minimization](#029-ci-permission-minimize)
- [030. Branch Protection Audit](#030-branch-protection-audit)
- [031. Release Rollback Drill](#031-release-rollback-drill)
- [032. Semantic Version Check](#032-semantic-version-check)

### devops-runtime
- [033. Docker Image Slimming](#033-docker-image-slimming)
- [034. Kubernetes Probe Repair](#034-k8s-readiness-liveness)
- [035. Terraform Plan Review](#035-terraform-plan-review)
- [036. Helm Values Drift](#036-helm-values-drift)
- [037. Autoscaling Thresholds](#037-autoscaling-thresholds)
- [038. Runtime Config Validation](#038-runtime-config-validation)
- [039. Zero-Downtime Migration](#039-zero-downtime-migration)
- [040. Observability Minimum](#040-observability-minimum)
- [041. Incident Runbook Gap](#041-incident-runbook-gap)
- [042. Queue Backpressure](#042-queue-backpressure)

### security-appsec
- [043. SQL Injection Audit](#043-sql-injection-audit)
- [044. Command Injection Audit](#044-command-injection-audit)
- [045. SSRF Defense Review](#045-ssrf-defense-review)
- [046. XSS Output Encoding](#046-xss-output-encoding)
- [047. CSRF Sensitive Action](#047-csrf-sensitive-action)
- [048. Auth Bypass Route Map](#048-auth-bypass-route-map)
- [049. File Upload Security](#049-file-upload-security)
- [050. Tenant Isolation Test](#050-tenant-isolation-test)
- [051. Replay Attack Defense](#051-replay-attack-defense)
- [052. IDOR Audit](#052-insecure-direct-object-ref)

### security-ops
- [053. Secret Scan Baseline](#053-secret-scan-baseline)
- [054. IAM Least Privilege](#054-iam-least-privilege)
- [055. GitHub Actions Supply Chain](#055-github-actions-supply-chain)
- [056. Container Vulnerability Triage](#056-container-vuln-triage)
- [057. Audit Log Coverage](#057-audit-log-coverage)
- [058. Secret Rotation Drill](#058-secret-rotation-drill)
- [059. Dependency Confusion Guard](#059-dependency-confusion-guard)
- [060. SBOM Generation](#060-sbom-generation)
- [061. Production Access Review](#061-prod-access-review)
- [062. Backup Restore Security](#062-backup-restore-security)

### data-eng
- [063. ETL Contract Tests](#063-etl-contract-tests)
- [064. Data Quality Rules](#064-data-quality-rules)
- [065. Backfill Safety Plan](#065-backfill-safety-plan)
- [066. Incremental Load Watermark](#066-incremental-load-watermark)
- [067. Late-Arriving Data](#067-late-arriving-data)
- [068. Data Lineage Map](#068-data-lineage-map)
- [069. PII Classification](#069-pii-classification)
- [070. Data Retention Enforcement](#070-data-retention-enforcement)
- [071. Warehouse Cost Audit](#071-warehouse-cost-audit)
- [072. Stream Processing Lag](#072-stream-processing-lag)

### data-analytics
- [073. Metric Definition Lock](#073-metric-definition-lock)
- [074. Dashboard Trust Audit](#074-dashboard-trust-audit)
- [075. A/B Test SRM Check](#075-ab-test-srm-check)
- [076. Funnel Dropoff Diagnosis](#076-funnel-dropoff-diagnosis)
- [077. Cohort Retention Query](#077-cohort-retention-query)
- [078. Revenue Reconciliation](#078-revenue-reconciliation)
- [079. Event Taxonomy Cleanup](#079-event-taxonomy-cleanup)
- [080. Anomaly Detection Baseline](#080-anomaly-detection-baseline)
- [081. Attribution Window Review](#081-attribution-window-review)
- [082. Self-Serve Data Contract](#082-self-serve-data-contract)

### ai-evals
- [083. LLM Golden Set Build](#083-llm-golden-set-build)
- [084. LLM Regression Gate](#084-llm-regression-gate)
- [085. Judge Calibration](#085-judge-calibration)
- [086. Hallucination Probe Suite](#086-hallucination-probe-suite)
- [087. RAG Answer Faithfulness](#087-rag-answer-faithfulness)
- [088. Tool Use Eval](#088-tool-use-eval)
- [089. Prompt Injection Red Team](#089-adversarial-prompt-redteam)
- [090. Eval Data Dedup](#090-eval-data-dedup)
- [091. Cost Quality Frontier](#091-cost-quality-frontier)
- [092. Rubric-Driven Eval](#092-rubric-driven-eval)

### ai-ops
- [093. Prompt Version Registry](#093-prompt-version-registry)
- [094. RAG Chunking Experiment](#094-rag-chunking-experiment)
- [095. Vector Index Refresh](#095-vector-index-refresh)
- [096. Model Routing Policy](#096-model-routing-policy)
- [097. LLM Timeout Budget](#097-llm-timeout-budget)
- [098. Token Cost Attribution](#098-token-cost-attribution)
- [099. RAG Prompt Injection Filter](#099-prompt-injection-filter)
- [100. AI Output Schema Guard](#100-ai-output-schema-guard)
- [101. Human Review Threshold](#101-human-review-threshold)
- [102. AI Observability Traces](#102-ai-observability-traces)

### frontend
- [103. Empty State System](#103-frontend-empty-states)
- [104. Error Boundary Experience](#104-frontend-error-boundary)
- [105. Loading Skeletons](#105-frontend-loading-skeletons)
- [106. Form Validation](#106-frontend-form-validation)
- [107. Data Table Density](#107-frontend-table-density)
- [108. Command Palette](#108-frontend-command-palette)
- [109. Navigation Map](#109-frontend-navigation-map)
- [110. State Recovery](#110-frontend-state-recovery)
- [111. Permission State UI](#111-frontend-permission-ui)
- [112. Bulk Actions](#112-frontend-bulk-actions)
- [113. Search Filter Experience](#113-frontend-search-filter)
- [114. Realtime Update Prompts](#114-frontend-realtime-updates)

### design
- [115. Visual Hierarchy Pass](#115-design-visual-hierarchy)
- [116. Design Token Audit](#116-design-token-audit)
- [117. Component Variant Matrix](#117-design-component-variants)
- [118. Dashboard Layout Pass](#118-design-dashboard-layout)
- [119. Modal Discipline](#119-design-modal-discipline)
- [120. Iconography System](#120-design-iconography)
- [121. Color Contrast Pass](#121-design-color-contrast)
- [122. Motion Rules](#122-design-motion-rules)
- [123. Responsive Grid](#123-design-responsive-grid)
- [124. Toolbar Usability](#124-design-toolbar-usability)
- [125. Data Card System](#125-design-data-card-system)
- [126. Brand Fit Pass](#126-design-brand-fit)

### mobile
- [127. Mobile Bottom Navigation](#127-mobile-bottom-nav)
- [128. Mobile Touch Targets](#128-mobile-touch-targets)
- [129. Mobile Form Flow](#129-mobile-form-flow)
- [130. Mobile Table Adaptation](#130-mobile-table-adaptation)
- [131. Mobile Filter Drawer](#131-mobile-filter-drawer)
- [132. Mobile Offline State](#132-mobile-offline-state)
- [133. Mobile Image Performance](#133-mobile-image-performance)
- [134. Mobile Safe Area](#134-mobile-safe-area)
- [135. Mobile Gesture Conflicts](#135-mobile-gesture-conflicts)
- [136. Mobile Login Flow](#136-mobile-login-flow)
- [137. Mobile Onboarding](#137-mobile-onboarding)
- [138. Mobile Device Matrix](#138-mobile-device-matrix)

### docs
- [139. Quickstart](#139-docs-quickstart)
- [140. Install Troubleshooting](#140-docs-install-troubleshooting)
- [141. API Examples](#141-docs-api-examples)
- [142. Architecture Overview](#142-docs-architecture-overview)
- [143. Contribution Guide](#143-docs-contribution-guide)
- [144. Release Notes](#144-docs-release-notes)
- [145. Environment Variables](#145-docs-env-vars)
- [146. Operator Runbook](#146-docs-runbook)
- [147. Architecture Decision Records](#147-docs-decision-records)
- [148. Glossary](#148-docs-glossary)
- [149. Screenshot Docs](#149-docs-screenshot-docs)
- [150. Docs Lint Gate](#150-docs-docs-lint)

### product
- [151. User Journeys](#151-product-user-journeys)
- [152. PRD Skeleton](#152-product-prd-skeleton)
- [153. Onboarding Metrics](#153-product-onboarding-metrics)
- [154. Feature Prioritization](#154-product-feature-prioritization)
- [155. Permission Model](#155-product-permission-model)
- [156. Notification Strategy](#156-product-notification-strategy)
- [157. Empty Data Policy](#157-product-empty-data-policy)
- [158. Upgrade Path](#158-product-upgrade-path)
- [159. Feedback Loop](#159-product-feedback-loop)
- [160. Search Relevance](#160-product-search-relevance)
- [161. Admin Workflows](#161-product-admin-workflows)
- [162. Success Criteria](#162-product-success-criteria)

### qa
- [163. Critical Path Tests](#163-qa-critical-paths)
- [164. Regression Matrix](#164-qa-regression-matrix)
- [165. Fixture Strategy](#165-qa-fixture-strategy)
- [166. Visual Regression](#166-qa-visual-regression)
- [167. API Contracts](#167-qa-api-contracts)
- [168. Flaky Test Audit](#168-qa-flaky-test-audit)
- [169. Error Injection](#169-qa-error-injection)
- [170. Cross-Browser Coverage](#170-qa-cross-browser)
- [171. Release Smoke](#171-qa-release-smoke)
- [172. Data Migration Test](#172-qa-data-migration)
- [173. Security Smoke](#173-qa-security-smoke)
- [174. Bug Reproduction Template](#174-qa-bug-repro-template)

### accessibility
- [175. Keyboard Navigation](#175-accessibility-keyboard-nav)
- [176. Screen Reader Semantics](#176-accessibility-screen-reader)
- [177. Focus Visible](#177-accessibility-focus-visible)
- [178. Color Contrast](#178-accessibility-color-contrast)
- [179. Accessible Form Errors](#179-accessibility-form-errors)
- [180. Modal Focus Trap](#180-accessibility-modal-trap)
- [181. Reduced Motion](#181-accessibility-reduced-motion)
- [182. Alt Text Audit](#182-accessibility-alt-text)
- [183. Heading Order](#183-accessibility-heading-order)
- [184. Live Region Feedback](#184-accessibility-live-region)
- [185. Touch Accessibility](#185-accessibility-touch-a11y)
- [186. Accessibility Audit Report](#186-accessibility-audit-report)

### performance
- [187. LCP Optimization](#187-performance-lcp)
- [188. CLS Fix](#188-performance-cls)
- [189. INP Optimization](#189-performance-inp)
- [190. Bundle Budget](#190-performance-bundle-budget)
- [191. Code Splitting](#191-performance-code-splitting)
- [192. Image Pipeline](#192-performance-image-pipeline)
- [193. Font Loading](#193-performance-font-loading)
- [194. API Waterfall](#194-performance-api-waterfall)
- [195. Cache Strategy](#195-performance-cache-strategy)
- [196. Memory Leak Audit](#196-performance-memory-leaks)
- [197. Render Count Audit](#197-performance-render-count)
- [198. Performance CI Gate](#198-performance-ci-gate)

### workflow
- [199. Goal Prompt Writer](#199-goal-meta-prompt-writer)
- [200. Goal Continuation Audit](#200-goal-continuation-audit)

## Examples

<a id="001-api-contract-drift-audit"></a>
### 001. API Contract Drift Audit

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="002-idempotent-create-endpoint"></a>
### 002. Idempotent Create Endpoint

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="003-api-error-taxonomy"></a>
### 003. API Error Taxonomy

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="004-pagination-consistency"></a>
### 004. Pagination Consistency

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="005-request-validation-boundary"></a>
### 005. Request Validation Boundary

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="006-api-rate-limit-policy"></a>
### 006. API Rate Limit Policy

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="007-webhook-retry-contract"></a>
### 007. Webhook Retry Contract

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="008-backward-compatible-response"></a>
### 008. Backward-Compatible Response

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="009-grpc-timeout-propagation"></a>
### 009. gRPC Timeout Propagation

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="010-async-job-state-machine"></a>
### 010. Async Job State Machine

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="011-authz-resource-scope"></a>
### 011. Resource-Level Authorization

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="012-api-versioning-plan"></a>
### 012. API Versioning Plan

- Category: `backend-api`
- Difficulty: `intermediate`
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

<a id="013-db-migration-safety"></a>
### 013. Database Migration Safety

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="014-transaction-boundary-audit"></a>
### 014. Transaction Boundary Audit

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="015-cache-invalidation-map"></a>
### 015. Cache Invalidation Map

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="016-n-plus-one-query-fix"></a>
### 016. N+1 Query Fix

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="017-optimistic-locking-rollout"></a>
### 017. Optimistic Locking Rollout

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="018-soft-delete-integrity"></a>
### 018. Soft Delete Integrity

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="019-db-index-regression"></a>
### 019. Index Regression Check

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="020-outbox-pattern-adoption"></a>
### 020. Outbox Reliable Events

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="021-read-replica-lag-guard"></a>
### 021. Read Replica Lag Guard

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="022-schema-drift-detector"></a>
### 022. Schema Drift Detector

- Category: `backend-data`
- Difficulty: `advanced`
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

<a id="023-ci-flaky-test-triage"></a>
### 023. CI Flaky Test Triage

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="024-build-cache-correctness"></a>
### 024. Build Cache Correctness

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="025-dependency-update-gate"></a>
### 025. Dependency Update Gate

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="026-monorepo-affected-tests"></a>
### 026. Monorepo Affected Tests

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="027-release-note-from-diff"></a>
### 027. Release Notes From Diff

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="028-artifact-provenance"></a>
### 028. Artifact Provenance

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="029-ci-permission-minimize"></a>
### 029. CI Permission Minimization

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="030-branch-protection-audit"></a>
### 030. Branch Protection Audit

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="031-release-rollback-drill"></a>
### 031. Release Rollback Drill

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="032-semantic-version-check"></a>
### 032. Semantic Version Check

- Category: `devops-ci`
- Difficulty: `intermediate`
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

<a id="033-docker-image-slimming"></a>
### 033. Docker Image Slimming

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="034-k8s-readiness-liveness"></a>
### 034. Kubernetes Probe Repair

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="035-terraform-plan-review"></a>
### 035. Terraform Plan Review

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="036-helm-values-drift"></a>
### 036. Helm Values Drift

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="037-autoscaling-thresholds"></a>
### 037. Autoscaling Thresholds

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="038-runtime-config-validation"></a>
### 038. Runtime Config Validation

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="039-zero-downtime-migration"></a>
### 039. Zero-Downtime Migration

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="040-observability-minimum"></a>
### 040. Observability Minimum

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="041-incident-runbook-gap"></a>
### 041. Incident Runbook Gap

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="042-queue-backpressure"></a>
### 042. Queue Backpressure

- Category: `devops-runtime`
- Difficulty: `advanced`
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

<a id="043-sql-injection-audit"></a>
### 043. SQL Injection Audit

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="044-command-injection-audit"></a>
### 044. Command Injection Audit

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="045-ssrf-defense-review"></a>
### 045. SSRF Defense Review

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="046-xss-output-encoding"></a>
### 046. XSS Output Encoding

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="047-csrf-sensitive-action"></a>
### 047. CSRF Sensitive Action

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="048-auth-bypass-route-map"></a>
### 048. Auth Bypass Route Map

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="049-file-upload-security"></a>
### 049. File Upload Security

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="050-tenant-isolation-test"></a>
### 050. Tenant Isolation Test

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="051-replay-attack-defense"></a>
### 051. Replay Attack Defense

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="052-insecure-direct-object-ref"></a>
### 052. IDOR Audit

- Category: `security-appsec`
- Difficulty: `advanced`
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

<a id="053-secret-scan-baseline"></a>
### 053. Secret Scan Baseline

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="054-iam-least-privilege"></a>
### 054. IAM Least Privilege

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="055-github-actions-supply-chain"></a>
### 055. GitHub Actions Supply Chain

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="056-container-vuln-triage"></a>
### 056. Container Vulnerability Triage

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="057-audit-log-coverage"></a>
### 057. Audit Log Coverage

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="058-secret-rotation-drill"></a>
### 058. Secret Rotation Drill

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="059-dependency-confusion-guard"></a>
### 059. Dependency Confusion Guard

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="060-sbom-generation"></a>
### 060. SBOM Generation

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="061-prod-access-review"></a>
### 061. Production Access Review

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="062-backup-restore-security"></a>
### 062. Backup Restore Security

- Category: `security-ops`
- Difficulty: `advanced`
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

<a id="063-etl-contract-tests"></a>
### 063. ETL Contract Tests

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="064-data-quality-rules"></a>
### 064. Data Quality Rules

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="065-backfill-safety-plan"></a>
### 065. Backfill Safety Plan

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="066-incremental-load-watermark"></a>
### 066. Incremental Load Watermark

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="067-late-arriving-data"></a>
### 067. Late-Arriving Data

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="068-data-lineage-map"></a>
### 068. Data Lineage Map

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="069-pii-classification"></a>
### 069. PII Classification

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="070-data-retention-enforcement"></a>
### 070. Data Retention Enforcement

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="071-warehouse-cost-audit"></a>
### 071. Warehouse Cost Audit

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="072-stream-processing-lag"></a>
### 072. Stream Processing Lag

- Category: `data-eng`
- Difficulty: `intermediate`
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

<a id="073-metric-definition-lock"></a>
### 073. Metric Definition Lock

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="074-dashboard-trust-audit"></a>
### 074. Dashboard Trust Audit

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="075-ab-test-srm-check"></a>
### 075. A/B Test SRM Check

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="076-funnel-dropoff-diagnosis"></a>
### 076. Funnel Dropoff Diagnosis

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="077-cohort-retention-query"></a>
### 077. Cohort Retention Query

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="078-revenue-reconciliation"></a>
### 078. Revenue Reconciliation

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="079-event-taxonomy-cleanup"></a>
### 079. Event Taxonomy Cleanup

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="080-anomaly-detection-baseline"></a>
### 080. Anomaly Detection Baseline

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="081-attribution-window-review"></a>
### 081. Attribution Window Review

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="082-self-serve-data-contract"></a>
### 082. Self-Serve Data Contract

- Category: `data-analytics`
- Difficulty: `intermediate`
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

<a id="083-llm-golden-set-build"></a>
### 083. LLM Golden Set Build

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="084-llm-regression-gate"></a>
### 084. LLM Regression Gate

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="085-judge-calibration"></a>
### 085. Judge Calibration

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="086-hallucination-probe-suite"></a>
### 086. Hallucination Probe Suite

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="087-rag-answer-faithfulness"></a>
### 087. RAG Answer Faithfulness

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="088-tool-use-eval"></a>
### 088. Tool Use Eval

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="089-adversarial-prompt-redteam"></a>
### 089. Prompt Injection Red Team

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="090-eval-data-dedup"></a>
### 090. Eval Data Dedup

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="091-cost-quality-frontier"></a>
### 091. Cost Quality Frontier

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="092-rubric-driven-eval"></a>
### 092. Rubric-Driven Eval

- Category: `ai-evals`
- Difficulty: `advanced`
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

<a id="093-prompt-version-registry"></a>
### 093. Prompt Version Registry

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="094-rag-chunking-experiment"></a>
### 094. RAG Chunking Experiment

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="095-vector-index-refresh"></a>
### 095. Vector Index Refresh

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="096-model-routing-policy"></a>
### 096. Model Routing Policy

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="097-llm-timeout-budget"></a>
### 097. LLM Timeout Budget

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="098-token-cost-attribution"></a>
### 098. Token Cost Attribution

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="099-prompt-injection-filter"></a>
### 099. RAG Prompt Injection Filter

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="100-ai-output-schema-guard"></a>
### 100. AI Output Schema Guard

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="101-human-review-threshold"></a>
### 101. Human Review Threshold

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="102-ai-observability-traces"></a>
### 102. AI Observability Traces

- Category: `ai-ops`
- Difficulty: `advanced`
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

<a id="103-frontend-empty-states"></a>
### 103. Empty State System

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="104-frontend-error-boundary"></a>
### 104. Error Boundary Experience

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="105-frontend-loading-skeletons"></a>
### 105. Loading Skeletons

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="106-frontend-form-validation"></a>
### 106. Form Validation

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="107-frontend-table-density"></a>
### 107. Data Table Density

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="108-frontend-command-palette"></a>
### 108. Command Palette

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="109-frontend-navigation-map"></a>
### 109. Navigation Map

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="110-frontend-state-recovery"></a>
### 110. State Recovery

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="111-frontend-permission-ui"></a>
### 111. Permission State UI

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="112-frontend-bulk-actions"></a>
### 112. Bulk Actions

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="113-frontend-search-filter"></a>
### 113. Search Filter Experience

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="114-frontend-realtime-updates"></a>
### 114. Realtime Update Prompts

- Category: `frontend`
- Difficulty: `intermediate`
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

<a id="115-design-visual-hierarchy"></a>
### 115. Visual Hierarchy Pass

- Category: `design`
- Difficulty: `intermediate`
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

<a id="116-design-token-audit"></a>
### 116. Design Token Audit

- Category: `design`
- Difficulty: `intermediate`
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

<a id="117-design-component-variants"></a>
### 117. Component Variant Matrix

- Category: `design`
- Difficulty: `intermediate`
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

<a id="118-design-dashboard-layout"></a>
### 118. Dashboard Layout Pass

- Category: `design`
- Difficulty: `intermediate`
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

<a id="119-design-modal-discipline"></a>
### 119. Modal Discipline

- Category: `design`
- Difficulty: `intermediate`
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

<a id="120-design-iconography"></a>
### 120. Iconography System

- Category: `design`
- Difficulty: `intermediate`
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

<a id="121-design-color-contrast"></a>
### 121. Color Contrast Pass

- Category: `design`
- Difficulty: `intermediate`
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

<a id="122-design-motion-rules"></a>
### 122. Motion Rules

- Category: `design`
- Difficulty: `intermediate`
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

<a id="123-design-responsive-grid"></a>
### 123. Responsive Grid

- Category: `design`
- Difficulty: `intermediate`
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

<a id="124-design-toolbar-usability"></a>
### 124. Toolbar Usability

- Category: `design`
- Difficulty: `intermediate`
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

<a id="125-design-data-card-system"></a>
### 125. Data Card System

- Category: `design`
- Difficulty: `intermediate`
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

<a id="126-design-brand-fit"></a>
### 126. Brand Fit Pass

- Category: `design`
- Difficulty: `intermediate`
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

<a id="127-mobile-bottom-nav"></a>
### 127. Mobile Bottom Navigation

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="128-mobile-touch-targets"></a>
### 128. Mobile Touch Targets

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="129-mobile-form-flow"></a>
### 129. Mobile Form Flow

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="130-mobile-table-adaptation"></a>
### 130. Mobile Table Adaptation

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="131-mobile-filter-drawer"></a>
### 131. Mobile Filter Drawer

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="132-mobile-offline-state"></a>
### 132. Mobile Offline State

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="133-mobile-image-performance"></a>
### 133. Mobile Image Performance

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="134-mobile-safe-area"></a>
### 134. Mobile Safe Area

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="135-mobile-gesture-conflicts"></a>
### 135. Mobile Gesture Conflicts

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="136-mobile-login-flow"></a>
### 136. Mobile Login Flow

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="137-mobile-onboarding"></a>
### 137. Mobile Onboarding

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="138-mobile-device-matrix"></a>
### 138. Mobile Device Matrix

- Category: `mobile`
- Difficulty: `intermediate`
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

<a id="139-docs-quickstart"></a>
### 139. Quickstart

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="140-docs-install-troubleshooting"></a>
### 140. Install Troubleshooting

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="141-docs-api-examples"></a>
### 141. API Examples

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="142-docs-architecture-overview"></a>
### 142. Architecture Overview

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="143-docs-contribution-guide"></a>
### 143. Contribution Guide

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="144-docs-release-notes"></a>
### 144. Release Notes

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="145-docs-env-vars"></a>
### 145. Environment Variables

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="146-docs-runbook"></a>
### 146. Operator Runbook

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="147-docs-decision-records"></a>
### 147. Architecture Decision Records

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="148-docs-glossary"></a>
### 148. Glossary

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="149-docs-screenshot-docs"></a>
### 149. Screenshot Docs

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="150-docs-docs-lint"></a>
### 150. Docs Lint Gate

- Category: `docs`
- Difficulty: `intermediate`
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

<a id="151-product-user-journeys"></a>
### 151. User Journeys

- Category: `product`
- Difficulty: `intermediate`
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

<a id="152-product-prd-skeleton"></a>
### 152. PRD Skeleton

- Category: `product`
- Difficulty: `intermediate`
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

<a id="153-product-onboarding-metrics"></a>
### 153. Onboarding Metrics

- Category: `product`
- Difficulty: `intermediate`
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

<a id="154-product-feature-prioritization"></a>
### 154. Feature Prioritization

- Category: `product`
- Difficulty: `intermediate`
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

<a id="155-product-permission-model"></a>
### 155. Permission Model

- Category: `product`
- Difficulty: `intermediate`
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

<a id="156-product-notification-strategy"></a>
### 156. Notification Strategy

- Category: `product`
- Difficulty: `intermediate`
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

<a id="157-product-empty-data-policy"></a>
### 157. Empty Data Policy

- Category: `product`
- Difficulty: `intermediate`
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

<a id="158-product-upgrade-path"></a>
### 158. Upgrade Path

- Category: `product`
- Difficulty: `intermediate`
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

<a id="159-product-feedback-loop"></a>
### 159. Feedback Loop

- Category: `product`
- Difficulty: `intermediate`
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

<a id="160-product-search-relevance"></a>
### 160. Search Relevance

- Category: `product`
- Difficulty: `intermediate`
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

<a id="161-product-admin-workflows"></a>
### 161. Admin Workflows

- Category: `product`
- Difficulty: `intermediate`
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

<a id="162-product-success-criteria"></a>
### 162. Success Criteria

- Category: `product`
- Difficulty: `intermediate`
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

<a id="163-qa-critical-paths"></a>
### 163. Critical Path Tests

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="164-qa-regression-matrix"></a>
### 164. Regression Matrix

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="165-qa-fixture-strategy"></a>
### 165. Fixture Strategy

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="166-qa-visual-regression"></a>
### 166. Visual Regression

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="167-qa-api-contracts"></a>
### 167. API Contracts

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="168-qa-flaky-test-audit"></a>
### 168. Flaky Test Audit

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="169-qa-error-injection"></a>
### 169. Error Injection

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="170-qa-cross-browser"></a>
### 170. Cross-Browser Coverage

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="171-qa-release-smoke"></a>
### 171. Release Smoke

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="172-qa-data-migration"></a>
### 172. Data Migration Test

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="173-qa-security-smoke"></a>
### 173. Security Smoke

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="174-qa-bug-repro-template"></a>
### 174. Bug Reproduction Template

- Category: `qa`
- Difficulty: `intermediate`
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

<a id="175-accessibility-keyboard-nav"></a>
### 175. Keyboard Navigation

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="176-accessibility-screen-reader"></a>
### 176. Screen Reader Semantics

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="177-accessibility-focus-visible"></a>
### 177. Focus Visible

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="178-accessibility-color-contrast"></a>
### 178. Color Contrast

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="179-accessibility-form-errors"></a>
### 179. Accessible Form Errors

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="180-accessibility-modal-trap"></a>
### 180. Modal Focus Trap

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="181-accessibility-reduced-motion"></a>
### 181. Reduced Motion

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="182-accessibility-alt-text"></a>
### 182. Alt Text Audit

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="183-accessibility-heading-order"></a>
### 183. Heading Order

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="184-accessibility-live-region"></a>
### 184. Live Region Feedback

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="185-accessibility-touch-a11y"></a>
### 185. Touch Accessibility

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="186-accessibility-audit-report"></a>
### 186. Accessibility Audit Report

- Category: `accessibility`
- Difficulty: `intermediate`
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

<a id="187-performance-lcp"></a>
### 187. LCP Optimization

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="188-performance-cls"></a>
### 188. CLS Fix

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="189-performance-inp"></a>
### 189. INP Optimization

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="190-performance-bundle-budget"></a>
### 190. Bundle Budget

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="191-performance-code-splitting"></a>
### 191. Code Splitting

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="192-performance-image-pipeline"></a>
### 192. Image Pipeline

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="193-performance-font-loading"></a>
### 193. Font Loading

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="194-performance-api-waterfall"></a>
### 194. API Waterfall

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="195-performance-cache-strategy"></a>
### 195. Cache Strategy

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="196-performance-memory-leaks"></a>
### 196. Memory Leak Audit

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="197-performance-render-count"></a>
### 197. Render Count Audit

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="198-performance-ci-gate"></a>
### 198. Performance CI Gate

- Category: `performance`
- Difficulty: `intermediate`
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

<a id="199-goal-meta-prompt-writer"></a>
### 199. Goal Prompt Writer

- Category: `workflow`
- Difficulty: `intermediate`
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

<a id="200-goal-continuation-audit"></a>
### 200. Goal Continuation Audit

- Category: `workflow`
- Difficulty: `intermediate`
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

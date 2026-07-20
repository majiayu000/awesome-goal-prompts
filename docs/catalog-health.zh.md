# 目录健康报告

## 概览

- 条目总数：359
- 有公开来源的条目：159
- Seed 条目：200
- 分类数：32
- 搜索评测：33/33 通过
- 缺少来源摘要的 source-backed 条目：0
- 缺少来源字段的 source-backed 条目：0

## 分类覆盖率

| 分类 | 有公开来源 | 总数 | 覆盖率 |
| --- | --- | --- | --- |
| accessibility | 1 | 13 | 8% |
| ai-evals | 2 | 12 | 17% |
| ai-ops | 2 | 12 | 17% |
| backend-api | 3 | 15 | 20% |
| backend-data | 3 | 13 | 23% |
| backlog | 3 | 3 | 100% |
| cli | 2 | 2 | 100% |
| data-analytics | 2 | 12 | 17% |
| data-eng | 2 | 12 | 17% |
| design | 2 | 14 | 14% |
| devops-ci | 2 | 12 | 17% |
| devops-runtime | 1 | 11 | 9% |
| docs | 7 | 19 | 37% |
| frontend | 6 | 18 | 33% |
| goal-maintenance | 15 | 15 | 100% |
| greenfield-build | 1 | 1 | 100% |
| investigation | 4 | 4 | 100% |
| maintenance | 2 | 2 | 100% |
| migration | 9 | 9 | 100% |
| mobile | 2 | 14 | 14% |
| orchestration | 4 | 4 | 100% |
| performance | 7 | 19 | 37% |
| product | 3 | 15 | 20% |
| prompt-optimization | 5 | 5 | 100% |
| prototype | 3 | 3 | 100% |
| qa | 3 | 15 | 20% |
| refactor | 5 | 5 | 100% |
| research | 6 | 6 | 100% |
| security-appsec | 4 | 14 | 29% |
| security-ops | 2 | 12 | 17% |
| testing | 22 | 22 | 100% |
| workflow | 24 | 26 | 92% |

## 来源类型分布

| 来源类型 | 数量 |
| --- | --- |
| github-discussion | 1 |
| github-issue | 7 |
| github-pr | 3 |
| none | 200 |
| official-agent-task | 37 |
| official-goal | 17 |
| official-workflow | 8 |
| public-forum | 12 |
| third-party-project | 8 |
| third-party-review | 3 |
| third-party-tutorial | 29 |
| tool-readme | 18 |
| video-summary | 2 |
| x-post | 14 |

## 搜索评测

| 查询 | 期望条目 | 排名 | 要求 | 状态 |
| --- | --- | --- | --- | --- |
| auth tests fail lint red | claude-auth-tests-lint | 1 | top 1 | pass |
| auth lint | claude-auth-tests-lint | 1 | top 3 | pass |
| database migration schema | claude-dev-database-migration | 1 | top 3 | pass |
| a11y wcag accessibility | github-accessibility-html-wcag | 1 | top 3 | pass |
| agent evals trace grading | openai-agent-trace-evals | 1 | top 3 | pass |
| agent tracing observability | openai-agent-tracing-observability | 1 | top 3 | pass |
| security guardrails tool calls | openai-tool-guardrails-appsec | 1 | top 3 | pass |
| backend api integration tests | openhands-api-integration-tests | 1 | top 3 | pass |
| mobile github issue agent | github-mobile-agent-task-handoff | 1 | top 3 | pass |
| remote agent server smoke | openhands-remote-agent-server-smoke | 1 | top 3 | pass |
| docs quickstart onboarding | docs-quickstart | 1 | top 5 | pass |
| feature flag percentage react hook | openhands-feature-flag-system | 1 | top 3 | pass |
| checkout crash root cause regression | openhands-checkout-crash-regression | 1 | top 3 | pass |
| slow query log optimization report | openhands-slow-query-optimization | 1 | top 3 | pass |
| semantic merge repair dag conflict planner | deadreckon-semantic-merge-repair | 1 | top 3 | pass |
| daily priority progress status | goal-agent-daily-priority-loop | 1 | top 3 | pass |
| sparc payment processing | claude-flow-sparc-payment-plan | 1 | top 3 | pass |
| okr measurable key results scoring guardrails | claude-recipes-okr-development | 1 | top 3 | pass |
| clinical research ai safety | clinical-research-ai-safety-boundary | 1 | top 3 | pass |
| legacy stack migration compatibility checkpoints rollback | openai-code-migration-checkpoints | 1 | top 3 | pass |
| difficult task eval driven improvement loop artifact score | openai-difficult-task-eval-loop | 1 | top 3 | pass |
| promptfoo eval suite target adapter seed cases assertions | openai-promptfoo-eval-suite | 1 | top 3 | pass |
| expo react native app expo router expo go | openai-expo-react-native-app | 1 | top 3 | pass |
| agent friendly cli companion skill command surface | openai-agent-friendly-cli-skill | 1 | top 3 | pass |
| define goal measurable evidence scope stop condition | openai-define-goal-quality-bar | 1 | top 3 | pass |
| audit friendly goal objective scope done when stop if | goal-builder-audit-friendly-template | 1 | top 3 | pass |
| copilot fleet parallel test suite subagents | github-copilot-fleet-parallel-test-suite | 1 | top 3 | pass |
| innerHTML xss unsafe rendering fix | github-copilot-xss-innerhtml-fix | 1 | top 3 | pass |
| checkout p95 latency benchmark correctness suite | halmob-checkout-p95-goal | 1 | top 3 | pass |
| voice e2e scenarios anti pattern fences goal | tecton-codex-voice-e2e-contract | 1 | top 3 | pass |
| copilot usage metrics dashboard api export reconciliation | github-copilot-usage-metrics-reconciliation | 1 | top 3 | pass |
| design tokens figma agent context layout md | layout-design-system-context-export | 1 | top 3 | pass |
| long horizon one goal roadmap state protocol phase specs | github-supergoal-artifact-backed-phase-runner | 1 | top 3 | pass |

## 维护建议

- 优先给覆盖率低的分类补充真实 source-backed 条目。
- 搜索评测要贴近用户真实输入，不要只测精确标题。
- 没有公开 URL 和证据短语时，不要把 seed 条目标成 source-backed。

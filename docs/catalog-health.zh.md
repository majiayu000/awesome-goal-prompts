# 目录健康报告

生成日期：2026-05-15

## 概览

- 条目总数：293
- 有公开来源的条目：93
- Seed 条目：200
- 分类数：32
- 搜索评测：11/11 通过
- 缺少来源摘要的 source-backed 条目：0
- 缺少来源字段的 source-backed 条目：0

## 分类覆盖率

| 分类 | 有公开来源 | 总数 | 覆盖率 |
| --- | --- | --- | --- |
| accessibility | 1 | 13 | 8% |
| ai-evals | 1 | 11 | 9% |
| ai-ops | 1 | 11 | 9% |
| backend-api | 1 | 13 | 8% |
| backend-data | 1 | 11 | 9% |
| backlog | 3 | 3 | 100% |
| cli | 1 | 1 | 100% |
| data-analytics | 1 | 11 | 9% |
| data-eng | 1 | 11 | 9% |
| design | 1 | 13 | 8% |
| devops-ci | 1 | 11 | 9% |
| devops-runtime | 1 | 11 | 9% |
| docs | 3 | 15 | 20% |
| frontend | 6 | 18 | 33% |
| goal-maintenance | 9 | 9 | 100% |
| greenfield-build | 1 | 1 | 100% |
| investigation | 2 | 2 | 100% |
| maintenance | 2 | 2 | 100% |
| migration | 8 | 8 | 100% |
| mobile | 1 | 13 | 8% |
| orchestration | 1 | 1 | 100% |
| performance | 3 | 15 | 20% |
| product | 1 | 13 | 8% |
| prompt-optimization | 3 | 3 | 100% |
| prototype | 3 | 3 | 100% |
| qa | 1 | 13 | 8% |
| refactor | 2 | 2 | 100% |
| research | 3 | 3 | 100% |
| security-appsec | 1 | 11 | 9% |
| security-ops | 1 | 11 | 9% |
| testing | 19 | 19 | 100% |
| workflow | 9 | 11 | 82% |

## 来源类型分布

| 来源类型 | 数量 |
| --- | --- |
| github-discussion | 1 |
| github-issue | 7 |
| github-pr | 3 |
| none | 200 |
| official-agent-task | 12 |
| official-goal | 17 |
| official-workflow | 5 |
| public-forum | 10 |
| third-party-project | 3 |
| third-party-review | 2 |
| third-party-tutorial | 20 |
| tool-readme | 3 |
| video-summary | 2 |
| x-post | 8 |

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

## 维护建议

- 优先给覆盖率低的分类补充真实 source-backed 条目。
- 搜索评测要贴近用户真实输入，不要只测精确标题。
- 没有公开 URL 和证据短语时，不要把 seed 条目标成 source-backed。

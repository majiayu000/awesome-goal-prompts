# Sources And Caveats

This repository is based on public documentation, source inspection notes, and community discussion. Treat undocumented community examples as inspiration, not as product contracts.

## Primary Sources

- OpenAI Codex docs, Follow a goal: https://developers.openai.com/codex/use-cases/follow-goals
- OpenAI Codex CLI slash commands: https://developers.openai.com/codex/cli/slash-commands
- OpenAI Codex changelog: https://developers.openai.com/codex/changelog
- OpenAI Codex discussion on non-interactive goals: https://github.com/openai/codex/discussions/21764
- OpenAI Codex issue on Plan mode and goal continuation: https://github.com/openai/codex/issues/20656
- OpenAI Codex issue on compaction and goal audit requirements: https://github.com/openai/codex/issues/19910
- Claude Code goal docs: https://code.claude.com/docs/en/goal
- Claude Code prompt library: https://code.claude.com/docs/en/prompt-library
- Hermes Agent persistent goals docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/goals
- OpenAI Agents SDK tracing docs: https://openai.github.io/openai-agents-python/tracing/
- OpenAI Agents SDK guardrails docs: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI agent evals docs: https://platform.openai.com/docs/guides/agent-evals
- OpenHands tutorial library: https://docs.openhands.dev/openhands/usage/get-started/tutorials
- OpenHands remote agent server docs: https://docs.openhands.dev/sdk/guides/agent-server/overview
- GitHub Copilot coding agent docs: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/assign-copilot-to-an-issue
- GitHub Copilot accessibility auditor: https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/accessibility-auditor
- Anthropic blog, Introduction to agentic coding: https://www.claude.com/blog/introduction-to-agentic-coding
- Claude Code power user tips: https://support.claude.com/en/articles/14554000-claude-code-power-user-tips

## Source-Backed Example Sources

Examples marked `source-backed` in `data/examples.json` are derived from public material that documents or demonstrates goal-style workflows. They are still rewritten as reusable task contracts instead of copied verbatim.

Every source-backed entry now carries:

- `source_name`: short label for the source
- `source_url`: public URL
- `source_type`: provenance class
- `evidence`: a short phrase from, or tightly tied to, the source
- `evidence_summary`: generated summary combining the evidence phrase, source label, source type, and verification path

Use `data/examples.json` as the source of truth for the full URL list.

## Source Types

- `official-goal`: official documentation for a goal feature.
- `official-workflow`: official documentation or blog post for a long-running coding-agent workflow.
- `official-agent-task`: official agent task example from a related coding-agent product, not necessarily `/goal`.
- `third-party-tutorial`: public tutorial or article with a concrete task or template.
- `third-party-review`: public review with a concrete tested task.
- `third-party-project`: public project page demonstrating an iterative goal workflow.
- `x-post`: public X post with a concrete goal pattern, task, or usage rule.
- `public-forum`: public Reddit, HN, Cursor forum, or similar discussion with a concrete task.
- `github-issue`, `github-pr`, `github-discussion`: public GitHub thread with a concrete goal behavior, task, or template.
- `tool-readme`: public repository README or docs with a concrete example.
- `video-summary`: public video summary page with a concrete demo task.

## Catalog Seeds

Entries with `origin: "seed"` are catalog patterns for common engineering goals. They are not presented as quotes from X, GitHub, or docs. When a seed entry is later traced to a public example, update it with `source_name`, `source_url`, and `origin: "source-backed"` instead of adding a duplicate.

## Caveats

- Codex `/goal` is experimental in the public docs at the time this catalog was created.
- Do not assume a goal works the same way across Codex, Claude Code, Hermes, Cursor, or other tools.
- Do not assume a judge or goal evaluator can run commands by itself. Write goals so the working agent exposes verification evidence in the conversation or artifacts.
- Do not rely on undocumented subcommands unless the target tool documents them.
- Community posts can be useful for patterns, but they should not be cited as authoritative behavior without verification.

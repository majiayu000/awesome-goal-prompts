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
- Hermes Agent persistent goals docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/goals
- Anthropic blog, Introduction to agentic coding: https://www.claude.com/blog/introduction-to-agentic-coding
- Claude Code power user tips: https://support.claude.com/en/articles/14554000-claude-code-power-user-tips

## Source-Backed Example Sources

Examples marked `source-backed` in `data/examples.json` are derived from public material that documents or demonstrates goal-style workflows. They are still rewritten as reusable task contracts instead of copied verbatim.

- OpenAI Codex follow-goals examples: https://developers.openai.com/codex/use-cases/follow-goals
- Claude Code goal examples: https://code.claude.com/docs/en/goal
- Hermes persistent goals examples: https://hermes-agent.nousresearch.com/docs/user-guide/features/goals
- ExplainX goal mode guide: https://explainx.ai/blog/goal-mode-ai-agents-complete-guide-2026
- Qiita goal examples and notes: https://qiita.com/y-morimatsu/items/a314e5bbfdc83616d3ae

## Catalog Seeds

Entries with `origin: "seed"` are catalog patterns for common engineering goals. They are not presented as quotes from X, GitHub, or docs. When a seed entry is later traced to a public example, update it with `source_name`, `source_url`, and `origin: "source-backed"` instead of adding a duplicate.

## Caveats

- Codex `/goal` is experimental in the public docs at the time this catalog was created.
- Do not assume a goal works the same way across Codex, Claude Code, Hermes, Cursor, or other tools.
- Do not assume a judge or goal evaluator can run commands by itself. Write goals so the working agent exposes verification evidence in the conversation or artifacts.
- Do not rely on undocumented subcommands unless the target tool documents them.
- Community posts can be useful for patterns, but they should not be cited as authoritative behavior without verification.

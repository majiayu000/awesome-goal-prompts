# Data Schema

`data/examples.json` and `docs/examples.json` contain the same generated catalog.

## Fields

- `id`: Stable slug used by links and tooling.
- `slug`: Same value as `id`.
- `category`: Browsing category used by README and the GitHub Pages catalog.
- `title`: Human-readable example title.
- `intent`: One-sentence description of the task.
- `verify`: Command, report, artifact, or evidence path that should prove completion.
- `difficulty`: `intermediate` or `advanced`.
- `origin`: `seed` or `source-backed`.
- `source_url`: Public URL for source-backed examples, otherwise `null`.
- `source_name`: Short source label for source-backed examples, otherwise `null`.
- `source_type`: Provenance class for source-backed examples, otherwise `null`.
- `evidence`: Short evidence phrase from, or tightly tied to, the source, otherwise `null`.
- `prompt`: Generated `/goal` task contract.

## Origin Rules

`source-backed` means the entry is tied to a public URL and a concrete task, example, or usage rule. It does not mean the prompt text is copied verbatim.

`seed` means the entry is a reusable catalog pattern. Do not describe seed entries as collected from X, GitHub, docs, or a named author.

## Source Types

See `SOURCES.md` for the canonical source type definitions.

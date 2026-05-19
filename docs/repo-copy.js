// Repo-specific prompt adapter. Loaded before app.js; reads app globals at click time.
// Exposes global functions: syncRepoCopyPlaceholders, buildAdaptedPrompt, copyAdaptedPrompt.

function repoCopyValue(input, fallback) {
  const value = input && input.value.trim();
  return value || fallback;
}

function repoCopyInlineCode(value) {
  return String(value).replace(/`/g, "'");
}

function syncRepoCopyPlaceholders(entry) {
  if (!entry) {
    return;
  }
  if (els.adapterModule) {
    els.adapterModule.placeholder = categoryLabel(entry.category);
  }
  if (els.adapterVerify) {
    els.adapterVerify.placeholder = entry.verify;
  }
}

function buildAdaptedPrompt(entry) {
  const projectType = repoCopyValue(els.adapterType, "the current repository");
  const targetModule = repoCopyValue(els.adapterModule, categoryLabel(entry.category));
  const verify = repoCopyInlineCode(repoCopyValue(els.adapterVerify, entry.verify));
  const extraConstraint = repoCopyValue(
    els.adapterConstraint,
    "Keep public behavior unchanged unless the goal explicitly requires it."
  );
  const sourceLine = entry.source_name && entry.source_url && isSafeHttpUrl(entry.source_url)
    ? `- Reference pattern: ${entry.source_name} (${entry.source_url}). Use it as context, not as repo truth.`
    : "- Treat the selected catalog example as a pattern; verify the real behavior in this repository.";

  return `/goal

GOAL:
In ${projectType}, complete "${entry.title}" for ${targetModule}: ${entry.intent}

CONTEXT:
- Read the nearest AGENTS.md/CLAUDE.md and the relevant project docs before editing.
- Inspect the ${targetModule} implementation, tests, configuration, and latest failing output.
${sourceLine}
- Establish a baseline with: \`${verify}\`.

CONSTRAINTS:
- Keep the scope limited to ${targetModule}; do not make unrelated refactors.
- Do not weaken, delete, or skip tests, lint, typecheck, or verification rules.
- ${extraConstraint}

DONE WHEN:
- The selected goal is satisfied: ${entry.intent}
- The verification command passes: \`${verify}\`.
- The final diff is limited to files needed for this goal.

VERIFY:
- Run \`${verify}\` or the closest repo-local equivalent.
- Run any repo-local typecheck or build command if this task touches compiled code.
- Include fresh command output in the final response.

OUTPUT:
- Root cause or implementation summary.
- Changed files.
- Verification commands and results.
- Remaining risk.

STOP RULES:
- Stop if the fix requires secrets, production access, destructive data operations, or a product/security decision.
- Stop after three failed fix attempts on the same symptom and reassess the root cause.
- Do not mark the goal complete until DONE WHEN is true in the current repository state.`;
}

async function copyAdaptedPrompt() {
  if (!state.selected) {
    return;
  }
  try {
    await navigator.clipboard.writeText(buildAdaptedPrompt(state.selected));
    setText(els.copyAdapted, t("copied"));
    showToast(t("adaptedCopied"));
    window.setTimeout(() => {
      setText(els.copyAdapted, t("copyForRepo"));
    }, 1400);
  } catch (error) {
    showToast(t("clipboardUnavailable"));
  }
}

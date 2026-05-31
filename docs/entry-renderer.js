// Contract card list renderer. Loaded after i18n.js and before app.js (see index.html).
// Exposes global function: renderResults — used by app.js applyFilters() and selectEntry().
// Reads runtime globals from app.js: state, els, padNumber, badge, categoryLabel,
// difficultyLabel, originLabel, sourceTypeLabel, selectEntry, clearAndAppend,
// staticContractUrl.
// Reads runtime globals from i18n.js: t.

function renderResults() {
  if (state.filtered.length === 0) {
    const empty = document.createElement("p");
    empty.className = "empty-list";
    empty.textContent = t("noContracts");
    clearAndAppend(els.results, [empty]);
    return;
  }

  const children = state.filtered.map((entry) => {
    const index = state.entries.findIndex((item) => item.id === entry.id) + 1;
    const staticUrl = staticContractUrl(entry);
    const link = document.createElement("a");
    link.href = staticUrl || `#${entry.slug}`;
    link.className = state.selected && state.selected.id === entry.id ? "entry active" : "entry";
    link.dataset.entryId = String(entry.id);
    if (staticUrl) {
      link.dataset.staticUrl = staticUrl;
    }
    link.setAttribute("aria-label", `${t("entryNumberPrefix")} ${padNumber(index)}: ${entry.title}`);
    link.addEventListener("click", (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.button !== 0) {
        return;
      }
      event.preventDefault();
      selectEntry(entry, true);
    });

    const no = document.createElement("span");
    no.className = "entry__no";
    no.textContent = `${t("entryNumberPrefix")} ${padNumber(index)}`;

    const content = document.createElement("span");
    content.className = "entry__content";
    const title = document.createElement("span");
    title.className = "entry__title";
    title.textContent = entry.title;
    const intent = document.createElement("span");
    intent.className = "entry__intent";
    intent.textContent = entry.intent;
    const meta = document.createElement("span");
    meta.className = "entry__meta";
    meta.appendChild(badge(categoryLabel(entry.category)));
    meta.appendChild(badge(difficultyLabel(entry.difficulty), entry.difficulty));
    meta.appendChild(badge(originLabel(entry.origin), entry.origin));
    if (entry.source_type) {
      meta.appendChild(badge(sourceTypeLabel(entry.source_type), "source-type"));
    }
    const verify = document.createElement("span");
    verify.className = "entry__verify";
    verify.textContent = entry.verify;
    content.appendChild(title);
    content.appendChild(intent);
    content.appendChild(meta);
    content.appendChild(verify);

    const action = document.createElement("span");
    action.className = "entry__action";
    action.textContent = "View";

    link.appendChild(no);
    link.appendChild(content);
    link.appendChild(action);
    return link;
  });

  clearAndAppend(els.results, children);
}

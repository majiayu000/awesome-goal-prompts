const state = {
  entries: [],
  filtered: [],
  selected: null,
  origin: "all",
};

const els = {
  total: document.querySelector("#stat-total"),
  categories: document.querySelector("#stat-categories"),
  sourced: document.querySelector("#stat-sourced"),
  search: document.querySelector("#search-input"),
  category: document.querySelector("#category-select"),
  difficulty: document.querySelector("#difficulty-select"),
  originButtons: Array.from(document.querySelectorAll("[data-origin]")),
  categoryList: document.querySelector("#category-list"),
  resultCount: document.querySelector("#result-count"),
  reset: document.querySelector("#reset-button"),
  results: document.querySelector("#results"),
  detailEmpty: document.querySelector("#detail-empty"),
  detailCard: document.querySelector("#detail-card"),
  detailMeta: document.querySelector("#detail-meta"),
  detailTitle: document.querySelector("#detail-title"),
  detailIntent: document.querySelector("#detail-intent"),
  detailVerify: document.querySelector("#detail-verify"),
  sourceRow: document.querySelector("#source-row"),
  detailSource: document.querySelector("#detail-source"),
  detailPrompt: document.querySelector("#detail-prompt"),
  copy: document.querySelector("#copy-button"),
};

function unique(values) {
  return Array.from(new Set(values)).sort((a, b) => a.localeCompare(b));
}

function countBy(items, key) {
  return items.reduce((acc, item) => {
    const value = item[key];
    acc[value] = (acc[value] || 0) + 1;
    return acc;
  }, {});
}

function createOption(value, label) {
  const option = document.createElement("option");
  option.value = value;
  option.textContent = label;
  return option;
}

function badge(text, extraClass) {
  const span = document.createElement("span");
  span.className = extraClass ? `badge ${extraClass}` : "badge";
  span.textContent = text;
  return span;
}

function setText(el, value) {
  el.textContent = value;
}

function normalize(value) {
  return String(value || "").toLowerCase();
}

function matchesSearch(entry, query) {
  if (!query) {
    return true;
  }
  const haystack = [
    entry.title,
    entry.intent,
    entry.category,
    entry.verify,
    entry.source_name,
    entry.prompt,
  ].map(normalize).join(" ");
  return haystack.includes(query);
}

function applyFilters() {
  const query = normalize(els.search.value.trim());
  const category = els.category.value;
  const difficulty = els.difficulty.value;
  const origin = state.origin;

  state.filtered = state.entries.filter((entry) => {
    return matchesSearch(entry, query)
      && (category === "all" || entry.category === category)
      && (difficulty === "all" || entry.difficulty === difficulty)
      && (origin === "all" || entry.origin === origin);
  });

  renderResults();
  renderCategoryShortcuts();

  if (!state.filtered.some((entry) => state.selected && entry.id === state.selected.id)) {
    selectEntry(state.filtered[0] || null, false);
  }
}

function renderStats() {
  const sourced = state.entries.filter((entry) => entry.origin === "source-backed").length;
  setText(els.total, String(state.entries.length));
  setText(els.categories, String(unique(state.entries.map((entry) => entry.category)).length));
  setText(els.sourced, String(sourced));
}

function renderCategorySelect() {
  els.category.replaceChildren(createOption("all", "All categories"));
  for (const category of unique(state.entries.map((entry) => entry.category))) {
    els.category.appendChild(createOption(category, category));
  }
}

function renderCategoryShortcuts() {
  const counts = countBy(state.entries, "category");
  const current = els.category.value;
  els.categoryList.replaceChildren();
  for (const category of unique(state.entries.map((entry) => entry.category))) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = current === category ? "chip active" : "chip";
    button.textContent = `${category} ${counts[category]}`;
    button.addEventListener("click", () => {
      els.category.value = category;
      applyFilters();
    });
    els.categoryList.appendChild(button);
  }
}

function renderResults() {
  setText(els.resultCount, `${state.filtered.length} matching goals`);
  els.results.replaceChildren();

  if (state.filtered.length === 0) {
    const empty = document.createElement("p");
    empty.className = "result-intent";
    empty.textContent = "No matching goals. Try a broader search.";
    els.results.appendChild(empty);
    return;
  }

  for (const entry of state.filtered) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = state.selected && state.selected.id === entry.id ? "result-card active" : "result-card";
    button.addEventListener("click", () => selectEntry(entry, true));

    const titleRow = document.createElement("div");
    titleRow.className = "result-title";
    const title = document.createElement("span");
    title.textContent = entry.title;
    titleRow.appendChild(title);
    if (entry.origin === "source-backed") {
      titleRow.appendChild(badge("source", "source-backed"));
    }

    const intent = document.createElement("p");
    intent.className = "result-intent";
    intent.textContent = entry.intent;

    const badges = document.createElement("div");
    badges.className = "badge-row";
    badges.appendChild(badge(entry.category));
    badges.appendChild(badge(entry.difficulty, entry.difficulty));
    badges.appendChild(badge(entry.origin === "source-backed" ? "source-backed" : "seed"));

    button.appendChild(titleRow);
    button.appendChild(intent);
    button.appendChild(badges);
    els.results.appendChild(button);
  }
}

function selectEntry(entry, updateHash) {
  state.selected = entry;
  renderResults();
  renderDetail();
  if (entry && updateHash) {
    history.replaceState(null, "", `#${entry.slug}`);
  }
}

function renderDetail() {
  const entry = state.selected;
  els.copy.textContent = "Copy";

  if (!entry) {
    els.detailEmpty.classList.remove("hidden");
    els.detailCard.classList.add("hidden");
    return;
  }

  els.detailEmpty.classList.add("hidden");
  els.detailCard.classList.remove("hidden");
  setText(els.detailMeta, `${entry.category} / ${entry.difficulty} / ${entry.origin}`);
  setText(els.detailTitle, entry.title);
  setText(els.detailIntent, entry.intent);
  setText(els.detailVerify, entry.verify);
  setText(els.detailPrompt, entry.prompt);

  if (entry.source_url && entry.source_name) {
    els.sourceRow.classList.remove("hidden");
    els.detailSource.href = entry.source_url;
    els.detailSource.textContent = entry.source_name;
  } else {
    els.sourceRow.classList.add("hidden");
    els.detailSource.removeAttribute("href");
    els.detailSource.textContent = "";
  }
}

function resetFilters() {
  els.search.value = "";
  els.category.value = "all";
  els.difficulty.value = "all";
  state.origin = "all";
  for (const button of els.originButtons) {
    button.classList.toggle("active", button.dataset.origin === "all");
  }
  applyFilters();
}

async function copySelected() {
  if (!state.selected) {
    return;
  }
  try {
    await navigator.clipboard.writeText(state.selected.prompt);
    els.copy.textContent = "Copied";
    window.setTimeout(() => {
      els.copy.textContent = "Copy";
    }, 1400);
  } catch (error) {
    els.copy.textContent = "Select text";
    window.setTimeout(() => {
      els.copy.textContent = "Copy";
    }, 1800);
  }
}

function bindEvents() {
  els.search.addEventListener("input", applyFilters);
  els.category.addEventListener("change", applyFilters);
  els.difficulty.addEventListener("change", applyFilters);
  els.reset.addEventListener("click", resetFilters);
  els.copy.addEventListener("click", copySelected);

  for (const button of els.originButtons) {
    button.addEventListener("click", () => {
      state.origin = button.dataset.origin;
      for (const option of els.originButtons) {
        option.classList.toggle("active", option === button);
      }
      applyFilters();
    });
  }
}

async function loadExamples() {
  try {
    const response = await fetch("examples.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Failed to load examples: ${response.status}`);
    }
    const entries = await response.json();
    state.entries = entries;
    state.filtered = entries;
    renderStats();
    renderCategorySelect();
    renderCategoryShortcuts();

    const wanted = decodeURIComponent(window.location.hash.replace("#", ""));
    const initial = entries.find((entry) => entry.slug === wanted) || entries[0] || null;
    selectEntry(initial, false);
    applyFilters();
  } catch (error) {
    setText(els.resultCount, "Failed to load examples");
    const message = document.createElement("p");
    message.className = "result-intent";
    message.textContent = error.message;
    els.results.replaceChildren(message);
  }
}

bindEvents();
loadExamples();

// Catalog SPA controller. Loaded after i18n.js and entry-renderer.js (see index.html).
// i18n state, copy dictionaries, and renderResults are defined in those sibling scripts.

const langStorageKey = "agp-lang";
const supportedLangs = ["en", "zh"];

function storedLang() {
  try {
    return window.localStorage.getItem(langStorageKey);
  } catch (error) {
    console.warn("Unable to read language preference", error);
    return "";
  }
}

function storeLang(lang) {
  try {
    window.localStorage.setItem(langStorageKey, lang);
  } catch (error) {
    console.warn("Unable to store language preference", error);
  }
}

function detectInitialLang() {
  const requested = new URLSearchParams(window.location.search).get("lang");
  if (supportedLangs.includes(requested)) {
    return requested;
  }
  const saved = storedLang();
  if (supportedLangs.includes(saved)) {
    return saved;
  }
  return normalize(navigator.language).startsWith("zh") ? "zh" : "en";
}

const state = {
  entries: [],
  recipes: [],
  filtered: [],
  selected: null,
  category: "all",
  difficulty: "all",
  origin: "source-backed",
  recipe: "all",
  lang: detectInitialLang(),
};

const els = {
  total: document.querySelector("#stat-total"),
  categories: document.querySelector("#stat-categories"),
  sourced: document.querySelector("#stat-sourced"),
  advanced: document.querySelector("#stat-advanced"),
  sealTotal: document.querySelector("#seal-total"),
  search: document.querySelector("#search-input"),
  langButtons: Array.from(document.querySelectorAll("[data-lang-option]")),
  recipeList: document.querySelector("#recipe-list"),
  recipeButtons: [],
  difficultyButtons: Array.from(document.querySelectorAll("[data-difficulty]")),
  originButtons: Array.from(document.querySelectorAll("[data-origin]")),
  categoryList: document.querySelector("#category-list"),
  categoryTitle: document.querySelector("#category-title"),
  resultCount: document.querySelector("#result-count"),
  reset: document.querySelector("#reset-button"),
  results: document.querySelector("#results"),
  detailEmpty: document.querySelector("#detail-empty"),
  detailCard: document.querySelector("#detail-card"),
  detailNumber: document.querySelector("#detail-number"),
  detailMeta: document.querySelector("#detail-meta"),
  detailTitle: document.querySelector("#detail-title"),
  detailIntent: document.querySelector("#detail-intent"),
  detailContext: document.querySelector("#detail-context"),
  detailConstraints: document.querySelector("#detail-constraints"),
  detailVerifyList: document.querySelector("#detail-verify-list"),
  detailStop: document.querySelector("#detail-stop"),
  detailDone: document.querySelector("#detail-done"),
  detailVerify: document.querySelector("#detail-verify"),
  sourceRow: document.querySelector("#source-row"),
  sourceTypeRow: document.querySelector("#source-type-row"),
  evidenceRow: document.querySelector("#evidence-row"),
  detailSource: document.querySelector("#detail-source"),
  detailSourceType: document.querySelector("#detail-source-type"),
  detailEvidence: document.querySelector("#detail-evidence"),
  detailPrompt: document.querySelector("#detail-prompt"),
  validate: document.querySelector("#validate-button"),
  copy: document.querySelector("#copy-button"),
  toast: document.querySelector("#toast"),
};

function unique(values) {
  return Array.from(new Set(values)).sort((a, b) => categoryLabel(a).localeCompare(categoryLabel(b)));
}

function countBy(items, key) {
  return items.reduce((acc, item) => {
    const value = item[key];
    acc[value] = (acc[value] || 0) + 1;
    return acc;
  }, {});
}

function normalize(value) {
  return String(value || "").toLowerCase();
}

function tokenize(value) {
  return normalize(value)
    .replace(/[^\p{L}\p{N}+.#/-]+/gu, " ")
    .split(/\s+/)
    .filter(Boolean);
}

function queryTerms(query) {
  return tokenize(query).map((token) => {
    const variants = [token, ...(queryAliases[token] || [])];
    for (const [alias, expanded] of Object.entries(queryAliases)) {
      if (/[^\x00-\x7F]/.test(alias) && token.includes(alias)) {
        variants.push(...expanded);
      }
    }
    return unique(variants);
  });
}

function searchableText(entry) {
  return [
    entry.title,
    entry.intent,
    entry.category,
    entry.difficulty,
    entry.origin,
    entry.verify,
    entry.source_name,
    entry.source_type,
    entry.evidence,
    entry.evidence_summary,
    entry.prompt,
  ].map(normalize).join(" ");
}

function termMatches(text, variants) {
  return variants.some((variant) => text.includes(variant));
}

function searchScore(entry, query) {
  if (!query) {
    return 1;
  }
  const text = searchableText(entry);
  const groups = queryTerms(query);
  if (groups.length === 0) {
    return 1;
  }
  if (!groups.every((group) => termMatches(text, group))) {
    return 0;
  }

  let score = 10;
  const title = normalize(entry.title);
  const intent = normalize(entry.intent);
  const verify = normalize(entry.verify);
  const evidence = normalize(`${entry.evidence || ""} ${entry.evidence_summary || ""}`);
  for (const group of groups) {
    if (termMatches(title, group)) score += 5;
    if (termMatches(intent, group)) score += 4;
    if (termMatches(verify, group)) score += 3;
    if (termMatches(evidence, group)) score += 2;
  }
  if (entry.origin === "source-backed") score += 3;
  if (entry.source_type === "official-goal") score += 4;
  return score;
}

function padNumber(value) {
  return String(value).padStart(3, "0");
}

function categoryLabel(category) {
  return localizedLabel("categoryLabels", category);
}

function categoryGlyph(category) {
  if (glyphs[category]) {
    return glyphs[category];
  }
  return category
    .split("-")
    .filter(Boolean)
    .map((part) => part[0])
    .join("")
    .slice(0, 3)
    .toUpperCase();
}

function originLabel(origin) {
  return localizedLabel("originLabels", origin, origin === "source-backed" ? "sourced" : origin);
}

function difficultyLabel(difficulty) {
  return localizedLabel("difficultyLabels", difficulty);
}

function sourceTypeLabel(sourceType) {
  return sourceType ? localizedLabel("sourceTypeLabels", sourceType) : "";
}

function verificationKindLabel(kind) {
  return localizedLabel("verifyKindLabels", kind, kind);
}

function setText(el, value) {
  if (el) {
    el.textContent = value;
  }
}

function clearAndAppend(el, children) {
  el.replaceChildren(...children);
}

function applyStaticCopy() {
  document.documentElement.lang = state.lang === "zh" ? "zh-CN" : "en";
  document.body.dataset.lang = state.lang;
  document.title = t("pageTitle");

  const description = document.querySelector('meta[name="description"]');
  if (description) {
    description.content = t("metaDescription");
  }

  for (const el of document.querySelectorAll("[data-i18n]")) {
    setText(el, t(el.dataset.i18n));
  }
  for (const el of document.querySelectorAll("[data-i18n-placeholder]")) {
    el.setAttribute("placeholder", t(el.dataset.i18nPlaceholder));
  }
  for (const el of document.querySelectorAll("[data-i18n-aria]")) {
    el.setAttribute("aria-label", t(el.dataset.i18nAria));
  }
  for (const button of els.langButtons) {
    const active = button.dataset.langOption === state.lang;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", active ? "true" : "false");
  }

  if (state.entries.length === 0) {
    setText(els.categoryTitle, t("allContracts"));
    setText(els.resultCount, t("loadingContracts"));
  }
}

function setLanguage(lang) {
  if (!supportedLangs.includes(lang) || lang === state.lang) {
    return;
  }
  state.lang = lang;
  storeLang(lang);
  applyStaticCopy();
  if (state.entries.length > 0) {
    renderRecipes();
    renderStats();
    applyFilters();
  }
}

function badge(text, extraClass) {
  const span = document.createElement("span");
  span.className = extraClass ? `badge ${extraClass}` : "badge";
  span.textContent = text;
  return span;
}

function showToast(message) {
  setText(els.toast, message);
  els.toast.classList.add("show");
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => {
    els.toast.classList.remove("show");
  }, 1500);
}

function extractSection(prompt, heading) {
  const pattern = new RegExp(`(?:^|\\n)${heading}:\\n([\\s\\S]*?)(?=\\n[A-Z][A-Z ]{1,24}:\\n|$)`, "i");
  const match = prompt.match(pattern);
  return match ? match[1].trim() : "";
}

function listFromSection(prompt, heading) {
  const section = extractSection(prompt, heading);
  if (!section) {
    return [];
  }
  return section
    .split(/\n+/)
    .map((line) => line.replace(/^\s*[-*]\s+/, "").trim())
    .filter(Boolean);
}

function parseDone(prompt) {
  const items = listFromSection(prompt, "DONE WHEN");
  if (items.length === 0) {
    return "";
  }
  return items.join(" ");
}

function parseVerification(prompt, fallback) {
  const items = listFromSection(prompt, "VERIFY");
  return items.length ? items : [fallback].filter(Boolean);
}

function kindForVerification(text) {
  const value = normalize(text);
  if (value.includes("metric") || value.includes("dashboard") || value.includes("honeycomb") || value.includes("grafana")) {
    return "metric";
  }
  if (value.includes("doc") || value.includes("readme") || value.includes("runbook")) {
    return "doc";
  }
  if (value.includes("rollout") || value.includes("canary") || value.includes("deploy")) {
    return "rollout";
  }
  return "test";
}

function renderPlainList(el, items, prefix = "§") {
  const children = (items.length ? items : [t("noExplicitTerms")]).map((item, index) => {
    const li = document.createElement("li");
    const bullet = document.createElement("span");
    bullet.className = "bullet";
    bullet.textContent = prefix === "!" ? "!" : `${prefix} ${index + 1}`;
    const text = document.createElement("span");
    text.textContent = item;
    li.appendChild(bullet);
    li.appendChild(text);
    return li;
  });
  clearAndAppend(el, children);
}

function renderVerifyList(el, items) {
  const children = (items.length ? items : [t("verifyFallback")]).map((item) => {
    const li = document.createElement("li");
    const kind = kindForVerification(item);
    const badgeEl = document.createElement("span");
    badgeEl.className = `kind ${kind}`;
    badgeEl.textContent = verificationKindLabel(kind);
    const text = document.createElement("span");
    text.textContent = item;
    li.appendChild(badgeEl);
    li.appendChild(text);
    return li;
  });
  clearAndAppend(el, children);
}

function matchesSearch(entry, query) {
  if (!query) {
    return true;
  }
  return searchScore(entry, query) > 0;
}

function applyFilters() {
  const query = normalize(els.search.value.trim());
  state.filtered = state.entries
    .filter((entry) => {
      return matchesSearch(entry, query)
      && (state.category === "all" || entry.category === state.category)
      && (state.difficulty === "all" || entry.difficulty === state.difficulty)
      && (state.origin === "all" || entry.origin === state.origin);
    })
    .sort((a, b) => {
      if (!query) {
        return state.entries.findIndex((entry) => entry.id === a.id) - state.entries.findIndex((entry) => entry.id === b.id);
      }
      return searchScore(b, query) - searchScore(a, query);
    });

  if (!state.filtered.some((entry) => state.selected && entry.id === state.selected.id)) {
    state.selected = state.filtered[0] || null;
  }

  renderCategoryShortcuts();
  renderResults();
  renderDetail();
  renderCatalogHeader();
}

function renderStats() {
  const sourced = state.entries.filter((entry) => entry.origin === "source-backed").length;
  const seed = state.entries.length - sourced;
  const advanced = state.entries.filter((entry) => entry.difficulty === "advanced").length;
  const categories = unique(state.entries.map((entry) => entry.category)).length;
  setText(els.total, String(sourced));
  setText(els.categories, String(categories));
  setText(els.sourced, padNumber(seed));
  setText(els.advanced, padNumber(advanced));
  setText(els.sealTotal, `${padNumber(sourced)} / ${padNumber(state.entries.length)}`);
}

function recipeLabel(recipe) {
  return state.lang === "zh" ? recipe.label_zh || recipe.label : recipe.label;
}

function renderRecipes() {
  const buttons = state.recipes.map((recipe) => {
    const button = document.createElement("button");
    button.className = recipe.id === state.recipe ? "recipe active" : "recipe";
    button.type = "button";
    button.dataset.recipe = recipe.id;
    button.textContent = recipeLabel(recipe);
    button.addEventListener("click", () => applyRecipe(recipe.id));
    return button;
  });
  clearAndAppend(els.recipeList, buttons);
  els.recipeButtons = buttons;
}

function renderCatalogHeader() {
  let label = state.category === "all" ? t("allContracts") : categoryLabel(state.category);
  if (state.category === "all" && state.origin === "source-backed") {
    label = t("sourceBackedContracts");
  } else if (state.category === "all" && state.origin === "seed") {
    label = t("seedPatterns");
  }
  setText(els.categoryTitle, label);
  setText(els.resultCount, formatContractsCount(state.filtered.length, state.entries.length));
}

function renderCategoryShortcuts() {
  const scopedEntries = state.entries.filter((entry) => {
    return (state.origin === "all" || entry.origin === state.origin)
      && (state.difficulty === "all" || entry.difficulty === state.difficulty);
  });
  const counts = countBy(scopedEntries, "category");
  const buttons = [];

  const all = document.createElement("button");
  all.type = "button";
  const allActive = state.category === "all";
  all.className = allActive ? "rail__cat active" : "rail__cat";
  all.setAttribute("aria-pressed", allActive ? "true" : "false");
  const allGlyph = document.createElement("span");
  allGlyph.className = "rail__glyph";
  allGlyph.textContent = "*";
  const allName = document.createElement("span");
  allName.className = "rail__name";
  allName.textContent = state.origin === "source-backed" ? t("sourceBackedContracts") : t("allContracts");
  if (state.origin === "seed") {
    allName.textContent = t("seedPatterns");
  }
  const allCount = document.createElement("span");
  allCount.className = "rail__count";
  allCount.textContent = String(scopedEntries.length);
  all.appendChild(allGlyph);
  all.appendChild(allName);
  all.appendChild(allCount);
  all.addEventListener("click", () => {
    setActiveRecipe("all");
    state.category = "all";
    applyFilters();
  });
  buttons.push(all);

  for (const category of unique(scopedEntries.map((entry) => entry.category))) {
    const button = document.createElement("button");
    button.type = "button";
    const active = state.category === category;
    button.className = active ? "rail__cat active" : "rail__cat";
    button.setAttribute("aria-pressed", active ? "true" : "false");

    const glyph = document.createElement("span");
    glyph.className = "rail__glyph";
    glyph.textContent = categoryGlyph(category);

    const name = document.createElement("span");
    name.className = "rail__name";
    name.textContent = categoryLabel(category);

    const count = document.createElement("span");
    count.className = "rail__count";
    count.textContent = String(counts[category]);

    button.appendChild(glyph);
    button.appendChild(name);
    button.appendChild(count);
    button.addEventListener("click", () => {
      setActiveRecipe("all");
      state.category = category;
      applyFilters();
    });
    buttons.push(button);
  }

  clearAndAppend(els.categoryList, buttons);
}

function selectEntry(entry, updateHash) {
  state.selected = entry;
  updateActiveEntryClass();
  renderDetail();
  if (entry && updateHash) {
    history.replaceState(null, "", `#${entry.slug}`);
  }
}

function updateActiveEntryClass() {
  const selectedId = state.selected ? String(state.selected.id) : null;
  for (const link of els.results.querySelectorAll(".entry")) {
    link.classList.toggle("active", link.dataset.entryId === selectedId);
  }
}

function isSafeHttpUrl(value) {
  if (typeof value !== "string") {
    return false;
  }
  try {
    const url = new URL(value, window.location.href);
    return url.protocol === "https:" || url.protocol === "http:";
  } catch (_) {
    return false;
  }
}

function renderDetail() {
  const entry = state.selected;
  setText(els.copy, t("copyOriginal"));

  for (const details of els.detailCard.querySelectorAll("details")) {
    details.open = false;
  }

  if (!entry) {
    els.detailEmpty.classList.remove("hidden");
    els.detailCard.classList.add("hidden");
    return;
  }

  const index = state.entries.findIndex((item) => item.id === entry.id) + 1;
  const context = listFromSection(entry.prompt, "CONTEXT");
  const constraints = listFromSection(entry.prompt, "CONSTRAINTS");
  const verify = parseVerification(entry.prompt, entry.verify);
  const stopRules = listFromSection(entry.prompt, "STOP RULES");
  const done = parseDone(entry.prompt) || entry.intent;

  els.detailEmpty.classList.add("hidden");
  els.detailCard.classList.remove("hidden");
  setText(els.detailNumber, padNumber(index));
  const sourceType = entry.source_type ? ` · ${sourceTypeLabel(entry.source_type)}` : "";
  setText(els.detailMeta, `${categoryLabel(entry.category)} · ${difficultyLabel(entry.difficulty)} · ${originLabel(entry.origin)}${sourceType}`);
  setText(els.detailTitle, entry.title);
  setText(els.detailIntent, entry.intent);
  setText(els.detailDone, done);
  setText(els.detailVerify, entry.verify);
  setText(els.detailPrompt, entry.prompt);
  renderPlainList(els.detailContext, context, "§");
  renderPlainList(els.detailConstraints, constraints, "§");
  renderVerifyList(els.detailVerifyList, verify);
  renderPlainList(els.detailStop, stopRules, "!");

  if (entry.source_url && entry.source_name && isSafeHttpUrl(entry.source_url)) {
    els.sourceRow.classList.remove("hidden");
    els.detailSource.href = entry.source_url;
    els.detailSource.textContent = entry.source_name;
  } else {
    els.sourceRow.classList.add("hidden");
    els.detailSource.removeAttribute("href");
    els.detailSource.textContent = "";
  }

  if (entry.source_type) {
    els.sourceTypeRow.classList.remove("hidden");
    els.detailSourceType.textContent = sourceTypeLabel(entry.source_type);
  } else {
    els.sourceTypeRow.classList.add("hidden");
    els.detailSourceType.textContent = "";
  }

  const evidenceText = entry.evidence_summary || entry.evidence;
  if (evidenceText) {
    els.evidenceRow.classList.remove("hidden");
    els.detailEvidence.textContent = evidenceText;
  } else {
    els.evidenceRow.classList.add("hidden");
    els.detailEvidence.textContent = "";
  }
}

function setActiveButtons(buttons, activeValue, dataKey) {
  for (const button of buttons) {
    const active = button.dataset[dataKey] === activeValue;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", active ? "true" : "false");
  }
}

function setActiveRecipe(recipe) {
  state.recipe = recipe;
  setActiveButtons(els.recipeButtons, recipe, "recipe");
}

function resetFilters() {
  els.search.value = "";
  state.category = "all";
  state.difficulty = "all";
  state.origin = "source-backed";
  setActiveRecipe("all");
  setActiveButtons(els.difficultyButtons, "all", "difficulty");
  setActiveButtons(els.originButtons, state.origin, "origin");
  applyFilters();
}

async function copySelected() {
  if (!state.selected) {
    return;
  }
  try {
    await navigator.clipboard.writeText(state.selected.prompt);
    setText(els.copy, t("copied"));
    showToast(t("contractCopied"));
    window.setTimeout(() => {
      setText(els.copy, t("copyOriginal"));
    }, 1400);
  } catch (error) {
    setText(els.copy, t("selectText"));
    showToast(t("clipboardUnavailable"));
    window.setTimeout(() => {
      setText(els.copy, t("copyOriginal"));
    }, 1800);
  }
}

function copyVerify() {
  if (!state.selected) {
    return;
  }
  navigator.clipboard.writeText(state.selected.verify)
    .then(() => showToast(t("verifyCopied")))
    .catch(() => showToast(t("selectVerifyText")));
}

function applyRecipe(recipe) {
  setActiveRecipe(recipe);
  if (recipe === "all") {
    resetFilters();
    return;
  }
  const config = state.recipes.find((item) => item.id === recipe);
  if (!config) {
    return;
  }
  els.search.value = config.query;
  state.category = config.category || "all";
  state.origin = config.origin || "all";
  state.difficulty = "all";
  setActiveButtons(els.difficultyButtons, state.difficulty, "difficulty");
  setActiveButtons(els.originButtons, state.origin, "origin");
  applyFilters();
}

function bindEvents() {
  let searchTimer = null;
  let composing = false;
  const runSearch = () => {
    setActiveRecipe("all");
    applyFilters();
  };
  els.search.addEventListener("compositionstart", () => {
    composing = true;
  });
  els.search.addEventListener("compositionend", () => {
    composing = false;
    runSearch();
  });
  els.search.addEventListener("input", () => {
    if (composing) {
      return;
    }
    window.clearTimeout(searchTimer);
    searchTimer = window.setTimeout(runSearch, 200);
  });
  els.reset.addEventListener("click", resetFilters);
  els.copy.addEventListener("click", copySelected);
  els.validate.addEventListener("click", copyVerify);

  for (const button of els.langButtons) {
    button.addEventListener("click", () => setLanguage(button.dataset.langOption));
  }

  for (const button of els.difficultyButtons) {
    button.addEventListener("click", () => {
      setActiveRecipe("all");
      state.difficulty = button.dataset.difficulty;
      setActiveButtons(els.difficultyButtons, state.difficulty, "difficulty");
      applyFilters();
    });
  }

  for (const button of els.originButtons) {
    button.addEventListener("click", () => {
      setActiveRecipe("all");
      state.origin = button.dataset.origin;
      setActiveButtons(els.originButtons, state.origin, "origin");
      applyFilters();
    });
  }
}

async function loadExamples() {
  try {
    const [examplesResponse, recipesResponse] = await Promise.all([
      fetch("examples.json"),
      fetch("recipes.json"),
    ]);
    if (!examplesResponse.ok) {
      throw new Error(`Failed to load examples: ${examplesResponse.status}`);
    }
    if (!recipesResponse.ok) {
      throw new Error(`Failed to load recipes: ${recipesResponse.status}`);
    }
    const entries = await examplesResponse.json();
    const recipes = await recipesResponse.json();
    state.entries = entries;
    state.recipes = recipes;
    state.filtered = entries;
    renderRecipes();
    renderStats();

    const wanted = decodeURIComponent(window.location.hash.replace("#", ""));
    const linkedEntry = entries.find((entry) => entry.slug === wanted);
    if (linkedEntry) {
      state.origin = linkedEntry.origin;
      setActiveButtons(els.originButtons, state.origin, "origin");
    }
    state.selected = linkedEntry || entries.find((entry) => entry.origin === state.origin) || entries[0] || null;
    applyFilters();
  } catch (error) {
    setText(els.resultCount, t("loadContractsFailed"));
    const message = document.createElement("p");
    message.className = "empty-list";
    message.textContent = `${t("loadContractsFailed")}: ${error.message}`;
    clearAndAppend(els.results, [message]);
  }
}

bindEvents();
applyStaticCopy();
loadExamples();

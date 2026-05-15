const langStorageKey = "agp-lang";
const supportedLangs = ["en", "zh"];

const docs = [
  {
    id: "how-to-write",
    glyph: "01",
    path: "how-to-write-goals.md",
    title: "How To Write A Good /goal",
    title_zh: "如何写好 /goal",
    summary: "A practical guide to turning a request into a verifiable task contract.",
    summary_zh: "把请求写成可验证任务契约的实用指南。",
  },
  {
    id: "launch-kit",
    glyph: "02",
    path: "launch-kit.md",
    title: "Launch Kit",
    title_zh: "发布素材包",
    summary: "Prepared launch copy, screenshots, posts, and checklist.",
    summary_zh: "发布文案、截图、帖子草稿和检查清单。",
  },
  {
    id: "schema",
    glyph: "03",
    path: "schema.md",
    title: "Data Schema",
    title_zh: "数据结构",
    summary: "Catalog fields, provenance rules, recipe fields, and search eval fields.",
    summary_zh: "目录字段、来源规则、recipe 字段和搜索评测字段。",
  },
  {
    id: "catalog-health",
    glyph: "04",
    path: "catalog-health.md",
    title: "Catalog Health",
    title_zh: "目录健康报告",
    summary: "Generated coverage, provenance, and search evaluation status.",
    summary_zh: "生成的覆盖率、来源和搜索评测状态。",
  },
];

const copy = {
  en: {
    pageTitle: "Docs · The Contract Codex",
    metaDescription: "The Contract Codex documentation: goal writing guide, launch kit, data schema, and catalog health.",
    homeAria: "The Contract Codex home",
    repoLinksAria: "Repository links",
    languageAria: "Language",
    brandName: "The Contract Codex",
    brandSub: "V1 · Awesome Goal Prompts",
    navCatalog: "Catalog",
    navWrite: "Write /goal",
    navDocs: "Docs",
    navSources: "Sources",
    navContribute: "Contribute",
    navGithub: "GitHub",
    docsEyebrow: "§ Documents · Local archive",
    docsTitle: "Read the docs without leaving the catalog.",
    docsCopy: "The guide, launch kit, schema, and health report are rendered from this repository's Pages files. No GitHub blob redirect, no raw markdown detour.",
    docsStatsAria: "Documentation statistics",
    docsLedgerGuides: "Guides",
    docsLedgerSource: "Source",
    docsLedgerRoute: "Route",
    docsBrowserAria: "Documentation browser",
    docsIndexAria: "Documentation index",
    docsShelfEyebrow: "§ II · Docs",
    docsShelfTitle: "Document Index",
    docsLoading: "Loading document...",
    docsFailed: "Unable to load this document.",
    docsSourceNote: "Rendered from Pages markdown",
    footerText: "The Contract Codex · MIT License · 2026",
    footerBack: "Back to catalog",
  },
  zh: {
    pageTitle: "文档 · 契约典籍",
    metaDescription: "契约典籍文档：goal 写作指南、发布素材包、数据结构和目录健康报告。",
    homeAria: "契约典籍首页",
    repoLinksAria: "仓库链接",
    languageAria: "语言",
    brandName: "契约典籍",
    brandSub: "V1 · Awesome Goal Prompts",
    navCatalog: "目录",
    navWrite: "写好 /goal",
    navDocs: "文档",
    navSources: "来源",
    navContribute: "贡献",
    navGithub: "GitHub",
    docsEyebrow: "§ 文档 · 站内档案",
    docsTitle: "不离开目录，也能阅读文档。",
    docsCopy: "指南、发布素材包、数据结构和健康报告都从本站 Pages 文件渲染。不跳 GitHub blob，也不展示 raw markdown。",
    docsStatsAria: "文档统计",
    docsLedgerGuides: "文档",
    docsLedgerSource: "来源",
    docsLedgerRoute: "路由",
    docsBrowserAria: "文档浏览器",
    docsIndexAria: "文档索引",
    docsShelfEyebrow: "§ II · 文档",
    docsShelfTitle: "文档索引",
    docsLoading: "正在载入文档...",
    docsFailed: "无法载入这份文档。",
    docsSourceNote: "由 Pages markdown 渲染",
    footerText: "契约典籍 · MIT License · 2026",
    footerBack: "返回目录",
  },
};

const state = {
  lang: detectInitialLang(),
  current: "",
  cache: new Map(),
};

const els = {
  count: document.querySelector("#docs-count"),
  list: document.querySelector("#doc-list"),
  kicker: document.querySelector("#doc-kicker"),
  title: document.querySelector("#doc-title"),
  summary: document.querySelector("#doc-summary"),
  content: document.querySelector("#doc-content"),
  langButtons: Array.from(document.querySelectorAll("[data-lang-option]")),
};

function normalize(value) {
  return String(value || "").toLowerCase();
}

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

function activeCopy() {
  return copy[state.lang] || copy.en;
}

function t(key) {
  return activeCopy()[key] || copy.en[key] || key;
}

function docTitle(doc) {
  return state.lang === "zh" ? doc.title_zh || doc.title : doc.title;
}

function docSummary(doc) {
  return state.lang === "zh" ? doc.summary_zh || doc.summary : doc.summary;
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
  for (const el of document.querySelectorAll("[data-i18n-aria]")) {
    el.setAttribute("aria-label", t(el.dataset.i18nAria));
  }
  for (const button of els.langButtons) {
    const active = button.dataset.langOption === state.lang;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", active ? "true" : "false");
  }
  setText(els.count, String(docs.length));
}

function setLanguage(lang) {
  if (!supportedLangs.includes(lang) || lang === state.lang) {
    return;
  }
  state.lang = lang;
  storeLang(lang);
  applyStaticCopy();
  renderDocList();
  updateDocumentMeta(activeDoc());
}

function slugify(value) {
  return normalize(value)
    .replace(/`/g, "")
    .replace(/[^\p{L}\p{N}]+/gu, "-")
    .replace(/^-+|-+$/g, "") || "section";
}

function activeDoc() {
  return docs.find((doc) => doc.id === state.current) || docs[0];
}

function getRequestedDoc() {
  const hash = decodeURIComponent(window.location.hash.replace("#", ""));
  return docs.find((doc) => doc.id === hash) || docs[0];
}

function renderDocList() {
  const buttons = docs.map((doc) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = doc.id === state.current ? "doc-link active" : "doc-link";
    button.dataset.doc = doc.id;

    const glyph = document.createElement("span");
    glyph.className = "doc-link__glyph";
    glyph.textContent = doc.glyph;

    const content = document.createElement("span");
    const title = document.createElement("strong");
    title.textContent = docTitle(doc);
    const summary = document.createElement("small");
    summary.textContent = docSummary(doc);
    content.appendChild(title);
    content.appendChild(summary);

    button.appendChild(glyph);
    button.appendChild(content);
    button.addEventListener("click", () => selectDoc(doc.id, true));
    return button;
  });
  clearAndAppend(els.list, buttons);
}

function updateDocumentMeta(doc) {
  setText(els.kicker, `${t("docsSourceNote")} · ${doc.path}`);
  setText(els.title, docTitle(doc));
  setText(els.summary, docSummary(doc));
}

async function selectDoc(id, updateHash) {
  const doc = docs.find((item) => item.id === id) || docs[0];
  state.current = doc.id;
  renderDocList();
  updateDocumentMeta(doc);
  if (updateHash) {
    history.replaceState(null, "", `#${doc.id}`);
  }

  setText(els.content, t("docsLoading"));
  els.content.classList.add("is-loading");

  try {
    const markdown = await loadMarkdown(doc);
    els.content.classList.remove("is-loading");
    clearAndAppend(els.content, [renderMarkdown(markdown)]);
  } catch (error) {
    els.content.classList.remove("is-loading");
    const message = document.createElement("p");
    message.className = "doc-error";
    message.textContent = `${t("docsFailed")} ${error.message}`;
    clearAndAppend(els.content, [message]);
  }
}

async function loadMarkdown(doc) {
  if (state.cache.has(doc.path)) {
    return state.cache.get(doc.path);
  }
  const response = await fetch(doc.path, { cache: "no-store" });
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  const markdown = await response.text();
  state.cache.set(doc.path, markdown);
  return markdown;
}

function renderMarkdown(markdown) {
  const fragment = document.createDocumentFragment();
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  let index = 0;
  if (/^#\s+/.test(lines[0] || "")) {
    index = 1;
  }

  while (index < lines.length) {
    const line = lines[index];
    if (!line.trim()) {
      index += 1;
      continue;
    }

    if (/^```/.test(line)) {
      const result = parseCodeBlock(lines, index);
      fragment.appendChild(result.node);
      index = result.next;
      continue;
    }

    if (/^\s*\|/.test(line) && isTableSeparator(lines[index + 1] || "")) {
      const result = parseTable(lines, index);
      fragment.appendChild(result.node);
      index = result.next;
      continue;
    }

    const heading = line.match(/^(#{1,4})\s+(.+)$/);
    if (heading) {
      const level = Math.min(heading[1].length + 1, 5);
      const el = document.createElement(`h${level}`);
      el.id = slugify(heading[2]);
      appendInline(el, heading[2]);
      fragment.appendChild(el);
      index += 1;
      continue;
    }

    if (/^\s*[-*]\s+/.test(line)) {
      const result = parseList(lines, index, "ul", /^\s*[-*]\s+(.+)$/);
      fragment.appendChild(result.node);
      index = result.next;
      continue;
    }

    if (/^\s*\d+\.\s+/.test(line)) {
      const result = parseList(lines, index, "ol", /^\s*\d+\.\s+(.+)$/);
      fragment.appendChild(result.node);
      index = result.next;
      continue;
    }

    if (/^\s*>\s?/.test(line)) {
      const quote = document.createElement("blockquote");
      appendInline(quote, line.replace(/^\s*>\s?/, ""));
      fragment.appendChild(quote);
      index += 1;
      continue;
    }

    const result = parseParagraph(lines, index);
    fragment.appendChild(result.node);
    index = result.next;
  }

  return fragment;
}

function parseCodeBlock(lines, start) {
  const language = lines[start].replace(/^```/, "").trim();
  const codeLines = [];
  let index = start + 1;
  while (index < lines.length && !/^```/.test(lines[index])) {
    codeLines.push(lines[index]);
    index += 1;
  }

  const pre = document.createElement("pre");
  const code = document.createElement("code");
  if (language) {
    code.dataset.language = language;
  }
  code.textContent = codeLines.join("\n");
  pre.appendChild(code);
  return { node: pre, next: Math.min(index + 1, lines.length) };
}

function isTableSeparator(line) {
  return /^\s*\|?[\s:|-]+\|[\s:|-]+\|?\s*$/.test(line) && line.includes("-");
}

function splitTableRow(line) {
  return line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((cell) => cell.trim());
}

function parseTable(lines, start) {
  const table = document.createElement("table");
  const thead = document.createElement("thead");
  const tbody = document.createElement("tbody");
  const headers = splitTableRow(lines[start]);
  const headerRow = document.createElement("tr");
  for (const header of headers) {
    const th = document.createElement("th");
    appendInline(th, header);
    headerRow.appendChild(th);
  }
  thead.appendChild(headerRow);

  let index = start + 2;
  while (index < lines.length && /^\s*\|/.test(lines[index])) {
    const row = document.createElement("tr");
    for (const cell of splitTableRow(lines[index])) {
      const td = document.createElement("td");
      appendInline(td, cell);
      row.appendChild(td);
    }
    tbody.appendChild(row);
    index += 1;
  }

  table.appendChild(thead);
  table.appendChild(tbody);
  return { node: table, next: index };
}

function parseList(lines, start, type, pattern) {
  const list = document.createElement(type);
  let index = start;
  while (index < lines.length) {
    const match = lines[index].match(pattern);
    if (!match) {
      break;
    }
    const li = document.createElement("li");
    appendInline(li, match[1]);
    list.appendChild(li);
    index += 1;
  }
  return { node: list, next: index };
}

function parseParagraph(lines, start) {
  const parts = [];
  let index = start;
  while (index < lines.length && lines[index].trim()) {
    const line = lines[index];
    if (
      /^```/.test(line)
      || /^(#{1,4})\s+/.test(line)
      || /^\s*[-*]\s+/.test(line)
      || /^\s*\d+\.\s+/.test(line)
      || (/^\s*\|/.test(line) && isTableSeparator(lines[index + 1] || ""))
    ) {
      break;
    }
    parts.push(line.trim());
    index += 1;
  }

  const paragraph = document.createElement("p");
  appendInline(paragraph, parts.join(" "));
  return { node: paragraph, next: index };
}

function appendInline(parent, text) {
  const codePattern = /`([^`]+)`/g;
  let last = 0;
  let match = codePattern.exec(text);
  while (match) {
    appendRichText(parent, text.slice(last, match.index));
    const code = document.createElement("code");
    code.textContent = match[1];
    parent.appendChild(code);
    last = match.index + match[0].length;
    match = codePattern.exec(text);
  }
  appendRichText(parent, text.slice(last));
}

function appendRichText(parent, text) {
  const pattern = /(\*\*([^*]+)\*\*)|\[([^\]]+)\]\(([^)]+)\)/g;
  let last = 0;
  let match = pattern.exec(text);
  while (match) {
    appendPlainText(parent, text.slice(last, match.index));
    if (match[2]) {
      const strong = document.createElement("strong");
      strong.textContent = match[2];
      parent.appendChild(strong);
    } else {
      const link = document.createElement("a");
      link.href = match[4];
      link.textContent = match[3];
      if (/^https?:\/\//.test(match[4])) {
        link.target = "_blank";
        link.rel = "noreferrer";
      }
      parent.appendChild(link);
    }
    last = match.index + match[0].length;
    match = pattern.exec(text);
  }
  appendPlainText(parent, text.slice(last));
}

function appendPlainText(parent, text) {
  const urlPattern = /(https?:\/\/[^\s)]+)/g;
  let last = 0;
  let match = urlPattern.exec(text);
  while (match) {
    parent.appendChild(document.createTextNode(text.slice(last, match.index)));
    const link = document.createElement("a");
    link.href = match[1];
    link.textContent = match[1];
    link.target = "_blank";
    link.rel = "noreferrer";
    parent.appendChild(link);
    last = match.index + match[0].length;
    match = urlPattern.exec(text);
  }
  parent.appendChild(document.createTextNode(text.slice(last)));
}

function bindEvents() {
  for (const button of els.langButtons) {
    button.addEventListener("click", () => setLanguage(button.dataset.langOption));
  }
  window.addEventListener("hashchange", () => selectDoc(getRequestedDoc().id, false));
}

bindEvents();
applyStaticCopy();
state.current = getRequestedDoc().id;
renderDocList();
selectDoc(state.current, false);

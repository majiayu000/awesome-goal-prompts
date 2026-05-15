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
  origin: "all",
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
  adapterType: document.querySelector("#adapter-type"),
  adapterModule: document.querySelector("#adapter-module"),
  adapterVerify: document.querySelector("#adapter-verify"),
  adapterConstraint: document.querySelector("#adapter-constraint"),
  copyAdapted: document.querySelector("#copy-adapted-button"),
  validate: document.querySelector("#validate-button"),
  copy: document.querySelector("#copy-button"),
  toast: document.querySelector("#toast"),
};

const copy = {
  en: {
    pageTitle: "The Contract Codex · Awesome Goal Prompts",
    metaDescription: "The Contract Codex: a searchable catalog of runnable /goal task contracts for coding agents.",
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
    heroEyebrow: "A catalog of runnable task contracts · founded 2026",
    heroTitleLead: "Goals are not ",
    heroTitleStrike: "vibes.",
    heroTitleBridge: " They are ",
    heroTitleEm: "contracts.",
    heroManifesto: "One goal. Enough context to inspect. Explicit constraints. Verifiable completion. Stop rules for uncertainty and risk. Browse production-grade task contracts before your coding agent starts editing, then copy the prompt into Codex, Claude Code, Hermes, or another agent.",
    goalStructureAria: "Goal prompt structure",
    flowObjective: "Goal",
    flowContext: "Context",
    flowConstraints: "Constraints",
    flowVerify: "Verify",
    flowStopRules: "Stop rules",
    catalogStatsAria: "Catalog statistics",
    sealWord: "Codex",
    statContracts: "Contracts",
    statCategories: "Categories",
    statExternalSources: "External Sources",
    statAdvanced: "Advanced",
    guideEyebrow: "§ Manual · How to write",
    guideTitle: "Turn a request into a contract before the agent edits.",
    guideCopy: "A strong goal has one finish line, real repo context, hard boundaries, fresh verification, and an escape hatch. Community X posts are useful for patterns, but official docs and repository evidence define what a tool can actually do.",
    guideLink: "Read the full tutorial",
    goalChecklistAria: "Goal writing checklist",
    stepOutcomeTitle: "Goal",
    stepOutcomeCopy: "Write one measurable goal. Replace \"fix everything\" with a concrete behavior, artifact, score, or passing command.",
    stepContextTitle: "Context",
    stepContextCopy: "Name the files, issues, logs, screenshots, plans, and repo rules the agent must inspect before changing code.",
    stepConstraintsTitle: "Constraints",
    stepConstraintsCopy: "Say what must not change: public APIs, data shape, auth behavior, tests, visual output, or deployment scope.",
    stepProofTitle: "Proof",
    stepProofCopy: "Define DONE WHEN and VERIFY with commands, reports, screenshots, or generated artifacts from the current run.",
    stepStopTitle: "Stop",
    stepStopCopy: "Tell the agent when to stop: missing secrets, production access, destructive operations, unclear decisions, or repeated failed fixes.",
    catalogFiltersAria: "Catalog filters",
    searchPlaceholder: "Search: auth lint, tests fail, migration...",
    difficultyFilterAria: "Difficulty filter",
    difficultyLabel: "Difficulty",
    all: "All",
    intermediate: "Intermediate",
    advanced: "Advanced",
    originFilterAria: "Origin filter",
    originLabel: "Origin",
    seed: "Seed",
    sourced: "Sourced",
    reset: "Reset",
    recipesAria: "Start here scenarios",
    startHere: "Start here",
    recipeAll: "All contracts",
    recipeAuth: "Auth tests + lint red",
    recipeMigration: "Migration with compatibility proof",
    recipeSecurity: "Security audit",
    recipeDocs: "Docs and onboarding",
    browserAria: "Goal prompt browser",
    categoryShelfAria: "Category shelf",
    shelfEyebrow: "§ I · Shelf",
    categoryIndex: "Category Index",
    matchingContractsAria: "Matching contracts",
    contractAwaiting: "§ Contract · Awaiting Signature",
    selectedContractAria: "Selected goal contract",
    selectContract: "Select a contract to inspect its terms.",
    contractIssued: "Contract · Issued",
    verifyButton: "Verify",
    copyGoal: "Copy /goal",
    contractNumberLabel: "No.",
    translationNote: "Prompt source text is preserved in English.",
    objective: "Goal",
    context: "Context",
    constraints: "Constraints",
    verification: "Verification",
    stopRules: "Stop Rules",
    doneWhen: "Done When",
    verifyTerm: "Verify",
    source: "Source",
    sourceType: "Source Type",
    evidence: "Evidence",
    fullPrompt: "Full prompt",
    adaptPrompt: "Adapt this prompt",
    projectType: "Project type",
    targetModule: "Target module",
    verificationCommand: "Verification command",
    extraConstraint: "Extra constraint",
    projectTypePlaceholder: "Node/TypeScript repo",
    targetModulePlaceholder: "auth module",
    verificationCommandPlaceholder: "npm test -- test/auth && npm run lint",
    extraConstraintPlaceholder: "Public API must remain unchanged",
    copyAdapted: "Copy adapted /goal",
    designedFor: "Designed for Codex · Claude Code · Hermes",
    footerText: "The Contract Codex · MIT License · 2026",
    allContracts: "All Contracts",
    loadingContracts: "Loading contracts...",
    noContracts: "No contracts match the current search.",
    noExplicitTerms: "No explicit terms were supplied in this section.",
    verifyFallback: "Run the closest repo-local verification and capture evidence.",
    contractCopied: "Contract copied",
    adaptedCopied: "Adapted contract copied",
    clipboardUnavailable: "Clipboard unavailable",
    verifyCopied: "Verify command copied",
    selectVerifyText: "Select verify text",
    loadContractsFailed: "Failed to load contracts",
    copied: "Copied",
    selectText: "Select text",
    entryNumberPrefix: "No.",
    contractsCount: (filtered, total) => `${filtered} / ${total} contracts`,
    categoryLabels: {
      "accessibility": "Accessibility",
      "ai-evals": "AI · Evals",
      "ai-ops": "AI · Ops",
      "backend-api": "Backend · API",
      "backend-data": "Backend · Data",
      "backlog": "Backlog",
      "cli": "CLI",
      "data-analytics": "Data · Analytics",
      "data-eng": "Data · Engineering",
      "design": "Design",
      "devops-ci": "DevOps · CI",
      "devops-runtime": "DevOps · Runtime",
      "docs": "Docs",
      "frontend": "Frontend",
      "goal-maintenance": "Goal Maintenance",
      "greenfield-build": "Greenfield Build",
      "investigation": "Investigation",
      "maintenance": "Maintenance",
      "migration": "Migration",
      "mobile": "Mobile",
      "orchestration": "Orchestration",
      "performance": "Performance",
      "product": "Product",
      "prompt-optimization": "Prompt Optimization",
      "prototype": "Prototype",
      "qa": "QA",
      "refactor": "Refactor",
      "research": "Research",
      "security-appsec": "Security · AppSec",
      "security-ops": "Security · Ops",
      "testing": "Testing",
      "workflow": "Workflow",
    },
    difficultyLabels: {
      advanced: "Advanced",
      intermediate: "Intermediate",
    },
    originLabels: {
      all: "All",
      seed: "Seed",
      "source-backed": "Sourced",
    },
    sourceTypeLabels: {
      "github-discussion": "GitHub Discussion",
      "github-issue": "GitHub Issue",
      "github-pr": "GitHub PR",
      "official-agent-task": "Official Agent Task",
      "official-goal": "Official /goal",
      "official-workflow": "Official Workflow",
      "public-forum": "Public Forum",
      "third-party-project": "Third-party Project",
      "third-party-review": "Third-party Review",
      "third-party-tutorial": "Third-party Tutorial",
      "tool-readme": "Tool README",
      "video-summary": "Video Summary",
      "x-post": "X Post",
    },
    verifyKindLabels: {
      test: "test",
      metric: "metric",
      doc: "doc",
      rollout: "rollout",
    },
  },
  zh: {
    pageTitle: "契约典籍 · Awesome Goal Prompts",
    metaDescription: "可检索的 /goal 任务契约目录，面向 Codex、Claude Code、Hermes 等编程智能体。",
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
    heroEyebrow: "可运行任务契约档案集 · 2026 创立",
    heroTitleLead: "goal 不是",
    heroTitleStrike: "愿望，",
    heroTitleBridge: "而是",
    heroTitleEm: "契约。",
    heroManifesto: "一个 goal。足够审视的上下文。明确的约束。可验证的完成条件。面对不确定性与风险的停止规则。浏览这些为编程智能体精选的生产级任务契约，在它开始编辑前先审视，然后复制到 Codex、Claude Code、Hermes 或其他智能体。",
    goalStructureAria: "goal prompt 结构",
    flowObjective: "goal",
    flowContext: "上下文",
    flowConstraints: "约束",
    flowVerify: "验证",
    flowStopRules: "停止规则",
    catalogStatsAria: "目录统计",
    sealWord: "Codex",
    statContracts: "契约总数",
    statCategories: "分类",
    statExternalSources: "外部来源",
    statAdvanced: "高阶级别",
    guideEyebrow: "§ 手册 · 如何写",
    guideTitle: "在智能体编辑前，先把请求写成契约。",
    guideCopy: "强 goal 只有一个终点、真实仓库上下文、硬边界、当前轮验证和退出条件。社区 X 帖适合看模式，但官方文档和仓库证据才决定工具实际能做什么。",
    guideLink: "阅读完整教程",
    goalChecklistAria: "goal 写作检查清单",
    stepOutcomeTitle: "goal",
    stepOutcomeCopy: "写一个可衡量的 goal。把“全部修好”换成具体行为、产物、分数或通过的命令。",
    stepContextTitle: "上下文",
    stepContextCopy: "点名智能体改代码前必须查看的文件、issue、日志、截图、计划和仓库规则。",
    stepConstraintsTitle: "约束",
    stepConstraintsCopy: "说清哪些不能变：公开 API、数据结构、鉴权行为、测试、视觉输出或部署范围。",
    stepProofTitle: "证明",
    stepProofCopy: "用本轮命令、报告、截图或生成产物定义 DONE WHEN 和 VERIFY。",
    stepStopTitle: "停止",
    stepStopCopy: "告诉智能体何时停下：缺少密钥、需要生产权限、破坏性操作、决策不清或同一问题反复失败。",
    catalogFiltersAria: "目录筛选",
    searchPlaceholder: "检索：鉴权 lint、测试失败、迁移...",
    difficultyFilterAria: "难度筛选",
    difficultyLabel: "难度",
    all: "全部",
    intermediate: "中阶",
    advanced: "高阶",
    originFilterAria: "来源筛选",
    originLabel: "来源",
    seed: "原生",
    sourced: "外部",
    reset: "重置",
    recipesAria: "快速场景",
    startHere: "从这里开始",
    recipeAll: "全部契约",
    recipeAuth: "鉴权测试 + lint 红灯",
    recipeMigration: "带兼容性证明的迁移",
    recipeSecurity: "安全审计",
    recipeDocs: "文档与上手",
    browserAria: "goal prompt 浏览器",
    categoryShelfAria: "分类书架",
    shelfEyebrow: "§ I · 书架",
    categoryIndex: "分类目录",
    matchingContractsAria: "匹配契约",
    contractAwaiting: "§ 契约 · 待签发",
    selectedContractAria: "已选 goal 契约",
    selectContract: "选择一条契约以审视条款。",
    contractIssued: "契约 · 已签发",
    verifyButton: "验证",
    copyGoal: "复制 /goal",
    contractNumberLabel: "编号",
    translationNote: "条目标题、说明和提示词正文保留英文源文。",
    objective: "goal",
    context: "上下文",
    constraints: "约束",
    verification: "验证",
    stopRules: "停止规则",
    doneWhen: "完成条件",
    verifyTerm: "验证",
    source: "来源",
    sourceType: "来源类型",
    evidence: "证据",
    fullPrompt: "完整提示词",
    adaptPrompt: "改写这条提示词",
    projectType: "项目类型",
    targetModule: "模块/路径",
    verificationCommand: "验证命令",
    extraConstraint: "额外约束",
    projectTypePlaceholder: "Node/TypeScript 仓库",
    targetModulePlaceholder: "鉴权模块",
    verificationCommandPlaceholder: "npm test -- test/auth && npm run lint",
    extraConstraintPlaceholder: "公开 API 必须保持不变",
    copyAdapted: "复制改写后的 /goal",
    designedFor: "适用于 Codex · Claude Code · Hermes",
    footerText: "契约典籍 · MIT License · 2026",
    allContracts: "全部契约",
    loadingContracts: "正在载入契约...",
    noContracts: "没有匹配当前检索条件的契约。",
    noExplicitTerms: "这一节没有显式条款。",
    verifyFallback: "运行最接近的仓库本地验证，并保留证据。",
    contractCopied: "契约已复制",
    adaptedCopied: "改写后的契约已复制",
    clipboardUnavailable: "剪贴板不可用",
    verifyCopied: "验证命令已复制",
    selectVerifyText: "请手动选择验证命令",
    loadContractsFailed: "契约载入失败",
    copied: "已复制",
    selectText: "请手动选择文本",
    entryNumberPrefix: "№",
    contractsCount: (filtered, total) => `${filtered} / ${total} 条契约`,
    categoryLabels: {
      "accessibility": "无障碍",
      "ai-evals": "AI · 评测",
      "ai-ops": "AI · 运维",
      "backend-api": "后端 · API",
      "backend-data": "后端 · 数据",
      "backlog": "待办",
      "cli": "命令行",
      "data-analytics": "数据 · 分析",
      "data-eng": "数据 · 工程",
      "design": "设计",
      "devops-ci": "DevOps · CI",
      "devops-runtime": "DevOps · 运行时",
      "docs": "文档",
      "frontend": "前端",
      "goal-maintenance": "goal 维护",
      "greenfield-build": "新项目构建",
      "investigation": "调查",
      "maintenance": "维护",
      "migration": "迁移",
      "mobile": "移动端",
      "orchestration": "编排",
      "performance": "性能",
      "product": "产品",
      "prompt-optimization": "提示词优化",
      "prototype": "原型",
      "qa": "测试 QA",
      "refactor": "重构",
      "research": "研究",
      "security-appsec": "安全 · 应用",
      "security-ops": "安全 · 运维",
      "testing": "测试",
      "workflow": "工作流",
    },
    difficultyLabels: {
      advanced: "高阶",
      intermediate: "中阶",
    },
    originLabels: {
      all: "全部",
      seed: "原生",
      "source-backed": "外部",
    },
    sourceTypeLabels: {
      "github-discussion": "GitHub 讨论",
      "github-issue": "GitHub Issue",
      "github-pr": "GitHub PR",
      "official-agent-task": "官方智能体任务",
      "official-goal": "官方 /goal",
      "official-workflow": "官方工作流",
      "public-forum": "公开论坛",
      "third-party-project": "第三方项目",
      "third-party-review": "第三方评测",
      "third-party-tutorial": "第三方教程",
      "tool-readme": "工具 README",
      "video-summary": "视频摘要",
      "x-post": "X 帖子",
    },
    verifyKindLabels: {
      test: "测试",
      metric: "指标",
      doc: "文档",
      rollout: "发布",
    },
  },
};

function activeCopy() {
  return copy[state.lang] || copy.en;
}

function t(key) {
  const value = activeCopy()[key] ?? copy.en[key];
  return typeof value === "function" ? value : value || key;
}

function formatContractsCount(filtered, total) {
  const formatter = activeCopy().contractsCount || copy.en.contractsCount;
  return formatter(filtered, total);
}

function localizedLabel(group, value, fallback = "") {
  const labels = activeCopy()[group] || copy.en[group] || {};
  const defaultLabels = copy.en[group] || {};
  return labels[value] || defaultLabels[value] || fallback || titleCase(value);
}

const queryAliases = {
  a11y: ["accessibility", "a11y", "wcag"],
  agent: ["agent", "agents", "codex", "claude", "hermes"],
  api: ["api", "endpoint", "route", "contract"],
  auth: ["auth", "authentication", "authorization", "authz", "login", "permission"],
  bug: ["bug", "fix", "repair", "failure", "failing", "error", "regression"],
  ci: ["ci", "workflow", "actions", "pipeline", "check"],
  database: ["database", "db", "schema", "migration", "sql"],
  docs: ["docs", "documentation", "readme", "guide", "runbook"],
  evals: ["eval", "evals", "evaluation", "grading", "score"],
  fail: ["fail", "fails", "failing", "failure", "red", "error", "repair", "fix", "pass", "clean"],
  flaky: ["flaky", "unstable", "race", "intermittent"],
  guardrails: ["guardrail", "guardrails", "safety", "policy", "security"],
  lint: ["lint", "eslint", "ruff", "format", "typecheck", "typescript"],
  migration: ["migration", "migrate", "port", "upgrade", "compatibility"],
  mobile: ["mobile", "ios", "android", "github mobile"],
  onboarding: ["onboarding", "quickstart", "docs", "guide", "contributor"],
  red: ["red", "failing", "failure", "error", "lint", "test", "clean"],
  refactor: ["refactor", "cleanup", "split", "standardize"],
  security: ["security", "auth", "authorization", "injection", "xss", "csrf", "ssrf", "secret"],
  tests: ["test", "tests", "testing", "suite", "vitest", "pytest", "playwright", "coverage"],
  trace: ["trace", "tracing", "span", "spans", "observability"],
  typescript: ["typescript", "ts", "typecheck", "eslint"],
  安全: ["security", "auth", "authorization", "injection", "xss", "csrf", "ssrf", "secret"],
  鉴权: ["auth", "authentication", "authorization", "authz", "login", "permission"],
  登录: ["auth", "login", "permission"],
  迁移: ["migration", "migrate", "port", "upgrade", "compatibility"],
  测试: ["test", "tests", "testing", "suite", "vitest", "pytest", "playwright", "coverage"],
  失败: ["fail", "fails", "failing", "failure", "red", "error", "repair", "fix"],
  报错: ["fail", "error", "failure", "bug", "fix"],
  文档: ["docs", "documentation", "readme", "guide", "runbook"],
  前端: ["frontend", "ui", "css", "react", "component"],
  后端: ["backend", "api", "endpoint", "route", "data"],
  性能: ["performance", "perf", "latency", "speed", "benchmark"],
  移动端: ["mobile", "ios", "android", "responsive"],
  工作流: ["workflow", "pipeline", "actions", "ci"],
  命令行: ["cli", "command", "terminal"],
  重构: ["refactor", "cleanup", "split", "standardize"],
};

const glyphs = {
  "accessibility": "A11",
  "ai-evals": "AE",
  "ai-ops": "AO",
  "backend-api": "BA",
  "backend-data": "BD",
  "cli": "CL",
  "data-analytics": "DA",
  "data-eng": "DE",
  "design": "DS",
  "devops-ci": "DC",
  "devops-runtime": "DR",
  "docs": "DO",
  "frontend": "FE",
  "goal-maintenance": "GM",
  "greenfield-build": "GB",
  "investigation": "IN",
  "migration": "MG",
  "mobile": "MO",
  "orchestration": "OR",
  "performance": "PF",
  "product": "PR",
  "prompt-optimization": "PO",
  "prototype": "PT",
  "qa": "QA",
  "refactor": "RF",
  "research": "RS",
  "security-appsec": "SA",
  "security-ops": "SO",
  "testing": "TS",
  "workflow": "WF",
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

function titleCase(value) {
  return String(value)
    .split("-")
    .map((part) => part ? part[0].toUpperCase() + part.slice(1) : part)
    .join(" ");
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
  const advanced = state.entries.filter((entry) => entry.difficulty === "advanced").length;
  const categories = unique(state.entries.map((entry) => entry.category)).length;
  setText(els.total, String(state.entries.length));
  setText(els.categories, String(categories));
  setText(els.sourced, padNumber(sourced));
  setText(els.advanced, padNumber(advanced));
  setText(els.sealTotal, `${padNumber(state.entries.length)} / ${padNumber(state.entries.length)}`);
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
  const label = state.category === "all" ? t("allContracts") : categoryLabel(state.category);
  setText(els.categoryTitle, label);
  setText(els.resultCount, formatContractsCount(state.filtered.length, state.entries.length));
}

function renderCategoryShortcuts() {
  const counts = countBy(state.entries, "category");
  const buttons = [];

  const all = document.createElement("button");
  all.type = "button";
  all.className = state.category === "all" ? "rail__cat active" : "rail__cat";
  const allGlyph = document.createElement("span");
  allGlyph.className = "rail__glyph";
  allGlyph.textContent = "*";
  const allName = document.createElement("span");
  allName.className = "rail__name";
  allName.textContent = t("allContracts");
  const allCount = document.createElement("span");
  allCount.className = "rail__count";
  allCount.textContent = String(state.entries.length);
  all.appendChild(allGlyph);
  all.appendChild(allName);
  all.appendChild(allCount);
  all.addEventListener("click", () => {
    setActiveRecipe("all");
    state.category = "all";
    applyFilters();
  });
  buttons.push(all);

  for (const category of unique(state.entries.map((entry) => entry.category))) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = state.category === category ? "rail__cat active" : "rail__cat";

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
    const button = document.createElement("button");
    button.type = "button";
    button.className = state.selected && state.selected.id === entry.id ? "entry active" : "entry";
    button.addEventListener("click", () => selectEntry(entry, true));

    const no = document.createElement("span");
    no.className = "entry__no";
    no.textContent = `${t("entryNumberPrefix")} ${padNumber(index)}`;

    const content = document.createElement("span");
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
    action.textContent = "/";

    button.appendChild(no);
    button.appendChild(content);
    button.appendChild(action);
    return button;
  });

  clearAndAppend(els.results, children);
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
  setText(els.copy, t("copyGoal"));

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

  if (entry.source_url && entry.source_name) {
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
    button.classList.toggle("active", button.dataset[dataKey] === activeValue);
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
  state.origin = "all";
  setActiveRecipe("all");
  setActiveButtons(els.difficultyButtons, "all", "difficulty");
  setActiveButtons(els.originButtons, "all", "origin");
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
      setText(els.copy, t("copyGoal"));
    }, 1400);
  } catch (error) {
    setText(els.copy, t("selectText"));
    showToast(t("clipboardUnavailable"));
    window.setTimeout(() => {
      setText(els.copy, t("copyGoal"));
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

function adapterValue(input, fallback) {
  const value = input && input.value.trim();
  return value || fallback;
}

function buildAdaptedPrompt(entry) {
  const projectType = adapterValue(els.adapterType, "the current repository");
  const targetModule = adapterValue(els.adapterModule, entry.category);
  const verify = adapterValue(els.adapterVerify, entry.verify);
  const extraConstraint = adapterValue(els.adapterConstraint, "Keep public behavior unchanged unless the goal explicitly requires it.");

  return `/goal

GOAL:
Complete ${entry.title} for ${projectType}, focused on ${targetModule}: ${entry.intent}

CONTEXT:
- Read the nearest AGENTS.md/CLAUDE.md and the relevant project docs before editing.
- Inspect the ${targetModule} implementation, tests, configuration, and latest failing output.
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
    showToast(t("adaptedCopied"));
  } catch (error) {
    showToast(t("clipboardUnavailable"));
  }
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
  els.search.addEventListener("input", () => {
    setActiveRecipe("all");
    applyFilters();
  });
  els.reset.addEventListener("click", resetFilters);
  els.copy.addEventListener("click", copySelected);
  els.validate.addEventListener("click", copyVerify);
  els.copyAdapted.addEventListener("click", copyAdaptedPrompt);

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
      fetch("examples.json", { cache: "no-store" }),
      fetch("recipes.json", { cache: "no-store" }),
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
    state.selected = entries.find((entry) => entry.slug === wanted) || entries[0] || null;
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

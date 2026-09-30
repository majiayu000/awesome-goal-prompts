const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const { test } = require("node:test");
const vm = require("node:vm");

const docsDir = path.join(__dirname, "../docs");
const entries = JSON.parse(readFileSync(path.join(docsDir, "examples.json"), "utf8"));
const recipes = JSON.parse(readFileSync(path.join(docsDir, "recipes.json"), "utf8"));
const markdown = readFileSync(path.join(docsDir, "how-to-write-goals.md"), "utf8");
const defaultEntry = entries.find((entry) => entry.origin === "source-backed");
const settle = () => new Promise((resolve) => setImmediate(resolve));

// Only the DOM operations used by the page scripts; rendering runs unmodified.
function element(tag = "div") {
  return {
    tagName: tag,
    textContent: "",
    value: "",
    dataset: {},
    children: [],
    attributes: {},
    classList: { add() {}, remove() {}, toggle() {} },
    appendChild(child) { this.children.push(child); },
    replaceChildren(...children) { this.children = children; },
    setAttribute(name, value) { this.attributes[name] = value; },
    removeAttribute(name) { delete this.attributes[name]; },
    addEventListener() {},
    querySelectorAll() { return []; },
  };
}

function textOf(node) {
  return node.textContent + node.children.map(textOf).join("");
}

async function page(name, hash, fetchImpl) {
  const elements = new Map();
  const listeners = new Map();
  const requests = [];
  const pending = [];
  const document = {
    documentElement: element("html"),
    body: element("body"),
    querySelector(selector) {
      if (!elements.has(selector)) elements.set(selector, element());
      return elements.get(selector);
    },
    querySelectorAll() { return []; },
    createElement: element,
    createDocumentFragment: () => element("fragment"),
    createTextNode(text) { return { textContent: text, children: [] }; },
  };
  const window = {
    location: { hash, search: "", href: `https://example.com/${name}${hash}` },
    localStorage: { getItem: () => null },
    addEventListener(name, listener) { listeners.set(name, listener); },
  };
  const context = vm.createContext({
    document, window, navigator: { language: "en" }, URL, URLSearchParams, console,
    fetch: (url) => {
      requests.push(url);
      const response = fetchImpl ? fetchImpl(url) : Promise.resolve({
        ok: true,
        json: async () => url === "examples.json" ? entries : recipes,
        text: async () => markdown,
      });
      pending.push(response);
      return response;
    },
  });
  const html = readFileSync(path.join(docsDir, name), "utf8");
  for (const [, script] of html.matchAll(/<script src="([^"]+)" defer><\/script>/g)) {
    vm.runInContext(readFileSync(path.join(docsDir, script), "utf8"), context, { filename: script });
  }
  await Promise.allSettled(pending);
  await settle();
  return { elements, listeners, window, context, requests };
}

for (const hash of ["#%", "#%E0%A4%A", "#%FF", "#%C0%AF"]) {
  test(`catalog renders after malformed fragment ${hash}`, async () => {
    const { elements, requests } = await page("index.html", hash);
    assert.deepEqual(requests, ["examples.json", "recipes.json"]);
    assert.equal(elements.get("#detail-title").textContent, defaultEntry.title);
    assert.ok(elements.get("#results").children.length > 0);
    assert.equal(elements.get("#results").children[0].tagName, "a");
    assert.doesNotMatch(textOf(elements.get("#results")), /Failed to load/);
  });

  test(`docs renders after malformed startup fragment ${hash}`, async () => {
    const { elements, requests } = await page("docs.html", hash);
    assert.deepEqual(requests, ["how-to-write-goals.md"]);
    assert.match(textOf(elements.get("#doc-content")), /GOAL/);
    assert.equal(elements.get("#doc-content").attributes["aria-busy"], "false");
  });

  test(`docs renders after malformed hashchange ${hash}`, async () => {
    const { elements, listeners, window, context, requests } = await page("docs.html", "#how-to-write");
    vm.runInContext("state.cache.clear(); els.content.replaceChildren()", context);
    window.location.hash = hash;
    await listeners.get("hashchange")();
    await settle();
    assert.equal(requests.length, 2);
    assert.match(textOf(elements.get("#doc-content")), /GOAL/);
    assert.equal(elements.get("#doc-content").attributes["aria-busy"], "false");
  });
}

test("valid encoded catalog fragment still selects its entry and origin", async () => {
  const entry = entries.find((entry) => entry.origin === "seed");
  const hash = `#${entry.slug.replace(/-/g, "%2D")}`;
  const { elements } = await page("index.html", hash);
  assert.equal(elements.get("#detail-title").textContent, entry.title);
  assert.ok(elements.get("#results").children.some((link) => link.dataset.entryId === String(entry.id)));
});

for (const hash of ["", "#unknown"]) {
  test(`catalog keeps its default selection for ${hash || "empty hash"}`, async () => {
    const { elements } = await page("index.html", hash);
    assert.equal(elements.get("#detail-title").textContent, defaultEntry.title);
    assert.equal(elements.get("#results").children[0].tagName, "a");
  });
}

for (const hash of ["", "#unknown", "#how%2Dto%2Dwrite"]) {
  test(`docs keeps its existing selection fallback for ${hash || "empty hash"}`, async () => {
    const { elements, requests } = await page("docs.html", hash);
    assert.deepEqual(requests, ["how-to-write-goals.md"]);
    assert.match(textOf(elements.get("#doc-content")), /GOAL/);
  });
}

async function withHttpFailure(run) {
  const server = http.createServer((_, response) => {
    response.writeHead(503, "Service Unavailable");
    response.end("unavailable");
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  try {
    const base = `http://127.0.0.1:${server.address().port}/`;
    await run((url) => fetch(new URL(url, base)));
  } finally {
    server.closeAllConnections();
    await new Promise((resolve, reject) => server.close((error) => error ? reject(error) : resolve()));
  }
}

test("catalog retains real HTTP fetch failure with a malformed fragment", async () => {
  await withHttpFailure(async (fetchImpl) => {
    const { elements } = await page("index.html", "#%", fetchImpl);
    assert.match(textOf(elements.get("#results")), /Failed to load examples: 503/);
  });
});

test("docs retains real HTTP fetch failure with a malformed fragment", async () => {
  await withHttpFailure(async (fetchImpl) => {
    const { elements } = await page("docs.html", "#%", fetchImpl);
    assert.equal(elements.get("#doc-content").children[0].className, "doc-error");
    assert.match(textOf(elements.get("#doc-content")), /503 Service Unavailable/);
  });
});

test("unexpected decoding errors still propagate", async () => {
  const { context } = await page("docs.html", "#how-to-write");
  vm.runInContext('decodeURIComponent = () => { throw new Error("unexpected decoder failure"); }', context);
  assert.throws(() => vm.runInContext("getRequestedDoc()", context), /unexpected decoder failure/);
});

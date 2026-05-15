# 数据结构

这个项目的目录数据是生成出来的，页面和 README 读取的是同一套结构化数据：

- `data/examples.json` 和 `docs/examples.json`：完整的 goal 目录。
- `data/recipes.json` 和 `docs/recipes.json`：首页“从这里开始”的筛选入口。
- `data/search-eval-cases.json`：CI 使用的搜索质量检查用例。

## 示例字段

- `id`：稳定 slug，用于链接和工具处理。
- `slug`：与 `id` 相同，保留给兼容读取方。
- `category`：目录分类，用于 README 和 GitHub Pages 页面筛选。
- `title`：示例标题。
- `intent`：一句话说明这个任务要解决什么问题。
- `verify`：证明完成的命令、报告、产物或证据路径。
- `difficulty`：难度，取值为 `intermediate` 或 `advanced`。
- `origin`：来源类型，取值为 `seed` 或 `source-backed`。
- `source_url`：有公开来源时填写 URL，否则为 `null`。
- `source_name`：公开来源的简短名称，否则为 `null`。
- `source_type`：来源分类，否则为 `null`。
- `evidence`：从来源中提取或与来源直接对应的证据短语，否则为 `null`。
- `evidence_summary`：生成的来源说明，组合证据短语、来源名称、来源类型和验证路径。
- `prompt`：生成后的 `/goal` 任务说明。

## 来源规则

`source-backed` 表示这个条目绑定了一个公开 URL，以及一个具体任务、示例或使用规则。它不表示 prompt 文本是从来源逐字复制的。

`seed` 表示这个条目是可复用的目录模式。不要把 seed 条目描述成来自 X、GitHub、官方文档或某个作者。

## 来源类型

标准来源类型以 `SOURCES.md` 为准。页面里展示的来源 badge 也来自这套字段。

## Recipe 字段

- `id`：稳定 recipe 标识。
- `label`：英文标签。
- `label_zh`：中文标签。
- `query`：点击 recipe 后应用的搜索词。
- `category`：分类过滤条件，或 `all`。
- `origin`：来源过滤条件，或 `all`。

## 搜索评测字段

- `query`：模拟真实用户会输入的自然语言查询。
- `expected`：应该被搜到的目录条目 ID。
- `max_rank`：该条目允许出现的最差排名。

CI 会运行这些用例，防止搜索逻辑改动后悄悄降低目录可发现性。

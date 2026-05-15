# 如何写好 `/goal`

一个好的 `/goal` 不是一句愿望，而是一份可以执行、可以验收的任务说明。它要告诉智能体：目标是什么，先看哪些上下文，哪些东西不能改，怎样证明完成，以及遇到风险时什么时候停下来。

不要直接套用目录里的示例。先看模式，再把它改成你当前仓库里的真实文件、命令、约束和验收标准。

## 基本结构

```text
/goal
GOAL:
<一个可衡量的目标。不要把无关待办塞进同一个任务。>

CONTEXT:
- 仓库、产品区域或 issue:
- 开始前必须阅读的文件、文档、日志、截图或计划:
- 当前基线或已知失败现象:
- 项目约定:

CONSTRAINTS:
- 不要修改:
- 必须保留:
- 安全、数据、测试或产品约束:
- 范围边界和非目标:

DONE WHEN:
- <具体完成条件 1>
- <具体完成条件 2>
- <具体完成条件 3>

VERIFY:
- 运行:
- 检查:
- 截取或记录:
- 如果无法验证，停下来说明具体阻塞。

OUTPUT:
- 修改的文件:
- 关键决策:
- 验证结果:
- 剩余风险:
- 后续事项:

STOP RULES:
- 缺少密钥、生产凭据、破坏性数据操作或产品决策时停止。
- 同一个问题连续修三次仍失败时停止，重新检查根因假设。
- 当前状态没有对照 DONE WHEN 检查前，不要宣布完成。
```

## 六步写清楚

### 1. 只写一个目标

不要这样写：

```text
/goal 修好应用，顺便清理代码，提升性能，保证别出错
```

可以这样写：

```text
/goal
GOAL:
修复登录偶发白屏问题，并保持 auth 测试集通过。
```

一个目标可以很大，但必须只有一个清楚的终点。

### 2. 指向真实上下文

不要让智能体猜哪里才是事实来源。把 issue、文件、日志、失败命令、设计文档或分支状态写清楚。

```text
CONTEXT:
- 修改前阅读 `AGENTS.md`、`docs/auth-flow.md` 和 issue #184。
- 从 `npm test -- auth` 的失败输出开始复现。
- 问题出现在 OAuth callback 之后，触发条件是存在过期 session cookie。
```

### 3. 写硬约束

约束用来阻止范围漂移。包括 API 兼容性、禁止修改的文件、数据安全、安全规则和测试完整性。

```text
CONSTRAINTS:
- 不要改变公开 API 的响应结构。
- 不要删除或弱化现有测试。
- 不要新增 auth 依赖。
- 修改范围只限 auth callback 处理和相关测试。
```

### 4. 让完成条件可验收

`DONE WHEN` 应该能被代码状态、命令输出或产物直接验证，而不是依赖智能体的自信。

```text
DONE WHEN:
- 白屏复现路径不再失败。
- 现有 auth 测试通过。
- 新增回归测试覆盖过期 cookie callback 场景。
- 最终 diff 没有无关格式化改动。
```

### 5. 要求本轮验证

验证可以是命令、报告、截图、日志或生成文件。如果某个仓库没有完全相同的命令，就要求使用最接近的仓库本地命令，并在无法运行时说明阻塞。

```text
VERIFY:
- 运行 `npm test -- auth`。
- 运行 `npm run lint`。
- 记录修复前后的复现结果。
- 如果本地缺少 OAuth 凭据，停止并报告缺少的变量名。
```

### 6. 给出停止规则

长任务需要安全的未完成状态。遇到生产访问、破坏性数据操作、缺少密钥、产品决策不清楚，或同一问题反复失败时，不应该继续猜。

```text
STOP RULES:
- 需要生产凭据、破坏性数据库变更或产品负责人决策时停止。
- 同一失败连续修三次仍未解决时停止，重新检查根因假设。
- 如果某一部分无法在本地完成，用证据标记未完成，只继续做互不依赖的安全工作。
```

## 值得保留的模式

社区帖子可以提供工作流灵感，但不能替代真实工具行为。把它们当作模式参考，最终仍要回到官方文档、仓库代码和本地验证。

| 模式 | 适用场景 | 目录条目 |
| --- | --- | --- |
| 先写 goal | 任务太模糊，但仓库里有足够上下文。先让智能体阅读上下文并起草 `/goal`。 | `x-meta-goal-prompt-generator` |
| 测试和 lint 闭环 | 目标很机械：测试通过、lint 干净、类型检查通过。 | `x-tests-lint-completion` |
| 退出条件 | 长任务里可能存在无法完成或被阻塞的部分。 | `x-goal-escape-hatch` |
| 仓库规则 + goal | `AGENTS.md` 或 `CLAUDE.md` 里的规则必须在长会话或压缩后继续生效。 | `x-agentsmd-goal-workflow` |
| 先计划再执行 | 工作需要先设计方案，再按稳定计划执行。 | `x-plan-then-goal-execution` |
| 可衡量证明 | 任务有变成泛泛待办列表的风险。 | `x-measurable-goal-structure` |

## 可复制示例

### 修复闭环

```text
/goal auth tests pass and lint is clean

Read first: `AGENTS.md`, failing auth test output, and auth route handlers.
Constraints: Do not change public API shapes. Do not delete or weaken tests.
Done when: auth tests pass, lint passes, and the fix includes a regression test for the reproduced bug.
Verify with: `npm test -- auth` and `npm run lint`.
Stop if: credentials, production access, or a product decision is required.
Final output: changed files, root cause, verification output, remaining risk.
```

### 带行为锁的重构

```text
/goal
GOAL:
把 `UserService` 拆成更小的模块，同时保持公开行为不变。

CONTEXT:
- 阅读 `AGENTS.md`、`src/services/UserService.ts`、当前调用方和现有 service 测试。
- 先用 `npm test -- UserService` 建立基线。

CONSTRAINTS:
- 不改变导出方法名、请求/响应结构或错误语义。
- 不引入新框架或新依赖。
- 不把无关清理合并进这次重构。

DONE WHEN:
- `UserService` 的职责被拆到更聚焦的模块。
- 现有调用方在不改 API 的情况下能编译。
- 现有 service 测试和行为刻画测试通过。
- 最终 diff 只限 service 和测试相关文件。

VERIFY:
- 运行 `npm test -- UserService`。
- 运行 `npx tsc --noEmit`。
- 记录刻画测试中发现的任何行为差异。

OUTPUT:
- 修改文件、模块拆分理由、验证输出、剩余风险。

STOP RULES:
- 如果“保持行为不变”和“拆分”发生冲突，停止说明。
- 同一个失败测试连续三次修不好时停止，重新检查假设。
```

## 检查清单

运行一个 goal 前，确认：

- 只有一个主要目标。
- 上下文里有真实文件、issue、日志、文档或命令。
- 约束明确说明哪些不能改。
- `DONE WHEN` 能用仓库状态或产物验收。
- `VERIFY` 要求本轮新鲜命令或证据。
- 停止规则覆盖密钥、生产访问、破坏性操作、决策不清和反复失败。
- 最终输出要求列出修改文件、验证结果、关键决策、风险和下一步。

## 不要写这些

不要用信心代替证明：

- `make no mistakes`
- `fix everything`
- `do whatever it takes`
- `improve the codebase`
- `keep going until perfect`
- `use your best judgment` 但没有约束

把这些换成可衡量的结束状态、真实验证和明确停止规则。

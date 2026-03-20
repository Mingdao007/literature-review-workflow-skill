# Literature Review Workflow Skill

用于做完整文献综述流程的可移植 skill，覆盖 scope 设定、语料建立、taxonomy 设计、证据提取与交付准备。

## 提供内容

- 可安装 skill: [`literature-review-workflow`](./literature-review-workflow)
- 公开 references: [`literature-review-workflow/references/`](./literature-review-workflow/references)
- 辅助脚本: [`literature-review-workflow/scripts/`](./literature-review-workflow/scripts)

## 安装 / 使用

- `Codex App`：从本仓库路径 `literature-review-workflow` 安装
- GitHub 安装目标：
  - repo：`<owner>/literature-review-workflow-skill`
  - path：`literature-review-workflow`
- 安装后重启 `Codex App`，让新 skill 被发现。

## 覆盖范围

- 覆盖 scope note、corpus log、taxonomy 与 comparison matrix 工作流
- 以 anchor papers 为主线做综合，而不是直接写最终交付物
- 提供 review notes、source log 与 slide outline 的模板

## 触发示例

- `Run a literature review on this topic.`
- `Build a taxonomy and comparison matrix for these papers.`
- `Prepare review-ready content from a paper corpus.`

## 不触发示例

- `Explain only one paper section.`
- `Only clean my bibliography database.`
- `Design slide visuals without doing the review workflow.`

## 隐私边界

这个公开仓库只保留可复用、可公开的工作流部分。

- User-specific defaults and local note conventions are rewritten into generic public defaults.
- The public package does not depend on private memory files or local reference-manager setup.

## 仓库结构

- `literature-review-workflow/`: installable `Codex App` skill
- `literature-review-workflow/references/`: bundled public references
- `literature-review-workflow/scripts/`: bundled public scripts
- `CHANGELOG.md`: release history
- `LICENSE`: `MIT`

English:

- [README.md](./README.md)

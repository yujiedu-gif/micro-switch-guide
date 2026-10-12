# Mac 本地内容监控器

`bin/content-supervisor` 是本项目的人工可控状态机。它不依赖 Codex，也不会随开机启动。
只有你主动运行命令时它才工作；`watch` 也只是占用当前终端的前台进程。

## 安全边界

- 只监控通过 `track` 加入白名单的 Batch，不扫描或接管历史 Batch。
- `watch` 只查询状态并在终态下载、幂等回填结果，不会提交新付费任务。
- OpenAI 预检和 Batch 提交必须手动运行 `submit --confirm-paid`。
- 创建 GitHub PR 必须手动运行 `finalize --create-pr`；永远不会自动合并。
- `pause` 只停止本地监控，不会取消 OpenAI 已提交的 Batch。
- 状态文件权限为 `0600`，日志不写 API 密钥。

## 当前 pilot 的日常命令

在仓库根目录运行：

```bash
# 看一眼当前进度和下一步建议
./bin/content-supervisor status --name pilot

# 只检查一次 OpenAI 状态；适合偶尔手动看
./bin/content-supervisor run-once --name pilot

# 当前终端持续监控，每 5 分钟检查一次；Ctrl-C 可退出
./bin/content-supervisor watch --name pilot --interval 300

# 也可从另一个终端暂停/恢复
./bin/content-supervisor pause --name pilot
./bin/content-supervisor resume --name pilot
```

## 文章审核闸门

V11 在正文响应内完成逻辑、参数、定义和非营销品牌自审，不再提交独立审核 Batch。V10 结果仍兼容；下面的 review 命令只用于仍在运行或回收中的 V9 请求。

文章 Batch 回收后：

```bash
# 本地文字复用检查；加 --semantic 才会运行本地 all-mpnet-base-v2 和 Qdrant
./bin/content-supervisor audit --name pilot --semantic

# 只生成审核请求文件，不花 OpenAI 费用
./bin/content-supervisor prepare --name pilot --kind review --limit 60

# V9 人工确认后提交审核 Batch（会产生费用）
./bin/content-supervisor submit --name pilot --kind review --confirm-paid
```

若审核未通过，最多准备一次内容修改：

```bash
./bin/content-supervisor prepare-repair --name pilot
./bin/content-supervisor submit --name pilot --kind repair --confirm-paid
```

若只是 OpenAI 网络、过期或服务端失败，使用原请求精确重试，不改文章：

```bash
./bin/content-supervisor prepare-retry --name pilot --batch-id BATCH_ID
./bin/content-supervisor submit --name pilot --kind repair --confirm-paid
```

达到 50 篇后，先本地验收；PR 是另一道显式闸门：

```bash
# 校验审核、固定正式发布集、只在发布集内修正内链、渲染文章、构建 Jekyll，但不创建 PR
./bin/content-supervisor finalize --name pilot

# 只有验收全部通过时才创建分支和 PR，仍不合并
./bin/content-supervisor finalize --name pilot --create-pr
```

## 新建另一轮

```bash
./bin/content-supervisor configure --name wave250 --run-id RUN_ID --target 250 --poll-seconds 300
./bin/content-supervisor track --name wave250 --batch-id BATCH_ID --kind article --input /absolute/path/to/article.jsonl
```

同名配置不会被静默覆盖。确定要重置时才给 `configure` 加 `--force`。
配置、日志、批次文件都位于 `pipeline/state/supervisor/`，该目录已被 Git 忽略。

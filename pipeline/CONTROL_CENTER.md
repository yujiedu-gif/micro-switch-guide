# MicroSwitchGuide 本地内容控制台

启动：

```bash
./bin/content-control serve --open
```

默认地址是 `http://127.0.0.1:8765`。它不会注册为登录项，也不会随 Mac 自动启动。关闭终端或按 `Ctrl-C` 会停止控制台；已提交到 OpenAI 的 Batch 不会因此取消，下次启动后可继续查询。

CSV 必须有 `keyword` 列，可选 `search_volume`、`intent`、`cpc`、`competition`。例如：

```csv
keyword,search_volume,intent
what is a micro switch,900,informational
micro switch no vs nc,500,informational
```

导入会执行：创建 run → 导入/过滤 → 本地 all-mpnet-base-v2 Embedding → Qdrant 增量聚类 → 建立文章任务 → 准备规划 Batch。这一段不会提交付费请求。

操作模式：

- 手动：按阶段点击“准备”和“提交”。每次提交需输入 `确认付费`。
- 自动：输入 `确认自动付费` 后，自动推进规划、正文、双重去重、逻辑审核及最多一次修改。不会自动创建 PR。
- 创建 PR：验收通过后输入 `创建PR`。系统不会合并 PR。

“只读扩词审计（免费）”会把被拒绝的原始词作为材料，提取设备、部件和任务，再生成带来源链和内容身份的候选。它不改关键词选择、不提交 DataForSEO/OpenAI，也不会生成正文。界面展示候选总量及前 100 个可规划候选。

命令框不是 Shell，只接受：`status`、`poll`、`pause`、`resume`、`prepare plan`、`prepare article`、`prepare review`、`audit`、`audit semantic`、`expand audit`、`prepare repair`、`finalize`、`auto stop`。

终端也可操作：

```bash
./bin/content-control status
./bin/content-control import /absolute/path/to/keywords.csv --target 50
./bin/content-control command "poll"
```

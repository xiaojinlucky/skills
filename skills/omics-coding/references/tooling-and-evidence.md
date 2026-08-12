# OmicVerse / SCOP 工具与证据维护规则

这份文件只记录已经核对过的工具边界。它服务于 skill 维护，不是正式分析代码的运行时配置。

## 已采用的成熟工具

| 工具 | 用法 | 边界 |
|---|---|---|
| OmicVerse 官方 `omicverse-skills` | Python/AnnData 路线确定后，用 `list_skills()` 和 `load_skill_text()` 查阶段顺序、输入输出、官方来源和验收示例 | 只作工作流参考；本地包、官方函数文档和项目已确认路线优先 |
| SCOP 官方文档 | R/Seurat 路线直接查函数、参数和 Seurat v5 对象要求 | 不用 Python skill 目录替代 R 路线判断 |
| scverse / AnnData / MuData | 处理 Python 组学对象和跨工具互操作时，优先采用其数据结构与官方教程 | 不能因为生态包更新就单独升级 OmicVerse 的关键依赖 |
| scib / scib-metrics | 只有研究问题确实需要比较批次校正或整合质量时使用 | 这是评估工具，不是默认分析步骤；不同版本的指标不要直接横向比较 |
| OmicOS 参考层 | 提醒可能的路线、风险和审查角色 | 不是函数权威，也不能单独决定方法 |
| 官方 OmicOS / OmicOS-Bio | 借鉴 `ingest -> plan -> execute -> verify -> deliver`、只读盘点、过程留痕和结果读回 | 当前 Codex/Positron 不依赖其云端账号、订阅、网关或自动恢复 |

## 官方 OmicVerse skill 桥接

Python 路线已确认后，可以先在 `omicverse` 环境中查看官方目录：

```bash
conda run -n omicverse python -c "from omicverse_skills import list_skills; print(len(list_skills())); print([s['slug'] for s in list_skills() if 'single-cell' in s['slug']][:20])"
conda run -n omicverse python -c "from omicverse_skills import load_skill_text; print(load_skill_text('single-cell-preprocessing'))"
```

重点借鉴四件事：阶段边界、输入输出契约、官方来源、最小验收 smoke test。不要把目录中的所有 skill 复制进本 skill，也不要把其中用于教学验收的 `try/except`、重复字段检查或自动降级搬进固定路线的正式 R/Python 代码。路线已经确认后，主流程仍然直接写。

`omicclaw` 可以作为网关、会话、工作区和过程记录的架构参考，但不作为 Codex/Positron 的必需运行依赖。它引入完整运行时的协调成本大于当前收益。

OmicOS/OmicOS-Bio 是更完整的官方产品化工作流参考：公开文档提供 Agents、Skills、Memory、远程/HPC、故障排查和单细胞案例。它最值得吸收的不是“让 Agent 自动替用户决定”，而是把分析拆成可复核阶段：先只读检查原始对象，再明确物种、表达形式、sample、donor、batch 和研究范围；用户确认方案后写出新文件；从磁盘读回并核对维度、关键字段和原文件未被修改。单细胞下游还要保留三个边界：已有 cluster 不重复聚类，注释先看 marker 再看候选证据，组间统计以 sample/donor 为独立单位而不是把细胞当重复。

官方案例也记录了真实执行中的参数完整性失败、按 batch 选 HVG 后的实际 fallback 和损坏 checkpoint 恢复。对本 skill 的吸收方式是：记录真实发生的分支和恢复过程；固定路线的正式代码仍然直接写，不预先堆一层假想 fallback。

## 版本与对象边界

- OmicVerse、`omicverse-skills`、SCOP 分别按官方包版本核对；不要只看 skill 文档日期。
- 当前 OmicVerse 依赖边界包含 `anndata<0.12`。scverse 的新版本可能改变 `layers` 和 Zarr 行为，因此不能为了“跟最新版”单独升级 `anndata`，必须随 OmicVerse 依赖一起验证。
- Seurat v5 的 assay 可能包含多个 layer。`LayerData`、`JoinLayers`、`GetAssayData` 的选择属于路线和对象契约，必须在写代码前确认；不要在脚本里用重复 `if/stop` 去掩盖 layer 不一致。
- 官方目录 README 中的 skill 数量可能落后于实际安装包；以 `list_skills()` 的本地运行结果和包版本为准。

### 2026-08-03 已验证基线

- OmicVerse：`omicverse==2.3.1`，运行于 `omicverse` / Python 3.10.14；本次同时核对了 `anndata==0.11.4`、`zarr==2.18.3`、`scanpy==1.10.4`。版本入口是 [OmicVerse PyPI](https://pypi.org/project/omicverse/)。
- SCOP：`scop==0.9.0`，官方 `DESCRIPTION` 日期为 2026-08-02，运行于 `seurat_v5` / R 4.4.3 / Seurat 5.4.0 / SeuratObject 5.3.0。版本和变更入口是 [SCOP DESCRIPTION](https://raw.githubusercontent.com/mengxu98/scop/main/DESCRIPTION) 与 [SCOP NEWS](https://raw.githubusercontent.com/mengxu98/scop/main/NEWS.md)。
- SCOP 0.9.0 的新代码优先使用 `RunStandardWorkflow()`、`RunIntegration()`、`RunscDblFinder()`、`Runscds()`、`RunScrublet()` 和 `RunDoubletDetection()`；`standard_scop()`、`integration_scop()` 以及 `db_*` 名称保留为兼容入口并会给出弃用提示。
- SCOP 0.9.0 增加了多种可选后端包装器（如 `RunCHOIR()`、`RunCell2fate()`、`RunCell2location()`、`RunCNV()`、`RunSCENICPlus()`、`RunGRNBoost2()`、`RunGENIE3()`、`RunCisTarget()` 和 `RunSpatialCellChat()`），以及空间基准/结果登记接口。使用前仍须打开对应本地函数页核对后端依赖和输入对象。
- SCOP 空间路线在多图像对象上要显式核对 `image`；涉及坐标距离或整合时，默认坐标契约是原始采集坐标，旧显示坐标只能作为明确的兼容选项。不要把这些规则写成猜测性的通用 fallback。
- 本次完整索引为 743 个函数页和 9,752 条参数记录；SCOP 文档使用 GitHub 官方 Rd 源刷新。若 pkgdown 不稳定，使用 `python3 scripts/update_docs.py --package all --scop-source github`，只有无错误的完整刷新才可以发布为 Canonical 索引。

## 三个角度筛选外部信息

### 开发者角度

优先看源码、release、依赖声明、官方文档、CI/验收文件和 issue 修复记录。开发者的“支持”只有在代码、版本和可复现实例能对应上时才进入采用候选。

### 使用者角度

优先收集能复现的输入、环境、命令、输出和失败过程。只有“我用过很好用”或营销式截图，不能证明工具适合正式分析。

### 评估者角度

关注对象契约、版本兼容、结果是否可审计、是否保留分析语义、基准或独立比较，以及失败时是否暴露原始错误。社区内容用于发现候选和真实踩坑；最终采用仍需回到官方源码、文档和本地运行验证。

动态社区页面、视频和评论区必须记录原始页面、作者、发布时间、内容类型和访问日期。搜索摘要、转载文章和商业宣传只作为线索，不能单独写成已验证结论。

## 当前筛选结论

- 采用：官方 `omicverse-skills` 作为 Python 工作流参考桥；scverse 数据结构作为互操作边界；scib-metrics 作为有明确整合评估问题时的可选工具；OmicOS 继续作为内部路线提醒。
- 不作为核心依赖：完整 OmicClaw 运行时、闭源零代码平台、个人开发者的全流程替代平台。它们可以帮助发现用户体验设计，但当前没有足够的独立证据替代 OmicVerse/SCOP 主路线。
- OmicOS/OmicOS-Bio 进入“工作流骨架和产品设计参考”，不进入“必须安装的分析依赖”。公开文档还明确存在云同步、订阅分层、serve/cli 会话隔离和离线缓存陈旧等运行边界，采用前必须把这些边界与本地环境分开。
- 对外部社区的结论必须区分“开发者宣称”“用户可复现反馈”和“评估证据”；三者不能混写。

## 2026-07-20 初轮调研记录

### 高证据来源

- [OmicVerse 官方仓库](https://github.com/omicverse/omicverse) 和 [官方 skill 目录](https://github.com/omicverse/omicverse-skills)：分别作为分析平台和 workflow skill 的源码入口。
- [SCOP 官方仓库](https://github.com/mengxu98/scop) 与 [SCOP 文档](https://mengxu98.github.io/scop/)：作为 R/Seurat 函数和版本入口。
- [Seurat v5 官方对象说明](https://satijalab.org/seurat/articles/seurat5_essential_commands.html)：用于确认 Assay5、细胞集合和 layer 的对象边界。
- [Seurat issue 8304](https://github.com/satijalab/seurat/issues/8304)、[issue 8176](https://github.com/satijalab/seurat/issues/8176)、[issue 8207](https://github.com/satijalab/seurat/issues/8207)：真实用户在多 layer、整合输入和 `JoinLayers()` 状态上的踩坑，进入 Murphy 风险卡。
- [SCOP 优化版说明](https://github.com/zhanghao-njmu/SCP/issues/281)：开发者解释旧 SCP 维护和 Seurat v5 兼容问题，支持把版本/对象边界放在路线确认阶段。

### 中低证据但有工程启发的来源

- [OmicVerse 论文](https://www.nature.com/articles/s41467-024-50194-3)：支持统一平台覆盖多类组学任务，但论文作者自己的 benchmark 不能替代独立评估。
- [CellAgent 论文](https://arxiv.org/abs/2407.09811)：提供 Planner、Executor、Evaluator、工具检索、代码沙箱和留痕的 Agent 架构启发；不作为生物学结论来源。
- [OmicsTools 个人开发者项目](https://github.com/zihaoxingstudy1/OmicsTools)：展示本地、零代码、结果留存等产品思路，但社区规模和独立测试不足，不纳入核心依赖。
- [CytoNavigator 平台介绍](https://www.novelbio.com/sx-1.html)、[ZeroCoding 平台](https://zc.bioinfosci.cn/) 和 [CASSIA](https://www.cassia.bio/)：可观察参数推荐、流程树、云端注释和报告设计；目前主要是厂商或项目方自述，不作为方法证据。
- [OmicOS/OmicOS-Bio 官方工作台](https://docs.omicos.cn/zh/)、[Agents/Skills/Memory 文档](https://docs.omicos.cn/zh/part1/13-advanced-agents-skills-memory.html)、[单细胞数据整理案例](https://docs.omicos.cn/zh/part4/single-cell/01-data-preparation.html)：高价值的流程与 UX 参考；案例本身是官方回放，不等于独立第三方 benchmark。

### 社区检索边界

本轮使用 GPT 内置网页检索，未调用用户电脑上的 Chrome、Edge 或其他本地浏览器，也没有进行登录。已检索公开可索引的抖音、公众号转载、个人项目入口和官方产品页面；目前能稳定核验的是教程、产品介绍、作者经验、公开 issue 以及视频页面可见的作者/发布时间/文字稿。播放量、搜索摘要、厂商好评或转载页的“用户反馈”不能单独算作独立真实用户证据。

小红书、抖音和微信公众号的动态搜索页、评论区和登录后内容，在 GPT 网页文本入口中没有稳定返回可引用的原文；这表示“当前没有可核验记录”，不表示这些社区没有相关内容。后续若用户提供登录授权，仍按“开发者—使用者—评估者”三类分别记录作者主页、正文、视频、评论原文、发布时间和访问日期；在此之前不把评论区内容写成已验证结论。

本轮公开索引中比较有用、但仍未达到核心采用标准的线索包括：[科研者之家抖音单细胞平台视频](https://www.douyin.com/shipin/7351249026081392676)、[统计之光的生信入门视频](https://jingxuan.douyin.com/m/video/7620766102838070571)、[生信跳跳唐的拟时序视频](https://jingxuan.douyin.com/m/video/7633682182623595816)、[OmicsTools 个人项目](https://github.com/zihaoxingstudy1/OmicsTools)、[Agent 单细胞实践转载](https://wxredian.com/art?id=d81a43ab0ba120d43dac083b9df8119c) 和 [Codex 生信工作流视频](https://jingxuan.douyin.com/m/video/7646221278726129690)。它们共同暴露的产品需求是：环境版本要固定，阶段输入输出要留下，脚本、图、表和日志要能回看，预测/注释/通讯结果不能越过证据边界直接写成因果结论。由于本轮没有核验到评论正文和独立复现，这些需求进入工程设计参考，不进入方法有效性结论。

本轮还核验了 [OmicOS-Bio 官方工作台](https://omicverse.com/index.html) 和 [OmicOS 单细胞案例文档](https://docs.omicos.cn/zh/part4/single-cell/01-data-preparation.html)：它们把只读盘点、方案确认、新文件写出、磁盘读回、marker 证据、已有 cluster 保留和 sample/donor 层级统计做成连续工作流。这正好对应本 skill 的使用痛点，因此已进入“工作流骨架和产品设计参考”；云账号、订阅、远程网关、自动恢复和自动生物学决策没有进入本地代码依赖。

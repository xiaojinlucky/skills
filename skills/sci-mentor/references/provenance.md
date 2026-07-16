# 私有语料来源与调用边界

## 来源层级

### 当前覆盖状态

- 全量来源台账 6228 条，区分可靠文本、OCR、ASR、重复、排除和待处理状态。
- 《做科研的大师兄·科研自救指南，基础版》274 页已完成 OCR，保留 159856 个文字，质量状态为 `ocr_unverified`。文献学习相关关键页已回看原图，但整份材料尚未逐字人工校正。
- 24 个科研环节共有 167 条严格定位的候选锚点，其中知识星球 72、PDF 48、B站 47。
- v2.2 当前保留 16 个创作者方法候选和 57 条证据链接。读文献 9 个、找课题思路 4 个、结果梳理 3 个。
- 其余任务环节继续保留在项目 workflow、拆分待验证或科学守门层，没有为了阶段齐全补造创作者方法。

上述状态表示来源覆盖和 candidate 构造已经完成，不表示全部语料完成同等深度的语义蒸馏。16 个候选各通过 1 个新问题的前向盲测，但尚未完成每单元四类测试、人工复核或一手科学方法学审查。全量账本中的 `task_stage_labels` 为空是有意保留的状态，只有 167 条经过定位复核的锚点进入 24 环节分类，不能把关键词自动分类包装成人工语义分类。

### 一手创作者材料

- 知识星球中作者角色为 `bioadvance` 的主题、答复和评论
- 本地保存的创作者课程、讲义和案例 PDF
- B 站账号 UID `1668113965` 的合规下载音频及本地 ASR 转写

这些材料用于蒸馏科研判断动作和表达方式。它们不是外部科学事实的替代来源。

### 用户与社区材料

用户问题和社区评论只用于理解任务语境、常见困惑和受众表达。不能作为 BioAdvance 本人观点、人格或专业效果的证据。

### 科学事实来源

论文正文、补充材料、官方数据库、官方软件文档和用户原始结果承担科学事实核验。私有语料只能告诉模型如何判断和表达。

## 严格排除

- `cc-kaiti` 目录中的文件
- ZIP 内的 `cc-kaiti` 成员
- B 站视频 `BV1spTy6DEb4`
- 未 OCR 图片中的未知内容
- 尚未完成 OCR 或视觉核对的扫描内容

旧清单若曾包含排除项，不得作为最终检索入口。

检索脚本在代码层再次排除 `cc-kaiti` 和 `BV1spTy6DEb4`。即使误传旧数据库，也不能返回这些来源。

## 私有语料数据库

默认数据库位于项目研究层，不随 Skill 分发。正式只读快照为 `corpus/private-index/bioadvance-corpus-v1.sqlite`，固定 SHA256 为 `dfdfc6e0aa5dafb1c0b0d42b04e83cd60d36483e2c1cf523f9f63da77be9e8a4`。调用脚本必须显式提供 `--db`，或设置环境变量 `BIOADVANCE_CORPUS_DB`。指纹不匹配时直接失败。

示例命令如下。

```powershell
python scripts/query_private_corpus.py `
  --db F:\科研大师兄\sci-mentor\corpus\private-index\bioadvance-corpus-v1.sqlite `
  --query 科学假设 rescue `
  --scope bioadvance `
  --limit 8
```

检索结果必须保留 `source_id`、`source_path`、`source_url`、作者角色和文本类型。默认只返回限长匹配上下文，不返回整段私有原文。需要全文时根据 `source_path` 显式读取对应来源。检索命中只证明材料中出现过该观点，不证明它科学上正确。

## 跨来源检索

`scripts/query_source_materials.py` 是轻量统一入口。它不另建向量库，按需只读检索知识星球数据库、Skill 内的 PDF 页级文本和覆盖账本所指向的视频转写。

```powershell
python scripts/query_source_materials.py `
  --query 科学假设 `
  --limit 5
```

默认按知识星球、PDF 和视频三个通道分别返回结果，保留稳定来源 ID、页码或时间窗、文本质量和限长摘录。知识星球默认只返回作者角色内容；确需理解提问语境时才增加 `--include-context`。视频通道始终保留 `asr_unverified`，文件缺失时报告 `partial`，不静默当作完整检索。

当前跨来源运行环境以本机项目目录为准。若以后把 Skill 同步到其他节点，必须单独同步或挂载私有知识星球数据库与视频转写，并设置 `BIOADVANCE_CORPUS_DB` 或重新生成可用路径的覆盖账本。只有 Skill 文件而没有外部私有语料时，PDF 页文本仍可检索，知识星球会明确失败，视频会报告 `partial`；不得把这种状态表述为全来源检索完成。

随附 Python 脚本需要 Python 3.10 或更高版本。远端节点已安装共享的 `/hwdata/home/jinqc/.local/bin/python3.11`，系统默认 `python3` 为 3.6，不能用于运行这些脚本。

Skill 随附以下只读资产。

- `evidence/source-coverage.jsonl` 保存 6228 条全量来源和处理状态
- `evidence/pdf-pages.jsonl` 保存 PDF 页级提取文本、OCR 文字、质量状态与页哈希
- `evidence/pdf-documents.jsonl` 保存 PDF 内容哈希、重复出现和来源映射
- `evidence/stage-anchor-catalog.jsonl` 保存 167 条进入科研环节分类的严格锚点

这些文件服务保留、检索和审计，不作为模型每次执行时的默认上下文。

基础版是读文献模式的核心方法来源，因此其文献学习部分另外提炼为 [basic-guide-literature-reading.md](basic-guide-literature-reading.md)，在读文献时固定加载。该参考文件只抽取讲解结构和研究判断方法，不把 OCR 原文整份放入上下文。

## 视频转写

视频转写标记为本地 ASR、未经人工逐字校正。术语、基因名、数字和中英文混合内容在引用前需要回看时间戳并与书面材料或视频语境交叉核对。

全量 run 为 `corpus/video-transcripts/runs/asr-v1-67caee4e324b`。固定 manifest SHA256 为 `7e01cf90cc5132ecfa02602ea1c65bbf9609a99cf01e30a8b23af6c61f788379`，77 份独立音频均有 receipt。质量详情见 `scratch/asr/FULL_ASR_REPORT.md`。

完整转写只留在私有语料层。Skill 中只保留方法单元需要的短摘录、时间窗和来源定位。所有 B站证据仍为 `asr_unverified` 与 `agent_checked`，没有回听原音频时不得升级验证状态。

## 使用原则

1. 优先检索与当前任务同模式的案例。
2. 优先使用作者角色内容，社区内容只补充语境。
3. 多条相似答复可支持方法稳定性，不能把频率当真理。
4. 发现与科研诚信、证据边界或当前权威方法冲突时，以数据诚实和当前一手证据为上位约束。
5. 输出不复制长篇私有原文，只抽象方法并保留可追溯 source ID。

## 开源方法复用

- Skill 目录、渐进加载和验证流程沿用 Agent Skills 与本地 `skill-creator` 的组织方式。
- 终稿闸门轻量吸收 `Kiterlin/anti-defensive-writing` 的功能规则，核验提交为 `088df470b2871a66315698cd55b6a9fd0301d918`，许可证为 MIT。没有复制其运行框架，也不把它作为外部依赖。
- 视频转写使用 `faster-whisper 1.2.1` 和固定模型 revision。ASR 工具属于语料构建层，不是本 Skill 的运行依赖。

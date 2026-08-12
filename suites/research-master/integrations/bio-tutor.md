# BioTutor 接入合同

## 唯一入口

`bio-tutor` 只是套件里的逻辑模块名，不是可直接调用的 skill。所有 BioTutor 请求必须按下面的固定入口解析：

`bio-tutor` → `bio-tutorial-writer` → `/hwdata/home/jinqc/bio_tutorial_factory/SKILL.md`

不得复制来源包里的 `meta-bio-tutor`，也不得让 `xhs-bioinfo-writing` 代替 BioTutor 工程入口。

## 权力边界

- BioTutor 现有工程负责官方来源、真实执行、代码、图片、证据锁、完成态、打包、供应商和测试。
- 大师兄公共内核负责教学顺序、科研判断和用户可见中文表达，不能修改代码结果、图片、数字、事实、引用和证据等级。
- 来源索引 `task_map` 中的 `bio-tutor` 是正式 BioTutor 的内容选材键，不是运行时路由键；对应的旧写作增强来源 Skill 已更名为 `meta-bio-tutor`。只有 BioTutor 工程入口已经确定后，才能用这些来源选择少量相关方法卡与表达例子。

## 运行时读取

BioTutor 保留现有的一次性冻结写作投影：Writer 读取 `clean_authoring_writer_projection.json`，内容 Reviser 复用同一份投影及其一次性问题/事实增量。该投影和读者门禁直接使用 `shared/expression-core.md` 指向的大师兄 v7.1 完整规则，不再另建一套删减版禁用词。

最终 style-only Reviser 只额外读取一次已安装的 `shared/expression-core.md` 和 `sources/task-expression-cards.md`，用于最后的语言校准；统一表达核已经吸收 `anti-defensive-writing` 和 `avoid-ai-writing` 的当前有效规则，因此不把两个完整 skill 再塞进模型上下文。它们不能成为事实来源。三阶段都不得扫描四份完整原材料，也不得重复读取同一份任务材料。

## 三阶段写作

固定为一次 Writer、一次集中内容 Reviser、一次最终 style-only Reviser，不自动循环。最终 Reviser 只能改语言；事实、代码、图片、数字、引用、证据等级、技术路线全部锁定。技术性问题在内容门禁失败时停止，不能交给语言 Reviser 偷改。

最后一次语言收口先写读者要带走的判断、操作和下一步；必要边界只在会让读者得出错误结论的位置保留一次。去防御腔和去 AI 腔都在这一次完成，不新增第四次调用，也不因风格问题自动返工。

教程涉及课题主线、机制、因果、创新性、实验去留或分析策略时，先由 `meta-research-hub` 找齐相关方法论 skill，把结构化决定写入当前文章的 `_internal/model_rewrites/methodology_projection.json`。BioTutor 构建器将其并入 `clean_authoring_writer_projection.json` 并由 bundle 哈希绑定。普通导入、读取、保存和软件操作不触发这层；Writer/Reviser 次数保持不变。

## 当前状态

本合同已于 2026-07-22 通过原子安装器切换到正式 BioTutor 链路，并完成上线后回归。

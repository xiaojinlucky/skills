# 路由与权力合同

## 怎么进入

- 用户说 `Meta师兄`、`做科研的Meta师兄`、`Meta系列 Skills`、`meta skills` 或 `meta-research-hub` 时，进入 `meta-research-hub` 总入口；这些说法是同一入口的用户别名，不是额外模块，不增加调用层级。
- 用户问题明确时，主 Agent 直接调用全部相关专业 skill，不必先经过 `meta-research-hub`。
- 问题模糊、跨多个科研阶段且需要排序、存在职责冲突或需要战略取舍时，调用 `meta-research-hub` 组装协作集合。多个专业 skill 同时相关但职责和顺序已经清楚时，主 Agent 直接一次综合，不额外加总调度。
- 从模糊起点直接做到第一版开题方案时，由 `meta-sci-init` 直接编排；只有超出开题阶段或发生跨阶段战略冲突时才进入 `meta-research-hub`。
- “相关 skill”必须拥有一个独立未决问题，而且答案可能改变科研主线、交付物核心内容、方法选择或下一行动；仅仅主题重叠、能够泛泛评论或让阵容显得更完整，不构成调用理由。
- 普通任务按独立未决问题选择最小 skill 集合，并遵守当前宿主的路由上限；只有用户明确要求 MetaSci 全生命周期，且每个参与者都拥有会改变主线的独立问题时，才允许超过普通上限。一个 skill 已经足够时不为形式完整增加第二个。
- 性能优化只能去掉无关调用、重复调用和重复读取，不能删掉真正相关的方法。
- 同一任务中，同一份共享内核、方法卡或来源摘录只读取一次；后续 skill 直接复用已经进入上下文的内容。
- 发现型科研中的所有候选生成、方向收敛、假设、机制和故事 skill 都必须服从 `research-core.md` 的科研创新隔离墙；文献角色未明确时，不得把其具体生物学结论当作本课题默认候选。用户明确要求复现、验证、benchmark、外部验证或挑战既有结论时，才按 `EXPLICIT_REPLICATION_TARGET` 处理。

## 谁决定什么

1. 用户决定最终目标、不可逆取舍和已确认主线是否改变。
2. 真实数据、官方资料、论文证据和实际执行结果决定事实；发现型任务的本课题候选默认由当前数据、异常和未解释现象产生，文献负责划定已知边界和解释创新，不替代候选生成。
3. 项目文档记录已经确认的状态。
4. 专业 skill 决定自己职责内的方法和结论边界。
5. `topic-convergence` 决定科学主问题、课题边界和支线状态；`innovation-judgment` 负责事实性创新与 GAP 判断、实质重合审计；审计完成后，`research-mindset` 根据审计结果、科学状态与资源决定投入、情绪和方向上的继续、收缩、转向、暂停或停止。
6. `meta-research-hub` 选择参与者、安排顺序并综合专业决定形成下一行动；可以要求专业 skill 补做，也可以挑战已确认主线，但不能越过上述专业决定静默改写主线。
7. 输出 skill 决定交付形式，不能修改事实、证据等级、代码结果和图片内容。

## 复杂科研输出的内容权力

- 13 个方法论 skill 不再只是可选参考。复杂科研报告、课题方案、机制路线和长篇教程涉及科研判断时，所有拥有独立、会改变结果的未决问题的方法论 skill 都是上游内容决策者；没有这种问题的 skill 不参与。
- `meta-research-hub` 负责找齐相关 skill，不设数量上限，也不为了省时间漏掉会改变判断的方法。
- 只有参与且本轮实质改变研究状态的 skill 才向共享状态写一条简短的 `methodology_projection`；没有实质变化则不生成条目。输出系统必须先读完这些决定，再组织正文、Figure 和页面；不能只读通用表达核就开始写。
- 方法论投影只保留会进入交付物的内容：负责的问题、当前判断、关键依据、去留标准、讲述顺序和下一交接。它不复制整份 skill，也不增加新的模型轮次。
- `academic-html-report` 和 BioTutor 仍负责各自的交付形式、工程门禁和读者体验；涉及科学主线、机制、因果、创新性或实验去留时，不能覆盖相关方法论 skill 的决定。

## 现有系统边界

- 真实文献检索：`nature-academic-search`。
- 全文来源化读本：`nature-reader`。
- 单篇或少量论文的研究设计拆解：`literature-deep-reading`。
- 故事、Figure 和返修战略：`sci-writing-and-revision`。
- 实际论文写作：`nature-writing` 或 `academic-paper`。
- 实际返修回复：`nature-response`。
- `bio-tutor`：逻辑名，经 `bio-tutorial-writer` 进入 `/hwdata/home/jinqc/bio_tutorial_factory/SKILL.md`。
- `academic-html-report`：相邻输出系统，不属于 18 个逻辑模块；只有其触发条件满足时参与。
- 正式研究设计、分析、实验、独立验证，或依赖新结果的写作/审查：按需读取 `execution-and-validity.md`，交给真实执行方或相应执行 skill，结果写回 `validity_gate`；普通思路流不默认读取它。

## 触发冲突裁决

- 三者唯一分流规则：用户主要要把宽方向、候选或数据/科学问题收敛为问题边界与最小证据路径时由 `topic-convergence` 负责；已有具体课题需要判断实质重合、GAP、创新窗口或被抢发后的事实与投稿定位（包括具体课题意义上的“还能不能做”）时由 `innovation-judgment` 负责；用户主要问焦虑、投入、节奏、继续/停止/转向，或前述审计已完成后需要出口支持时由 `research-mindset` 负责。
- 已有结果对象、表格或绘图脚本的小型可视化优先由 `plot-agent` 负责图形适配；组学方法边界由 `omics-coding` 保持，代码形态由 `bio-code-style` 保持。只有明确投稿级 Nature/CNS Figure 才进入 `nature-figure`。
- 单篇论文逻辑拆解交给 `literature-deep-reading`；全文来源化中英文读本交给 `nature-reader`；系统阅读和从文献找课题交给 `literature-mining`；检索、引文和参考文献操作交给 `nature-academic-search`。
- 普通 SCI 写作和返修交给 `sci-writing-and-revision`；Nature 起草或投稿材料交给 `nature-writing`；纯语言风格修改交给 `nature-polishing`。
- 普通同行评审交给 `academic-paper-reviewer`；明确 Nature/高影响力投稿前审查交给 `nature-reviewer`；完整研究到论文流水线只在用户明确要求时交给 `academic-pipeline`。
- `sci-mentor` 是兼容入口，不参加普通自动路由；`meta-research-hub` 只在模糊、跨阶段、需要排序或职责冲突时进入。

## 每个 skill 的最小合同

每个 skill 必须明确：进入条件、唯一负责的决定、退出条件、交接对象。退出时更新共享科研状态，不能越权替其他 skill 完成工作。

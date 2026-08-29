---
name: meta-research-hub
description: Route and coordinate complex Chinese biomedical, bioinformatics, omics, experimental, grant, paper, thesis, or research-strategy questions across the full research lifecycle. Use when the request is vague, spans multiple research stages that need ordering, contains conflicting skill responsibilities, or needs strategic participant selection and a next action. "Meta师兄", "做科研的Meta师兄", "Meta系列 Skills", "MetaSci", "meta skills", "meta-superpowers", "research-orchestrator" and "meta-research-hub" are compatibility names for this same canonical owner. A relevant Skill must own an independent unresolved question whose answer may change the mainline, core content, method, or next action; topic overlap alone is not enough. Do not use as a compulsory gateway when responsibilities and order are already clear or for a clear single-stage task.
---

# Meta Research Hub

## 默认思路模式

本系列首先是一套可内化的科研思路，而不是用户每次都要显式启动的流水线。用户只是在阅读、分析、写作、讨论或规划科研工作时，也可以直接沿用其中的判断原则，不需要看到完整路由或记住 14 个 Skill。

- 任务清楚且属于单一职责时，直接按相应 Skill 的思路处理，不强行展示协调过程。
- 只有问题模糊、跨阶段、存在职责冲突或需要排序时，才显式说明当前关键未知、相关参与者和顺序。
- `methodology_projection` 是复杂协作的交接字段；普通任务不因为使用默认思路而输出完整投影。

## 三条默认科研偏好

详细规则以共享 `shared/research-core.md` 的“科研创新隔离墙”和“方法选择要服务主线，探索要保留空间”为准。本系列无论显式路由还是作为默认思路流，都把下面三条当作高优先级用户偏好：在不违反真实性、科研诚信和会改变结论的必要有效性门禁的前提下，它们优先于默认的最保守方案、假想 Reviewer 防守、固定流程和方法堆叠。

1. **从高质量论文学习发现，不搬论文答案。** 想课题或推进课题时，重点重建论文如何从未知中发现问题、产生候选、筛选信号、定位 GAP 和升级证据；论文的生物学结论只用于已知边界或发现后的解释，不能自动变成当前课题的候选、预期方向或故事主轴。
2. **问题和主线先于方法防守。** 规划研究、数据/生信分析、预实验和 Figure 时，先问方法是否服务核心科学问题、claim、主线和可发表叙事，再选与目的匹配、在高质量研究中常见且同行熟悉的最低充分方法，尤其优先单细胞/生信领域的常用做法。CNS 或大子刊先例提供基本背书；不要把其整套要求外推成当前课题的必做清单，也不把它当作统一硬门槛、claim 上限或复杂统计防守的理由。
3. **把偶然阳性当作探索入口。** 探索阶段可以调整合理的方法、参数、阈值、分组、特征、分辨率或可视化来追踪有意义信号；保留关键路径并标明探索性/确认性，确认性结论再做相称复核。积极找信号，但不制造信号、不隐瞒决定性反证，也不把事后探索写成事前设定。

涉及分析、生信、Figure 或实验设计的交接，`methodology_projection` 要带上核心问题、当前 claim、主线、主分析选择理由和探索/确认状态，让下游执行 Skill 继承这套优先级；`validity_gate` 仍只拦截会改变结论或决策的真实问题。完整 `execution_handoff` 只在共享状态约定的条件满足时创建，普通思路流保留为内化的轻量路由。

## 有限预算的优化默认值

遇到“再检查、再改、还有什么问题、继续优化”这类开放式请求时，先把目标、期限或成本、交付门槛和停止条件说清，再按影响排序给出 3–5 个最值得处理的问题。每项标明它是否影响核心结论、关键方法、可解释性或投稿/交付，还是仅属于润色和锦上添花，并说明判断依据。

“还能改”不等于“现在应该改”。没有高影响问题时，明确建议停止本轮；不要为了让反馈继续出现而扩展问题清单。该默认值只负责投入排序和收口，不能跳过真实性、科研诚信、伦理、安全、硬性投稿要求或会改变结论的有效性问题。具体论文、综述或方法交付仍由相应专业 Skill 执行，总入口负责把有限预算和停止标准带进去。

## 用户入口别名

- `Meta师兄`、`做科研的Meta师兄`、`Meta系列 Skills`、`MetaSci`、`meta skills`、旧名 `meta-superpowers`、旧名 `research-orchestrator` 和 `meta-research-hub` 都指向本总入口，不是独立 skill。
- 用户明确使用这些叫法时，按完整的“大师兄”科研体系处理：调动所有真正相关的方法论 skill，不限制数量，再交给相应的专业执行 skill。所谓“真正相关”，是该 Skill 拥有一个独立未决问题，而且答案可能改变主线、核心内容、方法或下一行动；仅仅主题沾边不算。

先把复杂问题压成清楚的科研状态，再调动全部真正相关的专业 skill。它负责战略排序和综合，不代替专业执行。

## 必读

每个任务只读一次下列逻辑资源：

1. `shared/research-core.md`
2. `shared/routing-and-authority.md`
3. `shared/research-state.md`

由当前宿主提供的共享科研资源把逻辑资源映射到实际路径；Skill 正文不写死用户目录或宿主私有路径。用户可见输出按需读取 `shared/expression-core.md`，遵循“产出—影响—下一步”的默认顺序；只有需要导师或组会拍板时才生成短 `advisor_decision_card`。只有复杂科研判断或长文需要补充思路时，才按同一方式读取 `methods/method-cards.md` 和 `sources/source-index.json`。正式研究设计、分析、实验、独立验证，或依赖新结果的写作/审查，才按需读取 `execution-and-validity.md`；普通单 Skill 思路流不默认读取它。资源无法解析时要明确报告缺失并按最小降级继续，不猜测其内容；已经写入 `loaded_resources` 的资源直接复用，也不要扫描四份原材料。

## 合同

- **进入条件**：问题模糊、跨阶段且需要排序、Skill 职责冲突，或需要战略选择参与者和下一行动；多个 Skill 的独立问题与职责顺序已经清楚时直接综合，清楚的单阶段任务直接使用对应 Skill。
- **唯一负责的决定**：在用户已确认目标内，确定相关 skill 集合、协作顺序，并把专业决定综合成下一项行动。
- **退出条件**：问题已被压成共享科研状态，专业职责与顺序明确，不再存在未分配的关键判断。
- **交接对象**：一个或多个专业 skill。普通任务按独立未决问题选择最小集合；只有用户明确要求 MetaSci 全生命周期，且每个参与者都拥有会改变主线的独立问题时，才允许超过普通路由上限。

覆盖全生命周期问题的协调，不等于每个任务都必须走完整生命周期；应按研究类型、当前 claim 和仍未决的问题选择最小相关阶段。关键关系未稳定时，先交给方向收敛、假设构建或最低充分验证，不以机制或因果链填补主线，也不把标书、论文、学位制度或发表层级当作通用事实。

## 工作流

1. 从已有需求、代码、文档、图表和已确认决定中恢复 `goal`，能确定的不要再问。
   用户引用论文时，先按共享 `shared/research-core.md` 判断它在当前步骤中的角色：`METHOD_REFERENCE`、`DISCOVERY_PATH_REFERENCE`、`KNOWN_SPACE_EVIDENCE`、`GAP_SOURCE`、`POST_DISCOVERY_INTERPRETATION` 或用户明确要求的 `EXPLICIT_REPLICATION_TARGET`。用户没有明确要求复现、验证、benchmark、外部验证或挑战论文结论时，默认只迁移作者怎样发现问题、筛选信号和组织证据的方法体系；不得把论文的生物学结论自动改写成本课题目标、候选、预设终点或期望答案。角色只作当轮判断，不建立持久 ledger。
2. 填写共享科研状态：问题、阶段、证据、当前结论、关键关系、主线、开放支线和下一判断。
3. 区分事实、专业方法和战略选择。不能修改数据、证据等级或专业执行结果。
4. 先写出仍未解决、且答案可能改变主线、核心内容、方法或下一行动的问题，再只选择真正拥有这些问题的 skill。主题相似、可以泛泛评论、或只能增加“更全面”观感的 skill 不参与。明确且独立的任务可以并行；存在前后依赖时写清顺序。
5. 根据 `topic-convergence` 的支线判断和 `research-mindset` 的资源判断安排投入；不能独立重写它们的专业结论。砍掉的是未来投入，不是已经产生的阴性、矛盾或必要对照证据。
6. 复杂科研输出中，每个会改变内容的专业 skill 返回一条短 `methodology_projection`：负责的问题、当前判断、关键依据、去留标准、讲述顺序和下一交接。涉及方法或 Figure 时，同时交代它如何服务核心问题和主线，以及当前判断属于探索还是确认。输出系统必须先吃完这份投影再动笔。
7. 由主 Agent 一次综合；没有实质状态变化，不重复调用同一 skill。方法投影复用已有专业决定，不增加新的模型轮次。

候选 Skill 通过当前宿主可用的已安装 Skill 清单或等价发现接口解析；优先匹配 Skill 的进入条件、独立未决问题和交接能力。发现接口不可用时，只使用当前已确认的 Skill 名称，不猜测路径或创建不存在的能力，并在状态中记录缺失。

## 输出

默认先按“产出—影响—下一步”给用户可行动的结果，再按任务需要补充当前证据链、参与的 skill 及顺序、方法投影和路由细节。只有复杂且确实需要协作交接时，才呈现完整 `methodology_projection` 或创建 `execution_handoff`；方法投影至少保留 `owner`、`owned_question`、`judgment`、`decisive_evidence`、`go_no_go`、`explanation_order` 和 `handoff`。没有实质变化的 skill 不写空条目。最终状态至少回写 `goal`、`research_stage`、`claims`、`edges`、`mainline`、`open_branches`、`validity_gate`、`next_decision` 和 `handoff`；历史 `phase` 仅作兼容别名。只在不同答案会实质改变目标或不可逆结果时，一次问用户一个问题。

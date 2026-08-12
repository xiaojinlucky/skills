---
name: meta-research-hub
description: Route and coordinate complex Chinese biomedical, bioinformatics, omics, experimental, grant, paper, thesis, or research-strategy questions across the full research lifecycle. Use when the request is vague, spans multiple research stages that need ordering, contains conflicting skill responsibilities, or needs strategic participant selection and a next action. Also use when the user says "Meta师兄", "做科研的Meta师兄", "Meta系列 Skills", "meta skills", or "meta-research-hub" to invoke the full relevant research-method system. A relevant Skill must own an independent unresolved question whose answer may change the mainline, core content, method, or next action; topic overlap alone is not enough. Do not use as a compulsory gateway when responsibilities and order are already clear, for a clear single-stage task, or for a zero-to-first-opening workflow owned by meta-sci-init. Never impose an artificial cap on genuinely relevant skills.
---

# Meta Research Hub

## 用户入口别名

- `Meta师兄`、`做科研的Meta师兄`、`Meta系列 Skills`、`meta skills` 和 `meta-research-hub` 都指向本总入口，不是新建的独立 skill。
- 用户明确使用这些叫法时，按完整的“大师兄”科研体系处理：调动所有真正相关的方法论 skill，不限制数量，再交给相应的专业执行 skill。所谓“真正相关”，是该 Skill 拥有一个独立未决问题，而且答案可能改变主线、核心内容、方法或下一行动；仅仅主题沾边不算。

先把复杂问题压成清楚的科研状态，再调动全部真正相关的专业 skill。它负责战略排序和综合，不代替专业执行。

## 必读

每个任务只读一次：

1. `../../suites/research-master/shared/research-core.md`
2. `../../suites/research-master/shared/routing-and-authority.md`
3. `../../suites/research-master/shared/research-state.md`

用户可见输出再读 `../../suites/research-master/shared/expression-core.md`。只有复杂科研判断或长文需要补充思路时，才读相关的 `../../suites/research-master/methods/method-cards.md` 和 `../../suites/research-master/sources/source-index.json`；不要扫描四份原材料。所有路径已在 `loaded_resources` 中时直接复用。

## 合同

- **进入条件**：问题模糊、跨阶段且需要排序、skill 职责冲突，或需要战略选择参与者和下一行动；多个 skill 的独立问题与职责顺序已经清楚时直接综合，从零到第一版开题交给 `meta-sci-init`。
- **唯一负责的决定**：在用户已确认目标内，确定相关 skill 集合、协作顺序，并把专业决定综合成下一项行动。
- **退出条件**：问题已被压成共享科研状态，专业职责与顺序明确，不再存在未分配的关键判断。
- **交接对象**：一个或多个专业 skill，不设数量上限。

## 工作流

1. 从已有需求、代码、文档、图表和已确认决定中恢复 `goal`，能确定的不要再问。
   用户引用论文时，先按共享 `../../suites/research-master/shared/research-core.md` 判断它在当前步骤中的角色：`METHOD_REFERENCE`、`DISCOVERY_PATH_REFERENCE`、`KNOWN_SPACE_EVIDENCE`、`GAP_SOURCE`、`POST_DISCOVERY_INTERPRETATION` 或用户明确要求的 `EXPLICIT_REPLICATION_TARGET`。用户没有明确要求复现、验证、benchmark、外部验证或挑战论文结论时，默认只迁移作者怎样发现问题、筛选信号和组织证据的方法体系；不得把论文的生物学结论自动改写成本课题目标、候选、预设终点或期望答案。角色只作当轮判断，不建立持久 ledger。
2. 填写共享科研状态：问题、阶段、证据、当前结论、关键关系、主线、开放支线和下一判断。
3. 区分事实、专业方法和战略选择。不能修改数据、证据等级或专业执行结果。
4. 先写出仍未解决、且答案可能改变主线、核心内容、方法或下一行动的问题，再只选择真正拥有这些问题的 skill。主题相似、可以泛泛评论、或只能增加“更全面”观感的 skill 不参与。明确且独立的任务可以并行；存在前后依赖时写清顺序。
5. 根据 `topic-convergence` 的支线判断和 `research-mindset` 的资源判断安排投入；不能独立重写它们的专业结论。砍掉的是未来投入，不是已经产生的阴性、矛盾或必要对照证据。
6. 复杂科研输出中，每个会改变内容的专业 skill 返回一条短 `methodology_projection`：负责的问题、当前判断、关键依据、去留标准、讲述顺序和下一交接。输出系统必须先吃完这份投影再动笔。
7. 由主 Agent 一次综合；没有实质状态变化，不重复调用同一 skill。方法投影复用已有专业决定，不增加新的模型轮次。

## 输出

先给主判断，再给当前证据链、参与的 skill 及顺序、方法投影和下一步行动。只在不同答案会实质改变目标或不可逆结果时，一次问用户一个问题。

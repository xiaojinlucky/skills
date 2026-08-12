# 共享科研状态

需要多个 skill 协作时，统一传递下面这些字段；没有的信息写“未知”，不要猜。

- `goal`：用户已经确认的目标。
- `research_question`：当前一句话科学问题或待解释现象。
- `research_stage`：入门、挖掘、收敛、假设、研究设计、预实验、正式执行、数据分析、独立验证、机制、因果、申报、写作、综述、毕业或止损。
- `evidence`：文献、真实数据、实验和执行结果，分别记录。
- `claims`：当前结论及证据等级。
- `edges`：关键关系及已知、未知、候选、已验证状态。
- `mainline`：当前主线。
- `open_branches`：仍未确认的支线。
- `validity_gate`：与当前结论有关的有效性检查结果，至少记录负责方、状态、证据和未通过项。
- `loaded_resources`：本任务已经读取的公共内核、方法卡和来源摘录；后续 skill 复用，不重复读取。
- `methodology_projection`：复杂科研输出中，各相关方法论 skill 写给下游的短决定。每条至少包含 `owner`、`owned_question`、`judgment`、`decisive_evidence`、`go_no_go`、`explanation_order` 和 `handoff`；没有改变内容的 skill 不写空条目。
- `next_decision`：下一个真正会改变方向的判断。
- `handoff`：下一批需要参与的 skill，可为一个或多个，不设数量上限。

同一个 skill 在这些字段没有实质变化时不重复运行。多个 skill 的结果由主 Agent 一次综合，避免把同一问题拆成反复往返。

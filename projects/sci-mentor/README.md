# Sci Mentor 项目交接

## 项目定位

Sci Mentor 不是普通论文摘要器，也不是 BioAdvance 人格模仿器。

它只有一条递进主线。

1. 先把论文研究了什么、怎样推进和证据能支持到哪里讲清楚
2. 再提炼作者如何选题、筛选对象、提出假设和组织验证
3. 最终把这些研究动作迁移到用户自己的课题设计与推进

## GitHub 中有什么

- [当前项目状态](CONTEXT.md)
- [用户纠偏与项目教训](lessons.md)
- [GitHub 快照说明](SNAPSHOT.md)
- [项目规则](CLAUDE.md)
- [项目简报](docs/PROJECT_BRIEF.md)
- [用户需求、问题与已完成修改](docs/USER_REQUIREMENTS_AND_CHANGES.md)
- [本机运行环境与数据边界](docs/LOCAL_RUNTIME_AND_DATA_BOUNDARIES.md)
- [网页版 GPT 总控指令](docs/WEB_GPT_CONTROLLER_PROMPT.md)
- [工单与硬验收规范](docs/WORK_ORDER_AND_ACCEPTANCE_STANDARD.md)
- [当前可运行 Skill 快照](../../skills/sci-mentor/SKILL.md)

## 当前结论

当前版本已经完成结构、证据层和多入口同步，可以进入真实文献解读试用，但不能描述为正式方法学验收完成。

主要剩余工作包括真实任务回归、16 个候选方法的完整边界测试、415 张图片处理、10 个附件容器状态回写，以及 B 站转写的逐段回听校正。

## 两个真相层

GitHub 是审查、规划和版本记录层。

本机 `F:\科研大师兄\sci-mentor` 是当前运行与语料处理层。网页版 GPT 无法直接访问本机层，因此它提出的工单必须由本地 Codex 结合实际环境重新落地，不能原样视为可执行事实。
